# Reinforcement Learning

![Image](../../images/rl-01.png)

The model learns by `interacting with an environment` through a system of trial and error

<br/>

![Image](../../images/rl-03.png)

Terminology
![Image](../../images/rl-04.png)

![Image](../../images/rl-05.png)

<br/>

**RL Loop**:

![Image](../../images/rl-02.png)

<br/>

**Mechanism**:
It receives positive rewards for correct moves and penalties for mistakes. It aims to maximize its overall cumulative reward.

**Example**:
Training autonomous self-driving cars or teaching AI agents how to master chess and video games.

**Common Algorithms**:

- [Q-Learning](../rl/ql.md)
- [Deep Q-Networks (DQN)]() 
- [Actor-Critic]()

![Image](../../images/rl-12.png)

---

| Reinforcement Learning Method | Core Strategy | Core Objective | Key Algorithms | Best Applied To |
| :--- | :--- | :--- | :--- | :--- |
| **Model-Free (Value-Based)** | Estimates the long-term expected reward for every possible action. | Find the highest-paying choice. | • Q-Learning<br>• DQN (Deep Q-Network)<br>• SARSA | Environments with distinct, countable choices (e.g., retro video games, grid navigation). |
| **Model-Free (Policy-Based)** | Directly optimizes the action probabilities without scoring choices first. | Master the optimal behavior rulebook. | • Policy Gradient<br>• REINFORCE | Environments with fluid, continuous actions (e.g., robotic joints, autonomous steering). |
| **Model-Free (Actor-Critic Hybrid)**| Merges both worlds: one network acts, while the other network critiques the action. | Balance learning stability and speed. | • PPO (Proximal Policy Optimization)<br>• A2C / A3C<br>• TRPO | High-stakes, complex optimization problems (e.g., aligning Large Language Models via RLHF). |
| **Model-Based** | Builds an internal mental simulation to predict environmental changes. | Plan ahead by forecasting outcomes. | • AlphaZero / MuZero<br>• Dyna-Q<br>• MBPO | Complex strategy tasks where real-world mistakes are too costly (e.g., Chess, Go, industrial automation). |

<br/>

## How Works

Reinforcement Learning works on `Markov Decision Process`

![Image](../../images/rl-06.png)

Mainly should identify `Action`, `State` and `Reward`

![Image](../../images/rl-11.png)

<br/>