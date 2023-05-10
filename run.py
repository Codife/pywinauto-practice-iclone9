def func(name_audio, mouse, double_click, time, mouse_wheel, double_left_click, directory, os, librosa, send_keys, name_video, len, frames, find):
    mouse.click(button='left', coords=(192, 31))
    mouse.click(button='left', coords=(307, 66))
    mouse.click(button='left', coords=(531, 133))
    mouse.click(button='left', coords=(1217, 474))
    if len == 0:
        mouse.click(button='left', coords=(911, 602))
    if len == 0:
        double_left_click(
            "iClone||Window->AccuLips||Window->Open||Window->||Pane->Shell Folder View||Pane->Items View||List->audios||ListItem->Name||Edit")
        double_left_click(
            "iClone||Window->AccuLips||Window->Open||Window->File name:||ComboBox->File name:||Edit")
    print(name_audio)
    time.sleep(2.0)
    send_keys(name_audio)
    print(name_audio)
    send_keys('{ENTER}')
    mouse.click(button='left', coords=(1477, 770))
    time.sleep(20)
    mouse.click(button='left', coords=(1393, 923))
    mouse.click(button='left', coords=(285, 41))
    mouse.click(button='left', coords=(340, 93))
    mouse.click(button='left', coords=(966, 287))
    mouse_wheel(steps=-10)
    mouse.double_click(button='left', coords=(919, 722))
    send_keys(frames)
    mouse.click(button='left', coords=(1004, 867))
    mouse.click(button='left', coords=(71, 218))
    mouse.click(button='left', coords=(303, 194))
    time.sleep(2.0)
    send_keys('v')
    send_keys('{ENTER}')
    mouse.double_click(button='left', coords=(351, 425))
    send_keys(name_video)
    mouse.click(button='left', coords=(495, 501))
    foundDlg = True
    # while foundDlg:
    #     try:
    #         dlg = find("iClone||Window->Reminder||Window->||TitleBar")
    #         if (dlg):
    #             foundDlg = False
    #     except:
    #         print('POTTY')
    time.sleep(40.0)
    mouse.click(button='left', coords=(988, 567))  # close reminder
    mouse.click(button='left', coords=(1190, 155))
    mouse.click(button='left', coords=(1034, 533))
    print(name_audio)
    
