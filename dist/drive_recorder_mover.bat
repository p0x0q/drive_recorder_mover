echo off
cd /d %~dp0
echo �t�@�C���ړ����A���̉�ʂ�������܂ŁASD�J�[�h�����O���Ȃ��ł��������B
drive_recorder_mover.exe --search-file "*.mp4" --from-path "F:\EVENT" --dest-path "K:\�}�C�h���C�u\[SHARE]\Driving_Recode\autoplay\EVENT"
drive_recorder_mover.exe --search-file "*.mp4" --from-path "F:\VIDEO" --dest-path "K:\�}�C�h���C�u\[SHARE]\Driving_Recode\autoplay\VIDEO"
drive_recorder_mover.exe --search-file "*.avi" --from-path "F:" --dest-path "K:\�}�C�h���C�u\[SHARE]\Driving_Recode\autoplay"
echo �����͏I�����܂����B
timeout 10
exit