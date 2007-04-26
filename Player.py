class Player:
  """
     A Player including score and state
  """
  def __init__(self):
     self.score=0
     self.answer=0

  def set_answer(self,answer):
     if self.answer==0:	
        self.answer=answer
        return True
     else:
        return False

