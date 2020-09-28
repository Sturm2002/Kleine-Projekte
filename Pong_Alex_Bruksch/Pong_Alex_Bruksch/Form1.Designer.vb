<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class frm_pong
    Inherits System.Windows.Forms.Form

    'Das Formular überschreibt den Löschvorgang, um die Komponentenliste zu bereinigen.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Wird vom Windows Form-Designer benötigt.
    Private components As System.ComponentModel.IContainer

    'Hinweis: Die folgende Prozedur ist für den Windows Form-Designer erforderlich.
    'Das Bearbeiten ist mit dem Windows Form-Designer möglich.  
    'Das Bearbeiten mit dem Code-Editor ist nicht möglich.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(frm_pong))
        Me.ball = New System.Windows.Forms.Label()
        Me.spieler_b = New System.Windows.Forms.Label()
        Me.spieler_a = New System.Windows.Forms.Label()
        Me.sleep = New System.Windows.Forms.Timer(Me.components)
        Me.ball_pos = New System.Windows.Forms.Label()
        Me.lbl_punkte_a = New System.Windows.Forms.Label()
        Me.lbl_punkte_b = New System.Windows.Forms.Label()
        Me.menu_title = New System.Windows.Forms.Label()
        Me.menu_byalex = New System.Windows.Forms.Label()
        Me.cmd_LoadGame = New System.Windows.Forms.Button()
        Me.cmd_settings = New System.Windows.Forms.Button()
        Me.cmd_exit = New System.Windows.Forms.Button()
        Me.GameStart_timer = New System.Windows.Forms.Timer(Me.components)
        Me.input_winpunkte = New System.Windows.Forms.RichTextBox()
        Me.settings_lbl_winpunkte2 = New System.Windows.Forms.Label()
        Me.settings_lbl_winpunkte1 = New System.Windows.Forms.Label()
        Me.cmd_settings_exit = New System.Windows.Forms.Button()
        Me.lbl_bWinLos = New System.Windows.Forms.Label()
        Me.lbl_AWinLos = New System.Windows.Forms.Label()
        Me.lbl_UpDown = New System.Windows.Forms.Label()
        Me.pic_arrows = New System.Windows.Forms.PictureBox()
        Me.pic_ws = New System.Windows.Forms.PictureBox()
        Me.timer_point = New System.Windows.Forms.Timer(Me.components)
        Me.settings_lbl_speed1 = New System.Windows.Forms.Label()
        Me.input_speed = New System.Windows.Forms.RichTextBox()
        Me.settings_lbl_playerspeed = New System.Windows.Forms.Label()
        Me.input_playerspeed = New System.Windows.Forms.RichTextBox()
        Me.cmd_backtomenu = New System.Windows.Forms.Button()
        Me.cmd_singleplayer = New System.Windows.Forms.Button()
        Me.cmd_multiplayer = New System.Windows.Forms.Button()
        Me.ck_hindernis = New System.Windows.Forms.CheckBox()
        Me.hindernis = New System.Windows.Forms.Label()
        CType(Me.pic_arrows, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.pic_ws, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'ball
        '
        Me.ball.AutoSize = True
        Me.ball.BackColor = System.Drawing.Color.Red
        Me.ball.Font = New System.Drawing.Font("Microsoft Sans Serif", 12.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.ball.ForeColor = System.Drawing.Color.Red
        Me.ball.Location = New System.Drawing.Point(375, 215)
        Me.ball.MinimumSize = New System.Drawing.Size(30, 30)
        Me.ball.Name = "ball"
        Me.ball.Size = New System.Drawing.Size(30, 30)
        Me.ball.TabIndex = 0
        Me.ball.Text = "__"
        Me.ball.Visible = False
        '
        'spieler_b
        '
        Me.spieler_b.AutoSize = True
        Me.spieler_b.BackColor = System.Drawing.Color.White
        Me.spieler_b.Font = New System.Drawing.Font("Microsoft Sans Serif", 12.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.spieler_b.ForeColor = System.Drawing.Color.White
        Me.spieler_b.Location = New System.Drawing.Point(709, 215)
        Me.spieler_b.MaximumSize = New System.Drawing.Size(20, 100)
        Me.spieler_b.MinimumSize = New System.Drawing.Size(20, 100)
        Me.spieler_b.Name = "spieler_b"
        Me.spieler_b.Size = New System.Drawing.Size(20, 100)
        Me.spieler_b.TabIndex = 1
        Me.spieler_b.Text = "__"
        Me.spieler_b.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        Me.spieler_b.Visible = False
        '
        'spieler_a
        '
        Me.spieler_a.AutoSize = True
        Me.spieler_a.BackColor = System.Drawing.Color.White
        Me.spieler_a.Font = New System.Drawing.Font("Microsoft Sans Serif", 12.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.spieler_a.ForeColor = System.Drawing.Color.White
        Me.spieler_a.Location = New System.Drawing.Point(69, 215)
        Me.spieler_a.MaximumSize = New System.Drawing.Size(20, 100)
        Me.spieler_a.MinimumSize = New System.Drawing.Size(20, 100)
        Me.spieler_a.Name = "spieler_a"
        Me.spieler_a.Size = New System.Drawing.Size(20, 100)
        Me.spieler_a.TabIndex = 2
        Me.spieler_a.Text = "__"
        Me.spieler_a.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        Me.spieler_a.Visible = False
        '
        'sleep
        '
        Me.sleep.Enabled = True
        Me.sleep.Interval = 10
        '
        'ball_pos
        '
        Me.ball_pos.AutoSize = True
        Me.ball_pos.Font = New System.Drawing.Font("MS PGothic", 14.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.ball_pos.ForeColor = System.Drawing.Color.White
        Me.ball_pos.Location = New System.Drawing.Point(318, 533)
        Me.ball_pos.Name = "ball_pos"
        Me.ball_pos.Size = New System.Drawing.Size(157, 19)
        Me.ball_pos.TabIndex = 3
        Me.ball_pos.Text = "Koordinaten Ball"
        Me.ball_pos.Visible = False
        '
        'lbl_punkte_a
        '
        Me.lbl_punkte_a.AutoSize = True
        Me.lbl_punkte_a.Font = New System.Drawing.Font("MS PGothic", 12.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lbl_punkte_a.ForeColor = System.Drawing.Color.White
        Me.lbl_punkte_a.Location = New System.Drawing.Point(121, 9)
        Me.lbl_punkte_a.Name = "lbl_punkte_a"
        Me.lbl_punkte_a.Size = New System.Drawing.Size(120, 16)
        Me.lbl_punkte_a.TabIndex = 4
        Me.lbl_punkte_a.Text = "Punktestand A"
        Me.lbl_punkte_a.Visible = False
        '
        'lbl_punkte_b
        '
        Me.lbl_punkte_b.AutoSize = True
        Me.lbl_punkte_b.Font = New System.Drawing.Font("MS PGothic", 12.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lbl_punkte_b.ForeColor = System.Drawing.Color.White
        Me.lbl_punkte_b.Location = New System.Drawing.Point(559, 9)
        Me.lbl_punkte_b.Name = "lbl_punkte_b"
        Me.lbl_punkte_b.Size = New System.Drawing.Size(120, 16)
        Me.lbl_punkte_b.TabIndex = 5
        Me.lbl_punkte_b.Text = "Punktestand B"
        Me.lbl_punkte_b.Visible = False
        '
        'menu_title
        '
        Me.menu_title.AutoSize = True
        Me.menu_title.Font = New System.Drawing.Font("Harlow Solid Italic", 72.0!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.menu_title.ForeColor = System.Drawing.Color.Red
        Me.menu_title.Location = New System.Drawing.Point(211, 85)
        Me.menu_title.Name = "menu_title"
        Me.menu_title.Size = New System.Drawing.Size(264, 121)
        Me.menu_title.TabIndex = 6
        Me.menu_title.Text = "Pong"
        '
        'menu_byalex
        '
        Me.menu_byalex.AutoSize = True
        Me.menu_byalex.BackColor = System.Drawing.Color.Transparent
        Me.menu_byalex.Font = New System.Drawing.Font("Harlow Solid Italic", 18.0!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.menu_byalex.ForeColor = System.Drawing.Color.Silver
        Me.menu_byalex.Location = New System.Drawing.Point(411, 206)
        Me.menu_byalex.Name = "menu_byalex"
        Me.menu_byalex.Size = New System.Drawing.Size(105, 30)
        Me.menu_byalex.TabIndex = 7
        Me.menu_byalex.Text = "By Alex"
        '
        'cmd_LoadGame
        '
        Me.cmd_LoadGame.FlatAppearance.BorderColor = System.Drawing.Color.Red
        Me.cmd_LoadGame.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.cmd_LoadGame.Font = New System.Drawing.Font("Harlow Solid Italic", 20.25!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.cmd_LoadGame.ForeColor = System.Drawing.Color.White
        Me.cmd_LoadGame.Location = New System.Drawing.Point(257, 275)
        Me.cmd_LoadGame.Name = "cmd_LoadGame"
        Me.cmd_LoadGame.Size = New System.Drawing.Size(243, 50)
        Me.cmd_LoadGame.TabIndex = 8
        Me.cmd_LoadGame.Text = "Spiel Starten"
        Me.cmd_LoadGame.UseVisualStyleBackColor = True
        '
        'cmd_settings
        '
        Me.cmd_settings.BackColor = System.Drawing.Color.Black
        Me.cmd_settings.FlatAppearance.BorderColor = System.Drawing.Color.Red
        Me.cmd_settings.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.cmd_settings.Font = New System.Drawing.Font("Harlow Solid Italic", 20.25!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.cmd_settings.ForeColor = System.Drawing.Color.White
        Me.cmd_settings.Location = New System.Drawing.Point(257, 347)
        Me.cmd_settings.Name = "cmd_settings"
        Me.cmd_settings.Size = New System.Drawing.Size(243, 50)
        Me.cmd_settings.TabIndex = 9
        Me.cmd_settings.Text = "Einstellungen"
        Me.cmd_settings.UseVisualStyleBackColor = False
        '
        'cmd_exit
        '
        Me.cmd_exit.FlatAppearance.BorderColor = System.Drawing.Color.Red
        Me.cmd_exit.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.cmd_exit.Font = New System.Drawing.Font("Harlow Solid Italic", 20.25!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.cmd_exit.ForeColor = System.Drawing.Color.White
        Me.cmd_exit.Location = New System.Drawing.Point(257, 419)
        Me.cmd_exit.Name = "cmd_exit"
        Me.cmd_exit.Size = New System.Drawing.Size(243, 50)
        Me.cmd_exit.TabIndex = 10
        Me.cmd_exit.Text = "Spiel Verlassen"
        Me.cmd_exit.UseVisualStyleBackColor = True
        '
        'GameStart_timer
        '
        Me.GameStart_timer.Interval = 2000
        '
        'input_winpunkte
        '
        Me.input_winpunkte.BackColor = System.Drawing.Color.Black
        Me.input_winpunkte.ForeColor = System.Drawing.Color.Red
        Me.input_winpunkte.Location = New System.Drawing.Point(590, 374)
        Me.input_winpunkte.Name = "input_winpunkte"
        Me.input_winpunkte.ScrollBars = System.Windows.Forms.RichTextBoxScrollBars.None
        Me.input_winpunkte.Size = New System.Drawing.Size(89, 23)
        Me.input_winpunkte.TabIndex = 11
        Me.input_winpunkte.Text = "3"
        Me.input_winpunkte.Visible = False
        '
        'settings_lbl_winpunkte2
        '
        Me.settings_lbl_winpunkte2.AutoSize = True
        Me.settings_lbl_winpunkte2.Font = New System.Drawing.Font("Harlow Solid Italic", 15.75!, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.settings_lbl_winpunkte2.ForeColor = System.Drawing.Color.White
        Me.settings_lbl_winpunkte2.Location = New System.Drawing.Point(546, 315)
        Me.settings_lbl_winpunkte2.Name = "settings_lbl_winpunkte2"
        Me.settings_lbl_winpunkte2.Size = New System.Drawing.Size(157, 26)
        Me.settings_lbl_winpunkte2.TabIndex = 12
        Me.settings_lbl_winpunkte2.Text = "um zu Gewinnen?"
        Me.settings_lbl_winpunkte2.Visible = False
        '
        'settings_lbl_winpunkte1
        '
        Me.settings_lbl_winpunkte1.AutoSize = True
        Me.settings_lbl_winpunkte1.Font = New System.Drawing.Font("Harlow Solid Italic", 15.75!, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.settings_lbl_winpunkte1.ForeColor = System.Drawing.Color.White
        Me.settings_lbl_winpunkte1.Location = New System.Drawing.Point(506, 289)
        Me.settings_lbl_winpunkte1.Name = "settings_lbl_winpunkte1"
        Me.settings_lbl_winpunkte1.Size = New System.Drawing.Size(269, 26)
        Me.settings_lbl_winpunkte1.TabIndex = 12
        Me.settings_lbl_winpunkte1.Text = "Wieviele Punkte Braucht man"
        Me.settings_lbl_winpunkte1.Visible = False
        '
        'cmd_settings_exit
        '
        Me.cmd_settings_exit.FlatAppearance.BorderColor = System.Drawing.Color.Red
        Me.cmd_settings_exit.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.cmd_settings_exit.Font = New System.Drawing.Font("Harlow Solid Italic", 20.25!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.cmd_settings_exit.ForeColor = System.Drawing.Color.White
        Me.cmd_settings_exit.Location = New System.Drawing.Point(257, 419)
        Me.cmd_settings_exit.Name = "cmd_settings_exit"
        Me.cmd_settings_exit.Size = New System.Drawing.Size(243, 50)
        Me.cmd_settings_exit.TabIndex = 13
        Me.cmd_settings_exit.Text = "Zurück ins Menü"
        Me.cmd_settings_exit.UseVisualStyleBackColor = True
        Me.cmd_settings_exit.Visible = False
        '
        'lbl_bWinLos
        '
        Me.lbl_bWinLos.AutoSize = True
        Me.lbl_bWinLos.Font = New System.Drawing.Font("Harlow Solid Italic", 48.0!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lbl_bWinLos.ForeColor = System.Drawing.Color.Red
        Me.lbl_bWinLos.Location = New System.Drawing.Point(467, 45)
        Me.lbl_bWinLos.Name = "lbl_bWinLos"
        Me.lbl_bWinLos.Size = New System.Drawing.Size(101, 81)
        Me.lbl_bWinLos.TabIndex = 14
        Me.lbl_bWinLos.Text = "__"
        Me.lbl_bWinLos.Visible = False
        '
        'lbl_AWinLos
        '
        Me.lbl_AWinLos.AutoSize = True
        Me.lbl_AWinLos.Font = New System.Drawing.Font("Harlow Solid Italic", 48.0!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lbl_AWinLos.ForeColor = System.Drawing.Color.Red
        Me.lbl_AWinLos.Location = New System.Drawing.Point(12, 45)
        Me.lbl_AWinLos.Name = "lbl_AWinLos"
        Me.lbl_AWinLos.Size = New System.Drawing.Size(101, 81)
        Me.lbl_AWinLos.TabIndex = 15
        Me.lbl_AWinLos.Text = "__"
        Me.lbl_AWinLos.Visible = False
        '
        'lbl_UpDown
        '
        Me.lbl_UpDown.AutoSize = True
        Me.lbl_UpDown.Font = New System.Drawing.Font("Harlow Solid Italic", 20.25!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lbl_UpDown.ForeColor = System.Drawing.Color.Red
        Me.lbl_UpDown.Location = New System.Drawing.Point(615, 92)
        Me.lbl_UpDown.Name = "lbl_UpDown"
        Me.lbl_UpDown.Size = New System.Drawing.Size(0, 34)
        Me.lbl_UpDown.TabIndex = 16
        '
        'pic_arrows
        '
        Me.pic_arrows.Image = CType(resources.GetObject("pic_arrows.Image"), System.Drawing.Image)
        Me.pic_arrows.InitialImage = CType(resources.GetObject("pic_arrows.InitialImage"), System.Drawing.Image)
        Me.pic_arrows.Location = New System.Drawing.Point(597, 84)
        Me.pic_arrows.Name = "pic_arrows"
        Me.pic_arrows.Size = New System.Drawing.Size(106, 161)
        Me.pic_arrows.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
        Me.pic_arrows.TabIndex = 17
        Me.pic_arrows.TabStop = False
        Me.pic_arrows.Visible = False
        '
        'pic_ws
        '
        Me.pic_ws.Image = CType(resources.GetObject("pic_ws.Image"), System.Drawing.Image)
        Me.pic_ws.Location = New System.Drawing.Point(95, 75)
        Me.pic_ws.Name = "pic_ws"
        Me.pic_ws.Size = New System.Drawing.Size(106, 161)
        Me.pic_ws.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom
        Me.pic_ws.TabIndex = 18
        Me.pic_ws.TabStop = False
        Me.pic_ws.Visible = False
        '
        'timer_point
        '
        Me.timer_point.Interval = 2000
        '
        'settings_lbl_speed1
        '
        Me.settings_lbl_speed1.AutoSize = True
        Me.settings_lbl_speed1.Font = New System.Drawing.Font("Harlow Solid Italic", 15.75!, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.settings_lbl_speed1.ForeColor = System.Drawing.Color.White
        Me.settings_lbl_speed1.Location = New System.Drawing.Point(15, 289)
        Me.settings_lbl_speed1.Name = "settings_lbl_speed1"
        Me.settings_lbl_speed1.Size = New System.Drawing.Size(226, 26)
        Me.settings_lbl_speed1.TabIndex = 19
        Me.settings_lbl_speed1.Text = "Geschwindigkeit des Balls"
        Me.settings_lbl_speed1.Visible = False
        '
        'input_speed
        '
        Me.input_speed.BackColor = System.Drawing.Color.Black
        Me.input_speed.ForeColor = System.Drawing.Color.Red
        Me.input_speed.Location = New System.Drawing.Point(73, 374)
        Me.input_speed.Name = "input_speed"
        Me.input_speed.ScrollBars = System.Windows.Forms.RichTextBoxScrollBars.None
        Me.input_speed.Size = New System.Drawing.Size(89, 23)
        Me.input_speed.TabIndex = 20
        Me.input_speed.Text = "2"
        Me.input_speed.Visible = False
        '
        'settings_lbl_playerspeed
        '
        Me.settings_lbl_playerspeed.AutoSize = True
        Me.settings_lbl_playerspeed.Font = New System.Drawing.Font("Harlow Solid Italic", 15.75!, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.settings_lbl_playerspeed.ForeColor = System.Drawing.Color.White
        Me.settings_lbl_playerspeed.Location = New System.Drawing.Point(274, 289)
        Me.settings_lbl_playerspeed.Name = "settings_lbl_playerspeed"
        Me.settings_lbl_playerspeed.Size = New System.Drawing.Size(241, 26)
        Me.settings_lbl_playerspeed.TabIndex = 21
        Me.settings_lbl_playerspeed.Text = "Geschwindigkeit der Spieler"
        Me.settings_lbl_playerspeed.Visible = False
        '
        'input_playerspeed
        '
        Me.input_playerspeed.BackColor = System.Drawing.Color.Black
        Me.input_playerspeed.ForeColor = System.Drawing.Color.Red
        Me.input_playerspeed.Location = New System.Drawing.Point(339, 374)
        Me.input_playerspeed.Name = "input_playerspeed"
        Me.input_playerspeed.ScrollBars = System.Windows.Forms.RichTextBoxScrollBars.None
        Me.input_playerspeed.Size = New System.Drawing.Size(89, 23)
        Me.input_playerspeed.TabIndex = 22
        Me.input_playerspeed.Text = "2"
        Me.input_playerspeed.Visible = False
        '
        'cmd_backtomenu
        '
        Me.cmd_backtomenu.BackColor = System.Drawing.Color.Black
        Me.cmd_backtomenu.FlatAppearance.BorderColor = System.Drawing.Color.Red
        Me.cmd_backtomenu.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.cmd_backtomenu.Font = New System.Drawing.Font("Harlow Solid Italic", 14.25!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.cmd_backtomenu.ForeColor = System.Drawing.Color.White
        Me.cmd_backtomenu.Location = New System.Drawing.Point(279, 9)
        Me.cmd_backtomenu.Name = "cmd_backtomenu"
        Me.cmd_backtomenu.Size = New System.Drawing.Size(165, 34)
        Me.cmd_backtomenu.TabIndex = 23
        Me.cmd_backtomenu.Text = "Zurück"
        Me.cmd_backtomenu.UseVisualStyleBackColor = False
        Me.cmd_backtomenu.Visible = False
        '
        'cmd_singleplayer
        '
        Me.cmd_singleplayer.FlatAppearance.BorderColor = System.Drawing.Color.Red
        Me.cmd_singleplayer.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.cmd_singleplayer.Font = New System.Drawing.Font("Harlow Solid Italic", 20.25!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.cmd_singleplayer.ForeColor = System.Drawing.Color.White
        Me.cmd_singleplayer.Location = New System.Drawing.Point(52, 275)
        Me.cmd_singleplayer.Name = "cmd_singleplayer"
        Me.cmd_singleplayer.Size = New System.Drawing.Size(243, 50)
        Me.cmd_singleplayer.TabIndex = 24
        Me.cmd_singleplayer.Text = "Einzelspieler"
        Me.cmd_singleplayer.UseVisualStyleBackColor = True
        Me.cmd_singleplayer.Visible = False
        '
        'cmd_multiplayer
        '
        Me.cmd_multiplayer.FlatAppearance.BorderColor = System.Drawing.Color.Red
        Me.cmd_multiplayer.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.cmd_multiplayer.Font = New System.Drawing.Font("Harlow Solid Italic", 20.25!, CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle), System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.cmd_multiplayer.ForeColor = System.Drawing.Color.White
        Me.cmd_multiplayer.Location = New System.Drawing.Point(486, 275)
        Me.cmd_multiplayer.Name = "cmd_multiplayer"
        Me.cmd_multiplayer.Size = New System.Drawing.Size(243, 50)
        Me.cmd_multiplayer.TabIndex = 25
        Me.cmd_multiplayer.Text = "Mehrspieler"
        Me.cmd_multiplayer.UseVisualStyleBackColor = True
        Me.cmd_multiplayer.Visible = False
        '
        'ck_hindernis
        '
        Me.ck_hindernis.Appearance = System.Windows.Forms.Appearance.Button
        Me.ck_hindernis.AutoSize = True
        Me.ck_hindernis.FlatStyle = System.Windows.Forms.FlatStyle.Flat
        Me.ck_hindernis.Font = New System.Drawing.Font("Harlow Solid Italic", 20.25!, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.ck_hindernis.ForeColor = System.Drawing.Color.White
        Me.ck_hindernis.Location = New System.Drawing.Point(62, 425)
        Me.ck_hindernis.Name = "ck_hindernis"
        Me.ck_hindernis.Size = New System.Drawing.Size(139, 44)
        Me.ck_hindernis.TabIndex = 26
        Me.ck_hindernis.Text = "Hindernis"
        Me.ck_hindernis.UseVisualStyleBackColor = True
        Me.ck_hindernis.Visible = False
        '
        'hindernis
        '
        Me.hindernis.AutoSize = True
        Me.hindernis.BackColor = System.Drawing.Color.FromArgb(CType(CType(255, Byte), Integer), CType(CType(128, Byte), Integer), CType(CType(128, Byte), Integer))
        Me.hindernis.Font = New System.Drawing.Font("Microsoft Sans Serif", 12.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.hindernis.ForeColor = System.Drawing.Color.White
        Me.hindernis.Location = New System.Drawing.Point(385, 9)
        Me.hindernis.MaximumSize = New System.Drawing.Size(20, 180)
        Me.hindernis.MinimumSize = New System.Drawing.Size(20, 180)
        Me.hindernis.Name = "hindernis"
        Me.hindernis.Size = New System.Drawing.Size(20, 180)
        Me.hindernis.TabIndex = 27
        Me.hindernis.Text = "__"
        Me.hindernis.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        Me.hindernis.Visible = False
        '
        'frm_pong
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.BackColor = System.Drawing.Color.Black
        Me.ClientSize = New System.Drawing.Size(784, 561)
        Me.Controls.Add(Me.hindernis)
        Me.Controls.Add(Me.ck_hindernis)
        Me.Controls.Add(Me.cmd_multiplayer)
        Me.Controls.Add(Me.cmd_singleplayer)
        Me.Controls.Add(Me.cmd_backtomenu)
        Me.Controls.Add(Me.input_playerspeed)
        Me.Controls.Add(Me.settings_lbl_playerspeed)
        Me.Controls.Add(Me.input_speed)
        Me.Controls.Add(Me.settings_lbl_speed1)
        Me.Controls.Add(Me.pic_ws)
        Me.Controls.Add(Me.pic_arrows)
        Me.Controls.Add(Me.lbl_UpDown)
        Me.Controls.Add(Me.lbl_AWinLos)
        Me.Controls.Add(Me.lbl_bWinLos)
        Me.Controls.Add(Me.cmd_settings_exit)
        Me.Controls.Add(Me.settings_lbl_winpunkte1)
        Me.Controls.Add(Me.settings_lbl_winpunkte2)
        Me.Controls.Add(Me.input_winpunkte)
        Me.Controls.Add(Me.cmd_exit)
        Me.Controls.Add(Me.cmd_settings)
        Me.Controls.Add(Me.cmd_LoadGame)
        Me.Controls.Add(Me.menu_byalex)
        Me.Controls.Add(Me.menu_title)
        Me.Controls.Add(Me.lbl_punkte_b)
        Me.Controls.Add(Me.lbl_punkte_a)
        Me.Controls.Add(Me.ball_pos)
        Me.Controls.Add(Me.spieler_a)
        Me.Controls.Add(Me.spieler_b)
        Me.Controls.Add(Me.ball)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow
        Me.KeyPreview = True
        Me.Name = "frm_pong"
        Me.Text = "Pong By Alex Bruksch"
        CType(Me.pic_arrows, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.pic_ws, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents ball As Label
    Friend WithEvents spieler_b As Label
    Friend WithEvents spieler_a As Label
    Public WithEvents sleep As Timer
    Friend WithEvents ball_pos As Label
    Friend WithEvents lbl_punkte_a As Label
    Friend WithEvents lbl_punkte_b As Label
    Friend WithEvents menu_title As Label
    Friend WithEvents menu_byalex As Label
    Friend WithEvents cmd_LoadGame As Button
    Friend WithEvents cmd_settings As Button
    Friend WithEvents cmd_exit As Button
    Friend WithEvents GameStart_timer As Timer
    Friend WithEvents input_winpunkte As RichTextBox
    Friend WithEvents settings_lbl_winpunkte2 As Label
    Friend WithEvents settings_lbl_winpunkte1 As Label
    Friend WithEvents cmd_settings_exit As Button
    Friend WithEvents lbl_bWinLos As Label
    Friend WithEvents lbl_AWinLos As Label
    Friend WithEvents lbl_UpDown As Label
    Friend WithEvents pic_arrows As PictureBox
    Friend WithEvents pic_ws As PictureBox
    Friend WithEvents timer_point As Timer
    Friend WithEvents settings_lbl_speed1 As Label
    Friend WithEvents input_speed As RichTextBox
    Friend WithEvents settings_lbl_playerspeed As Label
    Friend WithEvents input_playerspeed As RichTextBox
    Friend WithEvents cmd_backtomenu As Button
    Friend WithEvents cmd_singleplayer As Button
    Friend WithEvents cmd_multiplayer As Button
    Friend WithEvents ck_hindernis As CheckBox
    Friend WithEvents hindernis As Label
End Class
