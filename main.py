import pygame
from pong import Game
import neat
import os
import pickle
"""
PongGame class represents the game environment for training and testing AI agents in the Pong game.

Attributes:
    - game: An instance of the Game class representing the Pong game environment.
    - left_paddle: The left paddle in the game.
    - right_paddle: The right paddle in the game.
    - ball: The ball object in the game.

Methods:
    - test_ai(genome, config): Test the given AI genome using player controls for comparison.
    - train_ai(genome1, genome2, config): Train two AI genomes against each other.
    - calculate_fitness(genome1, genome2, game_info): Calculate fitness based on hits for both AI genomes.
"""
class PongGame:
    def __init__(self, window, width, height):
        # Initialize PongGame with a game instance and access to paddles and ball
        self.game = Game(window, width, height)
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball

    def test_ai(self, genome, config):
        """
        Test the given AI genome using player controls for comparison.

        :param genome: NEAT genome representing the AI agent.
        :param config: NEAT configuration for the neural network.

        This function allows the player to control one paddle while the AI controls the other.
        The AI's decision-making process is based on the provided genome and neural network configuration.

        :return: None
        """
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            # Player controls for comparison
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_paddle(left=True, up=True)
            if keys[pygame.K_s]:
                self.game.move_paddle(left=True, up=False)

            # AI decision making
            output = net.activate(
                (self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            decision = output.index(max(output))

            # AI actions based on decision
            if decision == 0:
                pass
            elif decision == 1:
                self.game.move_paddle(left=False, up=True)
            else:
                self.game.move_paddle(left=False, up=False)

            # Game loop and display update
            game_info = self.game.loop()
            self.game.draw(True, False)
            pygame.display.update()

        pygame.quit()

    def train_ai(self, genome1, genome2, config):
        """
        Train two AI genomes against each other.

        :param genome1: NEAT genome representing the first AI agent.
        :param genome2: NEAT genome representing the second AI agent.
        :param config: NEAT configuration for the neural networks.

        This function simulates a game between two AI agents, updating their fitness based on the game outcome.

        :return: None
        """
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # AI 1 decision making and actions
            output1 = net1.activate((self.left_paddle.y, self.ball.y, abs(self.left_paddle.x - self.ball.x)))
            decision1 = output1.index(max(output1))

            if decision1 == 0:
                pass
            elif decision1 == 1:
                self.game.move_paddle(left=True, up=True)
            else:
                self.game.move_paddle(left=True, up=False)

            # AI 2 decision making and actions
            output2 = net2.activate(
                (self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            decision2 = output2.index(max(output2))

            if decision2 == 0:
                pass
            elif decision2 == 1:
                self.game.move_paddle(left=False, up=True)
            else:
                self.game.move_paddle(left=False, up=False)

            # Game loop, display update, and fitness calculation
            game_info = self.game.loop()
            self.game.draw(draw_score=False, draw_hits=True)
            pygame.display.update()

            # Exit condition and fitness calculation
            if game_info.left_score >= 1 or game_info.right_score >= 1 or game_info.left_hits > 50:
                self.calculate_fitness(genome1, genome2, game_info)
                break

    def calculate_fitness(self, genome1, genome2, game_info):
        """
        Calculate fitness based on hits for both AI genomes.

        :param genome1: NEAT genome representing the first AI agent.
        :param genome2: NEAT genome representing the second AI agent.
        :param game_info: Information about the game, including hit counts.

        This function updates the fitness scores of the provided genomes based on the game performance.

        :return: None
        """
        genome1.fitness += game_info.left_hits
        genome2.fitness += game_info.right_hits

def eval_genomes(genomes, config):
    """
    Evaluate genomes using the provided configuration.

    :param genomes: List of genomes to be evaluated.
    :param config: NEAT configuration for the neural networks.

    This function sets up a Pygame window and simulates games between pairs of genomes, updating their fitness scores.

    :return: None
    """
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))

    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[i+1:]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = PongGame(window, width, height)
            game.train_ai(genome1, genome2, config)

def run_neat(config):
    """
    Run the NEAT algorithm using the provided configuration.

    :param config: NEAT configuration for the neural networks.

    This function restores a checkpoint, runs the NEAT algorithm for a specified number of generations,
    and saves the best genome to a file.

    :return: None
    """
    # Uncomment the line below to create a new NEAT population
    # p = neat.Population(config)
    # Run NEAT algorithm using the provided configuration
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-22')
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    # Run NEAT with evaluation function and save the winner
    winner = p.run(eval_genomes, 10)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)

def test_ai(config):
    """
    Test the AI against the player using the best genome.

    :param config: NEAT configuration for the neural networks.

    This function sets up a Pygame window and allows the player to control one paddle
    while the AI controls the other using the best genome.

    :return: None
    """
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))

    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)

    game = PongGame(window, width, height)
    game.test_ai(winner, config)

if __name__ == "__main__":
    # Set up configuration for NEAT
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    # Uncomment the line below to run NEAT training
    #run_neat(config)
    # Uncomment the line below to test AI against player
    test_ai(config) # AI is playing against you
