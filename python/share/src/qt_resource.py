import asyncio
import hashlib
import os
from pathlib import Path
from typing import Callable, Optional
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase, QIcon, QPixmap
from PyQt5.QtWidgets import QLayout, QWidget, QPushButton, QLabel, QCheckBox, QDoubleSpinBox
import async_networking

from item import MarketItem
import definitions
import logger

fontSystemHudNormal: QFont
fontSystemHudBold: QFont
iconDelete: QIcon
iconFavDisabled: QIcon
iconFavEnabled: QIcon

def loadAppResources():
    global fontSystemHudNormal, fontSystemHudBold
    loadIcons()
    fontSystemHudNormal = loadFont(os.path.join(definitions.PATH_DIST_ASSETS, "fonts", "SystemHud-Normal.ttf"), 15, QFont.Weight.Normal)
    fontSystemHudBold = loadFont(os.path.join(definitions.PATH_DIST_ASSETS, "fonts", "SystemHud-Normal.ttf"), 15, QFont.Weight.Bold)

def loadIcons():
    global iconDelete
    global iconFavDisabled
    global iconFavEnabled
    iconDelete = QIcon(os.path.join(definitions.PATH_DIST_ASSETS, "icons_market_engine", "delete.png"))
    iconFavDisabled = QIcon(os.path.join(definitions.PATH_DIST_ASSETS, "icons_market_engine", "fav_disabled.png"))
    iconFavEnabled = QIcon(os.path.join(definitions.PATH_DIST_ASSETS, "icons_market_engine", "fav_enabled.png"))

def loadFont(path: str, size: int, weight: int) -> QFont:
    fontID = QFontDatabase.addApplicationFont(path)
    if fontID == -1:
        logger.sendMessage(f"ERROR! Font not loaded {path}")
        return QFont()
    fontFamily = QFontDatabase.applicationFontFamilies(fontID)[0]
    font: QFont = QFont(fontFamily, size)
    font.setWeight(weight)
    logger.sendMessage("Loaded font: " + fontFamily)
    return font

def getSkinIcon(item: MarketItem, callback: Callable[[QIcon], None]):
    imageURL = item.imageUrl
    cachePath = getSkinIconCachePath(imageURL)
    if os.path.exists(cachePath): 
        callback(QIcon(str(cachePath)))
        return
    
    asyncio.ensure_future(async_networking.fetchCacheContents(imageURL, cachePath, lambda cachePath: callback(QIcon(str(cachePath)))))

def getSkinIconCachePath(url: str):
    urlHash = hashlib.md5(url.encode()).hexdigest()
    return definitions.PATH_DATA_CLIENT_CACHE_DIR / (urlHash + ".png")

def createWidget(objectName: str, layout: QLayout, alignment: Optional[Qt.AlignmentFlag] = None, styleSheet: str = ""):
    widget: QWidget = QWidget()
    widget.setLayout(layout)
    widget.setObjectName(objectName)
    if alignment != None:
        widget.layout().setAlignment(alignment)
    if styleSheet != "":
        widget.setStyleSheet(styleSheet)
    return widget

def createLabel(objectName: str, text: str, font: QFont, alignment: Optional[Qt.AlignmentFlag] = None, styleSheet: str = ""):
    label = QLabel()
    label.setObjectName(objectName)
    label.setText(text)
    label.setFont(font)
    if alignment != None:
        label.setAlignment(alignment)
    if styleSheet != "":
        label.setStyleSheet(styleSheet)
    return label
    
def createButton(objectName: str, text: str, font: QFont, styleSheet: str = ""):
    button = QPushButton()
    button.setObjectName(objectName)
    button.setText(text)
    button.setFont(font)
    if styleSheet != "":
        button.setStyleSheet(styleSheet)
    return button

def createCheckbox(objectName: str, text: str, font: QFont, checked: bool):
    checkBox = QCheckBox()
    checkBox.setObjectName(objectName)
    checkBox.setText(text)
    checkBox.setFont(font)
    checkBox.setChecked(checked)
    return checkBox

def createDoubleSpinBox(objectName: str, prefix: str, suffix: str, font: QFont, rangeMin: float, rangeMax: float):
    spinBox = QDoubleSpinBox()
    spinBox.setObjectName(objectName)
    spinBox.setPrefix(prefix)
    spinBox.setSuffix(suffix)
    spinBox.setFont(font)
    spinBox.setRange(rangeMin, rangeMax)
    return spinBox

def clearWidget(widget: QWidget):
    while widget.layout().count():
        child = widget.layout().takeAt(0)
        if child.widget():
            child.widget().deleteLater()
