# Задача "Проверка на выносливость":

import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r = runner.Runner('Vadya')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = runner.Runner('Vadya')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        r1 = runner.Runner('Vadya')
        r2 = runner.Runner('Vasya')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()