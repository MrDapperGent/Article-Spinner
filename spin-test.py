import unittest
from spin import Spin

class SpinTest(unittest.TestCase):

  def test_word(self):
    spin = Spin()
    word = "create"
    word = spin.word(word, 1)
    self.assertEqual(word, "generate")

  def test_sentence(self):
    spin = Spin()
    sentence = ["The", "man", "created", "the", "report"]
    sentence = spin.sentence(sentence, 1)
    self.assertEqual(sentence, ['The', 'male', 'created', 'the', 'announce'])

  def test_paragraph(self):
    spin = Spin()
    paragraph = [
      [
        "The", "man", "created", "the", "report"
      ],
      [
        "The", "report", "was", "an", "observation"
      ],
      [
        "His", "colleagues", "rewarded", "him", "for", "his", "study"
      ],
      [
        "Thus", "the", "university", "paid", "him", "significantly"
      ]
    ]
    paragraph = spin.paragraph(paragraph, 1)
    print(paragraph)

if __name__ == "__main__":
  unittest.main()