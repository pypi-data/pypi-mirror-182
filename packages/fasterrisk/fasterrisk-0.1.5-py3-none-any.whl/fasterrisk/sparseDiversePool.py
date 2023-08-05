import numpy as np
import sys
# import warnings
# warnings.filterwarnings("ignore")
from fasterrisk.utils import get_support_indices, get_nonsupport_indices, compute_logisticLoss_from_ExpyXB
from fasterrisk.base_model import logRegModel

class sparseDiversePoolLogRegModel(logRegModel):
    def __init__(self, X, y, lambda2=1e-8, intercept=True, original_lb=-5, original_ub=5):
        super().__init__(X=X, y=y, lambda2=lambda2, intercept=intercept, original_lb=original_lb, original_ub=original_ub)
   
    def get_sparseDiversePool(self, gap_tolerance=0.05, select_top_m=10, maxAttempts=50):
        """For the current sparse solution, get from the sparse diverse pool [select_top_m] solutions, which perform equally well as the current sparse solution. This sparse diverse pool is also called the Rashomon set. We discover new solutions by swapping 1 feature in the support of the current sparse solution.

        Parameters
        ----------
        gap_tolerance : float, optional
            New solution is accepted after swapping features if the new loss is within the [gap_tolerance] of the old loss, by default 0.05
        select_top_m : int, optional
            We select the top [select_top_m] solutions from support_size*maxAttempts number of new solutions, by default 10
        maxAttempts : int, optional
            We try to swap each feature in the support with [maxAttempts] of new features, by default 50

        Returns
        -------
        intercept_array : ndarray
            (1D array with `float` type) Return the intercept array with shape = (select_top_m, )
        coefficients_array : ndarray
            (2D array with `float` type) Return the coefficients array with shape = (select_top_m, p)
        """
        # select top m solutions with the lowest logistic losses
        # Note Bene: loss comparison here does not include logistic loss
        nonzero_indices = get_support_indices(self.betas)
        zero_indices = get_nonsupport_indices(self.betas)

        num_support = len(nonzero_indices)
        num_nonsupport = len(zero_indices)

        maxAttempts = min(maxAttempts, num_nonsupport)
        max_num_new_js = maxAttempts

        total_solutions = 1 + num_support * maxAttempts
        sparseDiversePool_betas = np.zeros((total_solutions, self.p))
        sparseDiversePool_betas[:, nonzero_indices] = self.betas[nonzero_indices]

        sparseDiversePool_beta0 = self.beta0 * np.ones((total_solutions, ))
        sparseDiversePool_ExpyXB = np.zeros((total_solutions, self.n))
        sparseDiversePool_loss = 1e12 * np.ones((total_solutions, ))

        sparseDiversePool_ExpyXB[-1] = self.ExpyXB
        sparseDiversePool_loss[-1] = compute_logisticLoss_from_ExpyXB(self.ExpyXB) + self.lambda2 * self.betas[nonzero_indices].dot(self.betas[nonzero_indices])

        betas_squareSum = self.betas[nonzero_indices].dot(self.betas[nonzero_indices])
        for num_old_j, old_j in enumerate(nonzero_indices):
            # pick $maxAttempt$ number of features that can replace old_j
            sparseDiversePool_start = num_old_j * maxAttempts
            sparseDiversePool_end = (1 + num_old_j) * maxAttempts

            sparseDiversePool_ExpyXB[sparseDiversePool_start:sparseDiversePool_end] = self.ExpyXB * np.exp(-self.yXT[old_j] * self.betas[old_j])

            sparseDiversePool_betas[sparseDiversePool_start:sparseDiversePool_end, old_j] = 0
            
            betas_no_old_j_squareSum = betas_squareSum - self.betas[old_j]**2

            grad_on_nonsupport = -self.yXT[zero_indices].dot(np.reciprocal(1+sparseDiversePool_ExpyXB[sparseDiversePool_start]))
            abs_grad_on_nonsupport = np.abs(grad_on_nonsupport)

            # new_js = np.argpartition(abs_full_grad, -max_num_new_js)[-max_num_new_js:]
            new_js = zero_indices[np.argsort(-abs_grad_on_nonsupport)[:max_num_new_js]]

            for num_new_j, new_j in enumerate(new_js):
                sparseDiversePool_index = sparseDiversePool_start + num_new_j
                for _ in range(10):
                    self.optimize_1step_at_coord(sparseDiversePool_ExpyXB[sparseDiversePool_index], sparseDiversePool_betas[sparseDiversePool_index], self.yXT[new_j, :], new_j)
                
                loss_sparseDiversePool_index = compute_logisticLoss_from_ExpyXB(sparseDiversePool_ExpyXB[sparseDiversePool_index]) + self.lambda2 * (betas_no_old_j_squareSum + sparseDiversePool_betas[sparseDiversePool_index, new_j] ** 2)

                if (loss_sparseDiversePool_index - sparseDiversePool_loss[-1]) / sparseDiversePool_loss[-1] < gap_tolerance:
                    sparseDiversePool_ExpyXB[sparseDiversePool_index], sparseDiversePool_beta0[sparseDiversePool_index], sparseDiversePool_betas[sparseDiversePool_index] = self.finetune_on_current_support(sparseDiversePool_ExpyXB[sparseDiversePool_index], sparseDiversePool_beta0[sparseDiversePool_index], sparseDiversePool_betas[sparseDiversePool_index])

                    sparseDiversePool_loss[sparseDiversePool_index] = compute_logisticLoss_from_ExpyXB(sparseDiversePool_ExpyXB[sparseDiversePool_index]) + self.lambda2 * (betas_no_old_j_squareSum + sparseDiversePool_betas[sparseDiversePool_index, new_j] ** 2)

        selected_sparseDiversePool_indices = np.argsort(sparseDiversePool_loss)[:select_top_m]

        top_m_original_betas = np.zeros((len(selected_sparseDiversePool_indices), self.p))
        top_m_original_betas[:, self.scaled_feature_indices] = sparseDiversePool_betas[selected_sparseDiversePool_indices][:, self.scaled_feature_indices] / self.X_norm[self.scaled_feature_indices]
        top_m_original_beta0 = sparseDiversePool_beta0[selected_sparseDiversePool_indices] - top_m_original_betas.dot(self.X_mean)

        return top_m_original_beta0, top_m_original_betas

        original_sparseDiversePool_solution[1:] = sparseDiversePool_betas[selected_sparseDiversePool_indices].T
        original_sparseDiversePool_solution[1+self.scaled_feature_indices] /= self.X_norm[self.scaled_feature_indices].reshape(-1, 1)

        original_sparseDiversePool_solution[0] = sparseDiversePool_beta0[selected_sparseDiversePool_indices]
        original_sparseDiversePool_solution[0] -= self.X_mean.T @ original_sparseDiversePool_solution[1:]
        
        return original_sparseDiversePool_solution # (1+p, m) m is the number of solutions in the pool