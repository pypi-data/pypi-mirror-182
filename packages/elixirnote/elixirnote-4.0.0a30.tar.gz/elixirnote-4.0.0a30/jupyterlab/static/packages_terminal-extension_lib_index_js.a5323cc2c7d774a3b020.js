"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_terminal-extension_lib_index_js"],{

/***/ "../../packages/terminal-extension/lib/index.js":
/*!******************************************************!*\
  !*** ../../packages/terminal-extension/lib/index.js ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "addCommands": () => (/* binding */ addCommands),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/mainmenu */ "webpack/sharing/consume/default/@jupyterlab/mainmenu/@jupyterlab/mainmenu");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_running__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/running */ "webpack/sharing/consume/default/@jupyterlab/running/@jupyterlab/running");
/* harmony import */ var _jupyterlab_running__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_running__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_terminal__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/terminal */ "webpack/sharing/consume/default/@jupyterlab/terminal/@jupyterlab/terminal");
/* harmony import */ var _jupyterlab_terminal__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_terminal__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_11__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module terminal-extension
 */












/**
 * The command IDs used by the terminal plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.createNew = 'terminal:create-new';
    CommandIDs.open = 'terminal:open';
    CommandIDs.refresh = 'terminal:refresh';
    CommandIDs.increaseFont = 'terminal:increase-font';
    CommandIDs.decreaseFont = 'terminal:decrease-font';
    CommandIDs.setTheme = 'terminal:set-theme';
    CommandIDs.shutdown = 'terminal:shut-down';
})(CommandIDs || (CommandIDs = {}));
/**
 * The default terminal extension.
 */
const plugin = {
    activate,
    id: '@jupyterlab/terminal-extension:plugin',
    provides: _jupyterlab_terminal__WEBPACK_IMPORTED_MODULE_7__.ITerminalTracker,
    requires: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_6__.ISettingRegistry, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__.ITranslator],
    optional: [
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette,
        _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_2__.ILauncher,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer,
        _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__.IMainMenu,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IThemeManager,
        _jupyterlab_running__WEBPACK_IMPORTED_MODULE_4__.IRunningSessionManagers
    ],
    autoStart: true
};
/**
 * Export the plugin as default.
 */
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);
/**
 * Activate the terminal plugin.
 */
function activate(app, settingRegistry, translator, palette, launcher, restorer, mainMenu, themeManager, runningSessionManagers) {
    const trans = translator.load('jupyterlab');
    const { serviceManager, commands } = app;
    const category = trans.__('Terminal');
    const namespace = 'terminal';
    const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
        namespace
    });
    // Bail if there are no terminals available.
    if (!serviceManager.terminals.isAvailable()) {
        console.warn('Disabling terminals plugin because they are not available on the server');
        return tracker;
    }
    // Handle state restoration.
    if (restorer) {
        void restorer.restore(tracker, {
            command: CommandIDs.createNew,
            args: widget => ({ name: widget.content.session.name }),
            name: widget => widget.content.session.name
        });
    }
    // The cached terminal options from the setting editor.
    const options = {};
    /**
     * Update the cached option values.
     */
    function updateOptions(settings) {
        // Update the cached options by doing a shallow copy of key/values.
        // This is needed because options is passed and used in addcommand-palette and needs
        // to reflect the current cached values.
        Object.keys(settings.composite).forEach((key) => {
            options[key] = settings.composite[key];
        });
    }
    /**
     * Update terminal
     */
    function updateTerminal(widget) {
        const terminal = widget.content;
        if (!terminal) {
            return;
        }
        Object.keys(options).forEach((key) => {
            terminal.setOption(key, options[key]);
        });
    }
    /**
     * Update the settings of the current tracker instances.
     */
    function updateTracker() {
        tracker.forEach(widget => updateTerminal(widget));
    }
    // Fetch the initial state of the settings.
    settingRegistry
        .load(plugin.id)
        .then(settings => {
        updateOptions(settings);
        updateTracker();
        settings.changed.connect(() => {
            updateOptions(settings);
            updateTracker();
        });
    })
        .catch(Private.showErrorMessage);
    // Subscribe to changes in theme. This is needed as the theme
    // is computed dynamically based on the string value and DOM
    // properties.
    themeManager === null || themeManager === void 0 ? void 0 : themeManager.themeChanged.connect((sender, args) => {
        tracker.forEach(widget => {
            const terminal = widget.content;
            if (terminal.getOption('theme') === 'inherit') {
                terminal.setOption('theme', 'inherit');
            }
        });
    });
    addCommands(app, tracker, settingRegistry, translator, options);
    if (mainMenu) {
        // Add "Terminal Theme" menu below "Theme" menu.
        const themeMenu = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_11__.Menu({ commands });
        themeMenu.title.label = trans._p('menu', 'Terminal Theme');
        themeMenu.addItem({
            command: CommandIDs.setTheme,
            args: {
                theme: 'inherit',
                displayName: trans.__('Inherit'),
                isPalette: false
            }
        });
        themeMenu.addItem({
            command: CommandIDs.setTheme,
            args: {
                theme: 'light',
                displayName: trans.__('Light'),
                isPalette: false
            }
        });
        themeMenu.addItem({
            command: CommandIDs.setTheme,
            args: { theme: 'dark', displayName: trans.__('Dark'), isPalette: false }
        });
        // Add some commands to the "View" menu.
        mainMenu.settingsMenu.addGroup([
            { command: CommandIDs.increaseFont },
            { command: CommandIDs.decreaseFont },
            { type: 'submenu', submenu: themeMenu }
        ], 40);
        // Add terminal creation to the file menu.
        mainMenu.fileMenu.newMenu.addItem({
            command: CommandIDs.createNew,
            rank: 20
        });
        // Add terminal close-and-shutdown to the file menu.
        mainMenu.fileMenu.closeAndCleaners.add({
            id: CommandIDs.shutdown,
            isEnabled: (w) => tracker.currentWidget !== null && tracker.has(w)
        });
    }
    if (palette) {
        // Add command palette items.
        [
            CommandIDs.createNew,
            CommandIDs.refresh,
            CommandIDs.increaseFont,
            CommandIDs.decreaseFont
        ].forEach(command => {
            palette.addItem({ command, category, args: { isPalette: true } });
        });
        palette.addItem({
            command: CommandIDs.setTheme,
            category,
            args: {
                theme: 'inherit',
                displayName: trans.__('Inherit'),
                isPalette: true
            }
        });
        palette.addItem({
            command: CommandIDs.setTheme,
            category,
            args: { theme: 'light', displayName: trans.__('Light'), isPalette: true }
        });
        palette.addItem({
            command: CommandIDs.setTheme,
            category,
            args: { theme: 'dark', displayName: trans.__('Dark'), isPalette: true }
        });
    }
    // Add a launcher item if the launcher is available.
    if (launcher) {
        launcher.add({
            command: CommandIDs.createNew,
            category: trans.__('Other'),
            rank: 0
        });
    }
    // Add a sessions manager if the running extension is available
    if (runningSessionManagers) {
        addRunningSessionManager(runningSessionManagers, app, translator);
    }
    return tracker;
}
/**
 * Add the running terminal manager to the running panel.
 */
function addRunningSessionManager(managers, app, translator) {
    const trans = translator.load('jupyterlab');
    const manager = app.serviceManager.terminals;
    managers.add({
        name: trans.__('Terminals'),
        running: () => (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__.toArray)(manager.running()).map(model => new RunningTerminal(model)),
        shutdownAll: () => manager.shutdownAll(),
        refreshRunning: () => manager.refreshRunning(),
        runningChanged: manager.runningChanged,
        shutdownLabel: trans.__('Shut Down'),
        shutdownAllLabel: trans.__('Shut Down All'),
        shutdownAllConfirmationText: trans.__('Are you sure you want to permanently shut down all running terminals?')
    });
    class RunningTerminal {
        constructor(model) {
            this._model = model;
        }
        open() {
            void app.commands.execute('terminal:open', { name: this._model.name });
        }
        icon() {
            return _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.terminalIcon;
        }
        label() {
            return `terminals/${this._model.name}`;
        }
        shutdown() {
            return manager.shutdown(this._model.name);
        }
    }
}
/**
 * Add the commands for the terminal.
 */
