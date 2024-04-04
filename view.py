import flet as ft

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.window_height = 600
        self.page.window_width = 850
        self.page.title = "SpellChecker"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("SpellChecker", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.add(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Row 1
        self._txtLanguage = ft.Dropdown(
            label="Select Language",
            width=800,
            options=[
                ft.dropdown.Option("italian"),
                ft.dropdown.Option("english"),
                ft.dropdown.Option("spanish"), 
            ]  
        )
        __row1 = ft.Row([self._txtLanguage], alignment=ft.MainAxisAlignment.START)
        
        # Row 2
        self._txtModality = ft.Dropdown(
            label="Search Modality",
            width=200,
            options=[
                ft.dropdown.Option("Default"),
                ft.dropdown.Option("Linear"),
                ft.dropdown.Option("Dichotomic"), 
            ]  
        )
        self._txtSentence = ft.TextField(label="Add your sentence here", width=460) 
        __btn = ft.ElevatedButton("Spell Check", on_click=self.__controller.handleSentence)                       
        __row2 = ft.Row([self._txtModality, self._txtSentence, __btn], alignment=ft.MainAxisAlignment.START)
        
        # Row 3
        self._lvOut = ft.ListView()
        __row3 = ft.Row([self._lvOut], alignment=ft.MainAxisAlignment.START)
        
        self.page.add(__row1, __row2, __row3)
        self.page.update()

    def createListView(self, paroleErrate, tempoRichiesto):
        self._lvOut.controls.clear()
        self._lvOut.controls.append(ft.Text(f'Frase inserita: {self._txtSentence.value}'))
        self._lvOut.controls.append(ft.Text(f'{paroleErrate}'))
        self._lvOut.controls.append(ft.Text(f'Tempo richiesto dalla ricerca: {tempoRichiesto} secondi'))
        self._txtLanguage.value = ''
        self._txtModality.value = ''
        self._txtSentence.value = ''
        self.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
