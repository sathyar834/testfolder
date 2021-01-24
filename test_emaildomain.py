import unittest
import re
from emaildomain import validemail

class TestEmail(unittest.TestCase):

  def test_validemail(self):
    mail1= validemail("sathyar822@gmail.com")
    # email= "sathyar822@gmail.com"
    self.assertEqual(mail1, True)

if __name__ == '__main__':
  unittest.main()