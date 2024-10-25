import unittest
import runner_and_tournament as rat

"""Не выводится словарь. Пустой"""


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = rat.Runner('Усэйн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # for key, value in enumerate(TournamentTest.all_results):
        #     print(f'{key+1}: {value}')

        for i in range(0, len(TournamentTest.all_results)):
            print(TournamentTest.all_results[i])

    def test_race_usain_nick(self):
        tournament = rat.Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    def test_race_andrey_and_nik(self):
        tournament = rat.Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    def test_race_usain_andrey_and_nik(self):
        tournament = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[3] == 'Ник')


if __name__ == '__main__':
    unittest.main()
