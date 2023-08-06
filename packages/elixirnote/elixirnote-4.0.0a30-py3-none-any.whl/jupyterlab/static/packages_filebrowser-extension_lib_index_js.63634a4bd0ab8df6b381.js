"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_filebrowser-extension_lib_index_js"],{

/***/ "../../packages/filebrowser-extension/lib/index.js":
/*!*********************************************************!*\
  !*** ../../packages/filebrowser-extension/lib/index.js ***!
  \*********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__),
/* harmony export */   "fileUploadStatus": () => (/* binding */ fileUploadStatus)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/docmanager */ "webpack/sharing/consume/default/@jupyterlab/docmanager/@jupyterlab/docmanager");
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/statedb */ "webpack/sharing/consume/default/@jupyterlab/statedb/@jupyterlab/statedb");
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _lumino_commands__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @lumino/commands */ "webpack/sharing/consume/default/@lumino/commands/@lumino/commands");
/* harmony import */ var _lumino_commands__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(_lumino_commands__WEBPACK_IMPORTED_MODULE_11__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module filebrowser-extension
 */












const FILE_BROWSER_FACTORY = 'FileBrowser';
const FILE_BROWSER_PLUGIN_ID = '@jupyterlab/filebrowser-extension:browser';
/**
 * The command IDs used by the file browser plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.copy = 'filebrowser:copy';
    CommandIDs.copyDownloadLink = 'filebrowser:copy-download-link';
    CommandIDs.cut = 'filebrowser:cut';
    CommandIDs.del = 'filebrowser:delete';
    CommandIDs.download = 'filebrowser:download';
    CommandIDs.duplicate = 'filebrowser:duplicate';
    // For main browser only.
    CommandIDs.hideBrowser = 'filebrowser:hide-main';
    CommandIDs.goToPath = 'filebrowser:go-to-path';
    CommandIDs.goUp = 'filebrowser:go-up';
    CommandIDs.openPath = 'filebrowser:open-path';
    CommandIDs.openUrl = 'filebrowser:open-url';
    CommandIDs.open = 'filebrowser:open';
    CommandIDs.openBrowserTab = 'filebrowser:open-browser-tab';
    CommandIDs.paste = 'filebrowser:paste';
    CommandIDs.createNewDirectory = 'filebrowser:create-new-directory';
    CommandIDs.createNewFile = 'filebrowser:create-new-file';
    CommandIDs.createNewMarkdownFile = 'filebrowser:create-new-markdown-file';
    CommandIDs.refresh = 'filebrowser:refresh';
    CommandIDs.rename = 'filebrowser:rename';
    // For main browser only.
    CommandIDs.copyShareableLink = 'filebrowser:share-main';
    // For main browser only.
    CommandIDs.copyPath = 'filebrowser:copy-path';
    CommandIDs.showBrowser = 'filebrowser:activate';
    CommandIDs.shutdown = 'filebrowser:shutdown';
    // For main browser only.
    CommandIDs.toggleBrowser = 'filebrowser:toggle-main';
    CommandIDs.toggleNavigateToCurrentDirectory = 'filebrowser:toggle-navigate-to-current-directory';
    CommandIDs.toggleLastModified = 'filebrowser:toggle-last-modified';
    CommandIDs.search = 'filebrowser:search';
    CommandIDs.toggleHiddenFiles = 'filebrowser:toggle-hidden-files';
    CommandIDs.toggleFileCheckboxes = 'filebrowser:toggle-file-checkboxes';
})(CommandIDs || (CommandIDs = {}));
/**
 * The file browser namespace token.
 */
const namespace = 'filebrowser';
/**
 * The default file browser extension.
 */
const browser = {
    id: FILE_BROWSER_PLUGIN_ID,
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.IFileBrowserFactory, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__.ITranslator],
    optional: [
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer,
        _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.ISettingRegistry,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ITreePathUpdater,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette
    ],
    provides: _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.IFileBrowserCommands,
    autoStart: true,
    activate: async (app, factory, translator, restorer, settingRegistry, treePathUpdater, commandPalette) => {
        const trans = translator.load('jupyterlab');
        const browser = factory.defaultBrowser;
        // Let the application restorer track the primary file browser (that is
        // automatically created) for restoration of application state (e.g. setting
        // the file browser as the current side bar widget).
        //
        // All other file browsers created by using the factory function are
        // responsible for their own restoration behavior, if any.
        if (restorer) {
            restorer.add(browser, namespace);
        }
        // Navigate to preferred-dir trait if found
        const preferredPath = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getOption('preferredPath');
        if (preferredPath) {
            await browser.model.cd(preferredPath);
        }
        addCommands(app, factory, translator, settingRegistry, commandPalette);
        // Show the current file browser shortcut in its title.
        const updateBrowserTitle = () => {
            const binding = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__.find)(app.commands.keyBindings, b => b.command === CommandIDs.toggleBrowser);
            if (binding) {
                const ks = _lumino_commands__WEBPACK_IMPORTED_MODULE_11__.CommandRegistry.formatKeystroke(binding.keys.join(' '));
                browser.title.caption = trans.__('File Browser (%1)', ks);
            }
            else {
                browser.title.caption = trans.__('File Browser');
            }
        };
        updateBrowserTitle();
        app.commands.keyBindingChanged.connect(() => {
            updateBrowserTitle();
        });
        return void Promise.all([app.restored, browser.model.restored]).then(() => {
            if (treePathUpdater) {
                browser.model.pathChanged.connect((sender, args) => {
                    treePathUpdater(args.newValue);
                });
            }
            if (settingRegistry) {
                void settingRegistry.load(FILE_BROWSER_PLUGIN_ID).then(settings => {
                    /**
                     * File browser configuration.
                     */
                    const fileBrowserConfig = {
                        navigateToCurrentDirectory: false,
                        showLastModifiedColumn: true,
                        useFuzzyFilter: true,
                        showHiddenFiles: false,
                        showFileCheckboxes: false
                    };
                    const fileBrowserModelConfig = {
                        filterDirectories: true
                    };
                    function onSettingsChanged(settings) {
                        let key;
                        for (key in fileBrowserConfig) {
                            const value = settings.get(key).composite;
                            fileBrowserConfig[key] = value;
                            browser[key] = value;
                        }
                        const value = settings.get('filterDirectories')
                            .composite;
                        fileBrowserModelConfig.filterDirectories = value;
                        browser.model.filterDirectories = value;
                    }
                    settings.changed.connect(onSettingsChanged);
                    onSettingsChanged(settings);
                });
            }
        });
    }
};
/**
 * The default file browser factory provider.
 */
const factory = {
    id: '@jupyterlab/filebrowser-extension:factory',
    provides: _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.IFileBrowserFactory,
    requires: [_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.IDocumentManager, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__.ITranslator],
    optional: [
        _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_6__.IStateDB,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.IRouter,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterFrontEnd.ITreeResolver,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterLab.IInfo
    ],
    activate: async (app, docManager, translator, state, router, tree, info) => {
        const { commands } = app;
        const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({ namespace });
        const createFileBrowser = (id, options = {}) => {
            var _a;
            const model = new _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.FilterFileBrowserModel({
                translator: translator,
                auto: (_a = options.auto) !== null && _a !== void 0 ? _a : true,
                manager: docManager,
                driveName: options.driveName || '',
                refreshInterval: options.refreshInterval,
                refreshStandby: () => {
                    if (info) {
                        return !info.isConnected || 'when-hidden';
                    }
                    return 'when-hidden';
                },
                state: options.state === null
                    ? undefined
                    : options.state || state || undefined
            });
            const restore = options.restore;
            const widget = new _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.FileBrowser({ id, model, restore, translator });
            // Track the newly created file browser.
            void tracker.add(widget);
            return widget;
        };
        // Manually restore and load the default file browser.
        const defaultBrowser = createFileBrowser('filebrowser', {
            auto: false,
            restore: false
        });
        void Private.restoreBrowser(defaultBrowser, commands, router, tree);
        return { createFileBrowser, defaultBrowser, tracker };
    }
};
/**
 * A plugin providing download + copy download link commands in the context menu.
 *
 * Disabling this plugin will NOT disable downloading files from the server.
 * Users will still be able to retrieve files from the file download URLs the
 * server provides.
 */
const downloadPlugin = {
    id: '@jupyterlab/filebrowser-extension:download',
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.IFileBrowserFactory, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__.ITranslator],
    autoStart: true,
    activate: (app, factory, translator) => {
        const trans = translator.load('jupyterlab');
        const { commands } = app;
        const { tracker } = factory;
        commands.addCommand(CommandIDs.download, {
            execute: () => {
                const widget = tracker.currentWidget;
                if (widget) {
                    return widget.download();
                }
            },
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.downloadIcon.bindprops({ stylesheet: 'menuItem' }),
            label: trans.__('Download')
        });
        commands.addCommand(CommandIDs.copyDownloadLink, {
            execute: () => {
                const widget = tracker.currentWidget;
                if (!widget) {
                    return;
                }
                return widget.model.manager.services.contents
                    .getDownloadUrl(widget.selectedItems().next().path)
                    .then(url => {
                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Clipboard.copyToSystem(url);
                });
            },
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.copyIcon.bindprops({ stylesheet: 'menuItem' }),
            label: trans.__('Copy Download Link'),
            mnemonic: 0
        });
    }
};
/**
 * A plugin to add the file browser widget to an ILabShell
 */
const browserWidget = {
    id: '@jupyterlab/filebrowser-extension:widget',
    requires: [
        _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.IDocumentManager,
        _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.IFileBrowserFactory,
        _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.ISettingRegistry,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IToolbarWidgetRegistry,
        _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__.ITranslator,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell,
        _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.IFileBrowserCommands
    ],
    autoStart: true,
    activate: (app, docManager, factory, settings, toolbarRegistry, translator, labShell) => {
        const { commands } = app;
        const { defaultBrowser: browser, tracker } = factory;
        const trans = translator.load('jupyterlab');
        // Set attributes when adding the browser to the UI
        browser.node.setAttribute('role', 'region');
        browser.node.setAttribute('aria-label', trans.__('File Browser Section'));
        browser.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.folderIcon;
        // Toolbar
        toolbarRegistry.addFactory(FILE_BROWSER_FACTORY, 'uploader', (browser) => new _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.Uploader({ model: browser.model, translator }));
        (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.setToolbar)(browser, (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.createToolbarFactory)(toolbarRegistry, settings, FILE_BROWSER_FACTORY, browserWidget.id, translator));
        labShell.add(browser, 'left', { rank: 100, type: 'File Browser' });
        commands.addCommand(CommandIDs.showBrowser, {
            label: trans.__('Open the file browser for the provided `path`.'),
            execute: args => {
                const path = args.path || '';
                const browserForPath = Private.getBrowserForPath(path, factory);
                // Check for browser not found
                if (!browserForPath) {
                    return;
                }
                // Shortcut if we are using the main file browser
                if (browser === browserForPath) {
                    labShell.activateById(browser.id);
                    return;
                }
                else {
                    const areas = ['left', 'right'];
                    for (const area of areas) {
                        const it = labShell.widgets(area);
                        let widget = it.next();
                        while (widget) {
                            if (widget.contains(browserForPath)) {
                                labShell.activateById(widget.id);
                                return;
                            }
                            widget = it.next();
                        }
                    }
                }
            }
        });
        commands.addCommand(CommandIDs.hideBrowser, {
            label: trans.__('Hide the file browser.'),
            execute: () => {
                const widget = tracker.currentWidget;
                if (widget && !widget.isHidden) {
                    labShell.collapseLeft();
                }
            }
        });
        // If the layout is a fresh session without saved data and not in single document
        // mode, open file browser.
        void labShell.restored.then(layout => {
            if (layout.fresh && labShell.mode !== 'single-document') {
                void commands.execute(CommandIDs.showBrowser, void 0);
            }
        });
        void Promise.all([app.restored, browser.model.restored]).then(() => {
            // Whether to automatically navigate to a document's current directory
            labShell.currentChanged.connect(async (_, change) => {
                if (browser.navigateToCurrentDirectory && change.newValue) {
                    const { newValue } = change;
                    const context = docManager.contextForWidget(newValue);
                    if (context) {
                        const { path } = context;
                        try {
                            await Private.navigateToPath(path, factory, translator);
                        }
                        catch (reason) {
                            console.warn(`${CommandIDs.goToPath} failed to open: ${path}`, reason);
                        }
                    }
                }
            });
        });
    }
};
/**
 * The default file browser share-file plugin
 *
 * This extension adds a "Copy Shareable Link" command that generates a copy-
 * pastable URL. This url can be used to open a particular file in JupyterLab,
 * handy for emailing links or bookmarking for reference.
 *
 * If you need to change how this link is generated (for instance, to copy a
 * /user-redirect URL for JupyterHub), disable this plugin and replace it
 * with another implementation.
 */
const shareFile = {
    id: '@jupyterlab/filebrowser-extension:share-file',
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.IFileBrowserFactory, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__.ITranslator],
    autoStart: true,
    activate: (app, factory, translator) => {
        const trans = translator.load('jupyterlab');
        const { commands } = app;
        const { tracker } = factory;
        commands.addCommand(CommandIDs.copyShareableLink, {
            execute: () => {
                const widget = tracker.currentWidget;
                const model = widget === null || widget === void 0 ? void 0 : widget.selectedItems().next();
                if (!model) {
                    return;
                }
                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Clipboard.copyToSystem(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getUrl({
                    workspace: _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.defaultWorkspace,
                    treePath: model.path,
                    toShare: true
                }));
            },
            isVisible: () => !!tracker.currentWidget &&
                (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__.toArray)(tracker.currentWidget.selectedItems()).length === 1,
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.linkIcon.bindprops({ stylesheet: 'menuItem' }),
            label: trans.__('Copy Shareable Link')
        });
    }
};
/**
 * The "Open With" context menu.
 *
 * This is its own plugin in case you would like to disable this feature.
 * e.g. jupyter labextension disable @jupyterlab/filebrowser-extension:open-with
 */
const openWithPlugin = {
    id: '@jupyterlab/filebrowser-extension:open-with',
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.IFileBrowserFactory],
    autoStart: true,
    activate: (app, factory) => {
        const { docRegistry } = app;
        const { tracker } = factory;
        let items = [];
        function updateOpenWithMenu(contextMenu) {
            var _a, _b;
            const openWith = (_b = (_a = contextMenu.menu.items.find(item => {
                var _a;
                return item.type === 'submenu' &&
                    ((_a = item.submenu) === null || _a === void 0 ? void 0 : _a.id) === 'jp-contextmenu-open-with';
            })) === null || _a === void 0 ? void 0 : _a.submenu) !== null && _b !== void 0 ? _b : null;
            if (!openWith) {
                return; // Bail early if the open with menu is not displayed
            }
            // clear the current menu items
            items.forEach(item => item.dispose());
            items.length = 0;
            // Ensure that the menu is empty
            openWith.clearItems();
            // get the widget factories that could be used to open all of the items
            // in the current filebrowser selection
            const factories = tracker.currentWidget
                ? Private.OpenWith.intersection((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__.map)(tracker.currentWidget.selectedItems(), i => {
                    return Private.OpenWith.getFactories(docRegistry, i);
                }))
                : new Set();
            // make new menu items from the widget factories
            items = [...factories].map(factory => openWith.addItem({
                args: { factory: factory.name, label: factory.label || factory.name },
                command: CommandIDs.open
            }));
        }
        app.contextMenu.opened.connect(updateOpenWithMenu);
    }
};
/**
 * The "Open in New Browser Tab" context menu.
 *
 * This is its own plugin in case you would like to disable this feature.
 * e.g. jupyter labextension disable @jupyterlab/filebrowser-extension:open-browser-tab
 *
 * Note: If disabling this, you may also want to disable:
 * @jupyterlab/docmanager-extension:open-browser-tab
 */
const openBrowserTabPlugin = {
    id: '@jupyterlab/filebrowser-extension:open-browser-tab',
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.IFileBrowserFactory, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__.ITranslator],
    autoStart: true,
    activate: (app, factory, translator) => {
        const { commands } = app;
        const trans = translator.load('jupyterlab');
        const { tracker } = factory;
        commands.addCommand(CommandIDs.openBrowserTab, {
            execute: args => {
                const widget = tracker.currentWidget;
                if (!widget) {
                    return;
                }
                const mode = args['mode'];
                return Promise.all((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__.toArray)((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__.map)(widget.selectedItems(), item => {
                    if (mode === 'single-document') {
                        const url = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getUrl({
                            mode: 'single-document',
                            treePath: item.path
                        });
                        const opened = window.open();
                        if (opened) {
                            opened.opener = null;
                            opened.location.href = url;
                        }
                        else {
                            throw new Error('Failed to open new browser tab.');
                        }
                    }
                    else {
                        return commands.execute('docmanager:open-browser-tab', {
                            path: item.path
                        });
                    }
                })));
            },
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.addIcon.bindprops({ stylesheet: 'menuItem' }),
            label: args => args['mode'] === 'single-document'
                ? trans.__('Open in Simple Mode')
                : trans.__('Open in New Browser Tab'),
            mnemonic: 0
        });
    }
};
/**
 * A plugin providing file upload status.
 */
const fileUploadStatus = {
    id: '@jupyterlab/filebrowser-extension:file-upload-status',
    autoStart: true,
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.IFileBrowserFactory, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__.ITranslator],
    optional: [_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_7__.IStatusBar],
    activate: (app, browser, translator, statusBar) => {
        if (!statusBar) {
            // Automatically disable if statusbar missing
            return;
        }
        const item = new _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.FileUploadStatus({
            tracker: browser.tracker,
            translator
        });
        statusBar.registerStatusItem('@jupyterlab/filebrowser-extension:file-upload-status', {
            item,
            align: 'middle',
            isActive: () => {
                return !!item.model && item.model.items.length > 0;
            },
            activeStateChanged: item.model.stateChanged
        });
    }
};
/**
 * A plugin to open files from remote URLs
 */
