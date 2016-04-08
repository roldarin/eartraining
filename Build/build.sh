pip install pyinstaller
pyinstaller eartraining.py
pyinstaller --noconfirm --log-level=WARN --onefile --nowindow --hidden-import=secret1 --hidden-import=secret2 --upx-dir=/usr/local/share/  eartraining.spec
#or
python setup_cx_Freeze.py  build
#or
python setup_py2exe.py py2exe

cd build



