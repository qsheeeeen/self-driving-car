from rl_toolbox import Runner
from rl_toolbox.agent import PPOAgent
from rl_toolbox.policy import CNNPolicy


def main():
    # for i in range(4, 12, 2):
    #     runner = Runner(
    #         'CarRacing-v0',
    #         PPOAgent,
    #         CNNPolicy,
    #         record_data=False,
    #         data_path=None,
    #         save=True,
    #         load=(i > 4),
    #         weight_path='./weights/')
    #
    #     runner.run(abs_output_limit=[1, i / 10, 1], num_episode=100, continue_plot=(i < 12))

    runner = Runner(
        'CarRacing-v0',
        PPOAgent,
        CNNPolicy,
        record_data=False,
        data_path=None,
        save=True,
        load=False,
        weight_path='./weights/')

    runner.run(abs_output_limit=[1, 0.6, 1],num_episode=500)


if __name__ == '__main__':
    main()
