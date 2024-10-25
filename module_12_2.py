import unittest
import runner_and_tournament as rat

"""Не выводится словарь. Пустой"""


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rat.Runner('Усэйн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)
        # for key in cls.all_results.keys():
        #     print(cls.all_results[key])

    def test_race_usain_nick(self):
        tournament = rat.Tournament(90, self.runner1, self.runner3)
        self.all_results = tournament.start()
        last_result = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_result == 'Ник')

    def test_race_andrey_and_nik(self):
        tournament = rat.Tournament(90, self.runner2, self.runner3)
        self.all_results = tournament.start()
        last_result = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_result == 'Ник')

    def test_race_usain_andrey_and_nik(self):
        tournament = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results = tournament.start()
        last_result = self.all_results[max(self.all_results.keys())]
        self.assertTrue(last_result == 'Ник')


if __name__ == '__main__':
    unittest.main()
