# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\rajpu\\OneDrive\\Desktop\\Study\\Intershalla\\VSCode\\Python_FinalProject_ProblemStatement\\Version\\Version1.17\\IntershallaCricket'],
             binaries=[],
             datas=[],
             hiddenimports=['sqlite3'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['pydoc','xml'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


unwanted ="""
api-ms-win-crt-stdio-l1-1-0.dll
api-ms-win-crt-runtime-l1-1-0.dll
api-ms-win-crt-math-l1-1-0.dll
api-ms-win-crt-locale-l1-1-0.dll
api-ms-win-crt-heap-l1-1-0.dll
api-ms-win-crt-convert-l1-1-0.dll
api-ms-win-crt-string-l1-1-0.dll
api-ms-win-crt-time-l1-1-0.dll
api-ms-win-crt-conio-l1-1-0.dll
api-ms-win-crt-filesystem-l1-1-0.dll
api-ms-win-crt-environment-l1-1-0.dll
api-ms-win-crt-process-l1-1-0.dll
ucrtbase.dll
api-ms-win-core-timezone-l1-1-0.dll
api-ms-win-core-heap-l1-1-0.dll
api-ms-win-core-handle-l1-1-0.dll
api-ms-win-core-file-l1-1-0.dll
api-ms-win-core-datetime-l1-1-0.dll
api-ms-win-core-debug-l1-1-0.dll
api-ms-win-core-namedpipe-l1-1-0.dll
api-ms-win-core-processthreads-l1-1-1.dll
api-ms-win-core-synch-l1-1-0.dll
api-ms-win-core-file-l1-2-0.dll
api-ms-win-core-interlocked-l1-1-0.dll
api-ms-win-core-console-l1-1-0.dll
api-ms-win-core-processthreads-l1-1-0.dll
api-ms-win-core-localization-l1-2-0.dll
api-ms-win-core-profile-l1-1-0.dll
api-ms-win-core-string-l1-1-0.dll
api-ms-win-core-rtlsupport-l1-1-0.dll
api-ms-win-core-sysinfo-l1-1-0.dll
api-ms-win-core-file-l2-1-0.dll
api-ms-win-core-errorhandling-l1-1-0.dll
api-ms-win-core-libraryloader-l1-1-0.dll
api-ms-win-core-processenvironment-l1-1-0.dll
api-ms-win-core-synch-l1-2-0.dll
api-ms-win-core-util-l1-1-0.dll
api-ms-win-core-memory-l1-1-0.dll
api-ms-win-crt-utility-l1-1-0.dll
Qt5Svg.dll
Qt5DBus.dll
Qt5WebSockets.dll
Qt5Network.dll
Qt5Quick.dll
Qt5Qml.dll
Qt5QmlModels.dll
MSVCP140.dll
libcrypto-1_1.dll
libssl-1_1.dll
select
_bz2
unicodedata
api-ms-win-crt-multibyte-l1-1-0.dll
PyQt5\\Qt\\plugins\\imageformats\\qwebp.dll
PyQt5\\Qt\\plugins\\imageformats\\qgif.dll
PyQt5\\Qt\\plugins\\platforms\\qminimal.dll
PyQt5\\Qt\\plugins\\platforms\\qwebgl.dll
d3dcompiler_47.dll
opengl32sw.dll
VCRUNTIME140.dll
libEGL.dll
libGLESv2.dll
""".split()



a.binaries = [x for x in a.binaries if not x[0] in unwanted]


print("===================== After Removing Unecessary Operation======================")
for i in a.binaries:
	print(i)

print("======================Adding Image to the application==========================")

a.datas +=[('cricketImg.png','C:\\Users\\rajpu\\OneDrive\\Desktop\\Study\\Intershalla\\VSCode\\Python_FinalProject_ProblemStatement\\Version\\Version1.18\IntershallaCricket\\Image\\cricketImg.png','DATA')
          ,('evaluateImg.png','C:\\Users\\rajpu\\OneDrive\\Desktop\\Study\\Intershalla\\VSCode\\Python_FinalProject_ProblemStatement\\Version\\Version1.18\IntershallaCricket\\Image\\evaluateImg.png','DATA')
          ,('newImg.png','C:\\Users\\rajpu\\OneDrive\\Desktop\\Study\\Intershalla\\VSCode\\Python_FinalProject_ProblemStatement\\Version\\Version1.18\IntershallaCricket\\Image\\newImg.png','DATA')
          ,('openImg.jpg','C:\\Users\\rajpu\\OneDrive\\Desktop\\Study\\Intershalla\\VSCode\\Python_FinalProject_ProblemStatement\\Version\\Version1.18\IntershallaCricket\\Image\\openImg.jpg','DATA')
          ,('saveImg.png','C:\\Users\\rajpu\\OneDrive\\Desktop\\Study\\Intershalla\\VSCode\\Python_FinalProject_ProblemStatement\\Version\\Version1.18\IntershallaCricket\\Image\\saveImg.png','DATA')
          ,('scoreImg.png','C:\\Users\\rajpu\\OneDrive\\Desktop\\Study\\Intershalla\\VSCode\\Python_FinalProject_ProblemStatement\\Version\\Version1.18\IntershallaCricket\\Image\\scoreImg.png','DATA')
          ,('teamImg.jpeg','C:\\Users\\rajpu\\OneDrive\\Desktop\\Study\\Intershalla\\VSCode\\Python_FinalProject_ProblemStatement\\Version\\Version1.18\IntershallaCricket\\Image\\teamImg.jpeg','DATA')
          ]
for i in a.datas:
    print(i)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
