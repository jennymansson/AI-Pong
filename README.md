# Pong Game with NEAT

This Pong game is powered by the NEAT (NeuroEvolution of Augmenting Topologies) library, a Python framework for evolving neural networks. NEAT enables the creation of intelligent agents through an evolutionary process, where neural network architectures are evolved over generations.
Welcome to Pong, a classic arcade game with a twist! This version features an AI opponent powered by the NEAT (NeuroEvolution of Augmenting Topologies) library. Challenge yourself against an intelligent adversary that evolves and improves over time.

## Table of Contents
- [Overview](#overview)
- [NEAT Library](#NEATLibrary)
- [Features](#features)
- [Getting Started](#getting-started)
- [Training the AI](#training)

## Overview

This Pong game integrates the NEAT library, which stands for NeuroEvolution of Augmenting Topologies. NEAT is a Python library that facilitates the evolution of neural networks, allowing them to grow in complexity over generations. In this game, the AI opponent evolves through a process inspired by natural evolution, becoming a challenging opponent.

## NEAT Library

NEAT is a powerful Python library for evolving neural networks. Unlike manually designing architectures, NEAT starts with simple networks and evolves them over generations, resulting in intelligent agents capable of complex behaviors.

## Features

- AI Opponent: Experience Pong with an AI opponent trained using NEAT.
- Dynamic Evolution: The AI evolves over generations, adapting and improving its gameplay.

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/jennymansson/AI-Pong.git
```

2. Install the necessary dependencies by running:
```bash
pip install -r requirements.txt
```

3. Run the game:
```
python main.py
```

## Training the AI 
If you want to further train the AI using NEAT, follow these steps:

1. Uncomment the line in main.py to create a new NEAT population:
```bash
# p = neat.Population(config)
```
2. Comment out the line restoring a checkpoint:
```bash
p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-22')
```
3. Uncomment the line in main.py to run NEAT training:
```bash
# run_neat(config)
```
4. Comment the line in main.pyto test AI against player
```bash
test_ai(config) # AI is playing against you
```




