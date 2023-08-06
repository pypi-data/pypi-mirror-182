import main


class Test_Main_Do_sync_work:
    def test_do_sync_work_1(self):
        main.do_sync_work("Edmond")

    def test_do_sync_work_2(self):
        main.do_sync_work("Pierre Edouard")

    def test_do_sync_work_3(self):
        main.do_sync_work("Jean-Philippe")
