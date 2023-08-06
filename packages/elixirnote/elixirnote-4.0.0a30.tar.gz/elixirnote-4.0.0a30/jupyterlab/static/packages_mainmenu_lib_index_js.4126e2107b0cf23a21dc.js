"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_mainmenu_lib_index_js"],{

/***/ "../../packages/mainmenu/lib/edit.js":
/*!*******************************************!*\
  !*** ../../packages/mainmenu/lib/edit.js ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "EditMenu": () => (/* binding */ EditMenu)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


/**
 * An extensible Edit menu for the application.
 */
class EditMenu extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.RankedMenu {
    /**
     * Construct the edit menu.
     */
    constructor(options) {
        super(options);
        this.undoers = {
            redo: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand(),
            undo: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand()
        };
        this.clearers = {
            clearAll: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand(),
            clearCurrent: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand()
        };
        this.goToLiners = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand();
    }
}


/***/ }),

/***/ "../../packages/mainmenu/lib/file.js":
/*!*******************************************!*\
  !*** ../../packages/mainmenu/lib/file.js ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "FileMenu": () => (/* binding */ FileMenu)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/**
 * An extensible FileMenu for the application.
 */
class FileMenu extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.RankedMenu {
    constructor(options) {
        super(options);
        this.quitEntry = false;
        this.closeAndCleaners = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.SemanticCommand();
        this.consoleCreators = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.SemanticCommand();
    }
    /**
     * The New submenu.
     */
    get newMenu() {
        var _a, _b;
        if (!this._newMenu) {
            this._newMenu =
                (_b = (_a = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_1__.find)(this.items, menu => { var _a; return ((_a = menu.submenu) === null || _a === void 0 ? void 0 : _a.id) === 'jp-mainmenu-file-new'; })) === null || _a === void 0 ? void 0 : _a.submenu) !== null && _b !== void 0 ? _b : new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.RankedMenu({
                    commands: this.commands
                });
        }
        return this._newMenu;
    }
    /**
     * Dispose of the resources held by the file menu.
     */
    dispose() {
        var _a;
        (_a = this._newMenu) === null || _a === void 0 ? void 0 : _a.dispose();
        super.dispose();
    }
}


/***/ }),

/***/ "../../packages/mainmenu/lib/help.js":
/*!*******************************************!*\
  !*** ../../packages/mainmenu/lib/help.js ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "HelpMenu": () => (/* binding */ HelpMenu)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


/**
 * An extensible Help menu for the application.
 */
class HelpMenu extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.RankedMenu {
    /**
     * Construct the help menu.
     */
    constructor(options) {
        super(options);
        this.getKernel = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand();
    }
}


/***/ }),

/***/ "../../packages/mainmenu/lib/index.js":
/*!********************************************!*\
  !*** ../../packages/mainmenu/lib/index.js ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "EditMenu": () => (/* reexport safe */ _edit__WEBPACK_IMPORTED_MODULE_1__.EditMenu),
/* harmony export */   "FileMenu": () => (/* reexport safe */ _file__WEBPACK_IMPORTED_MODULE_2__.FileMenu),
/* harmony export */   "HelpMenu": () => (/* reexport safe */ _help__WEBPACK_IMPORTED_MODULE_3__.HelpMenu),
/* harmony export */   "IJupyterLabMenu": () => (/* reexport safe */ _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_10__.IRankedMenu),
/* harmony export */   "IMainMenu": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_9__.IMainMenu),
/* harmony export */   "JupyterLabMenu": () => (/* reexport safe */ _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_10__.RankedMenu),
/* harmony export */   "KernelMenu": () => (/* reexport safe */ _kernel__WEBPACK_IMPORTED_MODULE_4__.KernelMenu),
/* harmony export */   "MainMenu": () => (/* reexport safe */ _mainmenu__WEBPACK_IMPORTED_MODULE_0__.MainMenu),
/* harmony export */   "RunMenu": () => (/* reexport safe */ _run__WEBPACK_IMPORTED_MODULE_5__.RunMenu),
/* harmony export */   "SettingsMenu": () => (/* reexport safe */ _settings__WEBPACK_IMPORTED_MODULE_6__.SettingsMenu),
/* harmony export */   "TabsMenu": () => (/* reexport safe */ _tabs__WEBPACK_IMPORTED_MODULE_8__.TabsMenu),
/* harmony export */   "ViewMenu": () => (/* reexport safe */ _view__WEBPACK_IMPORTED_MODULE_7__.ViewMenu)
/* harmony export */ });
/* harmony import */ var _mainmenu__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./mainmenu */ "../../packages/mainmenu/lib/mainmenu.js");
/* harmony import */ var _edit__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./edit */ "../../packages/mainmenu/lib/edit.js");
/* harmony import */ var _file__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./file */ "../../packages/mainmenu/lib/file.js");
/* harmony import */ var _help__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./help */ "../../packages/mainmenu/lib/help.js");
/* harmony import */ var _kernel__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./kernel */ "../../packages/mainmenu/lib/kernel.js");
/* harmony import */ var _run__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./run */ "../../packages/mainmenu/lib/run.js");
/* harmony import */ var _settings__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./settings */ "../../packages/mainmenu/lib/settings.js");
/* harmony import */ var _view__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./view */ "../../packages/mainmenu/lib/view.js");
/* harmony import */ var _tabs__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./tabs */ "../../packages/mainmenu/lib/tabs.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./tokens */ "../../packages/mainmenu/lib/tokens.js");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_10__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module mainmenu
 */










/**
 * @deprecated since version 3.1
 */



/***/ }),

/***/ "../../packages/mainmenu/lib/kernel.js":
/*!*********************************************!*\
  !*** ../../packages/mainmenu/lib/kernel.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "KernelMenu": () => (/* binding */ KernelMenu)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


/**
 * An extensible Kernel menu for the application.
 */
class KernelMenu extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.RankedMenu {
    /**
     * Construct the kernel menu.
     */
    constructor(options) {
        super(options);
        this.kernelUsers = {
            changeKernel: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand(),
            clearWidget: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand(),
            interruptKernel: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand(),
            reconnectToKernel: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand(),
            restartKernel: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand(),
            shutdownKernel: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand()
        };
    }
}


/***/ }),

/***/ "../../packages/mainmenu/lib/mainmenu.js":
/*!***********************************************!*\
  !*** ../../packages/mainmenu/lib/mainmenu.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "MainMenu": () => (/* binding */ MainMenu)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _edit__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./edit */ "../../packages/mainmenu/lib/edit.js");
/* harmony import */ var _file__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./file */ "../../packages/mainmenu/lib/file.js");
/* harmony import */ var _help__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./help */ "../../packages/mainmenu/lib/help.js");
/* harmony import */ var _kernel__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./kernel */ "../../packages/mainmenu/lib/kernel.js");
/* harmony import */ var _run__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./run */ "../../packages/mainmenu/lib/run.js");
/* harmony import */ var _settings__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./settings */ "../../packages/mainmenu/lib/settings.js");
/* harmony import */ var _tabs__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./tabs */ "../../packages/mainmenu/lib/tabs.js");
/* harmony import */ var _view__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./view */ "../../packages/mainmenu/lib/view.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.











/**
 * The main menu class.  It is intended to be used as a singleton.
 */