function addCommands(app, tracker, settingRegistry, translator, options) {
    const trans = translator.load('jupyterlab');
    const { commands, serviceManager } = app;
    // Add terminal commands.
    commands.addCommand(CommandIDs.createNew, {
        label: args => args['isPalette'] ? trans.__('New Terminal') : trans.__('Terminal'),
        caption: trans.__('Start a new terminal session'),
        icon: args => (args['isPalette'] ? undefined : _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.terminalIcon),
        execute: async (args) => {
            // wait for the widget to lazy load
            let Terminal;
            try {
                Terminal = (await Private.ensureWidget()).Terminal;
            }
            catch (err) {
                Private.showErrorMessage(err);
                return;
            }
            const name = args['name'];
            const cwd = args['cwd'];
            let session;
            if (name) {
                const models = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_5__.TerminalAPI.listRunning();
                if (models.map(d => d.name).includes(name)) {
                    // we are restoring a terminal widget and the corresponding terminal exists
                    // let's connect to it
                    session = serviceManager.terminals.connectTo({ model: { name } });
                }
                else {
                    // we are restoring a terminal widget but the corresponding terminal was closed
                    // let's start a new terminal with the original name
                    session = await serviceManager.terminals.startNew({ name, cwd });
                }
            }
            else {
                // we are creating a new terminal widget with a new terminal
                // let the server choose the terminal name
                session = await serviceManager.terminals.startNew({ cwd });
            }
            const term = new Terminal(session, options, translator);
            term.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.terminalIcon;
            term.title.label = '...';
            const main = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget({ content: term });
            app.shell.add(main, 'main', { type: 'Terminal' });
            void tracker.add(main);
            app.shell.activateById(main.id);
            return main;
        }
    });
    commands.addCommand(CommandIDs.open, {
        label: trans.__('Open a terminal by its `name`.'),
        execute: args => {
            const name = args['name'];
            // Check for a running terminal with the given name.
            const widget = tracker.find(value => {
                const content = value.content;
                return content.session.name === name || false;
            });
            if (widget) {
                app.shell.activateById(widget.id);
            }
            else {
                // Otherwise, create a new terminal with a given name.
                return commands.execute(CommandIDs.createNew, { name });
            }
        }
    });
    commands.addCommand(CommandIDs.refresh, {
        label: trans.__('Refresh Terminal'),
        caption: trans.__('Refresh the current terminal session'),
        execute: async () => {
            const current = tracker.currentWidget;
            if (!current) {
                return;
            }
            app.shell.activateById(current.id);
            try {
                await current.content.refresh();
                if (current) {
                    current.content.activate();
                }
            }
            catch (err) {
                Private.showErrorMessage(err);
            }
        },
        isEnabled: () => tracker.currentWidget !== null
    });
    commands.addCommand(CommandIDs.shutdown, {
        label: trans.__('Shutdown Terminal'),
        execute: () => {
            const current = tracker.currentWidget;
            if (!current) {
                return;
            }
            // The widget is automatically disposed upon session shutdown.
            return current.content.session.shutdown();
        },
        isEnabled: () => tracker.currentWidget !== null
    });
    commands.addCommand(CommandIDs.increaseFont, {
        label: trans.__('Increase Terminal Font Size'),
        execute: async () => {
            const { fontSize } = options;
            if (fontSize && fontSize < 72) {
                try {
                    await settingRegistry.set(plugin.id, 'fontSize', fontSize + 1);
                }
                catch (err) {
                    Private.showErrorMessage(err);
                }
            }
        }
    });
    commands.addCommand(CommandIDs.decreaseFont, {
        label: trans.__('Decrease Terminal Font Size'),
        execute: async () => {
            const { fontSize } = options;
            if (fontSize && fontSize > 9) {
                try {
                    await settingRegistry.set(plugin.id, 'fontSize', fontSize - 1);
                }
                catch (err) {
                    Private.showErrorMessage(err);
                }
            }
        }
    });
    const themeDisplayedName = {
        inherit: trans.__('Inherit'),
        light: trans.__('Light'),
        dark: trans.__('Dark')
    };
    commands.addCommand(CommandIDs.setTheme, {
        label: args => {
            if (args.theme === undefined) {
                return trans.__('Set terminal theme to the provided `theme`.');
            }
            const theme = args['theme'];
            const displayName = theme in themeDisplayedName
                ? themeDisplayedName[theme]
                : trans.__(theme[0].toUpperCase() + theme.slice(1));
            return args['isPalette']
                ? trans.__('Use Terminal Theme: %1', displayName)
                : displayName;
        },
        caption: trans.__('Set the terminal theme'),
        isToggled: args => {
            const { theme } = options;
            return args['theme'] === theme;
        },
        execute: async (args) => {
            const theme = args['theme'];
            try {
                await settingRegistry.set(plugin.id, 'theme', theme);
                commands.notifyCommandChanged(CommandIDs.setTheme);
            }
            catch (err) {
                console.log(err);
                Private.showErrorMessage(err);
            }
        }
    });
}
/**
 * A namespace for private data.
 */
