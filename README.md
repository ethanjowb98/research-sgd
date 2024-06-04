# Stochastic Gradient Descent (SGD) with Mini-batching

**SGD (Stochastic Gradient Descent)** is an optimization algorithm commonly used for training models in machine learning, particularly for neural networks. It iteratively updates the model's parameters (weights and biases) to minimize a loss function that represents the model's error.

**Challenges with Batch Gradient Descent:**
- **Computational Cost:** When dealing with large datasets, calculating the gradient using the entire dataset (batch) for each update can be computationally expensive.
- **Noise Sensitivity:** The gradient calculated with the entire dataset can be noisy, leading to slow convergence or getting stuck in local minima.

**Mini-batch SGD addresses these challenges by:**

- **Processing data in smaller chunks (mini-batches) instead of the entire dataset.** This reduces computational cost per iteration.
- **Averaging the gradients calculated on each mini-batch.** This reduces noise and helps the model converge smoother.

**Implementation with Keras and Additional Features:**

Here's a complete implementation of traffic prediction using Keras with SGD mini-batching, TensorBoard visualization, and model saving/loading:
