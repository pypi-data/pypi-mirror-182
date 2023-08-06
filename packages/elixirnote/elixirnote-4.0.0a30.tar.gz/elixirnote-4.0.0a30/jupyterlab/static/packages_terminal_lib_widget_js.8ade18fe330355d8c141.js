"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_terminal_lib_widget_js"],{

/***/ "../../packages/terminal/lib/tokens.js":
/*!*********************************************!*\
  !*** ../../packages/terminal/lib/tokens.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ITerminal": () => (/* binding */ ITerminal),
/* harmony export */   "ITerminalTracker": () => (/* binding */ ITerminalTracker)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The editor tracker token.
 */
const ITerminalTracker = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/terminal:ITerminalTracker');
/**
 * The namespace for terminals. Separated from the widget so it can be lazy
 * loaded.
 */
var ITerminal;
(function (ITerminal) {
    /**
     * The default options used for creating terminals.
     */
    ITerminal.defaultOptions = {
        theme: 'inherit',
        fontFamily: 'Menlo, Consolas, "DejaVu Sans Mono", monospace',
        fontSize: 13,
        lineHeight: 1.0,
        scrollback: 1000,
        shutdownOnClose: false,
        closeOnExit: true,
        cursorBlink: true,
        initialCommand: '',
        screenReaderMode: false,
        pasteWithCtrlV: true,
        autoFit: true,
        macOptionIsMeta: false
    };
})(ITerminal || (ITerminal = {}));


/***/ }),

/***/ "../../packages/terminal/lib/widget.js":
/*!*********************************************!*\
  !*** ../../packages/terminal/lib/widget.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Terminal": () => (/* binding */ Terminal)
