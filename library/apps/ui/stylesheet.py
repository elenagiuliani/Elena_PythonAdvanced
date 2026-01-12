"""
Content  : theme.py
                Define the stylesheet for the UI

Date     : 2026-01-05

license  : MIT
Author   : Elena Giuliani
email    : elenagiuliani94@outlook.it
"""
PALETTE = {
            'my_white'    : 'rgb(240, 240, 240)',
            'my_black'    : 'rgb(24, 25, 28)',

            'dark_green'  : 'rgb(31, 49, 0)',
            'light_green' : 'rgb(71, 89, 30)',
            }

def get_stylesheet():
 return f"""
        QWidget {{
                color: {PALETTE['my_white']}; /* PUSH BTN TEXT COLOR */
                background-color: rgb(28, 29, 32); /* WIDGETS BACKGROUND COLOR */
                }}

        /* PUSH BTN */
        QPushButton:hover {{background-color: {PALETTE['dark_green']};}}
        QPushButton:checked {{background-color: {PALETTE['light_green']};}}
        QPushButton:disabled {{color: rgb(100, 100, 100);}} /* PUSH BTN TEXT COLOR, WHEN DISABLED */
        QPushButton {{ color: {PALETTE['my_white']}; }}

        /* TABS */
        QTabBar::tab:hover {{background-color: {PALETTE['dark_green']};}}
        QTabBar::tab:selected  {{background-color: {PALETTE['light_green']};}}

        
        /* *************************************************************
        /* LINE 
        4 is for horizontal line (5 for vertical line)*/
        QFrame[frameShape="4"]{{
                                background-color: rgb(100, 100, 100);
                                max-height: 1px;
                                border: none;
                                }}
        
        QFrame[frameShape="5"]{{
                                background-color: {PALETTE['my_white']};
                                max-width: 1px;
                                border: none;
                                }}

                                
        /* *************************************************************
        /* SCROLL BAR */
        QScrollBar:vertical {{
                            background: transparent;
                            width: 15px;
                            }}

        /* LIST WIDGET */
        QListWidget::item:disabled {{color: rgb(100, 100, 100); }}
        QListWidget::item:selected {{
                                    background-color: rgb(50, 50, 50); 
                                    color: white;
                                    border-left: 0px;
                                    }}

        /* *************************************************************
        /* RADIO BUTTONS */
        QRadioButton::indicator {{
                                width: 14px;
                                height: 14px;
                                }}

        /* UNCHECKED CIRCLE */
        QRadioButton::indicator:unchecked {{
                                        border: 1px solid #666;
                                        border-radius: 7px;
                                        background: none;
                                        }}

        /* CHECKED DOT */
        QRadioButton::indicator:checked {{
                                        border: 1px solid #666;
                                        border-radius: 7px;
                                        background-color: {PALETTE['light_green']}; /* DOT COLOR HERE */
                                        }}
        """