var Private;
(function (Private) {
    /**
     * Lazy-load the widget (and xterm library and addons)
     */
    function ensureWidget() {
        if (Private.widgetReady) {
            return Private.widgetReady;
        }
        Private.widgetReady = Promise.all(/*! import() */[__webpack_require__.e("vendors-node_modules_xterm-addon-fit_lib_xterm-addon-fit_js-node_modules_xterm_lib_xterm_js"), __webpack_require__.e("webpack_sharing_consume_default_lumino_coreutils_lumino_coreutils"), __webpack_require__.e("webpack_sharing_consume_default_lumino_messaging_lumino_messaging"), __webpack_require__.e("webpack_sharing_consume_default_lumino_domutils_lumino_domutils"), __webpack_require__.e("packages_terminal_lib_widget_js")]).then(__webpack_require__.bind(__webpack_require__, /*! @jupyterlab/terminal/lib/widget */ "../../packages/terminal/lib/widget.js"));
        return Private.widgetReady;
    }
    Private.ensureWidget = ensureWidget;
    /**
     *  Utility function for consistent error reporting
     */
    function showErrorMessage(error) {
        console.error(`Failed to configure ${plugin.id}: ${error.message}`);
    }
    Private.showErrorMessage = showErrorMessage;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdGVybWluYWwtZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy5hNTMyM2NjMmM3ZDc3NGEzYjAyMC5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBTThCO0FBTUg7QUFDbUI7QUFDQTtBQUMrQjtBQUNuQjtBQUNFO0FBQ0k7QUFHYjtBQUNHO0FBQ2I7QUFDRztBQUUvQzs7R0FFRztBQUNILElBQVUsVUFBVSxDQWNuQjtBQWRELFdBQVUsVUFBVTtJQUNMLG9CQUFTLEdBQUcscUJBQXFCLENBQUM7SUFFbEMsZUFBSSxHQUFHLGVBQWUsQ0FBQztJQUV2QixrQkFBTyxHQUFHLGtCQUFrQixDQUFDO0lBRTdCLHVCQUFZLEdBQUcsd0JBQXdCLENBQUM7SUFFeEMsdUJBQVksR0FBRyx3QkFBd0IsQ0FBQztJQUV4QyxtQkFBUSxHQUFHLG9CQUFvQixDQUFDO0lBRWhDLG1CQUFRLEdBQUcsb0JBQW9CLENBQUM7QUFDL0MsQ0FBQyxFQWRTLFVBQVUsS0FBVixVQUFVLFFBY25CO0FBRUQ7O0dBRUc7QUFDSCxNQUFNLE1BQU0sR0FBNEM7SUFDdEQsUUFBUTtJQUNSLEVBQUUsRUFBRSx1Q0FBdUM7SUFDM0MsUUFBUSxFQUFFLGtFQUFnQjtJQUMxQixRQUFRLEVBQUUsQ0FBQyx5RUFBZ0IsRUFBRSxnRUFBVyxDQUFDO0lBQ3pDLFFBQVEsRUFBRTtRQUNSLGlFQUFlO1FBQ2YsMkRBQVM7UUFDVCxvRUFBZTtRQUNmLDJEQUFTO1FBQ1QsK0RBQWE7UUFDYix3RUFBdUI7S0FDeEI7SUFDRCxTQUFTLEVBQUUsSUFBSTtDQUNoQixDQUFDO0FBRUY7O0dBRUc7QUFDSCxpRUFBZSxNQUFNLEVBQUM7QUFFdEI7O0dBRUc7QUFDSCxTQUFTLFFBQVEsQ0FDZixHQUFvQixFQUNwQixlQUFpQyxFQUNqQyxVQUF1QixFQUN2QixPQUErQixFQUMvQixRQUEwQixFQUMxQixR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QyxPQUFPLENBQUMsS0FBSyxLQUFLLENBQUM7UUFDakMsQ0FBQztRQUNELE9BQU8sRUFBRSxLQUFLLEVBQUMsSUFBSSxFQUFDLEVBQUU7WUFDcEIsTUFBTSxLQUFLLEdBQUcsSUFBSSxDQUFDLE9BQU8sQ0FBb0IsQ0FBQztZQUMvQyxJQUFJO2dCQUNGLE1BQU0sZUFBZSxDQUFDLEdBQUcsQ0FBQyxNQUFNLENBQUMsRUFBRSxFQUFFLE9BQU8sRUFBRSxLQUFLLENBQUMsQ0FBQztnQkFDckQsUUFBUSxDQUFDLG9CQUFvQixDQUFDLFVBQVUsQ0FBQyxRQUFRLENBQUMsQ0FBQzthQUNwRDtZQUFDLE9BQU8sR0FBRyxFQUFFO2dCQUNaLE9BQU8sQ0FBQyxHQUFHLENBQUMsR0FBRyxDQUFDLENBQUM7Z0JBQ2pCLE9BQU8sQ0FBQyxnQkFBZ0IsQ0FBQyxHQUFHLENBQUMsQ0FBQzthQUMvQjtRQUNILENBQUM7S0FDRixDQUFDLENBQUM7QUFDTCxDQUFDO0FBRUQ7O0dBRUc7QUFDSCxJQUFVLE9BQU8sQ0F5QmhCO0FBekJELFdBQVUsT0FBTztJQU1mOztPQUVHO0lBQ0gsU0FBZ0IsWUFBWTtRQUMxQixJQUFJLG1CQUFXLEVBQUU7WUFDZixPQUFPLG1CQUFXLENBQUM7U0FDcEI7UUFFRCxtQkFBVyxHQUFHLGttQkFBeUMsQ0FBQztRQUV4RCxPQUFPLG1CQUFXLENBQUM7SUFDckIsQ0FBQztJQVJlLG9CQUFZLGVBUTNCO0lBRUQ7O09BRUc7SUFDSCxTQUFnQixnQkFBZ0IsQ0FBQyxLQUFZO1FBQzNDLE9BQU8sQ0FBQyxLQUFLLENBQUMsdUJBQXVCLE1BQU0sQ0FBQyxFQUFFLEtBQUssS0FBSyxDQUFDLE9BQU8sRUFBRSxDQUFDLENBQUM7SUFDdEUsQ0FBQztJQUZlLHdCQUFnQixtQkFFL0I7QUFDSCxDQUFDLEVBekJTLE9BQU8sS0FBUCxPQUFPLFFBeUJoQiIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy90ZXJtaW5hbC1leHRlbnNpb24vc3JjL2luZGV4LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIHRlcm1pbmFsLWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7XG4gIElMYXlvdXRSZXN0b3JlcixcbiAgSnVweXRlckZyb250RW5kLFxuICBKdXB5dGVyRnJvbnRFbmRQbHVnaW5cbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24nO1xuaW1wb3J0IHtcbiAgSUNvbW1hbmRQYWxldHRlLFxuICBJVGhlbWVNYW5hZ2VyLFxuICBNYWluQXJlYVdpZGdldCxcbiAgV2lkZ2V0VHJhY2tlclxufSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBJTGF1bmNoZXIgfSBmcm9tICdAanVweXRlcmxhYi9sYXVuY2hlcic7XG5pbXBvcnQgeyBJTWFpbk1lbnUgfSBmcm9tICdAanVweXRlcmxhYi9tYWlubWVudSc7XG5pbXBvcnQgeyBJUnVubmluZ1Nlc3Npb25NYW5hZ2VycywgSVJ1bm5pbmdTZXNzaW9ucyB9IGZyb20gJ0BqdXB5dGVybGFiL3J1bm5pbmcnO1xuaW1wb3J0IHsgVGVybWluYWwsIFRlcm1pbmFsQVBJIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2VydmljZXMnO1xuaW1wb3J0IHsgSVNldHRpbmdSZWdpc3RyeSB9IGZyb20gJ0BqdXB5dGVybGFiL3NldHRpbmdyZWdpc3RyeSc7XG5pbXBvcnQgeyBJVGVybWluYWwsIElUZXJtaW5hbFRyYWNrZXIgfSBmcm9tICdAanVweXRlcmxhYi90ZXJtaW5hbCc7XG4vLyBOYW1lLW9ubHkgaW1wb3J0IHNvIGFzIHRvIG5vdCB0cmlnZ2VyIGluY2x1c2lvbiBpbiBtYWluIGJ1bmRsZVxuaW1wb3J0ICogYXMgV2lkZ2V0TW9kdWxlVHlwZSBmcm9tICdAanVweXRlcmxhYi90ZXJtaW5hbC9saWIvd2lkZ2V0JztcbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgdGVybWluYWxJY29uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyB0b0FycmF5IH0gZnJvbSAnQGx1bWluby9hbGdvcml0aG0nO1xuaW1wb3J0IHsgTWVudSwgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcblxuLyoqXG4gKiBUaGUgY29tbWFuZCBJRHMgdXNlZCBieSB0aGUgdGVybWluYWwgcGx1Z2luLlxuICovXG5uYW1lc3BhY2UgQ29tbWFuZElEcyB7XG4gIGV4cG9ydCBjb25zdCBjcmVhdGVOZXcgPSAndGVybWluYWw6Y3JlYXRlLW5ldyc7XG5cbiAgZXhwb3J0IGNvbnN0IG9wZW4gPSAndGVybWluYWw6b3Blbic7XG5cbiAgZXhwb3J0IGNvbnN0IHJlZnJlc2ggPSAndGVybWluYWw6cmVmcmVzaCc7XG5cbiAgZXhwb3J0IGNvbnN0IGluY3JlYXNlRm9udCA9ICd0ZXJtaW5hbDppbmNyZWFzZS1mb250JztcblxuICBleHBvcnQgY29uc3QgZGVjcmVhc2VGb250ID0gJ3Rlcm1pbmFsOmRlY3JlYXNlLWZvbnQnO1xuXG4gIGV4cG9ydCBjb25zdCBzZXRUaGVtZSA9ICd0ZXJtaW5hbDpzZXQtdGhlbWUnO1xuXG4gIGV4cG9ydCBjb25zdCBzaHV0ZG93biA9ICd0ZXJtaW5hbDpzaHV0LWRvd24nO1xufVxuXG4vKipcbiAqIFRoZSBkZWZhdWx0IHRlcm1pbmFsIGV4dGVuc2lvbi5cbiAqL1xuY29uc3QgcGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SVRlcm1pbmFsVHJhY2tlcj4gPSB7XG4gIGFjdGl2YXRlLFxuICBpZDogJ0BqdXB5dGVybGFiL3Rlcm1pbmFsLWV4dGVuc2lvbjpwbHVnaW4nLFxuICBwcm92aWRlczogSVRlcm1pbmFsVHJhY2tlcixcbiAgcmVxdWlyZXM6IFtJU2V0dGluZ1JlZ2lzdHJ5LCBJVHJhbnNsYXRvcl0sXG4gIG9wdGlvbmFsOiBbXG4gICAgSUNvbW1hbmRQYWxldHRlLFxuICAgIElMYXVuY2hlcixcbiAgICBJTGF5b3V0UmVzdG9yZXIsXG4gICAgSU1haW5NZW51LFxuICAgIElUaGVtZU1hbmFnZXIsXG4gICAgSVJ1bm5pbmdTZXNzaW9uTWFuYWdlcnNcbiAgXSxcbiAgYXV0b1N0YXJ0OiB0cnVlXG59O1xuXG4vKipcbiAqIEV4cG9ydCB0aGUgcGx1Z2luIGFzIGRlZmF1bHQuXG4gKi9cbmV4cG9ydCBkZWZhdWx0IHBsdWdpbjtcblxuLyoqXG4gKiBBY3RpdmF0ZSB0aGUgdGVybWluYWwgcGx1Z2luLlxuICovXG5mdW5jdGlvbiBhY3RpdmF0ZShcbiAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gIHNldHRpbmdSZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSxcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSB8IG51bGwsXG4gIGxhdW5jaGVyOiBJTGF1bmNoZXIgfCBudWxsLFxuICByZXN0b3JlcjogSUxheW91dFJlc3RvcmVyIHwgbnVsbCxcbiAgbWFpbk1lbnU6IElNYWluTWVudSB8IG51bGwsXG4gIHRoZW1lTWFuYWdlcjogSVRoZW1lTWFuYWdlciB8IG51bGwsXG4gIHJ1bm5pbmdTZXNzaW9uTWFuYWdlcnM6IElSdW5uaW5nU2Vzc2lvbk1hbmFnZXJzIHwgbnVsbFxuKTogSVRlcm1pbmFsVHJhY2tlciB7XG4gIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gIGNvbnN0IHsgc2VydmljZU1hbmFnZXIsIGNvbW1hbmRzIH0gPSBhcHA7XG4gIGNvbnN0IGNhdGVnb3J5ID0gdHJhbnMuX18oJ1Rlcm1pbmFsJyk7XG4gIGNvbnN0IG5hbWVzcGFjZSA9ICd0ZXJtaW5hbCc7XG4gIGNvbnN0IHRyYWNrZXIgPSBuZXcgV2lkZ2V0VHJhY2tlcjxNYWluQXJlYVdpZGdldDxJVGVybWluYWwuSVRlcm1pbmFsPj4oe1xuICAgIG5hbWVzcGFjZVxuICB9KTtcblxuICAvLyBCYWlsIGlmIHRoZXJlIGFyZSBubyB0ZXJtaW5hbHMgYXZhaWxhYmxlLlxuICBpZiAoIXNlcnZpY2VNYW5hZ2VyLnRlcm1pbmFscy5pc0F2YWlsYWJsZSgpKSB7XG4gICAgY29uc29sZS53YXJuKFxuICAgICAgJ0Rpc2FibGluZyB0ZXJtaW5hbHMgcGx1Z2luIGJlY2F1c2UgdGhleSBhcmUgbm90IGF2YWlsYWJsZSBvbiB0aGUgc2VydmVyJ1xuICAgICk7XG4gICAgcmV0dXJuIHRyYWNrZXI7XG4gIH1cblxuICAvLyBIYW5kbGUgc3RhdGUgcmVzdG9yYXRpb24uXG4gIGlmIChyZXN0b3Jlcikge1xuICAgIHZvaWQgcmVzdG9yZXIucmVzdG9yZSh0cmFja2VyLCB7XG4gICAgICBjb21tYW5kOiBDb21tYW5kSURzLmNyZWF0ZU5ldyxcbiAgICAgIGFyZ3M6IHdpZGdldCA9PiAoeyBuYW1lOiB3aWRnZXQuY29udGVudC5zZXNzaW9uLm5hbWUgfSksXG4gICAgICBuYW1lOiB3aWRnZXQgPT4gd2lkZ2V0LmNvbnRlbnQuc2Vzc2lvbi5uYW1lXG4gICAgfSk7XG4gIH1cblxuICAvLyBUaGUgY2FjaGVkIHRlcm1pbmFsIG9wdGlvbnMgZnJvbSB0aGUgc2V0dGluZyBlZGl0b3IuXG4gIGNvbnN0IG9wdGlvbnM6IFBhcnRpYWw8SVRlcm1pbmFsLklPcHRpb25zPiA9IHt9O1xuXG4gIC8qKlxuICAgKiBVcGRhdGUgdGhlIGNhY2hlZCBvcHRpb24gdmFsdWVzLlxuICAgKi9cbiAgZnVuY3Rpb24gdXBkYXRlT3B0aW9ucyhzZXR0aW5nczogSVNldHRpbmdSZWdpc3RyeS5JU2V0dGluZ3MpOiB2b2lkIHtcbiAgICAvLyBVcGRhdGUgdGhlIGNhY2hlZCBvcHRpb25zIGJ5IGRvaW5nIGEgc2hhbGxvdyBjb3B5IG9mIGtleS92YWx1ZXMuXG4gICAgLy8gVGhpcyBpcyBuZWVkZWQgYmVjYXVzZSBvcHRpb25zIGlzIHBhc3NlZCBhbmQgdXNlZCBpbiBhZGRjb21tYW5kLXBhbGV0dGUgYW5kIG5lZWRzXG4gICAgLy8gdG8gcmVmbGVjdCB0aGUgY3VycmVudCBjYWNoZWQgdmFsdWVzLlxuICAgIE9iamVjdC5rZXlzKHNldHRpbmdzLmNvbXBvc2l0ZSkuZm9yRWFjaCgoa2V5OiBrZXlvZiBJVGVybWluYWwuSU9wdGlvbnMpID0+IHtcbiAgICAgIChvcHRpb25zIGFzIGFueSlba2V5XSA9IHNldHRpbmdzLmNvbXBvc2l0ZVtrZXldO1xuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIFVwZGF0ZSB0ZXJtaW5hbFxuICAgKi9cbiAgZnVuY3Rpb24gdXBkYXRlVGVybWluYWwod2lkZ2V0OiBNYWluQXJlYVdpZGdldDxJVGVybWluYWwuSVRlcm1pbmFsPik6IHZvaWQge1xuICAgIGNvbnN0IHRlcm1pbmFsID0gd2lkZ2V0LmNvbnRlbnQ7XG4gICAgaWYgKCF0ZXJtaW5hbCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBPYmplY3Qua2V5cyhvcHRpb25zKS5mb3JFYWNoKChrZXk6IGtleW9mIElUZXJtaW5hbC5JT3B0aW9ucykgPT4ge1xuICAgICAgdGVybWluYWwuc2V0T3B0aW9uKGtleSwgb3B0aW9uc1trZXldKTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBVcGRhdGUgdGhlIHNldHRpbmdzIG9mIHRoZSBjdXJyZW50IHRyYWNrZXIgaW5zdGFuY2VzLlxuICAgKi9cbiAgZnVuY3Rpb24gdXBkYXRlVHJhY2tlcigpOiB2b2lkIHtcbiAgICB0cmFja2VyLmZvckVhY2god2lkZ2V0ID0+IHVwZGF0ZVRlcm1pbmFsKHdpZGdldCkpO1xuICB9XG5cbiAgLy8gRmV0Y2ggdGhlIGluaXRpYWwgc3RhdGUgb2YgdGhlIHNldHRpbmdzLlxuICBzZXR0aW5nUmVnaXN0cnlcbiAgICAubG9hZChwbHVnaW4uaWQpXG4gICAgLnRoZW4oc2V0dGluZ3MgPT4ge1xuICAgICAgdXBkYXRlT3B0aW9ucyhzZXR0aW5ncyk7XG4gICAgICB1cGRhdGVUcmFja2VyKCk7XG4gICAgICBzZXR0aW5ncy5jaGFuZ2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgICB1cGRhdGVPcHRpb25zKHNldHRpbmdzKTtcbiAgICAgICAgdXBkYXRlVHJhY2tlcigpO1xuICAgICAgfSk7XG4gICAgfSlcbiAgICAuY2F0Y2goUHJpdmF0ZS5zaG93RXJyb3JNZXNzYWdlKTtcblxuICAvLyBTdWJzY3JpYmUgdG8gY2hhbmdlcyBpbiB0aGVtZS4gVGhpcyBpcyBuZWVkZWQgYXMgdGhlIHRoZW1lXG4gIC8vIGlzIGNvbXB1dGVkIGR5bmFtaWNhbGx5IGJhc2VkIG9uIHRoZSBzdHJpbmcgdmFsdWUgYW5kIERPTVxuICAvLyBwcm9wZXJ0aWVzLlxuICB0aGVtZU1hbmFnZXI/LnRoZW1lQ2hhbmdlZC5jb25uZWN0KChzZW5kZXIsIGFyZ3MpID0+IHtcbiAgICB0cmFja2VyLmZvckVhY2god2lkZ2V0ID0+IHtcbiAgICAgIGNvbnN0IHRlcm1pbmFsID0gd2lkZ2V0LmNvbnRlbnQ7XG4gICAgICBpZiAodGVybWluYWwuZ2V0T3B0aW9uKCd0aGVtZScpID09PSAnaW5oZXJpdCcpIHtcbiAgICAgICAgdGVybWluYWwuc2V0T3B0aW9uKCd0aGVtZScsICdpbmhlcml0Jyk7XG4gICAgICB9XG4gICAgfSk7XG4gIH0pO1xuXG4gIGFkZENvbW1hbmRzKGFwcCwgdHJhY2tlciwgc2V0dGluZ1JlZ2lzdHJ5LCB0cmFuc2xhdG9yLCBvcHRpb25zKTtcblxuICBpZiAobWFpbk1lbnUpIHtcbiAgICAvLyBBZGQgXCJUZXJtaW5hbCBUaGVtZVwiIG1lbnUgYmVsb3cgXCJUaGVtZVwiIG1lbnUuXG4gICAgY29uc3QgdGhlbWVNZW51ID0gbmV3IE1lbnUoeyBjb21tYW5kcyB9KTtcbiAgICB0aGVtZU1lbnUudGl0bGUubGFiZWwgPSB0cmFucy5fcCgnbWVudScsICdUZXJtaW5hbCBUaGVtZScpO1xuICAgIHRoZW1lTWVudS5hZGRJdGVtKHtcbiAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMuc2V0VGhlbWUsXG4gICAgICBhcmdzOiB7XG4gICAgICAgIHRoZW1lOiAnaW5oZXJpdCcsXG4gICAgICAgIGRpc3BsYXlOYW1lOiB0cmFucy5fXygnSW5oZXJpdCcpLFxuICAgICAgICBpc1BhbGV0dGU6IGZhbHNlXG4gICAgICB9XG4gICAgfSk7XG4gICAgdGhlbWVNZW51LmFkZEl0ZW0oe1xuICAgICAgY29tbWFuZDogQ29tbWFuZElEcy5zZXRUaGVtZSxcbiAgICAgIGFyZ3M6IHtcbiAgICAgICAgdGhlbWU6ICdsaWdodCcsXG4gICAgICAgIGRpc3BsYXlOYW1lOiB0cmFucy5fXygnTGlnaHQnKSxcbiAgICAgICAgaXNQYWxldHRlOiBmYWxzZVxuICAgICAgfVxuICAgIH0pO1xuICAgIHRoZW1lTWVudS5hZGRJdGVtKHtcbiAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMuc2V0VGhlbWUsXG4gICAgICBhcmdzOiB7IHRoZW1lOiAnZGFyaycsIGRpc3BsYXlOYW1lOiB0cmFucy5fXygnRGFyaycpLCBpc1BhbGV0dGU6IGZhbHNlIH1cbiAgICB9KTtcblxuICAgIC8vIEFkZCBzb21lIGNvbW1hbmRzIHRvIHRoZSBcIlZpZXdcIiBtZW51LlxuICAgIG1haW5NZW51LnNldHRpbmdzTWVudS5hZGRHcm91cChcbiAgICAgIFtcbiAgICAgICAgeyBjb21tYW5kOiBDb21tYW5kSURzLmluY3JlYXNlRm9udCB9LFxuICAgICAgICB7IGNvbW1hbmQ6IENvbW1hbmRJRHMuZGVjcmVhc2VGb250IH0sXG4gICAgICAgIHsgdHlwZTogJ3N1Ym1lbnUnLCBzdWJtZW51OiB0aGVtZU1lbnUgfVxuICAgICAgXSxcbiAgICAgIDQwXG4gICAgKTtcblxuICAgIC8vIEFkZCB0ZXJtaW5hbCBjcmVhdGlvbiB0byB0aGUgZmlsZSBtZW51LlxuICAgIG1haW5NZW51LmZpbGVNZW51Lm5ld01lbnUuYWRkSXRlbSh7XG4gICAgICBjb21tYW5kOiBDb21tYW5kSURzLmNyZWF0ZU5ldyxcbiAgICAgIHJhbms6IDIwXG4gICAgfSk7XG5cbiAgICAvLyBBZGQgdGVybWluYWwgY2xvc2UtYW5kLXNodXRkb3duIHRvIHRoZSBmaWxlIG1lbnUuXG4gICAgbWFpbk1lbnUuZmlsZU1lbnUuY2xvc2VBbmRDbGVhbmVycy5hZGQoe1xuICAgICAgaWQ6IENvbW1hbmRJRHMuc2h1dGRvd24sXG4gICAgICBpc0VuYWJsZWQ6ICh3OiBXaWRnZXQpID0+IHRyYWNrZXIuY3VycmVudFdpZGdldCAhPT0gbnVsbCAmJiB0cmFja2VyLmhhcyh3KVxuICAgIH0pO1xuICB9XG5cbiAgaWYgKHBhbGV0dGUpIHtcbiAgICAvLyBBZGQgY29tbWFuZCBwYWxldHRlIGl0ZW1zLlxuICAgIFtcbiAgICAgIENvbW1hbmRJRHMuY3JlYXRlTmV3LFxuICAgICAgQ29tbWFuZElEcy5yZWZyZXNoLFxuICAgICAgQ29tbWFuZElEcy5pbmNyZWFzZUZvbnQsXG4gICAgICBDb21tYW5kSURzLmRlY3JlYXNlRm9udFxuICAgIF0uZm9yRWFjaChjb21tYW5kID0+IHtcbiAgICAgIHBhbGV0dGUuYWRkSXRlbSh7IGNvbW1hbmQsIGNhdGVnb3J5LCBhcmdzOiB7IGlzUGFsZXR0ZTogdHJ1ZSB9IH0pO1xuICAgIH0pO1xuICAgIHBhbGV0dGUuYWRkSXRlbSh7XG4gICAgICBjb21tYW5kOiBDb21tYW5kSURzLnNldFRoZW1lLFxuICAgICAgY2F0ZWdvcnksXG4gICAgICBhcmdzOiB7XG4gICAgICAgIHRoZW1lOiAnaW5oZXJpdCcsXG4gICAgICAgIGRpc3BsYXlOYW1lOiB0cmFucy5fXygnSW5oZXJpdCcpLFxuICAgICAgICBpc1BhbGV0dGU6IHRydWVcbiAgICAgIH1cbiAgICB9KTtcbiAgICBwYWxldHRlLmFkZEl0ZW0oe1xuICAgICAgY29tbWFuZDogQ29tbWFuZElEcy5zZXRUaGVtZSxcbiAgICAgIGNhdGVnb3J5LFxuICAgICAgYXJnczogeyB0aGVtZTogJ2xpZ2h0JywgZGlzcGxheU5hbWU6IHRyYW5zLl9fKCdMaWdodCcpLCBpc1BhbGV0dGU6IHRydWUgfVxuICAgIH0pO1xuICAgIHBhbGV0dGUuYWRkSXRlbSh7XG4gICAgICBjb21tYW5kOiBDb21tYW5kSURzLnNldFRoZW1lLFxuICAgICAgY2F0ZWdvcnksXG4gICAgICBhcmdzOiB7IHRoZW1lOiAnZGFyaycsIGRpc3BsYXlOYW1lOiB0cmFucy5fXygnRGFyaycpLCBpc1BhbGV0dGU6IHRydWUgfVxuICAgIH0pO1xuICB9XG5cbiAgLy8gQWRkIGEgbGF1bmNoZXIgaXRlbSBpZiB0aGUgbGF1bmNoZXIgaXMgYXZhaWxhYmxlLlxuICBpZiAobGF1bmNoZXIpIHtcbiAgICBsYXVuY2hlci5hZGQoe1xuICAgICAgY29tbWFuZDogQ29tbWFuZElEcy5jcmVhdGVOZXcsXG4gICAgICBjYXRlZ29yeTogdHJhbnMuX18oJ090aGVyJyksXG4gICAgICByYW5rOiAwXG4gICAgfSk7XG4gIH1cblxuICAvLyBBZGQgYSBzZXNzaW9ucyBtYW5hZ2VyIGlmIHRoZSBydW5uaW5nIGV4dGVuc2lvbiBpcyBhdmFpbGFibGVcbiAgaWYgKHJ1bm5pbmdTZXNzaW9uTWFuYWdlcnMpIHtcbiAgICBhZGRSdW5uaW5nU2Vzc2lvbk1hbmFnZXIocnVubmluZ1Nlc3Npb25NYW5hZ2VycywgYXBwLCB0cmFuc2xhdG9yKTtcbiAgfVxuXG4gIHJldHVybiB0cmFja2VyO1xufVxuXG4vKipcbiAqIEFkZCB0aGUgcnVubmluZyB0ZXJtaW5hbCBtYW5hZ2VyIHRvIHRoZSBydW5uaW5nIHBhbmVsLlxuICovXG5mdW5jdGlvbiBhZGRSdW5uaW5nU2Vzc2lvbk1hbmFnZXIoXG4gIG1hbmFnZXJzOiBJUnVubmluZ1Nlc3Npb25NYW5hZ2VycyxcbiAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yXG4pIHtcbiAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgY29uc3QgbWFuYWdlciA9IGFwcC5zZXJ2aWNlTWFuYWdlci50ZXJtaW5hbHM7XG5cbiAgbWFuYWdlcnMuYWRkKHtcbiAgICBuYW1lOiB0cmFucy5fXygnVGVybWluYWxzJyksXG4gICAgcnVubmluZzogKCkgPT5cbiAgICAgIHRvQXJyYXkobWFuYWdlci5ydW5uaW5nKCkpLm1hcChtb2RlbCA9PiBuZXcgUnVubmluZ1Rlcm1pbmFsKG1vZGVsKSksXG4gICAgc2h1dGRvd25BbGw6ICgpID0+IG1hbmFnZXIuc2h1dGRvd25BbGwoKSxcbiAgICByZWZyZXNoUnVubmluZzogKCkgPT4gbWFuYWdlci5yZWZyZXNoUnVubmluZygpLFxuICAgIHJ1bm5pbmdDaGFuZ2VkOiBtYW5hZ2VyLnJ1bm5pbmdDaGFuZ2VkLFxuICAgIHNodXRkb3duTGFiZWw6IHRyYW5zLl9fKCdTaHV0IERvd24nKSxcbiAgICBzaHV0ZG93bkFsbExhYmVsOiB0cmFucy5fXygnU2h1dCBEb3duIEFsbCcpLFxuICAgIHNodXRkb3duQWxsQ29uZmlybWF0aW9uVGV4dDogdHJhbnMuX18oXG4gICAgICAnQXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHBlcm1hbmVudGx5IHNodXQgZG93biBhbGwgcnVubmluZyB0ZXJtaW5hbHM/J1xuICAgIClcbiAgfSk7XG5cbiAgY2xhc3MgUnVubmluZ1Rlcm1pbmFsIGltcGxlbWVudHMgSVJ1bm5pbmdTZXNzaW9ucy5JUnVubmluZ0l0ZW0ge1xuICAgIGNvbnN0cnVjdG9yKG1vZGVsOiBUZXJtaW5hbC5JTW9kZWwpIHtcbiAgICAgIHRoaXMuX21vZGVsID0gbW9kZWw7XG4gICAgfVxuICAgIG9wZW4oKSB7XG4gICAgICB2b2lkIGFwcC5jb21tYW5kcy5leGVjdXRlKCd0ZXJtaW5hbDpvcGVuJywgeyBuYW1lOiB0aGlzLl9tb2RlbC5uYW1lIH0pO1xuICAgIH1cbiAgICBpY29uKCkge1xuICAgICAgcmV0dXJuIHRlcm1pbmFsSWNvbjtcbiAgICB9XG4gICAgbGFiZWwoKSB7XG4gICAgICByZXR1cm4gYHRlcm1pbmFscy8ke3RoaXMuX21vZGVsLm5hbWV9YDtcbiAgICB9XG4gICAgc2h1dGRvd24oKSB7XG4gICAgICByZXR1cm4gbWFuYWdlci5zaHV0ZG93bih0aGlzLl9tb2RlbC5uYW1lKTtcbiAgICB9XG5cbiAgICBwcml2YXRlIF9tb2RlbDogVGVybWluYWwuSU1vZGVsO1xuICB9XG59XG5cbi8qKlxuICogQWRkIHRoZSBjb21tYW5kcyBmb3IgdGhlIHRlcm1pbmFsLlxuICovXG5leHBvcnQgZnVuY3Rpb24gYWRkQ29tbWFuZHMoXG4gIGFwcDogSnVweXRlckZyb250RW5kLFxuICB0cmFja2VyOiBXaWRnZXRUcmFja2VyPE1haW5BcmVhV2lkZ2V0PElUZXJtaW5hbC5JVGVybWluYWw+PixcbiAgc2V0dGluZ1JlZ2lzdHJ5OiBJU2V0dGluZ1JlZ2lzdHJ5LFxuICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcixcbiAgb3B0aW9uczogUGFydGlhbDxJVGVybWluYWwuSU9wdGlvbnM+XG4pOiB2b2lkIHtcbiAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgY29uc3QgeyBjb21tYW5kcywgc2VydmljZU1hbmFnZXIgfSA9IGFwcDtcblxuICAvLyBBZGQgdGVybWluYWwgY29tbWFuZHMuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5jcmVhdGVOZXcsIHtcbiAgICBsYWJlbDogYXJncyA9PlxuICAgICAgYXJnc1snaXNQYWxldHRlJ10gPyB0cmFucy5fXygnTmV3IFRlcm1pbmFsJykgOiB0cmFucy5fXygnVGVybWluYWwnKSxcbiAgICBjYXB0aW9uOiB0cmFucy5fXygnU3RhcnQgYSBuZXcgdGVybWluYWwgc2Vzc2lvbicpLFxuICAgIGljb246IGFyZ3MgPT4gKGFyZ3NbJ2lzUGFsZXR0ZSddID8gdW5kZWZpbmVkIDogdGVybWluYWxJY29uKSxcbiAgICBleGVjdXRlOiBhc3luYyBhcmdzID0+IHtcbiAgICAgIC8vIHdhaXQgZm9yIHRoZSB3aWRnZXQgdG8gbGF6eSBsb2FkXG4gICAgICBsZXQgVGVybWluYWw6IHR5cGVvZiBXaWRnZXRNb2R1bGVUeXBlLlRlcm1pbmFsO1xuICAgICAgdHJ5IHtcbiAgICAgICAgVGVybWluYWwgPSAoYXdhaXQgUHJpdmF0ZS5lbnN1cmVXaWRnZXQoKSkuVGVybWluYWw7XG4gICAgICB9IGNhdGNoIChlcnIpIHtcbiAgICAgICAgUHJpdmF0ZS5zaG93RXJyb3JNZXNzYWdlKGVycik7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cblxuICAgICAgY29uc3QgbmFtZSA9IGFyZ3NbJ25hbWUnXSBhcyBzdHJpbmc7XG4gICAgICBjb25zdCBjd2QgPSBhcmdzWydjd2QnXSBhcyBzdHJpbmc7XG5cbiAgICAgIGxldCBzZXNzaW9uO1xuICAgICAgaWYgKG5hbWUpIHtcbiAgICAgICAgY29uc3QgbW9kZWxzID0gYXdhaXQgVGVybWluYWxBUEkubGlzdFJ1bm5pbmcoKTtcbiAgICAgICAgaWYgKG1vZGVscy5tYXAoZCA9PiBkLm5hbWUpLmluY2x1ZGVzKG5hbWUpKSB7XG4gICAgICAgICAgLy8gd2UgYXJlIHJlc3RvcmluZyBhIHRlcm1pbmFsIHdpZGdldCBhbmQgdGhlIGNvcnJlc3BvbmRpbmcgdGVybWluYWwgZXhpc3RzXG4gICAgICAgICAgLy8gbGV0J3MgY29ubmVjdCB0byBpdFxuICAgICAgICAgIHNlc3Npb24gPSBzZXJ2aWNlTWFuYWdlci50ZXJtaW5hbHMuY29ubmVjdFRvKHsgbW9kZWw6IHsgbmFtZSB9IH0pO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIC8vIHdlIGFyZSByZXN0b3JpbmcgYSB0ZXJtaW5hbCB3aWRnZXQgYnV0IHRoZSBjb3JyZXNwb25kaW5nIHRlcm1pbmFsIHdhcyBjbG9zZWRcbiAgICAgICAgICAvLyBsZXQncyBzdGFydCBhIG5ldyB0ZXJtaW5hbCB3aXRoIHRoZSBvcmlnaW5hbCBuYW1lXG4gICAgICAgICAgc2Vzc2lvbiA9IGF3YWl0IHNlcnZpY2VNYW5hZ2VyLnRlcm1pbmFscy5zdGFydE5ldyh7IG5hbWUsIGN3ZCB9KTtcbiAgICAgICAgfVxuICAgICAgfSBlbHNlIHtcbiAgICAgICAgLy8gd2UgYXJlIGNyZWF0aW5nIGEgbmV3IHRlcm1pbmFsIHdpZGdldCB3aXRoIGEgbmV3IHRlcm1pbmFsXG4gICAgICAgIC8vIGxldCB0aGUgc2VydmVyIGNob29zZSB0aGUgdGVybWluYWwgbmFtZVxuICAgICAgICBzZXNzaW9uID0gYXdhaXQgc2VydmljZU1hbmFnZXIudGVybWluYWxzLnN0YXJ0TmV3KHsgY3dkIH0pO1xuICAgICAgfVxuXG4gICAgICBjb25zdCB0ZXJtID0gbmV3IFRlcm1pbmFsKHNlc3Npb24sIG9wdGlvbnMsIHRyYW5zbGF0b3IpO1xuXG4gICAgICB0ZXJtLnRpdGxlLmljb24gPSB0ZXJtaW5hbEljb247XG4gICAgICB0ZXJtLnRpdGxlLmxhYmVsID0gJy4uLic7XG5cbiAgICAgIGNvbnN0IG1haW4gPSBuZXcgTWFpbkFyZWFXaWRnZXQoeyBjb250ZW50OiB0ZXJtIH0pO1xuICAgICAgYXBwLnNoZWxsLmFkZChtYWluLCAnbWFpbicsIHsgdHlwZTogJ1Rlcm1pbmFsJyB9KTtcbiAgICAgIHZvaWQgdHJhY2tlci5hZGQobWFpbik7XG4gICAgICBhcHAuc2hlbGwuYWN0aXZhdGVCeUlkKG1haW4uaWQpO1xuICAgICAgcmV0dXJuIG1haW47XG4gICAgfVxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMub3Blbiwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnT3BlbiBhIHRlcm1pbmFsIGJ5IGl0cyBgbmFtZWAuJyksXG4gICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICBjb25zdCBuYW1lID0gYXJnc1snbmFtZSddIGFzIHN0cmluZztcbiAgICAgIC8vIENoZWNrIGZvciBhIHJ1bm5pbmcgdGVybWluYWwgd2l0aCB0aGUgZ2l2ZW4gbmFtZS5cbiAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuZmluZCh2YWx1ZSA9PiB7XG4gICAgICAgIGNvbnN0IGNvbnRlbnQgPSB2YWx1ZS5jb250ZW50O1xuICAgICAgICByZXR1cm4gY29udGVudC5zZXNzaW9uLm5hbWUgPT09IG5hbWUgfHwgZmFsc2U7XG4gICAgICB9KTtcbiAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgYXBwLnNoZWxsLmFjdGl2YXRlQnlJZCh3aWRnZXQuaWQpO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgLy8gT3RoZXJ3aXNlLCBjcmVhdGUgYSBuZXcgdGVybWluYWwgd2l0aCBhIGdpdmVuIG5hbWUuXG4gICAgICAgIHJldHVybiBjb21tYW5kcy5leGVjdXRlKENvbW1hbmRJRHMuY3JlYXRlTmV3LCB7IG5hbWUgfSk7XG4gICAgICB9XG4gICAgfVxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMucmVmcmVzaCwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnUmVmcmVzaCBUZXJtaW5hbCcpLFxuICAgIGNhcHRpb246IHRyYW5zLl9fKCdSZWZyZXNoIHRoZSBjdXJyZW50IHRlcm1pbmFsIHNlc3Npb24nKSxcbiAgICBleGVjdXRlOiBhc3luYyAoKSA9PiB7XG4gICAgICBjb25zdCBjdXJyZW50ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuICAgICAgaWYgKCFjdXJyZW50KSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGFwcC5zaGVsbC5hY3RpdmF0ZUJ5SWQoY3VycmVudC5pZCk7XG4gICAgICB0cnkge1xuICAgICAgICBhd2FpdCBjdXJyZW50LmNvbnRlbnQucmVmcmVzaCgpO1xuICAgICAgICBpZiAoY3VycmVudCkge1xuICAgICAgICAgIGN1cnJlbnQuY29udGVudC5hY3RpdmF0ZSgpO1xuICAgICAgICB9XG4gICAgICB9IGNhdGNoIChlcnIpIHtcbiAgICAgICAgUHJpdmF0ZS5zaG93RXJyb3JNZXNzYWdlKGVycik7XG4gICAgICB9XG4gICAgfSxcbiAgICBpc0VuYWJsZWQ6ICgpID0+IHRyYWNrZXIuY3VycmVudFdpZGdldCAhPT0gbnVsbFxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuc2h1dGRvd24sIHtcbiAgICBsYWJlbDogdHJhbnMuX18oJ1NodXRkb3duIFRlcm1pbmFsJyksXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgY29uc3QgY3VycmVudCA9IHRyYWNrZXIuY3VycmVudFdpZGdldDtcbiAgICAgIGlmICghY3VycmVudCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG5cbiAgICAgIC8vIFRoZSB3aWRnZXQgaXMgYXV0b21hdGljYWxseSBkaXNwb3NlZCB1cG9uIHNlc3Npb24gc2h1dGRvd24uXG4gICAgICByZXR1cm4gY3VycmVudC5jb250ZW50LnNlc3Npb24uc2h1dGRvd24oKTtcbiAgICB9LFxuICAgIGlzRW5hYmxlZDogKCkgPT4gdHJhY2tlci5jdXJyZW50V2lkZ2V0ICE9PSBudWxsXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5pbmNyZWFzZUZvbnQsIHtcbiAgICBsYWJlbDogdHJhbnMuX18oJ0luY3JlYXNlIFRlcm1pbmFsIEZvbnQgU2l6ZScpLFxuICAgIGV4ZWN1dGU6IGFzeW5jICgpID0+IHtcbiAgICAgIGNvbnN0IHsgZm9udFNpemUgfSA9IG9wdGlvbnM7XG4gICAgICBpZiAoZm9udFNpemUgJiYgZm9udFNpemUgPCA3Mikge1xuICAgICAgICB0cnkge1xuICAgICAgICAgIGF3YWl0IHNldHRpbmdSZWdpc3RyeS5zZXQocGx1Z2luLmlkLCAnZm9udFNpemUnLCBmb250U2l6ZSArIDEpO1xuICAgICAgICB9IGNhdGNoIChlcnIpIHtcbiAgICAgICAgICBQcml2YXRlLnNob3dFcnJvck1lc3NhZ2UoZXJyKTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH1cbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmRlY3JlYXNlRm9udCwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnRGVjcmVhc2UgVGVybWluYWwgRm9udCBTaXplJyksXG4gICAgZXhlY3V0ZTogYXN5bmMgKCkgPT4ge1xuICAgICAgY29uc3QgeyBmb250U2l6ZSB9ID0gb3B0aW9ucztcbiAgICAgIGlmIChmb250U2l6ZSAmJiBmb250U2l6ZSA+IDkpIHtcbiAgICAgICAgdHJ5IHtcbiAgICAgICAgICBhd2FpdCBzZXR0aW5nUmVnaXN0cnkuc2V0KHBsdWdpbi5pZCwgJ2ZvbnRTaXplJywgZm9udFNpemUgLSAxKTtcbiAgICAgICAgfSBjYXRjaCAoZXJyKSB7XG4gICAgICAgICAgUHJpdmF0ZS5zaG93RXJyb3JNZXNzYWdlKGVycik7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9XG4gIH0pO1xuXG4gIGNvbnN0IHRoZW1lRGlzcGxheWVkTmFtZSA9IHtcbiAgICBpbmhlcml0OiB0cmFucy5fXygnSW5oZXJpdCcpLFxuICAgIGxpZ2h0OiB0cmFucy5fXygnTGlnaHQnKSxcbiAgICBkYXJrOiB0cmFucy5fXygnRGFyaycpXG4gIH07XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnNldFRoZW1lLCB7XG4gICAgbGFiZWw6IGFyZ3MgPT4ge1xuICAgICAgaWYgKGFyZ3MudGhlbWUgPT09IHVuZGVmaW5lZCkge1xuICAgICAgICByZXR1cm4gdHJhbnMuX18oJ1NldCB0ZXJtaW5hbCB0aGVtZSB0byB0aGUgcHJvdmlkZWQgYHRoZW1lYC4nKTtcbiAgICAgIH1cbiAgICAgIGNvbnN0IHRoZW1lID0gYXJnc1sndGhlbWUnXSBhcyBzdHJpbmc7XG4gICAgICBjb25zdCBkaXNwbGF5TmFtZSA9XG4gICAgICAgIHRoZW1lIGluIHRoZW1lRGlzcGxheWVkTmFtZVxuICAgICAgICAgID8gdGhlbWVEaXNwbGF5ZWROYW1lW3RoZW1lIGFzIGtleW9mIHR5cGVvZiB0aGVtZURpc3BsYXllZE5hbWVdXG4gICAgICAgICAgOiB0cmFucy5fXyh0aGVtZVswXS50b1VwcGVyQ2FzZSgpICsgdGhlbWUuc2xpY2UoMSkpO1xuICAgICAgcmV0dXJuIGFyZ3NbJ2lzUGFsZXR0ZSddXG4gICAgICAgID8gdHJhbnMuX18oJ1VzZSBUZXJtaW5hbCBUaGVtZTogJTEnLCBkaXNwbGF5TmFtZSlcbiAgICAgICAgOiBkaXNwbGF5TmFtZTtcbiAgICB9LFxuICAgIGNhcHRpb246IHRyYW5zLl9fKCdTZXQgdGhlIHRlcm1pbmFsIHRoZW1lJyksXG4gICAgaXNUb2dnbGVkOiBhcmdzID0+IHtcbiAgICAgIGNvbnN0IHsgdGhlbWUgfSA9IG9wdGlvbnM7XG4gICAgICByZXR1cm4gYXJnc1sndGhlbWUnXSA9PT0gdGhlbWU7XG4gICAgfSxcbiAgICBleGVjdXRlOiBhc3luYyBhcmdzID0+IHtcbiAgICAgIGNvbnN0IHRoZW1lID0gYXJnc1sndGhlbWUnXSBhcyBJVGVybWluYWwuVGhlbWU7XG4gICAgICB0cnkge1xuICAgICAgICBhd2FpdCBzZXR0aW5nUmVnaXN0cnkuc2V0KHBsdWdpbi5pZCwgJ3RoZW1lJywgdGhlbWUpO1xuICAgICAgICBjb21tYW5kcy5ub3RpZnlDb21tYW5kQ2hhbmdlZChDb21tYW5kSURzLnNldFRoZW1lKTtcbiAgICAgIH0gY2F0Y2ggKGVycikge1xuICAgICAgICBjb25zb2xlLmxvZyhlcnIpO1xuICAgICAgICBQcml2YXRlLnNob3dFcnJvck1lc3NhZ2UoZXJyKTtcbiAgICAgIH1cbiAgICB9XG4gIH0pO1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBwcml2YXRlIGRhdGEuXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgLyoqXG4gICAqIEEgUHJvbWlzZSBmb3IgdGhlIGluaXRpYWwgbG9hZCBvZiB0aGUgdGVybWluYWwgd2lkZ2V0LlxuICAgKi9cbiAgZXhwb3J0IGxldCB3aWRnZXRSZWFkeTogUHJvbWlzZTx0eXBlb2YgV2lkZ2V0TW9kdWxlVHlwZT47XG5cbiAgLyoqXG4gICAqIExhenktbG9hZCB0aGUgd2lkZ2V0IChhbmQgeHRlcm0gbGlicmFyeSBhbmQgYWRkb25zKVxuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIGVuc3VyZVdpZGdldCgpOiBQcm9taXNlPHR5cGVvZiBXaWRnZXRNb2R1bGVUeXBlPiB7XG4gICAgaWYgKHdpZGdldFJlYWR5KSB7XG4gICAgICByZXR1cm4gd2lkZ2V0UmVhZHk7XG4gICAgfVxuXG4gICAgd2lkZ2V0UmVhZHkgPSBpbXBvcnQoJ0BqdXB5dGVybGFiL3Rlcm1pbmFsL2xpYi93aWRnZXQnKTtcblxuICAgIHJldHVybiB3aWRnZXRSZWFkeTtcbiAgfVxuXG4gIC8qKlxuICAgKiAgVXRpbGl0eSBmdW5jdGlvbiBmb3IgY29uc2lzdGVudCBlcnJvciByZXBvcnRpbmdcbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBzaG93RXJyb3JNZXNzYWdlKGVycm9yOiBFcnJvcik6IHZvaWQge1xuICAgIGNvbnNvbGUuZXJyb3IoYEZhaWxlZCB0byBjb25maWd1cmUgJHtwbHVnaW4uaWR9OiAke2Vycm9yLm1lc3NhZ2V9YCk7XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==