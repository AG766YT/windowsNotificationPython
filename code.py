import pywintypes
from win10toast import ToastNotifier

toast = ToastNotifier()

toast.show_toast("Sample","Sample",duration=30)