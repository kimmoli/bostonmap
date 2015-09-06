TARGET = bostonmap
TEMPLATE = aux

system(kmap2qmap boston.kmap boston.qmap)

map.files = boston.qmap
map.path = /usr/share/qt5/keymaps/

INSTALLS = map

OTHER_FILES += \
    rpm/bostonmap.spec \
    boston.kmap
