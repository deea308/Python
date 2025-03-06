from repository import PointRepository
from UI import UI

Repo = PointRepository()
Ui = UI(Repo)
Ui.start()