class MainMenu extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.MenuBar {
    /**
     * Construct the main menu bar.
     */
    constructor(commands) {
        super();
        this._items = [];
        this._commands = commands;
    }
    /**
     * The application "Edit" menu.
     */
    get editMenu() {
        if (!this._editMenu) {
            this._editMenu = new _edit__WEBPACK_IMPORTED_MODULE_3__.EditMenu({
                commands: this._commands,
                rank: 2,
                renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
            });
        }
        return this._editMenu;
    }
    /**
     * The application "File" menu.
     */
    get fileMenu() {
        if (!this._fileMenu) {
            this._fileMenu = new _file__WEBPACK_IMPORTED_MODULE_4__.FileMenu({
                commands: this._commands,
                rank: 1,
                renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
            });
        }
        return this._fileMenu;
    }
    /**
     * The application "Help" menu.
     */
    get helpMenu() {
        if (!this._helpMenu) {
            this._helpMenu = new _help__WEBPACK_IMPORTED_MODULE_5__.HelpMenu({
                commands: this._commands,
                rank: 1000,
                renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
            });
        }
        return this._helpMenu;
    }
    /**
     * The application "Kernel" menu.
     */
    get kernelMenu() {
        if (!this._kernelMenu) {
            this._kernelMenu = new _kernel__WEBPACK_IMPORTED_MODULE_6__.KernelMenu({
                commands: this._commands,
                rank: 5,
                renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
            });
        }
        return this._kernelMenu;
    }
    /**
     * The application "Run" menu.
     */
    get runMenu() {
        if (!this._runMenu) {
            this._runMenu = new _run__WEBPACK_IMPORTED_MODULE_7__.RunMenu({
                commands: this._commands,
                rank: 4,
                renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
            });
        }
        return this._runMenu;
    }
    /**
     * The application "Settings" menu.
     */
    get settingsMenu() {
        if (!this._settingsMenu) {
            this._settingsMenu = new _settings__WEBPACK_IMPORTED_MODULE_8__.SettingsMenu({
                commands: this._commands,
                rank: 999,
                renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
            });
        }
        return this._settingsMenu;
    }
    /**
     * The application "View" menu.
     */
    get viewMenu() {
        if (!this._viewMenu) {
            this._viewMenu = new _view__WEBPACK_IMPORTED_MODULE_9__.ViewMenu({
                commands: this._commands,
                rank: 3,
                renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
            });
        }
        return this._viewMenu;
    }
    /**
     * The application "Tabs" menu.
     */
    get tabsMenu() {
        if (!this._tabsMenu) {
            this._tabsMenu = new _tabs__WEBPACK_IMPORTED_MODULE_10__.TabsMenu({
                commands: this._commands,
                rank: 500,
                renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
            });
        }
        return this._tabsMenu;
    }
    /**
     * Add a new menu to the main menu bar.
     */
    addMenu(menu, options = {}) {
        if (_lumino_algorithm__WEBPACK_IMPORTED_MODULE_1__.ArrayExt.firstIndexOf(this.menus, menu) > -1) {
            return;
        }
        // override default renderer with svg-supporting renderer
        _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.overrideDefaultRenderer(menu);
        const rank = 'rank' in options
            ? options.rank
            : 'rank' in menu
                ? menu.rank
                : _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.IRankedMenu.DEFAULT_RANK;
        const rankItem = { menu, rank };
        const index = _lumino_algorithm__WEBPACK_IMPORTED_MODULE_1__.ArrayExt.upperBound(this._items, rankItem, Private.itemCmp);
        // Upon disposal, remove the menu and its rank reference.
        menu.disposed.connect(this._onMenuDisposed, this);
        _lumino_algorithm__WEBPACK_IMPORTED_MODULE_1__.ArrayExt.insert(this._items, index, rankItem);
        /**
         * Create a new menu.
         */
        this.insertMenu(index, menu);
        // Link the menu to the API - backward compatibility when switching to menu description in settings
        switch (menu.id) {
            case 'jp-mainmenu-file':
                if (!this._fileMenu && menu instanceof _file__WEBPACK_IMPORTED_MODULE_4__.FileMenu) {
                    this._fileMenu = menu;
                }
                break;
            case 'jp-mainmenu-edit':
                if (!this._editMenu && menu instanceof _edit__WEBPACK_IMPORTED_MODULE_3__.EditMenu) {
                    this._editMenu = menu;
                }
                break;
            case 'jp-mainmenu-view':
                if (!this._viewMenu && menu instanceof _view__WEBPACK_IMPORTED_MODULE_9__.ViewMenu) {
                    this._viewMenu = menu;
                }
                break;
            case 'jp-mainmenu-run':
                if (!this._runMenu && menu instanceof _run__WEBPACK_IMPORTED_MODULE_7__.RunMenu) {
                    this._runMenu = menu;
                }
                break;
            case 'jp-mainmenu-kernel':
                if (!this._kernelMenu && menu instanceof _kernel__WEBPACK_IMPORTED_MODULE_6__.KernelMenu) {
                    this._kernelMenu = menu;
                }
                break;
            case 'jp-mainmenu-tabs':
                if (!this._tabsMenu && menu instanceof _tabs__WEBPACK_IMPORTED_MODULE_10__.TabsMenu) {
                    this._tabsMenu = menu;
                }
                break;
            case 'jp-mainmenu-settings':
                if (!this._settingsMenu && menu instanceof _settings__WEBPACK_IMPORTED_MODULE_8__.SettingsMenu) {
                    this._settingsMenu = menu;
                }
                break;
            case 'jp-mainmenu-help':
                if (!this._helpMenu && menu instanceof _help__WEBPACK_IMPORTED_MODULE_5__.HelpMenu) {
                    this._helpMenu = menu;
                }
                break;
        }
    }
    /**
     * Dispose of the resources held by the menu bar.
     */
    dispose() {
        var _a, _b, _c, _d, _e, _f, _g, _h;
        (_a = this._editMenu) === null || _a === void 0 ? void 0 : _a.dispose();
        (_b = this._fileMenu) === null || _b === void 0 ? void 0 : _b.dispose();
        (_c = this._helpMenu) === null || _c === void 0 ? void 0 : _c.dispose();
        (_d = this._kernelMenu) === null || _d === void 0 ? void 0 : _d.dispose();
        (_e = this._runMenu) === null || _e === void 0 ? void 0 : _e.dispose();
        (_f = this._settingsMenu) === null || _f === void 0 ? void 0 : _f.dispose();
        (_g = this._viewMenu) === null || _g === void 0 ? void 0 : _g.dispose();
        (_h = this._tabsMenu) === null || _h === void 0 ? void 0 : _h.dispose();
        super.dispose();
    }
    /**
     * Generate the menu.
     *
     * @param commands The command registry
     * @param options The main menu options.
     * @param trans - The application language translator.
     */
    static generateMenu(commands, options, trans) {
        let menu;
        const { id, label, rank } = options;
        switch (id) {
            case 'jp-mainmenu-file':
                menu = new _file__WEBPACK_IMPORTED_MODULE_4__.FileMenu({
                    commands,
                    rank,
                    renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
                });
                break;
            case 'jp-mainmenu-edit':
                menu = new _edit__WEBPACK_IMPORTED_MODULE_3__.EditMenu({
                    commands,
                    rank,
                    renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
                });
                break;
            case 'jp-mainmenu-view':
                menu = new _view__WEBPACK_IMPORTED_MODULE_9__.ViewMenu({
                    commands,
                    rank,
                    renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
                });
                break;
            case 'jp-mainmenu-run':
                menu = new _run__WEBPACK_IMPORTED_MODULE_7__.RunMenu({
                    commands,
                    rank,
                    renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
                });
                break;
            case 'jp-mainmenu-kernel':
                menu = new _kernel__WEBPACK_IMPORTED_MODULE_6__.KernelMenu({
                    commands,
                    rank,
                    renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
                });
                break;
            case 'jp-mainmenu-tabs':
                menu = new _tabs__WEBPACK_IMPORTED_MODULE_10__.TabsMenu({
                    commands,
                    rank,
                    renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
                });
                break;
            case 'jp-mainmenu-settings':
                menu = new _settings__WEBPACK_IMPORTED_MODULE_8__.SettingsMenu({
                    commands,
                    rank,
                    renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
                });
                break;
            case 'jp-mainmenu-help':
                menu = new _help__WEBPACK_IMPORTED_MODULE_5__.HelpMenu({
                    commands,
                    rank,
                    renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
                });
                break;
            default:
                menu = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.RankedMenu({
                    commands,
                    rank,
                    renderer: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.MenuSvg.defaultRenderer
                });
        }
        if (label) {
            menu.title.label = trans._p('menu', label);
        }
        return menu;
    }
    /**
     * Handle the disposal of a menu.
     */
    _onMenuDisposed(menu) {
        this.removeMenu(menu);
        const index = _lumino_algorithm__WEBPACK_IMPORTED_MODULE_1__.ArrayExt.findFirstIndex(this._items, item => item.menu === menu);
        if (index !== -1) {
            _lumino_algorithm__WEBPACK_IMPORTED_MODULE_1__.ArrayExt.removeAt(this._items, index);
        }
    }
}
/**
 * A namespace for private data.
 */
var Private;
(function (Private) {
    /**
     * A comparator function for menu rank items.
     */
    function itemCmp(first, second) {
        return first.rank - second.rank;
    }
    Private.itemCmp = itemCmp;
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/mainmenu/lib/run.js":
/*!******************************************!*\
  !*** ../../packages/mainmenu/lib/run.js ***!
  \******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "RunMenu": () => (/* binding */ RunMenu)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


/**
 * An extensible Run menu for the application.
 */
class RunMenu extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.RankedMenu {
    /**
     * Construct the run menu.
     */
    constructor(options) {
        super(options);
        this.codeRunners = {
            restart: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand(),
            run: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand(),
            runAll: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand()
        };
    }
}


/***/ }),

/***/ "../../packages/mainmenu/lib/settings.js":
/*!***********************************************!*\
  !*** ../../packages/mainmenu/lib/settings.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "SettingsMenu": () => (/* binding */ SettingsMenu)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * An extensible Settings menu for the application.
 */
class SettingsMenu extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.RankedMenu {
    /**
     * Construct the settings menu.
     */
    constructor(options) {
        super(options);
    }
}


/***/ }),

/***/ "../../packages/mainmenu/lib/tabs.js":
/*!*******************************************!*\
  !*** ../../packages/mainmenu/lib/tabs.js ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TabsMenu": () => (/* binding */ TabsMenu)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * An extensible Tabs menu for the application.
 */
class TabsMenu extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.RankedMenu {
    /**
     * Construct the tabs menu.
     */
    constructor(options) {
        super(options);
    }
}


/***/ }),

/***/ "../../packages/mainmenu/lib/tokens.js":
/*!*********************************************!*\
  !*** ../../packages/mainmenu/lib/tokens.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IMainMenu": () => (/* binding */ IMainMenu)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The main menu token.
 */
const IMainMenu = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/mainmenu:IMainMenu');


/***/ }),

/***/ "../../packages/mainmenu/lib/view.js":
/*!*******************************************!*\
  !*** ../../packages/mainmenu/lib/view.js ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ViewMenu": () => (/* binding */ ViewMenu)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


/**
 * An extensible View menu for the application.
 */
