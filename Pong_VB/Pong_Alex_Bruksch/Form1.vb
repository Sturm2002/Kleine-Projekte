
Public Class frm_pong
    Dim ball_speed_x As Integer
    Dim ball_speed_y As Integer

    Dim punkte_a As Integer
    Dim punkte_b As Integer

    Dim winpunkte As Integer

    Dim playerspeed As Integer

    Dim Game_Start As Boolean
    Dim hindernis_speed As Integer

    Dim gamemode_single As Boolean

    ' Erkennt die Eingabe an der Tastatur
    Private Sub frm_pong_KeyDown(sender As Object, e As KeyEventArgs) Handles Me.KeyDown

        'Spieler A

        ' Wenn "I" gedrückt wird
        If e.KeyCode = Keys.I And spieler_b.Top > 0 And Game_Start = True And gamemode_single = False Then
            move_a_up()
        End If


        ' Wenn "K" gedrückt wird
        If e.KeyCode = Keys.K And spieler_b.Top < 460 And Game_Start = True And gamemode_single = False Then
            move_a_down()
        End If


        ' Spieler B

        ' Wenn "W" gedrückt wird
        If e.KeyCode = Keys.W And spieler_a.Top > 0 And Game_Start = True Then
            move_b_up()
        End If

        ' Wenn "S" gedrückt wird
        If e.KeyCode = Keys.S And spieler_a.Top < 460 And Game_Start = True Then
            move_b_down()
        End If

    End Sub

    ' Macht das Sichtbare des Spielfelds Bereit (Alles was man sehen soll sieht man und was nicht das nicht)
    Private Sub Cmd_LoadGame_Click(sender As Object, e As EventArgs) Handles cmd_LoadGame.Click
        cmd_singleplayer.Visible = True
        cmd_multiplayer.Visible = True
        cmd_settings_exit.Visible = True

        cmd_settings.Visible = False
        cmd_LoadGame.Visible = False
        cmd_exit.Visible = False

    End Sub

    ' Wird nach der Pause nach dem drücken von Einzel/ - Mehrspieler einmal ausgeführt
    Private Sub GameStart_timer_Tick(sender As Object, e As EventArgs) Handles GameStart_timer.Tick

        pic_ws.Visible = False
        pic_arrows.Visible = False
        LoadGame()

        GameStart_timer.Stop() ' verhindert dass sich die Schleife mehrmals ausführt
    End Sub

    ' führt die Funktion "LoadSettings" aus
    Private Sub Cmd_settings_Click(sender As Object, e As EventArgs) Handles cmd_settings.Click
        LoadSettings()
    End Sub

    'Beendet das Programm
    Private Sub Cmd_exit_Click(sender As Object, e As EventArgs) Handles cmd_exit.Click
        End
    End Sub

    ' Führt die Funktion "LoadMenu" aus
    Private Sub Cmd_backtomenu_Click(sender As Object, e As EventArgs) Handles cmd_backtomenu.Click
        LoadMenu()
    End Sub


    ' Startet das Spiel im Einzelspieler-Modus
    Private Sub Cmd_singleplayer_Click(sender As Object, e As EventArgs) Handles cmd_singleplayer.Click

        ' Startet die Schleife bzw. die Pause nach dem Drücken und dem Spiel Start
        GameStart_timer.Start()

        lbl_punkte_a.Visible = False
        lbl_punkte_b.Visible = False

        ball_pos.Visible = False

        spieler_a.Visible = False
        spieler_b.Visible = False

        ball.Visible = False

        cmd_LoadGame.Visible = False
        cmd_settings.Visible = False
        cmd_exit.Visible = False
        pic_ws.Visible = True
        pic_arrows.Visible = False



        ' wird benötigt um den Spielmodus auf Einzelspieler zu setzen            Bei True, Einzelspieler, Bei False startet der Mehrspieler
        gamemode_single = True
    End Sub


    ' Identisch zu Oben 
    ' /\
    ' |
    ' |
    ' |

    Private Sub Cmd_multiplayer_Click(sender As Object, e As EventArgs) Handles cmd_multiplayer.Click
        GameStart_timer.Start()


        lbl_punkte_a.Visible = False
        lbl_punkte_b.Visible = False

        ball_pos.Visible = False

        spieler_a.Visible = False
        spieler_b.Visible = False

        ball.Visible = False

        cmd_LoadGame.Visible = False
        cmd_settings.Visible = False
        cmd_exit.Visible = False
        pic_ws.Visible = True
        pic_arrows.Visible = True

        ' Setzt den Spielmodus auf Mehrspieler
        gamemode_single = False


    End Sub

    Private Sub Cmd_settings_exit_Click(sender As Object, e As EventArgs) Handles cmd_settings_exit.Click
        winpunkte = input_winpunkte.Text
        ball_speed_x = input_speed.Text
        ball_speed_y = input_speed.Text
        playerspeed = input_playerspeed.Text

        cmd_singleplayer.Visible = False
        cmd_multiplayer.Visible = False
        ck_hindernis.Visible = False

        punkte_a = 0
        punkte_b = 0

        menu_title.Visible = True
        menu_byalex.Visible = True

        lbl_AWinLos.Visible = False
        lbl_bWinLos.Visible = False



        LoadMenu()
    End Sub




    ' Wird ausgeführt sobald der Benutzer das Spiel Startet 
    Function LoadGame()
        'My.Computer.Audio.Stop()

        If ck_hindernis.Checked = True Then         ' Überprüft ob in den Einstellungen das Hindernis eingeschaltet wurde
            hindernis.Visible = True
        End If

        cmd_singleplayer.Visible = False
        cmd_multiplayer.Visible = False

        pic_arrows.Visible = False
        pic_ws.Visible = False

        winpunkte = input_winpunkte.Text                ' Aktualisiert die Textfelder Oben & unten
        playerspeed = input_playerspeed.Text
        ball_speed_x = input_speed.Text
        ball_speed_y = input_speed.Text

        punkte_a = 0                ' Setzt bei Spielstart die Punkte beider Spieler auf 0
        punkte_b = 0

        ball.Left = 375                ' Startposition des Balls bei Spielstart
        ball.Top = 215

        spieler_a.Top = 215            ' Startposition der Spieler bei Spielstart
        spieler_b.Top = 215

        lbl_punkte_a.Visible = True
        lbl_punkte_b.Visible = True

        ball_pos.Visible = True

        spieler_a.Visible = True
        spieler_b.Visible = True

        ball.Visible = True
        menu_title.Visible = False
        menu_byalex.Visible = False
        cmd_exit.Visible = False
        cmd_LoadGame.Visible = False
        cmd_settings.Visible = False
        cmd_backtomenu.Visible = True

        Game_Start = True
        Return Game_Start               ' gibt den Wert des Booleans "Game_start" außerhalb der Funktion weiter
    End Function


    Function LoadMenu()
        ' My.Computer.Audio.Stop()
        'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\bgmusik.wav", AudioPlayMode.BackgroundLoop)

        lbl_punkte_a.Visible = False
        lbl_punkte_b.Visible = False

        ball_pos.Visible = False

        spieler_a.Visible = False
        spieler_b.Visible = False

        ball.Visible = False

        cmd_LoadGame.Visible = True
        cmd_settings.Visible = True
        cmd_exit.Visible = True

        cmd_settings_exit.Visible = False
        settings_lbl_winpunkte1.Visible = False
        settings_lbl_winpunkte2.Visible = False
        input_winpunkte.Visible = False
        ck_hindernis.Visible = False
        hindernis.Visible = False

        settings_lbl_playerspeed.Visible = False
        input_playerspeed.Visible = False

        settings_lbl_speed1.Visible = False
        input_speed.Visible = False
        cmd_backtomenu.Visible = False
        menu_byalex.Visible = True
        menu_title.Visible = True


        Game_Start = False
        Return Game_Start

    End Function

    Function LoadSettings()



        cmd_exit.Visible = False
        cmd_LoadGame.Visible = False
        cmd_settings.Visible = False



        settings_lbl_winpunkte1.Visible = True
        settings_lbl_winpunkte2.Visible = True
        settings_lbl_speed1.Visible = True
        settings_lbl_playerspeed.Visible = True
        ck_hindernis.Visible = True

        input_speed.Visible = True
        input_winpunkte.Visible = True
        input_playerspeed.Visible = True

        cmd_settings_exit.Visible = True

    End Function

    Function endscreen_a()

        Game_Start = False


        cmd_backtomenu.Visible = False

        lbl_punkte_a.Visible = False
        lbl_punkte_b.Visible = False

        ball_pos.Visible = False

        spieler_a.Visible = False
        spieler_b.Visible = False
        hindernis.Visible = False

        ball.Visible = False


        lbl_AWinLos.Text = ("Gewonnen!")
        lbl_bWinLos.Text = ("Verloren!")

        lbl_AWinLos.Visible = True
        lbl_bWinLos.Visible = True



        Return Game_Start
    End Function

    Function endscreen_b()


        Game_Start = False

        cmd_backtomenu.Visible = False
        lbl_punkte_a.Visible = False
        lbl_punkte_b.Visible = False

        ball_pos.Visible = False

        spieler_a.Visible = False
        spieler_b.Visible = False
        hindernis.Visible = False

        ball.Visible = False


        lbl_AWinLos.Text = ("Verloren!")
        lbl_bWinLos.Text = ("Gewonnen!")

        lbl_AWinLos.Visible = True
        lbl_bWinLos.Visible = True
        Return Game_Start
    End Function
    ' wird die jeweilige Funktion ausgeführt, ändert sich die Y-Koordinate des Jeweiligen spielers um in dem fall (10 * die eingestellte spielergeschwindigkeit)
    ' z.B bei einem wert von 2 (Standart) Wäre die Geschwindigkeit 20px pro ausführung
    Function move_a_up()
        spieler_b.Top -= (10 * playerspeed)
    End Function

    Function move_a_down()
        spieler_b.Top += (10 * playerspeed)
    End Function

    Function move_b_up()
        spieler_a.Top -= (10 * playerspeed)
    End Function
    Function move_b_down()
        spieler_a.Top += (10 * playerspeed)
    End Function




    Public Sub frm_pong_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        'My.Computer.Audio.Stop()
        'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\bgmusik.wav", AudioPlayMode.BackgroundLoop)

        ball_speed_x = 2
        ball_speed_y = 2

        hindernis_speed = 3


    End Sub



    ' läuft alle 100 ms einmal durch, interval wird durch den timer im entwurf festgelegt

    Public Sub Sleep_Tick(sender As Object, e As EventArgs) Handles sleep.Tick


        If Game_Start = True Then                   ' wenn das Spiel gestartet wird , werden alle nicht benötigten objekte "nicht sichtbar"

            cmd_exit.Visible = False
            cmd_settings.Visible = False
            cmd_multiplayer.Visible = False
            cmd_singleplayer.Visible = False
            cmd_LoadGame.Visible = False
            input_playerspeed.Visible = False
            input_speed.Visible = False
            input_winpunkte.Visible = False
            settings_lbl_playerspeed.Visible = False
            settings_lbl_speed1.Visible = False
            settings_lbl_winpunkte1.Visible = False
            settings_lbl_winpunkte2.Visible = False
            menu_byalex.Visible = False
            menu_title.Visible = False
            cmd_settings_exit.Visible = False





            If gamemode_single = False Then         ' wenn diese bedingung zutrifft, startet das Spiel im Mehrspieler

                If ck_hindernis.Checked = True Then ' überprüft zusätzlich ob es ein Hindernis geben soll
                    hindernis.Top += hindernis_speed
                    If hindernis.Top < 10 Then
                        hindernis_speed *= -1

                    ElseIf hindernis.Top > 400 Then
                        hindernis_speed *= -1

                    End If

                    '#### Schwierigster Part ######
                    ' Ich habe für diesen Part etwa 2 Stunden gebraucht da die ganze "If-Schleife" ziemlicher BRAINFUCK war (;

                    ' Überprüft ob die Ball X-Koordinate größer als die des (Hindernisses - 22) ist (Linke Wand des Hindernisses) und kleiner als die des (Hindernisses + 10) ist (Rechte wand des Hindernisses)
                    'zusätzlich ob die Ball Y-Koordinate größer als die des (Hindernisses - 40) ist (Obere Kante des Hindernisses) und kleiner als die des (Hindernisses + 160) ist (Untere Kante des Hindernisses)

                    '################ auch die der Spieler aber da bin ich jetzt zu faul das zu Kommentieren, viel Spaß beim Selbst entschlüsseln (; #############

                    If (ball.Left > hindernis.Left - 22 And ball.Left < hindernis.Left + 10 And ball.Top > hindernis.Top - 40 And ball.Top < hindernis.Top + 160) Or (ball.Left < hindernis.Left + 22 And ball.Left > hindernis.Left - 10 And ball.Top > hindernis.Top - 40 And ball.Top < hindernis.Top + 160) Then
                        ball_speed_x *= -1
                        ' My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\hit.wav")
                    End If


                End If


                If punkte_a >= winpunkte Then       ' überprüft ob der Punktestand eines Spielers der Gewinnbedingung übereinstimmt
                    endscreen_a()
                    cmd_settings_exit.Visible = True
                    'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\lost.wav")
                End If

                If punkte_b >= winpunkte Then      ' Same
                    endscreen_b()
                    cmd_settings_exit.Visible = True
                    'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\lost.wav")
                End If

                ' Prüft ob der Ball Hinter Spieler A ist, was zur addition eines Punktes führen würde

                If ball.Left < 60 Then
                    punkte_b += 1

                    spieler_a.Top = 215
                    spieler_b.Top = 215

                    ball_speed_x *= -1
                    ball_speed_y *= -1

                    ball.Left = 380
                    ball.Top = 240

                    timer_point.Start()
                    Game_Start = False

                    ' My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\lost.wav")


                End If

                ' Prüft ob der Ball Hinter Spieler B ist, was zur addition eines Punktes führen würde
                If ball.Left > 710 Then
                    punkte_a += 1

                    spieler_a.Top = 215
                    spieler_b.Top = 215

                    ball_speed_x *= -1
                    ball_speed_y *= -1

                    ball.Left = 380
                    ball.Top = 240

                    timer_point.Start()
                    Game_Start = False

                    'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\lost.wav")

                End If


                ' prüft ob der ball an der decke ist, und invertiert die Y bewegung, was dazu führt das der ball sich schräg nach unten bewegt
                If ball.Top < 4 Then
                    ball_speed_y *= -1             ' invertiert die y bewegung damit der ball nach UNTEN geht
                    ball.Top = 6
                    'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\hit.wav")
                End If

                'prüft ob der ball am Boden ist, und invertiert die Y bewegung, was dazu führt das der ball sich schräg nach oben bewegt
                If ball.Top > 530 Then
                    ball_speed_y *= -1              ' invertiert die y bewegung damit der ball nach OBEN geht
                    ball.Top = 528
                    ' My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\hit.wav")
                End If

                ' Prüft ob die x coordinate zu der von spieler a bzw. b ähnlich ist, und ob gleichzeitig die y coordinate passt

                If ((ball.Left < spieler_a.Left + 22 And ball.Left > spieler_a.Left - 11) And ball.Top > spieler_a.Top - 25 And ball.Top < spieler_a.Top + 90) Then
                    ball_speed_x *= -1              ' invertiert die x Bewegung damit der ball wieder richtung mitte geht
                    ' My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\hit.wav")
                End If

                If ((ball.Left > spieler_b.Left - 22 And ball.Left < spieler_b.Left + 11) And ball.Top > spieler_b.Top - 25 And ball.Top < spieler_b.Top + 90) Then
                    ball_speed_x *= -1
                    'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\hit.wav")

                End If


                ' Bewegt den Ball Kontinuirlich
                ball.Left += ball_speed_x
                ball.Top += ball_speed_y


                ' Zeigt die Coordinaten des Balls an
                ball_pos.Text = "(" & ball.Top & "," & ball.Left & ")"

                ' Zeigt den Punktestand an
                lbl_punkte_a.Text = punkte_a
                lbl_punkte_b.Text = punkte_b

            End If

            If gamemode_single = True Then          ' prüft ob der einzelspieler modus benutz werden soll

                ' Hier ist der Großteil identisch zum Mehrspieler, weshalb ich nur den "Bot" kommentieren werde
                If ck_hindernis.Checked = True Then
                    hindernis.Top += hindernis_speed
                    If hindernis.Top < 10 Then
                        hindernis_speed *= -1

                    ElseIf hindernis.Top > 400 Then
                        hindernis_speed *= -1

                    End If


                    If (ball.Left > hindernis.Left - 22 And ball.Left < hindernis.Left + 10 And ball.Top > hindernis.Top - 40 And ball.Top < hindernis.Top + 160) Or (ball.Left < hindernis.Left + 22 And ball.Left > hindernis.Left - 10 And ball.Top > hindernis.Top - 40 And ball.Top < hindernis.Top + 160) Then
                        ball_speed_x *= -1
                        ' My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\hit.wav")
                    End If


                End If

                If punkte_a >= winpunkte Then
                    endscreen_a()
                    cmd_settings_exit.Visible = True
                    'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\lost.wav")
                End If

                If punkte_b >= winpunkte Then
                    endscreen_b()
                    cmd_settings_exit.Visible = True
                    'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\lost.wav")
                End If

                If ball.Top < spieler_b.Top And spieler_b.Top > 0 Then           ' Falls die Y Koordinate des Balls unter der des Bots ist, wird der bot nach unten bewegt solange er nicht zu weit unten ist
                    spieler_b.Top -= 2

                ElseIf ball.Top > spieler_b.Top And spieler_b.Top < 550 Then     ' Falls die Y Koordinate des Balls über der des Bots ist, wird der bot nach oben bewegt solange er nicht zu weit oben ist
                    spieler_b.Top += 2


                End If



                ' Prüfen Ob Der Ball hinter Spieler A ist

                If ball.Left < 60 Then
                    punkte_b += 1

                    spieler_a.Top = 215
                    spieler_b.Top = 215

                    ball_speed_x *= -1
                    ball_speed_y *= -1

                    ball.Left = 380
                    ball.Top = 240

                    timer_point.Start()
                    Game_Start = False

                    'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\lost.wav")


                End If

                ' Prüfen Ob Der Ball hinter Spieler B ist
                If ball.Left > 710 Then
                    punkte_a += 1

                    spieler_a.Top = 215
                    spieler_b.Top = 215

                    ball_speed_x *= -1
                    ball_speed_y *= -1

                    ball.Left = 380
                    ball.Top = 240

                    timer_point.Start()
                    Game_Start = False



                    ' My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\lost.wav")

                End If


                ' prüfen ob der ball an der Decke ist
                If ball.Top < 4 Then
                    ball_speed_y *= -1              ' invertiert die y bewegung damit der ball nach UNTEN geht
                    ball.Top = 6
                    'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\hit.wav")
                End If

                'prüfen ob der ball am boden ist
                If ball.Top > 530 Then
                    ball_speed_y *= -1              ' invertiert die y bewegung damit der ball nach OBEN geht
                    ball.Top = 528
                    'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\hit.wav")
                End If

                ' Prüft ob die x coordinate zu der von spieler a bzw. b ähnlich ist, und ob gleichzeitig die y coordinate passt

                If ((ball.Left < spieler_a.Left + 22 And ball.Left > spieler_a.Left - 11) And ball.Top > spieler_a.Top - 25 And ball.Top < spieler_a.Top + 90) Then
                    ball_speed_x *= -1              ' invertiert die x Bewegung damit der ball wieder richtung mitte geht
                    'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\hit.wav")
                End If

                If ((ball.Left > spieler_b.Left - 22 And ball.Left < spieler_b.Left + 11) And ball.Top > spieler_b.Top - 25 And ball.Top < spieler_b.Top + 90) Then
                    ball_speed_x *= -1
                    'My.Computer.Audio.Play("C:\Users\sturm\source\repos\Pong_Alex_Bruksch\Pong_Alex_Bruksch\Pics\hit.wav")

                End If


                ' Bewegt den ball 
                ball.Left += ball_speed_x
                ball.Top += ball_speed_y


                ' Zeigt die Coordinaten des Balls an
                ball_pos.Text = "(" & ball.Top & "," & ball.Left & ")"

                ' Zeigt den Punktestand an
                lbl_punkte_a.Text = punkte_a
                lbl_punkte_b.Text = punkte_b

            End If
        End If
    End Sub

    Private Sub Timer_point_Tick(sender As Object, e As EventArgs) Handles timer_point.Tick
        Game_Start = True
        timer_point.Stop()
    End Sub


    ' Der Rest Sorgt dafür, das die Buttons sich hervorheben sobald die maus auf dem jeweiligen Button ist

    Private Sub cmd_LoadGame_MouseEnter(sender As Object, e As EventArgs) Handles cmd_LoadGame.MouseEnter
        cmd_LoadGame.BackColor = Color.Red
    End Sub

    Private Sub cmd_LoadGame_MouseLeave(sender As Object, e As EventArgs) Handles cmd_LoadGame.MouseLeave
        cmd_LoadGame.BackColor = Color.Black
    End Sub

    Private Sub cmd_settings_MouseEnter(sender As Object, e As EventArgs) Handles cmd_settings.MouseEnter
        cmd_settings.BackColor = Color.Red
    End Sub

    Private Sub cmd_settings_MouseLeave(sender As Object, e As EventArgs) Handles cmd_settings.MouseLeave
        cmd_settings.BackColor = Color.Black
    End Sub

    Private Sub cmd_exit_MouseEnter(sender As Object, e As EventArgs) Handles cmd_exit.MouseEnter
        cmd_exit.BackColor = Color.Red
    End Sub

    Private Sub cmd_exit_MouseLeave(sender As Object, e As EventArgs) Handles cmd_exit.MouseLeave
        cmd_exit.BackColor = Color.Black
    End Sub

    Private Sub cmd_settings_exit_MouseEnter(sender As Object, e As EventArgs) Handles cmd_settings_exit.MouseEnter
        cmd_settings_exit.BackColor = Color.Red
    End Sub

    Private Sub cmd_settings_exit_MouseLeave(sender As Object, e As EventArgs) Handles cmd_settings_exit.MouseLeave
        cmd_settings_exit.BackColor = Color.Black
    End Sub

    Private Sub cmd_backtomenu_MouseEnter(sender As Object, e As EventArgs) Handles cmd_backtomenu.MouseEnter
        cmd_backtomenu.BackColor = Color.Red
    End Sub

    Private Sub cmd_backtomenu_MouseLeave(sender As Object, e As EventArgs) Handles cmd_backtomenu.MouseLeave
        cmd_backtomenu.BackColor = Color.Black
    End Sub

    Private Sub cmd_singleplayer_MouseEnter(sender As Object, e As EventArgs) Handles cmd_singleplayer.MouseEnter
        cmd_singleplayer.BackColor = Color.Red
    End Sub

    Private Sub cmd_singleplayer_MouseLeave(sender As Object, e As EventArgs) Handles cmd_singleplayer.MouseLeave
        cmd_singleplayer.BackColor = Color.Black
    End Sub

    Private Sub cmd_multiplayer_MouseEnter(sender As Object, e As EventArgs) Handles cmd_multiplayer.MouseEnter
        cmd_multiplayer.BackColor = Color.Red
    End Sub

    Private Sub cmd_multiplayer_MouseLeave(sender As Object, e As EventArgs) Handles cmd_multiplayer.MouseLeave
        cmd_multiplayer.BackColor = Color.Black
    End Sub

    Private Sub ck_hindernis_MouseEnter(sender As Object, e As EventArgs) Handles ck_hindernis.MouseEnter
        If ck_hindernis.Checked = True Then
            ck_hindernis.BackColor = Color.Green

        ElseIf ck_hindernis.Checked = False Then
            ck_hindernis.BackColor = Color.Red

        End If
    End Sub

    Private Sub ck_hindernis_MouseLeave(sender As Object, e As EventArgs) Handles ck_hindernis.MouseLeave

        If ck_hindernis.Checked = True Then
            ck_hindernis.BackColor = Color.Green

        ElseIf ck_hindernis.Checked = False Then
            ck_hindernis.BackColor = Color.Red

        End If
    End Sub
End Class


' Made By Alex at the 28.7.2019
' Have Fun!!!
