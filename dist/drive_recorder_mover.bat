echo off
cd /d %~dp0
echo ファイル移動中、この画面が消えるまで、SDカードを取り外さないでください。
drive_recorder_mover.exe --search-file "*.mp4" --from-path "F:\EVENT" --dest-path "K:\マイドライブ\[SHARE]\Driving_Recode\autoplay\EVENT"
drive_recorder_mover.exe --search-file "*.mp4" --from-path "F:\VIDEO" --dest-path "K:\マイドライブ\[SHARE]\Driving_Recode\autoplay\VIDEO"
drive_recorder_mover.exe --search-file "*.avi" --from-path "F:" --dest-path "K:\マイドライブ\[SHARE]\Driving_Recode\autoplay"
echo 処理は終了しました。
timeout 10
exit