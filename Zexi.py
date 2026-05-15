import threading
from internet_check import is_online
from alert import Alert
from DATA.DLG_data import online_dlg,offline_dlg
import random
from co_brain import zexi
from TextToSpeech.fast_DF_TTS import speak
from Automation.battery  import check_plug
from Time_Operations.throw_alert import check_schedule,check_Alam
from os import getcwd

Alam_path = f"{getcwd()}\\alarm.txt"
file_path = f'{getcwd()}\\schedule.txt'

ran_online_dlg = random.choice(online_dlg)
ran_offline_dlg = random.choice(offline_dlg)


def main():
    if is_online():
        t1 = threading.Thread(target=speak,args=(ran_online_dlg,))
        t2 = threading.Thread(target=Alert,args=(ran_online_dlg,))
        t3 = threading.Thread(target=check_plug)
        t4 = threading.Thread(target=check_schedule,args=(file_path,))
        t5 = threading.Thread(target=zexi)
        t6 = threading.Thread(target=check_Alam,args=(Alam_path,))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
    else:
        Alert(ran_offline_dlg)

main()


