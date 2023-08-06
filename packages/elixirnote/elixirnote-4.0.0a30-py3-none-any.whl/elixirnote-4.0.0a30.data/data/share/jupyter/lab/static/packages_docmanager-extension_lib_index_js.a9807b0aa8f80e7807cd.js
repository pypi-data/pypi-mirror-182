"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_docmanager-extension_lib_index_js"],{

/***/ "../../packages/docmanager-extension/lib/index.js":
/*!********************************************************!*\
  !*** ../../packages/docmanager-extension/lib/index.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ToolbarItems": () => (/* binding */ ToolbarItems),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__),
/* harmony export */   "downloadPlugin": () => (/* binding */ downloadPlugin),
/* harmony export */   "openBrowserTabPlugin": () => (/* binding */ openBrowserTabPlugin),
/* harmony export */   "pathStatusPlugin": () => (/* binding */ pathStatusPlugin),
/* harmony export */   "savingStatusPlugin": () => (/* binding */ savingStatusPlugin)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/docmanager */ "webpack/sharing/consume/default/@jupyterlab/docmanager/@jupyterlab/docmanager");
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/docprovider */ "webpack/sharing/consume/default/@jupyterlab/docprovider/@jupyterlab/docprovider");
/* harmony import */ var _jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_12__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module docmanager-extension
 */













/**
 * The command IDs used by the document manager plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.clone = 'docmanager:clone';
    CommandIDs.deleteFile = 'docmanager:delete-file';
    CommandIDs.newUntitled = 'docmanager:new-untitled';
    CommandIDs.open = 'docmanager:open';
    CommandIDs.openBrowserTab = 'docmanager:open-browser-tab';
    CommandIDs.reload = 'docmanager:reload';
    CommandIDs.rename = 'docmanager:rename';
    CommandIDs.del = 'docmanager:delete';
    CommandIDs.duplicate = 'docmanager:duplicate';
    CommandIDs.restoreCheckpoint = 'docmanager:restore-checkpoint';
    CommandIDs.save = 'docmanager:save';
    CommandIDs.saveAll = 'docmanager:save-all';
    CommandIDs.saveAs = 'docmanager:save-as';
    CommandIDs.download = 'docmanager:download';
    CommandIDs.toggleAutosave = 'docmanager:toggle-autosave';
    CommandIDs.showInFileBrowser = 'docmanager:show-in-file-browser';
})(CommandIDs || (CommandIDs = {}));
/**
 * The id of the document manager plugin.
 */
const docManagerPluginId = '@jupyterlab/docmanager-extension:plugin';
/**
 * A plugin providing the default document manager.
 */
const manager = {
    id: '@jupyterlab/docmanager-extension:manager',
    provides: _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.IDocumentManager,
    optional: [
        _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabStatus,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ISessionContextDialogs,
        _jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_4__.IDocumentProviderFactory,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterLab.IInfo
    ],
    activate: (app, translator, status, sessionDialogs, docProviderFactory, info) => {
        var _a;
        const { serviceManager: manager, docRegistry: registry } = app;
        const contexts = new WeakSet();
        const when = app.restored.then(() => void 0);
        const opener = {
            open: (widget, options) => {
                if (!widget.id) {
                    widget.id = `document-manager-${++Private.id}`;
                }
                widget.title.dataset = Object.assign({ type: 'document-title' }, widget.title.dataset);
                if (!widget.isAttached) {
                    app.shell.add(widget, 'main', options || {});
                }
                app.shell.activateById(widget.id);
                // Handle dirty state for open documents.
                const context = docManager.contextForWidget(widget);
                if (context && !contexts.has(context)) {
                    if (status) {
                        handleContext(status, context);
                    }
                    contexts.add(context);
                }
            }
        };
        const docManager = new _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.DocumentManager({
            registry,
            manager,
            opener,
            when,
            setBusy: (_a = (status && (() => status.setBusy()))) !== null && _a !== void 0 ? _a : undefined,
            sessionDialogs: sessionDialogs || undefined,
            translator: translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.nullTranslator,
            collaborative: true,
            docProviderFactory: docProviderFactory !== null && docProviderFactory !== void 0 ? docProviderFactory : undefined,
            isConnectedCallback: () => {
                if (info) {
                    return info.isConnected;
                }
                return true;
            }
        });
        return docManager;
    }
};
/**
 * The default document manager provider.
 */
const docManagerPlugin = {
    id: docManagerPluginId,
    autoStart: true,
    requires: [_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.IDocumentManager, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.ISettingRegistry],
    optional: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell],
    activate: (app, docManager, settingRegistry, translator, palette, labShell) => {
        translator = translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.nullTranslator;
        const trans = translator.load('jupyterlab');
        const registry = app.docRegistry;
        // Register the file operations commands.
        addCommands(app, docManager, opener, settingRegistry, translator, labShell, palette);
        // Keep up to date with the settings registry.
        const onSettingsUpdated = (settings) => {
            // Handle whether to autosave
            const autosave = settings.get('autosave').composite;
            docManager.autosave =
                autosave === true || autosave === false ? autosave : true;
            app.commands.notifyCommandChanged(CommandIDs.toggleAutosave);
            // Handle autosave interval
            const autosaveInterval = settings.get('autosaveInterval').composite;
            docManager.autosaveInterval = autosaveInterval || 120;
            // Handle last modified timestamp check margin
            const lastModifiedCheckMargin = settings.get('lastModifiedCheckMargin')
                .composite;
            docManager.lastModifiedCheckMargin = lastModifiedCheckMargin || 500;
            const renameUntitledFile = settings.get('renameUntitledFileOnSave')
                .composite;
            docManager.renameUntitledFileOnSave = renameUntitledFile !== null && renameUntitledFile !== void 0 ? renameUntitledFile : true;
            // Handle default widget factory overrides.
            const defaultViewers = settings.get('defaultViewers').composite;
            const overrides = {};
            // Filter the defaultViewers and file types for existing ones.
            Object.keys(defaultViewers).forEach(ft => {
                if (!registry.getFileType(ft)) {
                    console.warn(`File Type ${ft} not found`);
                    return;
                }
                if (!registry.getWidgetFactory(defaultViewers[ft])) {
                    console.warn(`Document viewer ${defaultViewers[ft]} not found`);
                }
                overrides[ft] = defaultViewers[ft];
            });
            // Set the default factory overrides. If not provided, this has the
            // effect of unsetting any previous overrides.
            (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__.each)(registry.fileTypes(), ft => {
                try {
                    registry.setDefaultWidgetFactory(ft.name, overrides[ft.name]);
                }
                catch (_a) {
                    console.warn(`Failed to set default viewer ${overrides[ft.name]} for file type ${ft.name}`);
                }
            });
        };
        // Fetch the initial state of the settings.
        Promise.all([settingRegistry.load(docManagerPluginId), app.restored])
            .then(([settings]) => {
            settings.changed.connect(onSettingsUpdated);
            onSettingsUpdated(settings);
        })
            .catch((reason) => {
            console.error(reason.message);
        });
        // Register a fetch transformer for the settings registry,
        // allowing us to dynamically populate a help string with the
        // available document viewers and file types for the default
        // viewer overrides.
        settingRegistry.transform(docManagerPluginId, {
            fetch: plugin => {
                // Get the available file types.
                const fileTypes = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__.toArray)(registry.fileTypes())
                    .map(ft => ft.name)
                    .join('    \n');
                // Get the available widget factories.
                const factories = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__.toArray)(registry.widgetFactories())
                    .map(f => f.name)
                    .join('    \n');
                // Generate the help string.
                const description = trans.__(`Overrides for the default viewers for file types.
Specify a mapping from file type name to document viewer name, for example:

defaultViewers: {
  markdown: "Markdown Preview"
}

If you specify non-existent file types or viewers, or if a viewer cannot
open a given file type, the override will not function.

Available viewers:
%1

Available file types:
%2`, factories, fileTypes);
                const schema = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_10__.JSONExt.deepCopy(plugin.schema);
                schema.properties.defaultViewers.description = description;
                return Object.assign(Object.assign({}, plugin), { schema });
            }
        });
        // If the document registry gains or loses a factory or file type,
        // regenerate the settings description with the available options.
        registry.changed.connect(() => settingRegistry.reload(docManagerPluginId));
    }
};
/**
 * A plugin for adding a saving status item to the status bar.
 */
const savingStatusPlugin = {
    id: '@jupyterlab/docmanager-extension:saving-status',
    autoStart: true,
    requires: [_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.IDocumentManager, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell],
    optional: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator, _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__.IStatusBar],
    activate: (_, docManager, labShell, translator, statusBar) => {
        if (!statusBar) {
            // Automatically disable if statusbar missing
            return;
        }
        const saving = new _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.SavingStatus({
            docManager,
            translator: translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.nullTranslator
        });
        // Keep the currently active widget synchronized.
        saving.model.widget = labShell.currentWidget;
        labShell.currentChanged.connect(() => {
            saving.model.widget = labShell.currentWidget;
        });
        statusBar.registerStatusItem(savingStatusPlugin.id, {
            item: saving,
            align: 'middle',
            isActive: () => saving.model !== null && saving.model.status !== null,
            activeStateChanged: saving.model.stateChanged
        });
    }
};
/**
 * A plugin providing a file path widget to the status bar.
 */
const pathStatusPlugin = {
    id: '@jupyterlab/docmanager-extension:path-status',
    autoStart: true,
    requires: [_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.IDocumentManager, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell],
    optional: [_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__.IStatusBar],
    activate: (_, docManager, labShell, statusBar) => {
        if (!statusBar) {
            // Automatically disable if statusbar missing
            return;
        }
        const path = new _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.PathStatus({ docManager });
        // Keep the file path widget up-to-date with the application active widget.
        path.model.widget = labShell.currentWidget;
        labShell.currentChanged.connect(() => {
            path.model.widget = labShell.currentWidget;
        });
        statusBar.registerStatusItem(pathStatusPlugin.id, {
            item: path,
            align: 'right',
            rank: 0
        });
    }
};
/**
 * A plugin providing download commands in the file menu and command palette.
 */
const downloadPlugin = {
    id: '@jupyterlab/docmanager-extension:download',
    autoStart: true,
    requires: [_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.IDocumentManager],
    optional: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    activate: (app, docManager, translator, palette) => {
        const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.nullTranslator).load('jupyterlab');
        const { commands, shell } = app;
        const isEnabled = () => {
            const { currentWidget } = shell;
            return !!(currentWidget && docManager.contextForWidget(currentWidget));
        };
        commands.addCommand(CommandIDs.download, {
            label: trans.__('Download'),
            caption: trans.__('Download the file to your computer'),
            isEnabled,
            execute: () => {
                // Checks that shell.currentWidget is valid:
                if (isEnabled()) {
                    const context = docManager.contextForWidget(shell.currentWidget);
                    if (!context) {
                        return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                            title: trans.__('Cannot Download'),
                            body: trans.__('No context found for current widget!'),
                            buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton()]
                        });
                    }
                    return context.download();
                }
            }
        });
        const category = trans.__('File Operations');
        if (palette) {
            palette.addItem({ command: CommandIDs.download, category });
        }
    }
};
/**
 * A plugin providing open-browser-tab commands.
 *
 * This is its own plugin in case you would like to disable this feature.
 * e.g. jupyter labextension disable @jupyterlab/docmanager-extension:open-browser-tab
 *
 * Note: If disabling this, you may also want to disable:
 * @jupyterlab/filebrowser-extension:open-browser-tab
 */
const openBrowserTabPlugin = {
    id: '@jupyterlab/docmanager-extension:open-browser-tab',
    autoStart: true,
    requires: [_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.IDocumentManager],
    optional: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    activate: (app, docManager, translator) => {
        const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.nullTranslator).load('jupyterlab');
        const { commands } = app;
        commands.addCommand(CommandIDs.openBrowserTab, {
            execute: args => {
                const path = typeof args['path'] === 'undefined' ? '' : args['path'];
                if (!path) {
                    return;
                }
                return docManager.services.contents.getDownloadUrl(path).then(url => {
                    const opened = window.open();
                    if (opened) {
                        opened.opener = null;
                        opened.location.href = url;
                    }
                    else {
                        throw new Error('Failed to open new browser tab.');
                    }
                });
            },
            icon: args => args['icon'] || '',
            label: () => trans.__('Open in New Browser Tab')
        });
    }
};
/**
 * Export the plugins as default.
 */
const plugins = [
    manager,
    docManagerPlugin,
    pathStatusPlugin,
    savingStatusPlugin,
    downloadPlugin,
    openBrowserTabPlugin
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);
/**
 * Toolbar item factory
 */
var ToolbarItems;
(function (ToolbarItems) {
    /**
     * Create save button toolbar item.
     *
     */
    function createSaveButton(commands, fileChanged) {
        return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.addCommandToolbarButtonClass)(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ReactWidget.create(react__WEBPACK_IMPORTED_MODULE_12__.createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.UseSignal, { signal: fileChanged }, () => (react__WEBPACK_IMPORTED_MODULE_12__.createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.CommandToolbarButtonComponent, { commands: commands, id: CommandIDs.save, label: '', args: { toolbar: true } })))));
    }
    ToolbarItems.createSaveButton = createSaveButton;
})(ToolbarItems || (ToolbarItems = {}));
/* Widget to display the revert to checkpoint confirmation. */
class RevertConfirmWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_11__.Widget {
    /**
     * Construct a new revert confirmation widget.
     */
    constructor(checkpoint, trans, fileType = 'notebook') {
        super({
            node: Private.createRevertConfirmNode(checkpoint, fileType, trans)
        });
    }
}
// Returns the file type for a widget.
function fileType(widget, docManager) {
    if (!widget) {
        return 'File';
    }
    const context = docManager.contextForWidget(widget);
    if (!context) {
        return '';
    }
    const fts = docManager.registry.getFileTypesForPath(context.path);
    return fts.length && fts[0].displayName ? fts[0].displayName : 'File';
}
/**
 * Add the file operations commands to the application's command registry.
 */
function addCommands(app, docManager, opener, settingRegistry, translator, labShell, palette) {
    const trans = translator.load('jupyterlab');
    const { commands, shell } = app;
    const category = trans.__('File Operations');
    const isEnabled = () => {
        const { currentWidget } = shell;
        return !!(currentWidget && docManager.contextForWidget(currentWidget));
    };
    const isWritable = () => {
        const { currentWidget } = shell;
        if (!currentWidget) {
            return false;
        }
        const context = docManager.contextForWidget(currentWidget);
        return !!(context &&
            context.contentsModel &&
            context.contentsModel.writable);
    };
    // If inside a rich application like JupyterLab, add additional functionality.
    if (labShell) {
        addLabCommands(app, docManager, labShell, opener, translator);
    }
    commands.addCommand(CommandIDs.deleteFile, {
        label: () => `Delete ${fileType(shell.currentWidget, docManager)}`,
        execute: args => {
            const path = typeof args['path'] === 'undefined' ? '' : args['path'];
            if (!path) {
                const command = CommandIDs.deleteFile;
                throw new Error(`A non-empty path is required for ${command}.`);
            }
            return docManager.deleteFile(path);
        }
    });
    commands.addCommand(CommandIDs.newUntitled, {
        execute: args => {
            const errorTitle = args['error'] || trans.__('Error');
            const path = typeof args['path'] === 'undefined' ? '' : args['path'];
            const options = {
                type: args['type'],
                path
            };
            if (args['type'] === 'file') {
                options.ext = args['ext'] || '.txt';
            }
            return docManager.services.contents
                .newUntitled(options)
                .catch(error => (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)(errorTitle, error));
        },
        label: args => args['label'] || `New ${args['type']}`
    });
    commands.addCommand(CommandIDs.open, {
        execute: args => {
            const path = typeof args['path'] === 'undefined' ? '' : args['path'];
            const factory = args['factory'] || void 0;
            const kernel = args === null || args === void 0 ? void 0 : args.kernel;
            const options = args['options'] || void 0;
            return docManager.services.contents
                .get(path, { content: false })
                .then(() => docManager.openOrReveal(path, factory, kernel, options));
        },
        icon: args => args['icon'] || '',
        label: args => {
            var _a;
            return ((_a = (args['label'] || args['factory'])) !== null && _a !== void 0 ? _a : trans.__('Open the provided `path`.'));
        },
        mnemonic: args => args['mnemonic'] || -1
    });
    commands.addCommand(CommandIDs.reload, {
        label: () => trans.__('Reload %1 from Disk', fileType(shell.currentWidget, docManager)),
        caption: trans.__('Reload contents from disk'),
        isEnabled,
        execute: () => {
            // Checks that shell.currentWidget is valid:
            if (!isEnabled()) {
                return;
            }
            const context = docManager.contextForWidget(shell.currentWidget);
            const type = fileType(shell.currentWidget, docManager);
            if (!context) {
                return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                    title: trans.__('Cannot Reload'),
                    body: trans.__('No context found for current widget!'),
                    buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton()]
                });
            }
            if (context.model.dirty) {
                return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                    title: trans.__('Reload %1 from Disk', type),
                    body: trans.__('Are you sure you want to reload the %1 from the disk?', type),
                    buttons: [
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton(),
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.warnButton({ label: trans.__('Reload') })
                    ]
                }).then(result => {
                    if (result.button.accept && !context.isDisposed) {
                        return context.revert();
                    }
                });
            }
            else {
                if (!context.isDisposed) {
                    return context.revert();
                }
            }
        }
    });
    commands.addCommand(CommandIDs.restoreCheckpoint, {
        label: () => trans.__('Revert %1 to Checkpoint…', fileType(shell.currentWidget, docManager)),
        caption: trans.__('Revert contents to previous checkpoint'),
        isEnabled,
        execute: () => {
            // Checks that shell.currentWidget is valid:
            if (!isEnabled()) {
                return;
            }
            const context = docManager.contextForWidget(shell.currentWidget);
            if (!context) {
                return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                    title: trans.__('Cannot Revert'),
                    body: trans.__('No context found for current widget!'),
                    buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton()]
                });
            }
            return context.listCheckpoints().then(async (checkpoints) => {
                const type = fileType(shell.currentWidget, docManager);
                if (checkpoints.length < 1) {
                    await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)(trans.__('No checkpoints'), trans.__('No checkpoints are available for this %1.', type));
                    return;
                }
                const targetCheckpoint = checkpoints.length === 1
                    ? checkpoints[0]
                    : await Private.getTargetCheckpoint(checkpoints.reverse(), trans);
                if (!targetCheckpoint) {
                    return;
                }
                return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                    title: trans.__('Revert %1 to checkpoint', type),
                    body: new RevertConfirmWidget(targetCheckpoint, trans, type),
                    buttons: [
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton(),
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.warnButton({ label: trans.__('Revert') })
                    ]
                }).then(result => {
                    if (context.isDisposed) {
                        return;
                    }
                    if (result.button.accept) {
                        if (context.model.readOnly) {
                            return context.revert();
                        }
                        return context
                            .restoreCheckpoint(targetCheckpoint.id)
                            .then(() => context.revert());
                    }
                });
            });
        }
    });
    const caption = () => {
        if (_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getOption('collaborative') == 'true') {
            return trans.__('In collaborative mode, the document is saved automatically after every change');
        }
        else {
            return trans.__('Save and create checkpoint');
        }
    };
    const saveInProgress = new WeakSet();
    commands.addCommand(CommandIDs.save, {
        label: () => trans.__('Save %1', fileType(shell.currentWidget, docManager)),
        caption,
        icon: args => (args.toolbar ? _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__.saveIcon : ''),
        isEnabled: isWritable,
        execute: async () => {
            var _a, _b, _c;
            // Checks that shell.currentWidget is valid:
            if (isEnabled()) {
                const widget = shell.currentWidget;
                const context = docManager.contextForWidget(widget);
                if (!context) {
                    return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                        title: trans.__('Cannot Save'),
                        body: trans.__('No context found for current widget!'),
                        buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton()]
                    });
                }
                else {
                    if (saveInProgress.has(context)) {
                        return;
                    }
                    if (context.model.readOnly) {
                        return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                            title: trans.__('Cannot Save'),
                            body: trans.__('Document is read-only'),
                            buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton()]
                        });
                    }
                    saveInProgress.add(context);
                    const oldName = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PathExt.basename((_b = (_a = context.contentsModel) === null || _a === void 0 ? void 0 : _a.path) !== null && _b !== void 0 ? _b : '');
                    let newName = oldName;
                    if (docManager.renameUntitledFileOnSave &&
                        widget.isUntitled === true) {
                        const result = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.InputDialog.getText({
                            title: trans.__('Rename file'),
                            okLabel: trans.__('Rename'),
                            placeholder: trans.__('File name'),
                            text: oldName,
                            selectionRange: oldName.length - _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PathExt.extname(oldName).length,
                            checkbox: {
                                label: trans.__("Don't ask me again."),
                                caption: trans.__('If checked, you will not be asked to rename future untitled files when saving them.')
                            }
                        });
                        if (result.button.accept) {
                            newName = (_c = result.value) !== null && _c !== void 0 ? _c : oldName;
                            widget.isUntitled = false;
                            if (typeof result.isChecked === 'boolean') {
                                const currentSetting = (await settingRegistry.get(docManagerPluginId, 'renameUntitledFileOnSave')).composite;
                                if (result.isChecked === currentSetting) {
                                    settingRegistry
                                        .set(docManagerPluginId, 'renameUntitledFileOnSave', !result.isChecked)
                                        .catch(reason => {
                                        console.error(`Fail to set 'renameUntitledFileOnSave:\n${reason}`);
                                    });
                                }
                            }
                        }
                    }
                    try {
                        await context.save();
                        if (!(widget === null || widget === void 0 ? void 0 : widget.isDisposed)) {
                            return context.createCheckpoint();
                        }
                    }
                    catch (err) {
                        // If the save was canceled by user-action, do nothing.
                        if (err.name === 'ModalCancelError') {
                            return;
                        }
                        throw err;
                    }
                    finally {
                        saveInProgress.delete(context);
                        if (newName !== oldName) {
                            await context.rename(newName);
                        }
                    }
                }
            }
        }
    });
    commands.addCommand(CommandIDs.saveAll, {
        label: () => trans.__('Save All'),
        caption: trans.__('Save all open documents'),
        isEnabled: () => {
            return (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__.some)((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__.map)(shell.widgets('main'), w => docManager.contextForWidget(w)), c => { var _a, _b; return (_b = (_a = c === null || c === void 0 ? void 0 : c.contentsModel) === null || _a === void 0 ? void 0 : _a.writable) !== null && _b !== void 0 ? _b : false; });
        },
        execute: () => {
            const promises = [];
            const paths = new Set(); // Cache so we don't double save files.
            (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__.each)(shell.widgets('main'), widget => {
                const context = docManager.contextForWidget(widget);
                if (context && !context.model.readOnly && !paths.has(context.path)) {
                    paths.add(context.path);
                    promises.push(context.save());
                }
            });
            return Promise.all(promises);
        }
    });
    commands.addCommand(CommandIDs.saveAs, {
        label: () => trans.__('Save %1 As…', fileType(shell.currentWidget, docManager)),
        caption: trans.__('Save with new path'),
        isEnabled,
        execute: () => {
            // Checks that shell.currentWidget is valid:
            if (isEnabled()) {
                const context = docManager.contextForWidget(shell.currentWidget);
                if (!context) {
                    return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                        title: trans.__('Cannot Save'),
                        body: trans.__('No context found for current widget!'),
                        buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton()]
                    });
                }
                return context.saveAs();
            }
        }
    });
    commands.addCommand(CommandIDs.toggleAutosave, {
        label: trans.__('Autosave Documents'),
        isToggled: () => docManager.autosave,
        execute: () => {
            const value = !docManager.autosave;
            const key = 'autosave';
            return settingRegistry
                .set(docManagerPluginId, key, value)
                .catch((reason) => {
                console.error(`Failed to set ${docManagerPluginId}:${key} - ${reason.message}`);
            });
        }
    });
    if (palette) {
        [
            CommandIDs.reload,
            CommandIDs.restoreCheckpoint,
            CommandIDs.save,
            CommandIDs.saveAs,
            CommandIDs.toggleAutosave,
            CommandIDs.duplicate
        ].forEach(command => {
            palette.addItem({ command, category });
        });
    }
}
function addLabCommands(app, docManager, labShell, opener, translator) {
    const trans = translator.load('jupyterlab');
    const { commands } = app;
    // Returns the doc widget associated with the most recent contextmenu event.
    const contextMenuWidget = () => {
        var _a;
        const pathRe = /[Pp]ath:\s?(.*)\n?/;
        const test = (node) => { var _a; return !!((_a = node['title']) === null || _a === void 0 ? void 0 : _a.match(pathRe)); };
        const node = app.contextMenuHitTest(test);
        const pathMatch = node === null || node === void 0 ? void 0 : node['title'].match(pathRe);
        return ((_a = (pathMatch && docManager.findWidget(pathMatch[1], null))) !== null && _a !== void 0 ? _a : 
        // Fall back to active doc widget if path cannot be obtained from event.
        labShell.currentWidget);
    };
    // Returns `true` if the current widget has a document context.
    const isEnabled = () => {
        const { currentWidget } = labShell;
        return !!(currentWidget && docManager.contextForWidget(currentWidget));
    };
    commands.addCommand(CommandIDs.clone, {
        label: () => trans.__('New View for %1', fileType(contextMenuWidget(), docManager)),
        isEnabled,
        execute: args => {
            const widget = contextMenuWidget();
            const options = args['options'] || {
                mode: 'split-right'
            };
            if (!widget) {
                return;
            }
            // Clone the widget.
            const child = docManager.cloneWidget(widget);
            if (child) {
                opener.open(child, options);
            }
        }
    });
    commands.addCommand(CommandIDs.rename, {
        label: () => {
            let t = fileType(contextMenuWidget(), docManager);
            if (t) {
                t = ' ' + t;
            }
            return trans.__('Rename%1…', t);
        },
        isEnabled,
        execute: () => {
            // Implies contextMenuWidget() !== null
            if (isEnabled()) {
                const context = docManager.contextForWidget(contextMenuWidget());
                return (0,_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_3__.renameDialog)(docManager, context);
            }
        }
    });
    commands.addCommand(CommandIDs.duplicate, {
        label: () => trans.__('Duplicate %1', fileType(contextMenuWidget(), docManager)),
        isEnabled,
        execute: () => {
            if (isEnabled()) {
                const context = docManager.contextForWidget(contextMenuWidget());
                if (!context) {
                    return;
                }
                return docManager.duplicate(context.path);
            }
        }
    });
    commands.addCommand(CommandIDs.del, {
        label: () => trans.__('Delete %1', fileType(contextMenuWidget(), docManager)),
        isEnabled,
        execute: async () => {
            // Implies contextMenuWidget() !== null
            if (isEnabled()) {
                const context = docManager.contextForWidget(contextMenuWidget());
                if (!context) {
                    return;
                }
                const result = await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                    title: trans.__('Delete'),
                    body: trans.__('Are you sure you want to delete %1', context.path),
                    buttons: [
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton(),
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.warnButton({ label: trans.__('Delete') })
                    ]
                });
                if (result.button.accept) {
                    await app.commands.execute('docmanager:delete-file', {
                        path: context.path
                    });
                }
            }
        }
    });
    commands.addCommand(CommandIDs.showInFileBrowser, {
        label: () => trans.__('Show in File Browser'),
        isEnabled,
        execute: async () => {
            const widget = contextMenuWidget();
            const context = widget && docManager.contextForWidget(widget);
            if (!context) {
                return;
            }
            // 'activate' is needed if this command is selected in the "open tabs" sidebar
            await commands.execute('filebrowser:activate', { path: context.path });
            await commands.execute('filebrowser:go-to-path', { path: context.path });
        }
    });
}
/**
 * Handle dirty state for a context.
 */