/* harmony export */ });
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_domutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/domutils */ "webpack/sharing/consume/default/@lumino/domutils/@lumino/domutils");
/* harmony import */ var _lumino_domutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_domutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_messaging__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/messaging */ "webpack/sharing/consume/default/@lumino/messaging/@lumino/messaging");
/* harmony import */ var _lumino_messaging__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_messaging__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var xterm__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! xterm */ "../../node_modules/xterm/lib/xterm.js");
/* harmony import */ var xterm__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(xterm__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var xterm_addon_fit__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! xterm-addon-fit */ "../../node_modules/xterm-addon-fit/lib/xterm-addon-fit.js");
/* harmony import */ var xterm_addon_fit__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(xterm_addon_fit__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var ___WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! . */ "../../packages/terminal/lib/tokens.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
var __rest = (undefined && undefined.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};







/**
 * The class name added to a terminal widget.
 */
const TERMINAL_CLASS = 'jp-Terminal';
/**
 * The class name added to a terminal body.
 */
const TERMINAL_BODY_CLASS = 'jp-Terminal-body';
/**
 * A widget which manages a terminal session.
 */
class Terminal extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.Widget {
    /**
     * Construct a new terminal widget.
     *
     * @param session - The terminal session object.
     *
     * @param options - The terminal configuration options.
     *
     * @param translator - The language translator.
     */
    constructor(session, options = {}, translator) {
        super();
        this._needsResize = true;
        this._termOpened = false;
        this._offsetWidth = -1;
        this._offsetHeight = -1;
        translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator;
        this._trans = translator.load('jupyterlab');
        this.session = session;
        // Initialize settings.
        this._options = Object.assign(Object.assign({}, ___WEBPACK_IMPORTED_MODULE_6__.ITerminal.defaultOptions), options);
        const _a = this._options, { theme } = _a, other = __rest(_a, ["theme"]);
        const xtermOptions = Object.assign({ theme: Private.getXTermTheme(theme) }, other);
        this.addClass(TERMINAL_CLASS);
        this._setThemeAttribute(theme);
        // Create the xterm.
        this._term = new xterm__WEBPACK_IMPORTED_MODULE_4__.Terminal(xtermOptions);
        this._fitAddon = new xterm_addon_fit__WEBPACK_IMPORTED_MODULE_5__.FitAddon();
        this._term.loadAddon(this._fitAddon);
        this._initializeTerm();
        this.id = `jp-Terminal-${Private.id++}`;
        this.title.label = this._trans.__('Terminal');
        session.messageReceived.connect(this._onMessage, this);
        session.disposed.connect(() => {
            if (this.getOption('closeOnExit')) {
                this.dispose();
            }
        }, this);
        if (session.connectionStatus === 'connected') {
            this._initialConnection();
        }
        else {
            session.connectionStatusChanged.connect(this._initialConnection, this);
        }
    }
    _setThemeAttribute(theme) {
        if (this.isDisposed) {
            return;
        }
        this.node.setAttribute('data-term-theme', theme ? theme.toLowerCase() : 'inherit');
    }
    _initialConnection() {
        if (this.isDisposed) {
            return;
        }
        if (this.session.connectionStatus !== 'connected') {
            return;
        }
        this.title.label = this._trans.__('Terminal %1', this.session.name);
        this._setSessionSize();
        if (this._options.initialCommand) {
            this.session.send({
                type: 'stdin',
                content: [this._options.initialCommand + '\r']
            });
        }
        // Only run this initial connection logic once.
        this.session.connectionStatusChanged.disconnect(this._initialConnection, this);
    }
    /**
     * Get a config option for the terminal.
     */
    getOption(option) {
        return this._options[option];
    }
    /**
     * Set a config option for the terminal.
     */
    setOption(option, value) {
        if (option !== 'theme' &&
            (this._options[option] === value || option === 'initialCommand')) {
            return;
        }
        this._options[option] = value;
        switch (option) {
            case 'shutdownOnClose': // Do not transmit to XTerm
            case 'closeOnExit': // Do not transmit to XTerm
                break;
            case 'theme':
                this._term.setOption('theme', Private.getXTermTheme(value));
                this._setThemeAttribute(value);
                break;
            default:
                this._term.setOption(option, value);
                break;
        }
        this._needsResize = true;
        this.update();
    }
    /**
     * Dispose of the resources held by the terminal widget.
     */
    dispose() {
        if (!this.session.isDisposed) {
            if (this.getOption('shutdownOnClose')) {
                this.session.shutdown().catch(reason => {
                    console.error(`Terminal not shut down: ${reason}`);
                });
            }
        }
        this._term.dispose();
        super.dispose();
    }
    /**
     * Refresh the terminal session.
     *
     * #### Notes
     * Failure to reconnect to the session should be caught appropriately
     */
    async refresh() {
        if (!this.isDisposed) {
            await this.session.reconnect();
            this._term.clear();
        }
    }
    /**
     * Process a message sent to the widget.
     *
     * @param msg - The message sent to the widget.
     *
     * #### Notes
     * Subclasses may reimplement this method as needed.
     */
    processMessage(msg) {
        super.processMessage(msg);
        switch (msg.type) {
            case 'fit-request':
                this.onFitRequest(msg);
                break;
            default:
                break;
        }
    }
    /**
     * Set the size of the terminal when attached if dirty.
     */
    onAfterAttach(msg) {
        this.update();
    }
    /**
     * Set the size of the terminal when shown if dirty.
     */
    onAfterShow(msg) {
        this.update();
    }
    /**
     * On resize, use the computed row and column sizes to resize the terminal.
     */
    onResize(msg) {
        this._offsetWidth = msg.width;
        this._offsetHeight = msg.height;
        this._needsResize = true;
        this.update();
    }
    /**
     * A message handler invoked on an `'update-request'` message.
     */
    onUpdateRequest(msg) {
        var _a;
        if (!this.isVisible || !this.isAttached) {
            return;
        }
        // Open the terminal if necessary.
        if (!this._termOpened) {
            this._term.open(this.node);
            (_a = this._term.element) === null || _a === void 0 ? void 0 : _a.classList.add(TERMINAL_BODY_CLASS);
            this._termOpened = true;
        }
        if (this._needsResize) {
            this._resizeTerminal();
        }
    }
    /**
     * A message handler invoked on an `'fit-request'` message.
     */
    onFitRequest(msg) {
        const resize = _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.Widget.ResizeMessage.UnknownSize;
        _lumino_messaging__WEBPACK_IMPORTED_MODULE_2__.MessageLoop.sendMessage(this, resize);
    }
    /**
     * Handle `'activate-request'` messages.
     */
    onActivateRequest(msg) {
        this._term.focus();
    }
    /**
     * Initialize the terminal object.
     */
    _initializeTerm() {
        const term = this._term;
        term.onData((data) => {
            if (this.isDisposed) {
                return;
            }
            this.session.send({
                type: 'stdin',
                content: [data]
            });
        });
        term.onTitleChange((title) => {
            this.title.label = title;
        });
        // Do not add any Ctrl+C/Ctrl+V handling on macOS,
        // where Cmd+C/Cmd+V works as intended.
        if (_lumino_domutils__WEBPACK_IMPORTED_MODULE_1__.Platform.IS_MAC) {
            return;
        }
        term.attachCustomKeyEventHandler(event => {
            if (event.ctrlKey && event.key === 'c' && term.hasSelection()) {
                // Return so that the usual OS copy happens
                // instead of interrupt signal.
                return false;
            }
            if (event.ctrlKey && event.key === 'v' && this._options.pasteWithCtrlV) {
                // Return so that the usual paste happens.
                return false;
            }
            return true;
        });
    }
    /**
     * Handle a message from the terminal session.
     */
    _onMessage(sender, msg) {
        switch (msg.type) {
            case 'stdout':
                if (msg.content) {
                    this._term.write(msg.content[0]);
                }
                break;
            case 'disconnect':
                this._term.write('\r\n\r\n[Finished… Term Session]\r\n');
                break;
            default:
                break;
        }
    }
    /**
     * Resize the terminal based on computed geometry.
     */
    _resizeTerminal() {
        if (this._options.autoFit) {
            this._fitAddon.fit();
        }
        if (this._offsetWidth === -1) {
            this._offsetWidth = this.node.offsetWidth;
        }
        if (this._offsetHeight === -1) {
            this._offsetHeight = this.node.offsetHeight;
        }
        this._setSessionSize();
        this._needsResize = false;
    }
    /**
     * Set the size of the terminal in the session.
     */
    _setSessionSize() {
        const content = [
            this._term.rows,
            this._term.cols,
            this._offsetHeight,
            this._offsetWidth
        ];
        if (!this.isDisposed) {
            this.session.send({ type: 'set_size', content });
        }
    }
}
/**
 * A namespace for private data.
 */
var Private;
(function (Private) {
    /**
     * An incrementing counter for ids.
     */
    Private.id = 0;
    /**
     * The light terminal theme.
     */
    Private.lightTheme = {
        foreground: '#000',
        background: '#fff',
        cursor: '#616161',
        cursorAccent: '#F5F5F5',
        selection: 'rgba(97, 97, 97, 0.3)' // md-grey-700
    };
    /**
     * The dark terminal theme.
     */
    Private.darkTheme = {
        foreground: '#fff',
        background: '#000',
        cursor: '#fff',
        cursorAccent: '#000',
        selection: 'rgba(255, 255, 255, 0.3)'
    };
    /**
     * The current theme.
     */
    Private.inheritTheme = () => ({
        foreground: getComputedStyle(document.body)
            .getPropertyValue('--jp-ui-font-color0')
            .trim(),
        background: getComputedStyle(document.body)
            .getPropertyValue('--jp-layout-color0')
            .trim(),
        cursor: getComputedStyle(document.body)
            .getPropertyValue('--jp-ui-font-color1')
            .trim(),
        cursorAccent: getComputedStyle(document.body)
            .getPropertyValue('--jp-ui-inverse-font-color0')
            .trim(),
        selection: getComputedStyle(document.body)
            .getPropertyValue('--jp-ui-font-color3')
            .trim()
    });
    function getXTermTheme(theme) {
        switch (theme) {
            case 'light':
                return Private.lightTheme;
            case 'dark':
                return Private.darkTheme;
            case 'inherit':
            default:
                return Private.inheritTheme();
        }
    }
    Private.getXTermTheme = getXTermTheme;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdGVybWluYWxfbGliX3dpZGdldF9qcy44YWRlMThmZTMzMDM1NWQ4YzE0MS5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUlqQjtBQVMxQzs7R0FFRztBQUNJLE1BQU0sZ0JBQWdCLEdBQUcsSUFBSSxvREFBSyxDQUN2Qyx1Q0FBdUMsQ0FDeEMsQ0FBQztBQUVGOzs7R0FHRztBQUNJLElBQVUsU0FBUyxDQWlJekI7QUFqSUQsV0FBaUIsU0FBUztJQStGeEI7O09BRUc7SUFDVSx3QkFBYyxHQUFhO1FBQ3RDLEtBQUssRUFBRSxTQUFTO1FBQ2hCLFVBQVUsRUFBRSxnREFBZ0Q7UUFDNUQsUUFBUSxFQUFFLEVBQUU7UUFDWixVQUFVLEVBQUUsR0FBRztRQUNmLFVBQVUsRUFBRSxJQUFJO1FBQ2hCLGVBQWUsRUFBRSxLQUFLO1FBQ3RCLFdBQVcsRUFBRSxJQUFJO1FBQ2pCLFdBQVcsRUFBRSxJQUFJO1FBQ2pCLGNBQWMsRUFBRSxFQUFFO1FBQ2xCLGdCQUFnQixFQUFFLEtBQUs7UUFDdkIsY0FBYyxFQUFFLElBQUk7UUFDcEIsT0FBTyxFQUFFLElBQUk7UUFDYixlQUFlLEVBQUUsS0FBSztLQUN2QixDQUFDO0FBaUJKLENBQUMsRUFqSWdCLFNBQVMsS0FBVCxTQUFTLFFBaUl6Qjs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQzFKRCwwQ0FBMEM7QUFDMUMsMkRBQTJEOzs7Ozs7Ozs7Ozs7QUFPMUI7QUFDVztBQUNhO0FBQ2hCO0FBQ0M7QUFDQztBQUNiO0FBRTlCOztHQUVHO0FBQ0gsTUFBTSxjQUFjLEdBQUcsYUFBYSxDQUFDO0FBRXJDOztHQUVHO0FBQ0gsTUFBTSxtQkFBbUIsR0FBRyxrQkFBa0IsQ0FBQztBQUUvQzs7R0FFRztBQUNJLE1BQU0sUUFBUyxTQUFRLG1EQUFNO0lBQ2xDOzs7Ozs7OztPQVFHO0lBQ0gsWUFDRSxPQUF1QyxFQUN2QyxVQUF1QyxFQUFFLEVBQ3pDLFVBQXdCO1FBRXhCLEtBQUssRUFBRSxDQUFDO1FBMlVGLGlCQUFZLEdBQUcsSUFBSSxDQUFDO1FBQ3BCLGdCQUFXLEdBQUcsS0FBSyxDQUFDO1FBQ3BCLGlCQUFZLEdBQUcsQ0FBQyxDQUFDLENBQUM7UUFDbEIsa0JBQWEsR0FBRyxDQUFDLENBQUMsQ0FBQztRQTdVekIsVUFBVSxHQUFHLFVBQVUsSUFBSSxtRUFBYyxDQUFDO1FBQzFDLElBQUksQ0FBQyxNQUFNLEdBQUcsVUFBVSxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUMsQ0FBQztRQUM1QyxJQUFJLENBQUMsT0FBTyxHQUFHLE9BQU8sQ0FBQztRQUV2Qix1QkFBdUI7UUFDdkIsSUFBSSxDQUFDLFFBQVEsbUNBQVEsdURBQXdCLEdBQUssT0FBTyxDQUFFLENBQUM7UUFFNUQsTUFBTSxLQUFzQixJQUFJLENBQUMsUUFBUSxFQUFuQyxFQUFFLEtBQUssT0FBNEIsRUFBdkIsS0FBSyxjQUFqQixTQUFtQixDQUFnQixDQUFDO1FBQzFDLE1BQU0sWUFBWSxtQkFDaEIsS0FBSyxFQUFFLE9BQU8sQ0FBQyxhQUFhLENBQUMsS0FBSyxDQUFDLElBQ2hDLEtBQUssQ0FDVCxDQUFDO1FBRUYsSUFBSSxDQUFDLFFBQVEsQ0FBQyxjQUFjLENBQUMsQ0FBQztRQUU5QixJQUFJLENBQUMsa0JBQWtCLENBQUMsS0FBSyxDQUFDLENBQUM7UUFFL0Isb0JBQW9CO1FBQ3BCLElBQUksQ0FBQyxLQUFLLEdBQUcsSUFBSSwyQ0FBSyxDQUFDLFlBQVksQ0FBQyxDQUFDO1FBQ3JDLElBQUksQ0FBQyxTQUFTLEdBQUcsSUFBSSxxREFBUSxFQUFFLENBQUM7UUFDaEMsSUFBSSxDQUFDLEtBQUssQ0FBQyxTQUFTLENBQUMsSUFBSSxDQUFDLFNBQVMsQ0FBQyxDQUFDO1FBRXJDLElBQUksQ0FBQyxlQUFlLEVBQUUsQ0FBQztRQUV2QixJQUFJLENBQUMsRUFBRSxHQUFHLGVBQWUsT0FBTyxDQUFDLEVBQUUsRUFBRSxFQUFFLENBQUM7UUFDeEMsSUFBSSxDQUFDLEtBQUssQ0FBQyxLQUFLLEdBQUcsSUFBSSxDQUFDLE1BQU0sQ0FBQyxFQUFFLENBQUMsVUFBVSxDQUFDLENBQUM7UUFFOUMsT0FBTyxDQUFDLGVBQWUsQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLFVBQVUsRUFBRSxJQUFJLENBQUMsQ0FBQztRQUN2RCxPQUFPLENBQUMsUUFBUSxDQUFDLE9BQU8sQ0FBQyxHQUFHLEVBQUU7WUFDNUIsSUFBSSxJQUFJLENBQUMsU0FBUyxDQUFDLGFBQWEsQ0FBQyxFQUFFO2dCQUNqQyxJQUFJLENBQUMsT0FBTyxFQUFFLENBQUM7YUFDaEI7UUFDSCxDQUFDLEVBQUUsSUFBSSxDQUFDLENBQUM7UUFFVCxJQUFJLE9BQU8sQ0FBQyxnQkFBZ0IsS0FBSyxXQUFXLEVBQUU7WUFDNUMsSUFBSSxDQUFDLGtCQUFrQixFQUFFLENBQUM7U0FDM0I7YUFBTTtZQUNMLE9BQU8sQ0FBQyx1QkFBdUIsQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLGtCQUFrQixFQUFFLElBQUksQ0FBQyxDQUFDO1NBQ3hFO0lBQ0gsQ0FBQztJQUVPLGtCQUFrQixDQUFDLEtBQWdDO1FBQ3pELElBQUksSUFBSSxDQUFDLFVBQVUsRUFBRTtZQUNuQixPQUFPO1NBQ1I7UUFFRCxJQUFJLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FDcEIsaUJBQWlCLEVBQ2pCLEtBQUssQ0FBQyxDQUFDLENBQUMsS0FBSyxDQUFDLFdBQVcsRUFBRSxDQUFDLENBQUMsQ0FBQyxTQUFTLENBQ3hDLENBQUM7SUFDSixDQUFDO0lBRU8sa0JBQWtCO1FBQ3hCLElBQUksSUFBSSxDQUFDLFVBQVUsRUFBRTtZQUNuQixPQUFPO1NBQ1I7UUFFRCxJQUFJLElBQUksQ0FBQyxPQUFPLENBQUMsZ0JBQWdCLEtBQUssV0FBVyxFQUFFO1lBQ2pELE9BQU87U0FDUjtRQUVELElBQUksQ0FBQyxLQUFLLENBQUMsS0FBSyxHQUFHLElBQUksQ0FBQyxNQUFNLENBQUMsRUFBRSxDQUFDLGFBQWEsRUFBRSxJQUFJLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxDQUFDO1FBQ3BFLElBQUksQ0FBQyxlQUFlLEVBQUUsQ0FBQztRQUN2QixJQUFJLElBQUksQ0FBQyxRQUFRLENBQUMsY0FBYyxFQUFFO1lBQ2hDLElBQUksQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDO2dCQUNoQixJQUFJLEVBQUUsT0FBTztnQkFDYixPQUFPLEVBQUUsQ0FBQyxJQUFJLENBQUMsUUFBUSxDQUFDLGNBQWMsR0FBRyxJQUFJLENBQUM7YUFDL0MsQ0FBQyxDQUFDO1NBQ0o7UUFFRCwrQ0FBK0M7UUFDL0MsSUFBSSxDQUFDLE9BQU8sQ0FBQyx1QkFBdUIsQ0FBQyxVQUFVLENBQzdDLElBQUksQ0FBQyxrQkFBa0IsRUFDdkIsSUFBSSxDQUNMLENBQUM7SUFDSixDQUFDO0lBT0Q7O09BRUc7SUFDSCxTQUFTLENBQ1AsTUFBUztRQUVULE9BQU8sSUFBSSxDQUFDLFFBQVEsQ0FBQyxNQUFNLENBQUMsQ0FBQztJQUMvQixDQUFDO0lBRUQ7O09BRUc7SUFDSCxTQUFTLENBQ1AsTUFBUyxFQUNULEtBQTRCO1FBRTVCLElBQ0UsTUFBTSxLQUFLLE9BQU87WUFDbEIsQ0FBQyxJQUFJLENBQUMsUUFBUSxDQUFDLE1BQU0sQ0FBQyxLQUFLLEtBQUssSUFBSSxNQUFNLEtBQUssZ0JBQWdCLENBQUMsRUFDaEU7WUFDQSxPQUFPO1NBQ1I7UUFFRCxJQUFJLENBQUMsUUFBUSxDQUFDLE1BQU0sQ0FBQyxHQUFHLEtBQUssQ0FBQztRQUU5QixRQUFRLE1BQU0sRUFBRTtZQUNkLEtBQUssaUJBQWlCLENBQUMsQ0FBQywyQkFBMkI7WUFDbkQsS0FBSyxhQUFhLEVBQUUsMkJBQTJCO2dCQUM3QyxNQUFNO1lBQ1IsS0FBSyxPQUFPO2dCQUNWLElBQUksQ0FBQyxLQUFLLENBQUMsU0FBUyxDQUNsQixPQUFPLEVBQ1AsT0FBTyxDQUFDLGFBQWEsQ0FBQyxLQUF3QixDQUFDLENBQ2hELENBQUM7Z0JBQ0YsSUFBSSxDQUFDLGtCQUFrQixDQUFDLEtBQXdCLENBQUMsQ0FBQztnQkFDbEQsTUFBTTtZQUNSO2dCQUNFLElBQUksQ0FBQyxLQUFLLENBQUMsU0FBUyxDQUFDLE1BQU0sRUFBRSxLQUFLLENBQUMsQ0FBQztnQkFDcEMsTUFBTTtTQUNUO1FBRUQsSUFBSSxDQUFDLFlBQVksR0FBRyxJQUFJLENBQUM7UUFDekIsSUFBSSxDQUFDLE1BQU0sRUFBRSxDQUFDO0lBQ2hCLENBQUM7SUFFRDs7T0FFRztJQUNILE9BQU87UUFDTCxJQUFJLENBQUMsSUFBSSxDQUFDLE9BQU8sQ0FBQyxVQUFVLEVBQUU7WUFDNUIsSUFBSSxJQUFJLENBQUMsU0FBUyxDQUFDLGlCQUFpQixDQUFDLEVBQUU7Z0JBQ3JDLElBQUksQ0FBQyxPQUFPLENBQUMsUUFBUSxFQUFFLENBQUMsS0FBSyxDQUFDLE1BQU0sQ0FBQyxFQUFFO29CQUNyQyxPQUFPLENBQUMsS0FBSyxDQUFDLDJCQUEyQixNQUFNLEVBQUUsQ0FBQyxDQUFDO2dCQUNyRCxDQUFDLENBQUMsQ0FBQzthQUNKO1NBQ0Y7UUFDRCxJQUFJLENBQUMsS0FBSyxDQUFDLE9BQU8sRUFBRSxDQUFDO1FBQ3JCLEtBQUssQ0FBQyxPQUFPLEVBQUUsQ0FBQztJQUNsQixDQUFDO0lBRUQ7Ozs7O09BS0c7SUFDSCxLQUFLLENBQUMsT0FBTztRQUNYLElBQUksQ0FBQyxJQUFJLENBQUMsVUFBVSxFQUFFO1lBQ3BCLE1BQU0sSUFBSSxDQUFDLE9BQU8sQ0FBQyxTQUFTLEVBQUUsQ0FBQztZQUMvQixJQUFJLENBQUMsS0FBSyxDQUFDLEtBQUssRUFBRSxDQUFDO1NBQ3BCO0lBQ0gsQ0FBQztJQUVEOzs7Ozs7O09BT0c7SUFDSCxjQUFjLENBQUMsR0FBWTtRQUN6QixLQUFLLENBQUMsY0FBYyxDQUFDLEdBQUcsQ0FBQyxDQUFDO1FBQzFCLFFBQVEsR0FBRyxDQUFDLElBQUksRUFBRTtZQUNoQixLQUFLLGFBQWE7Z0JBQ2hCLElBQUksQ0FBQyxZQUFZLENBQUMsR0FBRyxDQUFDLENBQUM7Z0JBQ3ZCLE1BQU07WUFDUjtnQkFDRSxNQUFNO1NBQ1Q7SUFDSCxDQUFDO0lBRUQ7O09BRUc7SUFDTyxhQUFhLENBQUMsR0FBWTtRQUNsQyxJQUFJLENBQUMsTUFBTSxFQUFFLENBQUM7SUFDaEIsQ0FBQztJQUVEOztPQUVHO0lBQ08sV0FBVyxDQUFDLEdBQVk7UUFDaEMsSUFBSSxDQUFDLE1BQU0sRUFBRSxDQUFDO0lBQ2hCLENBQUM7SUFFRDs7T0FFRztJQUNPLFFBQVEsQ0FBQyxHQUF5QjtRQUMxQyxJQUFJLENBQUMsWUFBWSxHQUFHLEdBQUcsQ0FBQyxLQUFLLENBQUM7UUFDOUIsSUFBSSxDQUFDLGFBQWEsR0FBRyxHQUFHLENBQUMsTUFBTSxDQUFDO1FBQ2hDLElBQUksQ0FBQyxZQUFZLEdBQUcsSUFBSSxDQUFDO1FBQ3pCLElBQUksQ0FBQyxNQUFNLEVBQUUsQ0FBQztJQUNoQixDQUFDO0lBRUQ7O09BRUc7SUFDTyxlQUFlLENBQUMsR0FBWTs7UUFDcEMsSUFBSSxDQUFDLElBQUksQ0FBQyxTQUFTLElBQUksQ0FBQyxJQUFJLENBQUMsVUFBVSxFQUFFO1lBQ3ZDLE9BQU87U0FDUjtRQUVELGtDQUFrQztRQUNsQyxJQUFJLENBQUMsSUFBSSxDQUFDLFdBQVcsRUFBRTtZQUNyQixJQUFJLENBQUMsS0FBSyxDQUFDLElBQUksQ0FBQyxJQUFJLENBQUMsSUFBSSxDQUFDLENBQUM7WUFDM0IsVUFBSSxDQUFDLEtBQUssQ0FBQyxPQUFPLDBDQUFFLFNBQVMsQ0FBQyxHQUFHLENBQUMsbUJBQW1CLENBQUMsQ0FBQztZQUN2RCxJQUFJLENBQUMsV0FBVyxHQUFHLElBQUksQ0FBQztTQUN6QjtRQUVELElBQUksSUFBSSxDQUFDLFlBQVksRUFBRTtZQUNyQixJQUFJLENBQUMsZUFBZSxFQUFFLENBQUM7U0FDeEI7SUFDSCxDQUFDO0lBRUQ7O09BRUc7SUFDTyxZQUFZLENBQUMsR0FBWTtRQUNqQyxNQUFNLE1BQU0sR0FBRyw2RUFBZ0MsQ0FBQztRQUNoRCxzRUFBdUIsQ0FBQyxJQUFJLEVBQUUsTUFBTSxDQUFDLENBQUM7SUFDeEMsQ0FBQztJQUVEOztPQUVHO0lBQ08saUJBQWlCLENBQUMsR0FBWTtRQUN0QyxJQUFJLENBQUMsS0FBSyxDQUFDLEtBQUssRUFBRSxDQUFDO0lBQ3JCLENBQUM7SUFFRDs7T0FFRztJQUNLLGVBQWU7UUFDckIsTUFBTSxJQUFJLEdBQUcsSUFBSSxDQUFDLEtBQUssQ0FBQztRQUN4QixJQUFJLENBQUMsTUFBTSxDQUFDLENBQUMsSUFBWSxFQUFFLEVBQUU7WUFDM0IsSUFBSSxJQUFJLENBQUMsVUFBVSxFQUFFO2dCQUNuQixPQUFPO2FBQ1I7WUFDRCxJQUFJLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQztnQkFDaEIsSUFBSSxFQUFFLE9BQU87Z0JBQ2IsT0FBTyxFQUFFLENBQUMsSUFBSSxDQUFDO2FBQ2hCLENBQUMsQ0FBQztRQUNMLENBQUMsQ0FBQyxDQUFDO1FBRUgsSUFBSSxDQUFDLGFBQWEsQ0FBQyxDQUFDLEtBQWEsRUFBRSxFQUFFO1lBQ25DLElBQUksQ0FBQyxLQUFLLENBQUMsS0FBSyxHQUFHLEtBQUssQ0FBQztRQUMzQixDQUFDLENBQUMsQ0FBQztRQUVILGtEQUFrRDtRQUNsRCx1Q0FBdUM7UUFDdkMsSUFBSSw2REFBZSxFQUFFO1lBQ25CLE9BQU87U0FDUjtRQUVELElBQUksQ0FBQywyQkFBMkIsQ0FBQyxLQUFLLENBQUMsRUFBRTtZQUN2QyxJQUFJLEtBQUssQ0FBQyxPQUFPLElBQUksS0FBSyxDQUFDLEdBQUcsS0FBSyxHQUFHLElBQUksSUFBSSxDQUFDLFlBQVksRUFBRSxFQUFFO2dCQUM3RCwyQ0FBMkM7Z0JBQzNDLCtCQUErQjtnQkFDL0IsT0FBTyxLQUFLLENBQUM7YUFDZDtZQUVELElBQUksS0FBSyxDQUFDLE9BQU8sSUFBSSxLQUFLLENBQUMsR0FBRyxLQUFLLEdBQUcsSUFBSSxJQUFJLENBQUMsUUFBUSxDQUFDLGNBQWMsRUFBRTtnQkFDdEUsMENBQTBDO2dCQUMxQyxPQUFPLEtBQUssQ0FBQzthQUNkO1lBRUQsT0FBTyxJQUFJLENBQUM7UUFDZCxDQUFDLENBQUMsQ0FBQztJQUNMLENBQUM7SUFFRDs7T0FFRztJQUNLLFVBQVUsQ0FDaEIsTUFBc0MsRUFDdEMsR0FBd0I7UUFFeEIsUUFBUSxHQUFHLENBQUMsSUFBSSxFQUFFO1lBQ2hCLEtBQUssUUFBUTtnQkFDWCxJQUFJLEdBQUcsQ0FBQyxPQUFPLEVBQUU7b0JBQ2YsSUFBSSxDQUFDLEtBQUssQ0FBQyxLQUFLLENBQUMsR0FBRyxDQUFDLE9BQU8sQ0FBQyxDQUFDLENBQVcsQ0FBQyxDQUFDO2lCQUM1QztnQkFDRCxNQUFNO1lBQ1IsS0FBSyxZQUFZO2dCQUNmLElBQUksQ0FBQyxLQUFLLENBQUMsS0FBSyxDQUFDLHNDQUFzQyxDQUFDLENBQUM7Z0JBQ3pELE1BQU07WUFDUjtnQkFDRSxNQUFNO1NBQ1Q7SUFDSCxDQUFDO0lBRUQ7O09BRUc7SUFDSyxlQUFlO1FBQ3JCLElBQUksSUFBSSxDQUFDLFFBQVEsQ0FBQyxPQUFPLEVBQUU7WUFDekIsSUFBSSxDQUFDLFNBQVMsQ0FBQyxHQUFHLEVBQUUsQ0FBQztTQUN0QjtRQUNELElBQUksSUFBSSxDQUFDLFlBQVksS0FBSyxDQUFDLENBQUMsRUFBRTtZQUM1QixJQUFJLENBQUMsWUFBWSxHQUFHLElBQUksQ0FBQyxJQUFJLENBQUMsV0FBVyxDQUFDO1NBQzNDO1FBQ0QsSUFBSSxJQUFJLENBQUMsYUFBYSxLQUFLLENBQUMsQ0FBQyxFQUFFO1lBQzdCLElBQUksQ0FBQyxhQUFhLEdBQUcsSUFBSSxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUM7U0FDN0M7UUFDRCxJQUFJLENBQUMsZUFBZSxFQUFFLENBQUM7UUFDdkIsSUFBSSxDQUFDLFlBQVksR0FBRyxLQUFLLENBQUM7SUFDNUIsQ0FBQztJQUVEOztPQUVHO0lBQ0ssZUFBZTtRQUNyQixNQUFNLE9BQU8sR0FBRztZQUNkLElBQUksQ0FBQyxLQUFLLENBQUMsSUFBSTtZQUNmLElBQUksQ0FBQyxLQUFLLENBQUMsSUFBSTtZQUNmLElBQUksQ0FBQyxhQUFhO1lBQ2xCLElBQUksQ0FBQyxZQUFZO1NBQ2xCLENBQUM7UUFDRixJQUFJLENBQUMsSUFBSSxDQUFDLFVBQVUsRUFBRTtZQUNwQixJQUFJLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxFQUFFLElBQUksRUFBRSxVQUFVLEVBQUUsT0FBTyxFQUFFLENBQUMsQ0FBQztTQUNsRDtJQUNILENBQUM7Q0FVRjtBQUVEOztHQUVHO0FBQ0gsSUFBVSxPQUFPLENBOERoQjtBQTlERCxXQUFVLE9BQU87SUFDZjs7T0FFRztJQUNRLFVBQUUsR0FBRyxDQUFDLENBQUM7SUFFbEI7O09BRUc7SUFDVSxrQkFBVSxHQUEyQjtRQUNoRCxVQUFVLEVBQUUsTUFBTTtRQUNsQixVQUFVLEVBQUUsTUFBTTtRQUNsQixNQUFNLEVBQUUsU0FBUztRQUNqQixZQUFZLEVBQUUsU0FBUztRQUN2QixTQUFTLEVBQUUsdUJBQXVCLENBQUMsY0FBYztLQUNsRCxDQUFDO0lBRUY7O09BRUc7SUFDVSxpQkFBUyxHQUEyQjtRQUMvQyxVQUFVLEVBQUUsTUFBTTtRQUNsQixVQUFVLEVBQUUsTUFBTTtRQUNsQixNQUFNLEVBQUUsTUFBTTtRQUNkLFlBQVksRUFBRSxNQUFNO1FBQ3BCLFNBQVMsRUFBRSwwQkFBMEI7S0FDdEMsQ0FBQztJQUVGOztPQUVHO0lBQ1Usb0JBQVksR0FBRyxHQUEyQixFQUFFLENBQUMsQ0FBQztRQUN6RCxVQUFVLEVBQUUsZ0JBQWdCLENBQUMsUUFBUSxDQUFDLElBQUksQ0FBQzthQUN4QyxnQkFBZ0IsQ0FBQyxxQkFBcUIsQ0FBQzthQUN2QyxJQUFJLEVBQUU7UUFDVCxVQUFVLEVBQUUsZ0JBQWdCLENBQUMsUUFBUSxDQUFDLElBQUksQ0FBQzthQUN4QyxnQkFBZ0IsQ0FBQyxvQkFBb0IsQ0FBQzthQUN0QyxJQUFJLEVBQUU7UUFDVCxNQUFNLEVBQUUsZ0JBQWdCLENBQUMsUUFBUSxDQUFDLElBQUksQ0FBQzthQUNwQyxnQkFBZ0IsQ0FBQyxxQkFBcUIsQ0FBQzthQUN2QyxJQUFJLEVBQUU7UUFDVCxZQUFZLEVBQUUsZ0JBQWdCLENBQUMsUUFBUSxDQUFDLElBQUksQ0FBQzthQUMxQyxnQkFBZ0IsQ0FBQyw2QkFBNkIsQ0FBQzthQUMvQyxJQUFJLEVBQUU7UUFDVCxTQUFTLEVBQUUsZ0JBQWdCLENBQUMsUUFBUSxDQUFDLElBQUksQ0FBQzthQUN2QyxnQkFBZ0IsQ0FBQyxxQkFBcUIsQ0FBQzthQUN2QyxJQUFJLEVBQUU7S0FDVixDQUFDLENBQUM7SUFFSCxTQUFnQixhQUFhLENBQzNCLEtBQXNCO1FBRXRCLFFBQVEsS0FBSyxFQUFFO1lBQ2IsS0FBSyxPQUFPO2dCQUNWLE9BQU8sa0JBQVUsQ0FBQztZQUNwQixLQUFLLE1BQU07Z0JBQ1QsT0FBTyxpQkFBUyxDQUFDO1lBQ25CLEtBQUssU0FBUyxDQUFDO1lBQ2Y7Z0JBQ0UsT0FBTyxvQkFBWSxFQUFFLENBQUM7U0FDekI7SUFDSCxDQUFDO0lBWmUscUJBQWEsZ0JBWTVCO0FBQ0gsQ0FBQyxFQTlEUyxPQUFPLEtBQVAsT0FBTyxRQThEaEIiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvdGVybWluYWwvc3JjL3Rva2Vucy50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvdGVybWluYWwvc3JjL3dpZGdldC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElXaWRnZXRUcmFja2VyLCBNYWluQXJlYVdpZGdldCB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IFRlcm1pbmFsIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2VydmljZXMnO1xuaW1wb3J0IHsgVG9rZW4gfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuXG4vKipcbiAqIEEgY2xhc3MgdGhhdCB0cmFja3MgZWRpdG9yIHdpZGdldHMuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSVRlcm1pbmFsVHJhY2tlclxuICBleHRlbmRzIElXaWRnZXRUcmFja2VyPE1haW5BcmVhV2lkZ2V0PElUZXJtaW5hbC5JVGVybWluYWw+PiB7fVxuXG4vKipcbiAqIFRoZSBlZGl0b3IgdHJhY2tlciB0b2tlbi5cbiAqL1xuZXhwb3J0IGNvbnN0IElUZXJtaW5hbFRyYWNrZXIgPSBuZXcgVG9rZW48SVRlcm1pbmFsVHJhY2tlcj4oXG4gICdAanVweXRlcmxhYi90ZXJtaW5hbDpJVGVybWluYWxUcmFja2VyJ1xuKTtcblxuLyoqXG4gKiBUaGUgbmFtZXNwYWNlIGZvciB0ZXJtaW5hbHMuIFNlcGFyYXRlZCBmcm9tIHRoZSB3aWRnZXQgc28gaXQgY2FuIGJlIGxhenlcbiAqIGxvYWRlZC5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBJVGVybWluYWwge1xuICBleHBvcnQgaW50ZXJmYWNlIElUZXJtaW5hbCBleHRlbmRzIFdpZGdldCB7XG4gICAgLyoqXG4gICAgICogVGhlIHRlcm1pbmFsIHNlc3Npb24gYXNzb2NpYXRlZCB3aXRoIHRoZSB3aWRnZXQuXG4gICAgICovXG4gICAgc2Vzc2lvbjogVGVybWluYWwuSVRlcm1pbmFsQ29ubmVjdGlvbjtcblxuICAgIC8qKlxuICAgICAqIEdldCBhIGNvbmZpZyBvcHRpb24gZm9yIHRoZSB0ZXJtaW5hbC5cbiAgICAgKi9cbiAgICBnZXRPcHRpb248SyBleHRlbmRzIGtleW9mIElPcHRpb25zPihvcHRpb246IEspOiBJT3B0aW9uc1tLXTtcblxuICAgIC8qKlxuICAgICAqIFNldCBhIGNvbmZpZyBvcHRpb24gZm9yIHRoZSB0ZXJtaW5hbC5cbiAgICAgKi9cbiAgICBzZXRPcHRpb248SyBleHRlbmRzIGtleW9mIElPcHRpb25zPihvcHRpb246IEssIHZhbHVlOiBJT3B0aW9uc1tLXSk6IHZvaWQ7XG5cbiAgICAvKipcbiAgICAgKiBSZWZyZXNoIHRoZSB0ZXJtaW5hbCBzZXNzaW9uLlxuICAgICAqL1xuICAgIHJlZnJlc2goKTogUHJvbWlzZTx2b2lkPjtcbiAgfVxuICAvKipcbiAgICogT3B0aW9ucyBmb3IgdGhlIHRlcm1pbmFsIHdpZGdldC5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMge1xuICAgIC8qKlxuICAgICAqIFRoZSBmb250IGZhbWlseSB1c2VkIHRvIHJlbmRlciB0ZXh0LlxuICAgICAqL1xuICAgIGZvbnRGYW1pbHk/OiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgZm9udCBzaXplIG9mIHRoZSB0ZXJtaW5hbCBpbiBwaXhlbHMuXG4gICAgICovXG4gICAgZm9udFNpemU6IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBsaW5lIGhlaWdodCB1c2VkIHRvIHJlbmRlciB0ZXh0LlxuICAgICAqL1xuICAgIGxpbmVIZWlnaHQ/OiBudW1iZXI7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgdGhlbWUgb2YgdGhlIHRlcm1pbmFsLlxuICAgICAqL1xuICAgIHRoZW1lOiBUaGVtZTtcblxuICAgIC8qKlxuICAgICAqIFRoZSBhbW91bnQgb2YgYnVmZmVyIHNjcm9sbGJhY2sgdG8gYmUgdXNlZFxuICAgICAqIHdpdGggdGhlIHRlcm1pbmFsXG4gICAgICovXG4gICAgc2Nyb2xsYmFjaz86IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFdoZXRoZXIgdG8gc2h1dCBkb3duIHRoZSBzZXNzaW9uIHdoZW4gY2xvc2luZyBhIHRlcm1pbmFsIG9yIG5vdC5cbiAgICAgKi9cbiAgICBzaHV0ZG93bk9uQ2xvc2U6IGJvb2xlYW47XG5cbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIHRvIGNsb3NlIHRoZSB3aWRnZXQgd2hlbiBleGl0aW5nIGEgdGVybWluYWwgb3Igbm90LlxuICAgICAqL1xuICAgIGNsb3NlT25FeGl0OiBib29sZWFuO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0byBibGluayB0aGUgY3Vyc29yLiAgQ2FuIG9ubHkgYmUgc2V0IGF0IHN0YXJ0dXAuXG4gICAgICovXG4gICAgY3Vyc29yQmxpbms6IGJvb2xlYW47XG5cbiAgICAvKipcbiAgICAgKiBBbiBvcHRpb25hbCBjb21tYW5kIHRvIHJ1biB3aGVuIHRoZSBzZXNzaW9uIHN0YXJ0cy5cbiAgICAgKi9cbiAgICBpbml0aWFsQ29tbWFuZDogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0byBlbmFibGUgc2NyZWVuIHJlYWRlciBzdXBwb3J0LlxuICAgICAqL1xuICAgIHNjcmVlblJlYWRlck1vZGU6IGJvb2xlYW47XG5cbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIHRvIGVuYWJsZSB1c2luZyBDdHJsK1YgdG8gcGFzdGUuXG4gICAgICpcbiAgICAgKiBUaGlzIHNldHRpbmcgaGFzIG5vIGVmZmVjdCBvbiBtYWNPUywgd2hlcmUgQ21kK1YgaXMgYXZhaWxhYmxlLlxuICAgICAqL1xuICAgIHBhc3RlV2l0aEN0cmxWOiBib29sZWFuO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0byBhdXRvLWZpdCB0aGUgdGVybWluYWwgdG8gaXRzIGhvc3QgZWxlbWVudCBzaXplLlxuICAgICAqL1xuICAgIGF1dG9GaXQ/OiBib29sZWFuO1xuXG4gICAgLyoqXG4gICAgICogVHJlYXQgb3B0aW9uIGFzIG1ldGEga2V5IG9uIG1hY09TLlxuICAgICAqL1xuICAgIG1hY09wdGlvbklzTWV0YT86IGJvb2xlYW47XG4gIH1cblxuICAvKipcbiAgICogVGhlIGRlZmF1bHQgb3B0aW9ucyB1c2VkIGZvciBjcmVhdGluZyB0ZXJtaW5hbHMuXG4gICAqL1xuICBleHBvcnQgY29uc3QgZGVmYXVsdE9wdGlvbnM6IElPcHRpb25zID0ge1xuICAgIHRoZW1lOiAnaW5oZXJpdCcsXG4gICAgZm9udEZhbWlseTogJ01lbmxvLCBDb25zb2xhcywgXCJEZWphVnUgU2FucyBNb25vXCIsIG1vbm9zcGFjZScsXG4gICAgZm9udFNpemU6IDEzLFxuICAgIGxpbmVIZWlnaHQ6IDEuMCxcbiAgICBzY3JvbGxiYWNrOiAxMDAwLFxuICAgIHNodXRkb3duT25DbG9zZTogZmFsc2UsXG4gICAgY2xvc2VPbkV4aXQ6IHRydWUsXG4gICAgY3Vyc29yQmxpbms6IHRydWUsXG4gICAgaW5pdGlhbENvbW1hbmQ6ICcnLFxuICAgIHNjcmVlblJlYWRlck1vZGU6IGZhbHNlLCAvLyBGYWxzZSBieSBkZWZhdWx0LCBjYW4gY2F1c2Ugc2Nyb2xsYmFyIG1vdXNlIGludGVyYWN0aW9uIGlzc3Vlcy5cbiAgICBwYXN0ZVdpdGhDdHJsVjogdHJ1ZSxcbiAgICBhdXRvRml0OiB0cnVlLFxuICAgIG1hY09wdGlvbklzTWV0YTogZmFsc2VcbiAgfTtcblxuICAvKipcbiAgICogQSB0eXBlIGZvciB0aGUgdGVybWluYWwgdGhlbWUuXG4gICAqL1xuICBleHBvcnQgdHlwZSBUaGVtZSA9ICdsaWdodCcgfCAnZGFyaycgfCAnaW5oZXJpdCc7XG5cbiAgLyoqXG4gICAqIEEgdHlwZSBmb3IgdGhlIHRlcm1pbmFsIHRoZW1lLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJVGhlbWVPYmplY3Qge1xuICAgIGZvcmVncm91bmQ6IHN0cmluZztcbiAgICBiYWNrZ3JvdW5kOiBzdHJpbmc7XG4gICAgY3Vyc29yOiBzdHJpbmc7XG4gICAgY3Vyc29yQWNjZW50OiBzdHJpbmc7XG4gICAgc2VsZWN0aW9uOiBzdHJpbmc7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgVGVybWluYWwgYXMgVGVybWluYWxOUyB9IGZyb20gJ0BqdXB5dGVybGFiL3NlcnZpY2VzJztcbmltcG9ydCB7XG4gIElUcmFuc2xhdG9yLFxuICBudWxsVHJhbnNsYXRvcixcbiAgVHJhbnNsYXRpb25CdW5kbGVcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgUGxhdGZvcm0gfSBmcm9tICdAbHVtaW5vL2RvbXV0aWxzJztcbmltcG9ydCB7IE1lc3NhZ2UsIE1lc3NhZ2VMb29wIH0gZnJvbSAnQGx1bWluby9tZXNzYWdpbmcnO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IFRlcm1pbmFsIGFzIFh0ZXJtIH0gZnJvbSAneHRlcm0nO1xuaW1wb3J0IHsgRml0QWRkb24gfSBmcm9tICd4dGVybS1hZGRvbi1maXQnO1xuaW1wb3J0IHsgSVRlcm1pbmFsIH0gZnJvbSAnLic7XG5cbi8qKlxuICogVGhlIGNsYXNzIG5hbWUgYWRkZWQgdG8gYSB0ZXJtaW5hbCB3aWRnZXQuXG4gKi9cbmNvbnN0IFRFUk1JTkFMX0NMQVNTID0gJ2pwLVRlcm1pbmFsJztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCB0byBhIHRlcm1pbmFsIGJvZHkuXG4gKi9cbmNvbnN0IFRFUk1JTkFMX0JPRFlfQ0xBU1MgPSAnanAtVGVybWluYWwtYm9keSc7XG5cbi8qKlxuICogQSB3aWRnZXQgd2hpY2ggbWFuYWdlcyBhIHRlcm1pbmFsIHNlc3Npb24uXG4gKi9cbmV4cG9ydCBjbGFzcyBUZXJtaW5hbCBleHRlbmRzIFdpZGdldCBpbXBsZW1lbnRzIElUZXJtaW5hbC5JVGVybWluYWwge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IHRlcm1pbmFsIHdpZGdldC5cbiAgICpcbiAgICogQHBhcmFtIHNlc3Npb24gLSBUaGUgdGVybWluYWwgc2Vzc2lvbiBvYmplY3QuXG4gICAqXG4gICAqIEBwYXJhbSBvcHRpb25zIC0gVGhlIHRlcm1pbmFsIGNvbmZpZ3VyYXRpb24gb3B0aW9ucy5cbiAgICpcbiAgICogQHBhcmFtIHRyYW5zbGF0b3IgLSBUaGUgbGFuZ3VhZ2UgdHJhbnNsYXRvci5cbiAgICovXG4gIGNvbnN0cnVjdG9yKFxuICAgIHNlc3Npb246IFRlcm1pbmFsTlMuSVRlcm1pbmFsQ29ubmVjdGlvbixcbiAgICBvcHRpb25zOiBQYXJ0aWFsPElUZXJtaW5hbC5JT3B0aW9ucz4gPSB7fSxcbiAgICB0cmFuc2xhdG9yPzogSVRyYW5zbGF0b3JcbiAgKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0cmFuc2xhdG9yID0gdHJhbnNsYXRvciB8fCBudWxsVHJhbnNsYXRvcjtcbiAgICB0aGlzLl90cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIHRoaXMuc2Vzc2lvbiA9IHNlc3Npb247XG5cbiAgICAvLyBJbml0aWFsaXplIHNldHRpbmdzLlxuICAgIHRoaXMuX29wdGlvbnMgPSB7IC4uLklUZXJtaW5hbC5kZWZhdWx0T3B0aW9ucywgLi4ub3B0aW9ucyB9O1xuXG4gICAgY29uc3QgeyB0aGVtZSwgLi4ub3RoZXIgfSA9IHRoaXMuX29wdGlvbnM7XG4gICAgY29uc3QgeHRlcm1PcHRpb25zID0ge1xuICAgICAgdGhlbWU6IFByaXZhdGUuZ2V0WFRlcm1UaGVtZSh0aGVtZSksXG4gICAgICAuLi5vdGhlclxuICAgIH07XG5cbiAgICB0aGlzLmFkZENsYXNzKFRFUk1JTkFMX0NMQVNTKTtcblxuICAgIHRoaXMuX3NldFRoZW1lQXR0cmlidXRlKHRoZW1lKTtcblxuICAgIC8vIENyZWF0ZSB0aGUgeHRlcm0uXG4gICAgdGhpcy5fdGVybSA9IG5ldyBYdGVybSh4dGVybU9wdGlvbnMpO1xuICAgIHRoaXMuX2ZpdEFkZG9uID0gbmV3IEZpdEFkZG9uKCk7XG4gICAgdGhpcy5fdGVybS5sb2FkQWRkb24odGhpcy5fZml0QWRkb24pO1xuXG4gICAgdGhpcy5faW5pdGlhbGl6ZVRlcm0oKTtcblxuICAgIHRoaXMuaWQgPSBganAtVGVybWluYWwtJHtQcml2YXRlLmlkKyt9YDtcbiAgICB0aGlzLnRpdGxlLmxhYmVsID0gdGhpcy5fdHJhbnMuX18oJ1Rlcm1pbmFsJyk7XG5cbiAgICBzZXNzaW9uLm1lc3NhZ2VSZWNlaXZlZC5jb25uZWN0KHRoaXMuX29uTWVzc2FnZSwgdGhpcyk7XG4gICAgc2Vzc2lvbi5kaXNwb3NlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgIGlmICh0aGlzLmdldE9wdGlvbignY2xvc2VPbkV4aXQnKSkge1xuICAgICAgICB0aGlzLmRpc3Bvc2UoKTtcbiAgICAgIH1cbiAgICB9LCB0aGlzKTtcblxuICAgIGlmIChzZXNzaW9uLmNvbm5lY3Rpb25TdGF0dXMgPT09ICdjb25uZWN0ZWQnKSB7XG4gICAgICB0aGlzLl9pbml0aWFsQ29ubmVjdGlvbigpO1xuICAgIH0gZWxzZSB7XG4gICAgICBzZXNzaW9uLmNvbm5lY3Rpb25TdGF0dXNDaGFuZ2VkLmNvbm5lY3QodGhpcy5faW5pdGlhbENvbm5lY3Rpb24sIHRoaXMpO1xuICAgIH1cbiAgfVxuXG4gIHByaXZhdGUgX3NldFRoZW1lQXR0cmlidXRlKHRoZW1lOiBzdHJpbmcgfCBudWxsIHwgdW5kZWZpbmVkKSB7XG4gICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIHRoaXMubm9kZS5zZXRBdHRyaWJ1dGUoXG4gICAgICAnZGF0YS10ZXJtLXRoZW1lJyxcbiAgICAgIHRoZW1lID8gdGhlbWUudG9Mb3dlckNhc2UoKSA6ICdpbmhlcml0J1xuICAgICk7XG4gIH1cblxuICBwcml2YXRlIF9pbml0aWFsQ29ubmVjdGlvbigpIHtcbiAgICBpZiAodGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgaWYgKHRoaXMuc2Vzc2lvbi5jb25uZWN0aW9uU3RhdHVzICE9PSAnY29ubmVjdGVkJykge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIHRoaXMudGl0bGUubGFiZWwgPSB0aGlzLl90cmFucy5fXygnVGVybWluYWwgJTEnLCB0aGlzLnNlc3Npb24ubmFtZSk7XG4gICAgdGhpcy5fc2V0U2Vzc2lvblNpemUoKTtcbiAgICBpZiAodGhpcy5fb3B0aW9ucy5pbml0aWFsQ29tbWFuZCkge1xuICAgICAgdGhpcy5zZXNzaW9uLnNlbmQoe1xuICAgICAgICB0eXBlOiAnc3RkaW4nLFxuICAgICAgICBjb250ZW50OiBbdGhpcy5fb3B0aW9ucy5pbml0aWFsQ29tbWFuZCArICdcXHInXVxuICAgICAgfSk7XG4gICAgfVxuXG4gICAgLy8gT25seSBydW4gdGhpcyBpbml0aWFsIGNvbm5lY3Rpb24gbG9naWMgb25jZS5cbiAgICB0aGlzLnNlc3Npb24uY29ubmVjdGlvblN0YXR1c0NoYW5nZWQuZGlzY29ubmVjdChcbiAgICAgIHRoaXMuX2luaXRpYWxDb25uZWN0aW9uLFxuICAgICAgdGhpc1xuICAgICk7XG4gIH1cblxuICAvKipcbiAgICogVGhlIHRlcm1pbmFsIHNlc3Npb24gYXNzb2NpYXRlZCB3aXRoIHRoZSB3aWRnZXQuXG4gICAqL1xuICByZWFkb25seSBzZXNzaW9uOiBUZXJtaW5hbE5TLklUZXJtaW5hbENvbm5lY3Rpb247XG5cbiAgLyoqXG4gICAqIEdldCBhIGNvbmZpZyBvcHRpb24gZm9yIHRoZSB0ZXJtaW5hbC5cbiAgICovXG4gIGdldE9wdGlvbjxLIGV4dGVuZHMga2V5b2YgSVRlcm1pbmFsLklPcHRpb25zPihcbiAgICBvcHRpb246IEtcbiAgKTogSVRlcm1pbmFsLklPcHRpb25zW0tdIHtcbiAgICByZXR1cm4gdGhpcy5fb3B0aW9uc1tvcHRpb25dO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldCBhIGNvbmZpZyBvcHRpb24gZm9yIHRoZSB0ZXJtaW5hbC5cbiAgICovXG4gIHNldE9wdGlvbjxLIGV4dGVuZHMga2V5b2YgSVRlcm1pbmFsLklPcHRpb25zPihcbiAgICBvcHRpb246IEssXG4gICAgdmFsdWU6IElUZXJtaW5hbC5JT3B0aW9uc1tLXVxuICApOiB2b2lkIHtcbiAgICBpZiAoXG4gICAgICBvcHRpb24gIT09ICd0aGVtZScgJiZcbiAgICAgICh0aGlzLl9vcHRpb25zW29wdGlvbl0gPT09IHZhbHVlIHx8IG9wdGlvbiA9PT0gJ2luaXRpYWxDb21tYW5kJylcbiAgICApIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICB0aGlzLl9vcHRpb25zW29wdGlvbl0gPSB2YWx1ZTtcblxuICAgIHN3aXRjaCAob3B0aW9uKSB7XG4gICAgICBjYXNlICdzaHV0ZG93bk9uQ2xvc2UnOiAvLyBEbyBub3QgdHJhbnNtaXQgdG8gWFRlcm1cbiAgICAgIGNhc2UgJ2Nsb3NlT25FeGl0JzogLy8gRG8gbm90IHRyYW5zbWl0IHRvIFhUZXJtXG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAndGhlbWUnOlxuICAgICAgICB0aGlzLl90ZXJtLnNldE9wdGlvbihcbiAgICAgICAgICAndGhlbWUnLFxuICAgICAgICAgIFByaXZhdGUuZ2V0WFRlcm1UaGVtZSh2YWx1ZSBhcyBJVGVybWluYWwuVGhlbWUpXG4gICAgICAgICk7XG4gICAgICAgIHRoaXMuX3NldFRoZW1lQXR0cmlidXRlKHZhbHVlIGFzIElUZXJtaW5hbC5UaGVtZSk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgZGVmYXVsdDpcbiAgICAgICAgdGhpcy5fdGVybS5zZXRPcHRpb24ob3B0aW9uLCB2YWx1ZSk7XG4gICAgICAgIGJyZWFrO1xuICAgIH1cblxuICAgIHRoaXMuX25lZWRzUmVzaXplID0gdHJ1ZTtcbiAgICB0aGlzLnVwZGF0ZSgpO1xuICB9XG5cbiAgLyoqXG4gICAqIERpc3Bvc2Ugb2YgdGhlIHJlc291cmNlcyBoZWxkIGJ5IHRoZSB0ZXJtaW5hbCB3aWRnZXQuXG4gICAqL1xuICBkaXNwb3NlKCk6IHZvaWQge1xuICAgIGlmICghdGhpcy5zZXNzaW9uLmlzRGlzcG9zZWQpIHtcbiAgICAgIGlmICh0aGlzLmdldE9wdGlvbignc2h1dGRvd25PbkNsb3NlJykpIHtcbiAgICAgICAgdGhpcy5zZXNzaW9uLnNodXRkb3duKCkuY2F0Y2gocmVhc29uID0+IHtcbiAgICAgICAgICBjb25zb2xlLmVycm9yKGBUZXJtaW5hbCBub3Qgc2h1dCBkb3duOiAke3JlYXNvbn1gKTtcbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfVxuICAgIHRoaXMuX3Rlcm0uZGlzcG9zZSgpO1xuICAgIHN1cGVyLmRpc3Bvc2UoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZWZyZXNoIHRoZSB0ZXJtaW5hbCBzZXNzaW9uLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIEZhaWx1cmUgdG8gcmVjb25uZWN0IHRvIHRoZSBzZXNzaW9uIHNob3VsZCBiZSBjYXVnaHQgYXBwcm9wcmlhdGVseVxuICAgKi9cbiAgYXN5bmMgcmVmcmVzaCgpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBpZiAoIXRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgYXdhaXQgdGhpcy5zZXNzaW9uLnJlY29ubmVjdCgpO1xuICAgICAgdGhpcy5fdGVybS5jbGVhcigpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBQcm9jZXNzIGEgbWVzc2FnZSBzZW50IHRvIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSBtc2cgLSBUaGUgbWVzc2FnZSBzZW50IHRvIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogU3ViY2xhc3NlcyBtYXkgcmVpbXBsZW1lbnQgdGhpcyBtZXRob2QgYXMgbmVlZGVkLlxuICAgKi9cbiAgcHJvY2Vzc01lc3NhZ2UobXNnOiBNZXNzYWdlKTogdm9pZCB7XG4gICAgc3VwZXIucHJvY2Vzc01lc3NhZ2UobXNnKTtcbiAgICBzd2l0Y2ggKG1zZy50eXBlKSB7XG4gICAgICBjYXNlICdmaXQtcmVxdWVzdCc6XG4gICAgICAgIHRoaXMub25GaXRSZXF1ZXN0KG1zZyk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgZGVmYXVsdDpcbiAgICAgICAgYnJlYWs7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFNldCB0aGUgc2l6ZSBvZiB0aGUgdGVybWluYWwgd2hlbiBhdHRhY2hlZCBpZiBkaXJ0eS5cbiAgICovXG4gIHByb3RlY3RlZCBvbkFmdGVyQXR0YWNoKG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIHRoaXMudXBkYXRlKCk7XG4gIH1cblxuICAvKipcbiAgICogU2V0IHRoZSBzaXplIG9mIHRoZSB0ZXJtaW5hbCB3aGVuIHNob3duIGlmIGRpcnR5LlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQWZ0ZXJTaG93KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIHRoaXMudXBkYXRlKCk7XG4gIH1cblxuICAvKipcbiAgICogT24gcmVzaXplLCB1c2UgdGhlIGNvbXB1dGVkIHJvdyBhbmQgY29sdW1uIHNpemVzIHRvIHJlc2l6ZSB0aGUgdGVybWluYWwuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25SZXNpemUobXNnOiBXaWRnZXQuUmVzaXplTWVzc2FnZSk6IHZvaWQge1xuICAgIHRoaXMuX29mZnNldFdpZHRoID0gbXNnLndpZHRoO1xuICAgIHRoaXMuX29mZnNldEhlaWdodCA9IG1zZy5oZWlnaHQ7XG4gICAgdGhpcy5fbmVlZHNSZXNpemUgPSB0cnVlO1xuICAgIHRoaXMudXBkYXRlKCk7XG4gIH1cblxuICAvKipcbiAgICogQSBtZXNzYWdlIGhhbmRsZXIgaW52b2tlZCBvbiBhbiBgJ3VwZGF0ZS1yZXF1ZXN0J2AgbWVzc2FnZS5cbiAgICovXG4gIHByb3RlY3RlZCBvblVwZGF0ZVJlcXVlc3QobXNnOiBNZXNzYWdlKTogdm9pZCB7XG4gICAgaWYgKCF0aGlzLmlzVmlzaWJsZSB8fCAhdGhpcy5pc0F0dGFjaGVkKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgLy8gT3BlbiB0aGUgdGVybWluYWwgaWYgbmVjZXNzYXJ5LlxuICAgIGlmICghdGhpcy5fdGVybU9wZW5lZCkge1xuICAgICAgdGhpcy5fdGVybS5vcGVuKHRoaXMubm9kZSk7XG4gICAgICB0aGlzLl90ZXJtLmVsZW1lbnQ/LmNsYXNzTGlzdC5hZGQoVEVSTUlOQUxfQk9EWV9DTEFTUyk7XG4gICAgICB0aGlzLl90ZXJtT3BlbmVkID0gdHJ1ZTtcbiAgICB9XG5cbiAgICBpZiAodGhpcy5fbmVlZHNSZXNpemUpIHtcbiAgICAgIHRoaXMuX3Jlc2l6ZVRlcm1pbmFsKCk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEEgbWVzc2FnZSBoYW5kbGVyIGludm9rZWQgb24gYW4gYCdmaXQtcmVxdWVzdCdgIG1lc3NhZ2UuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25GaXRSZXF1ZXN0KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIGNvbnN0IHJlc2l6ZSA9IFdpZGdldC5SZXNpemVNZXNzYWdlLlVua25vd25TaXplO1xuICAgIE1lc3NhZ2VMb29wLnNlbmRNZXNzYWdlKHRoaXMsIHJlc2l6ZSk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGAnYWN0aXZhdGUtcmVxdWVzdCdgIG1lc3NhZ2VzLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQWN0aXZhdGVSZXF1ZXN0KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIHRoaXMuX3Rlcm0uZm9jdXMoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBJbml0aWFsaXplIHRoZSB0ZXJtaW5hbCBvYmplY3QuXG4gICAqL1xuICBwcml2YXRlIF9pbml0aWFsaXplVGVybSgpOiB2b2lkIHtcbiAgICBjb25zdCB0ZXJtID0gdGhpcy5fdGVybTtcbiAgICB0ZXJtLm9uRGF0YSgoZGF0YTogc3RyaW5nKSA9PiB7XG4gICAgICBpZiAodGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIHRoaXMuc2Vzc2lvbi5zZW5kKHtcbiAgICAgICAgdHlwZTogJ3N0ZGluJyxcbiAgICAgICAgY29udGVudDogW2RhdGFdXG4gICAgICB9KTtcbiAgICB9KTtcblxuICAgIHRlcm0ub25UaXRsZUNoYW5nZSgodGl0bGU6IHN0cmluZykgPT4ge1xuICAgICAgdGhpcy50aXRsZS5sYWJlbCA9IHRpdGxlO1xuICAgIH0pO1xuXG4gICAgLy8gRG8gbm90IGFkZCBhbnkgQ3RybCtDL0N0cmwrViBoYW5kbGluZyBvbiBtYWNPUyxcbiAgICAvLyB3aGVyZSBDbWQrQy9DbWQrViB3b3JrcyBhcyBpbnRlbmRlZC5cbiAgICBpZiAoUGxhdGZvcm0uSVNfTUFDKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgdGVybS5hdHRhY2hDdXN0b21LZXlFdmVudEhhbmRsZXIoZXZlbnQgPT4ge1xuICAgICAgaWYgKGV2ZW50LmN0cmxLZXkgJiYgZXZlbnQua2V5ID09PSAnYycgJiYgdGVybS5oYXNTZWxlY3Rpb24oKSkge1xuICAgICAgICAvLyBSZXR1cm4gc28gdGhhdCB0aGUgdXN1YWwgT1MgY29weSBoYXBwZW5zXG4gICAgICAgIC8vIGluc3RlYWQgb2YgaW50ZXJydXB0IHNpZ25hbC5cbiAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgfVxuXG4gICAgICBpZiAoZXZlbnQuY3RybEtleSAmJiBldmVudC5rZXkgPT09ICd2JyAmJiB0aGlzLl9vcHRpb25zLnBhc3RlV2l0aEN0cmxWKSB7XG4gICAgICAgIC8vIFJldHVybiBzbyB0aGF0IHRoZSB1c3VhbCBwYXN0ZSBoYXBwZW5zLlxuICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICB9XG5cbiAgICAgIHJldHVybiB0cnVlO1xuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBhIG1lc3NhZ2UgZnJvbSB0aGUgdGVybWluYWwgc2Vzc2lvbi5cbiAgICovXG4gIHByaXZhdGUgX29uTWVzc2FnZShcbiAgICBzZW5kZXI6IFRlcm1pbmFsTlMuSVRlcm1pbmFsQ29ubmVjdGlvbixcbiAgICBtc2c6IFRlcm1pbmFsTlMuSU1lc3NhZ2VcbiAgKTogdm9pZCB7XG4gICAgc3dpdGNoIChtc2cudHlwZSkge1xuICAgICAgY2FzZSAnc3Rkb3V0JzpcbiAgICAgICAgaWYgKG1zZy5jb250ZW50KSB7XG4gICAgICAgICAgdGhpcy5fdGVybS53cml0ZShtc2cuY29udGVudFswXSBhcyBzdHJpbmcpO1xuICAgICAgICB9XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnZGlzY29ubmVjdCc6XG4gICAgICAgIHRoaXMuX3Rlcm0ud3JpdGUoJ1xcclxcblxcclxcbltGaW5pc2hlZOKApiBUZXJtIFNlc3Npb25dXFxyXFxuJyk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgZGVmYXVsdDpcbiAgICAgICAgYnJlYWs7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFJlc2l6ZSB0aGUgdGVybWluYWwgYmFzZWQgb24gY29tcHV0ZWQgZ2VvbWV0cnkuXG4gICAqL1xuICBwcml2YXRlIF9yZXNpemVUZXJtaW5hbCgpIHtcbiAgICBpZiAodGhpcy5fb3B0aW9ucy5hdXRvRml0KSB7XG4gICAgICB0aGlzLl9maXRBZGRvbi5maXQoKTtcbiAgICB9XG4gICAgaWYgKHRoaXMuX29mZnNldFdpZHRoID09PSAtMSkge1xuICAgICAgdGhpcy5fb2Zmc2V0V2lkdGggPSB0aGlzLm5vZGUub2Zmc2V0V2lkdGg7XG4gICAgfVxuICAgIGlmICh0aGlzLl9vZmZzZXRIZWlnaHQgPT09IC0xKSB7XG4gICAgICB0aGlzLl9vZmZzZXRIZWlnaHQgPSB0aGlzLm5vZGUub2Zmc2V0SGVpZ2h0O1xuICAgIH1cbiAgICB0aGlzLl9zZXRTZXNzaW9uU2l6ZSgpO1xuICAgIHRoaXMuX25lZWRzUmVzaXplID0gZmFsc2U7XG4gIH1cblxuICAvKipcbiAgICogU2V0IHRoZSBzaXplIG9mIHRoZSB0ZXJtaW5hbCBpbiB0aGUgc2Vzc2lvbi5cbiAgICovXG4gIHByaXZhdGUgX3NldFNlc3Npb25TaXplKCk6IHZvaWQge1xuICAgIGNvbnN0IGNvbnRlbnQgPSBbXG4gICAgICB0aGlzLl90ZXJtLnJvd3MsXG4gICAgICB0aGlzLl90ZXJtLmNvbHMsXG4gICAgICB0aGlzLl9vZmZzZXRIZWlnaHQsXG4gICAgICB0aGlzLl9vZmZzZXRXaWR0aFxuICAgIF07XG4gICAgaWYgKCF0aGlzLmlzRGlzcG9zZWQpIHtcbiAgICAgIHRoaXMuc2Vzc2lvbi5zZW5kKHsgdHlwZTogJ3NldF9zaXplJywgY29udGVudCB9KTtcbiAgICB9XG4gIH1cblxuICBwcml2YXRlIHJlYWRvbmx5IF90ZXJtOiBYdGVybTtcbiAgcHJpdmF0ZSByZWFkb25seSBfZml0QWRkb246IEZpdEFkZG9uO1xuICBwcml2YXRlIF90cmFuczogVHJhbnNsYXRpb25CdW5kbGU7XG4gIHByaXZhdGUgX25lZWRzUmVzaXplID0gdHJ1ZTtcbiAgcHJpdmF0ZSBfdGVybU9wZW5lZCA9IGZhbHNlO1xuICBwcml2YXRlIF9vZmZzZXRXaWR0aCA9IC0xO1xuICBwcml2YXRlIF9vZmZzZXRIZWlnaHQgPSAtMTtcbiAgcHJpdmF0ZSBfb3B0aW9uczogSVRlcm1pbmFsLklPcHRpb25zO1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBwcml2YXRlIGRhdGEuXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgLyoqXG4gICAqIEFuIGluY3JlbWVudGluZyBjb3VudGVyIGZvciBpZHMuXG4gICAqL1xuICBleHBvcnQgbGV0IGlkID0gMDtcblxuICAvKipcbiAgICogVGhlIGxpZ2h0IHRlcm1pbmFsIHRoZW1lLlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IGxpZ2h0VGhlbWU6IElUZXJtaW5hbC5JVGhlbWVPYmplY3QgPSB7XG4gICAgZm9yZWdyb3VuZDogJyMwMDAnLFxuICAgIGJhY2tncm91bmQ6ICcjZmZmJyxcbiAgICBjdXJzb3I6ICcjNjE2MTYxJywgLy8gbWQtZ3JleS03MDBcbiAgICBjdXJzb3JBY2NlbnQ6ICcjRjVGNUY1JywgLy8gbWQtZ3JleS0xMDBcbiAgICBzZWxlY3Rpb246ICdyZ2JhKDk3LCA5NywgOTcsIDAuMyknIC8vIG1kLWdyZXktNzAwXG4gIH07XG5cbiAgLyoqXG4gICAqIFRoZSBkYXJrIHRlcm1pbmFsIHRoZW1lLlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IGRhcmtUaGVtZTogSVRlcm1pbmFsLklUaGVtZU9iamVjdCA9IHtcbiAgICBmb3JlZ3JvdW5kOiAnI2ZmZicsXG4gICAgYmFja2dyb3VuZDogJyMwMDAnLFxuICAgIGN1cnNvcjogJyNmZmYnLFxuICAgIGN1cnNvckFjY2VudDogJyMwMDAnLFxuICAgIHNlbGVjdGlvbjogJ3JnYmEoMjU1LCAyNTUsIDI1NSwgMC4zKSdcbiAgfTtcblxuICAvKipcbiAgICogVGhlIGN1cnJlbnQgdGhlbWUuXG4gICAqL1xuICBleHBvcnQgY29uc3QgaW5oZXJpdFRoZW1lID0gKCk6IElUZXJtaW5hbC5JVGhlbWVPYmplY3QgPT4gKHtcbiAgICBmb3JlZ3JvdW5kOiBnZXRDb21wdXRlZFN0eWxlKGRvY3VtZW50LmJvZHkpXG4gICAgICAuZ2V0UHJvcGVydHlWYWx1ZSgnLS1qcC11aS1mb250LWNvbG9yMCcpXG4gICAgICAudHJpbSgpLFxuICAgIGJhY2tncm91bmQ6IGdldENvbXB1dGVkU3R5bGUoZG9jdW1lbnQuYm9keSlcbiAgICAgIC5nZXRQcm9wZXJ0eVZhbHVlKCctLWpwLWxheW91dC1jb2xvcjAnKVxuICAgICAgLnRyaW0oKSxcbiAgICBjdXJzb3I6IGdldENvbXB1dGVkU3R5bGUoZG9jdW1lbnQuYm9keSlcbiAgICAgIC5nZXRQcm9wZXJ0eVZhbHVlKCctLWpwLXVpLWZvbnQtY29sb3IxJylcbiAgICAgIC50cmltKCksXG4gICAgY3Vyc29yQWNjZW50OiBnZXRDb21wdXRlZFN0eWxlKGRvY3VtZW50LmJvZHkpXG4gICAgICAuZ2V0UHJvcGVydHlWYWx1ZSgnLS1qcC11aS1pbnZlcnNlLWZvbnQtY29sb3IwJylcbiAgICAgIC50cmltKCksXG4gICAgc2VsZWN0aW9uOiBnZXRDb21wdXRlZFN0eWxlKGRvY3VtZW50LmJvZHkpXG4gICAgICAuZ2V0UHJvcGVydHlWYWx1ZSgnLS1qcC11aS1mb250LWNvbG9yMycpXG4gICAgICAudHJpbSgpXG4gIH0pO1xuXG4gIGV4cG9ydCBmdW5jdGlvbiBnZXRYVGVybVRoZW1lKFxuICAgIHRoZW1lOiBJVGVybWluYWwuVGhlbWVcbiAgKTogSVRlcm1pbmFsLklUaGVtZU9iamVjdCB7XG4gICAgc3dpdGNoICh0aGVtZSkge1xuICAgICAgY2FzZSAnbGlnaHQnOlxuICAgICAgICByZXR1cm4gbGlnaHRUaGVtZTtcbiAgICAgIGNhc2UgJ2RhcmsnOlxuICAgICAgICByZXR1cm4gZGFya1RoZW1lO1xuICAgICAgY2FzZSAnaW5oZXJpdCc6XG4gICAgICBkZWZhdWx0OlxuICAgICAgICByZXR1cm4gaW5oZXJpdFRoZW1lKCk7XG4gICAgfVxuICB9XG59XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=