const openUrlPlugin = {
    id: '@jupyterlab/filebrowser-extension:open-url',
    autoStart: true,
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_4__.IFileBrowserFactory, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_8__.ITranslator],
    optional: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    activate: (app, factory, translator, palette) => {
        const { commands } = app;
        const trans = translator.load('jupyterlab');
        const { defaultBrowser: browser } = factory;
        const command = CommandIDs.openUrl;
        commands.addCommand(command, {
            label: args => args.url ? trans.__('Open %1', args.url) : trans.__('Open from URL…'),
            caption: args => args.url ? trans.__('Open %1', args.url) : trans.__('Open from URL'),
            execute: async (args) => {
                var _a, _b, _c;
                let url = (_a = args === null || args === void 0 ? void 0 : args.url) !== null && _a !== void 0 ? _a : '';
                if (!url) {
                    url =
                        (_b = (await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.InputDialog.getText({
                            label: trans.__('URL'),
                            placeholder: 'https://example.com/path/to/file',
                            title: trans.__('Open URL'),
                            okLabel: trans.__('Open')
                        })).value) !== null && _b !== void 0 ? _b : undefined;
                }
                if (!url) {
                    return;
                }
                let type = '';
                let blob;
                // fetch the file from the URL
                try {
                    const req = await fetch(url);
                    blob = await req.blob();
                    type = (_c = req.headers.get('Content-Type')) !== null && _c !== void 0 ? _c : '';
                }
                catch (reason) {
                    if (reason.response && reason.response.status !== 200) {
                        reason.message = trans.__('Could not open URL: %1', url);
                    }
                    return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)(trans.__('Cannot fetch'), reason);
                }
                // upload the content of the file to the server
                try {
                    const name = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PathExt.basename(url);
                    const file = new File([blob], name, { type });
                    const model = await browser.model.upload(file);
                    return commands.execute('docmanager:open', {
                        path: model.path
                    });
                }
                catch (error) {
                    return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)(trans._p('showErrorMessage', 'Upload Error'), error);
                }
            }
        });
        if (palette) {
            palette.addItem({
                command,
                category: trans.__('File Operations')
            });
        }
    }
};
/**
 * Add the main file browser commands to the application's command registry.
 */