function handleContext(status, context) {
    let disposable = null;
    const onStateChanged = (sender, args) => {
        if (args.name === 'dirty') {
            if (args.newValue === true) {
                if (!disposable) {
                    disposable = status.setDirty();
                }
            }
            else if (disposable) {
                disposable.dispose();
                disposable = null;
            }
        }
    };
    void context.ready.then(() => {
        context.model.stateChanged.connect(onStateChanged);
        if (context.model.dirty) {
            disposable = status.setDirty();
        }
    });
    context.disposed.connect(() => {
        if (disposable) {
            disposable.dispose();
        }
    });
}
/**
 * A namespace for private module data.
 */
var Private;
(function (Private) {
    /**
     * A counter for unique IDs.
     */
    Private.id = 0;
    function createRevertConfirmNode(checkpoint, fileType, trans) {
        const body = document.createElement('div');
        const confirmMessage = document.createElement('p');
        const confirmText = document.createTextNode(trans.__('Are you sure you want to revert the %1 to checkpoint? ', fileType));
        const cannotUndoText = document.createElement('strong');
        cannotUndoText.textContent = trans.__('This cannot be undone.');
        confirmMessage.appendChild(confirmText);
        confirmMessage.appendChild(cannotUndoText);
        const lastCheckpointMessage = document.createElement('p');
        const lastCheckpointText = document.createTextNode(trans.__('The checkpoint was last updated at: '));
        const lastCheckpointDate = document.createElement('p');
        const date = new Date(checkpoint.last_modified);
        lastCheckpointDate.style.textAlign = 'center';
        lastCheckpointDate.textContent =
            _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.Time.format(date, 'dddd, MMMM Do YYYY, h:mm:ss a') +
                ' (' +
                _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.Time.formatHuman(date) +
                ')';
        lastCheckpointMessage.appendChild(lastCheckpointText);
        lastCheckpointMessage.appendChild(lastCheckpointDate);
        body.appendChild(confirmMessage);
        body.appendChild(lastCheckpointMessage);
        return body;
    }
    Private.createRevertConfirmNode = createRevertConfirmNode;
    /**
     * Ask user for a checkpoint to revert to.
     */
    async function getTargetCheckpoint(checkpoints, trans) {
        // the id could be too long to show so use the index instead
        const indexSeparator = '.';
        const items = checkpoints.map((checkpoint, index) => {
            const isoDate = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.Time.format(checkpoint.last_modified);
            const humanDate = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.Time.formatHuman(checkpoint.last_modified);
            return `${index}${indexSeparator} ${isoDate} (${humanDate})`;
        });
        const selectedItem = (await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.InputDialog.getItem({
            items: items,
            title: trans.__('Choose a checkpoint')
        })).value;
        if (!selectedItem) {
            return;
        }
        const selectedIndex = selectedItem.split(indexSeparator, 1)[0];
        return checkpoints[parseInt(selectedIndex, 10)];
    }
    Private.getTargetCheckpoint = getTargetCheckpoint;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfZG9jbWFuYWdlci1leHRlbnNpb25fbGliX2luZGV4X2pzLmE5ODA3YjBhYThmODBlNzgwN2NkLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFROEI7QUFZSDtBQUNrRDtBQU9oRDtBQUNtQztBQUdKO0FBQ1o7QUFLbEI7QUFDb0I7QUFDUTtBQUVqQjtBQUdIO0FBQ1Y7QUFFL0I7O0dBRUc7QUFDSCxJQUFVLFVBQVUsQ0FnQ25CO0FBaENELFdBQVUsVUFBVTtJQUNMLGdCQUFLLEdBQUcsa0JBQWtCLENBQUM7SUFFM0IscUJBQVUsR0FBRyx3QkFBd0IsQ0FBQztJQUV0QyxzQkFBVyxHQUFHLHlCQUF5QixDQUFDO0lBRXhDLGVBQUksR0FBRyxpQkFBaUIsQ0FBQztJQUV6Qix5QkFBYyxHQUFHLDZCQUE2QixDQUFDO0lBRS9DLGlCQUFNLEdBQUcsbUJBQW1CLENBQUM7SUFFN0IsaUJBQU0sR0FBRyxtQkFBbUIsQ0FBQztJQUU3QixjQUFHLEdBQUcsbUJBQW1CLENBQUM7SUFFMUIsb0JBQVMsR0FBRyxzQkFBc0IsQ0FBQztJQUVuQyw0QkFBaUIsR0FBRywrQkFBK0IsQ0FBQztJQUVwRCxlQUFJLEdBQUcsaUJBQWlCLENBQUM7SUFFekIsa0JBQU8sR0FBRyxxQkFBcUIsQ0FBQztJQUVoQyxpQkFBTSxHQUFHLG9CQUFvQixDQUFDO0lBRTlCLG1CQUFRLEdBQUcscUJBQXFCLENBQUM7SUFFakMseUJBQWMsR0FBRyw0QkFBNEIsQ0FBQztJQUU5Qyw0QkFBaUIsR0FBRyxpQ0FBaUMsQ0FBQztBQUNyRSxDQUFDLEVBaENTLFVBQVUsS0FBVixVQUFVLFFBZ0NuQjtBQUVEOztHQUVHO0FBQ0gsTUFBTSxrQkFBa0IsR0FBRyx5Q0FBeUMsQ0FBQztBQUVyRTs7R0FFRztBQUNILE1BQU0sT0FBTyxHQUE0QztJQUN2RCxFQUFFLEVBQUUsMENBQTBDO0lBQzlDLFFBQVEsRUFBRSxvRUFBZ0I7SUFDMUIsUUFBUSxFQUFFO1FBQ1IsZ0VBQVc7UUFDWCwrREFBVTtRQUNWLHdFQUFzQjtRQUN0Qiw2RUFBd0I7UUFDeEIscUVBQWdCO0tBQ2pCO0lBQ0QsUUFBUSxFQUFFLENBQ1IsR0FBb0IsRUFDcEIsVUFBOEIsRUFDOUIsTUFBeUIsRUFDekIsY0FBNkMsRUFDN0Msa0JBQW1ELEVBQ25ELElBQTZCLEVBQzdCLEVBQUU7O1FBQ0YsTUFBTSxFQUFFLGNBQWMsRUFBRSxPQUFPLEVBQUUsV0FBVyxFQUFFLFFBQVEsRUFBRSxHQUFHLEdBQUcsQ0FBQztRQUMvRCxNQUFNLFFBQVEsR0FBRyxJQUFJLE9BQU8sRUFBNEIsQ0FBQztRQUN6RCxNQUFNLElBQUksR0FBRyxHQUFHLENBQUMsUUFBUSxDQUFDLElBQUksQ0FBQyxHQUFHLEVBQUUsQ0FBQyxLQUFLLENBQUMsQ0FBQyxDQUFDO1FBRTdDLE1BQU0sTUFBTSxHQUFrQztZQUM1QyxJQUFJLEVBQUUsQ0FBQyxNQUFNLEVBQUUsT0FBTyxFQUFFLEVBQUU7Z0JBQ3hCLElBQUksQ0FBQyxNQUFNLENBQUMsRUFBRSxFQUFFO29CQUNkLE1BQU0sQ0FBQyxFQUFFLEdBQUcsb0JBQW9CLEVBQUUsT0FBTyxDQUFDLEVBQUUsRUFBRSxDQUFDO2lCQUNoRDtnQkFDRCxNQUFNLENBQUMsS0FBSyxDQUFDLE9BQU8sbUJBQ2xCLElBQUksRUFBRSxnQkFBZ0IsSUFDbkIsTUFBTSxDQUFDLEtBQUssQ0FBQyxPQUFPLENBQ3hCLENBQUM7Z0JBQ0YsSUFBSSxDQUFDLE1BQU0sQ0FBQyxVQUFVLEVBQUU7b0JBQ3RCLEdBQUcsQ0FBQyxLQUFLLENBQUMsR0FBRyxDQUFDLE1BQU0sRUFBRSxNQUFNLEVBQUUsT0FBTyxJQUFJLEVBQUUsQ0FBQyxDQUFDO2lCQUM5QztnQkFDRCxHQUFHLENBQUMsS0FBSyxDQUFDLFlBQVksQ0FBQyxNQUFNLENBQUMsRUFBRSxDQUFDLENBQUM7Z0JBRWxDLHlDQUF5QztnQkFDekMsTUFBTSxPQUFPLEdBQUcsVUFBVSxDQUFDLGdCQUFnQixDQUFDLE1BQU0sQ0FBQyxDQUFDO2dCQUNwRCxJQUFJLE9BQU8sSUFBSSxDQUFDLFFBQVEsQ0FBQyxHQUFHLENBQUMsT0FBTyxDQUFDLEVBQUU7b0JBQ3JDLElBQUksTUFBTSxFQUFFO3dCQUNWLGFBQWEsQ0FBQyxNQUFNLEVBQUUsT0FBTyxDQUFDLENBQUM7cUJBQ2hDO29CQUNELFFBQVEsQ0FBQyxHQUFHLENBQUMsT0FBTyxDQUFDLENBQUM7aUJBQ3ZCO1lBQ0gsQ0FBQztTQUNGLENBQUM7UUFFRixNQUFNLFVBQVUsR0FBRyxJQUFJLG1FQUFlLENBQUM7WUFDckMsUUFBUTtZQUNSLE9BQU87WUFDUCxNQUFNO1lBQ04sSUFBSTtZQUNKLE9BQU8sRUFBRSxPQUFDLE1BQU0sSUFBSSxDQUFDLEdBQUcsRUFBRSxDQUFDLE1BQU0sQ0FBQyxPQUFPLEVBQUUsQ0FBQyxDQUFDLG1DQUFJLFNBQVM7WUFDMUQsY0FBYyxFQUFFLGNBQWMsSUFBSSxTQUFTO1lBQzNDLFVBQVUsRUFBRSxVQUFVLGFBQVYsVUFBVSxjQUFWLFVBQVUsR0FBSSxtRUFBYztZQUN4QyxhQUFhLEVBQUUsSUFBSTtZQUNuQixrQkFBa0IsRUFBRSxrQkFBa0IsYUFBbEIsa0JBQWtCLGNBQWxCLGtCQUFrQixHQUFJLFNBQVM7WUFDbkQsbUJBQW1CLEVBQUUsR0FBRyxFQUFFO2dCQUN4QixJQUFJLElBQUksRUFBRTtvQkFDUixPQUFPLElBQUksQ0FBQyxXQUFXLENBQUM7aUJBQ3pCO2dCQUNELE9BQU8sSUFBSSxDQUFDO1lBQ2QsQ0FBQztTQUNGLENBQUMsQ0FBQztRQUVILE9BQU8sVUFBVSxDQUFDO0lBQ3BCLENBQUM7Q0FDRixDQUFDO0FBRUY7O0dBRUc7QUFDSCxNQUFNLGdCQUFnQixHQUFnQztJQUNwRCxFQUFFLEVBQUUsa0JBQWtCO0lBQ3RCLFNBQVMsRUFBRSxJQUFJO0lBQ2YsUUFBUSxFQUFFLENBQUMsb0VBQWdCLEVBQUUseUVBQWdCLENBQUM7SUFDOUMsUUFBUSxFQUFFLENBQUMsZ0VBQVcsRUFBRSxpRUFBZSxFQUFFLDhEQUFTLENBQUM7SUFDbkQsUUFBUSxFQUFFLENBQ1IsR0FBb0IsRUFDcEIsVUFBNEIsRUFDNUIsZUFBaUMsRUFDakMsVUFBOEIsRUFDOUIsT0FBK0IsRUFDL0IsUUFBMEIsRUFDcEIsRUFBRTtRQUNSLFVBQVUsR0FBRyxVQUFVLGFBQVYsVUFBVSxjQUFWLFVBQVUsR0FBSSxtRUFBYyxDQUFDO1FBQzFDLE1BQU0sS0FBSyxHQUFHLFVBQVUsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUM7UUFDNUMsTUFBTSxRQUFRLEdBQUcsR0FBRyxDQUFDLFdBQVcsQ0FBQztRQUVqQyx5Q0FBeUM7UUFDekMsV0FBVyxDQUNULEdBQUcsRUFDSCxVQUFVLEVBQ1YsTUFBTSxFQUNOLGVBQWUsRUFDZixVQUFVLEVBQ1YsUUFBUSxFQUNSLE9BQU8sQ0FDUixDQUFDO1FBRUYsOENBQThDO1FBQzlDLE1BQU0saUJBQWlCLEdBQUcsQ0FBQyxRQUFvQyxFQUFFLEVBQUU7WUFDakUsNkJBQTZCO1lBQzdCLE1BQU0sUUFBUSxHQUFHLFFBQVEsQ0FBQyxHQUFHLENBQUMsVUFBVSxDQUFDLENBQUMsU0FBMkIsQ0FBQztZQUN0RSxVQUFVLENBQUMsUUFBUTtnQkFDakIsUUFBUSxLQUFLLElBQUksSUFBSSxRQUFRLEtBQUssS0FBSyxDQUFDLENBQUMsQ0FBQyxRQUFRLENBQUMsQ0FBQyxDQUFDLElBQUksQ0FBQztZQUM1RCxHQUFHLENBQUMsUUFBUSxDQUFDLG9CQUFvQixDQUFDLFVBQVUsQ0FBQyxjQUFjLENBQUMsQ0FBQztZQUU3RCwyQkFBMkI7WUFDM0IsTUFBTSxnQkFBZ0IsR0FBRyxRQUFRLENBQUMsR0FBRyxDQUFDLGtCQUFrQixDQUFDLENBQUMsU0FFbEQsQ0FBQztZQUNULFVBQVUsQ0FBQyxnQkFBZ0IsR0FBRyxnQkFBZ0IsSUFBSSxHQUFHLENBQUM7WUFFdEQsOENBQThDO1lBQzlDLE1BQU0sdUJBQXVCLEdBQUcsUUFBUSxDQUFDLEdBQUcsQ0FBQyx5QkFBeUIsQ0FBQztpQkFDcEUsU0FBMEIsQ0FBQztZQUM5QixVQUFVLENBQUMsdUJBQXVCLEdBQUcsdUJBQXVCLElBQUksR0FBRyxDQUFDO1lBRXBFLE1BQU0sa0JBQWtCLEdBQUcsUUFBUSxDQUFDLEdBQUcsQ0FBQywwQkFBMEIsQ0FBQztpQkFDaEUsU0FBb0IsQ0FBQztZQUN4QixVQUFVLENBQUMsd0JBQXdCLEdBQUcsa0JBQWtCLGFBQWxCLGtCQUFrQixjQUFsQixrQkFBa0IsR0FBSSxJQUFJLENBQUM7WUFFakUsMkNBQTJDO1lBQzNDLE1BQU0sY0FBYyxHQUFHLFFBQVEsQ0FBQyxHQUFHLENBQUMsZ0JBQWdCLENBQUMsQ0FBQyxTQUVyRCxDQUFDO1lBQ0YsTUFBTSxTQUFTLEdBQTZCLEVBQUUsQ0FBQztZQUMvQyw4REFBOEQ7WUFDOUQsTUFBTSxDQUFDLElBQUksQ0FBQyxjQUFjLENBQUMsQ0FBQyxPQUFPLENBQUMsRUFBRSxDQUFDLEVBQUU7Z0JBQ3ZDLElBQUksQ0FBQyxRQUFRLENBQUMsV0FBVyxDQUFDLEVBQUUsQ0FBQyxFQUFFO29CQUM3QixPQUFPLENBQUMsSUFBSSxDQUFDLGFBQWEsRUFBRSxZQUFZLENBQUMsQ0FBQztvQkFDMUMsT0FBTztpQkFDUjtnQkFDRCxJQUFJLENBQUMsUUFBUSxDQUFDLGdCQUFnQixDQUFDLGNBQWMsQ0FBQyxFQUFFLENBQUMsQ0FBQyxFQUFFO29CQUNsRCxPQUFPLENBQUMsSUFBSSxDQUFDLG1CQUFtQixjQUFjLENBQUMsRUFBRSxDQUFDLFlBQVksQ0FBQyxDQUFDO2lCQUNqRTtnQkFDRCxTQUFTLENBQUMsRUFBRSxDQUFDLEdBQUcsY0FBYyxDQUFDLEVBQUUsQ0FBQyxDQUFDO1lBQ3JDLENBQUMsQ0FBQyxDQUFDO1lBQ0gsbUVBQW1FO1lBQ25FLDhDQUE4QztZQUM5Qyx1REFBSSxDQUFDLFFBQVEsQ0FBQyxTQUFTLEVBQUUsRUFBRSxFQUFFLENBQUMsRUFBRTtnQkFDOUIsSUFBSTtvQkFDRixRQUFRLENBQUMsdUJBQXVCLENBQUMsRUFBRSxDQUFDLElBQUksRUFBRSxTQUFTLENBQUMsRUFBRSxDQUFDLElBQUksQ0FBQyxDQUFDLENBQUM7aUJBQy9EO2dCQUFDLFdBQU07b0JBQ04sT0FBTyxDQUFDLElBQUksQ0FDVixnQ0FBZ0MsU0FBUyxDQUFDLEVBQUUsQ0FBQyxJQUFJLENBQUMsa0JBQ2hELEVBQUUsQ0FBQyxJQUNMLEVBQUUsQ0FDSCxDQUFDO2lCQUNIO1lBQ0gsQ0FBQyxDQUFDLENBQUM7UUFDTCxDQUFDLENBQUM7UUFFRiwyQ0FBMkM7UUFDM0MsT0FBTyxDQUFDLEdBQUcsQ0FBQyxDQUFDLGVBQWUsQ0FBQyxJQUFJLENBQUMsa0JBQWtCLENBQUMsRUFBRSxHQUFHLENBQUMsUUFBUSxDQUFDLENBQUM7YUFDbEUsSUFBSSxDQUFDLENBQUMsQ0FBQyxRQUFRLENBQUMsRUFBRSxFQUFFO1lBQ25CLFFBQVEsQ0FBQyxPQUFPLENBQUMsT0FBTyxDQUFDLGlCQUFpQixDQUFDLENBQUM7WUFDNUMsaUJBQWlCLENBQUMsUUFBUSxDQUFDLENBQUM7UUFDOUIsQ0FBQyxDQUFDO2FBQ0QsS0FBSyxDQUFDLENBQUMsTUFBYSxFQUFFLEVBQUU7WUFDdkIsT0FBTyxDQUFDLEtBQUssQ0FBQyxNQUFNLENBQUMsT0FBTyxDQUFDLENBQUM7UUFDaEMsQ0FBQyxDQUFDLENBQUM7UUFFTCwwREFBMEQ7UUFDMUQsNkRBQTZEO1FBQzdELDREQUE0RDtRQUM1RCxvQkFBb0I7UUFDcEIsZUFBZSxDQUFDLFNBQVMsQ0FBQyxrQkFBa0IsRUFBRTtZQUM1QyxLQUFLLEVBQUUsTUFBTSxDQUFDLEVBQUU7Z0JBQ2QsZ0NBQWdDO2dCQUNoQyxNQUFNLFNBQVMsR0FBRywwREFBTyxDQUFDLFFBQVEsQ0FBQyxTQUFTLEVBQUUsQ0FBQztxQkFDNUMsR0FBRyxDQUFDLEVBQUUsQ0FBQyxFQUFFLENBQUMsRUFBRSxDQUFDLElBQUksQ0FBQztxQkFDbEIsSUFBSSxDQUFDLFFBQVEsQ0FBQyxDQUFDO2dCQUNsQixzQ0FBc0M7Z0JBQ3RDLE1BQU0sU0FBUyxHQUFHLDBEQUFPLENBQUMsUUFBUSxDQUFDLGVBQWUsRUFBRSxDQUFDO3FCQUNsRCxHQUFHLENBQUMsQ0FBQyxDQUFDLEVBQUUsQ0FBQyxDQUFDLENBQUMsSUFBSSxDQUFDO3FCQUNoQixJQUFJLENBQUMsUUFBUSxDQUFDLENBQUM7Z0JBQ2xCLDRCQUE0QjtnQkFDNUIsTUFBTSxXQUFXLEdBQUcsS0FBSyxDQUFDLEVBQUUsQ0FDMUI7Ozs7Ozs7Ozs7Ozs7O0dBY1AsRUFDTyxTQUFTLEVBQ1QsU0FBUyxDQUNWLENBQUM7Z0JBQ0YsTUFBTSxNQUFNLEdBQUcsZ0VBQWdCLENBQUMsTUFBTSxDQUFDLE1BQU0sQ0FBQyxDQUFDO2dCQUMvQyxNQUFNLENBQUMsVUFBVyxDQUFDLGNBQWMsQ0FBQyxXQUFXLEdBQUcsV0FBVyxDQUFDO2dCQUM1RCx1Q0FBWSxNQUFNLEtBQUUsTUFBTSxJQUFHO1lBQy9CLENBQUM7U0FDRixDQUFDLENBQUM7UUFFSCxrRUFBa0U7UUFDbEUsa0VBQWtFO1FBQ2xFLFFBQVEsQ0FBQyxPQUFPLENBQUMsT0FBTyxDQUFDLEdBQUcsRUFBRSxDQUFDLGVBQWUsQ0FBQyxNQUFNLENBQUMsa0JBQWtCLENBQUMsQ0FBQyxDQUFDO0lBQzdFLENBQUM7Q0FDRixDQUFDO0FBRUY7O0dBRUc7QUFDSSxNQUFNLGtCQUFrQixHQUFnQztJQUM3RCxFQUFFLEVBQUUsZ0RBQWdEO0lBQ3BELFNBQVMsRUFBRSxJQUFJO0lBQ2YsUUFBUSxFQUFFLENBQUMsb0VBQWdCLEVBQUUsOERBQVMsQ0FBQztJQUN2QyxRQUFRLEVBQUUsQ0FBQyxnRUFBVyxFQUFFLDZEQUFVLENBQUM7SUFDbkMsUUFBUSxFQUFFLENBQ1IsQ0FBa0IsRUFDbEIsVUFBNEIsRUFDNUIsUUFBbUIsRUFDbkIsVUFBOEIsRUFDOUIsU0FBNEIsRUFDNUIsRUFBRTtRQUNGLElBQUksQ0FBQyxTQUFTLEVBQUU7WUFDZCw2Q0FBNkM7WUFDN0MsT0FBTztTQUNSO1FBQ0QsTUFBTSxNQUFNLEdBQUcsSUFBSSxnRUFBWSxDQUFDO1lBQzlCLFVBQVU7WUFDVixVQUFVLEVBQUUsVUFBVSxhQUFWLFVBQVUsY0FBVixVQUFVLEdBQUksbUVBQWM7U0FDekMsQ0FBQyxDQUFDO1FBRUgsaURBQWlEO1FBQ2pELE1BQU0sQ0FBQyxLQUFNLENBQUMsTUFBTSxHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUM7UUFDOUMsUUFBUSxDQUFDLGNBQWMsQ0FBQyxPQUFPLENBQUMsR0FBRyxFQUFFO1lBQ25DLE1BQU0sQ0FBQyxLQUFNLENBQUMsTUFBTSxHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUM7UUFDaEQsQ0FBQyxDQUFDLENBQUM7UUFFSCxTQUFTLENBQUMsa0JBQWtCLENBQUMsa0JBQWtCLENBQUMsRUFBRSxFQUFFO1lBQ2xELElBQUksRUFBRSxNQUFNO1lBQ1osS0FBSyxFQUFFLFFBQVE7WUFDZixRQUFRLEVBQUUsR0FBRyxFQUFFLENBQUMsTUFBTSxDQUFDLEtBQUssS0FBSyxJQUFJLElBQUksTUFBTSxDQUFDLEtBQUssQ0FBQyxNQUFNLEtBQUssSUFBSTtZQUNyRSxrQkFBa0IsRUFBRSxNQUFNLENBQUMsS0FBTSxDQUFDLFlBQVk7U0FDL0MsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztDQUNGLENBQUM7QUFFRjs7R0FFRztBQUNJLE1BQU0sZ0JBQWdCLEdBQWdDO0lBQzNELEVBQUUsRUFBRSw4Q0FBOEM7SUFDbEQsU0FBUyxFQUFFLElBQUk7SUFDZixRQUFRLEVBQUUsQ0FBQyxvRUFBZ0IsRUFBRSw4REFBUyxDQUFDO0lBQ3ZDLFFBQVEsRUFBRSxDQUFDLDZEQUFVLENBQUM7SUFDdEIsUUFBUSxFQUFFLENBQ1IsQ0FBa0IsRUFDbEIsVUFBNEIsRUFDNUIsUUFBbUIsRUFDbkIsU0FBNEIsRUFDNUIsRUFBRTtRQUNGLElBQUksQ0FBQyxTQUFTLEVBQUU7WUFDZCw2Q0FBNkM7WUFDN0MsT0FBTztTQUNSO1FBQ0QsTUFBTSxJQUFJLEdBQUcsSUFBSSw4REFBVSxDQUFDLEVBQUUsVUFBVSxFQUFFLENBQUMsQ0FBQztRQUU1QywyRUFBMkU7UUFDM0UsSUFBSSxDQUFDLEtBQU0sQ0FBQyxNQUFNLEdBQUcsUUFBUSxDQUFDLGFBQWEsQ0FBQztRQUM1QyxRQUFRLENBQUMsY0FBYyxDQUFDLE9BQU8sQ0FBQyxHQUFHLEVBQUU7WUFDbkMsSUFBSSxDQUFDLEtBQU0sQ0FBQyxNQUFNLEdBQUcsUUFBUSxDQUFDLGFBQWEsQ0FBQztRQUM5QyxDQUFDLENBQUMsQ0FBQztRQUVILFNBQVMsQ0FBQyxrQkFBa0IsQ0FBQyxnQkFBZ0IsQ0FBQyxFQUFFLEVBQUU7WUFDaEQsSUFBSSxFQUFFLElBQUk7WUFDVixLQUFLLEVBQUUsT0FBTztZQUNkLElBQUksRUFBRSxDQUFDO1NBQ1IsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztDQUNGLENBQUM7QUFFRjs7R0FFRztBQUNJLE1BQU0sY0FBYyxHQUFnQztJQUN6RCxFQUFFLEVBQUUsMkNBQTJDO0lBQy9DLFNBQVMsRUFBRSxJQUFJO0lBQ2YsUUFBUSxFQUFFLENBQUMsb0VBQWdCLENBQUM7SUFDNUIsUUFBUSxFQUFFLENBQUMsZ0VBQVcsRUFBRSxpRUFBZSxDQUFDO0lBQ3hDLFFBQVEsRUFBRSxDQUNSLEdBQW9CLEVBQ3BCLFVBQTRCLEVBQzVCLFVBQThCLEVBQzlCLE9BQStCLEVBQy9CLEVBQUU7UUFDRixNQUFNLEtBQUssR0FBRyxDQUFDLFVBQVUsYUFBVixVQUFVLGNBQVYsVUFBVSxHQUFJLG1FQUFjLENBQUMsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUM7UUFDaEUsTUFBTSxFQUFFLFFBQVEsRUFBRSxLQUFLLEVBQUUsR0FBRyxHQUFHLENBQUM7UUFDaEMsTUFBTSxTQUFTLEdBQUcsR0FBRyxFQUFFO1lBQ3JCLE1BQU0sRUFBRSxhQUFhLEVBQUUsR0FBRyxLQUFLLENBQUM7WUFDaEMsT0FBTyxDQUFDLENBQUMsQ0FBQyxhQUFhLElBQUksVUFBVSxDQUFDLGdCQUFnQixDQUFDLGFBQWEsQ0FBQyxDQUFDLENBQUM7UUFDekUsQ0FBQyxDQUFDO1FBQ0YsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsUUFBUSxFQUFFO1lBQ3ZDLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLFVBQVUsQ0FBQztZQUMzQixPQUFPLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxvQ0FBb0MsQ0FBQztZQUN2RCxTQUFTO1lBQ1QsT0FBTyxFQUFFLEdBQUcsRUFBRTtnQkFDWiw0Q0FBNEM7Z0JBQzVDLElBQUksU0FBUyxFQUFFLEVBQUU7b0JBQ2YsTUFBTSxPQUFPLEdBQUcsVUFBVSxDQUFDLGdCQUFnQixDQUFDLEtBQUssQ0FBQyxhQUFjLENBQUMsQ0FBQztvQkFDbEUsSUFBSSxDQUFDLE9BQU8sRUFBRTt3QkFDWixPQUFPLGdFQUFVLENBQUM7NEJBQ2hCLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLGlCQUFpQixDQUFDOzRCQUNsQyxJQUFJLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxzQ0FBc0MsQ0FBQzs0QkFDdEQsT0FBTyxFQUFFLENBQUMsaUVBQWUsRUFBRSxDQUFDO3lCQUM3QixDQUFDLENBQUM7cUJBQ0o7b0JBQ0QsT0FBTyxPQUFPLENBQUMsUUFBUSxFQUFFLENBQUM7aUJBQzNCO1lBQ0gsQ0FBQztTQUNGLENBQUMsQ0FBQztRQUVILE1BQU0sUUFBUSxHQUFHLEtBQUssQ0FBQyxFQUFFLENBQUMsaUJBQWlCLENBQUMsQ0FBQztRQUM3QyxJQUFJLE9BQU8sRUFBRTtZQUNYLE9BQU8sQ0FBQyxPQUFPLENBQUMsRUFBRSxPQUFPLEVBQUUsVUFBVSxDQUFDLFFBQVEsRUFBRSxRQUFRLEVBQUUsQ0FBQyxDQUFDO1NBQzdEO0lBQ0gsQ0FBQztDQUNGLENBQUM7QUFFRjs7Ozs7Ozs7R0FRRztBQUNJLE1BQU0sb0JBQW9CLEdBQWdDO0lBQy9ELEVBQUUsRUFBRSxtREFBbUQ7SUFDdkQsU0FBUyxFQUFFLElBQUk7SUFDZixRQUFRLEVBQUUsQ0FBQyxvRUFBZ0IsQ0FBQztJQUM1QixRQUFRLEVBQUUsQ0FBQyxnRUFBVyxDQUFDO0lBQ3ZCLFFBQVEsRUFBRSxDQUNSLEdBQW9CLEVBQ3BCLFVBQTRCLEVBQzVCLFVBQThCLEVBQzlCLEVBQUU7UUFDRixNQUFNLEtBQUssR0FBRyxDQUFDLFVBQVUsYUFBVixVQUFVLGNBQVYsVUFBVSxHQUFJLG1FQUFjLENBQUMsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUM7UUFDaEUsTUFBTSxFQUFFLFFBQVEsRUFBRSxHQUFHLEdBQUcsQ0FBQztRQUN6QixRQUFRLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyxjQUFjLEVBQUU7WUFDN0MsT0FBTyxFQUFFLElBQUksQ0FBQyxFQUFFO2dCQUNkLE1BQU0sSUFBSSxHQUNSLE9BQU8sSUFBSSxDQUFDLE1BQU0sQ0FBQyxLQUFLLFdBQVcsQ0FBQyxDQUFDLENBQUMsRUFBRSxDQUFDLENBQUMsQ0FBRSxJQUFJLENBQUMsTUFBTSxDQUFZLENBQUM7Z0JBRXRFLElBQUksQ0FBQyxJQUFJLEVBQUU7b0JBQ1QsT0FBTztpQkFDUjtnQkFFRCxPQUFPLFVBQVUsQ0FBQyxRQUFRLENBQUMsUUFBUSxDQUFDLGNBQWMsQ0FBQyxJQUFJLENBQUMsQ0FBQyxJQUFJLENBQUMsR0FBRyxDQUFDLEVBQUU7b0JBQ2xFLE1BQU0sTUFBTSxHQUFHLE1BQU0sQ0FBQyxJQUFJLEVBQUUsQ0FBQztvQkFDN0IsSUFBSSxNQUFNLEVBQUU7d0JBQ1YsTUFBTSxDQUFDLE1BQU0sR0FBRyxJQUFJLENBQUM7d0JBQ3JCLE1BQU0sQ0FBQyxRQUFRLENBQUMsSUFBSSxHQUFHLEdBQUcsQ0FBQztxQkFDNUI7eUJBQU07d0JBQ0wsTUFBTSxJQUFJLEtBQUssQ0FBQyxpQ0FBaUMsQ0FBQyxDQUFDO3FCQUNwRDtnQkFDSCxDQUFDLENBQUMsQ0FBQztZQUNMLENBQUM7WUFDRCxJQUFJLEVBQUUsSUFBSSxDQUFDLEVBQUUsQ0FBRSxJQUFJLENBQUMsTUFBTSxDQUFZLElBQUksRUFBRTtZQUM1QyxLQUFLLEVBQUUsR0FBRyxFQUFFLENBQUMsS0FBSyxDQUFDLEVBQUUsQ0FBQyx5QkFBeUIsQ0FBQztTQUNqRCxDQUFDLENBQUM7SUFDTCxDQUFDO0NBQ0YsQ0FBQztBQUVGOztHQUVHO0FBQ0gsTUFBTSxPQUFPLEdBQWlDO0lBQzVDLE9BQU87SUFDUCxnQkFBZ0I7SUFDaEIsZ0JBQWdCO0lBQ2hCLGtCQUFrQjtJQUNsQixjQUFjO0lBQ2Qsb0JBQW9CO0NBQ3JCLENBQUM7QUFDRixpRUFBZSxPQUFPLEVBQUM7QUFFdkI7O0dBRUc7QUFDSSxJQUFVLFlBQVksQ0F3QjVCO0FBeEJELFdBQWlCLFlBQVk7SUFDM0I7OztPQUdHO0lBQ0gsU0FBZ0IsZ0JBQWdCLENBQzlCLFFBQXlCLEVBQ3pCLFdBQTBDO1FBRTFDLE9BQU8sa0ZBQTRCLENBQ2pDLG9FQUFrQixDQUNoQixrREFBQywyREFBUyxJQUFDLE1BQU0sRUFBRSxXQUFXLElBQzNCLEdBQUcsRUFBRSxDQUFDLENBQ0wsa0RBQUMsK0VBQTZCLElBQzVCLFFBQVEsRUFBRSxRQUFRLEVBQ2xCLEVBQUUsRUFBRSxVQUFVLENBQUMsSUFBSSxFQUNuQixLQUFLLEVBQUUsRUFBRSxFQUNULElBQUksRUFBRSxFQUFFLE9BQU8sRUFBRSxJQUFJLEVBQUUsR0FDdkIsQ0FDSCxDQUNTLENBQ2IsQ0FDRixDQUFDO0lBQ0osQ0FBQztJQWxCZSw2QkFBZ0IsbUJBa0IvQjtBQUNILENBQUMsRUF4QmdCLFlBQVksS0FBWixZQUFZLFFBd0I1QjtBQUVELDhEQUE4RDtBQUM5RCxNQUFNLG1CQUFvQixTQUFRLG9EQUFNO0lBQ3RDOztPQUVHO0lBQ0gsWUFDRSxVQUFxQyxFQUNyQyxLQUF3QixFQUN4QixXQUFtQixVQUFVO1FBRTdCLEtBQUssQ0FBQztZQUNKLElBQUksRUFBRSxPQUFPLENBQUMsdUJBQXVCLENBQUMsVUFBVSxFQUFFLFFBQVEsRUFBRSxLQUFLLENBQUM7U0FDbkUsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztDQUNGO0FBRUQsc0NBQXNDO0FBQ3RDLFNBQVMsUUFBUSxDQUFDLE1BQXFCLEVBQUUsVUFBNEI7SUFDbkUsSUFBSSxDQUFDLE1BQU0sRUFBRTtRQUNYLE9BQU8sTUFBTSxDQUFDO0tBQ2Y7SUFDRCxNQUFNLE9BQU8sR0FBRyxVQUFVLENBQUMsZ0JBQWdCLENBQUMsTUFBTSxDQUFDLENBQUM7SUFDcEQsSUFBSSxDQUFDLE9BQU8sRUFBRTtRQUNaLE9BQU8sRUFBRSxDQUFDO0tBQ1g7SUFDRCxNQUFNLEdBQUcsR0FBRyxVQUFVLENBQUMsUUFBUSxDQUFDLG1CQUFtQixDQUFDLE9BQU8sQ0FBQyxJQUFJLENBQUMsQ0FBQztJQUNsRSxPQUFPLEdBQUcsQ0FBQyxNQUFNLElBQUksR0FBRyxDQUFDLENBQUMsQ0FBQyxDQUFDLFdBQVcsQ0FBQyxDQUFDLENBQUMsR0FBRyxDQUFDLENBQUMsQ0FBQyxDQUFDLFdBQVcsQ0FBQyxDQUFDLENBQUMsTUFBTSxDQUFDO0FBQ3hFLENBQUM7QUFFRDs7R0FFRztBQUNILFNBQVMsV0FBVyxDQUNsQixHQUFvQixFQUNwQixVQUE0QixFQUM1QixNQUFxQyxFQUNyQyxlQUFpQyxFQUNqQyxVQUF1QixFQUN2QixRQUEwQixFQUMxQixPQUErQjtJQUUvQixNQUFNLEtBQUssR0FBRyxVQUFVLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FBQyxDQUFDO0lBQzVDLE1BQU0sRUFBRSxRQUFRLEVBQUUsS0FBSyxFQUFFLEdBQUcsR0FBRyxDQUFDO0lBQ2hDLE1BQU0sUUFBUSxHQUFHLEtBQUssQ0FBQyxFQUFFLENBQUMsaUJBQWlCLENBQUMsQ0FBQztJQUM3QyxNQUFNLFNBQVMsR0FBRyxHQUFHLEVBQUU7UUFDckIsTUFBTSxFQUFFLGFBQWEsRUFBRSxHQUFHLEtBQUssQ0FBQztRQUNoQyxPQUFPLENBQUMsQ0FBQyxDQUFDLGFBQWEsSUFBSSxVQUFVLENBQUMsZ0JBQWdCLENBQUMsYUFBYSxDQUFDLENBQUMsQ0FBQztJQUN6RSxDQUFDLENBQUM7SUFFRixNQUFNLFVBQVUsR0FBRyxHQUFHLEVBQUU7UUFDdEIsTUFBTSxFQUFFLGFBQWEsRUFBRSxHQUFHLEtBQUssQ0FBQztRQUNoQyxJQUFJLENBQUMsYUFBYSxFQUFFO1lBQ2xCLE9BQU8sS0FBSyxDQUFDO1NBQ2Q7UUFDRCxNQUFNLE9BQU8sR0FBRyxVQUFVLENBQUMsZ0JBQWdCLENBQUMsYUFBYSxDQUFDLENBQUM7UUFDM0QsT0FBTyxDQUFDLENBQUMsQ0FDUCxPQUFPO1lBQ1AsT0FBTyxDQUFDLGFBQWE7WUFDckIsT0FBTyxDQUFDLGFBQWEsQ0FBQyxRQUFRLENBQy9CLENBQUM7SUFDSixDQUFDLENBQUM7SUFFRiw4RUFBOEU7SUFDOUUsSUFBSSxRQUFRLEVBQUU7UUFDWixjQUFjLENBQUMsR0FBRyxFQUFFLFVBQVUsRUFBRSxRQUFRLEVBQUUsTUFBTSxFQUFFLFVBQVUsQ0FBQyxDQUFDO0tBQy9EO0lBRUQsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsVUFBVSxFQUFFO1FBQ3pDLEtBQUssRUFBRSxHQUFHLEVBQUUsQ0FBQyxVQUFVLFFBQVEsQ0FBQyxLQUFLLENBQUMsYUFBYSxFQUFFLFVBQVUsQ0FBQyxFQUFFO1FBQ2xFLE9BQU8sRUFBRSxJQUFJLENBQUMsRUFBRTtZQUNkLE1BQU0sSUFBSSxHQUNSLE9BQU8sSUFBSSxDQUFDLE1BQU0sQ0FBQyxLQUFLLFdBQVcsQ0FBQyxDQUFDLENBQUMsRUFBRSxDQUFDLENBQUMsQ0FBRSxJQUFJLENBQUMsTUFBTSxDQUFZLENBQUM7WUFFdEUsSUFBSSxDQUFDLElBQUksRUFBRTtnQkFDVCxNQUFNLE9BQU8sR0FBRyxVQUFVLENBQUMsVUFBVSxDQUFDO2dCQUN0QyxNQUFNLElBQUksS0FBSyxDQUFDLG9DQUFvQyxPQUFPLEdBQUcsQ0FBQyxDQUFDO2FBQ2pFO1lBQ0QsT0FBTyxVQUFVLENBQUMsVUFBVSxDQUFDLElBQUksQ0FBQyxDQUFDO1FBQ3JDLENBQUM7S0FDRixDQUFDLENBQUM7SUFFSCxRQUFRLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyxXQUFXLEVBQUU7UUFDMUMsT0FBTyxFQUFFLElBQUksQ0FBQyxFQUFFO1lBQ2QsTUFBTSxVQUFVLEdBQUksSUFBSSxDQUFDLE9BQU8sQ0FBWSxJQUFJLEtBQUssQ0FBQyxFQUFFLENBQUMsT0FBTyxDQUFDLENBQUM7WUFDbEUsTUFBTSxJQUFJLEdBQ1IsT0FBTyxJQUFJLENBQUMsTUFBTSxDQUFDLEtBQUssV0FBVyxDQUFDLENBQUMsQ0FBQyxFQUFFLENBQUMsQ0FBQyxDQUFFLElBQUksQ0FBQyxNQUFNLENBQVksQ0FBQztZQUN0RSxNQUFNLE9BQU8sR0FBcUM7Z0JBQ2hELElBQUksRUFBRSxJQUFJLENBQUMsTUFBTSxDQUF5QjtnQkFDMUMsSUFBSTthQUNMLENBQUM7WUFFRixJQUFJLElBQUksQ0FBQyxNQUFNLENBQUMsS0FBSyxNQUFNLEVBQUU7Z0JBQzNCLE9BQU8sQ0FBQyxHQUFHLEdBQUksSUFBSSxDQUFDLEtBQUssQ0FBWSxJQUFJLE1BQU0sQ0FBQzthQUNqRDtZQUVELE9BQU8sVUFBVSxDQUFDLFFBQVEsQ0FBQyxRQUFRO2lCQUNoQyxXQUFXLENBQUMsT0FBTyxDQUFDO2lCQUNwQixLQUFLLENBQUMsS0FBSyxDQUFDLEVBQUUsQ0FBQyxzRUFBZ0IsQ0FBQyxVQUFVLEVBQUUsS0FBSyxDQUFDLENBQUMsQ0FBQztRQUN6RCxDQUFDO1FBQ0QsS0FBSyxFQUFFLElBQUksQ0FBQyxFQUFFLENBQUUsSUFBSSxDQUFDLE9BQU8sQ0FBWSxJQUFJLE9BQU8sSUFBSSxDQUFDLE1BQU0sQ0FBVyxFQUFFO0tBQzVFLENBQUMsQ0FBQztJQUVILFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLElBQUksRUFBRTtRQUNuQyxPQUFPLEVBQUUsSUFBSSxDQUFDLEVBQUU7WUFDZCxNQUFNLElBQUksR0FDUixPQUFPLElBQUksQ0FBQyxNQUFNLENBQUMsS0FBSyxXQUFXLENBQUMsQ0FBQyxDQUFDLEVBQUUsQ0FBQyxDQUFDLENBQUUsSUFBSSxDQUFDLE1BQU0sQ0FBWSxDQUFDO1lBQ3RFLE1BQU0sT0FBTyxHQUFJLElBQUksQ0FBQyxTQUFTLENBQVksSUFBSSxLQUFLLENBQUMsQ0FBQztZQUN0RCxNQUFNLE1BQU0sR0FBRyxJQUFJLGFBQUosSUFBSSx1QkFBSixJQUFJLENBQUUsTUFBOEMsQ0FBQztZQUNwRSxNQUFNLE9BQU8sR0FDVixJQUFJLENBQUMsU0FBUyxDQUFtQyxJQUFJLEtBQUssQ0FBQyxDQUFDO1lBQy9ELE9BQU8sVUFBVSxDQUFDLFFBQVEsQ0FBQyxRQUFRO2lCQUNoQyxHQUFHLENBQUMsSUFBSSxFQUFFLEVBQUUsT0FBTyxFQUFFLEtBQUssRUFBRSxDQUFDO2lCQUM3QixJQUFJLENBQUMsR0FBRyxFQUFFLENBQUMsVUFBVSxDQUFDLFlBQVksQ0FBQyxJQUFJLEVBQUUsT0FBTyxFQUFFLE1BQU0sRUFBRSxPQUFPLENBQUMsQ0FBQyxDQUFDO1FBQ3pFLENBQUM7UUFDRCxJQUFJLEVBQUUsSUFBSSxDQUFDLEVBQUUsQ0FBRSxJQUFJLENBQUMsTUFBTSxDQUFZLElBQUksRUFBRTtRQUM1QyxLQUFLLEVBQUUsSUFBSSxDQUFDLEVBQUU7O1lBQ1osUUFBQyxPQUFDLElBQUksQ0FBQyxPQUFPLENBQUMsSUFBSSxJQUFJLENBQUMsU0FBUyxDQUFDLENBQUMsbUNBQ2pDLEtBQUssQ0FBQyxFQUFFLENBQUMsMkJBQTJCLENBQUMsQ0FBVztTQUFBO1FBQ3BELFFBQVEsRUFBRSxJQUFJLENBQUMsRUFBRSxDQUFFLElBQUksQ0FBQyxVQUFVLENBQVksSUFBSSxDQUFDLENBQUM7S0FDckQsQ0FBQyxDQUFDO0lBRUgsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsTUFBTSxFQUFFO1FBQ3JDLEtBQUssRUFBRSxHQUFHLEVBQUUsQ0FDVixLQUFLLENBQUMsRUFBRSxDQUNOLHFCQUFxQixFQUNyQixRQUFRLENBQUMsS0FBSyxDQUFDLGFBQWEsRUFBRSxVQUFVLENBQUMsQ0FDMUM7UUFDSCxPQUFPLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQywyQkFBMkIsQ0FBQztRQUM5QyxTQUFTO1FBQ1QsT0FBTyxFQUFFLEdBQUcsRUFBRTtZQUNaLDRDQUE0QztZQUM1QyxJQUFJLENBQUMsU0FBUyxFQUFFLEVBQUU7Z0JBQ2hCLE9BQU87YUFDUjtZQUNELE1BQU0sT0FBTyxHQUFHLFVBQVUsQ0FBQyxnQkFBZ0IsQ0FBQyxLQUFLLENBQUMsYUFBYyxDQUFDLENBQUM7WUFDbEUsTUFBTSxJQUFJLEdBQUcsUUFBUSxDQUFDLEtBQUssQ0FBQyxhQUFjLEVBQUUsVUFBVSxDQUFDLENBQUM7WUFDeEQsSUFBSSxDQUFDLE9BQU8sRUFBRTtnQkFDWixPQUFPLGdFQUFVLENBQUM7b0JBQ2hCLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLGVBQWUsQ0FBQztvQkFDaEMsSUFBSSxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsc0NBQXNDLENBQUM7b0JBQ3RELE9BQU8sRUFBRSxDQUFDLGlFQUFlLEVBQUUsQ0FBQztpQkFDN0IsQ0FBQyxDQUFDO2FBQ0o7WUFDRCxJQUFJLE9BQU8sQ0FBQyxLQUFLLENBQUMsS0FBSyxFQUFFO2dCQUN2QixPQUFPLGdFQUFVLENBQUM7b0JBQ2hCLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLHFCQUFxQixFQUFFLElBQUksQ0FBQztvQkFDNUMsSUFBSSxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQ1osdURBQXVELEVBQ3ZELElBQUksQ0FDTDtvQkFDRCxPQUFPLEVBQUU7d0JBQ1AscUVBQW1CLEVBQUU7d0JBQ3JCLG1FQUFpQixDQUFDLEVBQUUsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsUUFBUSxDQUFDLEVBQUUsQ0FBQztxQkFDakQ7aUJBQ0YsQ0FBQyxDQUFDLElBQUksQ0FBQyxNQUFNLENBQUMsRUFBRTtvQkFDZixJQUFJLE1BQU0sQ0FBQyxNQUFNLENBQUMsTUFBTSxJQUFJLENBQUMsT0FBTyxDQUFDLFVBQVUsRUFBRTt3QkFDL0MsT0FBTyxPQUFPLENBQUMsTUFBTSxFQUFFLENBQUM7cUJBQ3pCO2dCQUNILENBQUMsQ0FBQyxDQUFDO2FBQ0o7aUJBQU07Z0JBQ0wsSUFBSSxDQUFDLE9BQU8sQ0FBQyxVQUFVLEVBQUU7b0JBQ3ZCLE9BQU8sT0FBTyxDQUFDLE1BQU0sRUFBRSxDQUFDO2lCQUN6QjthQUNGO1FBQ0gsQ0FBQztLQUNGLENBQUMsQ0FBQztJQUVILFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLGlCQUFpQixFQUFFO1FBQ2hELEtBQUssRUFBRSxHQUFHLEVBQUUsQ0FDVixLQUFLLENBQUMsRUFBRSxDQUNOLDBCQUEwQixFQUMxQixRQUFRLENBQUMsS0FBSyxDQUFDLGFBQWEsRUFBRSxVQUFVLENBQUMsQ0FDMUM7UUFDSCxPQUFPLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyx3Q0FBd0MsQ0FBQztRQUMzRCxTQUFTO1FBQ1QsT0FBTyxFQUFFLEdBQUcsRUFBRTtZQUNaLDRDQUE0QztZQUM1QyxJQUFJLENBQUMsU0FBUyxFQUFFLEVBQUU7Z0JBQ2hCLE9BQU87YUFDUjtZQUNELE1BQU0sT0FBTyxHQUFHLFVBQVUsQ0FBQyxnQkFBZ0IsQ0FBQyxLQUFLLENBQUMsYUFBYyxDQUFDLENBQUM7WUFDbEUsSUFBSSxDQUFDLE9BQU8sRUFBRTtnQkFDWixPQUFPLGdFQUFVLENBQUM7b0JBQ2hCLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLGVBQWUsQ0FBQztvQkFDaEMsSUFBSSxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsc0NBQXNDLENBQUM7b0JBQ3RELE9BQU8sRUFBRSxDQUFDLGlFQUFlLEVBQUUsQ0FBQztpQkFDN0IsQ0FBQyxDQUFDO2FBQ0o7WUFDRCxPQUFPLE9BQU8sQ0FBQyxlQUFlLEVBQUUsQ0FBQyxJQUFJLENBQUMsS0FBSyxFQUFDLFdBQVcsRUFBQyxFQUFFO2dCQUN4RCxNQUFNLElBQUksR0FBRyxRQUFRLENBQUMsS0FBSyxDQUFDLGFBQWEsRUFBRSxVQUFVLENBQUMsQ0FBQztnQkFDdkQsSUFBSSxXQUFXLENBQUMsTUFBTSxHQUFHLENBQUMsRUFBRTtvQkFDMUIsTUFBTSxzRUFBZ0IsQ0FDcEIsS0FBSyxDQUFDLEVBQUUsQ0FBQyxnQkFBZ0IsQ0FBQyxFQUMxQixLQUFLLENBQUMsRUFBRSxDQUFDLDJDQUEyQyxFQUFFLElBQUksQ0FBQyxDQUM1RCxDQUFDO29CQUNGLE9BQU87aUJBQ1I7Z0JBQ0QsTUFBTSxnQkFBZ0IsR0FDcEIsV0FBVyxDQUFDLE1BQU0sS0FBSyxDQUFDO29CQUN0QixDQUFDLENBQUMsV0FBVyxDQUFDLENBQUMsQ0FBQztvQkFDaEIsQ0FBQyxDQUFDLE1BQU0sT0FBTyxDQUFDLG1CQUFtQixDQUFDLFdBQVcsQ0FBQyxPQUFPLEVBQUUsRUFBRSxLQUFLLENBQUMsQ0FBQztnQkFFdEUsSUFBSSxDQUFDLGdCQUFnQixFQUFFO29CQUNyQixPQUFPO2lCQUNSO2dCQUNELE9BQU8sZ0VBQVUsQ0FBQztvQkFDaEIsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMseUJBQXlCLEVBQUUsSUFBSSxDQUFDO29CQUNoRCxJQUFJLEVBQUUsSUFBSSxtQkFBbUIsQ0FBQyxnQkFBZ0IsRUFBRSxLQUFLLEVBQUUsSUFBSSxDQUFDO29CQUM1RCxPQUFPLEVBQUU7d0JBQ1AscUVBQW1CLEVBQUU7d0JBQ3JCLG1FQUFpQixDQUFDLEVBQUUsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsUUFBUSxDQUFDLEVBQUUsQ0FBQztxQkFDakQ7aUJBQ0YsQ0FBQyxDQUFDLElBQUksQ0FBQyxNQUFNLENBQUMsRUFBRTtvQkFDZixJQUFJLE9BQU8sQ0FBQyxVQUFVLEVBQUU7d0JBQ3RCLE9BQU87cUJBQ1I7b0JBQ0QsSUFBSSxNQUFNLENBQUMsTUFBTSxDQUFDLE1BQU0sRUFBRTt3QkFDeEIsSUFBSSxPQUFPLENBQUMsS0FBSyxDQUFDLFFBQVEsRUFBRTs0QkFDMUIsT0FBTyxPQUFPLENBQUMsTUFBTSxFQUFFLENBQUM7eUJBQ3pCO3dCQUNELE9BQU8sT0FBTzs2QkFDWCxpQkFBaUIsQ0FBQyxnQkFBZ0IsQ0FBQyxFQUFFLENBQUM7NkJBQ3RDLElBQUksQ0FBQyxHQUFHLEVBQUUsQ0FBQyxPQUFPLENBQUMsTUFBTSxFQUFFLENBQUMsQ0FBQztxQkFDakM7Z0JBQ0gsQ0FBQyxDQUFDLENBQUM7WUFDTCxDQUFDLENBQUMsQ0FBQztRQUNMLENBQUM7S0FDRixDQUFDLENBQUM7SUFFSCxNQUFNLE9BQU8sR0FBRyxHQUFHLEVBQUU7UUFDbkIsSUFBSSx1RUFBb0IsQ0FBQyxlQUFlLENBQUMsSUFBSSxNQUFNLEVBQUU7WUFDbkQsT0FBTyxLQUFLLENBQUMsRUFBRSxDQUNiLCtFQUErRSxDQUNoRixDQUFDO1NBQ0g7YUFBTTtZQUNMLE9BQU8sS0FBSyxDQUFDLEVBQUUsQ0FBQyw0QkFBNEIsQ0FBQyxDQUFDO1NBQy9DO0lBQ0gsQ0FBQyxDQUFDO0lBRUYsTUFBTSxjQUFjLEdBQUcsSUFBSSxPQUFPLEVBQTRCLENBQUM7SUFFL0QsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsSUFBSSxFQUFFO1FBQ25DLEtBQUssRUFBRSxHQUFHLEVBQUUsQ0FBQyxLQUFLLENBQUMsRUFBRSxDQUFDLFNBQVMsRUFBRSxRQUFRLENBQUMsS0FBSyxDQUFDLGFBQWEsRUFBRSxVQUFVLENBQUMsQ0FBQztRQUMzRSxPQUFPO1FBQ1AsSUFBSSxFQUFFLElBQUksQ0FBQyxFQUFFLENBQUMsQ0FBQyxJQUFJLENBQUMsT0FBTyxDQUFDLENBQUMsQ0FBQywrREFBUSxDQUFDLENBQUMsQ0FBQyxFQUFFLENBQUM7UUFDNUMsU0FBUyxFQUFFLFVBQVU7UUFDckIsT0FBTyxFQUFFLEtBQUssSUFBSSxFQUFFOztZQUNsQiw0Q0FBNEM7WUFDNUMsSUFBSSxTQUFTLEVBQUUsRUFBRTtnQkFDZixNQUFNLE1BQU0sR0FBRyxLQUFLLENBQUMsYUFBYSxDQUFDO2dCQUNuQyxNQUFNLE9BQU8sR0FBRyxVQUFVLENBQUMsZ0JBQWdCLENBQUMsTUFBTyxDQUFDLENBQUM7Z0JBQ3JELElBQUksQ0FBQyxPQUFPLEVBQUU7b0JBQ1osT0FBTyxnRUFBVSxDQUFDO3dCQUNoQixLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxhQUFhLENBQUM7d0JBQzlCLElBQUksRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLHNDQUFzQyxDQUFDO3dCQUN0RCxPQUFPLEVBQUUsQ0FBQyxpRUFBZSxFQUFFLENBQUM7cUJBQzdCLENBQUMsQ0FBQztpQkFDSjtxQkFBTTtvQkFDTCxJQUFJLGNBQWMsQ0FBQyxHQUFHLENBQUMsT0FBTyxDQUFDLEVBQUU7d0JBQy9CLE9BQU87cUJBQ1I7b0JBRUQsSUFBSSxPQUFPLENBQUMsS0FBSyxDQUFDLFFBQVEsRUFBRTt3QkFDMUIsT0FBTyxnRUFBVSxDQUFDOzRCQUNoQixLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxhQUFhLENBQUM7NEJBQzlCLElBQUksRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLHVCQUF1QixDQUFDOzRCQUN2QyxPQUFPLEVBQUUsQ0FBQyxpRUFBZSxFQUFFLENBQUM7eUJBQzdCLENBQUMsQ0FBQztxQkFDSjtvQkFFRCxjQUFjLENBQUMsR0FBRyxDQUFDLE9BQU8sQ0FBQyxDQUFDO29CQUU1QixNQUFNLE9BQU8sR0FBRyxtRUFBZ0IsQ0FBQyxtQkFBTyxDQUFDLGFBQWEsMENBQUUsSUFBSSxtQ0FBSSxFQUFFLENBQUMsQ0FBQztvQkFDcEUsSUFBSSxPQUFPLEdBQUcsT0FBTyxDQUFDO29CQUV0QixJQUNFLFVBQVUsQ0FBQyx3QkFBd0I7d0JBQ2xDLE1BQTBCLENBQUMsVUFBVSxLQUFLLElBQUksRUFDL0M7d0JBQ0EsTUFBTSxNQUFNLEdBQUcsTUFBTSxxRUFBbUIsQ0FBQzs0QkFDdkMsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsYUFBYSxDQUFDOzRCQUM5QixPQUFPLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxRQUFRLENBQUM7NEJBQzNCLFdBQVcsRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLFdBQVcsQ0FBQzs0QkFDbEMsSUFBSSxFQUFFLE9BQU87NEJBQ2IsY0FBYyxFQUFFLE9BQU8sQ0FBQyxNQUFNLEdBQUcsa0VBQWUsQ0FBQyxPQUFPLENBQUMsQ0FBQyxNQUFNOzRCQUNoRSxRQUFRLEVBQUU7Z0NBQ1IsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMscUJBQXFCLENBQUM7Z0NBQ3RDLE9BQU8sRUFBRSxLQUFLLENBQUMsRUFBRSxDQUNmLHFGQUFxRixDQUN0Rjs2QkFDRjt5QkFDRixDQUFDLENBQUM7d0JBRUgsSUFBSSxNQUFNLENBQUMsTUFBTSxDQUFDLE1BQU0sRUFBRTs0QkFDeEIsT0FBTyxHQUFHLFlBQU0sQ0FBQyxLQUFLLG1DQUFJLE9BQU8sQ0FBQzs0QkFDakMsTUFBMEIsQ0FBQyxVQUFVLEdBQUcsS0FBSyxDQUFDOzRCQUMvQyxJQUFJLE9BQU8sTUFBTSxDQUFDLFNBQVMsS0FBSyxTQUFTLEVBQUU7Z0NBQ3pDLE1BQU0sY0FBYyxHQUFHLENBQ3JCLE1BQU0sZUFBZSxDQUFDLEdBQUcsQ0FDdkIsa0JBQWtCLEVBQ2xCLDBCQUEwQixDQUMzQixDQUNGLENBQUMsU0FBb0IsQ0FBQztnQ0FDdkIsSUFBSSxNQUFNLENBQUMsU0FBUyxLQUFLLGNBQWMsRUFBRTtvQ0FDdkMsZUFBZTt5Q0FDWixHQUFHLENBQ0Ysa0JBQWtCLEVBQ2xCLDBCQUEwQixFQUMxQixDQUFDLE1BQU0sQ0FBQyxTQUFTLENBQ2xCO3lDQUNBLEtBQUssQ0FBQyxNQUFNLENBQUMsRUFBRTt3Q0FDZCxPQUFPLENBQUMsS0FBSyxDQUNYLDJDQUEyQyxNQUFNLEVBQUUsQ0FDcEQsQ0FBQztvQ0FDSixDQUFDLENBQUMsQ0FBQztpQ0FDTjs2QkFDRjt5QkFDRjtxQkFDRjtvQkFFRCxJQUFJO3dCQUNGLE1BQU0sT0FBTyxDQUFDLElBQUksRUFBRSxDQUFDO3dCQUVyQixJQUFJLENBQUMsT0FBTSxhQUFOLE1BQU0sdUJBQU4sTUFBTSxDQUFFLFVBQVUsR0FBRTs0QkFDdkIsT0FBTyxPQUFRLENBQUMsZ0JBQWdCLEVBQUUsQ0FBQzt5QkFDcEM7cUJBQ0Y7b0JBQUMsT0FBTyxHQUFHLEVBQUU7d0JBQ1osdURBQXVEO3dCQUN2RCxJQUFJLEdBQUcsQ0FBQyxJQUFJLEtBQUssa0JBQWtCLEVBQUU7NEJBQ25DLE9BQU87eUJBQ1I7d0JBQ0QsTUFBTSxHQUFHLENBQUM7cUJBQ1g7NEJBQVM7d0JBQ1IsY0FBYyxDQUFDLE1BQU0sQ0FBQyxPQUFPLENBQUMsQ0FBQzt3QkFDL0IsSUFBSSxPQUFPLEtBQUssT0FBTyxFQUFFOzRCQUN2QixNQUFNLE9BQU8sQ0FBQyxNQUFNLENBQUMsT0FBTyxDQUFDLENBQUM7eUJBQy9CO3FCQUNGO2lCQUNGO2FBQ0Y7UUFDSCxDQUFDO0tBQ0YsQ0FBQyxDQUFDO0lBRUgsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsT0FBTyxFQUFFO1FBQ3RDLEtBQUssRUFBRSxHQUFHLEVBQUUsQ0FBQyxLQUFLLENBQUMsRUFBRSxDQUFDLFVBQVUsQ0FBQztRQUNqQyxPQUFPLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyx5QkFBeUIsQ0FBQztRQUM1QyxTQUFTLEVBQUUsR0FBRyxFQUFFO1lBQ2QsT0FBTyx1REFBSSxDQUNULHNEQUFHLENBQUMsS0FBSyxDQUFDLE9BQU8sQ0FBQyxNQUFNLENBQUMsRUFBRSxDQUFDLENBQUMsRUFBRSxDQUFDLFVBQVUsQ0FBQyxnQkFBZ0IsQ0FBQyxDQUFDLENBQUMsQ0FBQyxFQUMvRCxDQUFDLENBQUMsRUFBRSxlQUFDLG9CQUFDLGFBQUQsQ0FBQyx1QkFBRCxDQUFDLENBQUUsYUFBYSwwQ0FBRSxRQUFRLG1DQUFJLEtBQUssSUFDekMsQ0FBQztRQUNKLENBQUM7UUFDRCxPQUFPLEVBQUUsR0FBRyxFQUFFO1lBQ1osTUFBTSxRQUFRLEdBQW9CLEVBQUUsQ0FBQztZQUNyQyxNQUFNLEtBQUssR0FBRyxJQUFJLEdBQUcsRUFBVSxDQUFDLENBQUMsdUNBQXVDO1lBQ3hFLHVEQUFJLENBQUMsS0FBSyxDQUFDLE9BQU8sQ0FBQyxNQUFNLENBQUMsRUFBRSxNQUFNLENBQUMsRUFBRTtnQkFDbkMsTUFBTSxPQUFPLEdBQUcsVUFBVSxDQUFDLGdCQUFnQixDQUFDLE1BQU0sQ0FBQyxDQUFDO2dCQUNwRCxJQUFJLE9BQU8sSUFBSSxDQUFDLE9BQU8sQ0FBQyxLQUFLLENBQUMsUUFBUSxJQUFJLENBQUMsS0FBSyxDQUFDLEdBQUcsQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLEVBQUU7b0JBQ2xFLEtBQUssQ0FBQyxHQUFHLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxDQUFDO29CQUN4QixRQUFRLENBQUMsSUFBSSxDQUFDLE9BQU8sQ0FBQyxJQUFJLEVBQUUsQ0FBQyxDQUFDO2lCQUMvQjtZQUNILENBQUMsQ0FBQyxDQUFDO1lBQ0gsT0FBTyxPQUFPLENBQUMsR0FBRyxDQUFDLFFBQVEsQ0FBQyxDQUFDO1FBQy9CLENBQUM7S0FDRixDQUFDLENBQUM7SUFFSCxRQUFRLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyxNQUFNLEVBQUU7UUFDckMsS0FBSyxFQUFFLEdBQUcsRUFBRSxDQUNWLEtBQUssQ0FBQyxFQUFFLENBQUMsYUFBYSxFQUFFLFFBQVEsQ0FBQyxLQUFLLENBQUMsYUFBYSxFQUFFLFVBQVUsQ0FBQyxDQUFDO1FBQ3BFLE9BQU8sRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLG9CQUFvQixDQUFDO1FBQ3ZDLFNBQVM7UUFDVCxPQUFPLEVBQUUsR0FBRyxFQUFFO1lBQ1osNENBQTRDO1lBQzVDLElBQUksU0FBUyxFQUFFLEVBQUU7Z0JBQ2YsTUFBTSxPQUFPLEdBQUcsVUFBVSxDQUFDLGdCQUFnQixDQUFDLEtBQUssQ0FBQyxhQUFjLENBQUMsQ0FBQztnQkFDbEUsSUFBSSxDQUFDLE9BQU8sRUFBRTtvQkFDWixPQUFPLGdFQUFVLENBQUM7d0JBQ2hCLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLGFBQWEsQ0FBQzt3QkFDOUIsSUFBSSxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsc0NBQXNDLENBQUM7d0JBQ3RELE9BQU8sRUFBRSxDQUFDLGlFQUFlLEVBQUUsQ0FBQztxQkFDN0IsQ0FBQyxDQUFDO2lCQUNKO2dCQUNELE9BQU8sT0FBTyxDQUFDLE1BQU0sRUFBRSxDQUFDO2FBQ3pCO1FBQ0gsQ0FBQztLQUNGLENBQUMsQ0FBQztJQUVILFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLGNBQWMsRUFBRTtRQUM3QyxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxvQkFBb0IsQ0FBQztRQUNyQyxTQUFTLEVBQUUsR0FBRyxFQUFFLENBQUMsVUFBVSxDQUFDLFFBQVE7UUFDcEMsT0FBTyxFQUFFLEdBQUcsRUFBRTtZQUNaLE1BQU0sS0FBSyxHQUFHLENBQUMsVUFBVSxDQUFDLFFBQVEsQ0FBQztZQUNuQyxNQUFNLEdBQUcsR0FBRyxVQUFVLENBQUM7WUFDdkIsT0FBTyxlQUFlO2lCQUNuQixHQUFHLENBQUMsa0JBQWtCLEVBQUUsR0FBRyxFQUFFLEtBQUssQ0FBQztpQkFDbkMsS0FBSyxDQUFDLENBQUMsTUFBYSxFQUFFLEVBQUU7Z0JBQ3ZCLE9BQU8sQ0FBQyxLQUFLLENBQ1gsaUJBQWlCLGtCQUFrQixJQUFJLEdBQUcsTUFBTSxNQUFNLENBQUMsT0FBTyxFQUFFLENBQ2pFLENBQUM7WUFDSixDQUFDLENBQUMsQ0FBQztRQUNQLENBQUM7S0FDRixDQUFDLENBQUM7SUFFSCxJQUFJLE9BQU8sRUFBRTtRQUNYO1lBQ0UsVUFBVSxDQUFDLE1BQU07WUFDakIsVUFBVSxDQUFDLGlCQUFpQjtZQUM1QixVQUFVLENBQUMsSUFBSTtZQUNmLFVBQVUsQ0FBQyxNQUFNO1lBQ2pCLFVBQVUsQ0FBQyxjQUFjO1lBQ3pCLFVBQVUsQ0FBQyxTQUFTO1NBQ3JCLENBQUMsT0FBTyxDQUFDLE9BQU8sQ0FBQyxFQUFFO1lBQ2xCLE9BQU8sQ0FBQyxPQUFPLENBQUMsRUFBRSxPQUFPLEVBQUUsUUFBUSxFQUFFLENBQUMsQ0FBQztRQUN6QyxDQUFDLENBQUMsQ0FBQztLQUNKO0FBQ0gsQ0FBQztBQUVELFNBQVMsY0FBYyxDQUNyQixHQUFvQixFQUNwQixVQUE0QixFQUM1QixRQUFtQixFQUNuQixNQUFxQyxFQUNyQyxVQUF1QjtJQUV2QixNQUFNLEtBQUssR0FBRyxVQUFVLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FBQyxDQUFDO0lBQzVDLE1BQU0sRUFBRSxRQUFRLEVBQUUsR0FBRyxHQUFHLENBQUM7SUFFekIsNEVBQTRFO0lBQzVFLE1BQU0saUJBQWlCLEdBQUcsR0FBa0IsRUFBRTs7UUFDNUMsTUFBTSxNQUFNLEdBQUcsb0JBQW9CLENBQUM7UUFDcEMsTUFBTSxJQUFJLEdBQUcsQ0FBQyxJQUFpQixFQUFFLEVBQUUsV0FBQyxRQUFDLENBQUMsV0FBSSxDQUFDLE9BQU8sQ0FBQywwQ0FBRSxLQUFLLENBQUMsTUFBTSxDQUFDLEtBQUM7UUFDbkUsTUFBTSxJQUFJLEdBQUcsR0FBRyxDQUFDLGtCQUFrQixDQUFDLElBQUksQ0FBQyxDQUFDO1FBRTFDLE1BQU0sU0FBUyxHQUFHLElBQUksYUFBSixJQUFJLHVCQUFKLElBQUksQ0FBRyxPQUFPLEVBQUUsS0FBSyxDQUFDLE1BQU0sQ0FBQyxDQUFDO1FBQ2hELE9BQU8sQ0FDTCxPQUFDLFNBQVMsSUFBSSxVQUFVLENBQUMsVUFBVSxDQUFDLFNBQVMsQ0FBQyxDQUFDLENBQUMsRUFBRSxJQUFJLENBQUMsQ0FBQztRQUN4RCx3RUFBd0U7UUFDeEUsUUFBUSxDQUFDLGFBQWEsQ0FDdkIsQ0FBQztJQUNKLENBQUMsQ0FBQztJQUVGLCtEQUErRDtJQUMvRCxNQUFNLFNBQVMsR0FBRyxHQUFHLEVBQUU7UUFDckIsTUFBTSxFQUFFLGFBQWEsRUFBRSxHQUFHLFFBQVEsQ0FBQztRQUNuQyxPQUFPLENBQUMsQ0FBQyxDQUFDLGFBQWEsSUFBSSxVQUFVLENBQUMsZ0JBQWdCLENBQUMsYUFBYSxDQUFDLENBQUMsQ0FBQztJQUN6RSxDQUFDLENBQUM7SUFFRixRQUFRLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyxLQUFLLEVBQUU7UUFDcEMsS0FBSyxFQUFFLEdBQUcsRUFBRSxDQUNWLEtBQUssQ0FBQyxFQUFFLENBQUMsaUJBQWlCLEVBQUUsUUFBUSxDQUFDLGlCQUFpQixFQUFFLEVBQUUsVUFBVSxDQUFDLENBQUM7UUFDeEUsU0FBUztRQUNULE9BQU8sRUFBRSxJQUFJLENBQUMsRUFBRTtZQUNkLE1BQU0sTUFBTSxHQUFHLGlCQUFpQixFQUFFLENBQUM7WUFDbkMsTUFBTSxPQUFPLEdBQUksSUFBSSxDQUFDLFNBQVMsQ0FBbUMsSUFBSTtnQkFDcEUsSUFBSSxFQUFFLGFBQWE7YUFDcEIsQ0FBQztZQUNGLElBQUksQ0FBQyxNQUFNLEVBQUU7Z0JBQ1gsT0FBTzthQUNSO1lBQ0Qsb0JBQW9CO1lBQ3BCLE1BQU0sS0FBSyxHQUFHLFVBQVUsQ0FBQyxXQUFXLENBQUMsTUFBTSxDQUFDLENBQUM7WUFDN0MsSUFBSSxLQUFLLEVBQUU7Z0JBQ1QsTUFBTSxDQUFDLElBQUksQ0FBQyxLQUFLLEVBQUUsT0FBTyxDQUFDLENBQUM7YUFDN0I7UUFDSCxDQUFDO0tBQ0YsQ0FBQyxDQUFDO0lBRUgsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsTUFBTSxFQUFFO1FBQ3JDLEtBQUssRUFBRSxHQUFHLEVBQUU7WUFDVixJQUFJLENBQUMsR0FBRyxRQUFRLENBQUMsaUJBQWlCLEVBQUUsRUFBRSxVQUFVLENBQUMsQ0FBQztZQUNsRCxJQUFJLENBQUMsRUFBRTtnQkFDTCxDQUFDLEdBQUcsR0FBRyxHQUFHLENBQUMsQ0FBQzthQUNiO1lBQ0QsT0FBTyxLQUFLLENBQUMsRUFBRSxDQUFDLFdBQVcsRUFBRSxDQUFDLENBQUMsQ0FBQztRQUNsQyxDQUFDO1FBQ0QsU0FBUztRQUNULE9BQU8sRUFBRSxHQUFHLEVBQUU7WUFDWix1Q0FBdUM7WUFDdkMsSUFBSSxTQUFTLEVBQUUsRUFBRTtnQkFDZixNQUFNLE9BQU8sR0FBRyxVQUFVLENBQUMsZ0JBQWdCLENBQUMsaUJBQWlCLEVBQUcsQ0FBQyxDQUFDO2dCQUNsRSxPQUFPLG9FQUFZLENBQUMsVUFBVSxFQUFFLE9BQVEsQ0FBQyxDQUFDO2FBQzNDO1FBQ0gsQ0FBQztLQUNGLENBQUMsQ0FBQztJQUVILFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLFNBQVMsRUFBRTtRQUN4QyxLQUFLLEVBQUUsR0FBRyxFQUFFLENBQ1YsS0FBSyxDQUFDLEVBQUUsQ0FBQyxjQUFjLEVBQUUsUUFBUSxDQUFDLGlCQUFpQixFQUFFLEVBQUUsVUFBVSxDQUFDLENBQUM7UUFDckUsU0FBUztRQUNULE9BQU8sRUFBRSxHQUFHLEVBQUU7WUFDWixJQUFJLFNBQVMsRUFBRSxFQUFFO2dCQUNmLE1BQU0sT0FBTyxHQUFHLFVBQVUsQ0FBQyxnQkFBZ0IsQ0FBQyxpQkFBaUIsRUFBRyxDQUFDLENBQUM7Z0JBQ2xFLElBQUksQ0FBQyxPQUFPLEVBQUU7b0JBQ1osT0FBTztpQkFDUjtnQkFDRCxPQUFPLFVBQVUsQ0FBQyxTQUFTLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxDQUFDO2FBQzNDO1FBQ0gsQ0FBQztLQUNGLENBQUMsQ0FBQztJQUVILFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLEdBQUcsRUFBRTtRQUNsQyxLQUFLLEVBQUUsR0FBRyxFQUFFLENBQ1YsS0FBSyxDQUFDLEVBQUUsQ0FBQyxXQUFXLEVBQUUsUUFBUSxDQUFDLGlCQUFpQixFQUFFLEVBQUUsVUFBVSxDQUFDLENBQUM7UUFDbEUsU0FBUztRQUNULE9BQU8sRUFBRSxLQUFLLElBQUksRUFBRTtZQUNsQix1Q0FBdUM7WUFDdkMsSUFBSSxTQUFTLEVBQUUsRUFBRTtnQkFDZixNQUFNLE9BQU8sR0FBRyxVQUFVLENBQUMsZ0JBQWdCLENBQUMsaUJBQWlCLEVBQUcsQ0FBQyxDQUFDO2dCQUNsRSxJQUFJLENBQUMsT0FBTyxFQUFFO29CQUNaLE9BQU87aUJBQ1I7Z0JBQ0QsTUFBTSxNQUFNLEdBQUcsTUFBTSxnRUFBVSxDQUFDO29CQUM5QixLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxRQUFRLENBQUM7b0JBQ3pCLElBQUksRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLG9DQUFvQyxFQUFFLE9BQU8sQ0FBQyxJQUFJLENBQUM7b0JBQ2xFLE9BQU8sRUFBRTt3QkFDUCxxRUFBbUIsRUFBRTt3QkFDckIsbUVBQWlCLENBQUMsRUFBRSxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxRQUFRLENBQUMsRUFBRSxDQUFDO3FCQUNqRDtpQkFDRixDQUFDLENBQUM7Z0JBRUgsSUFBSSxNQUFNLENBQUMsTUFBTSxDQUFDLE1BQU0sRUFBRTtvQkFDeEIsTUFBTSxHQUFHLENBQUMsUUFBUSxDQUFDLE9BQU8sQ0FBQyx3QkFBd0IsRUFBRTt3QkFDbkQsSUFBSSxFQUFFLE9BQU8sQ0FBQyxJQUFJO3FCQUNuQixDQUFDLENBQUM7aUJBQ0o7YUFDRjtRQUNILENBQUM7S0FDRixDQUFDLENBQUM7SUFFSCxRQUFRLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyxpQkFBaUIsRUFBRTtRQUNoRCxLQUFLLEVBQUUsR0FBRyxFQUFFLENBQUMsS0FBSyxDQUFDLEVBQUUsQ0FBQyxzQkFBc0IsQ0FBQztRQUM3QyxTQUFTO1FBQ1QsT0FBTyxFQUFFLEtBQUssSUFBSSxFQUFFO1lBQ2xCLE1BQU0sTUFBTSxHQUFHLGlCQUFpQixFQUFFLENBQUM7WUFDbkMsTUFBTSxPQUFPLEdBQUcsTUFBTSxJQUFJLFVBQVUsQ0FBQyxnQkFBZ0IsQ0FBQyxNQUFNLENBQUMsQ0FBQztZQUM5RCxJQUFJLENBQUMsT0FBTyxFQUFFO2dCQUNaLE9BQU87YUFDUjtZQUVELDhFQUE4RTtZQUM5RSxNQUFNLFFBQVEsQ0FBQyxPQUFPLENBQUMsc0JBQXNCLEVBQUUsRUFBRSxJQUFJLEVBQUUsT0FBTyxDQUFDLElBQUksRUFBRSxDQUFDLENBQUM7WUFDdkUsTUFBTSxRQUFRLENBQUMsT0FBTyxDQUFDLHdCQUF3QixFQUFFLEVBQUUsSUFBSSxFQUFFLE9BQU8sQ0FBQyxJQUFJLEVBQUUsQ0FBQyxDQUFDO1FBQzNFLENBQUM7S0FDRixDQUFDLENBQUM7QUFDTCxDQUFDO0FBRUQ7O0dBRUc7QUFDSCxTQUFTLGFBQWEsQ0FDcEIsTUFBa0IsRUFDbEIsT0FBaUM7SUFFakMsSUFBSSxVQUFVLEdBQXVCLElBQUksQ0FBQztJQUMxQyxNQUFNLGNBQWMsR0FBRyxDQUFDLE1BQVcsRUFBRSxJQUF1QixFQUFFLEVBQUU7UUFDOUQsSUFBSSxJQUFJLENBQUMsSUFBSSxLQUFLLE9BQU8sRUFBRTtZQUN6QixJQUFJLElBQUksQ0FBQyxRQUFRLEtBQUssSUFBSSxFQUFFO2dCQUMxQixJQUFJLENBQUMsVUFBVSxFQUFFO29CQUNmLFVBQVUsR0FBRyxNQUFNLENBQUMsUUFBUSxFQUFFLENBQUM7aUJBQ2hDO2FBQ0Y7aUJBQU0sSUFBSSxVQUFVLEVBQUU7Z0JBQ3JCLFVBQVUsQ0FBQyxPQUFPLEVBQUUsQ0FBQztnQkFDckIsVUFBVSxHQUFHLElBQUksQ0FBQzthQUNuQjtTQUNGO0lBQ0gsQ0FBQyxDQUFDO0lBQ0YsS0FBSyxPQUFPLENBQUMsS0FBSyxDQUFDLElBQUksQ0FBQyxHQUFHLEVBQUU7UUFDM0IsT0FBTyxDQUFDLEtBQUssQ0FBQyxZQUFZLENBQUMsT0FBTyxDQUFDLGNBQWMsQ0FBQyxDQUFDO1FBQ25ELElBQUksT0FBTyxDQUFDLEtBQUssQ0FBQyxLQUFLLEVBQUU7WUFDdkIsVUFBVSxHQUFHLE1BQU0sQ0FBQyxRQUFRLEVBQUUsQ0FBQztTQUNoQztJQUNILENBQUMsQ0FBQyxDQUFDO0lBQ0gsT0FBTyxDQUFDLFFBQVEsQ0FBQyxPQUFPLENBQUMsR0FBRyxFQUFFO1FBQzVCLElBQUksVUFBVSxFQUFFO1lBQ2QsVUFBVSxDQUFDLE9BQU8sRUFBRSxDQUFDO1NBQ3RCO0lBQ0gsQ0FBQyxDQUFDLENBQUM7QUFDTCxDQUFDO0FBRUQ7O0dBRUc7QUFDSCxJQUFVLE9BQU8sQ0EwRWhCO0FBMUVELFdBQVUsT0FBTztJQUNmOztPQUVHO0lBQ1EsVUFBRSxHQUFHLENBQUMsQ0FBQztJQUVsQixTQUFnQix1QkFBdUIsQ0FDckMsVUFBcUMsRUFDckMsUUFBZ0IsRUFDaEIsS0FBd0I7UUFFeEIsTUFBTSxJQUFJLEdBQUcsUUFBUSxDQUFDLGFBQWEsQ0FBQyxLQUFLLENBQUMsQ0FBQztRQUMzQyxNQUFNLGNBQWMsR0FBRyxRQUFRLENBQUMsYUFBYSxDQUFDLEdBQUcsQ0FBQyxDQUFDO1FBQ25ELE1BQU0sV0FBVyxHQUFHLFFBQVEsQ0FBQyxjQUFjLENBQ3pDLEtBQUssQ0FBQyxFQUFFLENBQ04sd0RBQXdELEVBQ3hELFFBQVEsQ0FDVCxDQUNGLENBQUM7UUFDRixNQUFNLGNBQWMsR0FBRyxRQUFRLENBQUMsYUFBYSxDQUFDLFFBQVEsQ0FBQyxDQUFDO1FBQ3hELGNBQWMsQ0FBQyxXQUFXLEdBQUcsS0FBSyxDQUFDLEVBQUUsQ0FBQyx3QkFBd0IsQ0FBQyxDQUFDO1FBRWhFLGNBQWMsQ0FBQyxXQUFXLENBQUMsV0FBVyxDQUFDLENBQUM7UUFDeEMsY0FBYyxDQUFDLFdBQVcsQ0FBQyxjQUFjLENBQUMsQ0FBQztRQUUzQyxNQUFNLHFCQUFxQixHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUMsR0FBRyxDQUFDLENBQUM7UUFDMUQsTUFBTSxrQkFBa0IsR0FBRyxRQUFRLENBQUMsY0FBYyxDQUNoRCxLQUFLLENBQUMsRUFBRSxDQUFDLHNDQUFzQyxDQUFDLENBQ2pELENBQUM7UUFDRixNQUFNLGtCQUFrQixHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUMsR0FBRyxDQUFDLENBQUM7UUFDdkQsTUFBTSxJQUFJLEdBQUcsSUFBSSxJQUFJLENBQUMsVUFBVSxDQUFDLGFBQWEsQ0FBQyxDQUFDO1FBQ2hELGtCQUFrQixDQUFDLEtBQUssQ0FBQyxTQUFTLEdBQUcsUUFBUSxDQUFDO1FBQzlDLGtCQUFrQixDQUFDLFdBQVc7WUFDNUIsOERBQVcsQ0FBQyxJQUFJLEVBQUUsK0JBQStCLENBQUM7Z0JBQ2xELElBQUk7Z0JBQ0osbUVBQWdCLENBQUMsSUFBSSxDQUFDO2dCQUN0QixHQUFHLENBQUM7UUFFTixxQkFBcUIsQ0FBQyxXQUFXLENBQUMsa0JBQWtCLENBQUMsQ0FBQztRQUN0RCxxQkFBcUIsQ0FBQyxXQUFXLENBQUMsa0JBQWtCLENBQUMsQ0FBQztRQUV0RCxJQUFJLENBQUMsV0FBVyxDQUFDLGNBQWMsQ0FBQyxDQUFDO1FBQ2pDLElBQUksQ0FBQyxXQUFXLENBQUMscUJBQXFCLENBQUMsQ0FBQztRQUN4QyxPQUFPLElBQUksQ0FBQztJQUNkLENBQUM7SUF0Q2UsK0JBQXVCLDBCQXNDdEM7SUFFRDs7T0FFRztJQUNJLEtBQUssVUFBVSxtQkFBbUIsQ0FDdkMsV0FBd0MsRUFDeEMsS0FBd0I7UUFFeEIsNERBQTREO1FBQzVELE1BQU0sY0FBYyxHQUFHLEdBQUcsQ0FBQztRQUMzQixNQUFNLEtBQUssR0FBRyxXQUFXLENBQUMsR0FBRyxDQUFDLENBQUMsVUFBVSxFQUFFLEtBQUssRUFBRSxFQUFFO1lBQ2xELE1BQU0sT0FBTyxHQUFHLDhEQUFXLENBQUMsVUFBVSxDQUFDLGFBQWEsQ0FBQyxDQUFDO1lBQ3RELE1BQU0sU0FBUyxHQUFHLG1FQUFnQixDQUFDLFVBQVUsQ0FBQyxhQUFhLENBQUMsQ0FBQztZQUM3RCxPQUFPLEdBQUcsS0FBSyxHQUFHLGNBQWMsSUFBSSxPQUFPLEtBQUssU0FBUyxHQUFHLENBQUM7UUFDL0QsQ0FBQyxDQUFDLENBQUM7UUFFSCxNQUFNLFlBQVksR0FBRyxDQUNuQixNQUFNLHFFQUFtQixDQUFDO1lBQ3hCLEtBQUssRUFBRSxLQUFLO1lBQ1osS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMscUJBQXFCLENBQUM7U0FDdkMsQ0FBQyxDQUNILENBQUMsS0FBSyxDQUFDO1FBRVIsSUFBSSxDQUFDLFlBQVksRUFBRTtZQUNqQixPQUFPO1NBQ1I7UUFDRCxNQUFNLGFBQWEsR0FBRyxZQUFZLENBQUMsS0FBSyxDQUFDLGNBQWMsRUFBRSxDQUFDLENBQUMsQ0FBQyxDQUFDLENBQUMsQ0FBQztRQUMvRCxPQUFPLFdBQVcsQ0FBQyxRQUFRLENBQUMsYUFBYSxFQUFFLEVBQUUsQ0FBQyxDQUFDLENBQUM7SUFDbEQsQ0FBQztJQXhCcUIsMkJBQW1CLHNCQXdCeEM7QUFDSCxDQUFDLEVBMUVTLE9BQU8sS0FBUCxPQUFPLFFBMEVoQiIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9kb2NtYW5hZ2VyLWV4dGVuc2lvbi9zcmMvaW5kZXgudHN4Il0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGRvY21hbmFnZXItZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSUxhYlNoZWxsLFxuICBJTGFiU3RhdHVzLFxuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpbixcbiAgSnVweXRlckxhYlxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQge1xuICBhZGRDb21tYW5kVG9vbGJhckJ1dHRvbkNsYXNzLFxuICBDb21tYW5kVG9vbGJhckJ1dHRvbkNvbXBvbmVudCxcbiAgRGlhbG9nLFxuICBJQ29tbWFuZFBhbGV0dGUsXG4gIElucHV0RGlhbG9nLFxuICBJU2Vzc2lvbkNvbnRleHREaWFsb2dzLFxuICBSZWFjdFdpZGdldCxcbiAgc2hvd0RpYWxvZyxcbiAgc2hvd0Vycm9yTWVzc2FnZSxcbiAgVXNlU2lnbmFsXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IElDaGFuZ2VkQXJncywgUGFnZUNvbmZpZywgUGF0aEV4dCwgVGltZSB9IGZyb20gJ0BqdXB5dGVybGFiL2NvcmV1dGlscyc7XG5pbXBvcnQge1xuICBEb2N1bWVudE1hbmFnZXIsXG4gIElEb2N1bWVudE1hbmFnZXIsXG4gIFBhdGhTdGF0dXMsXG4gIHJlbmFtZURpYWxvZyxcbiAgU2F2aW5nU3RhdHVzXG59IGZyb20gJ0BqdXB5dGVybGFiL2RvY21hbmFnZXInO1xuaW1wb3J0IHsgSURvY3VtZW50UHJvdmlkZXJGYWN0b3J5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jcHJvdmlkZXInO1xuaW1wb3J0IHsgRG9jdW1lbnRSZWdpc3RyeSwgSURvY3VtZW50V2lkZ2V0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jcmVnaXN0cnknO1xuaW1wb3J0IHsgQ29udGVudHMsIEtlcm5lbCB9IGZyb20gJ0BqdXB5dGVybGFiL3NlcnZpY2VzJztcbmltcG9ydCB7IElTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHsgSVN0YXR1c0JhciB9IGZyb20gJ0BqdXB5dGVybGFiL3N0YXR1c2Jhcic7XG5pbXBvcnQge1xuICBJVHJhbnNsYXRvcixcbiAgbnVsbFRyYW5zbGF0b3IsXG4gIFRyYW5zbGF0aW9uQnVuZGxlXG59IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IHNhdmVJY29uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBlYWNoLCBtYXAsIHNvbWUsIHRvQXJyYXkgfSBmcm9tICdAbHVtaW5vL2FsZ29yaXRobSc7XG5pbXBvcnQgeyBDb21tYW5kUmVnaXN0cnkgfSBmcm9tICdAbHVtaW5vL2NvbW1hbmRzJztcbmltcG9ydCB7IEpTT05FeHQgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBJU2lnbmFsIH0gZnJvbSAnQGx1bWluby9zaWduYWxpbmcnO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCAqIGFzIFJlYWN0IGZyb20gJ3JlYWN0JztcblxuLyoqXG4gKiBUaGUgY29tbWFuZCBJRHMgdXNlZCBieSB0aGUgZG9jdW1lbnQgbWFuYWdlciBwbHVnaW4uXG4gKi9cbm5hbWVzcGFjZSBDb21tYW5kSURzIHtcbiAgZXhwb3J0IGNvbnN0IGNsb25lID0gJ2RvY21hbmFnZXI6Y2xvbmUnO1xuXG4gIGV4cG9ydCBjb25zdCBkZWxldGVGaWxlID0gJ2RvY21hbmFnZXI6ZGVsZXRlLWZpbGUnO1xuXG4gIGV4cG9ydCBjb25zdCBuZXdVbnRpdGxlZCA9ICdkb2NtYW5hZ2VyOm5ldy11bnRpdGxlZCc7XG5cbiAgZXhwb3J0IGNvbnN0IG9wZW4gPSAnZG9jbWFuYWdlcjpvcGVuJztcblxuICBleHBvcnQgY29uc3Qgb3BlbkJyb3dzZXJUYWIgPSAnZG9jbWFuYWdlcjpvcGVuLWJyb3dzZXItdGFiJztcblxuICBleHBvcnQgY29uc3QgcmVsb2FkID0gJ2RvY21hbmFnZXI6cmVsb2FkJztcblxuICBleHBvcnQgY29uc3QgcmVuYW1lID0gJ2RvY21hbmFnZXI6cmVuYW1lJztcblxuICBleHBvcnQgY29uc3QgZGVsID0gJ2RvY21hbmFnZXI6ZGVsZXRlJztcblxuICBleHBvcnQgY29uc3QgZHVwbGljYXRlID0gJ2RvY21hbmFnZXI6ZHVwbGljYXRlJztcblxuICBleHBvcnQgY29uc3QgcmVzdG9yZUNoZWNrcG9pbnQgPSAnZG9jbWFuYWdlcjpyZXN0b3JlLWNoZWNrcG9pbnQnO1xuXG4gIGV4cG9ydCBjb25zdCBzYXZlID0gJ2RvY21hbmFnZXI6c2F2ZSc7XG5cbiAgZXhwb3J0IGNvbnN0IHNhdmVBbGwgPSAnZG9jbWFuYWdlcjpzYXZlLWFsbCc7XG5cbiAgZXhwb3J0IGNvbnN0IHNhdmVBcyA9ICdkb2NtYW5hZ2VyOnNhdmUtYXMnO1xuXG4gIGV4cG9ydCBjb25zdCBkb3dubG9hZCA9ICdkb2NtYW5hZ2VyOmRvd25sb2FkJztcblxuICBleHBvcnQgY29uc3QgdG9nZ2xlQXV0b3NhdmUgPSAnZG9jbWFuYWdlcjp0b2dnbGUtYXV0b3NhdmUnO1xuXG4gIGV4cG9ydCBjb25zdCBzaG93SW5GaWxlQnJvd3NlciA9ICdkb2NtYW5hZ2VyOnNob3ctaW4tZmlsZS1icm93c2VyJztcbn1cblxuLyoqXG4gKiBUaGUgaWQgb2YgdGhlIGRvY3VtZW50IG1hbmFnZXIgcGx1Z2luLlxuICovXG5jb25zdCBkb2NNYW5hZ2VyUGx1Z2luSWQgPSAnQGp1cHl0ZXJsYWIvZG9jbWFuYWdlci1leHRlbnNpb246cGx1Z2luJztcblxuLyoqXG4gKiBBIHBsdWdpbiBwcm92aWRpbmcgdGhlIGRlZmF1bHQgZG9jdW1lbnQgbWFuYWdlci5cbiAqL1xuY29uc3QgbWFuYWdlcjogSnVweXRlckZyb250RW5kUGx1Z2luPElEb2N1bWVudE1hbmFnZXI+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2RvY21hbmFnZXItZXh0ZW5zaW9uOm1hbmFnZXInLFxuICBwcm92aWRlczogSURvY3VtZW50TWFuYWdlcixcbiAgb3B0aW9uYWw6IFtcbiAgICBJVHJhbnNsYXRvcixcbiAgICBJTGFiU3RhdHVzLFxuICAgIElTZXNzaW9uQ29udGV4dERpYWxvZ3MsXG4gICAgSURvY3VtZW50UHJvdmlkZXJGYWN0b3J5LFxuICAgIEp1cHl0ZXJMYWIuSUluZm9cbiAgXSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvciB8IG51bGwsXG4gICAgc3RhdHVzOiBJTGFiU3RhdHVzIHwgbnVsbCxcbiAgICBzZXNzaW9uRGlhbG9nczogSVNlc3Npb25Db250ZXh0RGlhbG9ncyB8IG51bGwsXG4gICAgZG9jUHJvdmlkZXJGYWN0b3J5OiBJRG9jdW1lbnRQcm92aWRlckZhY3RvcnkgfCBudWxsLFxuICAgIGluZm86IEp1cHl0ZXJMYWIuSUluZm8gfCBudWxsXG4gICkgPT4ge1xuICAgIGNvbnN0IHsgc2VydmljZU1hbmFnZXI6IG1hbmFnZXIsIGRvY1JlZ2lzdHJ5OiByZWdpc3RyeSB9ID0gYXBwO1xuICAgIGNvbnN0IGNvbnRleHRzID0gbmV3IFdlYWtTZXQ8RG9jdW1lbnRSZWdpc3RyeS5Db250ZXh0PigpO1xuICAgIGNvbnN0IHdoZW4gPSBhcHAucmVzdG9yZWQudGhlbigoKSA9PiB2b2lkIDApO1xuXG4gICAgY29uc3Qgb3BlbmVyOiBEb2N1bWVudE1hbmFnZXIuSVdpZGdldE9wZW5lciA9IHtcbiAgICAgIG9wZW46ICh3aWRnZXQsIG9wdGlvbnMpID0+IHtcbiAgICAgICAgaWYgKCF3aWRnZXQuaWQpIHtcbiAgICAgICAgICB3aWRnZXQuaWQgPSBgZG9jdW1lbnQtbWFuYWdlci0keysrUHJpdmF0ZS5pZH1gO1xuICAgICAgICB9XG4gICAgICAgIHdpZGdldC50aXRsZS5kYXRhc2V0ID0ge1xuICAgICAgICAgIHR5cGU6ICdkb2N1bWVudC10aXRsZScsXG4gICAgICAgICAgLi4ud2lkZ2V0LnRpdGxlLmRhdGFzZXRcbiAgICAgICAgfTtcbiAgICAgICAgaWYgKCF3aWRnZXQuaXNBdHRhY2hlZCkge1xuICAgICAgICAgIGFwcC5zaGVsbC5hZGQod2lkZ2V0LCAnbWFpbicsIG9wdGlvbnMgfHwge30pO1xuICAgICAgICB9XG4gICAgICAgIGFwcC5zaGVsbC5hY3RpdmF0ZUJ5SWQod2lkZ2V0LmlkKTtcblxuICAgICAgICAvLyBIYW5kbGUgZGlydHkgc3RhdGUgZm9yIG9wZW4gZG9jdW1lbnRzLlxuICAgICAgICBjb25zdCBjb250ZXh0ID0gZG9jTWFuYWdlci5jb250ZXh0Rm9yV2lkZ2V0KHdpZGdldCk7XG4gICAgICAgIGlmIChjb250ZXh0ICYmICFjb250ZXh0cy5oYXMoY29udGV4dCkpIHtcbiAgICAgICAgICBpZiAoc3RhdHVzKSB7XG4gICAgICAgICAgICBoYW5kbGVDb250ZXh0KHN0YXR1cywgY29udGV4dCk7XG4gICAgICAgICAgfVxuICAgICAgICAgIGNvbnRleHRzLmFkZChjb250ZXh0KTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH07XG5cbiAgICBjb25zdCBkb2NNYW5hZ2VyID0gbmV3IERvY3VtZW50TWFuYWdlcih7XG4gICAgICByZWdpc3RyeSxcbiAgICAgIG1hbmFnZXIsXG4gICAgICBvcGVuZXIsXG4gICAgICB3aGVuLFxuICAgICAgc2V0QnVzeTogKHN0YXR1cyAmJiAoKCkgPT4gc3RhdHVzLnNldEJ1c3koKSkpID8/IHVuZGVmaW5lZCxcbiAgICAgIHNlc3Npb25EaWFsb2dzOiBzZXNzaW9uRGlhbG9ncyB8fCB1bmRlZmluZWQsXG4gICAgICB0cmFuc2xhdG9yOiB0cmFuc2xhdG9yID8/IG51bGxUcmFuc2xhdG9yLFxuICAgICAgY29sbGFib3JhdGl2ZTogdHJ1ZSxcbiAgICAgIGRvY1Byb3ZpZGVyRmFjdG9yeTogZG9jUHJvdmlkZXJGYWN0b3J5ID8/IHVuZGVmaW5lZCxcbiAgICAgIGlzQ29ubmVjdGVkQ2FsbGJhY2s6ICgpID0+IHtcbiAgICAgICAgaWYgKGluZm8pIHtcbiAgICAgICAgICByZXR1cm4gaW5mby5pc0Nvbm5lY3RlZDtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIHJldHVybiBkb2NNYW5hZ2VyO1xuICB9XG59O1xuXG4vKipcbiAqIFRoZSBkZWZhdWx0IGRvY3VtZW50IG1hbmFnZXIgcHJvdmlkZXIuXG4gKi9cbmNvbnN0IGRvY01hbmFnZXJQbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6IGRvY01hbmFnZXJQbHVnaW5JZCxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICByZXF1aXJlczogW0lEb2N1bWVudE1hbmFnZXIsIElTZXR0aW5nUmVnaXN0cnldLFxuICBvcHRpb25hbDogW0lUcmFuc2xhdG9yLCBJQ29tbWFuZFBhbGV0dGUsIElMYWJTaGVsbF0sXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgZG9jTWFuYWdlcjogSURvY3VtZW50TWFuYWdlcixcbiAgICBzZXR0aW5nUmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnksXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IgfCBudWxsLFxuICAgIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSB8IG51bGwsXG4gICAgbGFiU2hlbGw6IElMYWJTaGVsbCB8IG51bGxcbiAgKTogdm9pZCA9PiB7XG4gICAgdHJhbnNsYXRvciA9IHRyYW5zbGF0b3IgPz8gbnVsbFRyYW5zbGF0b3I7XG4gICAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICBjb25zdCByZWdpc3RyeSA9IGFwcC5kb2NSZWdpc3RyeTtcblxuICAgIC8vIFJlZ2lzdGVyIHRoZSBmaWxlIG9wZXJhdGlvbnMgY29tbWFuZHMuXG4gICAgYWRkQ29tbWFuZHMoXG4gICAgICBhcHAsXG4gICAgICBkb2NNYW5hZ2VyLFxuICAgICAgb3BlbmVyLFxuICAgICAgc2V0dGluZ1JlZ2lzdHJ5LFxuICAgICAgdHJhbnNsYXRvcixcbiAgICAgIGxhYlNoZWxsLFxuICAgICAgcGFsZXR0ZVxuICAgICk7XG5cbiAgICAvLyBLZWVwIHVwIHRvIGRhdGUgd2l0aCB0aGUgc2V0dGluZ3MgcmVnaXN0cnkuXG4gICAgY29uc3Qgb25TZXR0aW5nc1VwZGF0ZWQgPSAoc2V0dGluZ3M6IElTZXR0aW5nUmVnaXN0cnkuSVNldHRpbmdzKSA9PiB7XG4gICAgICAvLyBIYW5kbGUgd2hldGhlciB0byBhdXRvc2F2ZVxuICAgICAgY29uc3QgYXV0b3NhdmUgPSBzZXR0aW5ncy5nZXQoJ2F1dG9zYXZlJykuY29tcG9zaXRlIGFzIGJvb2xlYW4gfCBudWxsO1xuICAgICAgZG9jTWFuYWdlci5hdXRvc2F2ZSA9XG4gICAgICAgIGF1dG9zYXZlID09PSB0cnVlIHx8IGF1dG9zYXZlID09PSBmYWxzZSA/IGF1dG9zYXZlIDogdHJ1ZTtcbiAgICAgIGFwcC5jb21tYW5kcy5ub3RpZnlDb21tYW5kQ2hhbmdlZChDb21tYW5kSURzLnRvZ2dsZUF1dG9zYXZlKTtcblxuICAgICAgLy8gSGFuZGxlIGF1dG9zYXZlIGludGVydmFsXG4gICAgICBjb25zdCBhdXRvc2F2ZUludGVydmFsID0gc2V0dGluZ3MuZ2V0KCdhdXRvc2F2ZUludGVydmFsJykuY29tcG9zaXRlIGFzXG4gICAgICAgIHwgbnVtYmVyXG4gICAgICAgIHwgbnVsbDtcbiAgICAgIGRvY01hbmFnZXIuYXV0b3NhdmVJbnRlcnZhbCA9IGF1dG9zYXZlSW50ZXJ2YWwgfHwgMTIwO1xuXG4gICAgICAvLyBIYW5kbGUgbGFzdCBtb2RpZmllZCB0aW1lc3RhbXAgY2hlY2sgbWFyZ2luXG4gICAgICBjb25zdCBsYXN0TW9kaWZpZWRDaGVja01hcmdpbiA9IHNldHRpbmdzLmdldCgnbGFzdE1vZGlmaWVkQ2hlY2tNYXJnaW4nKVxuICAgICAgICAuY29tcG9zaXRlIGFzIG51bWJlciB8IG51bGw7XG4gICAgICBkb2NNYW5hZ2VyLmxhc3RNb2RpZmllZENoZWNrTWFyZ2luID0gbGFzdE1vZGlmaWVkQ2hlY2tNYXJnaW4gfHwgNTAwO1xuXG4gICAgICBjb25zdCByZW5hbWVVbnRpdGxlZEZpbGUgPSBzZXR0aW5ncy5nZXQoJ3JlbmFtZVVudGl0bGVkRmlsZU9uU2F2ZScpXG4gICAgICAgIC5jb21wb3NpdGUgYXMgYm9vbGVhbjtcbiAgICAgIGRvY01hbmFnZXIucmVuYW1lVW50aXRsZWRGaWxlT25TYXZlID0gcmVuYW1lVW50aXRsZWRGaWxlID8/IHRydWU7XG5cbiAgICAgIC8vIEhhbmRsZSBkZWZhdWx0IHdpZGdldCBmYWN0b3J5IG92ZXJyaWRlcy5cbiAgICAgIGNvbnN0IGRlZmF1bHRWaWV3ZXJzID0gc2V0dGluZ3MuZ2V0KCdkZWZhdWx0Vmlld2VycycpLmNvbXBvc2l0ZSBhcyB7XG4gICAgICAgIFtmdDogc3RyaW5nXTogc3RyaW5nO1xuICAgICAgfTtcbiAgICAgIGNvbnN0IG92ZXJyaWRlczogeyBbZnQ6IHN0cmluZ106IHN0cmluZyB9ID0ge307XG4gICAgICAvLyBGaWx0ZXIgdGhlIGRlZmF1bHRWaWV3ZXJzIGFuZCBmaWxlIHR5cGVzIGZvciBleGlzdGluZyBvbmVzLlxuICAgICAgT2JqZWN0LmtleXMoZGVmYXVsdFZpZXdlcnMpLmZvckVhY2goZnQgPT4ge1xuICAgICAgICBpZiAoIXJlZ2lzdHJ5LmdldEZpbGVUeXBlKGZ0KSkge1xuICAgICAgICAgIGNvbnNvbGUud2FybihgRmlsZSBUeXBlICR7ZnR9IG5vdCBmb3VuZGApO1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuICAgICAgICBpZiAoIXJlZ2lzdHJ5LmdldFdpZGdldEZhY3RvcnkoZGVmYXVsdFZpZXdlcnNbZnRdKSkge1xuICAgICAgICAgIGNvbnNvbGUud2FybihgRG9jdW1lbnQgdmlld2VyICR7ZGVmYXVsdFZpZXdlcnNbZnRdfSBub3QgZm91bmRgKTtcbiAgICAgICAgfVxuICAgICAgICBvdmVycmlkZXNbZnRdID0gZGVmYXVsdFZpZXdlcnNbZnRdO1xuICAgICAgfSk7XG4gICAgICAvLyBTZXQgdGhlIGRlZmF1bHQgZmFjdG9yeSBvdmVycmlkZXMuIElmIG5vdCBwcm92aWRlZCwgdGhpcyBoYXMgdGhlXG4gICAgICAvLyBlZmZlY3Qgb2YgdW5zZXR0aW5nIGFueSBwcmV2aW91cyBvdmVycmlkZXMuXG4gICAgICBlYWNoKHJlZ2lzdHJ5LmZpbGVUeXBlcygpLCBmdCA9PiB7XG4gICAgICAgIHRyeSB7XG4gICAgICAgICAgcmVnaXN0cnkuc2V0RGVmYXVsdFdpZGdldEZhY3RvcnkoZnQubmFtZSwgb3ZlcnJpZGVzW2Z0Lm5hbWVdKTtcbiAgICAgICAgfSBjYXRjaCB7XG4gICAgICAgICAgY29uc29sZS53YXJuKFxuICAgICAgICAgICAgYEZhaWxlZCB0byBzZXQgZGVmYXVsdCB2aWV3ZXIgJHtvdmVycmlkZXNbZnQubmFtZV19IGZvciBmaWxlIHR5cGUgJHtcbiAgICAgICAgICAgICAgZnQubmFtZVxuICAgICAgICAgICAgfWBcbiAgICAgICAgICApO1xuICAgICAgICB9XG4gICAgICB9KTtcbiAgICB9O1xuXG4gICAgLy8gRmV0Y2ggdGhlIGluaXRpYWwgc3RhdGUgb2YgdGhlIHNldHRpbmdzLlxuICAgIFByb21pc2UuYWxsKFtzZXR0aW5nUmVnaXN0cnkubG9hZChkb2NNYW5hZ2VyUGx1Z2luSWQpLCBhcHAucmVzdG9yZWRdKVxuICAgICAgLnRoZW4oKFtzZXR0aW5nc10pID0+IHtcbiAgICAgICAgc2V0dGluZ3MuY2hhbmdlZC5jb25uZWN0KG9uU2V0dGluZ3NVcGRhdGVkKTtcbiAgICAgICAgb25TZXR0aW5nc1VwZGF0ZWQoc2V0dGluZ3MpO1xuICAgICAgfSlcbiAgICAgIC5jYXRjaCgocmVhc29uOiBFcnJvcikgPT4ge1xuICAgICAgICBjb25zb2xlLmVycm9yKHJlYXNvbi5tZXNzYWdlKTtcbiAgICAgIH0pO1xuXG4gICAgLy8gUmVnaXN0ZXIgYSBmZXRjaCB0cmFuc2Zvcm1lciBmb3IgdGhlIHNldHRpbmdzIHJlZ2lzdHJ5LFxuICAgIC8vIGFsbG93aW5nIHVzIHRvIGR5bmFtaWNhbGx5IHBvcHVsYXRlIGEgaGVscCBzdHJpbmcgd2l0aCB0aGVcbiAgICAvLyBhdmFpbGFibGUgZG9jdW1lbnQgdmlld2VycyBhbmQgZmlsZSB0eXBlcyBmb3IgdGhlIGRlZmF1bHRcbiAgICAvLyB2aWV3ZXIgb3ZlcnJpZGVzLlxuICAgIHNldHRpbmdSZWdpc3RyeS50cmFuc2Zvcm0oZG9jTWFuYWdlclBsdWdpbklkLCB7XG4gICAgICBmZXRjaDogcGx1Z2luID0+IHtcbiAgICAgICAgLy8gR2V0IHRoZSBhdmFpbGFibGUgZmlsZSB0eXBlcy5cbiAgICAgICAgY29uc3QgZmlsZVR5cGVzID0gdG9BcnJheShyZWdpc3RyeS5maWxlVHlwZXMoKSlcbiAgICAgICAgICAubWFwKGZ0ID0+IGZ0Lm5hbWUpXG4gICAgICAgICAgLmpvaW4oJyAgICBcXG4nKTtcbiAgICAgICAgLy8gR2V0IHRoZSBhdmFpbGFibGUgd2lkZ2V0IGZhY3Rvcmllcy5cbiAgICAgICAgY29uc3QgZmFjdG9yaWVzID0gdG9BcnJheShyZWdpc3RyeS53aWRnZXRGYWN0b3JpZXMoKSlcbiAgICAgICAgICAubWFwKGYgPT4gZi5uYW1lKVxuICAgICAgICAgIC5qb2luKCcgICAgXFxuJyk7XG4gICAgICAgIC8vIEdlbmVyYXRlIHRoZSBoZWxwIHN0cmluZy5cbiAgICAgICAgY29uc3QgZGVzY3JpcHRpb24gPSB0cmFucy5fXyhcbiAgICAgICAgICBgT3ZlcnJpZGVzIGZvciB0aGUgZGVmYXVsdCB2aWV3ZXJzIGZvciBmaWxlIHR5cGVzLlxuU3BlY2lmeSBhIG1hcHBpbmcgZnJvbSBmaWxlIHR5cGUgbmFtZSB0byBkb2N1bWVudCB2aWV3ZXIgbmFtZSwgZm9yIGV4YW1wbGU6XG5cbmRlZmF1bHRWaWV3ZXJzOiB7XG4gIG1hcmtkb3duOiBcIk1hcmtkb3duIFByZXZpZXdcIlxufVxuXG5JZiB5b3Ugc3BlY2lmeSBub24tZXhpc3RlbnQgZmlsZSB0eXBlcyBvciB2aWV3ZXJzLCBvciBpZiBhIHZpZXdlciBjYW5ub3Rcbm9wZW4gYSBnaXZlbiBmaWxlIHR5cGUsIHRoZSBvdmVycmlkZSB3aWxsIG5vdCBmdW5jdGlvbi5cblxuQXZhaWxhYmxlIHZpZXdlcnM6XG4lMVxuXG5BdmFpbGFibGUgZmlsZSB0eXBlczpcbiUyYCxcbiAgICAgICAgICBmYWN0b3JpZXMsXG4gICAgICAgICAgZmlsZVR5cGVzXG4gICAgICAgICk7XG4gICAgICAgIGNvbnN0IHNjaGVtYSA9IEpTT05FeHQuZGVlcENvcHkocGx1Z2luLnNjaGVtYSk7XG4gICAgICAgIHNjaGVtYS5wcm9wZXJ0aWVzIS5kZWZhdWx0Vmlld2Vycy5kZXNjcmlwdGlvbiA9IGRlc2NyaXB0aW9uO1xuICAgICAgICByZXR1cm4geyAuLi5wbHVnaW4sIHNjaGVtYSB9O1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgLy8gSWYgdGhlIGRvY3VtZW50IHJlZ2lzdHJ5IGdhaW5zIG9yIGxvc2VzIGEgZmFjdG9yeSBvciBmaWxlIHR5cGUsXG4gICAgLy8gcmVnZW5lcmF0ZSB0aGUgc2V0dGluZ3MgZGVzY3JpcHRpb24gd2l0aCB0aGUgYXZhaWxhYmxlIG9wdGlvbnMuXG4gICAgcmVnaXN0cnkuY2hhbmdlZC5jb25uZWN0KCgpID0+IHNldHRpbmdSZWdpc3RyeS5yZWxvYWQoZG9jTWFuYWdlclBsdWdpbklkKSk7XG4gIH1cbn07XG5cbi8qKlxuICogQSBwbHVnaW4gZm9yIGFkZGluZyBhIHNhdmluZyBzdGF0dXMgaXRlbSB0byB0aGUgc3RhdHVzIGJhci5cbiAqL1xuZXhwb3J0IGNvbnN0IHNhdmluZ1N0YXR1c1BsdWdpbjogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2RvY21hbmFnZXItZXh0ZW5zaW9uOnNhdmluZy1zdGF0dXMnLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHJlcXVpcmVzOiBbSURvY3VtZW50TWFuYWdlciwgSUxhYlNoZWxsXSxcbiAgb3B0aW9uYWw6IFtJVHJhbnNsYXRvciwgSVN0YXR1c0Jhcl0sXG4gIGFjdGl2YXRlOiAoXG4gICAgXzogSnVweXRlckZyb250RW5kLFxuICAgIGRvY01hbmFnZXI6IElEb2N1bWVudE1hbmFnZXIsXG4gICAgbGFiU2hlbGw6IElMYWJTaGVsbCxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvciB8IG51bGwsXG4gICAgc3RhdHVzQmFyOiBJU3RhdHVzQmFyIHwgbnVsbFxuICApID0+IHtcbiAgICBpZiAoIXN0YXR1c0Jhcikge1xuICAgICAgLy8gQXV0b21hdGljYWxseSBkaXNhYmxlIGlmIHN0YXR1c2JhciBtaXNzaW5nXG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbnN0IHNhdmluZyA9IG5ldyBTYXZpbmdTdGF0dXMoe1xuICAgICAgZG9jTWFuYWdlcixcbiAgICAgIHRyYW5zbGF0b3I6IHRyYW5zbGF0b3IgPz8gbnVsbFRyYW5zbGF0b3JcbiAgICB9KTtcblxuICAgIC8vIEtlZXAgdGhlIGN1cnJlbnRseSBhY3RpdmUgd2lkZ2V0IHN5bmNocm9uaXplZC5cbiAgICBzYXZpbmcubW9kZWwhLndpZGdldCA9IGxhYlNoZWxsLmN1cnJlbnRXaWRnZXQ7XG4gICAgbGFiU2hlbGwuY3VycmVudENoYW5nZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICBzYXZpbmcubW9kZWwhLndpZGdldCA9IGxhYlNoZWxsLmN1cnJlbnRXaWRnZXQ7XG4gICAgfSk7XG5cbiAgICBzdGF0dXNCYXIucmVnaXN0ZXJTdGF0dXNJdGVtKHNhdmluZ1N0YXR1c1BsdWdpbi5pZCwge1xuICAgICAgaXRlbTogc2F2aW5nLFxuICAgICAgYWxpZ246ICdtaWRkbGUnLFxuICAgICAgaXNBY3RpdmU6ICgpID0+IHNhdmluZy5tb2RlbCAhPT0gbnVsbCAmJiBzYXZpbmcubW9kZWwuc3RhdHVzICE9PSBudWxsLFxuICAgICAgYWN0aXZlU3RhdGVDaGFuZ2VkOiBzYXZpbmcubW9kZWwhLnN0YXRlQ2hhbmdlZFxuICAgIH0pO1xuICB9XG59O1xuXG4vKipcbiAqIEEgcGx1Z2luIHByb3ZpZGluZyBhIGZpbGUgcGF0aCB3aWRnZXQgdG8gdGhlIHN0YXR1cyBiYXIuXG4gKi9cbmV4cG9ydCBjb25zdCBwYXRoU3RhdHVzUGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvZG9jbWFuYWdlci1leHRlbnNpb246cGF0aC1zdGF0dXMnLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHJlcXVpcmVzOiBbSURvY3VtZW50TWFuYWdlciwgSUxhYlNoZWxsXSxcbiAgb3B0aW9uYWw6IFtJU3RhdHVzQmFyXSxcbiAgYWN0aXZhdGU6IChcbiAgICBfOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgZG9jTWFuYWdlcjogSURvY3VtZW50TWFuYWdlcixcbiAgICBsYWJTaGVsbDogSUxhYlNoZWxsLFxuICAgIHN0YXR1c0JhcjogSVN0YXR1c0JhciB8IG51bGxcbiAgKSA9PiB7XG4gICAgaWYgKCFzdGF0dXNCYXIpIHtcbiAgICAgIC8vIEF1dG9tYXRpY2FsbHkgZGlzYWJsZSBpZiBzdGF0dXNiYXIgbWlzc2luZ1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBjb25zdCBwYXRoID0gbmV3IFBhdGhTdGF0dXMoeyBkb2NNYW5hZ2VyIH0pO1xuXG4gICAgLy8gS2VlcCB0aGUgZmlsZSBwYXRoIHdpZGdldCB1cC10by1kYXRlIHdpdGggdGhlIGFwcGxpY2F0aW9uIGFjdGl2ZSB3aWRnZXQuXG4gICAgcGF0aC5tb2RlbCEud2lkZ2V0ID0gbGFiU2hlbGwuY3VycmVudFdpZGdldDtcbiAgICBsYWJTaGVsbC5jdXJyZW50Q2hhbmdlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgIHBhdGgubW9kZWwhLndpZGdldCA9IGxhYlNoZWxsLmN1cnJlbnRXaWRnZXQ7XG4gICAgfSk7XG5cbiAgICBzdGF0dXNCYXIucmVnaXN0ZXJTdGF0dXNJdGVtKHBhdGhTdGF0dXNQbHVnaW4uaWQsIHtcbiAgICAgIGl0ZW06IHBhdGgsXG4gICAgICBhbGlnbjogJ3JpZ2h0JyxcbiAgICAgIHJhbms6IDBcbiAgICB9KTtcbiAgfVxufTtcblxuLyoqXG4gKiBBIHBsdWdpbiBwcm92aWRpbmcgZG93bmxvYWQgY29tbWFuZHMgaW4gdGhlIGZpbGUgbWVudSBhbmQgY29tbWFuZCBwYWxldHRlLlxuICovXG5leHBvcnQgY29uc3QgZG93bmxvYWRQbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9kb2NtYW5hZ2VyLWV4dGVuc2lvbjpkb3dubG9hZCcsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcmVxdWlyZXM6IFtJRG9jdW1lbnRNYW5hZ2VyXSxcbiAgb3B0aW9uYWw6IFtJVHJhbnNsYXRvciwgSUNvbW1hbmRQYWxldHRlXSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICBkb2NNYW5hZ2VyOiBJRG9jdW1lbnRNYW5hZ2VyLFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yIHwgbnVsbCxcbiAgICBwYWxldHRlOiBJQ29tbWFuZFBhbGV0dGUgfCBudWxsXG4gICkgPT4ge1xuICAgIGNvbnN0IHRyYW5zID0gKHRyYW5zbGF0b3IgPz8gbnVsbFRyYW5zbGF0b3IpLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICBjb25zdCB7IGNvbW1hbmRzLCBzaGVsbCB9ID0gYXBwO1xuICAgIGNvbnN0IGlzRW5hYmxlZCA9ICgpID0+IHtcbiAgICAgIGNvbnN0IHsgY3VycmVudFdpZGdldCB9ID0gc2hlbGw7XG4gICAgICByZXR1cm4gISEoY3VycmVudFdpZGdldCAmJiBkb2NNYW5hZ2VyLmNvbnRleHRGb3JXaWRnZXQoY3VycmVudFdpZGdldCkpO1xuICAgIH07XG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmRvd25sb2FkLCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ0Rvd25sb2FkJyksXG4gICAgICBjYXB0aW9uOiB0cmFucy5fXygnRG93bmxvYWQgdGhlIGZpbGUgdG8geW91ciBjb21wdXRlcicpLFxuICAgICAgaXNFbmFibGVkLFxuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICAvLyBDaGVja3MgdGhhdCBzaGVsbC5jdXJyZW50V2lkZ2V0IGlzIHZhbGlkOlxuICAgICAgICBpZiAoaXNFbmFibGVkKCkpIHtcbiAgICAgICAgICBjb25zdCBjb250ZXh0ID0gZG9jTWFuYWdlci5jb250ZXh0Rm9yV2lkZ2V0KHNoZWxsLmN1cnJlbnRXaWRnZXQhKTtcbiAgICAgICAgICBpZiAoIWNvbnRleHQpIHtcbiAgICAgICAgICAgIHJldHVybiBzaG93RGlhbG9nKHtcbiAgICAgICAgICAgICAgdGl0bGU6IHRyYW5zLl9fKCdDYW5ub3QgRG93bmxvYWQnKSxcbiAgICAgICAgICAgICAgYm9keTogdHJhbnMuX18oJ05vIGNvbnRleHQgZm91bmQgZm9yIGN1cnJlbnQgd2lkZ2V0IScpLFxuICAgICAgICAgICAgICBidXR0b25zOiBbRGlhbG9nLm9rQnV0dG9uKCldXG4gICAgICAgICAgICB9KTtcbiAgICAgICAgICB9XG4gICAgICAgICAgcmV0dXJuIGNvbnRleHQuZG93bmxvYWQoKTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH0pO1xuXG4gICAgY29uc3QgY2F0ZWdvcnkgPSB0cmFucy5fXygnRmlsZSBPcGVyYXRpb25zJyk7XG4gICAgaWYgKHBhbGV0dGUpIHtcbiAgICAgIHBhbGV0dGUuYWRkSXRlbSh7IGNvbW1hbmQ6IENvbW1hbmRJRHMuZG93bmxvYWQsIGNhdGVnb3J5IH0pO1xuICAgIH1cbiAgfVxufTtcblxuLyoqXG4gKiBBIHBsdWdpbiBwcm92aWRpbmcgb3Blbi1icm93c2VyLXRhYiBjb21tYW5kcy5cbiAqXG4gKiBUaGlzIGlzIGl0cyBvd24gcGx1Z2luIGluIGNhc2UgeW91IHdvdWxkIGxpa2UgdG8gZGlzYWJsZSB0aGlzIGZlYXR1cmUuXG4gKiBlLmcuIGp1cHl0ZXIgbGFiZXh0ZW5zaW9uIGRpc2FibGUgQGp1cHl0ZXJsYWIvZG9jbWFuYWdlci1leHRlbnNpb246b3Blbi1icm93c2VyLXRhYlxuICpcbiAqIE5vdGU6IElmIGRpc2FibGluZyB0aGlzLCB5b3UgbWF5IGFsc28gd2FudCB0byBkaXNhYmxlOlxuICogQGp1cHl0ZXJsYWIvZmlsZWJyb3dzZXItZXh0ZW5zaW9uOm9wZW4tYnJvd3Nlci10YWJcbiAqL1xuZXhwb3J0IGNvbnN0IG9wZW5Ccm93c2VyVGFiUGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvZG9jbWFuYWdlci1leHRlbnNpb246b3Blbi1icm93c2VyLXRhYicsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcmVxdWlyZXM6IFtJRG9jdW1lbnRNYW5hZ2VyXSxcbiAgb3B0aW9uYWw6IFtJVHJhbnNsYXRvcl0sXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgZG9jTWFuYWdlcjogSURvY3VtZW50TWFuYWdlcixcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvciB8IG51bGxcbiAgKSA9PiB7XG4gICAgY29uc3QgdHJhbnMgPSAodHJhbnNsYXRvciA/PyBudWxsVHJhbnNsYXRvcikubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IHsgY29tbWFuZHMgfSA9IGFwcDtcbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMub3BlbkJyb3dzZXJUYWIsIHtcbiAgICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgICBjb25zdCBwYXRoID1cbiAgICAgICAgICB0eXBlb2YgYXJnc1sncGF0aCddID09PSAndW5kZWZpbmVkJyA/ICcnIDogKGFyZ3NbJ3BhdGgnXSBhcyBzdHJpbmcpO1xuXG4gICAgICAgIGlmICghcGF0aCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIHJldHVybiBkb2NNYW5hZ2VyLnNlcnZpY2VzLmNvbnRlbnRzLmdldERvd25sb2FkVXJsKHBhdGgpLnRoZW4odXJsID0+IHtcbiAgICAgICAgICBjb25zdCBvcGVuZWQgPSB3aW5kb3cub3BlbigpO1xuICAgICAgICAgIGlmIChvcGVuZWQpIHtcbiAgICAgICAgICAgIG9wZW5lZC5vcGVuZXIgPSBudWxsO1xuICAgICAgICAgICAgb3BlbmVkLmxvY2F0aW9uLmhyZWYgPSB1cmw7XG4gICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIHRocm93IG5ldyBFcnJvcignRmFpbGVkIHRvIG9wZW4gbmV3IGJyb3dzZXIgdGFiLicpO1xuICAgICAgICAgIH1cbiAgICAgICAgfSk7XG4gICAgICB9LFxuICAgICAgaWNvbjogYXJncyA9PiAoYXJnc1snaWNvbiddIGFzIHN0cmluZykgfHwgJycsXG4gICAgICBsYWJlbDogKCkgPT4gdHJhbnMuX18oJ09wZW4gaW4gTmV3IEJyb3dzZXIgVGFiJylcbiAgICB9KTtcbiAgfVxufTtcblxuLyoqXG4gKiBFeHBvcnQgdGhlIHBsdWdpbnMgYXMgZGVmYXVsdC5cbiAqL1xuY29uc3QgcGx1Z2luczogSnVweXRlckZyb250RW5kUGx1Z2luPGFueT5bXSA9IFtcbiAgbWFuYWdlcixcbiAgZG9jTWFuYWdlclBsdWdpbixcbiAgcGF0aFN0YXR1c1BsdWdpbixcbiAgc2F2aW5nU3RhdHVzUGx1Z2luLFxuICBkb3dubG9hZFBsdWdpbixcbiAgb3BlbkJyb3dzZXJUYWJQbHVnaW5cbl07XG5leHBvcnQgZGVmYXVsdCBwbHVnaW5zO1xuXG4vKipcbiAqIFRvb2xiYXIgaXRlbSBmYWN0b3J5XG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgVG9vbGJhckl0ZW1zIHtcbiAgLyoqXG4gICAqIENyZWF0ZSBzYXZlIGJ1dHRvbiB0b29sYmFyIGl0ZW0uXG4gICAqXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gY3JlYXRlU2F2ZUJ1dHRvbihcbiAgICBjb21tYW5kczogQ29tbWFuZFJlZ2lzdHJ5LFxuICAgIGZpbGVDaGFuZ2VkOiBJU2lnbmFsPGFueSwgQ29udGVudHMuSU1vZGVsPlxuICApOiBXaWRnZXQge1xuICAgIHJldHVybiBhZGRDb21tYW5kVG9vbGJhckJ1dHRvbkNsYXNzKFxuICAgICAgUmVhY3RXaWRnZXQuY3JlYXRlKFxuICAgICAgICA8VXNlU2lnbmFsIHNpZ25hbD17ZmlsZUNoYW5nZWR9PlxuICAgICAgICAgIHsoKSA9PiAoXG4gICAgICAgICAgICA8Q29tbWFuZFRvb2xiYXJCdXR0b25Db21wb25lbnRcbiAgICAgICAgICAgICAgY29tbWFuZHM9e2NvbW1hbmRzfVxuICAgICAgICAgICAgICBpZD17Q29tbWFuZElEcy5zYXZlfVxuICAgICAgICAgICAgICBsYWJlbD17Jyd9XG4gICAgICAgICAgICAgIGFyZ3M9e3sgdG9vbGJhcjogdHJ1ZSB9fVxuICAgICAgICAgICAgLz5cbiAgICAgICAgICApfVxuICAgICAgICA8L1VzZVNpZ25hbD5cbiAgICAgIClcbiAgICApO1xuICB9XG59XG5cbi8qIFdpZGdldCB0byBkaXNwbGF5IHRoZSByZXZlcnQgdG8gY2hlY2twb2ludCBjb25maXJtYXRpb24uICovXG5jbGFzcyBSZXZlcnRDb25maXJtV2lkZ2V0IGV4dGVuZHMgV2lkZ2V0IHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCBhIG5ldyByZXZlcnQgY29uZmlybWF0aW9uIHdpZGdldC5cbiAgICovXG4gIGNvbnN0cnVjdG9yKFxuICAgIGNoZWNrcG9pbnQ6IENvbnRlbnRzLklDaGVja3BvaW50TW9kZWwsXG4gICAgdHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlLFxuICAgIGZpbGVUeXBlOiBzdHJpbmcgPSAnbm90ZWJvb2snXG4gICkge1xuICAgIHN1cGVyKHtcbiAgICAgIG5vZGU6IFByaXZhdGUuY3JlYXRlUmV2ZXJ0Q29uZmlybU5vZGUoY2hlY2twb2ludCwgZmlsZVR5cGUsIHRyYW5zKVxuICAgIH0pO1xuICB9XG59XG5cbi8vIFJldHVybnMgdGhlIGZpbGUgdHlwZSBmb3IgYSB3aWRnZXQuXG5mdW5jdGlvbiBmaWxlVHlwZSh3aWRnZXQ6IFdpZGdldCB8IG51bGwsIGRvY01hbmFnZXI6IElEb2N1bWVudE1hbmFnZXIpOiBzdHJpbmcge1xuICBpZiAoIXdpZGdldCkge1xuICAgIHJldHVybiAnRmlsZSc7XG4gIH1cbiAgY29uc3QgY29udGV4dCA9IGRvY01hbmFnZXIuY29udGV4dEZvcldpZGdldCh3aWRnZXQpO1xuICBpZiAoIWNvbnRleHQpIHtcbiAgICByZXR1cm4gJyc7XG4gIH1cbiAgY29uc3QgZnRzID0gZG9jTWFuYWdlci5yZWdpc3RyeS5nZXRGaWxlVHlwZXNGb3JQYXRoKGNvbnRleHQucGF0aCk7XG4gIHJldHVybiBmdHMubGVuZ3RoICYmIGZ0c1swXS5kaXNwbGF5TmFtZSA/IGZ0c1swXS5kaXNwbGF5TmFtZSA6ICdGaWxlJztcbn1cblxuLyoqXG4gKiBBZGQgdGhlIGZpbGUgb3BlcmF0aW9ucyBjb21tYW5kcyB0byB0aGUgYXBwbGljYXRpb24ncyBjb21tYW5kIHJlZ2lzdHJ5LlxuICovXG5mdW5jdGlvbiBhZGRDb21tYW5kcyhcbiAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gIGRvY01hbmFnZXI6IElEb2N1bWVudE1hbmFnZXIsXG4gIG9wZW5lcjogRG9jdW1lbnRNYW5hZ2VyLklXaWRnZXRPcGVuZXIsXG4gIHNldHRpbmdSZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSxcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gIGxhYlNoZWxsOiBJTGFiU2hlbGwgfCBudWxsLFxuICBwYWxldHRlOiBJQ29tbWFuZFBhbGV0dGUgfCBudWxsXG4pOiB2b2lkIHtcbiAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgY29uc3QgeyBjb21tYW5kcywgc2hlbGwgfSA9IGFwcDtcbiAgY29uc3QgY2F0ZWdvcnkgPSB0cmFucy5fXygnRmlsZSBPcGVyYXRpb25zJyk7XG4gIGNvbnN0IGlzRW5hYmxlZCA9ICgpID0+IHtcbiAgICBjb25zdCB7IGN1cnJlbnRXaWRnZXQgfSA9IHNoZWxsO1xuICAgIHJldHVybiAhIShjdXJyZW50V2lkZ2V0ICYmIGRvY01hbmFnZXIuY29udGV4dEZvcldpZGdldChjdXJyZW50V2lkZ2V0KSk7XG4gIH07XG5cbiAgY29uc3QgaXNXcml0YWJsZSA9ICgpID0+IHtcbiAgICBjb25zdCB7IGN1cnJlbnRXaWRnZXQgfSA9IHNoZWxsO1xuICAgIGlmICghY3VycmVudFdpZGdldCkge1xuICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH1cbiAgICBjb25zdCBjb250ZXh0ID0gZG9jTWFuYWdlci5jb250ZXh0Rm9yV2lkZ2V0KGN1cnJlbnRXaWRnZXQpO1xuICAgIHJldHVybiAhIShcbiAgICAgIGNvbnRleHQgJiZcbiAgICAgIGNvbnRleHQuY29udGVudHNNb2RlbCAmJlxuICAgICAgY29udGV4dC5jb250ZW50c01vZGVsLndyaXRhYmxlXG4gICAgKTtcbiAgfTtcblxuICAvLyBJZiBpbnNpZGUgYSByaWNoIGFwcGxpY2F0aW9uIGxpa2UgSnVweXRlckxhYiwgYWRkIGFkZGl0aW9uYWwgZnVuY3Rpb25hbGl0eS5cbiAgaWYgKGxhYlNoZWxsKSB7XG4gICAgYWRkTGFiQ29tbWFuZHMoYXBwLCBkb2NNYW5hZ2VyLCBsYWJTaGVsbCwgb3BlbmVyLCB0cmFuc2xhdG9yKTtcbiAgfVxuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5kZWxldGVGaWxlLCB7XG4gICAgbGFiZWw6ICgpID0+IGBEZWxldGUgJHtmaWxlVHlwZShzaGVsbC5jdXJyZW50V2lkZ2V0LCBkb2NNYW5hZ2VyKX1gLFxuICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgY29uc3QgcGF0aCA9XG4gICAgICAgIHR5cGVvZiBhcmdzWydwYXRoJ10gPT09ICd1bmRlZmluZWQnID8gJycgOiAoYXJnc1sncGF0aCddIGFzIHN0cmluZyk7XG5cbiAgICAgIGlmICghcGF0aCkge1xuICAgICAgICBjb25zdCBjb21tYW5kID0gQ29tbWFuZElEcy5kZWxldGVGaWxlO1xuICAgICAgICB0aHJvdyBuZXcgRXJyb3IoYEEgbm9uLWVtcHR5IHBhdGggaXMgcmVxdWlyZWQgZm9yICR7Y29tbWFuZH0uYCk7XG4gICAgICB9XG4gICAgICByZXR1cm4gZG9jTWFuYWdlci5kZWxldGVGaWxlKHBhdGgpO1xuICAgIH1cbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLm5ld1VudGl0bGVkLCB7XG4gICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICBjb25zdCBlcnJvclRpdGxlID0gKGFyZ3NbJ2Vycm9yJ10gYXMgc3RyaW5nKSB8fCB0cmFucy5fXygnRXJyb3InKTtcbiAgICAgIGNvbnN0IHBhdGggPVxuICAgICAgICB0eXBlb2YgYXJnc1sncGF0aCddID09PSAndW5kZWZpbmVkJyA/ICcnIDogKGFyZ3NbJ3BhdGgnXSBhcyBzdHJpbmcpO1xuICAgICAgY29uc3Qgb3B0aW9uczogUGFydGlhbDxDb250ZW50cy5JQ3JlYXRlT3B0aW9ucz4gPSB7XG4gICAgICAgIHR5cGU6IGFyZ3NbJ3R5cGUnXSBhcyBDb250ZW50cy5Db250ZW50VHlwZSxcbiAgICAgICAgcGF0aFxuICAgICAgfTtcblxuICAgICAgaWYgKGFyZ3NbJ3R5cGUnXSA9PT0gJ2ZpbGUnKSB7XG4gICAgICAgIG9wdGlvbnMuZXh0ID0gKGFyZ3NbJ2V4dCddIGFzIHN0cmluZykgfHwgJy50eHQnO1xuICAgICAgfVxuXG4gICAgICByZXR1cm4gZG9jTWFuYWdlci5zZXJ2aWNlcy5jb250ZW50c1xuICAgICAgICAubmV3VW50aXRsZWQob3B0aW9ucylcbiAgICAgICAgLmNhdGNoKGVycm9yID0+IHNob3dFcnJvck1lc3NhZ2UoZXJyb3JUaXRsZSwgZXJyb3IpKTtcbiAgICB9LFxuICAgIGxhYmVsOiBhcmdzID0+IChhcmdzWydsYWJlbCddIGFzIHN0cmluZykgfHwgYE5ldyAke2FyZ3NbJ3R5cGUnXSBhcyBzdHJpbmd9YFxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMub3Blbiwge1xuICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgY29uc3QgcGF0aCA9XG4gICAgICAgIHR5cGVvZiBhcmdzWydwYXRoJ10gPT09ICd1bmRlZmluZWQnID8gJycgOiAoYXJnc1sncGF0aCddIGFzIHN0cmluZyk7XG4gICAgICBjb25zdCBmYWN0b3J5ID0gKGFyZ3NbJ2ZhY3RvcnknXSBhcyBzdHJpbmcpIHx8IHZvaWQgMDtcbiAgICAgIGNvbnN0IGtlcm5lbCA9IGFyZ3M/Lmtlcm5lbCBhcyB1bmtub3duIGFzIEtlcm5lbC5JTW9kZWwgfCB1bmRlZmluZWQ7XG4gICAgICBjb25zdCBvcHRpb25zID1cbiAgICAgICAgKGFyZ3NbJ29wdGlvbnMnXSBhcyBEb2N1bWVudFJlZ2lzdHJ5LklPcGVuT3B0aW9ucykgfHwgdm9pZCAwO1xuICAgICAgcmV0dXJuIGRvY01hbmFnZXIuc2VydmljZXMuY29udGVudHNcbiAgICAgICAgLmdldChwYXRoLCB7IGNvbnRlbnQ6IGZhbHNlIH0pXG4gICAgICAgIC50aGVuKCgpID0+IGRvY01hbmFnZXIub3Blbk9yUmV2ZWFsKHBhdGgsIGZhY3RvcnksIGtlcm5lbCwgb3B0aW9ucykpO1xuICAgIH0sXG4gICAgaWNvbjogYXJncyA9PiAoYXJnc1snaWNvbiddIGFzIHN0cmluZykgfHwgJycsXG4gICAgbGFiZWw6IGFyZ3MgPT5cbiAgICAgICgoYXJnc1snbGFiZWwnXSB8fCBhcmdzWydmYWN0b3J5J10pID8/XG4gICAgICAgIHRyYW5zLl9fKCdPcGVuIHRoZSBwcm92aWRlZCBgcGF0aGAuJykpIGFzIHN0cmluZyxcbiAgICBtbmVtb25pYzogYXJncyA9PiAoYXJnc1snbW5lbW9uaWMnXSBhcyBudW1iZXIpIHx8IC0xXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5yZWxvYWQsIHtcbiAgICBsYWJlbDogKCkgPT5cbiAgICAgIHRyYW5zLl9fKFxuICAgICAgICAnUmVsb2FkICUxIGZyb20gRGlzaycsXG4gICAgICAgIGZpbGVUeXBlKHNoZWxsLmN1cnJlbnRXaWRnZXQsIGRvY01hbmFnZXIpXG4gICAgICApLFxuICAgIGNhcHRpb246IHRyYW5zLl9fKCdSZWxvYWQgY29udGVudHMgZnJvbSBkaXNrJyksXG4gICAgaXNFbmFibGVkLFxuICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgIC8vIENoZWNrcyB0aGF0IHNoZWxsLmN1cnJlbnRXaWRnZXQgaXMgdmFsaWQ6XG4gICAgICBpZiAoIWlzRW5hYmxlZCgpKSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGNvbnN0IGNvbnRleHQgPSBkb2NNYW5hZ2VyLmNvbnRleHRGb3JXaWRnZXQoc2hlbGwuY3VycmVudFdpZGdldCEpO1xuICAgICAgY29uc3QgdHlwZSA9IGZpbGVUeXBlKHNoZWxsLmN1cnJlbnRXaWRnZXQhLCBkb2NNYW5hZ2VyKTtcbiAgICAgIGlmICghY29udGV4dCkge1xuICAgICAgICByZXR1cm4gc2hvd0RpYWxvZyh7XG4gICAgICAgICAgdGl0bGU6IHRyYW5zLl9fKCdDYW5ub3QgUmVsb2FkJyksXG4gICAgICAgICAgYm9keTogdHJhbnMuX18oJ05vIGNvbnRleHQgZm91bmQgZm9yIGN1cnJlbnQgd2lkZ2V0IScpLFxuICAgICAgICAgIGJ1dHRvbnM6IFtEaWFsb2cub2tCdXR0b24oKV1cbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgICBpZiAoY29udGV4dC5tb2RlbC5kaXJ0eSkge1xuICAgICAgICByZXR1cm4gc2hvd0RpYWxvZyh7XG4gICAgICAgICAgdGl0bGU6IHRyYW5zLl9fKCdSZWxvYWQgJTEgZnJvbSBEaXNrJywgdHlwZSksXG4gICAgICAgICAgYm9keTogdHJhbnMuX18oXG4gICAgICAgICAgICAnQXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJlbG9hZCB0aGUgJTEgZnJvbSB0aGUgZGlzaz8nLFxuICAgICAgICAgICAgdHlwZVxuICAgICAgICAgICksXG4gICAgICAgICAgYnV0dG9uczogW1xuICAgICAgICAgICAgRGlhbG9nLmNhbmNlbEJ1dHRvbigpLFxuICAgICAgICAgICAgRGlhbG9nLndhcm5CdXR0b24oeyBsYWJlbDogdHJhbnMuX18oJ1JlbG9hZCcpIH0pXG4gICAgICAgICAgXVxuICAgICAgICB9KS50aGVuKHJlc3VsdCA9PiB7XG4gICAgICAgICAgaWYgKHJlc3VsdC5idXR0b24uYWNjZXB0ICYmICFjb250ZXh0LmlzRGlzcG9zZWQpIHtcbiAgICAgICAgICAgIHJldHVybiBjb250ZXh0LnJldmVydCgpO1xuICAgICAgICAgIH1cbiAgICAgICAgfSk7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICBpZiAoIWNvbnRleHQuaXNEaXNwb3NlZCkge1xuICAgICAgICAgIHJldHVybiBjb250ZXh0LnJldmVydCgpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfVxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMucmVzdG9yZUNoZWNrcG9pbnQsIHtcbiAgICBsYWJlbDogKCkgPT5cbiAgICAgIHRyYW5zLl9fKFxuICAgICAgICAnUmV2ZXJ0ICUxIHRvIENoZWNrcG9pbnTigKYnLFxuICAgICAgICBmaWxlVHlwZShzaGVsbC5jdXJyZW50V2lkZ2V0LCBkb2NNYW5hZ2VyKVxuICAgICAgKSxcbiAgICBjYXB0aW9uOiB0cmFucy5fXygnUmV2ZXJ0IGNvbnRlbnRzIHRvIHByZXZpb3VzIGNoZWNrcG9pbnQnKSxcbiAgICBpc0VuYWJsZWQsXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgLy8gQ2hlY2tzIHRoYXQgc2hlbGwuY3VycmVudFdpZGdldCBpcyB2YWxpZDpcbiAgICAgIGlmICghaXNFbmFibGVkKCkpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgY29uc3QgY29udGV4dCA9IGRvY01hbmFnZXIuY29udGV4dEZvcldpZGdldChzaGVsbC5jdXJyZW50V2lkZ2V0ISk7XG4gICAgICBpZiAoIWNvbnRleHQpIHtcbiAgICAgICAgcmV0dXJuIHNob3dEaWFsb2coe1xuICAgICAgICAgIHRpdGxlOiB0cmFucy5fXygnQ2Fubm90IFJldmVydCcpLFxuICAgICAgICAgIGJvZHk6IHRyYW5zLl9fKCdObyBjb250ZXh0IGZvdW5kIGZvciBjdXJyZW50IHdpZGdldCEnKSxcbiAgICAgICAgICBidXR0b25zOiBbRGlhbG9nLm9rQnV0dG9uKCldXG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgICAgcmV0dXJuIGNvbnRleHQubGlzdENoZWNrcG9pbnRzKCkudGhlbihhc3luYyBjaGVja3BvaW50cyA9PiB7XG4gICAgICAgIGNvbnN0IHR5cGUgPSBmaWxlVHlwZShzaGVsbC5jdXJyZW50V2lkZ2V0LCBkb2NNYW5hZ2VyKTtcbiAgICAgICAgaWYgKGNoZWNrcG9pbnRzLmxlbmd0aCA8IDEpIHtcbiAgICAgICAgICBhd2FpdCBzaG93RXJyb3JNZXNzYWdlKFxuICAgICAgICAgICAgdHJhbnMuX18oJ05vIGNoZWNrcG9pbnRzJyksXG4gICAgICAgICAgICB0cmFucy5fXygnTm8gY2hlY2twb2ludHMgYXJlIGF2YWlsYWJsZSBmb3IgdGhpcyAlMS4nLCB0eXBlKVxuICAgICAgICAgICk7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IHRhcmdldENoZWNrcG9pbnQgPVxuICAgICAgICAgIGNoZWNrcG9pbnRzLmxlbmd0aCA9PT0gMVxuICAgICAgICAgICAgPyBjaGVja3BvaW50c1swXVxuICAgICAgICAgICAgOiBhd2FpdCBQcml2YXRlLmdldFRhcmdldENoZWNrcG9pbnQoY2hlY2twb2ludHMucmV2ZXJzZSgpLCB0cmFucyk7XG5cbiAgICAgICAgaWYgKCF0YXJnZXRDaGVja3BvaW50KSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiBzaG93RGlhbG9nKHtcbiAgICAgICAgICB0aXRsZTogdHJhbnMuX18oJ1JldmVydCAlMSB0byBjaGVja3BvaW50JywgdHlwZSksXG4gICAgICAgICAgYm9keTogbmV3IFJldmVydENvbmZpcm1XaWRnZXQodGFyZ2V0Q2hlY2twb2ludCwgdHJhbnMsIHR5cGUpLFxuICAgICAgICAgIGJ1dHRvbnM6IFtcbiAgICAgICAgICAgIERpYWxvZy5jYW5jZWxCdXR0b24oKSxcbiAgICAgICAgICAgIERpYWxvZy53YXJuQnV0dG9uKHsgbGFiZWw6IHRyYW5zLl9fKCdSZXZlcnQnKSB9KVxuICAgICAgICAgIF1cbiAgICAgICAgfSkudGhlbihyZXN1bHQgPT4ge1xuICAgICAgICAgIGlmIChjb250ZXh0LmlzRGlzcG9zZWQpIHtcbiAgICAgICAgICAgIHJldHVybjtcbiAgICAgICAgICB9XG4gICAgICAgICAgaWYgKHJlc3VsdC5idXR0b24uYWNjZXB0KSB7XG4gICAgICAgICAgICBpZiAoY29udGV4dC5tb2RlbC5yZWFkT25seSkge1xuICAgICAgICAgICAgICByZXR1cm4gY29udGV4dC5yZXZlcnQoKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIHJldHVybiBjb250ZXh0XG4gICAgICAgICAgICAgIC5yZXN0b3JlQ2hlY2twb2ludCh0YXJnZXRDaGVja3BvaW50LmlkKVxuICAgICAgICAgICAgICAudGhlbigoKSA9PiBjb250ZXh0LnJldmVydCgpKTtcbiAgICAgICAgICB9XG4gICAgICAgIH0pO1xuICAgICAgfSk7XG4gICAgfVxuICB9KTtcblxuICBjb25zdCBjYXB0aW9uID0gKCkgPT4ge1xuICAgIGlmIChQYWdlQ29uZmlnLmdldE9wdGlvbignY29sbGFib3JhdGl2ZScpID09ICd0cnVlJykge1xuICAgICAgcmV0dXJuIHRyYW5zLl9fKFxuICAgICAgICAnSW4gY29sbGFib3JhdGl2ZSBtb2RlLCB0aGUgZG9jdW1lbnQgaXMgc2F2ZWQgYXV0b21hdGljYWxseSBhZnRlciBldmVyeSBjaGFuZ2UnXG4gICAgICApO1xuICAgIH0gZWxzZSB7XG4gICAgICByZXR1cm4gdHJhbnMuX18oJ1NhdmUgYW5kIGNyZWF0ZSBjaGVja3BvaW50Jyk7XG4gICAgfVxuICB9O1xuXG4gIGNvbnN0IHNhdmVJblByb2dyZXNzID0gbmV3IFdlYWtTZXQ8RG9jdW1lbnRSZWdpc3RyeS5Db250ZXh0PigpO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5zYXZlLCB7XG4gICAgbGFiZWw6ICgpID0+IHRyYW5zLl9fKCdTYXZlICUxJywgZmlsZVR5cGUoc2hlbGwuY3VycmVudFdpZGdldCwgZG9jTWFuYWdlcikpLFxuICAgIGNhcHRpb24sXG4gICAgaWNvbjogYXJncyA9PiAoYXJncy50b29sYmFyID8gc2F2ZUljb24gOiAnJyksXG4gICAgaXNFbmFibGVkOiBpc1dyaXRhYmxlLFxuICAgIGV4ZWN1dGU6IGFzeW5jICgpID0+IHtcbiAgICAgIC8vIENoZWNrcyB0aGF0IHNoZWxsLmN1cnJlbnRXaWRnZXQgaXMgdmFsaWQ6XG4gICAgICBpZiAoaXNFbmFibGVkKCkpIHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gc2hlbGwuY3VycmVudFdpZGdldDtcbiAgICAgICAgY29uc3QgY29udGV4dCA9IGRvY01hbmFnZXIuY29udGV4dEZvcldpZGdldCh3aWRnZXQhKTtcbiAgICAgICAgaWYgKCFjb250ZXh0KSB7XG4gICAgICAgICAgcmV0dXJuIHNob3dEaWFsb2coe1xuICAgICAgICAgICAgdGl0bGU6IHRyYW5zLl9fKCdDYW5ub3QgU2F2ZScpLFxuICAgICAgICAgICAgYm9keTogdHJhbnMuX18oJ05vIGNvbnRleHQgZm91bmQgZm9yIGN1cnJlbnQgd2lkZ2V0IScpLFxuICAgICAgICAgICAgYnV0dG9uczogW0RpYWxvZy5va0J1dHRvbigpXVxuICAgICAgICAgIH0pO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIGlmIChzYXZlSW5Qcm9ncmVzcy5oYXMoY29udGV4dCkpIHtcbiAgICAgICAgICAgIHJldHVybjtcbiAgICAgICAgICB9XG5cbiAgICAgICAgICBpZiAoY29udGV4dC5tb2RlbC5yZWFkT25seSkge1xuICAgICAgICAgICAgcmV0dXJuIHNob3dEaWFsb2coe1xuICAgICAgICAgICAgICB0aXRsZTogdHJhbnMuX18oJ0Nhbm5vdCBTYXZlJyksXG4gICAgICAgICAgICAgIGJvZHk6IHRyYW5zLl9fKCdEb2N1bWVudCBpcyByZWFkLW9ubHknKSxcbiAgICAgICAgICAgICAgYnV0dG9uczogW0RpYWxvZy5va0J1dHRvbigpXVxuICAgICAgICAgICAgfSk7XG4gICAgICAgICAgfVxuXG4gICAgICAgICAgc2F2ZUluUHJvZ3Jlc3MuYWRkKGNvbnRleHQpO1xuXG4gICAgICAgICAgY29uc3Qgb2xkTmFtZSA9IFBhdGhFeHQuYmFzZW5hbWUoY29udGV4dC5jb250ZW50c01vZGVsPy5wYXRoID8/ICcnKTtcbiAgICAgICAgICBsZXQgbmV3TmFtZSA9IG9sZE5hbWU7XG5cbiAgICAgICAgICBpZiAoXG4gICAgICAgICAgICBkb2NNYW5hZ2VyLnJlbmFtZVVudGl0bGVkRmlsZU9uU2F2ZSAmJlxuICAgICAgICAgICAgKHdpZGdldCBhcyBJRG9jdW1lbnRXaWRnZXQpLmlzVW50aXRsZWQgPT09IHRydWVcbiAgICAgICAgICApIHtcbiAgICAgICAgICAgIGNvbnN0IHJlc3VsdCA9IGF3YWl0IElucHV0RGlhbG9nLmdldFRleHQoe1xuICAgICAgICAgICAgICB0aXRsZTogdHJhbnMuX18oJ1JlbmFtZSBmaWxlJyksXG4gICAgICAgICAgICAgIG9rTGFiZWw6IHRyYW5zLl9fKCdSZW5hbWUnKSxcbiAgICAgICAgICAgICAgcGxhY2Vob2xkZXI6IHRyYW5zLl9fKCdGaWxlIG5hbWUnKSxcbiAgICAgICAgICAgICAgdGV4dDogb2xkTmFtZSxcbiAgICAgICAgICAgICAgc2VsZWN0aW9uUmFuZ2U6IG9sZE5hbWUubGVuZ3RoIC0gUGF0aEV4dC5leHRuYW1lKG9sZE5hbWUpLmxlbmd0aCxcbiAgICAgICAgICAgICAgY2hlY2tib3g6IHtcbiAgICAgICAgICAgICAgICBsYWJlbDogdHJhbnMuX18oXCJEb24ndCBhc2sgbWUgYWdhaW4uXCIpLFxuICAgICAgICAgICAgICAgIGNhcHRpb246IHRyYW5zLl9fKFxuICAgICAgICAgICAgICAgICAgJ0lmIGNoZWNrZWQsIHlvdSB3aWxsIG5vdCBiZSBhc2tlZCB0byByZW5hbWUgZnV0dXJlIHVudGl0bGVkIGZpbGVzIHdoZW4gc2F2aW5nIHRoZW0uJ1xuICAgICAgICAgICAgICAgIClcbiAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfSk7XG5cbiAgICAgICAgICAgIGlmIChyZXN1bHQuYnV0dG9uLmFjY2VwdCkge1xuICAgICAgICAgICAgICBuZXdOYW1lID0gcmVzdWx0LnZhbHVlID8/IG9sZE5hbWU7XG4gICAgICAgICAgICAgICh3aWRnZXQgYXMgSURvY3VtZW50V2lkZ2V0KS5pc1VudGl0bGVkID0gZmFsc2U7XG4gICAgICAgICAgICAgIGlmICh0eXBlb2YgcmVzdWx0LmlzQ2hlY2tlZCA9PT0gJ2Jvb2xlYW4nKSB7XG4gICAgICAgICAgICAgICAgY29uc3QgY3VycmVudFNldHRpbmcgPSAoXG4gICAgICAgICAgICAgICAgICBhd2FpdCBzZXR0aW5nUmVnaXN0cnkuZ2V0KFxuICAgICAgICAgICAgICAgICAgICBkb2NNYW5hZ2VyUGx1Z2luSWQsXG4gICAgICAgICAgICAgICAgICAgICdyZW5hbWVVbnRpdGxlZEZpbGVPblNhdmUnXG4gICAgICAgICAgICAgICAgICApXG4gICAgICAgICAgICAgICAgKS5jb21wb3NpdGUgYXMgYm9vbGVhbjtcbiAgICAgICAgICAgICAgICBpZiAocmVzdWx0LmlzQ2hlY2tlZCA9PT0gY3VycmVudFNldHRpbmcpIHtcbiAgICAgICAgICAgICAgICAgIHNldHRpbmdSZWdpc3RyeVxuICAgICAgICAgICAgICAgICAgICAuc2V0KFxuICAgICAgICAgICAgICAgICAgICAgIGRvY01hbmFnZXJQbHVnaW5JZCxcbiAgICAgICAgICAgICAgICAgICAgICAncmVuYW1lVW50aXRsZWRGaWxlT25TYXZlJyxcbiAgICAgICAgICAgICAgICAgICAgICAhcmVzdWx0LmlzQ2hlY2tlZFxuICAgICAgICAgICAgICAgICAgICApXG4gICAgICAgICAgICAgICAgICAgIC5jYXRjaChyZWFzb24gPT4ge1xuICAgICAgICAgICAgICAgICAgICAgIGNvbnNvbGUuZXJyb3IoXG4gICAgICAgICAgICAgICAgICAgICAgICBgRmFpbCB0byBzZXQgJ3JlbmFtZVVudGl0bGVkRmlsZU9uU2F2ZTpcXG4ke3JlYXNvbn1gXG4gICAgICAgICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICB9XG4gICAgICAgICAgICB9XG4gICAgICAgICAgfVxuXG4gICAgICAgICAgdHJ5IHtcbiAgICAgICAgICAgIGF3YWl0IGNvbnRleHQuc2F2ZSgpO1xuXG4gICAgICAgICAgICBpZiAoIXdpZGdldD8uaXNEaXNwb3NlZCkge1xuICAgICAgICAgICAgICByZXR1cm4gY29udGV4dCEuY3JlYXRlQ2hlY2twb2ludCgpO1xuICAgICAgICAgICAgfVxuICAgICAgICAgIH0gY2F0Y2ggKGVycikge1xuICAgICAgICAgICAgLy8gSWYgdGhlIHNhdmUgd2FzIGNhbmNlbGVkIGJ5IHVzZXItYWN0aW9uLCBkbyBub3RoaW5nLlxuICAgICAgICAgICAgaWYgKGVyci5uYW1lID09PSAnTW9kYWxDYW5jZWxFcnJvcicpIHtcbiAgICAgICAgICAgICAgcmV0dXJuO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgdGhyb3cgZXJyO1xuICAgICAgICAgIH0gZmluYWxseSB7XG4gICAgICAgICAgICBzYXZlSW5Qcm9ncmVzcy5kZWxldGUoY29udGV4dCk7XG4gICAgICAgICAgICBpZiAobmV3TmFtZSAhPT0gb2xkTmFtZSkge1xuICAgICAgICAgICAgICBhd2FpdCBjb250ZXh0LnJlbmFtZShuZXdOYW1lKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9XG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5zYXZlQWxsLCB7XG4gICAgbGFiZWw6ICgpID0+IHRyYW5zLl9fKCdTYXZlIEFsbCcpLFxuICAgIGNhcHRpb246IHRyYW5zLl9fKCdTYXZlIGFsbCBvcGVuIGRvY3VtZW50cycpLFxuICAgIGlzRW5hYmxlZDogKCkgPT4ge1xuICAgICAgcmV0dXJuIHNvbWUoXG4gICAgICAgIG1hcChzaGVsbC53aWRnZXRzKCdtYWluJyksIHcgPT4gZG9jTWFuYWdlci5jb250ZXh0Rm9yV2lkZ2V0KHcpKSxcbiAgICAgICAgYyA9PiBjPy5jb250ZW50c01vZGVsPy53cml0YWJsZSA/PyBmYWxzZVxuICAgICAgKTtcbiAgICB9LFxuICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgIGNvbnN0IHByb21pc2VzOiBQcm9taXNlPHZvaWQ+W10gPSBbXTtcbiAgICAgIGNvbnN0IHBhdGhzID0gbmV3IFNldDxzdHJpbmc+KCk7IC8vIENhY2hlIHNvIHdlIGRvbid0IGRvdWJsZSBzYXZlIGZpbGVzLlxuICAgICAgZWFjaChzaGVsbC53aWRnZXRzKCdtYWluJyksIHdpZGdldCA9PiB7XG4gICAgICAgIGNvbnN0IGNvbnRleHQgPSBkb2NNYW5hZ2VyLmNvbnRleHRGb3JXaWRnZXQod2lkZ2V0KTtcbiAgICAgICAgaWYgKGNvbnRleHQgJiYgIWNvbnRleHQubW9kZWwucmVhZE9ubHkgJiYgIXBhdGhzLmhhcyhjb250ZXh0LnBhdGgpKSB7XG4gICAgICAgICAgcGF0aHMuYWRkKGNvbnRleHQucGF0aCk7XG4gICAgICAgICAgcHJvbWlzZXMucHVzaChjb250ZXh0LnNhdmUoKSk7XG4gICAgICAgIH1cbiAgICAgIH0pO1xuICAgICAgcmV0dXJuIFByb21pc2UuYWxsKHByb21pc2VzKTtcbiAgICB9XG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5zYXZlQXMsIHtcbiAgICBsYWJlbDogKCkgPT5cbiAgICAgIHRyYW5zLl9fKCdTYXZlICUxIEFz4oCmJywgZmlsZVR5cGUoc2hlbGwuY3VycmVudFdpZGdldCwgZG9jTWFuYWdlcikpLFxuICAgIGNhcHRpb246IHRyYW5zLl9fKCdTYXZlIHdpdGggbmV3IHBhdGgnKSxcbiAgICBpc0VuYWJsZWQsXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgLy8gQ2hlY2tzIHRoYXQgc2hlbGwuY3VycmVudFdpZGdldCBpcyB2YWxpZDpcbiAgICAgIGlmIChpc0VuYWJsZWQoKSkge1xuICAgICAgICBjb25zdCBjb250ZXh0ID0gZG9jTWFuYWdlci5jb250ZXh0Rm9yV2lkZ2V0KHNoZWxsLmN1cnJlbnRXaWRnZXQhKTtcbiAgICAgICAgaWYgKCFjb250ZXh0KSB7XG4gICAgICAgICAgcmV0dXJuIHNob3dEaWFsb2coe1xuICAgICAgICAgICAgdGl0bGU6IHRyYW5zLl9fKCdDYW5ub3QgU2F2ZScpLFxuICAgICAgICAgICAgYm9keTogdHJhbnMuX18oJ05vIGNvbnRleHQgZm91bmQgZm9yIGN1cnJlbnQgd2lkZ2V0IScpLFxuICAgICAgICAgICAgYnV0dG9uczogW0RpYWxvZy5va0J1dHRvbigpXVxuICAgICAgICAgIH0pO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiBjb250ZXh0LnNhdmVBcygpO1xuICAgICAgfVxuICAgIH1cbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnRvZ2dsZUF1dG9zYXZlLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdBdXRvc2F2ZSBEb2N1bWVudHMnKSxcbiAgICBpc1RvZ2dsZWQ6ICgpID0+IGRvY01hbmFnZXIuYXV0b3NhdmUsXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgY29uc3QgdmFsdWUgPSAhZG9jTWFuYWdlci5hdXRvc2F2ZTtcbiAgICAgIGNvbnN0IGtleSA9ICdhdXRvc2F2ZSc7XG4gICAgICByZXR1cm4gc2V0dGluZ1JlZ2lzdHJ5XG4gICAgICAgIC5zZXQoZG9jTWFuYWdlclBsdWdpbklkLCBrZXksIHZhbHVlKVxuICAgICAgICAuY2F0Y2goKHJlYXNvbjogRXJyb3IpID0+IHtcbiAgICAgICAgICBjb25zb2xlLmVycm9yKFxuICAgICAgICAgICAgYEZhaWxlZCB0byBzZXQgJHtkb2NNYW5hZ2VyUGx1Z2luSWR9OiR7a2V5fSAtICR7cmVhc29uLm1lc3NhZ2V9YFxuICAgICAgICAgICk7XG4gICAgICAgIH0pO1xuICAgIH1cbiAgfSk7XG5cbiAgaWYgKHBhbGV0dGUpIHtcbiAgICBbXG4gICAgICBDb21tYW5kSURzLnJlbG9hZCxcbiAgICAgIENvbW1hbmRJRHMucmVzdG9yZUNoZWNrcG9pbnQsXG4gICAgICBDb21tYW5kSURzLnNhdmUsXG4gICAgICBDb21tYW5kSURzLnNhdmVBcyxcbiAgICAgIENvbW1hbmRJRHMudG9nZ2xlQXV0b3NhdmUsXG4gICAgICBDb21tYW5kSURzLmR1cGxpY2F0ZVxuICAgIF0uZm9yRWFjaChjb21tYW5kID0+IHtcbiAgICAgIHBhbGV0dGUuYWRkSXRlbSh7IGNvbW1hbmQsIGNhdGVnb3J5IH0pO1xuICAgIH0pO1xuICB9XG59XG5cbmZ1bmN0aW9uIGFkZExhYkNvbW1hbmRzKFxuICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgZG9jTWFuYWdlcjogSURvY3VtZW50TWFuYWdlcixcbiAgbGFiU2hlbGw6IElMYWJTaGVsbCxcbiAgb3BlbmVyOiBEb2N1bWVudE1hbmFnZXIuSVdpZGdldE9wZW5lcixcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3Jcbik6IHZvaWQge1xuICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICBjb25zdCB7IGNvbW1hbmRzIH0gPSBhcHA7XG5cbiAgLy8gUmV0dXJucyB0aGUgZG9jIHdpZGdldCBhc3NvY2lhdGVkIHdpdGggdGhlIG1vc3QgcmVjZW50IGNvbnRleHRtZW51IGV2ZW50LlxuICBjb25zdCBjb250ZXh0TWVudVdpZGdldCA9ICgpOiBXaWRnZXQgfCBudWxsID0+IHtcbiAgICBjb25zdCBwYXRoUmUgPSAvW1BwXWF0aDpcXHM/KC4qKVxcbj8vO1xuICAgIGNvbnN0IHRlc3QgPSAobm9kZTogSFRNTEVsZW1lbnQpID0+ICEhbm9kZVsndGl0bGUnXT8ubWF0Y2gocGF0aFJlKTtcbiAgICBjb25zdCBub2RlID0gYXBwLmNvbnRleHRNZW51SGl0VGVzdCh0ZXN0KTtcblxuICAgIGNvbnN0IHBhdGhNYXRjaCA9IG5vZGU/LlsndGl0bGUnXS5tYXRjaChwYXRoUmUpO1xuICAgIHJldHVybiAoXG4gICAgICAocGF0aE1hdGNoICYmIGRvY01hbmFnZXIuZmluZFdpZGdldChwYXRoTWF0Y2hbMV0sIG51bGwpKSA/P1xuICAgICAgLy8gRmFsbCBiYWNrIHRvIGFjdGl2ZSBkb2Mgd2lkZ2V0IGlmIHBhdGggY2Fubm90IGJlIG9idGFpbmVkIGZyb20gZXZlbnQuXG4gICAgICBsYWJTaGVsbC5jdXJyZW50V2lkZ2V0XG4gICAgKTtcbiAgfTtcblxuICAvLyBSZXR1cm5zIGB0cnVlYCBpZiB0aGUgY3VycmVudCB3aWRnZXQgaGFzIGEgZG9jdW1lbnQgY29udGV4dC5cbiAgY29uc3QgaXNFbmFibGVkID0gKCkgPT4ge1xuICAgIGNvbnN0IHsgY3VycmVudFdpZGdldCB9ID0gbGFiU2hlbGw7XG4gICAgcmV0dXJuICEhKGN1cnJlbnRXaWRnZXQgJiYgZG9jTWFuYWdlci5jb250ZXh0Rm9yV2lkZ2V0KGN1cnJlbnRXaWRnZXQpKTtcbiAgfTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY2xvbmUsIHtcbiAgICBsYWJlbDogKCkgPT5cbiAgICAgIHRyYW5zLl9fKCdOZXcgVmlldyBmb3IgJTEnLCBmaWxlVHlwZShjb250ZXh0TWVudVdpZGdldCgpLCBkb2NNYW5hZ2VyKSksXG4gICAgaXNFbmFibGVkLFxuICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgY29uc3Qgd2lkZ2V0ID0gY29udGV4dE1lbnVXaWRnZXQoKTtcbiAgICAgIGNvbnN0IG9wdGlvbnMgPSAoYXJnc1snb3B0aW9ucyddIGFzIERvY3VtZW50UmVnaXN0cnkuSU9wZW5PcHRpb25zKSB8fCB7XG4gICAgICAgIG1vZGU6ICdzcGxpdC1yaWdodCdcbiAgICAgIH07XG4gICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICAvLyBDbG9uZSB0aGUgd2lkZ2V0LlxuICAgICAgY29uc3QgY2hpbGQgPSBkb2NNYW5hZ2VyLmNsb25lV2lkZ2V0KHdpZGdldCk7XG4gICAgICBpZiAoY2hpbGQpIHtcbiAgICAgICAgb3BlbmVyLm9wZW4oY2hpbGQsIG9wdGlvbnMpO1xuICAgICAgfVxuICAgIH1cbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnJlbmFtZSwge1xuICAgIGxhYmVsOiAoKSA9PiB7XG4gICAgICBsZXQgdCA9IGZpbGVUeXBlKGNvbnRleHRNZW51V2lkZ2V0KCksIGRvY01hbmFnZXIpO1xuICAgICAgaWYgKHQpIHtcbiAgICAgICAgdCA9ICcgJyArIHQ7XG4gICAgICB9XG4gICAgICByZXR1cm4gdHJhbnMuX18oJ1JlbmFtZSUx4oCmJywgdCk7XG4gICAgfSxcbiAgICBpc0VuYWJsZWQsXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgLy8gSW1wbGllcyBjb250ZXh0TWVudVdpZGdldCgpICE9PSBudWxsXG4gICAgICBpZiAoaXNFbmFibGVkKCkpIHtcbiAgICAgICAgY29uc3QgY29udGV4dCA9IGRvY01hbmFnZXIuY29udGV4dEZvcldpZGdldChjb250ZXh0TWVudVdpZGdldCgpISk7XG4gICAgICAgIHJldHVybiByZW5hbWVEaWFsb2coZG9jTWFuYWdlciwgY29udGV4dCEpO1xuICAgICAgfVxuICAgIH1cbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmR1cGxpY2F0ZSwge1xuICAgIGxhYmVsOiAoKSA9PlxuICAgICAgdHJhbnMuX18oJ0R1cGxpY2F0ZSAlMScsIGZpbGVUeXBlKGNvbnRleHRNZW51V2lkZ2V0KCksIGRvY01hbmFnZXIpKSxcbiAgICBpc0VuYWJsZWQsXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgaWYgKGlzRW5hYmxlZCgpKSB7XG4gICAgICAgIGNvbnN0IGNvbnRleHQgPSBkb2NNYW5hZ2VyLmNvbnRleHRGb3JXaWRnZXQoY29udGV4dE1lbnVXaWRnZXQoKSEpO1xuICAgICAgICBpZiAoIWNvbnRleHQpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIGRvY01hbmFnZXIuZHVwbGljYXRlKGNvbnRleHQucGF0aCk7XG4gICAgICB9XG4gICAgfVxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuZGVsLCB7XG4gICAgbGFiZWw6ICgpID0+XG4gICAgICB0cmFucy5fXygnRGVsZXRlICUxJywgZmlsZVR5cGUoY29udGV4dE1lbnVXaWRnZXQoKSwgZG9jTWFuYWdlcikpLFxuICAgIGlzRW5hYmxlZCxcbiAgICBleGVjdXRlOiBhc3luYyAoKSA9PiB7XG4gICAgICAvLyBJbXBsaWVzIGNvbnRleHRNZW51V2lkZ2V0KCkgIT09IG51bGxcbiAgICAgIGlmIChpc0VuYWJsZWQoKSkge1xuICAgICAgICBjb25zdCBjb250ZXh0ID0gZG9jTWFuYWdlci5jb250ZXh0Rm9yV2lkZ2V0KGNvbnRleHRNZW51V2lkZ2V0KCkhKTtcbiAgICAgICAgaWYgKCFjb250ZXh0KSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IHJlc3VsdCA9IGF3YWl0IHNob3dEaWFsb2coe1xuICAgICAgICAgIHRpdGxlOiB0cmFucy5fXygnRGVsZXRlJyksXG4gICAgICAgICAgYm9keTogdHJhbnMuX18oJ0FyZSB5b3Ugc3VyZSB5b3Ugd2FudCB0byBkZWxldGUgJTEnLCBjb250ZXh0LnBhdGgpLFxuICAgICAgICAgIGJ1dHRvbnM6IFtcbiAgICAgICAgICAgIERpYWxvZy5jYW5jZWxCdXR0b24oKSxcbiAgICAgICAgICAgIERpYWxvZy53YXJuQnV0dG9uKHsgbGFiZWw6IHRyYW5zLl9fKCdEZWxldGUnKSB9KVxuICAgICAgICAgIF1cbiAgICAgICAgfSk7XG5cbiAgICAgICAgaWYgKHJlc3VsdC5idXR0b24uYWNjZXB0KSB7XG4gICAgICAgICAgYXdhaXQgYXBwLmNvbW1hbmRzLmV4ZWN1dGUoJ2RvY21hbmFnZXI6ZGVsZXRlLWZpbGUnLCB7XG4gICAgICAgICAgICBwYXRoOiBjb250ZXh0LnBhdGhcbiAgICAgICAgICB9KTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH1cbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnNob3dJbkZpbGVCcm93c2VyLCB7XG4gICAgbGFiZWw6ICgpID0+IHRyYW5zLl9fKCdTaG93IGluIEZpbGUgQnJvd3NlcicpLFxuICAgIGlzRW5hYmxlZCxcbiAgICBleGVjdXRlOiBhc3luYyAoKSA9PiB7XG4gICAgICBjb25zdCB3aWRnZXQgPSBjb250ZXh0TWVudVdpZGdldCgpO1xuICAgICAgY29uc3QgY29udGV4dCA9IHdpZGdldCAmJiBkb2NNYW5hZ2VyLmNvbnRleHRGb3JXaWRnZXQod2lkZ2V0KTtcbiAgICAgIGlmICghY29udGV4dCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG5cbiAgICAgIC8vICdhY3RpdmF0ZScgaXMgbmVlZGVkIGlmIHRoaXMgY29tbWFuZCBpcyBzZWxlY3RlZCBpbiB0aGUgXCJvcGVuIHRhYnNcIiBzaWRlYmFyXG4gICAgICBhd2FpdCBjb21tYW5kcy5leGVjdXRlKCdmaWxlYnJvd3NlcjphY3RpdmF0ZScsIHsgcGF0aDogY29udGV4dC5wYXRoIH0pO1xuICAgICAgYXdhaXQgY29tbWFuZHMuZXhlY3V0ZSgnZmlsZWJyb3dzZXI6Z28tdG8tcGF0aCcsIHsgcGF0aDogY29udGV4dC5wYXRoIH0pO1xuICAgIH1cbiAgfSk7XG59XG5cbi8qKlxuICogSGFuZGxlIGRpcnR5IHN0YXRlIGZvciBhIGNvbnRleHQuXG4gKi9cbmZ1bmN0aW9uIGhhbmRsZUNvbnRleHQoXG4gIHN0YXR1czogSUxhYlN0YXR1cyxcbiAgY29udGV4dDogRG9jdW1lbnRSZWdpc3RyeS5Db250ZXh0XG4pOiB2b2lkIHtcbiAgbGV0IGRpc3Bvc2FibGU6IElEaXNwb3NhYmxlIHwgbnVsbCA9IG51bGw7XG4gIGNvbnN0IG9uU3RhdGVDaGFuZ2VkID0gKHNlbmRlcjogYW55LCBhcmdzOiBJQ2hhbmdlZEFyZ3M8YW55PikgPT4ge1xuICAgIGlmIChhcmdzLm5hbWUgPT09ICdkaXJ0eScpIHtcbiAgICAgIGlmIChhcmdzLm5ld1ZhbHVlID09PSB0cnVlKSB7XG4gICAgICAgIGlmICghZGlzcG9zYWJsZSkge1xuICAgICAgICAgIGRpc3Bvc2FibGUgPSBzdGF0dXMuc2V0RGlydHkoKTtcbiAgICAgICAgfVxuICAgICAgfSBlbHNlIGlmIChkaXNwb3NhYmxlKSB7XG4gICAgICAgIGRpc3Bvc2FibGUuZGlzcG9zZSgpO1xuICAgICAgICBkaXNwb3NhYmxlID0gbnVsbDtcbiAgICAgIH1cbiAgICB9XG4gIH07XG4gIHZvaWQgY29udGV4dC5yZWFkeS50aGVuKCgpID0+IHtcbiAgICBjb250ZXh0Lm1vZGVsLnN0YXRlQ2hhbmdlZC5jb25uZWN0KG9uU3RhdGVDaGFuZ2VkKTtcbiAgICBpZiAoY29udGV4dC5tb2RlbC5kaXJ0eSkge1xuICAgICAgZGlzcG9zYWJsZSA9IHN0YXR1cy5zZXREaXJ0eSgpO1xuICAgIH1cbiAgfSk7XG4gIGNvbnRleHQuZGlzcG9zZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgaWYgKGRpc3Bvc2FibGUpIHtcbiAgICAgIGRpc3Bvc2FibGUuZGlzcG9zZSgpO1xuICAgIH1cbiAgfSk7XG59XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIHByaXZhdGUgbW9kdWxlIGRhdGEuXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgLyoqXG4gICAqIEEgY291bnRlciBmb3IgdW5pcXVlIElEcy5cbiAgICovXG4gIGV4cG9ydCBsZXQgaWQgPSAwO1xuXG4gIGV4cG9ydCBmdW5jdGlvbiBjcmVhdGVSZXZlcnRDb25maXJtTm9kZShcbiAgICBjaGVja3BvaW50OiBDb250ZW50cy5JQ2hlY2twb2ludE1vZGVsLFxuICAgIGZpbGVUeXBlOiBzdHJpbmcsXG4gICAgdHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlXG4gICk6IEhUTUxFbGVtZW50IHtcbiAgICBjb25zdCBib2R5ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2Jyk7XG4gICAgY29uc3QgY29uZmlybU1lc3NhZ2UgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdwJyk7XG4gICAgY29uc3QgY29uZmlybVRleHQgPSBkb2N1bWVudC5jcmVhdGVUZXh0Tm9kZShcbiAgICAgIHRyYW5zLl9fKFxuICAgICAgICAnQXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHJldmVydCB0aGUgJTEgdG8gY2hlY2twb2ludD8gJyxcbiAgICAgICAgZmlsZVR5cGVcbiAgICAgIClcbiAgICApO1xuICAgIGNvbnN0IGNhbm5vdFVuZG9UZXh0ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3Ryb25nJyk7XG4gICAgY2Fubm90VW5kb1RleHQudGV4dENvbnRlbnQgPSB0cmFucy5fXygnVGhpcyBjYW5ub3QgYmUgdW5kb25lLicpO1xuXG4gICAgY29uZmlybU1lc3NhZ2UuYXBwZW5kQ2hpbGQoY29uZmlybVRleHQpO1xuICAgIGNvbmZpcm1NZXNzYWdlLmFwcGVuZENoaWxkKGNhbm5vdFVuZG9UZXh0KTtcblxuICAgIGNvbnN0IGxhc3RDaGVja3BvaW50TWVzc2FnZSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3AnKTtcbiAgICBjb25zdCBsYXN0Q2hlY2twb2ludFRleHQgPSBkb2N1bWVudC5jcmVhdGVUZXh0Tm9kZShcbiAgICAgIHRyYW5zLl9fKCdUaGUgY2hlY2twb2ludCB3YXMgbGFzdCB1cGRhdGVkIGF0OiAnKVxuICAgICk7XG4gICAgY29uc3QgbGFzdENoZWNrcG9pbnREYXRlID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgncCcpO1xuICAgIGNvbnN0IGRhdGUgPSBuZXcgRGF0ZShjaGVja3BvaW50Lmxhc3RfbW9kaWZpZWQpO1xuICAgIGxhc3RDaGVja3BvaW50RGF0ZS5zdHlsZS50ZXh0QWxpZ24gPSAnY2VudGVyJztcbiAgICBsYXN0Q2hlY2twb2ludERhdGUudGV4dENvbnRlbnQgPVxuICAgICAgVGltZS5mb3JtYXQoZGF0ZSwgJ2RkZGQsIE1NTU0gRG8gWVlZWSwgaDptbTpzcyBhJykgK1xuICAgICAgJyAoJyArXG4gICAgICBUaW1lLmZvcm1hdEh1bWFuKGRhdGUpICtcbiAgICAgICcpJztcblxuICAgIGxhc3RDaGVja3BvaW50TWVzc2FnZS5hcHBlbmRDaGlsZChsYXN0Q2hlY2twb2ludFRleHQpO1xuICAgIGxhc3RDaGVja3BvaW50TWVzc2FnZS5hcHBlbmRDaGlsZChsYXN0Q2hlY2twb2ludERhdGUpO1xuXG4gICAgYm9keS5hcHBlbmRDaGlsZChjb25maXJtTWVzc2FnZSk7XG4gICAgYm9keS5hcHBlbmRDaGlsZChsYXN0Q2hlY2twb2ludE1lc3NhZ2UpO1xuICAgIHJldHVybiBib2R5O1xuICB9XG5cbiAgLyoqXG4gICAqIEFzayB1c2VyIGZvciBhIGNoZWNrcG9pbnQgdG8gcmV2ZXJ0IHRvLlxuICAgKi9cbiAgZXhwb3J0IGFzeW5jIGZ1bmN0aW9uIGdldFRhcmdldENoZWNrcG9pbnQoXG4gICAgY2hlY2twb2ludHM6IENvbnRlbnRzLklDaGVja3BvaW50TW9kZWxbXSxcbiAgICB0cmFuczogVHJhbnNsYXRpb25CdW5kbGVcbiAgKTogUHJvbWlzZTxDb250ZW50cy5JQ2hlY2twb2ludE1vZGVsIHwgdW5kZWZpbmVkPiB7XG4gICAgLy8gdGhlIGlkIGNvdWxkIGJlIHRvbyBsb25nIHRvIHNob3cgc28gdXNlIHRoZSBpbmRleCBpbnN0ZWFkXG4gICAgY29uc3QgaW5kZXhTZXBhcmF0b3IgPSAnLic7XG4gICAgY29uc3QgaXRlbXMgPSBjaGVja3BvaW50cy5tYXAoKGNoZWNrcG9pbnQsIGluZGV4KSA9PiB7XG4gICAgICBjb25zdCBpc29EYXRlID0gVGltZS5mb3JtYXQoY2hlY2twb2ludC5sYXN0X21vZGlmaWVkKTtcbiAgICAgIGNvbnN0IGh1bWFuRGF0ZSA9IFRpbWUuZm9ybWF0SHVtYW4oY2hlY2twb2ludC5sYXN0X21vZGlmaWVkKTtcbiAgICAgIHJldHVybiBgJHtpbmRleH0ke2luZGV4U2VwYXJhdG9yfSAke2lzb0RhdGV9ICgke2h1bWFuRGF0ZX0pYDtcbiAgICB9KTtcblxuICAgIGNvbnN0IHNlbGVjdGVkSXRlbSA9IChcbiAgICAgIGF3YWl0IElucHV0RGlhbG9nLmdldEl0ZW0oe1xuICAgICAgICBpdGVtczogaXRlbXMsXG4gICAgICAgIHRpdGxlOiB0cmFucy5fXygnQ2hvb3NlIGEgY2hlY2twb2ludCcpXG4gICAgICB9KVxuICAgICkudmFsdWU7XG5cbiAgICBpZiAoIXNlbGVjdGVkSXRlbSkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBjb25zdCBzZWxlY3RlZEluZGV4ID0gc2VsZWN0ZWRJdGVtLnNwbGl0KGluZGV4U2VwYXJhdG9yLCAxKVswXTtcbiAgICByZXR1cm4gY2hlY2twb2ludHNbcGFyc2VJbnQoc2VsZWN0ZWRJbmRleCwgMTApXTtcbiAgfVxufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9