class ViewMenu extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.RankedMenu {
    /**
     * Construct the view menu.
     */
    constructor(options) {
        super(options);
        this.editorViewers = {
            toggleLineNumbers: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand(),
            toggleMatchBrackets: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand(),
            toggleWordWrap: new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.SemanticCommand()
        };
    }
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfbWFpbm1lbnVfbGliX2luZGV4X2pzLjQxMjZlMjEwN2IwY2YyM2EyMWRjLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUVTO0FBQ2I7QUFzQnZEOztHQUVHO0FBQ0ksTUFBTSxRQUFTLFNBQVEsaUVBQVU7SUFDdEM7O09BRUc7SUFDSCxZQUFZLE9BQTZCO1FBQ3ZDLEtBQUssQ0FBQyxPQUFPLENBQUMsQ0FBQztRQUVmLElBQUksQ0FBQyxPQUFPLEdBQUc7WUFDYixJQUFJLEVBQUUsSUFBSSxpRUFBZSxFQUFFO1lBQzNCLElBQUksRUFBRSxJQUFJLGlFQUFlLEVBQUU7U0FDNUIsQ0FBQztRQUVGLElBQUksQ0FBQyxRQUFRLEdBQUc7WUFDZCxRQUFRLEVBQUUsSUFBSSxpRUFBZSxFQUFFO1lBQy9CLFlBQVksRUFBRSxJQUFJLGlFQUFlLEVBQUU7U0FDcEMsQ0FBQztRQUVGLElBQUksQ0FBQyxVQUFVLEdBQUcsSUFBSSxpRUFBZSxFQUFFLENBQUM7SUFDMUMsQ0FBQztDQWdCRjs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDL0RELDBDQUEwQztBQUMxQywyREFBMkQ7QUFFUztBQUMzQjtBQUNjO0FBMkJ2RDs7R0FFRztBQUNJLE1BQU0sUUFBUyxTQUFRLGlFQUFVO0lBQ3RDLFlBQVksT0FBNkI7UUFDdkMsS0FBSyxDQUFDLE9BQU8sQ0FBQyxDQUFDO1FBQ2YsSUFBSSxDQUFDLFNBQVMsR0FBRyxLQUFLLENBQUM7UUFFdkIsSUFBSSxDQUFDLGdCQUFnQixHQUFHLElBQUksaUVBQWUsRUFBRSxDQUFDO1FBQzlDLElBQUksQ0FBQyxlQUFlLEdBQUcsSUFBSSxpRUFBZSxFQUFFLENBQUM7SUFDL0MsQ0FBQztJQUVEOztPQUVHO0lBQ0gsSUFBSSxPQUFPOztRQUNULElBQUksQ0FBQyxJQUFJLENBQUMsUUFBUSxFQUFFO1lBQ2xCLElBQUksQ0FBQyxRQUFRO2dCQUNYLE1BQUMsNkRBQUksQ0FBQyxJQUFJ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Z0MsQ0FBQyxDQUFDOzs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDbEJoRiwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBRVM7QUFDYjtBQVl2RDs7R0FFRztBQUNJLE1BQU0sUUFBUyxTQUFRLGlFQUFVO0lBQ3RDOztPQUVHO0lBQ0gsWUFBWSxPQUE2QjtRQUN2QyxLQUFLLENBQUMsT0FBTyxDQUFDLENBQUM7UUFDZixJQUFJLENBQUMsYUFBYSxHQUFHO1lBQ25CLGlCQUFpQixFQUFFLElBQUksaUVBQWUsRUFBRTtZQUN4QyxtQkFBbUIsRUFBRSxJQUFJLGlFQUFlLEVBQUU7WUFDMUMsY0FBYyxFQUFFLElBQUksaUVBQWUsRUFBRTtTQUN0QyxDQUFDO0lBQ0osQ0FBQztDQU1GIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL21haW5tZW51L3NyYy9lZGl0LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9tYWlubWVudS9zcmMvZmlsZS50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvbWFpbm1lbnUvc3JjL2hlbHAudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL21haW5tZW51L3NyYy9pbmRleC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvbWFpbm1lbnUvc3JjL2tlcm5lbC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvbWFpbm1lbnUvc3JjL21haW5tZW51LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9tYWlubWVudS9zcmMvcnVuLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9tYWlubWVudS9zcmMvc2V0dGluZ3MudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL21haW5tZW51L3NyYy90YWJzLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9tYWlubWVudS9zcmMvdG9rZW5zLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9tYWlubWVudS9zcmMvdmlldy50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElSYW5rZWRNZW51LCBSYW5rZWRNZW51IH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBTZW1hbnRpY0NvbW1hbmQgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5cbi8qKlxuICogQW4gaW50ZXJmYWNlIGZvciBhbiBFZGl0IG1lbnUuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSUVkaXRNZW51IGV4dGVuZHMgSVJhbmtlZE1lbnUge1xuICAvKipcbiAgICogU2VtYW50aWMgY29tbWFuZHMgSVVuZG9lcnMgZm9yIHRoZSBFZGl0IG1lbnUuXG4gICAqL1xuICByZWFkb25seSB1bmRvZXJzOiBJRWRpdE1lbnUuSVVuZG9lcjtcblxuICAvKipcbiAgICogU2VtYW50aWMgY29tbWFuZHMgSUNsZWFyZXJzIGZvciB0aGUgRWRpdCBtZW51LlxuICAgKi9cbiAgcmVhZG9ubHkgY2xlYXJlcnM6IElFZGl0TWVudS5JQ2xlYXJlcjtcblxuICAvKipcbiAgICogU2VtYW50aWMgY29tbWFuZHMgSUdvVG9MaW5lcnMgZm9yIHRoZSBFZGl0IG1lbnUuXG4gICAqL1xuICByZWFkb25seSBnb1RvTGluZXJzOiBTZW1hbnRpY0NvbW1hbmQ7XG59XG5cbi8qKlxuICogQW4gZXh0ZW5zaWJsZSBFZGl0IG1lbnUgZm9yIHRoZSBhcHBsaWNhdGlvbi5cbiAqL1xuZXhwb3J0IGNsYXNzIEVkaXRNZW51IGV4dGVuZHMgUmFua2VkTWVudSBpbXBsZW1lbnRzIElFZGl0TWVudSB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgdGhlIGVkaXQgbWVudS5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IElSYW5rZWRNZW51LklPcHRpb25zKSB7XG4gICAgc3VwZXIob3B0aW9ucyk7XG5cbiAgICB0aGlzLnVuZG9lcnMgPSB7XG4gICAgICByZWRvOiBuZXcgU2VtYW50aWNDb21tYW5kKCksXG4gICAgICB1bmRvOiBuZXcgU2VtYW50aWNDb21tYW5kKClcbiAgICB9O1xuXG4gICAgdGhpcy5jbGVhcmVycyA9IHtcbiAgICAgIGNsZWFyQWxsOiBuZXcgU2VtYW50aWNDb21tYW5kKCksXG4gICAgICBjbGVhckN1cnJlbnQ6IG5ldyBTZW1hbnRpY0NvbW1hbmQoKVxuICAgIH07XG5cbiAgICB0aGlzLmdvVG9MaW5lcnMgPSBuZXcgU2VtYW50aWNDb21tYW5kKCk7XG4gIH1cblxuICAvKipcbiAgICogU2VtYW50aWMgY29tbWFuZHMgSVVuZG9lcnMgZm9yIHRoZSBFZGl0IG1lbnUuXG4gICAqL1xuICByZWFkb25seSB1bmRvZXJzOiBJRWRpdE1lbnUuSVVuZG9lcjtcblxuICAvKipcbiAgICogU2VtYW50aWMgY29tbWFuZHMgSUNsZWFyZXJzIGZvciB0aGUgRWRpdCBtZW51LlxuICAgKi9cbiAgcmVhZG9ubHkgY2xlYXJlcnM6IElFZGl0TWVudS5JQ2xlYXJlcjtcblxuICAvKipcbiAgICogU2VtYW50aWMgY29tbWFuZHMgSUdvVG9MaW5lcnMgZm9yIHRoZSBFZGl0IG1lbnUuXG4gICAqL1xuICByZWFkb25seSBnb1RvTGluZXJzOiBTZW1hbnRpY0NvbW1hbmQ7XG59XG5cbi8qKlxuICogTmFtZXNwYWNlIGZvciBJRWRpdE1lbnVcbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBJRWRpdE1lbnUge1xuICAvKipcbiAgICogSW50ZXJmYWNlIGZvciBhbiBhY3Rpdml0eSB0aGF0IHVzZXMgVW5kby9SZWRvLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJVW5kb2VyIHtcbiAgICAvKipcbiAgICAgKiBBIHNlbWFudGljIGNvbW1hbmQgdG8gZXhlY3V0ZSBhbiB1bmRvIGNvbW1hbmQgZm9yIHRoZSBhY3Rpdml0eS5cbiAgICAgKi9cbiAgICB1bmRvOiBTZW1hbnRpY0NvbW1hbmQ7XG5cbiAgICAvKipcbiAgICAgKiBBIHNlbWFudGljIGNvbW1hbmQgdG8gZXhlY3V0ZSBhIHJlZG8gY29tbWFuZCBmb3IgdGhlIGFjdGl2aXR5LlxuICAgICAqL1xuICAgIHJlZG86IFNlbWFudGljQ29tbWFuZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBJbnRlcmZhY2UgZm9yIGFuIGFjdGl2aXR5IHRoYXQgd2FudHMgdG8gcmVnaXN0ZXIgYSAnQ2xlYXIuLi4nIG1lbnUgaXRlbVxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJQ2xlYXJlciB7XG4gICAgLyoqXG4gICAgICogQSBzZW1hbnRpYyBjb21tYW5kIHRvIGNsZWFyIHRoZSBjdXJyZW50bHkgcG9ydGlvbiBvZiBhY3Rpdml0eS5cbiAgICAgKi9cbiAgICBjbGVhckN1cnJlbnQ6IFNlbWFudGljQ29tbWFuZDtcblxuICAgIC8qKlxuICAgICAqIEEgc2VtYW50aWMgY29tbWFuZCB0byBjbGVhciBhbGwgb2YgYW4gYWN0aXZpdHkuXG4gICAgICovXG4gICAgY2xlYXJBbGw6IFNlbWFudGljQ29tbWFuZDtcbiAgfVxufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBJUmFua2VkTWVudSwgUmFua2VkTWVudSB9IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0IHsgZmluZCB9IGZyb20gJ0BsdW1pbm8vYWxnb3JpdGhtJztcbmltcG9ydCB7IFNlbWFudGljQ29tbWFuZCB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcblxuLyoqXG4gKiBBbiBpbnRlcmZhY2UgZm9yIGEgRmlsZSBtZW51LlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElGaWxlTWVudSBleHRlbmRzIElSYW5rZWRNZW51IHtcbiAgLyoqXG4gICAqIE9wdGlvbiB0byBhZGQgYSBgUXVpdGAgZW50cnkgaW4gdGhlIEZpbGUgbWVudVxuICAgKi9cbiAgcXVpdEVudHJ5OiBib29sZWFuO1xuXG4gIC8qKlxuICAgKiBBIHN1Ym1lbnUgZm9yIGNyZWF0aW5nIG5ldyBmaWxlcy9sYXVuY2hpbmcgbmV3IGFjdGl2aXRpZXMuXG4gICAqL1xuICByZWFkb25seSBuZXdNZW51OiBJUmFua2VkTWVudTtcblxuICAvKipcbiAgICogVGhlIGNsb3NlIGFuZCBjbGVhbnVwIHNlbWFudGljIGNvbW1hbmQuXG4gICAqL1xuICByZWFkb25seSBjbG9zZUFuZENsZWFuZXJzOiBTZW1hbnRpY0NvbW1hbmQ7XG5cbiAgLyoqXG4gICAqIFRoZSBjb25zb2xlIGNyZWF0b3Igc2VtYW50aWMgY29tbWFuZC5cbiAgICovXG4gIHJlYWRvbmx5IGNvbnNvbGVDcmVhdG9yczogU2VtYW50aWNDb21tYW5kO1xufVxuXG4vKipcbiAqIEFuIGV4dGVuc2libGUgRmlsZU1lbnUgZm9yIHRoZSBhcHBsaWNhdGlvbi5cbiAqL1xuZXhwb3J0IGNsYXNzIEZpbGVNZW51IGV4dGVuZHMgUmFua2VkTWVudSBpbXBsZW1lbnRzIElGaWxlTWVudSB7XG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IElSYW5rZWRNZW51LklPcHRpb25zKSB7XG4gICAgc3VwZXIob3B0aW9ucyk7XG4gICAgdGhpcy5xdWl0RW50cnkgPSBmYWxzZTtcblxuICAgIHRoaXMuY2xvc2VBbmRDbGVhbmVycyA9IG5ldyBTZW1hbnRpY0NvbW1hbmQoKTtcbiAgICB0aGlzLmNvbnNvbGVDcmVhdG9ycyA9IG5ldyBTZW1hbnRpY0NvbW1hbmQoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgTmV3IHN1Ym1lbnUuXG4gICAqL1xuICBnZXQgbmV3TWVudSgpOiBSYW5rZWRNZW51IHtcbiAgICBpZiAoIXRoaXMuX25ld01lbnUpIHtcbiAgICAgIHRoaXMuX25ld01lbnUgPVxuICAgICAgICAoZmluZCh0aGlzLml0ZW1zLCBtZW51ID0+IG1lbnUuc3VibWVudT8uaWQgPT09ICdqcC1tYWlubWVudS1maWxlLW5ldycpXG4gICAgICAgICAgPy5zdWJtZW51IGFzIFJhbmtlZE1lbnUpID8/XG4gICAgICAgIG5ldyBSYW5rZWRNZW51KHtcbiAgICAgICAgICBjb21tYW5kczogdGhpcy5jb21tYW5kc1xuICAgICAgICB9KTtcbiAgICB9XG4gICAgcmV0dXJuIHRoaXMuX25ld01lbnU7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGNsb3NlIGFuZCBjbGVhbnVwIHNlbWFudGljIGNvbW1hbmQuXG4gICAqL1xuICByZWFkb25seSBjbG9zZUFuZENsZWFuZXJzOiBTZW1hbnRpY0NvbW1hbmQ7XG5cbiAgLyoqXG4gICAqIFRoZSBjb25zb2xlIGNyZWF0b3Igc2VtYW50aWMgY29tbWFuZC5cbiAgICovXG4gIHJlYWRvbmx5IGNvbnNvbGVDcmVhdG9yczogU2VtYW50aWNDb21tYW5kO1xuXG4gIC8qKlxuICAgKiBEaXNwb3NlIG9mIHRoZSByZXNvdXJjZXMgaGVsZCBieSB0aGUgZmlsZSBtZW51LlxuICAgKi9cbiAgZGlzcG9zZSgpOiB2b2lkIHtcbiAgICB0aGlzLl9uZXdNZW51Py5kaXNwb3NlKCk7XG4gICAgc3VwZXIuZGlzcG9zZSgpO1xuICB9XG5cbiAgLyoqXG4gICAqIE9wdGlvbiB0byBhZGQgYSBgUXVpdGAgZW50cnkgaW4gRmlsZSBtZW51XG4gICAqL1xuICBwdWJsaWMgcXVpdEVudHJ5OiBib29sZWFuO1xuXG4gIHByaXZhdGUgX25ld01lbnU6IFJhbmtlZE1lbnU7XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElSYW5rZWRNZW51LCBSYW5rZWRNZW51IH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBTZW1hbnRpY0NvbW1hbmQgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5cbi8qKlxuICogQW4gaW50ZXJmYWNlIGZvciBhIEhlbHAgbWVudS5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJSGVscE1lbnUgZXh0ZW5kcyBJUmFua2VkTWVudSB7XG4gIC8qKlxuICAgKiBBIHNlbWFudGljIGNvbW1hbmQgdG8gZ2V0IHRoZSBrZXJuZWwgZm9yIHRoZSBoZWxwIG1lbnUuXG4gICAqIFRoaXMgaXMgdXNlZCB0byBwb3B1bGF0ZSBhZGRpdGlvbmFsIGhlbHBcbiAgICogbGlua3MgcHJvdmlkZWQgYnkgdGhlIGtlcm5lbCBvZiBhIHdpZGdldC5cbiAgICpcbiAgICogIyMjIyBOb3RlXG4gICAqIFRoZSBjb21tYW5kIG11c3QgcmV0dXJuIGEgS2VybmVsLklLZXJuZWxDb25uZWN0aW9uIG9iamVjdFxuICAgKi9cbiAgcmVhZG9ubHkgZ2V0S2VybmVsOiBTZW1hbnRpY0NvbW1hbmQ7XG59XG5cbi8qKlxuICogQW4gZXh0ZW5zaWJsZSBIZWxwIG1lbnUgZm9yIHRoZSBhcHBsaWNhdGlvbi5cbiAqL1xuZXhwb3J0IGNsYXNzIEhlbHBNZW51IGV4dGVuZHMgUmFua2VkTWVudSBpbXBsZW1lbnRzIElIZWxwTWVudSB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgdGhlIGhlbHAgbWVudS5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IElSYW5rZWRNZW51LklPcHRpb25zKSB7XG4gICAgc3VwZXIob3B0aW9ucyk7XG4gICAgdGhpcy5nZXRLZXJuZWwgPSBuZXcgU2VtYW50aWNDb21tYW5kKCk7XG4gIH1cblxuICAvKipcbiAgICogQSBzZW1hbnRpYyBjb21tYW5kIHRvIGdldCB0aGUga2VybmVsIGZvciB0aGUgaGVscCBtZW51LlxuICAgKiBUaGlzIGlzIHVzZWQgdG8gcG9wdWxhdGUgYWRkaXRpb25hbCBoZWxwXG4gICAqIGxpbmtzIHByb3ZpZGVkIGJ5IHRoZSBrZXJuZWwgb2YgYSB3aWRnZXQuXG4gICAqXG4gICAqICMjIyMgTm90ZVxuICAgKiBUaGUgY29tbWFuZCBtdXN0IHJldHVybiBhIEtlcm5lbC5JS2VybmVsQ29ubmVjdGlvbiBvYmplY3RcbiAgICovXG4gIHJlYWRvbmx5IGdldEtlcm5lbDogU2VtYW50aWNDb21tYW5kO1xufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgbWFpbm1lbnVcbiAqL1xuXG5leHBvcnQgKiBmcm9tICcuL21haW5tZW51JztcbmV4cG9ydCAqIGZyb20gJy4vZWRpdCc7XG5leHBvcnQgKiBmcm9tICcuL2ZpbGUnO1xuZXhwb3J0ICogZnJvbSAnLi9oZWxwJztcbmV4cG9ydCAqIGZyb20gJy4va2VybmVsJztcbmV4cG9ydCAqIGZyb20gJy4vcnVuJztcbmV4cG9ydCAqIGZyb20gJy4vc2V0dGluZ3MnO1xuZXhwb3J0ICogZnJvbSAnLi92aWV3JztcbmV4cG9ydCAqIGZyb20gJy4vdGFicyc7XG5leHBvcnQgKiBmcm9tICcuL3Rva2Vucyc7XG5cbi8qKlxuICogQGRlcHJlY2F0ZWQgc2luY2UgdmVyc2lvbiAzLjFcbiAqL1xuZXhwb3J0IHtcbiAgSVJhbmtlZE1lbnUgYXMgSUp1cHl0ZXJMYWJNZW51LFxuICBSYW5rZWRNZW51IGFzIEp1cHl0ZXJMYWJNZW51XG59IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBJUmFua2VkTWVudSwgUmFua2VkTWVudSB9IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0IHsgU2VtYW50aWNDb21tYW5kIH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuXG4vKipcbiAqIEFuIGludGVyZmFjZSBmb3IgYSBLZXJuZWwgbWVudS5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJS2VybmVsTWVudSBleHRlbmRzIElSYW5rZWRNZW51IHtcbiAgLyoqXG4gICAqIFNlbWFudGljIGNvbW1hbmRzIElLZXJuZWxVc2VycyBmb3IgdGhlIEtlcm5lbCBtZW51LlxuICAgKi9cbiAgcmVhZG9ubHkga2VybmVsVXNlcnM6IElLZXJuZWxNZW51LklLZXJuZWxVc2VyO1xufVxuXG4vKipcbiAqIEFuIGV4dGVuc2libGUgS2VybmVsIG1lbnUgZm9yIHRoZSBhcHBsaWNhdGlvbi5cbiAqL1xuZXhwb3J0IGNsYXNzIEtlcm5lbE1lbnUgZXh0ZW5kcyBSYW5rZWRNZW51IGltcGxlbWVudHMgSUtlcm5lbE1lbnUge1xuICAvKipcbiAgICogQ29uc3RydWN0IHRoZSBrZXJuZWwgbWVudS5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IElSYW5rZWRNZW51LklPcHRpb25zKSB7XG4gICAgc3VwZXIob3B0aW9ucyk7XG4gICAgdGhpcy5rZXJuZWxVc2VycyA9IHtcbiAgICAgIGNoYW5nZUtlcm5lbDogbmV3IFNlbWFudGljQ29tbWFuZCgpLFxuICAgICAgY2xlYXJXaWRnZXQ6IG5ldyBTZW1hbnRpY0NvbW1hbmQoKSxcbiAgICAgIGludGVycnVwdEtlcm5lbDogbmV3IFNlbWFudGljQ29tbWFuZCgpLFxuICAgICAgcmVjb25uZWN0VG9LZXJuZWw6IG5ldyBTZW1hbnRpY0NvbW1hbmQoKSxcbiAgICAgIHJlc3RhcnRLZXJuZWw6IG5ldyBTZW1hbnRpY0NvbW1hbmQoKSxcbiAgICAgIHNodXRkb3duS2VybmVsOiBuZXcgU2VtYW50aWNDb21tYW5kKClcbiAgICB9O1xuICB9XG5cbiAgLyoqXG4gICAqIFNlbWFudGljIGNvbW1hbmRzIElLZXJuZWxVc2VycyBmb3IgdGhlIEtlcm5lbCBtZW51LlxuICAgKi9cbiAgcmVhZG9ubHkga2VybmVsVXNlcnM6IElLZXJuZWxNZW51LklLZXJuZWxVc2VyO1xufVxuXG4vKipcbiAqIE5hbWVzcGFjZSBmb3IgSUtlcm5lbE1lbnVcbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBJS2VybmVsTWVudSB7XG4gIC8qKlxuICAgKiBJbnRlcmZhY2UgZm9yIGEgS2VybmVsIHVzZXIgdG8gcmVnaXN0ZXIgaXRzZWxmXG4gICAqIHdpdGggdGhlIElLZXJuZWxNZW51J3Mgc2VtYW50aWMgZXh0ZW5zaW9uIHBvaW50cy5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUtlcm5lbFVzZXIge1xuICAgIC8qKlxuICAgICAqIEEgc2VtYW50aWMgY29tbWFuZCB0byBpbnRlcnJ1cHQgdGhlIGtlcm5lbC5cbiAgICAgKi9cbiAgICBpbnRlcnJ1cHRLZXJuZWw6IFNlbWFudGljQ29tbWFuZDtcblxuICAgIC8qKlxuICAgICAqIEEgc2VtYW50aWMgY29tbWFuZCB0byByZWNvbm5lY3QgdG8gdGhlIGtlcm5lbFxuICAgICAqL1xuICAgIHJlY29ubmVjdFRvS2VybmVsOiBTZW1hbnRpY0NvbW1hbmQ7XG5cbiAgICAvKipcbiAgICAgKiBBIHNlbWFudGljIGNvbW1hbmQgdG8gcmVzdGFydCB0aGUga2VybmVsLCB3aGljaFxuICAgICAqIHJldHVybnMgYSBwcm9taXNlIG9mIHdoZXRoZXIgdGhlIGtlcm5lbCB3YXMgcmVzdGFydGVkLlxuICAgICAqL1xuICAgIHJlc3RhcnRLZXJuZWw6IFNlbWFudGljQ29tbWFuZDtcblxuICAgIC8qKlxuICAgICAqIEEgc2VtYW50aWMgY29tbWFuZCB0byBjbGVhciB0aGUgd2lkZ2V0LlxuICAgICAqL1xuICAgIGNsZWFyV2lkZ2V0OiBTZW1hbnRpY0NvbW1hbmQ7XG5cbiAgICAvKipcbiAgICAgKiBBIHNlbWFudGljIGNvbW1hbmQgdG8gY2hhbmdlIHRoZSBrZXJuZWwuXG4gICAgICovXG4gICAgY2hhbmdlS2VybmVsOiBTZW1hbnRpY0NvbW1hbmQ7XG5cbiAgICAvKipcbiAgICAgKiBBIHNlbWFudGljIGNvbW1hbmQgdG8gc2h1dCBkb3duIHRoZSBrZXJuZWwuXG4gICAgICovXG4gICAgc2h1dGRvd25LZXJuZWw6IFNlbWFudGljQ29tbWFuZDtcbiAgfVxufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBUcmFuc2xhdGlvbkJ1bmRsZSB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IElSYW5rZWRNZW51LCBNZW51U3ZnLCBSYW5rZWRNZW51IH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBBcnJheUV4dCB9IGZyb20gJ0BsdW1pbm8vYWxnb3JpdGhtJztcbmltcG9ydCB7IENvbW1hbmRSZWdpc3RyeSB9IGZyb20gJ0BsdW1pbm8vY29tbWFuZHMnO1xuaW1wb3J0IHsgTWVudSwgTWVudUJhciB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgeyBFZGl0TWVudSB9IGZyb20gJy4vZWRpdCc7XG5pbXBvcnQgeyBGaWxlTWVudSB9IGZyb20gJy4vZmlsZSc7XG5pbXBvcnQgeyBIZWxwTWVudSB9IGZyb20gJy4vaGVscCc7XG5pbXBvcnQgeyBLZXJuZWxNZW51IH0gZnJvbSAnLi9rZXJuZWwnO1xuaW1wb3J0IHsgUnVuTWVudSB9IGZyb20gJy4vcnVuJztcbmltcG9ydCB7IFNldHRpbmdzTWVudSB9IGZyb20gJy4vc2V0dGluZ3MnO1xuaW1wb3J0IHsgVGFic01lbnUgfSBmcm9tICcuL3RhYnMnO1xuaW1wb3J0IHsgSU1haW5NZW51IH0gZnJvbSAnLi90b2tlbnMnO1xuaW1wb3J0IHsgVmlld01lbnUgfSBmcm9tICcuL3ZpZXcnO1xuXG4vKipcbiAqIFRoZSBtYWluIG1lbnUgY2xhc3MuICBJdCBpcyBpbnRlbmRlZCB0byBiZSB1c2VkIGFzIGEgc2luZ2xldG9uLlxuICovXG5leHBvcnQgY2xhc3MgTWFpbk1lbnUgZXh0ZW5kcyBNZW51QmFyIGltcGxlbWVudHMgSU1haW5NZW51IHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCB0aGUgbWFpbiBtZW51IGJhci5cbiAgICovXG4gIGNvbnN0cnVjdG9yKGNvbW1hbmRzOiBDb21tYW5kUmVnaXN0cnkpIHtcbiAgICBzdXBlcigpO1xuICAgIHRoaXMuX2NvbW1hbmRzID0gY29tbWFuZHM7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGFwcGxpY2F0aW9uIFwiRWRpdFwiIG1lbnUuXG4gICAqL1xuICBnZXQgZWRpdE1lbnUoKTogRWRpdE1lbnUge1xuICAgIGlmICghdGhpcy5fZWRpdE1lbnUpIHtcbiAgICAgIHRoaXMuX2VkaXRNZW51ID0gbmV3IEVkaXRNZW51KHtcbiAgICAgICAgY29tbWFuZHM6IHRoaXMuX2NvbW1hbmRzLFxuICAgICAgICByYW5rOiAyLFxuICAgICAgICByZW5kZXJlcjogTWVudVN2Zy5kZWZhdWx0UmVuZGVyZXJcbiAgICAgIH0pO1xuICAgIH1cbiAgICByZXR1cm4gdGhpcy5fZWRpdE1lbnU7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGFwcGxpY2F0aW9uIFwiRmlsZVwiIG1lbnUuXG4gICAqL1xuICBnZXQgZmlsZU1lbnUoKTogRmlsZU1lbnUge1xuICAgIGlmICghdGhpcy5fZmlsZU1lbnUpIHtcbiAgICAgIHRoaXMuX2ZpbGVNZW51ID0gbmV3IEZpbGVNZW51KHtcbiAgICAgICAgY29tbWFuZHM6IHRoaXMuX2NvbW1hbmRzLFxuICAgICAgICByYW5rOiAxLFxuICAgICAgICByZW5kZXJlcjogTWVudVN2Zy5kZWZhdWx0UmVuZGVyZXJcbiAgICAgIH0pO1xuICAgIH1cbiAgICByZXR1cm4gdGhpcy5fZmlsZU1lbnU7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGFwcGxpY2F0aW9uIFwiSGVscFwiIG1lbnUuXG4gICAqL1xuICBnZXQgaGVscE1lbnUoKTogSGVscE1lbnUge1xuICAgIGlmICghdGhpcy5faGVscE1lbnUpIHtcbiAgICAgIHRoaXMuX2hlbHBNZW51ID0gbmV3IEhlbHBNZW51KHtcbiAgICAgICAgY29tbWFuZHM6IHRoaXMuX2NvbW1hbmRzLFxuICAgICAgICByYW5rOiAxMDAwLFxuICAgICAgICByZW5kZXJlcjogTWVudVN2Zy5kZWZhdWx0UmVuZGVyZXJcbiAgICAgIH0pO1xuICAgIH1cbiAgICByZXR1cm4gdGhpcy5faGVscE1lbnU7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGFwcGxpY2F0aW9uIFwiS2VybmVsXCIgbWVudS5cbiAgICovXG4gIGdldCBrZXJuZWxNZW51KCk6IEtlcm5lbE1lbnUge1xuICAgIGlmICghdGhpcy5fa2VybmVsTWVudSkge1xuICAgICAgdGhpcy5fa2VybmVsTWVudSA9IG5ldyBLZXJuZWxNZW51KHtcbiAgICAgICAgY29tbWFuZHM6IHRoaXMuX2NvbW1hbmRzLFxuICAgICAgICByYW5rOiA1LFxuICAgICAgICByZW5kZXJlcjogTWVudVN2Zy5kZWZhdWx0UmVuZGVyZXJcbiAgICAgIH0pO1xuICAgIH1cbiAgICByZXR1cm4gdGhpcy5fa2VybmVsTWVudTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgYXBwbGljYXRpb24gXCJSdW5cIiBtZW51LlxuICAgKi9cbiAgZ2V0IHJ1bk1lbnUoKTogUnVuTWVudSB7XG4gICAgaWYgKCF0aGlzLl9ydW5NZW51KSB7XG4gICAgICB0aGlzLl9ydW5NZW51ID0gbmV3IFJ1bk1lbnUoe1xuICAgICAgICBjb21tYW5kczogdGhpcy5fY29tbWFuZHMsXG4gICAgICAgIHJhbms6IDQsXG4gICAgICAgIHJlbmRlcmVyOiBNZW51U3ZnLmRlZmF1bHRSZW5kZXJlclxuICAgICAgfSk7XG4gICAgfVxuICAgIHJldHVybiB0aGlzLl9ydW5NZW51O1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBhcHBsaWNhdGlvbiBcIlNldHRpbmdzXCIgbWVudS5cbiAgICovXG4gIGdldCBzZXR0aW5nc01lbnUoKTogU2V0dGluZ3NNZW51IHtcbiAgICBpZiAoIXRoaXMuX3NldHRpbmdzTWVudSkge1xuICAgICAgdGhpcy5fc2V0dGluZ3NNZW51ID0gbmV3IFNldHRpbmdzTWVudSh7XG4gICAgICAgIGNvbW1hbmRzOiB0aGlzLl9jb21tYW5kcyxcbiAgICAgICAgcmFuazogOTk5LFxuICAgICAgICByZW5kZXJlcjogTWVudVN2Zy5kZWZhdWx0UmVuZGVyZXJcbiAgICAgIH0pO1xuICAgIH1cbiAgICByZXR1cm4gdGhpcy5fc2V0dGluZ3NNZW51O1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBhcHBsaWNhdGlvbiBcIlZpZXdcIiBtZW51LlxuICAgKi9cbiAgZ2V0IHZpZXdNZW51KCk6IFZpZXdNZW51IHtcbiAgICBpZiAoIXRoaXMuX3ZpZXdNZW51KSB7XG4gICAgICB0aGlzLl92aWV3TWVudSA9IG5ldyBWaWV3TWVudSh7XG4gICAgICAgIGNvbW1hbmRzOiB0aGlzLl9jb21tYW5kcyxcbiAgICAgICAgcmFuazogMyxcbiAgICAgICAgcmVuZGVyZXI6IE1lbnVTdmcuZGVmYXVsdFJlbmRlcmVyXG4gICAgICB9KTtcbiAgICB9XG4gICAgcmV0dXJuIHRoaXMuX3ZpZXdNZW51O1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBhcHBsaWNhdGlvbiBcIlRhYnNcIiBtZW51LlxuICAgKi9cbiAgZ2V0IHRhYnNNZW51KCk6IFRhYnNNZW51IHtcbiAgICBpZiAoIXRoaXMuX3RhYnNNZW51KSB7XG4gICAgICB0aGlzLl90YWJzTWVudSA9IG5ldyBUYWJzTWVudSh7XG4gICAgICAgIGNvbW1hbmRzOiB0aGlzLl9jb21tYW5kcyxcbiAgICAgICAgcmFuazogNTAwLFxuICAgICAgICByZW5kZXJlcjogTWVudVN2Zy5kZWZhdWx0UmVuZGVyZXJcbiAgICAgIH0pO1xuICAgIH1cbiAgICByZXR1cm4gdGhpcy5fdGFic01lbnU7XG4gIH1cblxuICAvKipcbiAgICogQWRkIGEgbmV3IG1lbnUgdG8gdGhlIG1haW4gbWVudSBiYXIuXG4gICAqL1xuICBhZGRNZW51KG1lbnU6IE1lbnUsIG9wdGlvbnM6IElNYWluTWVudS5JQWRkT3B0aW9ucyA9IHt9KTogdm9pZCB7XG4gICAgaWYgKEFycmF5RXh0LmZpcnN0SW5kZXhPZih0aGlzLm1lbnVzLCBtZW51KSA+IC0xKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgLy8gb3ZlcnJpZGUgZGVmYXVsdCByZW5kZXJlciB3aXRoIHN2Zy1zdXBwb3J0aW5nIHJlbmRlcmVyXG4gICAgTWVudVN2Zy5vdmVycmlkZURlZmF1bHRSZW5kZXJlcihtZW51KTtcblxuICAgIGNvbnN0IHJhbmsgPVxuICAgICAgJ3JhbmsnIGluIG9wdGlvbnNcbiAgICAgICAgPyBvcHRpb25zLnJhbmtcbiAgICAgICAgOiAncmFuaycgaW4gbWVudVxuICAgICAgICA/IChtZW51IGFzIGFueSkucmFua1xuICAgICAgICA6IElSYW5rZWRNZW51LkRFRkFVTFRfUkFOSztcbiAgICBjb25zdCByYW5rSXRlbSA9IHsgbWVudSwgcmFuayB9O1xuICAgIGNvbnN0IGluZGV4ID0gQXJyYXlFeHQudXBwZXJCb3VuZCh0aGlzLl9pdGVtcywgcmFua0l0ZW0sIFByaXZhdGUuaXRlbUNtcCk7XG5cbiAgICAvLyBVcG9uIGRpc3Bvc2FsLCByZW1vdmUgdGhlIG1lbnUgYW5kIGl0cyByYW5rIHJlZmVyZW5jZS5cbiAgICBtZW51LmRpc3Bvc2VkLmNvbm5lY3QodGhpcy5fb25NZW51RGlzcG9zZWQsIHRoaXMpO1xuXG4gICAgQXJyYXlFeHQuaW5zZXJ0KHRoaXMuX2l0ZW1zLCBpbmRleCwgcmFua0l0ZW0pO1xuICAgIC8qKlxuICAgICAqIENyZWF0ZSBhIG5ldyBtZW51LlxuICAgICAqL1xuICAgIHRoaXMuaW5zZXJ0TWVudShpbmRleCwgbWVudSk7XG5cbiAgICAvLyBMaW5rIHRoZSBtZW51IHRvIHRoZSBBUEkgLSBiYWNrd2FyZCBjb21wYXRpYmlsaXR5IHdoZW4gc3dpdGNoaW5nIHRvIG1lbnUgZGVzY3JpcHRpb24gaW4gc2V0dGluZ3NcbiAgICBzd2l0Y2ggKG1lbnUuaWQpIHtcbiAgICAgIGNhc2UgJ2pwLW1haW5tZW51LWZpbGUnOlxuICAgICAgICBpZiAoIXRoaXMuX2ZpbGVNZW51ICYmIG1lbnUgaW5zdGFuY2VvZiBGaWxlTWVudSkge1xuICAgICAgICAgIHRoaXMuX2ZpbGVNZW51ID0gbWVudTtcbiAgICAgICAgfVxuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2pwLW1haW5tZW51LWVkaXQnOlxuICAgICAgICBpZiAoIXRoaXMuX2VkaXRNZW51ICYmIG1lbnUgaW5zdGFuY2VvZiBFZGl0TWVudSkge1xuICAgICAgICAgIHRoaXMuX2VkaXRNZW51ID0gbWVudTtcbiAgICAgICAgfVxuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2pwLW1haW5tZW51LXZpZXcnOlxuICAgICAgICBpZiAoIXRoaXMuX3ZpZXdNZW51ICYmIG1lbnUgaW5zdGFuY2VvZiBWaWV3TWVudSkge1xuICAgICAgICAgIHRoaXMuX3ZpZXdNZW51ID0gbWVudTtcbiAgICAgICAgfVxuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2pwLW1haW5tZW51LXJ1bic6XG4gICAgICAgIGlmICghdGhpcy5fcnVuTWVudSAmJiBtZW51IGluc3RhbmNlb2YgUnVuTWVudSkge1xuICAgICAgICAgIHRoaXMuX3J1bk1lbnUgPSBtZW51O1xuICAgICAgICB9XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnanAtbWFpbm1lbnUta2VybmVsJzpcbiAgICAgICAgaWYgKCF0aGlzLl9rZXJuZWxNZW51ICYmIG1lbnUgaW5zdGFuY2VvZiBLZXJuZWxNZW51KSB7XG4gICAgICAgICAgdGhpcy5fa2VybmVsTWVudSA9IG1lbnU7XG4gICAgICAgIH1cbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdqcC1tYWlubWVudS10YWJzJzpcbiAgICAgICAgaWYgKCF0aGlzLl90YWJzTWVudSAmJiBtZW51IGluc3RhbmNlb2YgVGFic01lbnUpIHtcbiAgICAgICAgICB0aGlzLl90YWJzTWVudSA9IG1lbnU7XG4gICAgICAgIH1cbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdqcC1tYWlubWVudS1zZXR0aW5ncyc6XG4gICAgICAgIGlmICghdGhpcy5fc2V0dGluZ3NNZW51ICYmIG1lbnUgaW5zdGFuY2VvZiBTZXR0aW5nc01lbnUpIHtcbiAgICAgICAgICB0aGlzLl9zZXR0aW5nc01lbnUgPSBtZW51O1xuICAgICAgICB9XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnanAtbWFpbm1lbnUtaGVscCc6XG4gICAgICAgIGlmICghdGhpcy5faGVscE1lbnUgJiYgbWVudSBpbnN0YW5jZW9mIEhlbHBNZW51KSB7XG4gICAgICAgICAgdGhpcy5faGVscE1lbnUgPSBtZW51O1xuICAgICAgICB9XG4gICAgICAgIGJyZWFrO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIG9mIHRoZSByZXNvdXJjZXMgaGVsZCBieSB0aGUgbWVudSBiYXIuXG4gICAqL1xuICBkaXNwb3NlKCk6IHZvaWQge1xuICAgIHRoaXMuX2VkaXRNZW51Py5kaXNwb3NlKCk7XG4gICAgdGhpcy5fZmlsZU1lbnU/LmRpc3Bvc2UoKTtcbiAgICB0aGlzLl9oZWxwTWVudT8uZGlzcG9zZSgpO1xuICAgIHRoaXMuX2tlcm5lbE1lbnU/LmRpc3Bvc2UoKTtcbiAgICB0aGlzLl9ydW5NZW51Py5kaXNwb3NlKCk7XG4gICAgdGhpcy5fc2V0dGluZ3NNZW51Py5kaXNwb3NlKCk7XG4gICAgdGhpcy5fdmlld01lbnU/LmRpc3Bvc2UoKTtcbiAgICB0aGlzLl90YWJzTWVudT8uZGlzcG9zZSgpO1xuICAgIHN1cGVyLmRpc3Bvc2UoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZW5lcmF0ZSB0aGUgbWVudS5cbiAgICpcbiAgICogQHBhcmFtIGNvbW1hbmRzIFRoZSBjb21tYW5kIHJlZ2lzdHJ5XG4gICAqIEBwYXJhbSBvcHRpb25zIFRoZSBtYWluIG1lbnUgb3B0aW9ucy5cbiAgICogQHBhcmFtIHRyYW5zIC0gVGhlIGFwcGxpY2F0aW9uIGxhbmd1YWdlIHRyYW5zbGF0b3IuXG4gICAqL1xuICBzdGF0aWMgZ2VuZXJhdGVNZW51KFxuICAgIGNvbW1hbmRzOiBDb21tYW5kUmVnaXN0cnksXG4gICAgb3B0aW9uczogSU1haW5NZW51LklNZW51T3B0aW9ucyxcbiAgICB0cmFuczogVHJhbnNsYXRpb25CdW5kbGVcbiAgKTogUmFua2VkTWVudSB7XG4gICAgbGV0IG1lbnU6IFJhbmtlZE1lbnU7XG4gICAgY29uc3QgeyBpZCwgbGFiZWwsIHJhbmsgfSA9IG9wdGlvbnM7XG4gICAgc3dpdGNoIChpZCkge1xuICAgICAgY2FzZSAnanAtbWFpbm1lbnUtZmlsZSc6XG4gICAgICAgIG1lbnUgPSBuZXcgRmlsZU1lbnUoe1xuICAgICAgICAgIGNvbW1hbmRzLFxuICAgICAgICAgIHJhbmssXG4gICAgICAgICAgcmVuZGVyZXI6IE1lbnVTdmcuZGVmYXVsdFJlbmRlcmVyXG4gICAgICAgIH0pO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2pwLW1haW5tZW51LWVkaXQnOlxuICAgICAgICBtZW51ID0gbmV3IEVkaXRNZW51KHtcbiAgICAgICAgICBjb21tYW5kcyxcbiAgICAgICAgICByYW5rLFxuICAgICAgICAgIHJlbmRlcmVyOiBNZW51U3ZnLmRlZmF1bHRSZW5kZXJlclxuICAgICAgICB9KTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdqcC1tYWlubWVudS12aWV3JzpcbiAgICAgICAgbWVudSA9IG5ldyBWaWV3TWVudSh7XG4gICAgICAgICAgY29tbWFuZHMsXG4gICAgICAgICAgcmFuayxcbiAgICAgICAgICByZW5kZXJlcjogTWVudVN2Zy5kZWZhdWx0UmVuZGVyZXJcbiAgICAgICAgfSk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnanAtbWFpbm1lbnUtcnVuJzpcbiAgICAgICAgbWVudSA9IG5ldyBSdW5NZW51KHtcbiAgICAgICAgICBjb21tYW5kcyxcbiAgICAgICAgICByYW5rLFxuICAgICAgICAgIHJlbmRlcmVyOiBNZW51U3ZnLmRlZmF1bHRSZW5kZXJlclxuICAgICAgICB9KTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdqcC1tYWlubWVudS1rZXJuZWwnOlxuICAgICAgICBtZW51ID0gbmV3IEtlcm5lbE1lbnUoe1xuICAgICAgICAgIGNvbW1hbmRzLFxuICAgICAgICAgIHJhbmssXG4gICAgICAgICAgcmVuZGVyZXI6IE1lbnVTdmcuZGVmYXVsdFJlbmRlcmVyXG4gICAgICAgIH0pO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2pwLW1haW5tZW51LXRhYnMnOlxuICAgICAgICBtZW51ID0gbmV3IFRhYnNNZW51KHtcbiAgICAgICAgICBjb21tYW5kcyxcbiAgICAgICAgICByYW5rLFxuICAgICAgICAgIHJlbmRlcmVyOiBNZW51U3ZnLmRlZmF1bHRSZW5kZXJlclxuICAgICAgICB9KTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdqcC1tYWlubWVudS1zZXR0aW5ncyc6XG4gICAgICAgIG1lbnUgPSBuZXcgU2V0dGluZ3NNZW51KHtcbiAgICAgICAgICBjb21tYW5kcyxcbiAgICAgICAgICByYW5rLFxuICAgICAgICAgIHJlbmRlcmVyOiBNZW51U3ZnLmRlZmF1bHRSZW5kZXJlclxuICAgICAgICB9KTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdqcC1tYWlubWVudS1oZWxwJzpcbiAgICAgICAgbWVudSA9IG5ldyBIZWxwTWVudSh7XG4gICAgICAgICAgY29tbWFuZHMsXG4gICAgICAgICAgcmFuayxcbiAgICAgICAgICByZW5kZXJlcjogTWVudVN2Zy5kZWZhdWx0UmVuZGVyZXJcbiAgICAgICAgfSk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgZGVmYXVsdDpcbiAgICAgICAgbWVudSA9IG5ldyBSYW5rZWRNZW51KHtcbiAgICAgICAgICBjb21tYW5kcyxcbiAgICAgICAgICByYW5rLFxuICAgICAgICAgIHJlbmRlcmVyOiBNZW51U3ZnLmRlZmF1bHRSZW5kZXJlclxuICAgICAgICB9KTtcbiAgICB9XG5cbiAgICBpZiAobGFiZWwpIHtcbiAgICAgIG1lbnUudGl0bGUubGFiZWwgPSB0cmFucy5fcCgnbWVudScsIGxhYmVsKTtcbiAgICB9XG5cbiAgICByZXR1cm4gbWVudTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIGRpc3Bvc2FsIG9mIGEgbWVudS5cbiAgICovXG4gIHByaXZhdGUgX29uTWVudURpc3Bvc2VkKG1lbnU6IE1lbnUpOiB2b2lkIHtcbiAgICB0aGlzLnJlbW92ZU1lbnUobWVudSk7XG4gICAgY29uc3QgaW5kZXggPSBBcnJheUV4dC5maW5kRmlyc3RJbmRleChcbiAgICAgIHRoaXMuX2l0ZW1zLFxuICAgICAgaXRlbSA9PiBpdGVtLm1lbnUgPT09IG1lbnVcbiAgICApO1xuICAgIGlmIChpbmRleCAhPT0gLTEpIHtcbiAgICAgIEFycmF5RXh0LnJlbW92ZUF0KHRoaXMuX2l0ZW1zLCBpbmRleCk7XG4gICAgfVxuICB9XG5cbiAgcHJpdmF0ZSBfY29tbWFuZHM6IENvbW1hbmRSZWdpc3RyeTtcbiAgcHJpdmF0ZSBfaXRlbXM6IFByaXZhdGUuSVJhbmtJdGVtW10gPSBbXTtcbiAgcHJpdmF0ZSBfZWRpdE1lbnU6IEVkaXRNZW51O1xuICBwcml2YXRlIF9maWxlTWVudTogRmlsZU1lbnU7XG4gIHByaXZhdGUgX2hlbHBNZW51OiBIZWxwTWVudTtcbiAgcHJpdmF0ZSBfa2VybmVsTWVudTogS2VybmVsTWVudTtcbiAgcHJpdmF0ZSBfcnVuTWVudTogUnVuTWVudTtcbiAgcHJpdmF0ZSBfc2V0dGluZ3NNZW51OiBTZXR0aW5nc01lbnU7XG4gIHByaXZhdGUgX3ZpZXdNZW51OiBWaWV3TWVudTtcbiAgcHJpdmF0ZSBfdGFic01lbnU6IFRhYnNNZW51O1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBwcml2YXRlIGRhdGEuXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgLyoqXG4gICAqIEFuIG9iamVjdCB3aGljaCBob2xkcyBhIG1lbnUgYW5kIGl0cyBzb3J0IHJhbmsuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElSYW5rSXRlbSB7XG4gICAgLyoqXG4gICAgICogVGhlIG1lbnUgZm9yIHRoZSBpdGVtLlxuICAgICAqL1xuICAgIG1lbnU6IE1lbnU7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgc29ydCByYW5rIG9mIHRoZSBtZW51LlxuICAgICAqL1xuICAgIHJhbms6IG51bWJlcjtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIGNvbXBhcmF0b3IgZnVuY3Rpb24gZm9yIG1lbnUgcmFuayBpdGVtcy5cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBpdGVtQ21wKGZpcnN0OiBJUmFua0l0ZW0sIHNlY29uZDogSVJhbmtJdGVtKTogbnVtYmVyIHtcbiAgICByZXR1cm4gZmlyc3QucmFuayAtIHNlY29uZC5yYW5rO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElSYW5rZWRNZW51LCBSYW5rZWRNZW51IH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBTZW1hbnRpY0NvbW1hbmQgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5cbi8qKlxuICogQW4gaW50ZXJmYWNlIGZvciBhIFJ1biBtZW51LlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElSdW5NZW51IGV4dGVuZHMgSVJhbmtlZE1lbnUge1xuICAvKipcbiAgICogU2VtYW50aWMgY29tbWFuZHMgSUNvZGVSdW5uZXIgZm9yIHRoZSBSdW4gbWVudS5cbiAgICovXG4gIHJlYWRvbmx5IGNvZGVSdW5uZXJzOiBJUnVuTWVudS5JQ29kZVJ1bm5lcjtcbn1cblxuLyoqXG4gKiBBbiBleHRlbnNpYmxlIFJ1biBtZW51IGZvciB0aGUgYXBwbGljYXRpb24uXG4gKi9cbmV4cG9ydCBjbGFzcyBSdW5NZW51IGV4dGVuZHMgUmFua2VkTWVudSBpbXBsZW1lbnRzIElSdW5NZW51IHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCB0aGUgcnVuIG1lbnUuXG4gICAqL1xuICBjb25zdHJ1Y3RvcihvcHRpb25zOiBJUmFua2VkTWVudS5JT3B0aW9ucykge1xuICAgIHN1cGVyKG9wdGlvbnMpO1xuICAgIHRoaXMuY29kZVJ1bm5lcnMgPSB7XG4gICAgICByZXN0YXJ0OiBuZXcgU2VtYW50aWNDb21tYW5kKCksXG4gICAgICBydW46IG5ldyBTZW1hbnRpY0NvbW1hbmQoKSxcbiAgICAgIHJ1bkFsbDogbmV3IFNlbWFudGljQ29tbWFuZCgpXG4gICAgfTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZW1hbnRpYyBjb21tYW5kcyBJQ29kZVJ1bm5lciBmb3IgdGhlIFJ1biBtZW51LlxuICAgKi9cbiAgcmVhZG9ubHkgY29kZVJ1bm5lcnM6IElSdW5NZW51LklDb2RlUnVubmVyO1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBSdW5NZW51IHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgSVJ1bk1lbnUge1xuICAvKipcbiAgICogQW4gb2JqZWN0IHRoYXQgcnVucyBjb2RlLCB3aGljaCBtYXkgYmVcbiAgICogcmVnaXN0ZXJlZCB3aXRoIHRoZSBSdW4gbWVudS5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUNvZGVSdW5uZXIge1xuICAgIC8qKlxuICAgICAqIEEgc2VtYW50aWMgY29tbWFuZCB0byBydW4gYSBzdWJwYXJ0IG9mIGEgZG9jdW1lbnQuXG4gICAgICovXG4gICAgcnVuOiBTZW1hbnRpY0NvbW1hbmQ7XG4gICAgLyoqXG4gICAgICogQSBzZW1hbnRpYyBjb21tYW5kIHRvIHJ1biBhIHdob2xlIGRvY3VtZW50XG4gICAgICovXG4gICAgcnVuQWxsOiBTZW1hbnRpY0NvbW1hbmQ7XG4gICAgLyoqXG4gICAgICogQSBzZW1hbnRpYyBjb21tYW5kIHRvIHJlc3RhcnQgYSBrZXJuZWxcbiAgICAgKi9cbiAgICByZXN0YXJ0OiBTZW1hbnRpY0NvbW1hbmQ7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgSVJhbmtlZE1lbnUsIFJhbmtlZE1lbnUgfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcblxuLyoqXG4gKiBBbiBpbnRlcmZhY2UgZm9yIGEgU2V0dGluZ3MgbWVudS5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJU2V0dGluZ3NNZW51IGV4dGVuZHMgSVJhbmtlZE1lbnUge31cblxuLyoqXG4gKiBBbiBleHRlbnNpYmxlIFNldHRpbmdzIG1lbnUgZm9yIHRoZSBhcHBsaWNhdGlvbi5cbiAqL1xuZXhwb3J0IGNsYXNzIFNldHRpbmdzTWVudSBleHRlbmRzIFJhbmtlZE1lbnUgaW1wbGVtZW50cyBJU2V0dGluZ3NNZW51IHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCB0aGUgc2V0dGluZ3MgbWVudS5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IElSYW5rZWRNZW51LklPcHRpb25zKSB7XG4gICAgc3VwZXIob3B0aW9ucyk7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgSVJhbmtlZE1lbnUsIFJhbmtlZE1lbnUgfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcblxuLyoqXG4gKiBBbiBpbnRlcmZhY2UgZm9yIGEgVGFicyBtZW51LlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElUYWJzTWVudSBleHRlbmRzIElSYW5rZWRNZW51IHt9XG5cbi8qKlxuICogQW4gZXh0ZW5zaWJsZSBUYWJzIG1lbnUgZm9yIHRoZSBhcHBsaWNhdGlvbi5cbiAqL1xuZXhwb3J0IGNsYXNzIFRhYnNNZW51IGV4dGVuZHMgUmFua2VkTWVudSBpbXBsZW1lbnRzIElUYWJzTWVudSB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgdGhlIHRhYnMgbWVudS5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IElSYW5rZWRNZW51LklPcHRpb25zKSB7XG4gICAgc3VwZXIob3B0aW9ucyk7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgTWVudUZhY3RvcnkgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBUb2tlbiB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IE1lbnUgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0IHsgSUVkaXRNZW51IH0gZnJvbSAnLi9lZGl0JztcbmltcG9ydCB7IElGaWxlTWVudSB9IGZyb20gJy4vZmlsZSc7XG5pbXBvcnQgeyBJSGVscE1lbnUgfSBmcm9tICcuL2hlbHAnO1xuaW1wb3J0IHsgSUtlcm5lbE1lbnUgfSBmcm9tICcuL2tlcm5lbCc7XG5pbXBvcnQgeyBJUnVuTWVudSB9IGZyb20gJy4vcnVuJztcbmltcG9ydCB7IElTZXR0aW5nc01lbnUgfSBmcm9tICcuL3NldHRpbmdzJztcbmltcG9ydCB7IElUYWJzTWVudSB9IGZyb20gJy4vdGFicyc7XG5pbXBvcnQgeyBJVmlld01lbnUgfSBmcm9tICcuL3ZpZXcnO1xuXG4vKipcbiAqIFRoZSBtYWluIG1lbnUgdG9rZW4uXG4gKi9cbmV4cG9ydCBjb25zdCBJTWFpbk1lbnUgPSBuZXcgVG9rZW48SU1haW5NZW51PignQGp1cHl0ZXJsYWIvbWFpbm1lbnU6SU1haW5NZW51Jyk7XG5cbi8qKlxuICogVGhlIG1haW4gbWVudSBpbnRlcmZhY2UuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSU1haW5NZW51IHtcbiAgLyoqXG4gICAqIEFkZCBhIG5ldyBtZW51IHRvIHRoZSBtYWluIG1lbnUgYmFyLlxuICAgKi9cbiAgYWRkTWVudShtZW51OiBNZW51LCBvcHRpb25zPzogSU1haW5NZW51LklBZGRPcHRpb25zKTogdm9pZDtcblxuICAvKipcbiAgICogVGhlIGFwcGxpY2F0aW9uIFwiRmlsZVwiIG1lbnUuXG4gICAqL1xuICByZWFkb25seSBmaWxlTWVudTogSUZpbGVNZW51O1xuXG4gIC8qKlxuICAgKiBUaGUgYXBwbGljYXRpb24gXCJFZGl0XCIgbWVudS5cbiAgICovXG4gIHJlYWRvbmx5IGVkaXRNZW51OiBJRWRpdE1lbnU7XG5cbiAgLyoqXG4gICAqIFRoZSBhcHBsaWNhdGlvbiBcIlZpZXdcIiBtZW51LlxuICAgKi9cbiAgcmVhZG9ubHkgdmlld01lbnU6IElWaWV3TWVudTtcblxuICAvKipcbiAgICogVGhlIGFwcGxpY2F0aW9uIFwiSGVscFwiIG1lbnUuXG4gICAqL1xuICByZWFkb25seSBoZWxwTWVudTogSUhlbHBNZW51O1xuXG4gIC8qKlxuICAgKiBUaGUgYXBwbGljYXRpb24gXCJLZXJuZWxcIiBtZW51LlxuICAgKi9cbiAgcmVhZG9ubHkga2VybmVsTWVudTogSUtlcm5lbE1lbnU7XG5cbiAgLyoqXG4gICAqIFRoZSBhcHBsaWNhdGlvbiBcIlJ1blwiIG1lbnUuXG4gICAqL1xuICByZWFkb25seSBydW5NZW51OiBJUnVuTWVudTtcblxuICAvKipcbiAgICogVGhlIGFwcGxpY2F0aW9uIFwiU2V0dGluZ3NcIiBtZW51LlxuICAgKi9cbiAgcmVhZG9ubHkgc2V0dGluZ3NNZW51OiBJU2V0dGluZ3NNZW51O1xuXG4gIC8qKlxuICAgKiBUaGUgYXBwbGljYXRpb24gXCJUYWJzXCIgbWVudS5cbiAgICovXG4gIHJlYWRvbmx5IHRhYnNNZW51OiBJVGFic01lbnU7XG59XG5cbi8qKlxuICogVGhlIG5hbWVzcGFjZSBmb3IgSU1haW5NZW51IGF0dGFjaGVkIGludGVyZmFjZXMuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgSU1haW5NZW51IHtcbiAgLyoqXG4gICAqIFRoZSBvcHRpb25zIHVzZWQgdG8gYWRkIGEgbWVudSB0byB0aGUgbWFpbiBtZW51LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJQWRkT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIHJhbmsgb3JkZXIgb2YgdGhlIG1lbnUgYW1vbmcgaXRzIHNpYmxpbmdzLlxuICAgICAqL1xuICAgIHJhbms/OiBudW1iZXI7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGluc3RhbnRpYXRpb24gb3B0aW9ucyBmb3IgYW4gSU1haW5NZW51LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJTWVudU9wdGlvbnMgZXh0ZW5kcyBNZW51RmFjdG9yeS5JTWVudU9wdGlvbnMge31cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgSVJhbmtlZE1lbnUsIFJhbmtlZE1lbnUgfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IFNlbWFudGljQ29tbWFuZCB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcblxuLyoqXG4gKiBBbiBpbnRlcmZhY2UgZm9yIGEgVmlldyBtZW51LlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElWaWV3TWVudSBleHRlbmRzIElSYW5rZWRNZW51IHtcbiAgLyoqXG4gICAqIFNlbWFudGljIGNvbW1hbmRzIElFZGl0b3JWaWV3ZXIgZm9yIHRoZSBWaWV3IG1lbnUuXG4gICAqL1xuICByZWFkb25seSBlZGl0b3JWaWV3ZXJzOiBJVmlld01lbnUuSUVkaXRvclZpZXdlcjtcbn1cblxuLyoqXG4gKiBBbiBleHRlbnNpYmxlIFZpZXcgbWVudSBmb3IgdGhlIGFwcGxpY2F0aW9uLlxuICovXG5leHBvcnQgY2xhc3MgVmlld01lbnUgZXh0ZW5kcyBSYW5rZWRNZW51IGltcGxlbWVudHMgSVZpZXdNZW51IHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCB0aGUgdmlldyBtZW51LlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogSVJhbmtlZE1lbnUuSU9wdGlvbnMpIHtcbiAgICBzdXBlcihvcHRpb25zKTtcbiAgICB0aGlzLmVkaXRvclZpZXdlcnMgPSB7XG4gICAgICB0b2dnbGVMaW5lTnVtYmVyczogbmV3IFNlbWFudGljQ29tbWFuZCgpLFxuICAgICAgdG9nZ2xlTWF0Y2hCcmFja2V0czogbmV3IFNlbWFudGljQ29tbWFuZCgpLFxuICAgICAgdG9nZ2xlV29yZFdyYXA6IG5ldyBTZW1hbnRpY0NvbW1hbmQoKVxuICAgIH07XG4gIH1cblxuICAvKipcbiAgICogU2VtYW50aWMgY29tbWFuZHMgSUVkaXRvclZpZXdlciBmb3IgdGhlIFZpZXcgbWVudS5cbiAgICovXG4gIHJlYWRvbmx5IGVkaXRvclZpZXdlcnM6IElWaWV3TWVudS5JRWRpdG9yVmlld2VyO1xufVxuXG4vKipcbiAqIE5hbWVzcGFjZSBmb3IgSVZpZXdNZW51LlxuICovXG5leHBvcnQgbmFtZXNwYWNlIElWaWV3TWVudSB7XG4gIC8qKlxuICAgKiBJbnRlcmZhY2UgZm9yIGEgdGV4dCBlZGl0b3Igdmlld2VyIHRvIHJlZ2lzdGVyXG4gICAqIGl0c2VsZiB3aXRoIHRoZSB0ZXh0IGVkaXRvciBzZW1hbnRpYyBjb21tYW5kcy5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUVkaXRvclZpZXdlciB7XG4gICAgLyoqXG4gICAgICogQSBzZW1hbnRpYyBjb21tYW5kIHRvIHNob3cgbGluZSBudW1iZXJzIGluIHRoZSBlZGl0b3IuXG4gICAgICovXG4gICAgdG9nZ2xlTGluZU51bWJlcnM6IFNlbWFudGljQ29tbWFuZDtcblxuICAgIC8qKlxuICAgICAqIEEgc2VtYW50aWMgY29tbWFuZCB0byB3b3JkLXdyYXAgdGhlIGVkaXRvci5cbiAgICAgKi9cbiAgICB0b2dnbGVXb3JkV3JhcDogU2VtYW50aWNDb21tYW5kO1xuXG4gICAgLyoqXG4gICAgICogQSBzZW1hbnRpYyBjb21tYW5kIHRvIG1hdGNoIGJyYWNrZXRzIGluIHRoZSBlZGl0b3IuXG4gICAgICovXG4gICAgdG9nZ2xlTWF0Y2hCcmFja2V0czogU2VtYW50aWNDb21tYW5kO1xuICB9XG59XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=