function addCommands(app, factory, translator, settingRegistry, commandPalette) {
    const trans = translator.load('jupyterlab');
    const { docRegistry: registry, commands } = app;
    const { defaultBrowser: browser, tracker } = factory;
    commands.addCommand(CommandIDs.del, {
        execute: () => {
            const widget = tracker.currentWidget;
            if (widget) {
                return widget.delete();
            }
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.closeIcon.bindprops({ stylesheet: 'menuItem' }),
        label: trans.__('Delete'),
        mnemonic: 0
    });
    commands.addCommand(CommandIDs.copy, {
        execute: () => {
            const widget = tracker.currentWidget;
            if (widget) {
                return widget.copy();
            }
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.copyIcon.bindprops({ stylesheet: 'menuItem' }),
        label: trans.__('Copy'),
        mnemonic: 0
    });
    commands.addCommand(CommandIDs.cut, {
        execute: () => {
            const widget = tracker.currentWidget;
            if (widget) {
                return widget.cut();
            }
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.cutIcon.bindprops({ stylesheet: 'menuItem' }),
        label: trans.__('Cut')
    });
    commands.addCommand(CommandIDs.duplicate, {
        execute: () => {
            const widget = tracker.currentWidget;
            if (widget) {
                return widget.duplicate();
            }
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.copyIcon.bindprops({ stylesheet: 'menuItem' }),
        label: trans.__('Duplicate')
    });
    commands.addCommand(CommandIDs.goToPath, {
        label: trans.__('Update the file browser to display the provided `path`.'),
        execute: async (args) => {
            var _a;
            const path = args.path || '';
            const showBrowser = !((_a = args === null || args === void 0 ? void 0 : args.dontShowBrowser) !== null && _a !== void 0 ? _a : false);
            try {
                const item = await Private.navigateToPath(path, factory, translator);
                if (item.type !== 'directory' && showBrowser) {
                    const browserForPath = Private.getBrowserForPath(path, factory);
                    if (browserForPath) {
                        browserForPath.clearSelectedItems();
                        const parts = path.split('/');
                        const name = parts[parts.length - 1];
                        if (name) {
                            await browserForPath.selectItemByName(name);
                        }
                    }
                }
            }
            catch (reason) {
                console.warn(`${CommandIDs.goToPath} failed to go to: ${path}`, reason);
            }
            if (showBrowser) {
                return commands.execute(CommandIDs.showBrowser, { path });
            }
        }
    });
    commands.addCommand(CommandIDs.goUp, {
        label: 'go up',
        execute: async () => {
            const browserForPath = Private.getBrowserForPath('', factory);
            if (!browserForPath) {
                return;
            }
            const { model } = browserForPath;
            await model.restored;
            if (model.path === model.rootPath) {
                return;
            }
            try {
                await model.cd('..');
            }
            catch (reason) {
                console.warn(`${CommandIDs.goUp} failed to go to parent directory of ${model.path}`, reason);
            }
        }
    });
    commands.addCommand(CommandIDs.openPath, {
        label: args => args.path ? trans.__('Open %1', args.path) : trans.__('Open from Path…'),
        caption: args => args.path ? trans.__('Open %1', args.path) : trans.__('Open from path'),
        execute: async (args) => {
            var _a;
            let path;
            if (args === null || args === void 0 ? void 0 : args.path) {
                path = args.path;
            }
            else {
                path =
                    (_a = (await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.InputDialog.getText({
                        label: trans.__('Path'),
                        placeholder: '/path/relative/to/jlab/root',
                        title: trans.__('Open Path'),
                        okLabel: trans.__('Open')
                    })).value) !== null && _a !== void 0 ? _a : undefined;
            }
            if (!path) {
                return;
            }
            try {
                const trailingSlash = path !== '/' && path.endsWith('/');
                if (trailingSlash) {
                    // The normal contents service errors on paths ending in slash
                    path = path.slice(0, path.length - 1);
                }
                const browserForPath = Private.getBrowserForPath(path, factory);
                const { services } = browserForPath.model.manager;
                const item = await services.contents.get(path, {
                    content: false
                });
                if (trailingSlash && item.type !== 'directory') {
                    throw new Error(`Path ${path}/ is not a directory`);
                }
                await commands.execute(CommandIDs.goToPath, {
                    path,
                    dontShowBrowser: args.dontShowBrowser
                });
                if (item.type === 'directory') {
                    return;
                }
                return commands.execute('docmanager:open', { path });
            }
            catch (reason) {
                if (reason.response && reason.response.status === 404) {
                    reason.message = trans.__('Could not find path: %1', path);
                }
                return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)(trans.__('Cannot open'), reason);
            }
        }
    });
    // Add the openPath command to the command palette
    if (commandPalette) {
        commandPalette.addItem({
            command: CommandIDs.openPath,
            category: trans.__('File Operations')
        });
    }
    commands.addCommand(CommandIDs.open, {
        execute: args => {
            const factory = args['factory'] || void 0;
            const widget = tracker.currentWidget;
            if (!widget) {
                return;
            }
            const { contents } = widget.model.manager.services;
            return Promise.all((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__.toArray)((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__.map)(widget.selectedItems(), item => {
                if (item.type === 'directory') {
                    const localPath = contents.localPath(item.path);
                    return widget.model.cd(`/${localPath}`);
                }
                return commands.execute('docmanager:open', {
                    factory: factory,
                    path: item.path
                });
            })));
        },
        icon: args => {
            var _a;
            const factory = args['factory'] || void 0;
            if (factory) {
                // if an explicit factory is passed...
                const ft = registry.getFileType(factory);
                // ...set an icon if the factory name corresponds to a file type name...
                // ...or leave the icon blank
                return (_a = ft === null || ft === void 0 ? void 0 : ft.icon) === null || _a === void 0 ? void 0 : _a.bindprops({ stylesheet: 'menuItem' });
            }
            else {
                return _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.folderIcon.bindprops({ stylesheet: 'menuItem' });
            }
        },
        label: args => (args['label'] || args['factory'] || trans.__('Open')),
        mnemonic: 0
    });
    commands.addCommand(CommandIDs.paste, {
        execute: () => {
            const widget = tracker.currentWidget;
            if (widget) {
                return widget.paste();
            }
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.pasteIcon.bindprops({ stylesheet: 'menuItem' }),
        label: trans.__('Paste'),
        mnemonic: 0
    });
    commands.addCommand(CommandIDs.createNewDirectory, {
        execute: () => {
            const widget = tracker.currentWidget;
            if (widget) {
                return widget.createNewDirectory();
            }
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.newFolderIcon.bindprops({ stylesheet: 'menuItem' }),
        label: trans.__('New Folder')
    });
    commands.addCommand(CommandIDs.createNewFile, {
        execute: () => {
            const widget = tracker.currentWidget;
            if (widget) {
                return widget.createNewFile({ ext: 'txt' });
            }
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.textEditorIcon.bindprops({ stylesheet: 'menuItem' }),
        label: trans.__('New File')
    });
    commands.addCommand(CommandIDs.createNewMarkdownFile, {
        execute: () => {
            const widget = tracker.currentWidget;
            if (widget) {
                return widget.createNewFile({ ext: 'md' });
            }
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.markdownIcon.bindprops({ stylesheet: 'menuItem' }),
        label: trans.__('New Markdown File')
    });
    commands.addCommand(CommandIDs.refresh, {
        execute: args => {
            const widget = tracker.currentWidget;
            if (widget) {
                return widget.model.refresh();
            }
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.refreshIcon.bindprops({ stylesheet: 'menuItem' }),
        caption: trans.__('Refresh the file browser.'),
        label: trans.__('Refresh File List')
    });
    commands.addCommand(CommandIDs.rename, {
        execute: args => {
            const widget = tracker.currentWidget;
            if (widget) {
                return widget.rename();
            }
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.editIcon.bindprops({ stylesheet: 'menuItem' }),
        label: trans.__('Rename'),
        mnemonic: 0
    });
    commands.addCommand(CommandIDs.copyPath, {
        execute: () => {
            const widget = tracker.currentWidget;
            if (!widget) {
                return;
            }
            const item = widget.selectedItems().next();
            if (!item) {
                return;
            }
            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Clipboard.copyToSystem(item.path);
        },
        isVisible: () => !!tracker.currentWidget &&
            tracker.currentWidget.selectedItems().next !== undefined,
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.fileIcon.bindprops({ stylesheet: 'menuItem' }),
        label: trans.__('Copy Path')
    });
    commands.addCommand(CommandIDs.shutdown, {
        execute: () => {
            const widget = tracker.currentWidget;
            if (widget) {
                return widget.shutdownKernels();
            }
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_9__.stopIcon.bindprops({ stylesheet: 'menuItem' }),
        label: trans.__('Shut Down Kernel')
    });
    commands.addCommand(CommandIDs.toggleBrowser, {
        label: trans.__('File Browser'),
        execute: () => {
            if (browser.isHidden) {
                return commands.execute(CommandIDs.showBrowser, void 0);
            }
            return commands.execute(CommandIDs.hideBrowser, void 0);
        }
    });
    if (settingRegistry) {
        commands.addCommand(CommandIDs.toggleNavigateToCurrentDirectory, {
            label: trans.__('Show Active File in File Browser'),
            isToggled: () => browser.navigateToCurrentDirectory,
            execute: () => {
                const value = !browser.navigateToCurrentDirectory;
                const key = 'navigateToCurrentDirectory';
                return settingRegistry
                    .set(FILE_BROWSER_PLUGIN_ID, key, value)
                    .catch((reason) => {
                    console.error(`Failed to set navigateToCurrentDirectory setting`);
                });
            }
        });
    }
    commands.addCommand(CommandIDs.toggleLastModified, {
        label: trans.__('Show Last Modified Column'),
        isToggled: () => browser.showLastModifiedColumn,
        execute: () => {
            const value = !browser.showLastModifiedColumn;
            const key = 'showLastModifiedColumn';
            if (settingRegistry) {
                return settingRegistry
                    .set(FILE_BROWSER_PLUGIN_ID, key, value)
                    .catch((reason) => {
                    console.error(`Failed to set showLastModifiedColumn setting`);
                });
            }
        }
    });
    commands.addCommand(CommandIDs.toggleHiddenFiles, {
        label: trans.__('Show Hidden Files'),
        isToggled: () => browser.showHiddenFiles,
        isVisible: () => _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getOption('allow_hidden_files') === 'true',
        execute: () => {
            const value = !browser.showHiddenFiles;
            const key = 'showHiddenFiles';
            if (settingRegistry) {
                return settingRegistry
                    .set(FILE_BROWSER_PLUGIN_ID, key, value)
                    .catch((reason) => {
                    console.error(`Failed to set showHiddenFiles setting`);
                });
            }
        }
    });
    commands.addCommand(CommandIDs.toggleFileCheckboxes, {
        label: trans.__('Show File Checkboxes'),
        isToggled: () => browser.showFileCheckboxes,
        execute: () => {
            const value = !browser.showFileCheckboxes;
            const key = 'showFileCheckboxes';
            if (settingRegistry) {
                return settingRegistry
                    .set(FILE_BROWSER_PLUGIN_ID, key, value)
                    .catch((reason) => {
                    console.error(`Failed to set showFileCheckboxes setting`);
                });
            }
        }
    });
    commands.addCommand(CommandIDs.search, {
        label: trans.__('Search on File Names'),
        execute: () => alert('search')
    });
    if (commandPalette) {
        commandPalette.addItem({
            command: CommandIDs.toggleNavigateToCurrentDirectory,
            category: trans.__('File Operations')
        });
    }
}
/**
 * Export the plugins as default.
 */
const plugins = [
    factory,
    browser,
    shareFile,
    fileUploadStatus,
    downloadPlugin,
    browserWidget,
    openWithPlugin,
    openBrowserTabPlugin,
    openUrlPlugin
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);
/**
 * A namespace for private module data.
 */
var Private;
(function (Private) {
    /**
     * Get browser object given file path.
     */
    function getBrowserForPath(path, factory) {
        const { defaultBrowser: browser, tracker } = factory;
        const driveName = browser.model.manager.services.contents.driveName(path);
        if (driveName) {
            const browserForPath = tracker.find(_path => _path.model.driveName === driveName);
            if (!browserForPath) {
                // warn that no filebrowser could be found for this driveName
                console.warn(`${CommandIDs.goToPath} failed to find filebrowser for path: ${path}`);
                return;
            }
            return browserForPath;
        }
        // if driveName is empty, assume the main filebrowser
        return browser;
    }
    Private.getBrowserForPath = getBrowserForPath;
    /**
     * Navigate to a path or the path containing a file.
     */
    async function navigateToPath(path, factory, translator) {
        const trans = translator.load('jupyterlab');
        const browserForPath = Private.getBrowserForPath(path, factory);
        if (!browserForPath) {
            throw new Error(trans.__('No browser for path'));
        }
        const { services } = browserForPath.model.manager;
        const localPath = services.contents.localPath(path);
        await services.ready;
        const item = await services.contents.get(path, { content: false });
        const { model } = browserForPath;
        await model.restored;
        if (item.type === 'directory') {
            await model.cd(`/${localPath}`);
        }
        else {
            await model.cd(`/${_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PathExt.dirname(localPath)}`);
        }
        return item;
    }
    Private.navigateToPath = navigateToPath;
    /**
     * Restores file browser state and overrides state if tree resolver resolves.
     */
    async function restoreBrowser(browser, commands, router, tree) {
        const restoring = 'jp-mod-restoring';
        browser.addClass(restoring);
        if (!router) {
            await browser.model.restore(browser.id);
            await browser.model.refresh();
            browser.removeClass(restoring);
            return;
        }
        const listener = async () => {
            router.routed.disconnect(listener);
            const paths = await (tree === null || tree === void 0 ? void 0 : tree.paths);
            if ((paths === null || paths === void 0 ? void 0 : paths.file) || (paths === null || paths === void 0 ? void 0 : paths.browser)) {
                // Restore the model without populating it.
                await browser.model.restore(browser.id, false);
                if (paths.file) {
                    await commands.execute(CommandIDs.openPath, {
                        path: paths.file,
                        dontShowBrowser: true
                    });
                }
                if (paths.browser) {
                    await commands.execute(CommandIDs.openPath, {
                        path: paths.browser,
                        dontShowBrowser: true
                    });
                }
            }
            else {
                await browser.model.restore(browser.id);
                await browser.model.refresh();
            }
            browser.removeClass(restoring);
        };
        router.routed.connect(listener);
    }
    Private.restoreBrowser = restoreBrowser;
    let OpenWith;
    (function (OpenWith) {
        /**
         * Get the factories for the selected item
         *
         * @param docRegistry Application document registry
         * @param item Selected item model
         * @returns Available factories for the model
         */
        function getFactories(docRegistry, item) {
            const factories = docRegistry.preferredWidgetFactories(item.path);
            const notebookFactory = docRegistry.getWidgetFactory('notebook');
            if (notebookFactory &&
                item.type === 'notebook' &&
                factories.indexOf(notebookFactory) === -1) {
                factories.unshift(notebookFactory);
            }
            return factories;
        }
        OpenWith.getFactories = getFactories;
        /**
         * Return the intersection of multiple arrays.
         *
         * @param iter Iterator of arrays
         * @returns Set of common elements to all arrays
         */
        function intersection(iter) {
            // pop the first element of iter
            const first = iter.next();
            // first will be undefined if iter is empty
            if (!first) {
                return new Set();
            }
            // "initialize" the intersection from first
            const isect = new Set(first);
            // reduce over the remaining elements of iter
            return (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_10__.reduce)(iter, (isect, subarr) => {
                // filter out all elements not present in both isect and subarr,
                // accumulate result in new set
                return new Set(subarr.filter(x => isect.has(x)));
            }, isect);
        }
        OpenWith.intersection = intersection;
    })(OpenWith = Private.OpenWith || (Private.OpenWith = {}));
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfZmlsZWJyb3dzZXItZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy42MzYzNGE0YmQwYWI4ZGY2YjM4MS5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBVThCO0FBVUg7QUFDOEI7QUFDRjtBQVN6QjtBQUU4QjtBQUNoQjtBQUNJO0FBQ0c7QUFtQm5CO0FBQ3VDO0FBQ3ZCO0FBR25ELE1BQU0sb0JBQW9CLEdBQUcsYUFBYSxDQUFDO0FBQzNDLE1BQU0sc0JBQXNCLEdBQUcsMkNBQTJDLENBQUM7QUFFM0U7O0dBRUc7QUFDSCxJQUFVLFVBQVUsQ0ErRG5CO0FBL0RELFdBQVUsVUFBVTtJQUNMLGVBQUksR0FBRyxrQkFBa0IsQ0FBQztJQUUxQiwyQkFBZ0IsR0FBRyxnQ0FBZ0MsQ0FBQztJQUVwRCxjQUFHLEdBQUcsaUJBQWlCLENBQUM7SUFFeEIsY0FBRyxHQUFHLG9CQUFvQixDQUFDO0lBRTNCLG1CQUFRLEdBQUcsc0JBQXNCLENBQUM7SUFFbEMsb0JBQVMsR0FBRyx1QkFBdUIsQ0FBQztJQUVqRCx5QkFBeUI7SUFDWixzQkFBVyxHQUFHLHVCQUF1QixDQUFDO0lBRXRDLG1CQUFRLEdBQUcsd0JBQXdCLENBQUM7SUFFcEMsZUFBSSxHQUFHLG1CQUFtQixDQUFDO0lBRTNCLG1CQUFRLEdBQUcsdUJBQXVCLENBQUM7SUFFbkMsa0JBQU8sR0FBRyxzQkFBc0IsQ0FBQztJQUVqQyxlQUFJLEdBQUcsa0JBQWtCLENBQUM7SUFFMUIseUJBQWMsR0FBRyw4QkFBOEIsQ0FBQztJQUVoRCxnQkFBSyxHQUFHLG1CQUFtQixDQUFDO0lBRTVCLDZCQUFrQixHQUFHLGtDQUFrQyxDQUFDO0lBRXhELHdCQUFhLEdBQUcsNkJBQTZCLENBQUM7SUFFOUMsZ0NBQXFCLEdBQUcsc0NBQXNDLENBQUM7SUFFL0Qsa0JBQU8sR0FBRyxxQkFBcUIsQ0FBQztJQUVo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WUFDdkQsZ0NBQWdDO1lBQ2hDLE1BQU0sS0FBSyxHQUFHLElBQUksQ0FBQyxJQUFJLEVBQUUsQ0FBQztZQUMxQiwyQ0FBMkM7WUFDM0MsSUFBSSxDQUFDLEtBQUssRUFBRTtnQkFDVixPQUFPLElBQUksR0FBRyxFQUFLLENBQUM7YUFDckI7WUFFRCwyQ0FBMkM7WUFDM0MsTUFBTSxLQUFLLEdBQUcsSUFBSSxHQUFHLENBQUMsS0FBSyxDQUFDLENBQUM7WUFDN0IsNkNBQTZDO1lBQzdDLE9BQU8sMERBQU0sQ0FDWCxJQUFJLEVBQ0osQ0FBQyxLQUFLLEVBQUUsTUFBTSxFQUFFLEVBQUU7Z0JBQ2hCLGdFQUFnRTtnQkFDaEUsK0JBQStCO2dCQUMvQixPQUFPLElBQUksR0FBRyxDQUFDLE1BQU0sQ0FBQyxNQUFNLENBQUMsQ0FBQyxDQUFDLEVBQUUsQ0FBQyxLQUFLLENBQUMsR0FBRyxDQUFDLENBQUMsQ0FBQyxDQUFDLENBQUMsQ0FBQztZQUNuRCxDQUFDLEVBQ0QsS0FBSyxDQUNOLENBQUM7UUFDSixDQUFDO1FBcEJlLHFCQUFZLGVBb0IzQjtJQUNILENBQUMsRUFwRGdCLFFBQVEsR0FBUixnQkFBUSxLQUFSLGdCQUFRLFFBb0R4QjtBQUNILENBQUMsRUFoS1MsT0FBTyxLQUFQLE9BQU8sUUFnS2hCIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2ZpbGVicm93c2VyLWV4dGVuc2lvbi9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgZmlsZWJyb3dzZXItZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSUxhYlNoZWxsLFxuICBJTGF5b3V0UmVzdG9yZXIsXG4gIElSb3V0ZXIsXG4gIElUcmVlUGF0aFVwZGF0ZXIsXG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luLFxuICBKdXB5dGVyTGFiXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7XG4gIENsaXBib2FyZCxcbiAgY3JlYXRlVG9vbGJhckZhY3RvcnksXG4gIElDb21tYW5kUGFsZXR0ZSxcbiAgSW5wdXREaWFsb2csXG4gIElUb29sYmFyV2lkZ2V0UmVnaXN0cnksXG4gIHNldFRvb2xiYXIsXG4gIHNob3dFcnJvck1lc3NhZ2UsXG4gIFdpZGdldFRyYWNrZXJcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgUGFnZUNvbmZpZywgUGF0aEV4dCB9IGZyb20gJ0BqdXB5dGVybGFiL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBJRG9jdW1lbnRNYW5hZ2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jbWFuYWdlcic7XG5pbXBvcnQgeyBEb2N1bWVudFJlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jcmVnaXN0cnknO1xuaW1wb3J0IHtcbiAgRmlsZUJyb3dzZXIsXG4gIEZpbGVVcGxvYWRTdGF0dXMsXG4gIEZpbHRlckZpbGVCcm93c2VyTW9kZWwsXG4gIElGaWxlQnJvd3NlckNvbW1hbmRzLFxuICBJRmlsZUJyb3dzZXJGYWN0b3J5LFxuICBVcGxvYWRlclxufSBmcm9tICdAanVweXRlcmxhYi9maWxlYnJvd3Nlcic7XG5pbXBvcnQgeyBDb250ZW50cyB9IGZyb20gJ0BqdXB5dGVybGFiL3NlcnZpY2VzJztcbmltcG9ydCB7IElTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHsgSVN0YXRlREIgfSBmcm9tICdAanVweXRlcmxhYi9zdGF0ZWRiJztcbmltcG9ydCB7IElTdGF0dXNCYXIgfSBmcm9tICdAanVweXRlcmxhYi9zdGF0dXNiYXInO1xuaW1wb3J0IHsgSVRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQge1xuICBhZGRJY29uLFxuICBjbG9zZUljb24sXG4gIGNvcHlJY29uLFxuICBjdXRJY29uLFxuICBkb3dubG9hZEljb24sXG4gIGVkaXRJY29uLFxuICBmaWxlSWNvbixcbiAgZm9sZGVySWNvbixcbiAgSURpc3Bvc2FibGVNZW51SXRlbSxcbiAgbGlua0ljb24sXG4gIG1hcmtkb3duSWNvbixcbiAgbmV3Rm9sZGVySWNvbixcbiAgcGFzdGVJY29uLFxuICBSYW5rZWRNZW51LFxuICByZWZyZXNoSWNvbixcbiAgc3RvcEljb24sXG4gIHRleHRFZGl0b3JJY29uXG59IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0IHsgZmluZCwgSUl0ZXJhdG9yLCBtYXAsIHJlZHVjZSwgdG9BcnJheSB9IGZyb20gJ0BsdW1pbm8vYWxnb3JpdGhtJztcbmltcG9ydCB7IENvbW1hbmRSZWdpc3RyeSB9IGZyb20gJ0BsdW1pbm8vY29tbWFuZHMnO1xuaW1wb3J0IHsgQ29udGV4dE1lbnUgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuXG5jb25zdCBGSUxFX0JST1dTRVJfRkFDVE9SWSA9ICdGaWxlQnJvd3Nlcic7XG5jb25zdCBGSUxFX0JST1dTRVJfUExVR0lOX0lEID0gJ0BqdXB5dGVybGFiL2ZpbGVicm93c2VyLWV4dGVuc2lvbjpicm93c2VyJztcblxuLyoqXG4gKiBUaGUgY29tbWFuZCBJRHMgdXNlZCBieSB0aGUgZmlsZSBicm93c2VyIHBsdWdpbi5cbiAqL1xubmFtZXNwYWNlIENvbW1hbmRJRHMge1xuICBleHBvcnQgY29uc3QgY29weSA9ICdmaWxlYnJvd3Nlcjpjb3B5JztcblxuICBleHBvcnQgY29uc3QgY29weURvd25sb2FkTGluayA9ICdmaWxlYnJvd3Nlcjpjb3B5LWRvd25sb2FkLWxpbmsnO1xuXG4gIGV4cG9ydCBjb25zdCBjdXQgPSAnZmlsZWJyb3dzZXI6Y3V0JztcblxuICBleHBvcnQgY29uc3QgZGVsID0gJ2ZpbGVicm93c2VyOmRlbGV0ZSc7XG5cbiAgZXhwb3J0IGNvbnN0IGRvd25sb2FkID0gJ2ZpbGVicm93c2VyOmRvd25sb2FkJztcblxuICBleHBvcnQgY29uc3QgZHVwbGljYXRlID0gJ2ZpbGVicm93c2VyOmR1cGxpY2F0ZSc7XG5cbiAgLy8gRm9yIG1haW4gYnJvd3NlciBvbmx5LlxuICBleHBvcnQgY29uc3QgaGlkZUJyb3dzZXIgPSAnZmlsZWJyb3dzZXI6aGlkZS1tYWluJztcblxuICBleHBvcnQgY29uc3QgZ29Ub1BhdGggPSAnZmlsZWJyb3dzZXI6Z28tdG8tcGF0aCc7XG5cbiAgZXhwb3J0IGNvbnN0IGdvVXAgPSAnZmlsZWJyb3dzZXI6Z28tdXAnO1xuXG4gIGV4cG9ydCBjb25zdCBvcGVuUGF0aCA9ICdmaWxlYnJvd3NlcjpvcGVuLXBhdGgnO1xuXG4gIGV4cG9ydCBjb25zdCBvcGVuVXJsID0gJ2ZpbGVicm93c2VyOm9wZW4tdXJsJztcblxuICBleHBvcnQgY29uc3Qgb3BlbiA9ICdmaWxlYnJvd3NlcjpvcGVuJztcblxuICBleHBvcnQgY29uc3Qgb3BlbkJyb3dzZXJUYWIgPSAnZmlsZWJyb3dzZXI6b3Blbi1icm93c2VyLXRhYic7XG5cbiAgZXhwb3J0IGNvbnN0IHBhc3RlID0gJ2ZpbGVicm93c2VyOnBhc3RlJztcblxuICBleHBvcnQgY29uc3QgY3JlYXRlTmV3RGlyZWN0b3J5ID0gJ2ZpbGVicm93c2VyOmNyZWF0ZS1uZXctZGlyZWN0b3J5JztcblxuICBleHBvcnQgY29uc3QgY3JlYXRlTmV3RmlsZSA9ICdmaWxlYnJvd3NlcjpjcmVhdGUtbmV3LWZpbGUnO1xuXG4gIGV4cG9ydCBjb25zdCBjcmVhdGVOZXdNYXJrZG93bkZpbGUgPSAnZmlsZWJyb3dzZXI6Y3JlYXRlLW5ldy1tYXJrZG93bi1maWxlJztcblxuICBleHBvcnQgY29uc3QgcmVmcmVzaCA9ICdmaWxlYnJvd3NlcjpyZWZyZXNoJztcblxuICBleHBvcnQgY29uc3QgcmVuYW1lID0gJ2ZpbGVicm93c2VyOnJlbmFtZSc7XG5cbiAgLy8gRm9yIG1haW4gYnJvd3NlciBvbmx5LlxuICBleHBvcnQgY29uc3QgY29weVNoYXJlYWJsZUxpbmsgPSAnZmlsZWJyb3dzZXI6c2hhcmUtbWFpbic7XG5cbiAgLy8gRm9yIG1haW4gYnJvd3NlciBvbmx5LlxuICBleHBvcnQgY29uc3QgY29weVBhdGggPSAnZmlsZWJyb3dzZXI6Y29weS1wYXRoJztcblxuICBleHBvcnQgY29uc3Qgc2hvd0Jyb3dzZXIgPSAnZmlsZWJyb3dzZXI6YWN0aXZhdGUnO1xuXG4gIGV4cG9ydCBjb25zdCBzaHV0ZG93biA9ICdmaWxlYnJvd3NlcjpzaHV0ZG93bic7XG5cbiAgLy8gRm9yIG1haW4gYnJvd3NlciBvbmx5LlxuICBleHBvcnQgY29uc3QgdG9nZ2xlQnJvd3NlciA9ICdmaWxlYnJvd3Nlcjp0b2dnbGUtbWFpbic7XG5cbiAgZXhwb3J0IGNvbnN0IHRvZ2dsZU5hdmlnYXRlVG9DdXJyZW50RGlyZWN0b3J5ID1cbiAgICAnZmlsZWJyb3dzZXI6dG9nZ2xlLW5hdmlnYXRlLXRvLWN1cnJlbnQtZGlyZWN0b3J5JztcblxuICBleHBvcnQgY29uc3QgdG9nZ2xlTGFzdE1vZGlmaWVkID0gJ2ZpbGVicm93c2VyOnRvZ2dsZS1sYXN0LW1vZGlmaWVkJztcblxuICBleHBvcnQgY29uc3Qgc2VhcmNoID0gJ2ZpbGVicm93c2VyOnNlYXJjaCc7XG5cbiAgZXhwb3J0IGNvbnN0IHRvZ2dsZUhpZGRlbkZpbGVzID0gJ2ZpbGVicm93c2VyOnRvZ2dsZS1oaWRkZW4tZmlsZXMnO1xuXG4gIGV4cG9ydCBjb25zdCB0b2dnbGVGaWxlQ2hlY2tib3hlcyA9ICdmaWxlYnJvd3Nlcjp0b2dnbGUtZmlsZS1jaGVja2JveGVzJztcbn1cblxuLyoqXG4gKiBUaGUgZmlsZSBicm93c2VyIG5hbWVzcGFjZSB0b2tlbi5cbiAqL1xuY29uc3QgbmFtZXNwYWNlID0gJ2ZpbGVicm93c2VyJztcblxuLyoqXG4gKiBUaGUgZGVmYXVsdCBmaWxlIGJyb3dzZXIgZXh0ZW5zaW9uLlxuICovXG5jb25zdCBicm93c2VyOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiBGSUxFX0JST1dTRVJfUExVR0lOX0lELFxuICByZXF1aXJlczogW0lGaWxlQnJvd3NlckZhY3RvcnksIElUcmFuc2xhdG9yXSxcbiAgb3B0aW9uYWw6IFtcbiAgICBJTGF5b3V0UmVzdG9yZXIsXG4gICAgSVNldHRpbmdSZWdpc3RyeSxcbiAgICBJVHJlZVBhdGhVcGRhdGVyLFxuICAgIElDb21tYW5kUGFsZXR0ZVxuICBdLFxuICBwcm92aWRlczogSUZpbGVCcm93c2VyQ29tbWFuZHMsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgYWN0aXZhdGU6IGFzeW5jIChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICBmYWN0b3J5OiBJRmlsZUJyb3dzZXJGYWN0b3J5LFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICAgIHJlc3RvcmVyOiBJTGF5b3V0UmVzdG9yZXIgfCBudWxsLFxuICAgIHNldHRpbmdSZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSB8IG51bGwsXG4gICAgdHJlZVBhdGhVcGRhdGVyOiBJVHJlZVBhdGhVcGRhdGVyIHwgbnVsbCxcbiAgICBjb21tYW5kUGFsZXR0ZTogSUNvbW1hbmRQYWxldHRlIHwgbnVsbFxuICApOiBQcm9taXNlPHZvaWQ+ID0+IHtcbiAgICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IGJyb3dzZXIgPSBmYWN0b3J5LmRlZmF1bHRCcm93c2VyO1xuXG4gICAgLy8gTGV0IHRoZSBhcHBsaWNhdGlvbiByZXN0b3JlciB0cmFjayB0aGUgcHJpbWFyeSBmaWxlIGJyb3dzZXIgKHRoYXQgaXNcbiAgICAvLyBhdXRvbWF0aWNhbGx5IGNyZWF0ZWQpIGZvciByZXN0b3JhdGlvbiBvZiBhcHBsaWNhdGlvbiBzdGF0ZSAoZS5nLiBzZXR0aW5nXG4gICAgLy8gdGhlIGZpbGUgYnJvd3NlciBhcyB0aGUgY3VycmVudCBzaWRlIGJhciB3aWRnZXQpLlxuICAgIC8vXG4gICAgLy8gQWxsIG90aGVyIGZpbGUgYnJvd3NlcnMgY3JlYXRlZCBieSB1c2luZyB0aGUgZmFjdG9yeSBmdW5jdGlvbiBhcmVcbiAgICAvLyByZXNwb25zaWJsZSBmb3IgdGhlaXIgb3duIHJlc3RvcmF0aW9uIGJlaGF2aW9yLCBpZiBhbnkuXG4gICAgaWYgKHJlc3RvcmVyKSB7XG4gICAgICByZXN0b3Jlci5hZGQoYnJvd3NlciwgbmFtZXNwYWNlKTtcbiAgICB9XG5cbiAgICAvLyBOYXZpZ2F0ZSB0byBwcmVmZXJyZWQtZGlyIHRyYWl0IGlmIGZvdW5kXG4gICAgY29uc3QgcHJlZmVycmVkUGF0aCA9IFBhZ2VDb25maWcuZ2V0T3B0aW9uKCdwcmVmZXJyZWRQYXRoJyk7XG4gICAgaWYgKHByZWZlcnJlZFBhdGgpIHtcbiAgICAgIGF3YWl0IGJyb3dzZXIubW9kZWwuY2QocHJlZmVycmVkUGF0aCk7XG4gICAgfVxuXG4gICAgYWRkQ29tbWFuZHMoYXBwLCBmYWN0b3J5LCB0cmFuc2xhdG9yLCBzZXR0aW5nUmVnaXN0cnksIGNvbW1hbmRQYWxldHRlKTtcblxuICAgIC8vIFNob3cgdGhlIGN1cnJlbnQgZmlsZSBicm93c2VyIHNob3J0Y3V0IGluIGl0cyB0aXRsZS5cbiAgICBjb25zdCB1cGRhdGVCcm93c2VyVGl0bGUgPSAoKSA9PiB7XG4gICAgICBjb25zdCBiaW5kaW5nID0gZmluZChcbiAgICAgICAgYXBwLmNvbW1hbmRzLmtleUJpbmRpbmdzLFxuICAgICAgICBiID0+IGIuY29tbWFuZCA9PT0gQ29tbWFuZElEcy50b2dnbGVCcm93c2VyXG4gICAgICApO1xuICAgICAgaWYgKGJpbmRpbmcpIHtcbiAgICAgICAgY29uc3Qga3MgPSBDb21tYW5kUmVnaXN0cnkuZm9ybWF0S2V5c3Ryb2tlKGJpbmRpbmcua2V5cy5qb2luKCcgJykpO1xuICAgICAgICBicm93c2VyLnRpdGxlLmNhcHRpb24gPSB0cmFucy5fXygnRmlsZSBCcm93c2VyICglMSknLCBrcyk7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICBicm93c2VyLnRpdGxlLmNhcHRpb24gPSB0cmFucy5fXygnRmlsZSBCcm93c2VyJyk7XG4gICAgICB9XG4gICAgfTtcbiAgICB1cGRhdGVCcm93c2VyVGl0bGUoKTtcbiAgICBhcHAuY29tbWFuZHMua2V5QmluZGluZ0NoYW5nZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICB1cGRhdGVCcm93c2VyVGl0bGUoKTtcbiAgICB9KTtcblxuICAgIHJldHVybiB2b2lkIFByb21pc2UuYWxsKFthcHAucmVzdG9yZWQsIGJyb3dzZXIubW9kZWwucmVzdG9yZWRdKS50aGVuKCgpID0+IHtcbiAgICAgIGlmICh0cmVlUGF0aFVwZGF0ZXIpIHtcbiAgICAgICAgYnJvd3Nlci5tb2RlbC5wYXRoQ2hhbmdlZC5jb25uZWN0KChzZW5kZXIsIGFyZ3MpID0+IHtcbiAgICAgICAgICB0cmVlUGF0aFVwZGF0ZXIoYXJncy5uZXdWYWx1ZSk7XG4gICAgICAgIH0pO1xuICAgICAgfVxuXG4gICAgICBpZiAoc2V0dGluZ1JlZ2lzdHJ5KSB7XG4gICAgICAgIHZvaWQgc2V0dGluZ1JlZ2lzdHJ5LmxvYWQoRklMRV9CUk9XU0VSX1BMVUdJTl9JRCkudGhlbihzZXR0aW5ncyA9PiB7XG4gICAgICAgICAgLyoqXG4gICAgICAgICAgICogRmlsZSBicm93c2VyIGNvbmZpZ3VyYXRpb24uXG4gICAgICAgICAgICovXG4gICAgICAgICAgY29uc3QgZmlsZUJyb3dzZXJDb25maWcgPSB7XG4gICAgICAgICAgICBuYXZpZ2F0ZVRvQ3VycmVudERpcmVjdG9yeTogZmFsc2UsXG4gICAgICAgICAgICBzaG93TGFzdE1vZGlmaWVkQ29sdW1uOiB0cnVlLFxuICAgICAgICAgICAgdXNlRnV6enlGaWx0ZXI6IHRydWUsXG4gICAgICAgICAgICBzaG93SGlkZGVuRmlsZXM6IGZhbHNlLFxuICAgICAgICAgICAgc2hvd0ZpbGVDaGVja2JveGVzOiBmYWxzZVxuICAgICAgICAgIH07XG4gICAgICAgICAgY29uc3QgZmlsZUJyb3dzZXJNb2RlbENvbmZpZyA9IHtcbiAgICAgICAgICAgIGZpbHRlckRpcmVjdG9yaWVzOiB0cnVlXG4gICAgICAgICAgfTtcblxuICAgICAgICAgIGZ1bmN0aW9uIG9uU2V0dGluZ3NDaGFuZ2VkKFxuICAgICAgICAgICAgc2V0dGluZ3M6IElTZXR0aW5nUmVnaXN0cnkuSVNldHRpbmdzXG4gICAgICAgICAgKTogdm9pZCB7XG4gICAgICAgICAgICBsZXQga2V5OiBrZXlvZiB0eXBlb2YgZmlsZUJyb3dzZXJDb25maWc7XG4gICAgICAgICAgICBmb3IgKGtleSBpbiBmaWxlQnJvd3NlckNvbmZpZykge1xuICAgICAgICAgICAgICBjb25zdCB2YWx1ZSA9IHNldHRpbmdzLmdldChrZXkpLmNvbXBvc2l0ZSBhcyBib29sZWFuO1xuICAgICAgICAgICAgICBmaWxlQnJvd3NlckNvbmZpZ1trZXldID0gdmFsdWU7XG4gICAgICAgICAgICAgIGJyb3dzZXJba2V5XSA9IHZhbHVlO1xuICAgICAgICAgICAgfVxuXG4gICAgICAgICAgICBjb25zdCB2YWx1ZSA9IHNldHRpbmdzLmdldCgnZmlsdGVyRGlyZWN0b3JpZXMnKVxuICAgICAgICAgICAgICAuY29tcG9zaXRlIGFzIGJvb2xlYW47XG4gICAgICAgICAgICBmaWxlQnJvd3Nlck1vZGVsQ29uZmlnLmZpbHRlckRpcmVjdG9yaWVzID0gdmFsdWU7XG4gICAgICAgICAgICBicm93c2VyLm1vZGVsLmZpbHRlckRpcmVjdG9yaWVzID0gdmFsdWU7XG4gICAgICAgICAgfVxuICAgICAgICAgIHNldHRpbmdzLmNoYW5nZWQuY29ubmVjdChvblNldHRpbmdzQ2hhbmdlZCk7XG4gICAgICAgICAgb25TZXR0aW5nc0NoYW5nZWQoc2V0dGluZ3MpO1xuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9KTtcbiAgfVxufTtcblxuLyoqXG4gKiBUaGUgZGVmYXVsdCBmaWxlIGJyb3dzZXIgZmFjdG9yeSBwcm92aWRlci5cbiAqL1xuY29uc3QgZmFjdG9yeTogSnVweXRlckZyb250RW5kUGx1Z2luPElGaWxlQnJvd3NlckZhY3Rvcnk+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2ZpbGVicm93c2VyLWV4dGVuc2lvbjpmYWN0b3J5JyxcbiAgcHJvdmlkZXM6IElGaWxlQnJvd3NlckZhY3RvcnksXG4gIHJlcXVpcmVzOiBbSURvY3VtZW50TWFuYWdlciwgSVRyYW5zbGF0b3JdLFxuICBvcHRpb25hbDogW1xuICAgIElTdGF0ZURCLFxuICAgIElSb3V0ZXIsXG4gICAgSnVweXRlckZyb250RW5kLklUcmVlUmVzb2x2ZXIsXG4gICAgSnVweXRlckxhYi5JSW5mb1xuICBdLFxuICBhY3RpdmF0ZTogYXN5bmMgKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIGRvY01hbmFnZXI6IElEb2N1bWVudE1hbmFnZXIsXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gICAgc3RhdGU6IElTdGF0ZURCIHwgbnVsbCxcbiAgICByb3V0ZXI6IElSb3V0ZXIgfCBudWxsLFxuICAgIHRyZWU6IEp1cHl0ZXJGcm9udEVuZC5JVHJlZVJlc29sdmVyIHwgbnVsbCxcbiAgICBpbmZvOiBKdXB5dGVyTGFiLklJbmZvIHwgbnVsbFxuICApOiBQcm9taXNlPElGaWxlQnJvd3NlckZhY3Rvcnk+ID0+IHtcbiAgICBjb25zdCB7IGNvbW1hbmRzIH0gPSBhcHA7XG4gICAgY29uc3QgdHJhY2tlciA9IG5ldyBXaWRnZXRUcmFja2VyPEZpbGVCcm93c2VyPih7IG5hbWVzcGFjZSB9KTtcbiAgICBjb25zdCBjcmVhdGVGaWxlQnJvd3NlciA9IChcbiAgICAgIGlkOiBzdHJpbmcsXG4gICAgICBvcHRpb25zOiBJRmlsZUJyb3dzZXJGYWN0b3J5LklPcHRpb25zID0ge31cbiAgICApID0+IHtcbiAgICAgIGNvbnN0IG1vZGVsID0gbmV3IEZpbHRlckZpbGVCcm93c2VyTW9kZWwoe1xuICAgICAgICB0cmFuc2xhdG9yOiB0cmFuc2xhdG9yLFxuICAgICAgICBhdXRvOiBvcHRpb25zLmF1dG8gPz8gdHJ1ZSxcbiAgICAgICAgbWFuYWdlcjogZG9jTWFuYWdlcixcbiAgICAgICAgZHJpdmVOYW1lOiBvcHRpb25zLmRyaXZlTmFtZSB8fCAnJyxcbiAgICAgICAgcmVmcmVzaEludGVydmFsOiBvcHRpb25zLnJlZnJlc2hJbnRlcnZhbCxcbiAgICAgICAgcmVmcmVzaFN0YW5kYnk6ICgpID0+IHtcbiAgICAgICAgICBpZiAoaW5mbykge1xuICAgICAgICAgICAgcmV0dXJuICFpbmZvLmlzQ29ubmVjdGVkIHx8ICd3aGVuLWhpZGRlbic7XG4gICAgICAgICAgfVxuICAgICAgICAgIHJldHVybiAnd2hlbi1oaWRkZW4nO1xuICAgICAgICB9LFxuICAgICAgICBzdGF0ZTpcbiAgICAgICAgICBvcHRpb25zLnN0YXRlID09PSBudWxsXG4gICAgICAgICAgICA/IHVuZGVmaW5lZFxuICAgICAgICAgICAgOiBvcHRpb25zLnN0YXRlIHx8IHN0YXRlIHx8IHVuZGVmaW5lZFxuICAgICAgfSk7XG4gICAgICBjb25zdCByZXN0b3JlID0gb3B0aW9ucy5yZXN0b3JlO1xuICAgICAgY29uc3Qgd2lkZ2V0ID0gbmV3IEZpbGVCcm93c2VyKHsgaWQsIG1vZGVsLCByZXN0b3JlLCB0cmFuc2xhdG9yIH0pO1xuXG4gICAgICAvLyBUcmFjayB0aGUgbmV3bHkgY3JlYXRlZCBmaWxlIGJyb3dzZXIuXG4gICAgICB2b2lkIHRyYWNrZXIuYWRkKHdpZGdldCk7XG5cbiAgICAgIHJldHVybiB3aWRnZXQ7XG4gICAgfTtcblxuICAgIC8vIE1hbnVhbGx5IHJlc3RvcmUgYW5kIGxvYWQgdGhlIGRlZmF1bHQgZmlsZSBicm93c2VyLlxuICAgIGNvbnN0IGRlZmF1bHRCcm93c2VyID0gY3JlYXRlRmlsZUJyb3dzZXIoJ2ZpbGVicm93c2VyJywge1xuICAgICAgYXV0bzogZmFsc2UsXG4gICAgICByZXN0b3JlOiBmYWxzZVxuICAgIH0pO1xuICAgIHZvaWQgUHJpdmF0ZS5yZXN0b3JlQnJvd3NlcihkZWZhdWx0QnJvd3NlciwgY29tbWFuZHMsIHJvdXRlciwgdHJlZSk7XG5cbiAgICByZXR1cm4geyBjcmVhdGVGaWxlQnJvd3NlciwgZGVmYXVsdEJyb3dzZXIsIHRyYWNrZXIgfTtcbiAgfVxufTtcblxuLyoqXG4gKiBBIHBsdWdpbiBwcm92aWRpbmcgZG93bmxvYWQgKyBjb3B5IGRvd25sb2FkIGxpbmsgY29tbWFuZHMgaW4gdGhlIGNvbnRleHQgbWVudS5cbiAqXG4gKiBEaXNhYmxpbmcgdGhpcyBwbHVnaW4gd2lsbCBOT1QgZGlzYWJsZSBkb3dubG9hZGluZyBmaWxlcyBmcm9tIHRoZSBzZXJ2ZXIuXG4gKiBVc2VycyB3aWxsIHN0aWxsIGJlIGFibGUgdG8gcmV0cmlldmUgZmlsZXMgZnJvbSB0aGUgZmlsZSBkb3dubG9hZCBVUkxzIHRoZVxuICogc2VydmVyIHByb3ZpZGVzLlxuICovXG5jb25zdCBkb3dubG9hZFBsdWdpbjogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2ZpbGVicm93c2VyLWV4dGVuc2lvbjpkb3dubG9hZCcsXG4gIHJlcXVpcmVzOiBbSUZpbGVCcm93c2VyRmFjdG9yeSwgSVRyYW5zbGF0b3JdLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgZmFjdG9yeTogSUZpbGVCcm93c2VyRmFjdG9yeSxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvclxuICApOiB2b2lkID0+IHtcbiAgICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IHsgY29tbWFuZHMgfSA9IGFwcDtcbiAgICBjb25zdCB7IHRyYWNrZXIgfSA9IGZhY3Rvcnk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuZG93bmxvYWQsIHtcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuXG4gICAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgICByZXR1cm4gd2lkZ2V0LmRvd25sb2FkKCk7XG4gICAgICAgIH1cbiAgICAgIH0sXG4gICAgICBpY29uOiBkb3dubG9hZEljb24uYmluZHByb3BzKHsgc3R5bGVzaGVldDogJ21lbnVJdGVtJyB9KSxcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnRG93bmxvYWQnKVxuICAgIH0pO1xuXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmNvcHlEb3dubG9hZExpbmssIHtcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuICAgICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIHJldHVybiB3aWRnZXQubW9kZWwubWFuYWdlci5zZXJ2aWNlcy5jb250ZW50c1xuICAgICAgICAgIC5nZXREb3dubG9hZFVybCh3aWRnZXQuc2VsZWN0ZWRJdGVtcygpLm5leHQoKSEucGF0aClcbiAgICAgICAgICAudGhlbih1cmwgPT4ge1xuICAgICAgICAgICAgQ2xpcGJvYXJkLmNvcHlUb1N5c3RlbSh1cmwpO1xuICAgICAgICAgIH0pO1xuICAgICAgfSxcbiAgICAgIGljb246IGNvcHlJY29uLmJpbmRwcm9wcyh7IHN0eWxlc2hlZXQ6ICdtZW51SXRlbScgfSksXG4gICAgICBsYWJlbDogdHJhbnMuX18oJ0NvcHkgRG93bmxvYWQgTGluaycpLFxuICAgICAgbW5lbW9uaWM6IDBcbiAgICB9KTtcbiAgfVxufTtcblxuLyoqXG4gKiBBIHBsdWdpbiB0byBhZGQgdGhlIGZpbGUgYnJvd3NlciB3aWRnZXQgdG8gYW4gSUxhYlNoZWxsXG4gKi9cbmNvbnN0IGJyb3dzZXJXaWRnZXQ6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9maWxlYnJvd3Nlci1leHRlbnNpb246d2lkZ2V0JyxcbiAgcmVxdWlyZXM6IFtcbiAgICBJRG9jdW1lbnRNYW5hZ2VyLFxuICAgIElGaWxlQnJvd3NlckZhY3RvcnksXG4gICAgSVNldHRpbmdSZWdpc3RyeSxcbiAgICBJVG9vbGJhcldpZGdldFJlZ2lzdHJ5LFxuICAgIElUcmFuc2xhdG9yLFxuICAgIElMYWJTaGVsbCxcbiAgICBJRmlsZUJyb3dzZXJDb21tYW5kc1xuICBdLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgZG9jTWFuYWdlcjogSURvY3VtZW50TWFuYWdlcixcbiAgICBmYWN0b3J5OiBJRmlsZUJyb3dzZXJGYWN0b3J5LFxuICAgIHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LFxuICAgIHRvb2xiYXJSZWdpc3RyeTogSVRvb2xiYXJXaWRnZXRSZWdpc3RyeSxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcixcbiAgICBsYWJTaGVsbDogSUxhYlNoZWxsXG4gICk6IHZvaWQgPT4ge1xuICAgIGNvbnN0IHsgY29tbWFuZHMgfSA9IGFwcDtcbiAgICBjb25zdCB7IGRlZmF1bHRCcm93c2VyOiBicm93c2VyLCB0cmFja2VyIH0gPSBmYWN0b3J5O1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG5cbiAgICAvLyBTZXQgYXR0cmlidXRlcyB3aGVuIGFkZGluZyB0aGUgYnJvd3NlciB0byB0aGUgVUlcbiAgICBicm93c2VyLm5vZGUuc2V0QXR0cmlidXRlKCdyb2xlJywgJ3JlZ2lvbicpO1xuICAgIGJyb3dzZXIubm9kZS5zZXRBdHRyaWJ1dGUoJ2FyaWEtbGFiZWwnLCB0cmFucy5fXygnRmlsZSBCcm93c2VyIFNlY3Rpb24nKSk7XG4gICAgYnJvd3Nlci50aXRsZS5pY29uID0gZm9sZGVySWNvbjtcblxuICAgIC8vIFRvb2xiYXJcbiAgICB0b29sYmFyUmVnaXN0cnkuYWRkRmFjdG9yeShcbiAgICAgIEZJTEVfQlJPV1NFUl9GQUNUT1JZLFxuICAgICAgJ3VwbG9hZGVyJyxcbiAgICAgIChicm93c2VyOiBGaWxlQnJvd3NlcikgPT5cbiAgICAgICAgbmV3IFVwbG9hZGVyKHsgbW9kZWw6IGJyb3dzZXIubW9kZWwsIHRyYW5zbGF0b3IgfSlcbiAgICApO1xuXG4gICAgc2V0VG9vbGJhcihcbiAgICAgIGJyb3dzZXIsXG4gICAgICBjcmVhdGVUb29sYmFyRmFjdG9yeShcbiAgICAgICAgdG9vbGJhclJlZ2lzdHJ5LFxuICAgICAgICBzZXR0aW5ncyxcbiAgICAgICAgRklMRV9CUk9XU0VSX0ZBQ1RPUlksXG4gICAgICAgIGJyb3dzZXJXaWRnZXQuaWQsXG4gICAgICAgIHRyYW5zbGF0b3JcbiAgICAgIClcbiAgICApO1xuXG4gICAgbGFiU2hlbGwuYWRkKGJyb3dzZXIsICdsZWZ0JywgeyByYW5rOiAxMDAsIHR5cGU6ICdGaWxlIEJyb3dzZXInIH0pO1xuXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnNob3dCcm93c2VyLCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ09wZW4gdGhlIGZpbGUgYnJvd3NlciBmb3IgdGhlIHByb3ZpZGVkIGBwYXRoYC4nKSxcbiAgICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgICBjb25zdCBwYXRoID0gKGFyZ3MucGF0aCBhcyBzdHJpbmcpIHx8ICcnO1xuICAgICAgICBjb25zdCBicm93c2VyRm9yUGF0aCA9IFByaXZhdGUuZ2V0QnJvd3NlckZvclBhdGgocGF0aCwgZmFjdG9yeSk7XG5cbiAgICAgICAgLy8gQ2hlY2sgZm9yIGJyb3dzZXIgbm90IGZvdW5kXG4gICAgICAgIGlmICghYnJvd3NlckZvclBhdGgpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cbiAgICAgICAgLy8gU2hvcnRjdXQgaWYgd2UgYXJlIHVzaW5nIHRoZSBtYWluIGZpbGUgYnJvd3NlclxuICAgICAgICBpZiAoYnJvd3NlciA9PT0gYnJvd3NlckZvclBhdGgpIHtcbiAgICAgICAgICBsYWJTaGVsbC5hY3RpdmF0ZUJ5SWQoYnJvd3Nlci5pZCk7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIGNvbnN0IGFyZWFzOiBJTGFiU2hlbGwuQXJlYVtdID0gWydsZWZ0JywgJ3JpZ2h0J107XG4gICAgICAgICAgZm9yIChjb25zdCBhcmVhIG9mIGFyZWFzKSB7XG4gICAgICAgICAgICBjb25zdCBpdCA9IGxhYlNoZWxsLndpZGdldHMoYXJlYSk7XG4gICAgICAgICAgICBsZXQgd2lkZ2V0ID0gaXQubmV4dCgpO1xuICAgICAgICAgICAgd2hpbGUgKHdpZGdldCkge1xuICAgICAgICAgICAgICBpZiAod2lkZ2V0LmNvbnRhaW5zKGJyb3dzZXJGb3JQYXRoKSkge1xuICAgICAgICAgICAgICAgIGxhYlNoZWxsLmFjdGl2YXRlQnlJZCh3aWRnZXQuaWQpO1xuICAgICAgICAgICAgICAgIHJldHVybjtcbiAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICB3aWRnZXQgPSBpdC5uZXh0KCk7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgfVxuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuaGlkZUJyb3dzZXIsIHtcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnSGlkZSB0aGUgZmlsZSBicm93c2VyLicpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgICAgIGlmICh3aWRnZXQgJiYgIXdpZGdldC5pc0hpZGRlbikge1xuICAgICAgICAgIGxhYlNoZWxsLmNvbGxhcHNlTGVmdCgpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICAvLyBJZiB0aGUgbGF5b3V0IGlzIGEgZnJlc2ggc2Vzc2lvbiB3aXRob3V0IHNhdmVkIGRhdGEgYW5kIG5vdCBpbiBzaW5nbGUgZG9jdW1lbnRcbiAgICAvLyBtb2RlLCBvcGVuIGZpbGUgYnJvd3Nlci5cbiAgICB2b2lkIGxhYlNoZWxsLnJlc3RvcmVkLnRoZW4obGF5b3V0ID0+IHtcbiAgICAgIGlmIChsYXlvdXQuZnJlc2ggJiYgbGFiU2hlbGwubW9kZSAhPT0gJ3NpbmdsZS1kb2N1bWVudCcpIHtcbiAgICAgICAgdm9pZCBjb21tYW5kcy5leGVjdXRlKENvbW1hbmRJRHMuc2hvd0Jyb3dzZXIsIHZvaWQgMCk7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICB2b2lkIFByb21pc2UuYWxsKFthcHAucmVzdG9yZWQsIGJyb3dzZXIubW9kZWwucmVzdG9yZWRdKS50aGVuKCgpID0+IHtcbiAgICAgIC8vIFdoZXRoZXIgdG8gYXV0b21hdGljYWxseSBuYXZpZ2F0ZSB0byBhIGRvY3VtZW50J3MgY3VycmVudCBkaXJlY3RvcnlcbiAgICAgIGxhYlNoZWxsLmN1cnJlbnRDaGFuZ2VkLmNvbm5lY3QoYXN5bmMgKF8sIGNoYW5nZSkgPT4ge1xuICAgICAgICBpZiAoYnJvd3Nlci5uYXZpZ2F0ZVRvQ3VycmVudERpcmVjdG9yeSAmJiBjaGFuZ2UubmV3VmFsdWUpIHtcbiAgICAgICAgICBjb25zdCB7IG5ld1ZhbHVlIH0gPSBjaGFuZ2U7XG4gICAgICAgICAgY29uc3QgY29udGV4dCA9IGRvY01hbmFnZXIuY29udGV4dEZvcldpZGdldChuZXdWYWx1ZSk7XG4gICAgICAgICAgaWYgKGNvbnRleHQpIHtcbiAgICAgICAgICAgIGNvbnN0IHsgcGF0aCB9ID0gY29udGV4dDtcbiAgICAgICAgICAgIHRyeSB7XG4gICAgICAgICAgICAgIGF3YWl0IFByaXZhdGUubmF2aWdhdGVUb1BhdGgocGF0aCwgZmFjdG9yeSwgdHJhbnNsYXRvcik7XG4gICAgICAgICAgICB9IGNhdGNoIChyZWFzb24pIHtcbiAgICAgICAgICAgICAgY29uc29sZS53YXJuKFxuICAgICAgICAgICAgICAgIGAke0NvbW1hbmRJRHMuZ29Ub1BhdGh9IGZhaWxlZCB0byBvcGVuOiAke3BhdGh9YCxcbiAgICAgICAgICAgICAgICByZWFzb25cbiAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICAgIH0pO1xuICAgIH0pO1xuICB9XG59O1xuXG4vKipcbiAqIFRoZSBkZWZhdWx0IGZpbGUgYnJvd3NlciBzaGFyZS1maWxlIHBsdWdpblxuICpcbiAqIFRoaXMgZXh0ZW5zaW9uIGFkZHMgYSBcIkNvcHkgU2hhcmVhYmxlIExpbmtcIiBjb21tYW5kIHRoYXQgZ2VuZXJhdGVzIGEgY29weS1cbiAqIHBhc3RhYmxlIFVSTC4gVGhpcyB1cmwgY2FuIGJlIHVzZWQgdG8gb3BlbiBhIHBhcnRpY3VsYXIgZmlsZSBpbiBKdXB5dGVyTGFiLFxuICogaGFuZHkgZm9yIGVtYWlsaW5nIGxpbmtzIG9yIGJvb2ttYXJraW5nIGZvciByZWZlcmVuY2UuXG4gKlxuICogSWYgeW91IG5lZWQgdG8gY2hhbmdlIGhvdyB0aGlzIGxpbmsgaXMgZ2VuZXJhdGVkIChmb3IgaW5zdGFuY2UsIHRvIGNvcHkgYVxuICogL3VzZXItcmVkaXJlY3QgVVJMIGZvciBKdXB5dGVySHViKSwgZGlzYWJsZSB0aGlzIHBsdWdpbiBhbmQgcmVwbGFjZSBpdFxuICogd2l0aCBhbm90aGVyIGltcGxlbWVudGF0aW9uLlxuICovXG5jb25zdCBzaGFyZUZpbGU6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9maWxlYnJvd3Nlci1leHRlbnNpb246c2hhcmUtZmlsZScsXG4gIHJlcXVpcmVzOiBbSUZpbGVCcm93c2VyRmFjdG9yeSwgSVRyYW5zbGF0b3JdLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgZmFjdG9yeTogSUZpbGVCcm93c2VyRmFjdG9yeSxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvclxuICApOiB2b2lkID0+IHtcbiAgICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IHsgY29tbWFuZHMgfSA9IGFwcDtcbiAgICBjb25zdCB7IHRyYWNrZXIgfSA9IGZhY3Rvcnk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY29weVNoYXJlYWJsZUxpbmssIHtcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuICAgICAgICBjb25zdCBtb2RlbCA9IHdpZGdldD8uc2VsZWN0ZWRJdGVtcygpLm5leHQoKTtcbiAgICAgICAgaWYgKCFtb2RlbCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIENsaXBib2FyZC5jb3B5VG9TeXN0ZW0oXG4gICAgICAgICAgUGFnZUNvbmZpZy5nZXRVcmwoe1xuICAgICAgICAgICAgd29ya3NwYWNlOiBQYWdlQ29uZmlnLmRlZmF1bHRXb3Jrc3BhY2UsXG4gICAgICAgICAgICB0cmVlUGF0aDogbW9kZWwucGF0aCxcbiAgICAgICAgICAgIHRvU2hhcmU6IHRydWVcbiAgICAgICAgICB9KVxuICAgICAgICApO1xuICAgICAgfSxcbiAgICAgIGlzVmlzaWJsZTogKCkgPT5cbiAgICAgICAgISF0cmFja2VyLmN1cnJlbnRXaWRnZXQgJiZcbiAgICAgICAgdG9BcnJheSh0cmFja2VyLmN1cnJlbnRXaWRnZXQuc2VsZWN0ZWRJdGVtcygpKS5sZW5ndGggPT09IDEsXG4gICAgICBpY29uOiBsaW5rSWNvbi5iaW5kcHJvcHMoeyBzdHlsZXNoZWV0OiAnbWVudUl0ZW0nIH0pLFxuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdDb3B5IFNoYXJlYWJsZSBMaW5rJylcbiAgICB9KTtcbiAgfVxufTtcblxuLyoqXG4gKiBUaGUgXCJPcGVuIFdpdGhcIiBjb250ZXh0IG1lbnUuXG4gKlxuICogVGhpcyBpcyBpdHMgb3duIHBsdWdpbiBpbiBjYXNlIHlvdSB3b3VsZCBsaWtlIHRvIGRpc2FibGUgdGhpcyBmZWF0dXJlLlxuICogZS5nLiBqdXB5dGVyIGxhYmV4dGVuc2lvbiBkaXNhYmxlIEBqdXB5dGVybGFiL2ZpbGVicm93c2VyLWV4dGVuc2lvbjpvcGVuLXdpdGhcbiAqL1xuY29uc3Qgb3BlbldpdGhQbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9maWxlYnJvd3Nlci1leHRlbnNpb246b3Blbi13aXRoJyxcbiAgcmVxdWlyZXM6IFtJRmlsZUJyb3dzZXJGYWN0b3J5XSxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBhY3RpdmF0ZTogKGFwcDogSnVweXRlckZyb250RW5kLCBmYWN0b3J5OiBJRmlsZUJyb3dzZXJGYWN0b3J5KTogdm9pZCA9PiB7XG4gICAgY29uc3QgeyBkb2NSZWdpc3RyeSB9ID0gYXBwO1xuICAgIGNvbnN0IHsgdHJhY2tlciB9ID0gZmFjdG9yeTtcblxuICAgIGxldCBpdGVtczogSURpc3Bvc2FibGVNZW51SXRlbVtdID0gW107XG5cbiAgICBmdW5jdGlvbiB1cGRhdGVPcGVuV2l0aE1lbnUoY29udGV4dE1lbnU6IENvbnRleHRNZW51KSB7XG4gICAgICBjb25zdCBvcGVuV2l0aCA9XG4gICAgICAgIChjb250ZXh0TWVudS5tZW51Lml0ZW1zLmZpbmQoXG4gICAgICAgICAgaXRlbSA9PlxuICAgICAgICAgICAgaXRlbS50eXBlID09PSAnc3VibWVudScgJiZcbiAgICAgICAgICAgIGl0ZW0uc3VibWVudT8uaWQgPT09ICdqcC1jb250ZXh0bWVudS1vcGVuLXdpdGgnXG4gICAgICAgICk/LnN1Ym1lbnUgYXMgUmFua2VkTWVudSkgPz8gbnVsbDtcblxuICAgICAgaWYgKCFvcGVuV2l0aCkge1xuICAgICAgICByZXR1cm47IC8vIEJhaWwgZWFybHkgaWYgdGhlIG9wZW4gd2l0aCBtZW51IGlzIG5vdCBkaXNwbGF5ZWRcbiAgICAgIH1cblxuICAgICAgLy8gY2xlYXIgdGhlIGN1cnJlbnQgbWVudSBpdGVtc1xuICAgICAgaXRlbXMuZm9yRWFjaChpdGVtID0+IGl0ZW0uZGlzcG9zZSgpKTtcbiAgICAgIGl0ZW1zLmxlbmd0aCA9IDA7XG4gICAgICAvLyBFbnN1cmUgdGhhdCB0aGUgbWVudSBpcyBlbXB0eVxuICAgICAgb3BlbldpdGguY2xlYXJJdGVtcygpO1xuXG4gICAgICAvLyBnZXQgdGhlIHdpZGdldCBmYWN0b3JpZXMgdGhhdCBjb3VsZCBiZSB1c2VkIHRvIG9wZW4gYWxsIG9mIHRoZSBpdGVtc1xuICAgICAgLy8gaW4gdGhlIGN1cnJlbnQgZmlsZWJyb3dzZXIgc2VsZWN0aW9uXG4gICAgICBjb25zdCBmYWN0b3JpZXMgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXRcbiAgICAgICAgPyBQcml2YXRlLk9wZW5XaXRoLmludGVyc2VjdGlvbjxEb2N1bWVudFJlZ2lzdHJ5LldpZGdldEZhY3Rvcnk+KFxuICAgICAgICAgICAgbWFwKHRyYWNrZXIuY3VycmVudFdpZGdldC5zZWxlY3RlZEl0ZW1zKCksIGkgPT4ge1xuICAgICAgICAgICAgICByZXR1cm4gUHJpdmF0ZS5PcGVuV2l0aC5nZXRGYWN0b3JpZXMoZG9jUmVnaXN0cnksIGkpO1xuICAgICAgICAgICAgfSlcbiAgICAgICAgICApXG4gICAgICAgIDogbmV3IFNldDxEb2N1bWVudFJlZ2lzdHJ5LldpZGdldEZhY3Rvcnk+KCk7XG5cbiAgICAgIC8vIG1ha2UgbmV3IG1lbnUgaXRlbXMgZnJvbSB0aGUgd2lkZ2V0IGZhY3Rvcmllc1xuICAgICAgaXRlbXMgPSBbLi4uZmFjdG9yaWVzXS5tYXAoZmFjdG9yeSA9PlxuICAgICAgICBvcGVuV2l0aC5hZGRJdGVtKHtcbiAgICAgICAgICBhcmdzOiB7IGZhY3Rvcnk6IGZhY3RvcnkubmFtZSwgbGFiZWw6IGZhY3RvcnkubGFiZWwgfHwgZmFjdG9yeS5uYW1lIH0sXG4gICAgICAgICAgY29tbWFuZDogQ29tbWFuZElEcy5vcGVuXG4gICAgICAgIH0pXG4gICAgICApO1xuICAgIH1cblxuICAgIGFwcC5jb250ZXh0TWVudS5vcGVuZWQuY29ubmVjdCh1cGRhdGVPcGVuV2l0aE1lbnUpO1xuICB9XG59O1xuXG4vKipcbiAqIFRoZSBcIk9wZW4gaW4gTmV3IEJyb3dzZXIgVGFiXCIgY29udGV4dCBtZW51LlxuICpcbiAqIFRoaXMgaXMgaXRzIG93biBwbHVnaW4gaW4gY2FzZSB5b3Ugd291bGQgbGlrZSB0byBkaXNhYmxlIHRoaXMgZmVhdHVyZS5cbiAqIGUuZy4ganVweXRlciBsYWJleHRlbnNpb24gZGlzYWJsZSBAanVweXRlcmxhYi9maWxlYnJvd3Nlci1leHRlbnNpb246b3Blbi1icm93c2VyLXRhYlxuICpcbiAqIE5vdGU6IElmIGRpc2FibGluZyB0aGlzLCB5b3UgbWF5IGFsc28gd2FudCB0byBkaXNhYmxlOlxuICogQGp1cHl0ZXJsYWIvZG9jbWFuYWdlci1leHRlbnNpb246b3Blbi1icm93c2VyLXRhYlxuICovXG5jb25zdCBvcGVuQnJvd3NlclRhYlBsdWdpbjogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2ZpbGVicm93c2VyLWV4dGVuc2lvbjpvcGVuLWJyb3dzZXItdGFiJyxcbiAgcmVxdWlyZXM6IFtJRmlsZUJyb3dzZXJGYWN0b3J5LCBJVHJhbnNsYXRvcl0sXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICBmYWN0b3J5OiBJRmlsZUJyb3dzZXJGYWN0b3J5LFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yXG4gICk6IHZvaWQgPT4ge1xuICAgIGNvbnN0IHsgY29tbWFuZHMgfSA9IGFwcDtcbiAgICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IHsgdHJhY2tlciB9ID0gZmFjdG9yeTtcblxuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5vcGVuQnJvd3NlclRhYiwge1xuICAgICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldDtcblxuICAgICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIGNvbnN0IG1vZGUgPSBhcmdzWydtb2RlJ10gYXMgc3RyaW5nIHwgdW5kZWZpbmVkO1xuXG4gICAgICAgIHJldHVybiBQcm9taXNlLmFsbChcbiAgICAgICAgICB0b0FycmF5KFxuICAgICAgICAgICAgbWFwKHdpZGdldC5zZWxlY3RlZEl0ZW1zKCksIGl0ZW0gPT4ge1xuICAgICAgICAgICAgICBpZiAobW9kZSA9PT0gJ3NpbmdsZS1kb2N1bWVudCcpIHtcbiAgICAgICAgICAgICAgICBjb25zdCB1cmwgPSBQYWdlQ29uZmlnLmdldFVybCh7XG4gICAgICAgICAgICAgICAgICBtb2RlOiAnc2luZ2xlLWRvY3VtZW50JyxcbiAgICAgICAgICAgICAgICAgIHRyZWVQYXRoOiBpdGVtLnBhdGhcbiAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICBjb25zdCBvcGVuZWQgPSB3aW5kb3cub3BlbigpO1xuICAgICAgICAgICAgICAgIGlmIChvcGVuZWQpIHtcbiAgICAgICAgICAgICAgICAgIG9wZW5lZC5vcGVuZXIgPSBudWxsO1xuICAgICAgICAgICAgICAgICAgb3BlbmVkLmxvY2F0aW9uLmhyZWYgPSB1cmw7XG4gICAgICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICAgIHRocm93IG5ldyBFcnJvcignRmFpbGVkIHRvIG9wZW4gbmV3IGJyb3dzZXIgdGFiLicpO1xuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICByZXR1cm4gY29tbWFuZHMuZXhlY3V0ZSgnZG9jbWFuYWdlcjpvcGVuLWJyb3dzZXItdGFiJywge1xuICAgICAgICAgICAgICAgICAgcGF0aDogaXRlbS5wYXRoXG4gICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH0pXG4gICAgICAgICAgKVxuICAgICAgICApO1xuICAgICAgfSxcbiAgICAgIGljb246IGFkZEljb24uYmluZHByb3BzKHsgc3R5bGVzaGVldDogJ21lbnVJdGVtJyB9KSxcbiAgICAgIGxhYmVsOiBhcmdzID0+XG4gICAgICAgIGFyZ3NbJ21vZGUnXSA9PT0gJ3NpbmdsZS1kb2N1bWVudCdcbiAgICAgICAgICA/IHRyYW5zLl9fKCdPcGVuIGluIFNpbXBsZSBNb2RlJylcbiAgICAgICAgICA6IHRyYW5zLl9fKCdPcGVuIGluIE5ldyBCcm93c2VyIFRhYicpLFxuICAgICAgbW5lbW9uaWM6IDBcbiAgICB9KTtcbiAgfVxufTtcblxuLyoqXG4gKiBBIHBsdWdpbiBwcm92aWRpbmcgZmlsZSB1cGxvYWQgc3RhdHVzLlxuICovXG5leHBvcnQgY29uc3QgZmlsZVVwbG9hZFN0YXR1czogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2ZpbGVicm93c2VyLWV4dGVuc2lvbjpmaWxlLXVwbG9hZC1zdGF0dXMnLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHJlcXVpcmVzOiBbSUZpbGVCcm93c2VyRmFjdG9yeSwgSVRyYW5zbGF0b3JdLFxuICBvcHRpb25hbDogW0lTdGF0dXNCYXJdLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIGJyb3dzZXI6IElGaWxlQnJvd3NlckZhY3RvcnksXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gICAgc3RhdHVzQmFyOiBJU3RhdHVzQmFyIHwgbnVsbFxuICApID0+IHtcbiAgICBpZiAoIXN0YXR1c0Jhcikge1xuICAgICAgLy8gQXV0b21hdGljYWxseSBkaXNhYmxlIGlmIHN0YXR1c2JhciBtaXNzaW5nXG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbnN0IGl0ZW0gPSBuZXcgRmlsZVVwbG9hZFN0YXR1cyh7XG4gICAgICB0cmFja2VyOiBicm93c2VyLnRyYWNrZXIsXG4gICAgICB0cmFuc2xhdG9yXG4gICAgfSk7XG5cbiAgICBzdGF0dXNCYXIucmVnaXN0ZXJTdGF0dXNJdGVtKFxuICAgICAgJ0BqdXB5dGVybGFiL2ZpbGVicm93c2VyLWV4dGVuc2lvbjpmaWxlLXVwbG9hZC1zdGF0dXMnLFxuICAgICAge1xuICAgICAgICBpdGVtLFxuICAgICAgICBhbGlnbjogJ21pZGRsZScsXG4gICAgICAgIGlzQWN0aXZlOiAoKSA9PiB7XG4gICAgICAgICAgcmV0dXJuICEhaXRlbS5tb2RlbCAmJiBpdGVtLm1vZGVsLml0ZW1zLmxlbmd0aCA+IDA7XG4gICAgICAgIH0sXG4gICAgICAgIGFjdGl2ZVN0YXRlQ2hhbmdlZDogaXRlbS5tb2RlbC5zdGF0ZUNoYW5nZWRcbiAgICAgIH1cbiAgICApO1xuICB9XG59O1xuXG4vKipcbiAqIEEgcGx1Z2luIHRvIG9wZW4gZmlsZXMgZnJvbSByZW1vdGUgVVJMc1xuICovXG5jb25zdCBvcGVuVXJsUGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvZmlsZWJyb3dzZXItZXh0ZW5zaW9uOm9wZW4tdXJsJyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICByZXF1aXJlczogW0lGaWxlQnJvd3NlckZhY3RvcnksIElUcmFuc2xhdG9yXSxcbiAgb3B0aW9uYWw6IFtJQ29tbWFuZFBhbGV0dGVdLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIGZhY3Rvcnk6IElGaWxlQnJvd3NlckZhY3RvcnksXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gICAgcGFsZXR0ZTogSUNvbW1hbmRQYWxldHRlIHwgbnVsbFxuICApID0+IHtcbiAgICBjb25zdCB7IGNvbW1hbmRzIH0gPSBhcHA7XG4gICAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICBjb25zdCB7IGRlZmF1bHRCcm93c2VyOiBicm93c2VyIH0gPSBmYWN0b3J5O1xuICAgIGNvbnN0IGNvbW1hbmQgPSBDb21tYW5kSURzLm9wZW5Vcmw7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKGNvbW1hbmQsIHtcbiAgICAgIGxhYmVsOiBhcmdzID0+XG4gICAgICAgIGFyZ3MudXJsID8gdHJhbnMuX18oJ09wZW4gJTEnLCBhcmdzLnVybCkgOiB0cmFucy5fXygnT3BlbiBmcm9tIFVSTOKApicpLFxuICAgICAgY2FwdGlvbjogYXJncyA9PlxuICAgICAgICBhcmdzLnVybCA/IHRyYW5zLl9fKCdPcGVuICUxJywgYXJncy51cmwpIDogdHJhbnMuX18oJ09wZW4gZnJvbSBVUkwnKSxcbiAgICAgIGV4ZWN1dGU6IGFzeW5jIGFyZ3MgPT4ge1xuICAgICAgICBsZXQgdXJsOiBzdHJpbmcgfCB1bmRlZmluZWQgPSAoYXJncz8udXJsIGFzIHN0cmluZykgPz8gJyc7XG4gICAgICAgIGlmICghdXJsKSB7XG4gICAgICAgICAgdXJsID1cbiAgICAgICAgICAgIChcbiAgICAgICAgICAgICAgYXdhaXQgSW5wdXREaWFsb2cuZ2V0VGV4dCh7XG4gICAgICAgICAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdVUkwnKSxcbiAgICAgICAgICAgICAgICBwbGFjZWhvbGRlcjogJ2h0dHBzOi8vZXhhbXBsZS5jb20vcGF0aC90by9maWxlJyxcbiAgICAgICAgICAgICAgICB0aXRsZTogdHJhbnMuX18oJ09wZW4gVVJMJyksXG4gICAgICAgICAgICAgICAgb2tMYWJlbDogdHJhbnMuX18oJ09wZW4nKVxuICAgICAgICAgICAgICB9KVxuICAgICAgICAgICAgKS52YWx1ZSA/PyB1bmRlZmluZWQ7XG4gICAgICAgIH1cbiAgICAgICAgaWYgKCF1cmwpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cblxuICAgICAgICBsZXQgdHlwZSA9ICcnO1xuICAgICAgICBsZXQgYmxvYjtcblxuICAgICAgICAvLyBmZXRjaCB0aGUgZmlsZSBmcm9tIHRoZSBVUkxcbiAgICAgICAgdHJ5IHtcbiAgICAgICAgICBjb25zdCByZXEgPSBhd2FpdCBmZXRjaCh1cmwpO1xuICAgICAgICAgIGJsb2IgPSBhd2FpdCByZXEuYmxvYigpO1xuICAgICAgICAgIHR5cGUgPSByZXEuaGVhZGVycy5nZXQoJ0NvbnRlbnQtVHlwZScpID8/ICcnO1xuICAgICAgICB9IGNhdGNoIChyZWFzb24pIHtcbiAgICAgICAgICBpZiAocmVhc29uLnJlc3BvbnNlICYmIHJlYXNvbi5yZXNwb25zZS5zdGF0dXMgIT09IDIwMCkge1xuICAgICAgICAgICAgcmVhc29uLm1lc3NhZ2UgPSB0cmFucy5fXygnQ291bGQgbm90IG9wZW4gVVJMOiAlMScsIHVybCk7XG4gICAgICAgICAgfVxuICAgICAgICAgIHJldHVybiBzaG93RXJyb3JNZXNzYWdlKHRyYW5zLl9fKCdDYW5ub3QgZmV0Y2gnKSwgcmVhc29uKTtcbiAgICAgICAgfVxuXG4gICAgICAgIC8vIHVwbG9hZCB0aGUgY29udGVudCBvZiB0aGUgZmlsZSB0byB0aGUgc2VydmVyXG4gICAgICAgIHRyeSB7XG4gICAgICAgICAgY29uc3QgbmFtZSA9IFBhdGhFeHQuYmFzZW5hbWUodXJsKTtcbiAgICAgICAgICBjb25zdCBmaWxlID0gbmV3IEZpbGUoW2Jsb2JdLCBuYW1lLCB7IHR5cGUgfSk7XG4gICAgICAgICAgY29uc3QgbW9kZWwgPSBhd2FpdCBicm93c2VyLm1vZGVsLnVwbG9hZChmaWxlKTtcbiAgICAgICAgICByZXR1cm4gY29tbWFuZHMuZXhlY3V0ZSgnZG9jbWFuYWdlcjpvcGVuJywge1xuICAgICAgICAgICAgcGF0aDogbW9kZWwucGF0aFxuICAgICAgICAgIH0pO1xuICAgICAgICB9IGNhdGNoIChlcnJvcikge1xuICAgICAgICAgIHJldHVybiBzaG93RXJyb3JNZXNzYWdlKFxuICAgICAgICAgICAgdHJhbnMuX3AoJ3Nob3dFcnJvck1lc3NhZ2UnLCAnVXBsb2FkIEVycm9yJyksXG4gICAgICAgICAgICBlcnJvclxuICAgICAgICAgICk7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9KTtcblxuICAgIGlmIChwYWxldHRlKSB7XG4gICAgICBwYWxldHRlLmFkZEl0ZW0oe1xuICAgICAgICBjb21tYW5kLFxuICAgICAgICBjYXRlZ29yeTogdHJhbnMuX18oJ0ZpbGUgT3BlcmF0aW9ucycpXG4gICAgICB9KTtcbiAgICB9XG4gIH1cbn07XG5cbi8qKlxuICogQWRkIHRoZSBtYWluIGZpbGUgYnJvd3NlciBjb21tYW5kcyB0byB0aGUgYXBwbGljYXRpb24ncyBjb21tYW5kIHJlZ2lzdHJ5LlxuICovXG5mdW5jdGlvbiBhZGRDb21tYW5kcyhcbiAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gIGZhY3Rvcnk6IElGaWxlQnJvd3NlckZhY3RvcnksXG4gIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICBzZXR0aW5nUmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnkgfCBudWxsLFxuICBjb21tYW5kUGFsZXR0ZTogSUNvbW1hbmRQYWxldHRlIHwgbnVsbFxuKTogdm9pZCB7XG4gIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gIGNvbnN0IHsgZG9jUmVnaXN0cnk6IHJlZ2lzdHJ5LCBjb21tYW5kcyB9ID0gYXBwO1xuICBjb25zdCB7IGRlZmF1bHRCcm93c2VyOiBicm93c2VyLCB0cmFja2VyIH0gPSBmYWN0b3J5O1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5kZWwsIHtcbiAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG5cbiAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgcmV0dXJuIHdpZGdldC5kZWxldGUoKTtcbiAgICAgIH1cbiAgICB9LFxuICAgIGljb246IGNsb3NlSWNvbi5iaW5kcHJvcHMoeyBzdHlsZXNoZWV0OiAnbWVudUl0ZW0nIH0pLFxuICAgIGxhYmVsOiB0cmFucy5fXygnRGVsZXRlJyksXG4gICAgbW5lbW9uaWM6IDBcbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmNvcHksIHtcbiAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG5cbiAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgcmV0dXJuIHdpZGdldC5jb3B5KCk7XG4gICAgICB9XG4gICAgfSxcbiAgICBpY29uOiBjb3B5SWNvbi5iaW5kcHJvcHMoeyBzdHlsZXNoZWV0OiAnbWVudUl0ZW0nIH0pLFxuICAgIGxhYmVsOiB0cmFucy5fXygnQ29weScpLFxuICAgIG1uZW1vbmljOiAwXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5jdXQsIHtcbiAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG5cbiAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgcmV0dXJuIHdpZGdldC5jdXQoKTtcbiAgICAgIH1cbiAgICB9LFxuICAgIGljb246IGN1dEljb24uYmluZHByb3BzKHsgc3R5bGVzaGVldDogJ21lbnVJdGVtJyB9KSxcbiAgICBsYWJlbDogdHJhbnMuX18oJ0N1dCcpXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5kdXBsaWNhdGUsIHtcbiAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG5cbiAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgcmV0dXJuIHdpZGdldC5kdXBsaWNhdGUoKTtcbiAgICAgIH1cbiAgICB9LFxuICAgIGljb246IGNvcHlJY29uLmJpbmRwcm9wcyh7IHN0eWxlc2hlZXQ6ICdtZW51SXRlbScgfSksXG4gICAgbGFiZWw6IHRyYW5zLl9fKCdEdXBsaWNhdGUnKVxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuZ29Ub1BhdGgsIHtcbiAgICBsYWJlbDogdHJhbnMuX18oJ1VwZGF0ZSB0aGUgZmlsZSBicm93c2VyIHRvIGRpc3BsYXkgdGhlIHByb3ZpZGVkIGBwYXRoYC4nKSxcbiAgICBleGVjdXRlOiBhc3luYyBhcmdzID0+IHtcbiAgICAgIGNvbnN0IHBhdGggPSAoYXJncy5wYXRoIGFzIHN0cmluZykgfHwgJyc7XG4gICAgICBjb25zdCBzaG93QnJvd3NlciA9ICEoYXJncz8uZG9udFNob3dCcm93c2VyID8/IGZhbHNlKTtcbiAgICAgIHRyeSB7XG4gICAgICAgIGNvbnN0IGl0ZW0gPSBhd2FpdCBQcml2YXRlLm5hdmlnYXRlVG9QYXRoKHBhdGgsIGZhY3RvcnksIHRyYW5zbGF0b3IpO1xuICAgICAgICBpZiAoaXRlbS50eXBlICE9PSAnZGlyZWN0b3J5JyAmJiBzaG93QnJvd3Nlcikge1xuICAgICAgICAgIGNvbnN0IGJyb3dzZXJGb3JQYXRoID0gUHJpdmF0ZS5nZXRCcm93c2VyRm9yUGF0aChwYXRoLCBmYWN0b3J5KTtcbiAgICAgICAgICBpZiAoYnJvd3NlckZvclBhdGgpIHtcbiAgICAgICAgICAgIGJyb3dzZXJGb3JQYXRoLmNsZWFyU2VsZWN0ZWRJdGVtcygpO1xuICAgICAgICAgICAgY29uc3QgcGFydHMgPSBwYXRoLnNwbGl0KCcvJyk7XG4gICAgICAgICAgICBjb25zdCBuYW1lID0gcGFydHNbcGFydHMubGVuZ3RoIC0gMV07XG4gICAgICAgICAgICBpZiAobmFtZSkge1xuICAgICAgICAgICAgICBhd2FpdCBicm93c2VyRm9yUGF0aC5zZWxlY3RJdGVtQnlOYW1lKG5hbWUpO1xuICAgICAgICAgICAgfVxuICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgfSBjYXRjaCAocmVhc29uKSB7XG4gICAgICAgIGNvbnNvbGUud2FybihgJHtDb21tYW5kSURzLmdvVG9QYXRofSBmYWlsZWQgdG8gZ28gdG86ICR7cGF0aH1gLCByZWFzb24pO1xuICAgICAgfVxuICAgICAgaWYgKHNob3dCcm93c2VyKSB7XG4gICAgICAgIHJldHVybiBjb21tYW5kcy5leGVjdXRlKENvbW1hbmRJRHMuc2hvd0Jyb3dzZXIsIHsgcGF0aCB9KTtcbiAgICAgIH1cbiAgICB9XG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5nb1VwLCB7XG4gICAgbGFiZWw6ICdnbyB1cCcsXG4gICAgZXhlY3V0ZTogYXN5bmMgKCkgPT4ge1xuICAgICAgY29uc3QgYnJvd3NlckZvclBhdGggPSBQcml2YXRlLmdldEJyb3dzZXJGb3JQYXRoKCcnLCBmYWN0b3J5KTtcbiAgICAgIGlmICghYnJvd3NlckZvclBhdGgpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgY29uc3QgeyBtb2RlbCB9ID0gYnJvd3NlckZvclBhdGg7XG5cbiAgICAgIGF3YWl0IG1vZGVsLnJlc3RvcmVkO1xuICAgICAgaWYgKG1vZGVsLnBhdGggPT09IG1vZGVsLnJvb3RQYXRoKSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIHRyeSB7XG4gICAgICAgIGF3YWl0IG1vZGVsLmNkKCcuLicpO1xuICAgICAgfSBjYXRjaCAocmVhc29uKSB7XG4gICAgICAgIGNvbnNvbGUud2FybihcbiAgICAgICAgICBgJHtDb21tYW5kSURzLmdvVXB9IGZhaWxlZCB0byBnbyB0byBwYXJlbnQgZGlyZWN0b3J5IG9mICR7bW9kZWwucGF0aH1gLFxuICAgICAgICAgIHJlYXNvblxuICAgICAgICApO1xuICAgICAgfVxuICAgIH1cbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLm9wZW5QYXRoLCB7XG4gICAgbGFiZWw6IGFyZ3MgPT5cbiAgICAgIGFyZ3MucGF0aCA/IHRyYW5zLl9fKCdPcGVuICUxJywgYXJncy5wYXRoKSA6IHRyYW5zLl9fKCdPcGVuIGZyb20gUGF0aOKApicpLFxuICAgIGNhcHRpb246IGFyZ3MgPT5cbiAgICAgIGFyZ3MucGF0aCA/IHRyYW5zLl9fKCdPcGVuICUxJywgYXJncy5wYXRoKSA6IHRyYW5zLl9fKCdPcGVuIGZyb20gcGF0aCcpLFxuICAgIGV4ZWN1dGU6IGFzeW5jIGFyZ3MgPT4ge1xuICAgICAgbGV0IHBhdGg6IHN0cmluZyB8IHVuZGVmaW5lZDtcbiAgICAgIGlmIChhcmdzPy5wYXRoKSB7XG4gICAgICAgIHBhdGggPSBhcmdzLnBhdGggYXMgc3RyaW5nO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgcGF0aCA9XG4gICAgICAgICAgKFxuICAgICAgICAgICAgYXdhaXQgSW5wdXREaWFsb2cuZ2V0VGV4dCh7XG4gICAgICAgICAgICAgIGxhYmVsOiB0cmFucy5fXygnUGF0aCcpLFxuICAgICAgICAgICAgICBwbGFjZWhvbGRlcjogJy9wYXRoL3JlbGF0aXZlL3RvL2psYWIvcm9vdCcsXG4gICAgICAgICAgICAgIHRpdGxlOiB0cmFucy5fXygnT3BlbiBQYXRoJyksXG4gICAgICAgICAgICAgIG9rTGFiZWw6IHRyYW5zLl9fKCdPcGVuJylcbiAgICAgICAgICAgIH0pXG4gICAgICAgICAgKS52YWx1ZSA/PyB1bmRlZmluZWQ7XG4gICAgICB9XG4gICAgICBpZiAoIXBhdGgpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgdHJ5IHtcbiAgICAgICAgY29uc3QgdHJhaWxpbmdTbGFzaCA9IHBhdGggIT09ICcvJyAmJiBwYXRoLmVuZHNXaXRoKCcvJyk7XG4gICAgICAgIGlmICh0cmFpbGluZ1NsYXNoKSB7XG4gICAgICAgICAgLy8gVGhlIG5vcm1hbCBjb250ZW50cyBzZXJ2aWNlIGVycm9ycyBvbiBwYXRocyBlbmRpbmcgaW4gc2xhc2hcbiAgICAgICAgICBwYXRoID0gcGF0aC5zbGljZSgwLCBwYXRoLmxlbmd0aCAtIDEpO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IGJyb3dzZXJGb3JQYXRoID0gUHJpdmF0ZS5nZXRCcm93c2VyRm9yUGF0aChwYXRoLCBmYWN0b3J5KSE7XG4gICAgICAgIGNvbnN0IHsgc2VydmljZXMgfSA9IGJyb3dzZXJGb3JQYXRoLm1vZGVsLm1hbmFnZXI7XG4gICAgICAgIGNvbnN0IGl0ZW0gPSBhd2FpdCBzZXJ2aWNlcy5jb250ZW50cy5nZXQocGF0aCwge1xuICAgICAgICAgIGNvbnRlbnQ6IGZhbHNlXG4gICAgICAgIH0pO1xuICAgICAgICBpZiAodHJhaWxpbmdTbGFzaCAmJiBpdGVtLnR5cGUgIT09ICdkaXJlY3RvcnknKSB7XG4gICAgICAgICAgdGhyb3cgbmV3IEVycm9yKGBQYXRoICR7cGF0aH0vIGlzIG5vdCBhIGRpcmVjdG9yeWApO1xuICAgICAgICB9XG4gICAgICAgIGF3YWl0IGNvbW1hbmRzLmV4ZWN1dGUoQ29tbWFuZElEcy5nb1RvUGF0aCwge1xuICAgICAgICAgIHBhdGgsXG4gICAgICAgICAgZG9udFNob3dCcm93c2VyOiBhcmdzLmRvbnRTaG93QnJvd3NlclxuICAgICAgICB9KTtcbiAgICAgICAgaWYgKGl0ZW0udHlwZSA9PT0gJ2RpcmVjdG9yeScpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIGNvbW1hbmRzLmV4ZWN1dGUoJ2RvY21hbmFnZXI6b3BlbicsIHsgcGF0aCB9KTtcbiAgICAgIH0gY2F0Y2ggKHJlYXNvbikge1xuICAgICAgICBpZiAocmVhc29uLnJlc3BvbnNlICYmIHJlYXNvbi5yZXNwb25zZS5zdGF0dXMgPT09IDQwNCkge1xuICAgICAgICAgIHJlYXNvbi5tZXNzYWdlID0gdHJhbnMuX18oJ0NvdWxkIG5vdCBmaW5kIHBhdGg6ICUxJywgcGF0aCk7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIHNob3dFcnJvck1lc3NhZ2UodHJhbnMuX18oJ0Nhbm5vdCBvcGVuJyksIHJlYXNvbik7XG4gICAgICB9XG4gICAgfVxuICB9KTtcblxuICAvLyBBZGQgdGhlIG9wZW5QYXRoIGNvbW1hbmQgdG8gdGhlIGNvbW1hbmQgcGFsZXR0ZVxuICBpZiAoY29tbWFuZFBhbGV0dGUpIHtcbiAgICBjb21tYW5kUGFsZXR0ZS5hZGRJdGVtKHtcbiAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMub3BlblBhdGgsXG4gICAgICBjYXRlZ29yeTogdHJhbnMuX18oJ0ZpbGUgT3BlcmF0aW9ucycpXG4gICAgfSk7XG4gIH1cblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMub3Blbiwge1xuICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgY29uc3QgZmFjdG9yeSA9IChhcmdzWydmYWN0b3J5J10gYXMgc3RyaW5nKSB8fCB2b2lkIDA7XG4gICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG5cbiAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cblxuICAgICAgY29uc3QgeyBjb250ZW50cyB9ID0gd2lkZ2V0Lm1vZGVsLm1hbmFnZXIuc2VydmljZXM7XG4gICAgICByZXR1cm4gUHJvbWlzZS5hbGwoXG4gICAgICAgIHRvQXJyYXkoXG4gICAgICAgICAgbWFwKHdpZGdldC5zZWxlY3RlZEl0ZW1zKCksIGl0ZW0gPT4ge1xuICAgICAgICAgICAgaWYgKGl0ZW0udHlwZSA9PT0gJ2RpcmVjdG9yeScpIHtcbiAgICAgICAgICAgICAgY29uc3QgbG9jYWxQYXRoID0gY29udGVudHMubG9jYWxQYXRoKGl0ZW0ucGF0aCk7XG4gICAgICAgICAgICAgIHJldHVybiB3aWRnZXQubW9kZWwuY2QoYC8ke2xvY2FsUGF0aH1gKTtcbiAgICAgICAgICAgIH1cblxuICAgICAgICAgICAgcmV0dXJuIGNvbW1hbmRzLmV4ZWN1dGUoJ2RvY21hbmFnZXI6b3BlbicsIHtcbiAgICAgICAgICAgICAgZmFjdG9yeTogZmFjdG9yeSxcbiAgICAgICAgICAgICAgcGF0aDogaXRlbS5wYXRoXG4gICAgICAgICAgICB9KTtcbiAgICAgICAgICB9KVxuICAgICAgICApXG4gICAgICApO1xuICAgIH0sXG4gICAgaWNvbjogYXJncyA9PiB7XG4gICAgICBjb25zdCBmYWN0b3J5ID0gKGFyZ3NbJ2ZhY3RvcnknXSBhcyBzdHJpbmcpIHx8IHZvaWQgMDtcbiAgICAgIGlmIChmYWN0b3J5KSB7XG4gICAgICAgIC8vIGlmIGFuIGV4cGxpY2l0IGZhY3RvcnkgaXMgcGFzc2VkLi4uXG4gICAgICAgIGNvbnN0IGZ0ID0gcmVnaXN0cnkuZ2V0RmlsZVR5cGUoZmFjdG9yeSk7XG4gICAgICAgIC8vIC4uLnNldCBhbiBpY29uIGlmIHRoZSBmYWN0b3J5IG5hbWUgY29ycmVzcG9uZHMgdG8gYSBmaWxlIHR5cGUgbmFtZS4uLlxuICAgICAgICAvLyAuLi5vciBsZWF2ZSB0aGUgaWNvbiBibGFua1xuICAgICAgICByZXR1cm4gZnQ/Lmljb24/LmJpbmRwcm9wcyh7IHN0eWxlc2hlZXQ6ICdtZW51SXRlbScgfSk7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICByZXR1cm4gZm9sZGVySWNvbi5iaW5kcHJvcHMoeyBzdHlsZXNoZWV0OiAnbWVudUl0ZW0nIH0pO1xuICAgICAgfVxuICAgIH0sXG4gICAgbGFiZWw6IGFyZ3MgPT5cbiAgICAgIChhcmdzWydsYWJlbCddIHx8IGFyZ3NbJ2ZhY3RvcnknXSB8fCB0cmFucy5fXygnT3BlbicpKSBhcyBzdHJpbmcsXG4gICAgbW5lbW9uaWM6IDBcbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnBhc3RlLCB7XG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuXG4gICAgICBpZiAod2lkZ2V0KSB7XG4gICAgICAgIHJldHVybiB3aWRnZXQucGFzdGUoKTtcbiAgICAgIH1cbiAgICB9LFxuICAgIGljb246IHBhc3RlSWNvbi5iaW5kcHJvcHMoeyBzdHlsZXNoZWV0OiAnbWVudUl0ZW0nIH0pLFxuICAgIGxhYmVsOiB0cmFucy5fXygnUGFzdGUnKSxcbiAgICBtbmVtb25pYzogMFxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY3JlYXRlTmV3RGlyZWN0b3J5LCB7XG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuXG4gICAgICBpZiAod2lkZ2V0KSB7XG4gICAgICAgIHJldHVybiB3aWRnZXQuY3JlYXRlTmV3RGlyZWN0b3J5KCk7XG4gICAgICB9XG4gICAgfSxcbiAgICBpY29uOiBuZXdGb2xkZXJJY29uLmJpbmRwcm9wcyh7IHN0eWxlc2hlZXQ6ICdtZW51SXRlbScgfSksXG4gICAgbGFiZWw6IHRyYW5zLl9fKCdOZXcgRm9sZGVyJylcbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmNyZWF0ZU5ld0ZpbGUsIHtcbiAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG5cbiAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgcmV0dXJuIHdpZGdldC5jcmVhdGVOZXdGaWxlKHsgZXh0OiAndHh0JyB9KTtcbiAgICAgIH1cbiAgICB9LFxuICAgIGljb246IHRleHRFZGl0b3JJY29uLmJpbmRwcm9wcyh7IHN0eWxlc2hlZXQ6ICdtZW51SXRlbScgfSksXG4gICAgbGFiZWw6IHRyYW5zLl9fKCdOZXcgRmlsZScpXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5jcmVhdGVOZXdNYXJrZG93bkZpbGUsIHtcbiAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG5cbiAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgcmV0dXJuIHdpZGdldC5jcmVhdGVOZXdGaWxlKHsgZXh0OiAnbWQnIH0pO1xuICAgICAgfVxuICAgIH0sXG4gICAgaWNvbjogbWFya2Rvd25JY29uLmJpbmRwcm9wcyh7IHN0eWxlc2hlZXQ6ICdtZW51SXRlbScgfSksXG4gICAgbGFiZWw6IHRyYW5zLl9fKCdOZXcgTWFya2Rvd24gRmlsZScpXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5yZWZyZXNoLCB7XG4gICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG5cbiAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgcmV0dXJuIHdpZGdldC5tb2RlbC5yZWZyZXNoKCk7XG4gICAgICB9XG4gICAgfSxcbiAgICBpY29uOiByZWZyZXNoSWNvbi5iaW5kcHJvcHMoeyBzdHlsZXNoZWV0OiAnbWVudUl0ZW0nIH0pLFxuICAgIGNhcHRpb246IHRyYW5zLl9fKCdSZWZyZXNoIHRoZSBmaWxlIGJyb3dzZXIuJyksXG4gICAgbGFiZWw6IHRyYW5zLl9fKCdSZWZyZXNoIEZpbGUgTGlzdCcpXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5yZW5hbWUsIHtcbiAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldDtcblxuICAgICAgaWYgKHdpZGdldCkge1xuICAgICAgICByZXR1cm4gd2lkZ2V0LnJlbmFtZSgpO1xuICAgICAgfVxuICAgIH0sXG4gICAgaWNvbjogZWRpdEljb24uYmluZHByb3BzKHsgc3R5bGVzaGVldDogJ21lbnVJdGVtJyB9KSxcbiAgICBsYWJlbDogdHJhbnMuX18oJ1JlbmFtZScpLFxuICAgIG1uZW1vbmljOiAwXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5jb3B5UGF0aCwge1xuICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldDtcbiAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGNvbnN0IGl0ZW0gPSB3aWRnZXQuc2VsZWN0ZWRJdGVtcygpLm5leHQoKTtcbiAgICAgIGlmICghaXRlbSkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG5cbiAgICAgIENsaXBib2FyZC5jb3B5VG9TeXN0ZW0oaXRlbS5wYXRoKTtcbiAgICB9LFxuICAgIGlzVmlzaWJsZTogKCkgPT5cbiAgICAgICEhdHJhY2tlci5jdXJyZW50V2lkZ2V0ICYmXG4gICAgICB0cmFja2VyLmN1cnJlbnRXaWRnZXQuc2VsZWN0ZWRJdGVtcygpLm5leHQgIT09IHVuZGVmaW5lZCxcbiAgICBpY29uOiBmaWxlSWNvbi5iaW5kcHJvcHMoeyBzdHlsZXNoZWV0OiAnbWVudUl0ZW0nIH0pLFxuICAgIGxhYmVsOiB0cmFucy5fXygnQ29weSBQYXRoJylcbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnNodXRkb3duLCB7XG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuXG4gICAgICBpZiAod2lkZ2V0KSB7XG4gICAgICAgIHJldHVybiB3aWRnZXQuc2h1dGRvd25LZXJuZWxzKCk7XG4gICAgICB9XG4gICAgfSxcbiAgICBpY29uOiBzdG9wSWNvbi5iaW5kcHJvcHMoeyBzdHlsZXNoZWV0OiAnbWVudUl0ZW0nIH0pLFxuICAgIGxhYmVsOiB0cmFucy5fXygnU2h1dCBEb3duIEtlcm5lbCcpXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy50b2dnbGVCcm93c2VyLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdGaWxlIEJyb3dzZXInKSxcbiAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICBpZiAoYnJvd3Nlci5pc0hpZGRlbikge1xuICAgICAgICByZXR1cm4gY29tbWFuZHMuZXhlY3V0ZShDb21tYW5kSURzLnNob3dCcm93c2VyLCB2b2lkIDApO1xuICAgICAgfVxuXG4gICAgICByZXR1cm4gY29tbWFuZHMuZXhlY3V0ZShDb21tYW5kSURzLmhpZGVCcm93c2VyLCB2b2lkIDApO1xuICAgIH1cbiAgfSk7XG5cbiAgaWYgKHNldHRpbmdSZWdpc3RyeSkge1xuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy50b2dnbGVOYXZpZ2F0ZVRvQ3VycmVudERpcmVjdG9yeSwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdTaG93IEFjdGl2ZSBGaWxlIGluIEZpbGUgQnJvd3NlcicpLFxuICAgICAgaXNUb2dnbGVkOiAoKSA9PiBicm93c2VyLm5hdmlnYXRlVG9DdXJyZW50RGlyZWN0b3J5LFxuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICBjb25zdCB2YWx1ZSA9ICFicm93c2VyLm5hdmlnYXRlVG9DdXJyZW50RGlyZWN0b3J5O1xuICAgICAgICBjb25zdCBrZXkgPSAnbmF2aWdhdGVUb0N1cnJlbnREaXJlY3RvcnknO1xuICAgICAgICByZXR1cm4gc2V0dGluZ1JlZ2lzdHJ5XG4gICAgICAgICAgLnNldChGSUxFX0JST1dTRVJfUExVR0lOX0lELCBrZXksIHZhbHVlKVxuICAgICAgICAgIC5jYXRjaCgocmVhc29uOiBFcnJvcikgPT4ge1xuICAgICAgICAgICAgY29uc29sZS5lcnJvcihgRmFpbGVkIHRvIHNldCBuYXZpZ2F0ZVRvQ3VycmVudERpcmVjdG9yeSBzZXR0aW5nYCk7XG4gICAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfSk7XG4gIH1cblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMudG9nZ2xlTGFzdE1vZGlmaWVkLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdTaG93IExhc3QgTW9kaWZpZWQgQ29sdW1uJyksXG4gICAgaXNUb2dnbGVkOiAoKSA9PiBicm93c2VyLnNob3dMYXN0TW9kaWZpZWRDb2x1bW4sXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgY29uc3QgdmFsdWUgPSAhYnJvd3Nlci5zaG93TGFzdE1vZGlmaWVkQ29sdW1uO1xuICAgICAgY29uc3Qga2V5ID0gJ3Nob3dMYXN0TW9kaWZpZWRDb2x1bW4nO1xuICAgICAgaWYgKHNldHRpbmdSZWdpc3RyeSkge1xuICAgICAgICByZXR1cm4gc2V0dGluZ1JlZ2lzdHJ5XG4gICAgICAgICAgLnNldChGSUxFX0JST1dTRVJfUExVR0lOX0lELCBrZXksIHZhbHVlKVxuICAgICAgICAgIC5jYXRjaCgocmVhc29uOiBFcnJvcikgPT4ge1xuICAgICAgICAgICAgY29uc29sZS5lcnJvcihgRmFpbGVkIHRvIHNldCBzaG93TGFzdE1vZGlmaWVkQ29sdW1uIHNldHRpbmdgKTtcbiAgICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9XG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy50b2dnbGVIaWRkZW5GaWxlcywge1xuICAgIGxhYmVsOiB0cmFucy5fXygnU2hvdyBIaWRkZW4gRmlsZXMnKSxcbiAgICBpc1RvZ2dsZWQ6ICgpID0+IGJyb3dzZXIuc2hvd0hpZGRlbkZpbGVzLFxuICAgIGlzVmlzaWJsZTogKCkgPT4gUGFnZUNvbmZpZy5nZXRPcHRpb24oJ2FsbG93X2hpZGRlbl9maWxlcycpID09PSAndHJ1ZScsXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgY29uc3QgdmFsdWUgPSAhYnJvd3Nlci5zaG93SGlkZGVuRmlsZXM7XG4gICAgICBjb25zdCBrZXkgPSAnc2hvd0hpZGRlbkZpbGVzJztcbiAgICAgIGlmIChzZXR0aW5nUmVnaXN0cnkpIHtcbiAgICAgICAgcmV0dXJuIHNldHRpbmdSZWdpc3RyeVxuICAgICAgICAgIC5zZXQoRklMRV9CUk9XU0VSX1BMVUdJTl9JRCwga2V5LCB2YWx1ZSlcbiAgICAgICAgICAuY2F0Y2goKHJlYXNvbjogRXJyb3IpID0+IHtcbiAgICAgICAgICAgIGNvbnNvbGUuZXJyb3IoYEZhaWxlZCB0byBzZXQgc2hvd0hpZGRlbkZpbGVzIHNldHRpbmdgKTtcbiAgICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9XG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy50b2dnbGVGaWxlQ2hlY2tib3hlcywge1xuICAgIGxhYmVsOiB0cmFucy5fXygnU2hvdyBGaWxlIENoZWNrYm94ZXMnKSxcbiAgICBpc1RvZ2dsZWQ6ICgpID0+IGJyb3dzZXIuc2hvd0ZpbGVDaGVja2JveGVzLFxuICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgIGNvbnN0IHZhbHVlID0gIWJyb3dzZXIuc2hvd0ZpbGVDaGVja2JveGVzO1xuICAgICAgY29uc3Qga2V5ID0gJ3Nob3dGaWxlQ2hlY2tib3hlcyc7XG4gICAgICBpZiAoc2V0dGluZ1JlZ2lzdHJ5KSB7XG4gICAgICAgIHJldHVybiBzZXR0aW5nUmVnaXN0cnlcbiAgICAgICAgICAuc2V0KEZJTEVfQlJPV1NFUl9QTFVHSU5fSUQsIGtleSwgdmFsdWUpXG4gICAgICAgICAgLmNhdGNoKChyZWFzb246IEVycm9yKSA9PiB7XG4gICAgICAgICAgICBjb25zb2xlLmVycm9yKGBGYWlsZWQgdG8gc2V0IHNob3dGaWxlQ2hlY2tib3hlcyBzZXR0aW5nYCk7XG4gICAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfVxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuc2VhcmNoLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdTZWFyY2ggb24gRmlsZSBOYW1lcycpLFxuICAgIGV4ZWN1dGU6ICgpID0+IGFsZXJ0KCdzZWFyY2gnKVxuICB9KTtcblxuICBpZiAoY29tbWFuZFBhbGV0dGUpIHtcbiAgICBjb21tYW5kUGFsZXR0ZS5hZGRJdGVtKHtcbiAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMudG9nZ2xlTmF2aWdhdGVUb0N1cnJlbnREaXJlY3RvcnksXG4gICAgICBjYXRlZ29yeTogdHJhbnMuX18oJ0ZpbGUgT3BlcmF0aW9ucycpXG4gICAgfSk7XG4gIH1cbn1cblxuLyoqXG4gKiBFeHBvcnQgdGhlIHBsdWdpbnMgYXMgZGVmYXVsdC5cbiAqL1xuY29uc3QgcGx1Z2luczogSnVweXRlckZyb250RW5kUGx1Z2luPGFueT5bXSA9IFtcbiAgZmFjdG9yeSxcbiAgYnJvd3NlcixcbiAgc2hhcmVGaWxlLFxuICBmaWxlVXBsb2FkU3RhdHVzLFxuICBkb3dubG9hZFBsdWdpbixcbiAgYnJvd3NlcldpZGdldCxcbiAgb3BlbldpdGhQbHVnaW4sXG4gIG9wZW5Ccm93c2VyVGFiUGx1Z2luLFxuICBvcGVuVXJsUGx1Z2luXG5dO1xuZXhwb3J0IGRlZmF1bHQgcGx1Z2lucztcblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgcHJpdmF0ZSBtb2R1bGUgZGF0YS5cbiAqL1xubmFtZXNwYWNlIFByaXZhdGUge1xuICAvKipcbiAgICogR2V0IGJyb3dzZXIgb2JqZWN0IGdpdmVuIGZpbGUgcGF0aC5cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBnZXRCcm93c2VyRm9yUGF0aChcbiAgICBwYXRoOiBzdHJpbmcsXG4gICAgZmFjdG9yeTogSUZpbGVCcm93c2VyRmFjdG9yeVxuICApOiBGaWxlQnJvd3NlciB8IHVuZGVmaW5lZCB7XG4gICAgY29uc3QgeyBkZWZhdWx0QnJvd3NlcjogYnJvd3NlciwgdHJhY2tlciB9ID0gZmFjdG9yeTtcbiAgICBjb25zdCBkcml2ZU5hbWUgPSBicm93c2VyLm1vZGVsLm1hbmFnZXIuc2VydmljZXMuY29udGVudHMuZHJpdmVOYW1lKHBhdGgpO1xuXG4gICAgaWYgKGRyaXZlTmFtZSkge1xuICAgICAgY29uc3QgYnJvd3NlckZvclBhdGggPSB0cmFja2VyLmZpbmQoXG4gICAgICAgIF9wYXRoID0+IF9wYXRoLm1vZGVsLmRyaXZlTmFtZSA9PT0gZHJpdmVOYW1lXG4gICAgICApO1xuXG4gICAgICBpZiAoIWJyb3dzZXJGb3JQYXRoKSB7XG4gICAgICAgIC8vIHdhcm4gdGhhdCBubyBmaWxlYnJvd3NlciBjb3VsZCBiZSBmb3VuZCBmb3IgdGhpcyBkcml2ZU5hbWVcbiAgICAgICAgY29uc29sZS53YXJuKFxuICAgICAgICAgIGAke0NvbW1hbmRJRHMuZ29Ub1BhdGh9IGZhaWxlZCB0byBmaW5kIGZpbGVicm93c2VyIGZvciBwYXRoOiAke3BhdGh9YFxuICAgICAgICApO1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG5cbiAgICAgIHJldHVybiBicm93c2VyRm9yUGF0aDtcbiAgICB9XG5cbiAgICAvLyBpZiBkcml2ZU5hbWUgaXMgZW1wdHksIGFzc3VtZSB0aGUgbWFpbiBmaWxlYnJvd3NlclxuICAgIHJldHVybiBicm93c2VyO1xuICB9XG5cbiAgLyoqXG4gICAqIE5hdmlnYXRlIHRvIGEgcGF0aCBvciB0aGUgcGF0aCBjb250YWluaW5nIGEgZmlsZS5cbiAgICovXG4gIGV4cG9ydCBhc3luYyBmdW5jdGlvbiBuYXZpZ2F0ZVRvUGF0aChcbiAgICBwYXRoOiBzdHJpbmcsXG4gICAgZmFjdG9yeTogSUZpbGVCcm93c2VyRmFjdG9yeSxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvclxuICApOiBQcm9taXNlPENvbnRlbnRzLklNb2RlbD4ge1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgY29uc3QgYnJvd3NlckZvclBhdGggPSBQcml2YXRlLmdldEJyb3dzZXJGb3JQYXRoKHBhdGgsIGZhY3RvcnkpO1xuICAgIGlmICghYnJvd3NlckZvclBhdGgpIHtcbiAgICAgIHRocm93IG5ldyBFcnJvcih0cmFucy5fXygnTm8gYnJvd3NlciBmb3IgcGF0aCcpKTtcbiAgICB9XG4gICAgY29uc3QgeyBzZXJ2aWNlcyB9ID0gYnJvd3NlckZvclBhdGgubW9kZWwubWFuYWdlcjtcbiAgICBjb25zdCBsb2NhbFBhdGggPSBzZXJ2aWNlcy5jb250ZW50cy5sb2NhbFBhdGgocGF0aCk7XG5cbiAgICBhd2FpdCBzZXJ2aWNlcy5yZWFkeTtcbiAgICBjb25zdCBpdGVtID0gYXdhaXQgc2VydmljZXMuY29udGVudHMuZ2V0KHBhdGgsIHsgY29udGVudDogZmFsc2UgfSk7XG4gICAgY29uc3QgeyBtb2RlbCB9ID0gYnJvd3NlckZvclBhdGg7XG4gICAgYXdhaXQgbW9kZWwucmVzdG9yZWQ7XG4gICAgaWYgKGl0ZW0udHlwZSA9PT0gJ2RpcmVjdG9yeScpIHtcbiAgICAgIGF3YWl0IG1vZGVsLmNkKGAvJHtsb2NhbFBhdGh9YCk7XG4gICAgfSBlbHNlIHtcbiAgICAgIGF3YWl0IG1vZGVsLmNkKGAvJHtQYXRoRXh0LmRpcm5hbWUobG9jYWxQYXRoKX1gKTtcbiAgICB9XG4gICAgcmV0dXJuIGl0ZW07XG4gIH1cblxuICAvKipcbiAgICogUmVzdG9yZXMgZmlsZSBicm93c2VyIHN0YXRlIGFuZCBvdmVycmlkZXMgc3RhdGUgaWYgdHJlZSByZXNvbHZlciByZXNvbHZlcy5cbiAgICovXG4gIGV4cG9ydCBhc3luYyBmdW5jdGlvbiByZXN0b3JlQnJvd3NlcihcbiAgICBicm93c2VyOiBGaWxlQnJvd3NlcixcbiAgICBjb21tYW5kczogQ29tbWFuZFJlZ2lzdHJ5LFxuICAgIHJvdXRlcjogSVJvdXRlciB8IG51bGwsXG4gICAgdHJlZTogSnVweXRlckZyb250RW5kLklUcmVlUmVzb2x2ZXIgfCBudWxsXG4gICk6IFByb21pc2U8dm9pZD4ge1xuICAgIGNvbnN0IHJlc3RvcmluZyA9ICdqcC1tb2QtcmVzdG9yaW5nJztcblxuICAgIGJyb3dzZXIuYWRkQ2xhc3MocmVzdG9yaW5nKTtcblxuICAgIGlmICghcm91dGVyKSB7XG4gICAgICBhd2FpdCBicm93c2VyLm1vZGVsLnJlc3RvcmUoYnJvd3Nlci5pZCk7XG4gICAgICBhd2FpdCBicm93c2VyLm1vZGVsLnJlZnJlc2goKTtcbiAgICAgIGJyb3dzZXIucmVtb3ZlQ2xhc3MocmVzdG9yaW5nKTtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICBjb25zdCBsaXN0ZW5lciA9IGFzeW5jICgpID0+IHtcbiAgICAgIHJvdXRlci5yb3V0ZWQuZGlzY29ubmVjdChsaXN0ZW5lcik7XG5cbiAgICAgIGNvbnN0IHBhdGhzID0gYXdhaXQgdHJlZT8ucGF0aHM7XG4gICAgICBpZiAocGF0aHM/LmZpbGUgfHwgcGF0aHM/LmJyb3dzZXIpIHtcbiAgICAgICAgLy8gUmVzdG9yZSB0aGUgbW9kZWwgd2l0aG91dCBwb3B1bGF0aW5nIGl0LlxuICAgICAgICBhd2FpdCBicm93c2VyLm1vZGVsLnJlc3RvcmUoYnJvd3Nlci5pZCwgZmFsc2UpO1xuICAgICAgICBpZiAocGF0aHMuZmlsZSkge1xuICAgICAgICAgIGF3YWl0IGNvbW1hbmRzLmV4ZWN1dGUoQ29tbWFuZElEcy5vcGVuUGF0aCwge1xuICAgICAgICAgICAgcGF0aDogcGF0aHMuZmlsZSxcbiAgICAgICAgICAgIGRvbnRTaG93QnJvd3NlcjogdHJ1ZVxuICAgICAgICAgIH0pO1xuICAgICAgICB9XG4gICAgICAgIGlmIChwYXRocy5icm93c2VyKSB7XG4gICAgICAgICAgYXdhaXQgY29tbWFuZHMuZXhlY3V0ZShDb21tYW5kSURzLm9wZW5QYXRoLCB7XG4gICAgICAgICAgICBwYXRoOiBwYXRocy5icm93c2VyLFxuICAgICAgICAgICAgZG9udFNob3dCcm93c2VyOiB0cnVlXG4gICAgICAgICAgfSk7XG4gICAgICAgIH1cbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIGF3YWl0IGJyb3dzZXIubW9kZWwucmVzdG9yZShicm93c2VyLmlkKTtcbiAgICAgICAgYXdhaXQgYnJvd3Nlci5tb2RlbC5yZWZyZXNoKCk7XG4gICAgICB9XG4gICAgICBicm93c2VyLnJlbW92ZUNsYXNzKHJlc3RvcmluZyk7XG4gICAgfTtcbiAgICByb3V0ZXIucm91dGVkLmNvbm5lY3QobGlzdGVuZXIpO1xuICB9XG5cbiAgZXhwb3J0IG5hbWVzcGFjZSBPcGVuV2l0aCB7XG4gICAgLyoqXG4gICAgICogR2V0IHRoZSBmYWN0b3JpZXMgZm9yIHRoZSBzZWxlY3RlZCBpdGVtXG4gICAgICpcbiAgICAgKiBAcGFyYW0gZG9jUmVnaXN0cnkgQXBwbGljYXRpb24gZG9jdW1lbnQgcmVnaXN0cnlcbiAgICAgKiBAcGFyYW0gaXRlbSBTZWxlY3RlZCBpdGVtIG1vZGVsXG4gICAgICogQHJldHVybnMgQXZhaWxhYmxlIGZhY3RvcmllcyBmb3IgdGhlIG1vZGVsXG4gICAgICovXG4gICAgZXhwb3J0IGZ1bmN0aW9uIGdldEZhY3RvcmllcyhcbiAgICAgIGRvY1JlZ2lzdHJ5OiBEb2N1bWVudFJlZ2lzdHJ5LFxuICAgICAgaXRlbTogQ29udGVudHMuSU1vZGVsXG4gICAgKTogQXJyYXk8RG9jdW1lbnRSZWdpc3RyeS5XaWRnZXRGYWN0b3J5PiB7XG4gICAgICBjb25zdCBmYWN0b3JpZXMgPSBkb2NSZWdpc3RyeS5wcmVmZXJyZWRXaWRnZXRGYWN0b3JpZXMoaXRlbS5wYXRoKTtcbiAgICAgIGNvbnN0IG5vdGVib29rRmFjdG9yeSA9IGRvY1JlZ2lzdHJ5LmdldFdpZGdldEZhY3RvcnkoJ25vdGVib29rJyk7XG4gICAgICBpZiAoXG4gICAgICAgIG5vdGVib29rRmFjdG9yeSAmJlxuICAgICAgICBpdGVtLnR5cGUgPT09ICdub3RlYm9vaycgJiZcbiAgICAgICAgZmFjdG9yaWVzLmluZGV4T2Yobm90ZWJvb2tGYWN0b3J5KSA9PT0gLTFcbiAgICAgICkge1xuICAgICAgICBmYWN0b3JpZXMudW5zaGlmdChub3RlYm9va0ZhY3RvcnkpO1xuICAgICAgfVxuXG4gICAgICByZXR1cm4gZmFjdG9yaWVzO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIFJldHVybiB0aGUgaW50ZXJzZWN0aW9uIG9mIG11bHRpcGxlIGFycmF5cy5cbiAgICAgKlxuICAgICAqIEBwYXJhbSBpdGVyIEl0ZXJhdG9yIG9mIGFycmF5c1xuICAgICAqIEByZXR1cm5zIFNldCBvZiBjb21tb24gZWxlbWVudHMgdG8gYWxsIGFycmF5c1xuICAgICAqL1xuICAgIGV4cG9ydCBmdW5jdGlvbiBpbnRlcnNlY3Rpb248VD4oaXRlcjogSUl0ZXJhdG9yPEFycmF5PFQ+Pik6IFNldDxUPiB7XG4gICAgICAvLyBwb3AgdGhlIGZpcnN0IGVsZW1lbnQgb2YgaXRlclxuICAgICAgY29uc3QgZmlyc3QgPSBpdGVyLm5leHQoKTtcbiAgICAgIC8vIGZpcnN0IHdpbGwgYmUgdW5kZWZpbmVkIGlmIGl0ZXIgaXMgZW1wdHlcbiAgICAgIGlmICghZmlyc3QpIHtcbiAgICAgICAgcmV0dXJuIG5ldyBTZXQ8VD4oKTtcbiAgICAgIH1cblxuICAgICAgLy8gXCJpbml0aWFsaXplXCIgdGhlIGludGVyc2VjdGlvbiBmcm9tIGZpcnN0XG4gICAgICBjb25zdCBpc2VjdCA9IG5ldyBTZXQoZmlyc3QpO1xuICAgICAgLy8gcmVkdWNlIG92ZXIgdGhlIHJlbWFpbmluZyBlbGVtZW50cyBvZiBpdGVyXG4gICAgICByZXR1cm4gcmVkdWNlKFxuICAgICAgICBpdGVyLFxuICAgICAgICAoaXNlY3QsIHN1YmFycikgPT4ge1xuICAgICAgICAgIC8vIGZpbHRlciBvdXQgYWxsIGVsZW1lbnRzIG5vdCBwcmVzZW50IGluIGJvdGggaXNlY3QgYW5kIHN1YmFycixcbiAgICAgICAgICAvLyBhY2N1bXVsYXRlIHJlc3VsdCBpbiBuZXcgc2V0XG4gICAgICAgICAgcmV0dXJuIG5ldyBTZXQoc3ViYXJyLmZpbHRlcih4ID0+IGlzZWN0Lmhhcyh4KSkpO1xuICAgICAgICB9LFxuICAgICAgICBpc2VjdFxuICAgICAgKTtcbiAgICB9XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==