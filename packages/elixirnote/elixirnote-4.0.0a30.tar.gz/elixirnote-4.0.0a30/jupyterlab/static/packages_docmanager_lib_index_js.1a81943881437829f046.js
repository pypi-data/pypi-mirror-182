"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_docmanager_lib_index_js"],{

/***/ "../../packages/docmanager/lib/dialogs.js":
/*!************************************************!*\
  !*** ../../packages/docmanager/lib/dialogs.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "isValidFileName": () => (/* binding */ isValidFileName),
/* harmony export */   "renameDialog": () => (/* binding */ renameDialog),
/* harmony export */   "renameFile": () => (/* binding */ renameFile),
/* harmony export */   "shouldOverwrite": () => (/* binding */ shouldOverwrite)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_3__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




/**
 * The class name added to file dialogs.
 */
const FILE_DIALOG_CLASS = 'jp-FileDialog';
/**
 * The class name added for the new name label in the rename dialog
 */
const RENAME_NEW_NAME_TITLE_CLASS = 'jp-new-name-title';
/**
 * Rename a file with a dialog.
 */
function renameDialog(manager, context, translator) {
    translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.nullTranslator;
    const trans = translator.load('jupyterlab');
    const localPath = context.localPath.split('/');
    const fileName = localPath.pop() || context.localPath;
    return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showDialog)({
        title: trans.__('Rename File'),
        body: new RenameHandler(fileName),
        focusNodeSelector: 'input',
        buttons: [
            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.cancelButton(),
            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({ label: trans.__('Rename') })
        ]
    }).then(result => {
        if (!result.value) {
            return null;
        }
        if (!isValidFileName(result.value)) {
            void (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showErrorMessage)(trans.__('Rename Error'), Error(trans.__('"%1" is not a valid name for a file. Names must have nonzero length, and cannot include "/", "\\", or ":"', result.value)));
            return null;
        }
        return context.rename(result.value);
    });
}
/**
 * Rename a file, asking for confirmation if it is overwriting another.
 */
function renameFile(manager, oldPath, newPath) {
    return manager.rename(oldPath, newPath).catch(error => {
        if (error.response.status !== 409) {
            // if it's not caused by an already existing file, rethrow
            throw error;
        }
        // otherwise, ask for confirmation
        return shouldOverwrite(newPath).then((value) => {
            if (value) {
                return manager.overwrite(oldPath, newPath);
            }
            return Promise.reject('File not renamed');
        });
    });
}
/**
 * Ask the user whether to overwrite a file.
 */
function shouldOverwrite(path, translator) {
    translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.nullTranslator;
    const trans = translator.load('jupyterlab');
    const options = {
        title: trans.__('Overwrite file?'),
        body: trans.__('"%1" already exists, overwrite?', path),
        buttons: [
            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.cancelButton(),
            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.warnButton({ label: trans.__('Overwrite') })
        ]
    };
    return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showDialog)(options).then(result => {
        return Promise.resolve(result.button.accept);
    });
}
/**
 * Test whether a name is a valid file name
 *
 * Disallows "/", "\", and ":" in file names, as well as names with zero length.
 */
function isValidFileName(name) {
    const validNameExp = /[\/\\:]/;
    return name.length > 0 && !validNameExp.test(name);
}
/**
 * A widget used to rename a file.
 */
class RenameHandler extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.Widget {
    /**
     * Construct a new "rename" dialog.
     */
    constructor(oldPath) {
        super({ node: Private.createRenameNode(oldPath) });
        this.addClass(FILE_DIALOG_CLASS);
        const ext = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.PathExt.extname(oldPath);
        const value = (this.inputNode.value = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.PathExt.basename(oldPath));
        this.inputNode.setSelectionRange(0, value.length - ext.length);
    }
    /**
     * Get the input text node.
     */
    get inputNode() {
        return this.node.getElementsByTagName('input')[0];
    }
    /**
     * Get the value of the widget.
     */
    getValue() {
        return this.inputNode.value;
    }
}
/**
 * A namespace for private data.
 */
var Private;
(function (Private) {
    /**
     * Create the node for a rename handler.
     */
    function createRenameNode(oldPath, translator) {
        translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.nullTranslator;
        const trans = translator.load('jupyterlab');
        const body = document.createElement('div');
        const existingLabel = document.createElement('label');
        existingLabel.textContent = trans.__('File Path');
        const existingPath = document.createElement('span');
        existingPath.textContent = oldPath;
        const nameTitle = document.createElement('label');
        nameTitle.textContent = trans.__('New Name');
        nameTitle.className = RENAME_NEW_NAME_TITLE_CLASS;
        const name = document.createElement('input');
        body.appendChild(existingLabel);
        body.appendChild(existingPath);
        body.appendChild(nameTitle);
        body.appendChild(name);
        return body;
    }
    Private.createRenameNode = createRenameNode;
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/docmanager/lib/index.js":
/*!**********************************************!*\
  !*** ../../packages/docmanager/lib/index.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "DocumentManager": () => (/* reexport safe */ _manager__WEBPACK_IMPORTED_MODULE_1__.DocumentManager),
/* harmony export */   "DocumentWidgetManager": () => (/* reexport safe */ _widgetmanager__WEBPACK_IMPORTED_MODULE_6__.DocumentWidgetManager),
/* harmony export */   "IDocumentManager": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_5__.IDocumentManager),
/* harmony export */   "PathStatus": () => (/* reexport safe */ _pathstatus__WEBPACK_IMPORTED_MODULE_2__.PathStatus),
/* harmony export */   "SaveHandler": () => (/* reexport safe */ _savehandler__WEBPACK_IMPORTED_MODULE_3__.SaveHandler),
/* harmony export */   "SavingStatus": () => (/* reexport safe */ _savingstatus__WEBPACK_IMPORTED_MODULE_4__.SavingStatus),
/* harmony export */   "isValidFileName": () => (/* reexport safe */ _dialogs__WEBPACK_IMPORTED_MODULE_0__.isValidFileName),
/* harmony export */   "renameDialog": () => (/* reexport safe */ _dialogs__WEBPACK_IMPORTED_MODULE_0__.renameDialog),
/* harmony export */   "renameFile": () => (/* reexport safe */ _dialogs__WEBPACK_IMPORTED_MODULE_0__.renameFile),
/* harmony export */   "shouldOverwrite": () => (/* reexport safe */ _dialogs__WEBPACK_IMPORTED_MODULE_0__.shouldOverwrite)
/* harmony export */ });
/* harmony import */ var _dialogs__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./dialogs */ "../../packages/docmanager/lib/dialogs.js");
/* harmony import */ var _manager__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./manager */ "../../packages/docmanager/lib/manager.js");
/* harmony import */ var _pathstatus__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./pathstatus */ "../../packages/docmanager/lib/pathstatus.js");
/* harmony import */ var _savehandler__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./savehandler */ "../../packages/docmanager/lib/savehandler.js");
/* harmony import */ var _savingstatus__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./savingstatus */ "../../packages/docmanager/lib/savingstatus.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./tokens */ "../../packages/docmanager/lib/tokens.js");
/* harmony import */ var _widgetmanager__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./widgetmanager */ "../../packages/docmanager/lib/widgetmanager.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module docmanager
 */









/***/ }),

/***/ "../../packages/docmanager/lib/manager.js":
/*!************************************************!*\
  !*** ../../packages/docmanager/lib/manager.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "DocumentManager": () => (/* binding */ DocumentManager)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/docregistry */ "webpack/sharing/consume/default/@jupyterlab/docregistry/@jupyterlab/docregistry");
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _lumino_properties__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @lumino/properties */ "webpack/sharing/consume/default/@lumino/properties/@lumino/properties");
/* harmony import */ var _lumino_properties__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_lumino_properties__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _savehandler__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./savehandler */ "../../packages/docmanager/lib/savehandler.js");
/* harmony import */ var _widgetmanager__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./widgetmanager */ "../../packages/docmanager/lib/widgetmanager.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.










/**
 * The document manager.
 *
 * #### Notes
 * The document manager is used to register model and widget creators,
 * and the file browser uses the document manager to create widgets. The
 * document manager maintains a context for each path and model type that is
 * open, and a list of widgets for each context. The document manager is in
 * control of the proper closing and disposal of the widgets and contexts.
 */
class DocumentManager {
    /**
     * Construct a new document manager.
     */
    constructor(options) {
        this._activateRequested = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_7__.Signal(this);
        this._contexts = [];
        this._isDisposed = false;
        this._autosave = true;
        this._autosaveInterval = 120;
        this._lastModifiedCheckMargin = 500;
        this._renameUntitledFileOnSave = true;
        this.translator = options.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__.nullTranslator;
        this.registry = options.registry;
        this.services = options.manager;
        this._collaborative = !!options.collaborative;
        this._dialogs = options.sessionDialogs || _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.sessionContextDialogs;
        this._docProviderFactory = options.docProviderFactory;
        this._isConnectedCallback = options.isConnectedCallback || (() => true);
        this._opener = options.opener;
        this._when = options.when || options.manager.ready;
        const widgetManager = new _widgetmanager__WEBPACK_IMPORTED_MODULE_8__.DocumentWidgetManager({
            registry: this.registry,
            translator: this.translator
        });
        widgetManager.activateRequested.connect(this._onActivateRequested, this);
        this._widgetManager = widgetManager;
        this._setBusy = options.setBusy;
    }
    /**
     * A signal emitted when one of the documents is activated.
     */
    get activateRequested() {
        return this._activateRequested;
    }
    /**
     * Whether to autosave documents.
     */
    get autosave() {
        return this._autosave;
    }
    set autosave(value) {
        this._autosave = value;
        // For each existing context, start/stop the autosave handler as needed.
        this._contexts.forEach(context => {
            const handler = Private.saveHandlerProperty.get(context);
            if (!handler) {
                return;
            }
            if (value === true && !handler.isActive) {
                handler.start();
            }
            else if (value === false && handler.isActive) {
                handler.stop();
            }
        });
    }
    /**
     * Determines the time interval for autosave in seconds.
     */
    get autosaveInterval() {
        return this._autosaveInterval;
    }
    set autosaveInterval(value) {
        this._autosaveInterval = value;
        // For each existing context, set the save interval as needed.
        this._contexts.forEach(context => {
            const handler = Private.saveHandlerProperty.get(context);
            if (!handler) {
                return;
            }
            handler.saveInterval = value || 120;
        });
    }
    /**
     * Defines max acceptable difference, in milliseconds, between last modified timestamps on disk and client
     */
    get lastModifiedCheckMargin() {
        return this._lastModifiedCheckMargin;
    }
    set lastModifiedCheckMargin(value) {
        this._lastModifiedCheckMargin = value;
        // For each existing context, update the margin value.
        this._contexts.forEach(context => {
            context.lastModifiedCheckMargin = value;
        });
    }
    /**
     * Whether to ask the user to rename untitled file on first manual save.
     */
    get renameUntitledFileOnSave() {
        return this._renameUntitledFileOnSave;
    }
    set renameUntitledFileOnSave(value) {
        this._renameUntitledFileOnSave = value;
    }
    /**
     * Get whether the document manager has been disposed.
     */
    get isDisposed() {
        return this._isDisposed;
    }
    /**
     * Dispose of the resources held by the document manager.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        this._isDisposed = true;
        // Clear any listeners for our signals.
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_7__.Signal.clearData(this);
        // Close all the widgets for our contexts and dispose the widget manager.
        this._contexts.forEach(context => {
            return this._widgetManager.closeWidgets(context);
        });
        this._widgetManager.dispose();
        // Clear the context list.
        this._contexts.length = 0;
    }
    /**
     * Clone a widget.
     *
     * @param widget - The source widget.
     *
     * @returns A new widget or `undefined`.
     *
     * #### Notes
     *  Uses the same widget factory and context as the source, or returns
     *  `undefined` if the source widget is not managed by this manager.
     */
    cloneWidget(widget) {
        return this._widgetManager.cloneWidget(widget);
    }
    /**
     * Close all of the open documents.
     *
     * @returns A promise resolving when the widgets are closed.
     */
    closeAll() {
        return Promise.all(this._contexts.map(context => this._widgetManager.closeWidgets(context))).then(() => undefined);
    }
    /**
     * Close the widgets associated with a given path.
     *
     * @param path - The target path.
     *
     * @returns A promise resolving when the widgets are closed.
     */
    closeFile(path) {
        const close = this._contextsForPath(path).map(c => this._widgetManager.closeWidgets(c));
        return Promise.all(close).then(x => undefined);
    }
    /**
     * Get the document context for a widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The context associated with the widget, or `undefined` if no such
     * context exists.
     */
    contextForWidget(widget) {
        return this._widgetManager.contextForWidget(widget);
    }
    /**
     * Copy a file.
     *
     * @param fromFile - The full path of the original file.
     *
     * @param toDir - The full path to the target directory.
     *
     * @returns A promise which resolves to the contents of the file.
     */
    copy(fromFile, toDir) {
        return this.services.contents.copy(fromFile, toDir);
    }
    /**
     * Create a new file and return the widget used to view it.
     *
     * @param path - The file path to create.
     *
     * @param widgetName - The name of the widget factory to use. 'default' will use the default widget.
     *
     * @param kernel - An optional kernel name/id to override the default.
     *
     * @returns The created widget, or `undefined`.
     *
     * #### Notes
     * This function will return `undefined` if a valid widget factory
     * cannot be found.
     */
    createNew(path, widgetName = 'default', kernel) {
        return this._createOrOpenDocument('create', path, widgetName, kernel);
    }
    /**
     * Delete a file.
     *
     * @param path - The full path to the file to be deleted.
     *
     * @returns A promise which resolves when the file is deleted.
     *
     * #### Notes
     * If there is a running session associated with the file and no other
     * sessions are using the kernel, the session will be shut down.
     */
    deleteFile(path) {
        return this.services.sessions
            .stopIfNeeded(path)
            .then(() => {
            return this.services.contents.delete(path);
        })
            .then(() => {
            this._contextsForPath(path).forEach(context => this._widgetManager.deleteWidgets(context));
            return Promise.resolve(void 0);
        });
    }
    /**
     * Duplicate a file.
     *
     * @param path - The full path to the file to be duplicated.
     *
     * @returns A promise which resolves when the file is duplicated.
     */
    duplicate(path) {
        const basePath = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.PathExt.dirname(path);
        return this.services.contents.copy(path, basePath);
    }
    /**
     * See if a widget already exists for the given path and widget name.
     *
     * @param path - The file path to use.
     *
     * @param widgetName - The name of the widget factory to use. 'default' will use the default widget.
     *
     * @returns The found widget, or `undefined`.
     *
     * #### Notes
     * This can be used to find an existing widget instead of opening
     * a new widget.
     */
    findWidget(path, widgetName = 'default') {
        const newPath = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.PathExt.normalize(path);
        let widgetNames = [widgetName];
        if (widgetName === 'default') {
            const factory = this.registry.defaultWidgetFactory(newPath);
            if (!factory) {
                return undefined;
            }
            widgetNames = [factory.name];
        }
        else if (widgetName === null) {
            widgetNames = this.registry
                .preferredWidgetFactories(newPath)
                .map(f => f.name);
        }
        for (const context of this._contextsForPath(newPath)) {
            for (const widgetName of widgetNames) {
                if (widgetName !== null) {
                    const widget = this._widgetManager.findWidget(context, widgetName);
                    if (widget) {
                        return widget;
                    }
                }
            }
        }
        return undefined;
    }
    /**
     * Create a new untitled file.
     *
     * @param options - The file content creation options.
     */
    newUntitled(options) {
        if (options.type === 'file') {
            options.ext = options.ext || '.txt';
        }
        return this.services.contents.newUntitled(options);
    }
    /**
     * Open a file and return the widget used to view it.
     *
     * @param path - The file path to open.
     *
     * @param widgetName - The name of the widget factory to use. 'default' will use the default widget.
     *
     * @param kernel - An optional kernel name/id to override the default.
     *
     * @returns The created widget, or `undefined`.
     *
     * #### Notes
     * This function will return `undefined` if a valid widget factory
     * cannot be found.
     */
    open(path, widgetName = 'default', kernel, options) {
        return this._createOrOpenDocument('open', path, widgetName, kernel, options);
    }
    /**
     * Open a file and return the widget used to view it.
     * Reveals an already existing editor.
     *
     * @param path - The file path to open.
     *
     * @param widgetName - The name of the widget factory to use. 'default' will use the default widget.
     *
     * @param kernel - An optional kernel name/id to override the default.
     *
     * @returns The created widget, or `undefined`.
     *
     * #### Notes
     * This function will return `undefined` if a valid widget factory
     * cannot be found.
     */
    openOrReveal(path, widgetName = 'default', kernel, options) {
        const widget = this.findWidget(path, widgetName);
        if (widget) {
            this._opener.open(widget, Object.assign({ type: widgetName }, options));
            return widget;
        }
        return this.open(path, widgetName, kernel, options !== null && options !== void 0 ? options : {});
    }
    /**
     * Overwrite a file.
     *
     * @param oldPath - The full path to the original file.
     *
     * @param newPath - The full path to the new file.
     *
     * @returns A promise containing the new file contents model.
     */
    overwrite(oldPath, newPath) {
        // Cleanly overwrite the file by moving it, making sure the original does
        // not exist, and then renaming to the new path.
        const tempPath = `${newPath}.${_lumino_coreutils__WEBPACK_IMPORTED_MODULE_5__.UUID.uuid4()}`;
        const cb = () => this.rename(tempPath, newPath);
        return this.rename(oldPath, tempPath)
            .then(() => {
            return this.deleteFile(newPath);
        })
            .then(cb, cb);
    }
    /**
     * Rename a file or directory.
     *
     * @param oldPath - The full path to the original file.
     *
     * @param newPath - The full path to the new file.
     *
     * @returns A promise containing the new file contents model.  The promise
     * will reject if the newPath already exists.  Use [[overwrite]] to overwrite
     * a file.
     */
    rename(oldPath, newPath) {
        return this.services.contents.rename(oldPath, newPath);
    }
    /**
     * Find a context for a given path and factory name.
     */
    _findContext(path, factoryName) {
        const normalizedPath = this.services.contents.normalize(path);
        return (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_4__.find)(this._contexts, context => {
            return (context.path === normalizedPath && context.factoryName === factoryName);
        });
    }
    /**
     * Get the contexts for a given path.
     *
     * #### Notes
     * There may be more than one context for a given path if the path is open
     * with multiple model factories (for example, a notebook can be open with a
     * notebook model factory and a text model factory).
     */
    _contextsForPath(path) {
        const normalizedPath = this.services.contents.normalize(path);
        return this._contexts.filter(context => context.path === normalizedPath);
    }
    /**
     * Create a context from a path and a model factory.
     */
    _createContext(path, factory, kernelPreference) {
        // TODO: Make it impossible to open two different contexts for the same
        // path. Or at least prompt the closing of all widgets associated with the
        // old context before opening the new context. This will make things much
        // more consistent for the users, at the cost of some confusion about what
        // models are and why sometimes they cannot open the same file in different
        // widgets that have different models.
        // Allow options to be passed when adding a sibling.
        const adopter = (widget, options) => {
            this._widgetManager.adoptWidget(context, widget);
            // TODO should we pass the type for layout customization
            this._opener.open(widget, options);
        };
        const modelDBFactory = this.services.contents.getModelDBFactory(path) || undefined;
        const context = new _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__.Context({
            opener: adopter,
            manager: this.services,
            factory,
            path,
            kernelPreference,
            modelDBFactory,
            setBusy: this._setBusy,
            sessionDialogs: this._dialogs,
            collaborative: this._collaborative,
            docProviderFactory: this._docProviderFactory,
            lastModifiedCheckMargin: this._lastModifiedCheckMargin,
            translator: this.translator
        });
        const handler = new _savehandler__WEBPACK_IMPORTED_MODULE_9__.SaveHandler({
            context,
            isConnectedCallback: this._isConnectedCallback,
            saveInterval: this.autosaveInterval
        });
        Private.saveHandlerProperty.set(context, handler);
        void context.ready.then(() => {
            if (this.autosave) {
                handler.start();
            }
        });
        context.disposed.connect(this._onContextDisposed, this);
        this._contexts.push(context);
        return context;
    }
    /**
     * Handle a context disposal.
     */
    _onContextDisposed(context) {
        _lumino_algorithm__WEBPACK_IMPORTED_MODULE_4__.ArrayExt.removeFirstOf(this._contexts, context);
    }
    /**
     * Get the widget factory for a given widget name.
     */
    _widgetFactoryFor(path, widgetName) {
        const { registry } = this;
        if (widgetName === 'default') {
            const factory = registry.defaultWidgetFactory(path);
            if (!factory) {
                return undefined;
            }
            widgetName = factory.name;
        }
        return registry.getWidgetFactory(widgetName);
    }
    /**
     * Creates a new document, or loads one from disk, depending on the `which` argument.
     * If `which==='create'`, then it creates a new document. If `which==='open'`,
     * then it loads the document from disk.
     *
     * The two cases differ in how the document context is handled, but the creation
     * of the widget and launching of the kernel are identical.
     */
    _createOrOpenDocument(which, path, widgetName = 'default', kernel, options) {
        const widgetFactory = this._widgetFactoryFor(path, widgetName);
        if (!widgetFactory) {
            return undefined;
        }
        const modelName = widgetFactory.modelName || 'text';
        const factory = this.registry.getModelFactory(modelName);
        if (!factory) {
            return undefined;
        }
        // Handle the kernel preference.
        const preference = this.registry.getKernelPreference(path, widgetFactory.name, kernel);
        let context;
        let ready = Promise.resolve(undefined);
        // Handle the load-from-disk case
        if (which === 'open') {
            // Use an existing context if available.
            context = this._findContext(path, factory.name) || null;
            if (!context) {
                context = this._createContext(path, factory, preference);
                // Populate the model, either from disk or a
                // model backend.
                ready = this._when.then(() => context.initialize(false));
            }
        }
        else if (which === 'create') {
            context = this._createContext(path, factory, preference);
            // Immediately save the contents to disk.
            ready = this._when.then(() => context.initialize(true));
        }
        else {
            throw new Error(`Invalid argument 'which': ${which}`);
        }
        const widget = this._widgetManager.createWidget(widgetFactory, context);
        this._opener.open(widget, Object.assign({ type: widgetFactory.name }, options));
        // If the initial opening of the context fails, dispose of the widget.
        ready.catch(err => {
            console.error(`Failed to initialize the context with '${factory.name}' for ${path}`, err);
            widget.close();
        });
        return widget;
    }
    /**
     * Handle an activateRequested signal from the widget manager.
     */
    _onActivateRequested(sender, args) {
        this._activateRequested.emit(args);
    }
}
/**
 * A namespace for private data.
 */
var Private;
(function (Private) {
    /**
     * An attached property for a context save handler.
     */
    Private.saveHandlerProperty = new _lumino_properties__WEBPACK_IMPORTED_MODULE_6__.AttachedProperty({
        name: 'saveHandler',
        create: () => undefined
    });
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/docmanager/lib/pathstatus.js":
/*!***************************************************!*\
  !*** ../../packages/docmanager/lib/pathstatus.js ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "PathStatus": () => (/* binding */ PathStatus)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_3__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




/**
 * A pure component for rendering a file path (or activity name).
 *
 * @param props - the props for the component.
 *
 * @returns a tsx component for a file path.
 */
function PathStatusComponent(props) {
    return react__WEBPACK_IMPORTED_MODULE_3___default().createElement(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_1__.TextItem, { source: props.name, title: props.fullPath });
}
/**
 * A status bar item for the current file path (or activity name).
 */
class PathStatus extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.VDomRenderer {
    /**
     * Construct a new PathStatus status item.
     */
    constructor(opts) {
        super(new PathStatus.Model(opts.docManager));
        this.node.title = this.model.path;
    }
    /**
     * Render the status item.
     */
    render() {
        return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement(PathStatusComponent, { fullPath: this.model.path, name: this.model.name }));
    }
}
/**
 * A namespace for PathStatus statics.
 */
(function (PathStatus) {
    /**
     * A VDomModel for rendering the PathStatus status item.
     */
    class Model extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.VDomModel {
        /**
         * Construct a new model.
         *
         * @param docManager: the application document manager. Used to check
         *   whether the current widget is a document.
         */
        constructor(docManager) {
            super();
            /**
             * React to a title change for the current widget.
             */
            this._onTitleChange = (title) => {
                const oldState = this._getAllState();
                this._name = title.label;
                this._triggerChange(oldState, this._getAllState());
            };
            /**
             * React to a path change for the current document.
             */
            this._onPathChange = (_documentModel, newPath) => {
                const oldState = this._getAllState();
                this._path = newPath;
                this._name = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.PathExt.basename(newPath);
                this._triggerChange(oldState, this._getAllState());
            };
            this._path = '';
            this._name = '';
            this._widget = null;
            this._docManager = docManager;
        }
        /**
         * The current path for the application.
         */
        get path() {
            return this._path;
        }
        /**
         * The name of the current activity.
         */
        get name() {
            return this._name;
        }
        /**
         * The current widget for the application.
         */
        get widget() {
            return this._widget;
        }
        set widget(widget) {
            const oldWidget = this._widget;
            if (oldWidget !== null) {
                const oldContext = this._docManager.contextForWidget(oldWidget);
                if (oldContext) {
                    oldContext.pathChanged.disconnect(this._onPathChange);
                }
                else {
                    oldWidget.title.changed.disconnect(this._onTitleChange);
                }
            }
            const oldState = this._getAllState();
            this._widget = widget;
            if (this._widget === null) {
                this._path = '';
                this._name = '';
            }
            else {
                const widgetContext = this._docManager.contextForWidget(this._widget);
                if (widgetContext) {
                    this._path = widgetContext.path;
                    this._name = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.PathExt.basename(widgetContext.path);
                    widgetContext.pathChanged.connect(this._onPathChange);
                }
                else {
                    this._path = '';
                    this._name = this._widget.title.label;
                    this._widget.title.changed.connect(this._onTitleChange);
                }
            }
            this._triggerChange(oldState, this._getAllState());
        }
        /**
         * Get the current state of the model.
         */
        _getAllState() {
            return [this._path, this._name];
        }
        /**
         * Trigger a state change to rerender.
         */
        _triggerChange(oldState, newState) {
            if (oldState[0] !== newState[0] || oldState[1] !== newState[1]) {
                this.stateChanged.emit(void 0);
            }
        }
    }
    PathStatus.Model = Model;
})(PathStatus || (PathStatus = {}));


/***/ }),

/***/ "../../packages/docmanager/lib/savehandler.js":
/*!****************************************************!*\
  !*** ../../packages/docmanager/lib/savehandler.js ***!
  \****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "SaveHandler": () => (/* binding */ SaveHandler)
/* harmony export */ });
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * A class that manages the auto saving of a document.
 *
 * #### Notes
 * Implements https://github.com/ipython/ipython/wiki/IPEP-15:-Autosaving-the-IPython-Notebook.
 */
class SaveHandler {
    /**
     * Construct a new save handler.
     */
    constructor(options) {
        this._autosaveTimer = -1;
        this._minInterval = -1;
        this._interval = -1;
        this._isActive = false;
        this._inDialog = false;
        this._isDisposed = false;
        this._multiplier = 10;
        this._context = options.context;
        this._isConnectedCallback = options.isConnectedCallback || (() => true);
        const interval = options.saveInterval || 120;
        this._minInterval = interval * 1000;
        this._interval = this._minInterval;
        // Restart the timer when the contents model is updated.
        this._context.fileChanged.connect(this._setTimer, this);
        this._context.disposed.connect(this.dispose, this);
    }
    /**
     * The save interval used by the timer (in seconds).
     */
    get saveInterval() {
        return this._interval / 1000;
    }
    set saveInterval(value) {
        this._minInterval = this._interval = value * 1000;
        if (this._isActive) {
            this._setTimer();
        }
    }
    /**
     * Get whether the handler is active.
     */
    get isActive() {
        return this._isActive;
    }
    /**
     * Get whether the save handler is disposed.
     */
    get isDisposed() {
        return this._isDisposed;
    }
    /**
     * Dispose of the resources used by the save handler.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        this._isDisposed = true;
        clearTimeout(this._autosaveTimer);
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__.Signal.clearData(this);
    }
    /**
     * Start the autosaver.
     */
    start() {
        this._isActive = true;
        this._setTimer();
    }
    /**
     * Stop the autosaver.
     */
    stop() {
        this._isActive = false;
        clearTimeout(this._autosaveTimer);
    }
    /**
     * Set the timer.
     */
    _setTimer() {
        clearTimeout(this._autosaveTimer);
        if (!this._isActive) {
            return;
        }
        this._autosaveTimer = window.setTimeout(() => {
            if (this._isConnectedCallback()) {
                this._save();
            }
        }, this._interval);
    }
    /**
     * Handle an autosave timeout.
     */
    _save() {
        const context = this._context;
        // Trigger the next update.
        this._setTimer();
        if (!context) {
            return;
        }
        // Bail if the model is not dirty or the file is not writable, or the dialog
        // is already showing.
        const writable = context.contentsModel && context.contentsModel.writable;
        if (!writable || !context.model.dirty || this._inDialog) {
            return;
        }
        const start = new Date().getTime();
        context
            .save()
            .then(() => {
            if (this.isDisposed) {
                return;
            }
            const duration = new Date().getTime() - start;
            // New save interval: higher of 10x save duration or min interval.
            this._interval = Math.max(this._multiplier * duration, this._minInterval);
            // Restart the update to pick up the new interval.
            this._setTimer();
        })
            .catch(err => {
            // If the user canceled the save, do nothing.
            const { name } = err;
            if (name === 'ModalCancelError' || name === 'ModalDuplicateError') {
                return;
            }
            // Otherwise, log the error.
            console.error('Error in Auto-Save', err.message);
        });
    }
}


/***/ }),

/***/ "../../packages/docmanager/lib/savingstatus.js":
/*!*****************************************************!*\
  !*** ../../packages/docmanager/lib/savingstatus.js ***!
  \*****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "SavingStatus": () => (/* binding */ SavingStatus)
/* harmony export */ });
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_3__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




/**
 * A pure functional component for a Saving status item.
 *
 * @param props - the props for the component.
 *
 * @returns a tsx component for rendering the saving state.
 */
function SavingStatusComponent(props) {
    return react__WEBPACK_IMPORTED_MODULE_3___default().createElement(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__.TextItem, { source: props.fileStatus });
}
/**
 * The amount of time (in ms) to retain the saving completed message
 * before hiding the status item.
 */
const SAVING_COMPLETE_MESSAGE_MILLIS = 2000;
/**
 * A VDomRenderer for a saving status item.
 */
class SavingStatus extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.VDomRenderer {
    /**
     * Create a new SavingStatus item.
     */
    constructor(opts) {
        super(new SavingStatus.Model(opts.docManager));
        const translator = opts.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.nullTranslator;
        const trans = translator.load('jupyterlab');
        this._statusMap = {
            completed: trans.__('Saving completed'),
            started: trans.__('Saving started'),
            failed: trans.__('Saving failed')
        };
    }
    /**
     * Render the SavingStatus item.
     */
    render() {
        if (this.model === null || this.model.status === null) {
            return null;
        }
        else {
            return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement(SavingStatusComponent, { fileStatus: this._statusMap[this.model.status] }));
        }
    }
}
/**
 * A namespace for SavingStatus statics.
 */
(function (SavingStatus) {
    /**
     * A VDomModel for the SavingStatus item.
     */
    class Model extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.VDomModel {
        /**
         * Create a new SavingStatus model.
         */
        constructor(docManager) {
            super();
            /**
             * React to a saving status change from the current document widget.
             */
            this._onStatusChange = (_, newStatus) => {
                this._status = newStatus;
                if (this._status === 'completed') {
                    setTimeout(() => {
                        this._status = null;
                        this.stateChanged.emit(void 0);
                    }, SAVING_COMPLETE_MESSAGE_MILLIS);
                    this.stateChanged.emit(void 0);
                }
                else {
                    this.stateChanged.emit(void 0);
                }
            };
            this._status = null;
            this._widget = null;
            this._status = null;
            this.widget = null;
            this._docManager = docManager;
        }
        /**
         * The current status of the model.
         */
        get status() {
            return this._status;
        }
        /**
         * The current widget for the model. Any widget can be assigned,
         * but it only has any effect if the widget is an IDocument widget
         * known to the application document manager.
         */
        get widget() {
            return this._widget;
        }
        set widget(widget) {
            var _a, _b;
            const oldWidget = this._widget;
            if (oldWidget !== null) {
                const oldContext = this._docManager.contextForWidget(oldWidget);
                if (oldContext) {
                    oldContext.saveState.disconnect(this._onStatusChange);
                }
                else if ((_a = this._widget.content) === null || _a === void 0 ? void 0 : _a.saveStateChanged) {
                    this._widget.content.saveStateChanged.disconnect(this._onStatusChange);
                }
            }
            this._widget = widget;
            if (this._widget === null) {
                this._status = null;
            }
            else {
                const widgetContext = this._docManager.contextForWidget(this._widget);
                if (widgetContext) {
                    widgetContext.saveState.connect(this._onStatusChange);
                }
                else if ((_b = this._widget.content) === null || _b === void 0 ? void 0 : _b.saveStateChanged) {
                    this._widget.content.saveStateChanged.connect(this._onStatusChange);
                }
            }
        }
    }
    SavingStatus.Model = Model;
})(SavingStatus || (SavingStatus = {}));


/***/ }),

/***/ "../../packages/docmanager/lib/tokens.js":
/*!***********************************************!*\
  !*** ../../packages/docmanager/lib/tokens.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IDocumentManager": () => (/* binding */ IDocumentManager)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The document registry token.
 */
const IDocumentManager = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/docmanager:IDocumentManager');


/***/ }),

/***/ "../../packages/docmanager/lib/widgetmanager.js":
/*!******************************************************!*\
  !*** ../../packages/docmanager/lib/widgetmanager.js ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "DocumentWidgetManager": () => (/* binding */ DocumentWidgetManager)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_messaging__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/messaging */ "webpack/sharing/consume/default/@lumino/messaging/@lumino/messaging");
/* harmony import */ var _lumino_messaging__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_messaging__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _lumino_properties__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @lumino/properties */ "webpack/sharing/consume/default/@lumino/properties/@lumino/properties");
/* harmony import */ var _lumino_properties__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_lumino_properties__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_7__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.








/**
 * The class name added to document widgets.
 */
const DOCUMENT_CLASS = 'jp-Document';
/**
 * A class that maintains the lifecycle of file-backed widgets.
 */
class DocumentWidgetManager {
    /**
     * Construct a new document widget manager.
     */
    constructor(options) {
        this._activateRequested = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_7__.Signal(this);
        this._isDisposed = false;
        this._registry = options.registry;
        this.translator = options.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.nullTranslator;
    }
    /**
     * A signal emitted when one of the documents is activated.
     */
    get activateRequested() {
        return this._activateRequested;
    }
    /**
     * Test whether the document widget manager is disposed.
     */
    get isDisposed() {
        return this._isDisposed;
    }
    /**
     * Dispose of the resources used by the widget manager.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        this._isDisposed = true;
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_7__.Signal.disconnectReceiver(this);
    }
    /**
     * Create a widget for a document and handle its lifecycle.
     *
     * @param factory - The widget factory.
     *
     * @param context - The document context object.
     *
     * @returns A widget created by the factory.
     *
     * @throws If the factory is not registered.
     */
    createWidget(factory, context) {
        const widget = factory.createNew(context);
        this._initializeWidget(widget, factory, context);
        return widget;
    }
    /**
     * When a new widget is created, we need to hook it up
     * with some signals, update the widget extensions (for
     * this kind of widget) in the docregistry, among
     * other things.
     */
    _initializeWidget(widget, factory, context) {
        Private.factoryProperty.set(widget, factory);
        // Handle widget extensions.
        const disposables = new _lumino_disposable__WEBPACK_IMPORTED_MODULE_4__.DisposableSet();
        (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.each)(this._registry.widgetExtensions(factory.name), extender => {
            const disposable = extender.createNew(widget, context);
            if (disposable) {
                disposables.add(disposable);
            }
        });
        Private.disposablesProperty.set(widget, disposables);
        widget.disposed.connect(this._onWidgetDisposed, this);
        this.adoptWidget(context, widget);
        context.fileChanged.connect(this._onFileChanged, this);
        context.pathChanged.connect(this._onPathChanged, this);
        void context.ready.then(() => {
            void this.setCaption(widget);
        });
    }
    /**
     * Install the message hook for the widget and add to list
     * of known widgets.
     *
     * @param context - The document context object.
     *
     * @param widget - The widget to adopt.
     */
    adoptWidget(context, widget) {
        const widgets = Private.widgetsProperty.get(context);
        widgets.push(widget);
        _lumino_messaging__WEBPACK_IMPORTED_MODULE_5__.MessageLoop.installMessageHook(widget, this);
        widget.addClass(DOCUMENT_CLASS);
        widget.title.closable = true;
        widget.disposed.connect(this._widgetDisposed, this);
        Private.contextProperty.set(widget, context);
    }
    /**
     * See if a widget already exists for the given context and widget name.
     *
     * @param context - The document context object.
     *
     * @returns The found widget, or `undefined`.
     *
     * #### Notes
     * This can be used to use an existing widget instead of opening
     * a new widget.
     */
    findWidget(context, widgetName) {
        const widgets = Private.widgetsProperty.get(context);
        if (!widgets) {
            return undefined;
        }
        return (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.find)(widgets, widget => {
            const factory = Private.factoryProperty.get(widget);
            if (!factory) {
                return false;
            }
            return factory.name === widgetName;
        });
    }
    /**
     * Get the document context for a widget.
     *
     * @param widget - The widget of interest.
     *
     * @returns The context associated with the widget, or `undefined`.
     */
    contextForWidget(widget) {
        return Private.contextProperty.get(widget);
    }
    /**
     * Clone a widget.
     *
     * @param widget - The source widget.
     *
     * @returns A new widget or `undefined`.
     *
     * #### Notes
     *  Uses the same widget factory and context as the source, or throws
     *  if the source widget is not managed by this manager.
     */
    cloneWidget(widget) {
        const context = Private.contextProperty.get(widget);
        if (!context) {
            return undefined;
        }
        const factory = Private.factoryProperty.get(widget);
        if (!factory) {
            return undefined;
        }
        const newWidget = factory.createNew(context, widget);
        this._initializeWidget(newWidget, factory, context);
        return newWidget;
    }
    /**
     * Close the widgets associated with a given context.
     *
     * @param context - The document context object.
     */
    closeWidgets(context) {
        const widgets = Private.widgetsProperty.get(context);
        return Promise.all((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.toArray)((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.map)(widgets, widget => this.onClose(widget)))).then(() => undefined);
    }
    /**
     * Dispose of the widgets associated with a given context
     * regardless of the widget's dirty state.
     *
     * @param context - The document context object.
     */
    deleteWidgets(context) {
        const widgets = Private.widgetsProperty.get(context);
        return Promise.all((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.toArray)((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.map)(widgets, widget => this.onDelete(widget)))).then(() => undefined);
    }
    /**
     * Filter a message sent to a message handler.
     *
     * @param handler - The target handler of the message.
     *
     * @param msg - The message dispatched to the handler.
     *
     * @returns `false` if the message should be filtered, of `true`
     *   if the message should be dispatched to the handler as normal.
     */
    messageHook(handler, msg) {
        switch (msg.type) {
            case 'close-request':
                void this.onClose(handler);
                return false;
            case 'activate-request': {
                const context = this.contextForWidget(handler);
                if (context) {
                    this._activateRequested.emit(context.path);
                }
                break;
            }
            default:
                break;
        }
        return true;
    }
    /**
     * Set the caption for widget title.
     *
     * @param widget - The target widget.
     */
    async setCaption(widget) {
        const trans = this.translator.load('jupyterlab');
        const context = Private.contextProperty.get(widget);
        if (!context) {
            return;
        }
        const model = context.contentsModel;
        if (!model) {
            widget.title.caption = '';
            return;
        }
        return context
            .listCheckpoints()
            .then((checkpoints) => {
            if (widget.isDisposed) {
                return;
            }
            const last = checkpoints[checkpoints.length - 1];
            const checkpoint = last ? _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.Time.format(last.last_modified) : 'None';
            let caption = trans.__('Name: %1\nPath: %2\n', model.name, model.path);
            if (context.model.readOnly) {
                caption += trans.__('Read-only');
            }
            else {
                caption +=
                    trans.__('Last Saved: %1\n', _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.Time.format(model.last_modified)) +
                        trans.__('Last Checkpoint: %1', checkpoint);
            }
            widget.title.caption = caption;
        });
    }
    /**
     * Handle `'close-request'` messages.
     *
     * @param widget - The target widget.
     *
     * @returns A promise that resolves with whether the widget was closed.
     */
    async onClose(widget) {
        var _a;
        // Handle dirty state.
        const [shouldClose, ignoreSave] = await this._maybeClose(widget, this.translator);
        if (widget.isDisposed) {
            return true;
        }
        if (shouldClose) {
            if (!ignoreSave) {
                const context = Private.contextProperty.get(widget);
                if (!context) {
                    return true;
                }
                if ((_a = context.contentsModel) === null || _a === void 0 ? void 0 : _a.writable) {
                    await context.save();
                }
                else {
                    await context.saveAs();
                }
            }
            if (widget.isDisposed) {
                return true;
            }
            widget.dispose();
        }
        return shouldClose;
    }
    /**
     * Dispose of widget regardless of widget's dirty state.
     *
     * @param widget - The target widget.
     */
    onDelete(widget) {
        widget.dispose();
        return Promise.resolve(void 0);
    }
    /**
     * Ask the user whether to close an unsaved file.
     */
    _maybeClose(widget, translator) {
        var _a;
        translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.nullTranslator;
        const trans = translator.load('jupyterlab');
        // Bail if the model is not dirty or other widgets are using the model.)
        const context = Private.contextProperty.get(widget);
        if (!context) {
            return Promise.resolve([true, true]);
        }
        let widgets = Private.widgetsProperty.get(context);
        if (!widgets) {
            return Promise.resolve([true, true]);
        }
        // Filter by whether the factories are read only.
        widgets = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.toArray)((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.filter)(widgets, widget => {
            const factory = Private.factoryProperty.get(widget);
            if (!factory) {
                return false;
            }
            return factory.readOnly === false;
        }));
        const factory = Private.factoryProperty.get(widget);
        if (!factory) {
            return Promise.resolve([true, true]);
        }
        const model = context.model;
        if (!model.dirty || widgets.length > 1 || factory.readOnly) {
            return Promise.resolve([true, true]);
        }
        const fileName = widget.title.label;
        const saveLabel = ((_a = context.contentsModel) === null || _a === void 0 ? void 0 : _a.writable)
            ? trans.__('Save')
            : trans.__('Save as');
        return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showDialog)({
            title: trans.__('Save your work'),
            body: trans.__('Save changes in "%1" before closing?', fileName),
            buttons: [
                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.cancelButton(),
                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.warnButton({ label: trans.__('Discard') }),
                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Dialog.okButton({ label: saveLabel })
            ]
        }).then(result => {
            return [result.button.accept, result.button.displayType === 'warn'];
        });
    }
    /**
     * Handle the disposal of a widget.
     */
    _widgetDisposed(widget) {
        const context = Private.contextProperty.get(widget);
        if (!context) {
            return;
        }
        const widgets = Private.widgetsProperty.get(context);
        if (!widgets) {
            return;
        }
        // Remove the widget.
        _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.ArrayExt.removeFirstOf(widgets, widget);
        // Dispose of the context if this is the last widget using it.
        if (!widgets.length) {
            context.dispose();
        }
    }
    /**
     * Handle the disposal of a widget.
     */
    _onWidgetDisposed(widget) {
        const disposables = Private.disposablesProperty.get(widget);
        disposables.dispose();
    }
    /**
     * Handle a file changed signal for a context.
     */
    _onFileChanged(context) {
        const widgets = Private.widgetsProperty.get(context);
        (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.each)(widgets, widget => {
            void this.setCaption(widget);
        });
    }
    /**
     * Handle a path changed signal for a context.
     */
    _onPathChanged(context) {
        const widgets = Private.widgetsProperty.get(context);
        (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.each)(widgets, widget => {
            void this.setCaption(widget);
        });
    }
}
/**
 * A private namespace for DocumentManager data.
 */
var Private;
(function (Private) {
    /**
     * A private attached property for a widget context.
     */
    Private.contextProperty = new _lumino_properties__WEBPACK_IMPORTED_MODULE_6__.AttachedProperty({
        name: 'context',
        create: () => undefined
    });
    /**
     * A private attached property for a widget factory.
     */
    Private.factoryProperty = new _lumino_properties__WEBPACK_IMPORTED_MODULE_6__.AttachedProperty({
        name: 'factory',
        create: () => undefined
    });
    /**
     * A private attached property for the widgets associated with a context.
     */
    Private.widgetsProperty = new _lumino_properties__WEBPACK_IMPORTED_MODULE_6__.AttachedProperty({
        name: 'widgets',
        create: () => []
    });
    /**
     * A private attached property for a widget's disposables.
     */
    Private.disposablesProperty = new _lumino_properties__WEBPACK_IMPORTED_MODULE_6__.AttachedProperty({
        name: 'disposables',
        create: () => new _lumino_disposable__WEBPACK_IMPORTED_MODULE_4__.DisposableSet()
    });
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfZG9jbWFuYWdlcl9saWJfaW5kZXhfanMuMWE4MTk0Mzg4MTQzNzgyOWYwNDYuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUVpQjtBQUU1QjtBQUVzQjtBQUU3QjtBQUd6Qzs7R0FFRztBQUNILE1BQU0saUJBQWlCLEdBQUcsZUFBZSxDQUFDO0FBRTFDOztHQUVHO0FBQ0gsTUFBTSwyQkFBMkIsR0FBRyxtQkFBbUIsQ0FBQztBQWdCeEQ7O0dBRUc7QUFDSSxTQUFTLFlBQVksQ0FDMUIsT0FBeUIsRUFDekIsT0FBaUMsRUFDakMsVUFBd0I7SUFFeEIsVUFBVSxHQUFHLFVBQVUsSUFBSSxtRUFBYyxDQUFDO0lBQzFDLE1BQU0sS0FBSyxHQUFHLFVBQVUsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUM7SUFFNUMsTUFBTSxTQUFTLEdBQUcsT0FBTyxDQUFDLFNBQVMsQ0FBQyxLQUFLLENBQUMsR0FBRyxDQUFDLENBQUM7SUFDL0MsTUFBTSxRQUFRLEdBQUcsU0FBUyxDQUFDLEdBQUcsRUFBRSxJQUFJLE9BQU8sQ0FBQyxTQUFTLENBQUM7SUFFdEQsT0FBTyxnRUFBVSxDQUFDO1FBQ2hCLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLGFBQWEsQ0FBQztRQUM5QixJQUFJLEVBQUUsSUFBSSxhQUFhLENBQUMsUUFBUSxDQUFDO1FBQ2pDLGlCQUFpQixFQUFFLE9BQU87UUFDMUIsT0FBTyxFQUFFO1lBQ1AscUVBQW1CLEVBQUU7WUFDckIsaUVBQWUsQ0FBQyxFQUFFLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLFFBQVEsQ0FBQyxFQUFFLENBQUM7U0FDL0M7S0FDRixDQUFDLENBQUMsSUFBSSxDQUFDLE1BQU0sQ0FBQyxFQUFFO1FBQ2YsSUFBSSxDQUFDLE1BQU0sQ0FBQyxLQUFLLEVBQUU7WUFDakIsT0FBTyxJQUFJLENBQUM7U0FDYjtRQUNELElBQUksQ0FB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RUc7SUFDVSx1QkFBZSxHQUFHLElBQUksZ0VBQWdCLENBR2pEO1FBQ0EsSUFBSSxFQUFFLFNBQVM7UUFDZixNQUFNLEVBQUUsR0FBRyxFQUFFLENBQUMsU0FBUztLQUN4QixDQUFDLENBQUM7SUFFSDs7T0FFRztJQUNVLHVCQUFlLEdBQUcsSUFBSSxnRUFBZ0IsQ0FHakQ7UUFDQSxJQUFJLEVBQUUsU0FBUztRQUNmLE1BQU0sRUFBRSxHQUFHLEVBQUUsQ0FBQyxTQUFTO0tBQ3hCLENBQUMsQ0FBQztJQUVIOztPQUVHO0lBQ1UsdUJBQWUsR0FBRyxJQUFJLGdFQUFnQixDQUdqRDtRQUNBLElBQUksRUFBRSxTQUFTO1FBQ2YsTUFBTSxFQUFFLEdBQUcsRUFBRSxDQUFDLEVBQUU7S0FDakIsQ0FBQyxDQUFDO0lBRUg7O09BRUc7SUFDVSwyQkFBbUIsR0FBRyxJQUFJLGdFQUFnQixDQUdyRDtRQUNBLElBQUksRUFBRSxhQUFhO1FBQ25CLE1BQU0sRUFBRSxHQUFHLEVBQUUsQ0FBQyxJQUFJLDZEQUFhLEVBQUU7S0FDbEMsQ0FBQyxDQUFDO0FBQ0wsQ0FBQyxFQTVDUyxPQUFPLEtBQVAsT0FBTyxRQTRDaEIiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZG9jbWFuYWdlci9zcmMvZGlhbG9ncy50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZG9jbWFuYWdlci9zcmMvaW5kZXgudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2RvY21hbmFnZXIvc3JjL21hbmFnZXIudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2RvY21hbmFnZXIvc3JjL3BhdGhzdGF0dXMudHN4Iiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9kb2NtYW5hZ2VyL3NyYy9zYXZlaGFuZGxlci50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZG9jbWFuYWdlci9zcmMvc2F2aW5nc3RhdHVzLnRzeCIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZG9jbWFuYWdlci9zcmMvdG9rZW5zLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9kb2NtYW5hZ2VyL3NyYy93aWRnZXRtYW5hZ2VyLnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgRGlhbG9nLCBzaG93RGlhbG9nLCBzaG93RXJyb3JNZXNzYWdlIH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgRG9jdW1lbnRSZWdpc3RyeSB9IGZyb20gJ0BqdXB5dGVybGFiL2RvY3JlZ2lzdHJ5JztcbmltcG9ydCB7IFBhdGhFeHQgfSBmcm9tICdAanVweXRlcmxhYi9jb3JldXRpbHMnO1xuaW1wb3J0IHsgQ29udGVudHMgfSBmcm9tICdAanVweXRlcmxhYi9zZXJ2aWNlcyc7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciwgbnVsbFRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQgeyBKU09OT2JqZWN0IH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IElEb2N1bWVudE1hbmFnZXIgfSBmcm9tICcuLyc7XG5cbi8qKlxuICogVGhlIGNsYXNzIG5hbWUgYWRkZWQgdG8gZmlsZSBkaWFsb2dzLlxuICovXG5jb25zdCBGSUxFX0RJQUxPR19DTEFTUyA9ICdqcC1GaWxlRGlhbG9nJztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCBmb3IgdGhlIG5ldyBuYW1lIGxhYmVsIGluIHRoZSByZW5hbWUgZGlhbG9nXG4gKi9cbmNvbnN0IFJFTkFNRV9ORVdfTkFNRV9USVRMRV9DTEFTUyA9ICdqcC1uZXctbmFtZS10aXRsZSc7XG5cbi8qKlxuICogQSBzdHJpcHBlZC1kb3duIGludGVyZmFjZSBmb3IgYSBmaWxlIGNvbnRhaW5lci5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJRmlsZUNvbnRhaW5lciBleHRlbmRzIEpTT05PYmplY3Qge1xuICAvKipcbiAgICogVGhlIGxpc3Qgb2YgaXRlbSBuYW1lcyBpbiB0aGUgY3VycmVudCB3b3JraW5nIGRpcmVjdG9yeS5cbiAgICovXG4gIGl0ZW1zOiBzdHJpbmdbXTtcbiAgLyoqXG4gICAqIFRoZSBjdXJyZW50IHdvcmtpbmcgZGlyZWN0b3J5IG9mIHRoZSBmaWxlIGNvbnRhaW5lci5cbiAgICovXG4gIHBhdGg6IHN0cmluZztcbn1cblxuLyoqXG4gKiBSZW5hbWUgYSBmaWxlIHdpdGggYSBkaWFsb2cuXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiByZW5hbWVEaWFsb2coXG4gIG1hbmFnZXI6IElEb2N1bWVudE1hbmFnZXIsXG4gIGNvbnRleHQ6IERvY3VtZW50UmVnaXN0cnkuQ29udGV4dCxcbiAgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yXG4pOiBQcm9taXNlPHZvaWQgfCBudWxsPiB7XG4gIHRyYW5zbGF0b3IgPSB0cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuXG4gIGNvbnN0IGxvY2FsUGF0aCA9IGNvbnRleHQubG9jYWxQYXRoLnNwbGl0KCcvJyk7XG4gIGNvbnN0IGZpbGVOYW1lID0gbG9jYWxQYXRoLnBvcCgpIHx8IGNvbnRleHQubG9jYWxQYXRoO1xuXG4gIHJldHVybiBzaG93RGlhbG9nKHtcbiAgICB0aXRsZTogdHJhbnMuX18oJ1JlbmFtZSBGaWxlJyksXG4gICAgYm9keTogbmV3IFJlbmFtZUhhbmRsZXIoZmlsZU5hbWUpLFxuICAgIGZvY3VzTm9kZVNlbGVjdG9yOiAnaW5wdXQnLFxuICAgIGJ1dHRvbnM6IFtcbiAgICAgIERpYWxvZy5jYW5jZWxCdXR0b24oKSxcbiAgICAgIERpYWxvZy5va0J1dHRvbih7IGxhYmVsOiB0cmFucy5fXygnUmVuYW1lJykgfSlcbiAgICBdXG4gIH0pLnRoZW4ocmVzdWx0ID0+IHtcbiAgICBpZiAoIXJlc3VsdC52YWx1ZSkge1xuICAgICAgcmV0dXJuIG51bGw7XG4gICAgfVxuICAgIGlmICghaXNWYWxpZEZpbGVOYW1lKHJlc3VsdC52YWx1ZSkpIHtcbiAgICAgIHZvaWQgc2hvd0Vycm9yTWVzc2FnZShcbiAgICAgICAgdHJhbnMuX18oJ1JlbmFtZSBFcnJvcicpLFxuICAgICAgICBFcnJvcihcbiAgICAgICAgICB0cmFucy5fXyhcbiAgICAgICAgICAgICdcIiUxXCIgaXMgbm90IGEgdmFsaWQgbmFtZSBmb3IgYSBmaWxlLiBOYW1lcyBtdXN0IGhhdmUgbm9uemVybyBsZW5ndGgsIGFuZCBjYW5ub3QgaW5jbHVkZSBcIi9cIiwgXCJcXFxcXCIsIG9yIFwiOlwiJyxcbiAgICAgICAgICAgIHJlc3VsdC52YWx1ZVxuICAgICAgICAgIClcbiAgICAgICAgKVxuICAgICAgKTtcbiAgICAgIHJldHVybiBudWxsO1xuICAgIH1cbiAgICByZXR1cm4gY29udGV4dC5yZW5hbWUocmVzdWx0LnZhbHVlKTtcbiAgfSk7XG59XG5cbi8qKlxuICogUmVuYW1lIGEgZmlsZSwgYXNraW5nIGZvciBjb25maXJtYXRpb24gaWYgaXQgaXMgb3ZlcndyaXRpbmcgYW5vdGhlci5cbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIHJlbmFtZUZpbGUoXG4gIG1hbmFnZXI6IElEb2N1bWVudE1hbmFnZXIsXG4gIG9sZFBhdGg6IHN0cmluZyxcbiAgbmV3UGF0aDogc3RyaW5nXG4pOiBQcm9taXNlPENvbnRlbnRzLklNb2RlbCB8IG51bGw+IHtcbiAgcmV0dXJuIG1hbmFnZXIucmVuYW1lKG9sZFBhdGgsIG5ld1BhdGgpLmNhdGNoKGVycm9yID0+IHtcbiAgICBpZiAoZXJyb3IucmVzcG9uc2Uuc3RhdHVzICE9PSA0MDkpIHtcbiAgICAgIC8vIGlmIGl0J3Mgbm90IGNhdXNlZCBieSBhbiBhbHJlYWR5IGV4aXN0aW5nIGZpbGUsIHJldGhyb3dcbiAgICAgIHRocm93IGVycm9yO1xuICAgIH1cblxuICAgIC8vIG90aGVyd2lzZSwgYXNrIGZvciBjb25maXJtYXRpb25cbiAgICByZXR1cm4gc2hvdWxkT3ZlcndyaXRlKG5ld1BhdGgpLnRoZW4oKHZhbHVlOiBib29sZWFuKSA9PiB7XG4gICAgICBpZiAodmFsdWUpIHtcbiAgICAgICAgcmV0dXJuIG1hbmFnZXIub3ZlcndyaXRlKG9sZFBhdGgsIG5ld1BhdGgpO1xuICAgICAgfVxuICAgICAgcmV0dXJuIFByb21pc2UucmVqZWN0KCdGaWxlIG5vdCByZW5hbWVkJyk7XG4gICAgfSk7XG4gIH0pO1xufVxuXG4vKipcbiAqIEFzayB0aGUgdXNlciB3aGV0aGVyIHRvIG92ZXJ3cml0ZSBhIGZpbGUuXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiBzaG91bGRPdmVyd3JpdGUoXG4gIHBhdGg6IHN0cmluZyxcbiAgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yXG4pOiBQcm9taXNlPGJvb2xlYW4+IHtcbiAgdHJhbnNsYXRvciA9IHRyYW5zbGF0b3IgfHwgbnVsbFRyYW5zbGF0b3I7XG4gIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG5cbiAgY29uc3Qgb3B0aW9ucyA9IHtcbiAgICB0aXRsZTogdHJhbnMuX18oJ092ZXJ3cml0ZSBmaWxlPycpLFxuICAgIGJvZHk6IHRyYW5zLl9fKCdcIiUxXCIgYWxyZWFkeSBleGlzdHMsIG92ZXJ3cml0ZT8nLCBwYXRoKSxcbiAgICBidXR0b25zOiBbXG4gICAgICBEaWFsb2cuY2FuY2VsQnV0dG9uKCksXG4gICAgICBEaWFsb2cud2FybkJ1dHRvbih7IGxhYmVsOiB0cmFucy5fXygnT3ZlcndyaXRlJykgfSlcbiAgICBdXG4gIH07XG4gIHJldHVybiBzaG93RGlhbG9nKG9wdGlvbnMpLnRoZW4ocmVzdWx0ID0+IHtcbiAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKHJlc3VsdC5idXR0b24uYWNjZXB0KTtcbiAgfSk7XG59XG5cbi8qKlxuICogVGVzdCB3aGV0aGVyIGEgbmFtZSBpcyBhIHZhbGlkIGZpbGUgbmFtZVxuICpcbiAqIERpc2FsbG93cyBcIi9cIiwgXCJcXFwiLCBhbmQgXCI6XCIgaW4gZmlsZSBuYW1lcywgYXMgd2VsbCBhcyBuYW1lcyB3aXRoIHplcm8gbGVuZ3RoLlxuICovXG5leHBvcnQgZnVuY3Rpb24gaXNWYWxpZEZpbGVOYW1lKG5hbWU6IHN0cmluZyk6IGJvb2xlYW4ge1xuICBjb25zdCB2YWxpZE5hbWVFeHAgPSAvW1xcL1xcXFw6XS87XG4gIHJldHVybiBuYW1lLmxlbmd0aCA+IDAgJiYgIXZhbGlkTmFtZUV4cC50ZXN0KG5hbWUpO1xufVxuXG4vKipcbiAqIEEgd2lkZ2V0IHVzZWQgdG8gcmVuYW1lIGEgZmlsZS5cbiAqL1xuY2xhc3MgUmVuYW1lSGFuZGxlciBleHRlbmRzIFdpZGdldCB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgYSBuZXcgXCJyZW5hbWVcIiBkaWFsb2cuXG4gICAqL1xuICBjb25zdHJ1Y3RvcihvbGRQYXRoOiBzdHJpbmcpIHtcbiAgICBzdXBlcih7IG5vZGU6IFByaXZhdGUuY3JlYXRlUmVuYW1lTm9kZShvbGRQYXRoKSB9KTtcbiAgICB0aGlzLmFkZENsYXNzKEZJTEVfRElBTE9HX0NMQVNTKTtcbiAgICBjb25zdCBleHQgPSBQYXRoRXh0LmV4dG5hbWUob2xkUGF0aCk7XG4gICAgY29uc3QgdmFsdWUgPSAodGhpcy5pbnB1dE5vZGUudmFsdWUgPSBQYXRoRXh0LmJhc2VuYW1lKG9sZFBhdGgpKTtcbiAgICB0aGlzLmlucHV0Tm9kZS5zZXRTZWxlY3Rpb25SYW5nZSgwLCB2YWx1ZS5sZW5ndGggLSBleHQubGVuZ3RoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgdGhlIGlucHV0IHRleHQgbm9kZS5cbiAgICovXG4gIGdldCBpbnB1dE5vZGUoKTogSFRNTElucHV0RWxlbWVudCB7XG4gICAgcmV0dXJuIHRoaXMubm9kZS5nZXRFbGVtZW50c0J5VGFnTmFtZSgnaW5wdXQnKVswXSBhcyBIVE1MSW5wdXRFbGVtZW50O1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgdmFsdWUgb2YgdGhlIHdpZGdldC5cbiAgICovXG4gIGdldFZhbHVlKCk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMuaW5wdXROb2RlLnZhbHVlO1xuICB9XG59XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIHByaXZhdGUgZGF0YS5cbiAqL1xubmFtZXNwYWNlIFByaXZhdGUge1xuICAvKipcbiAgICogQ3JlYXRlIHRoZSBub2RlIGZvciBhIHJlbmFtZSBoYW5kbGVyLlxuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIGNyZWF0ZVJlbmFtZU5vZGUoXG4gICAgb2xkUGF0aDogc3RyaW5nLFxuICAgIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvclxuICApOiBIVE1MRWxlbWVudCB7XG4gICAgdHJhbnNsYXRvciA9IHRyYW5zbGF0b3IgfHwgbnVsbFRyYW5zbGF0b3I7XG4gICAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcblxuICAgIGNvbnN0IGJvZHkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdkaXYnKTtcbiAgICBjb25zdCBleGlzdGluZ0xhYmVsID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnbGFiZWwnKTtcbiAgICBleGlzdGluZ0xhYmVsLnRleHRDb250ZW50ID0gdHJhbnMuX18oJ0ZpbGUgUGF0aCcpO1xuICAgIGNvbnN0IGV4aXN0aW5nUGF0aCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3NwYW4nKTtcbiAgICBleGlzdGluZ1BhdGgudGV4dENvbnRlbnQgPSBvbGRQYXRoO1xuXG4gICAgY29uc3QgbmFtZVRpdGxlID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnbGFiZWwnKTtcbiAgICBuYW1lVGl0bGUudGV4dENvbnRlbnQgPSB0cmFucy5fXygnTmV3IE5hbWUnKTtcbiAgICBuYW1lVGl0bGUuY2xhc3NOYW1lID0gUkVOQU1FX05FV19OQU1FX1RJVExFX0NMQVNTO1xuICAgIGNvbnN0IG5hbWUgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdpbnB1dCcpO1xuXG4gICAgYm9keS5hcHBlbmRDaGlsZChleGlzdGluZ0xhYmVsKTtcbiAgICBib2R5LmFwcGVuZENoaWxkKGV4aXN0aW5nUGF0aCk7XG4gICAgYm9keS5hcHBlbmRDaGlsZChuYW1lVGl0bGUpO1xuICAgIGJvZHkuYXBwZW5kQ2hpbGQobmFtZSk7XG4gICAgcmV0dXJuIGJvZHk7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGRvY21hbmFnZXJcbiAqL1xuXG5leHBvcnQgKiBmcm9tICcuL2RpYWxvZ3MnO1xuZXhwb3J0ICogZnJvbSAnLi9tYW5hZ2VyJztcbmV4cG9ydCAqIGZyb20gJy4vcGF0aHN0YXR1cyc7XG5leHBvcnQgKiBmcm9tICcuL3NhdmVoYW5kbGVyJztcbmV4cG9ydCAqIGZyb20gJy4vc2F2aW5nc3RhdHVzJztcbmV4cG9ydCAqIGZyb20gJy4vdG9rZW5zJztcbmV4cG9ydCAqIGZyb20gJy4vd2lkZ2V0bWFuYWdlcic7XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElTZXNzaW9uQ29udGV4dCwgc2Vzc2lvbkNvbnRleHREaWFsb2dzIH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgUGF0aEV4dCB9IGZyb20gJ0BqdXB5dGVybGFiL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBJRG9jdW1lbnRQcm92aWRlckZhY3RvcnkgfSBmcm9tICdAanVweXRlcmxhYi9kb2Nwcm92aWRlcic7XG5pbXBvcnQge1xuICBDb250ZXh0LFxuICBEb2N1bWVudFJlZ2lzdHJ5LFxuICBJRG9jdW1lbnRXaWRnZXRcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jcmVnaXN0cnknO1xuaW1wb3J0IHsgQ29udGVudHMsIEtlcm5lbCwgU2VydmljZU1hbmFnZXIgfSBmcm9tICdAanVweXRlcmxhYi9zZXJ2aWNlcyc7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciwgbnVsbFRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQgeyBBcnJheUV4dCwgZmluZCB9IGZyb20gJ0BsdW1pbm8vYWxnb3JpdGhtJztcbmltcG9ydCB7IFVVSUQgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBBdHRhY2hlZFByb3BlcnR5IH0gZnJvbSAnQGx1bWluby9wcm9wZXJ0aWVzJztcbmltcG9ydCB7IElTaWduYWwsIFNpZ25hbCB9IGZyb20gJ0BsdW1pbm8vc2lnbmFsaW5nJztcbmltcG9ydCB7IFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgeyBTYXZlSGFuZGxlciB9IGZyb20gJy4vc2F2ZWhhbmRsZXInO1xuaW1wb3J0IHsgSURvY3VtZW50TWFuYWdlciB9IGZyb20gJy4vdG9rZW5zJztcbmltcG9ydCB7IERvY3VtZW50V2lkZ2V0TWFuYWdlciB9IGZyb20gJy4vd2lkZ2V0bWFuYWdlcic7XG5cbi8qKlxuICogVGhlIGRvY3VtZW50IG1hbmFnZXIuXG4gKlxuICogIyMjIyBOb3Rlc1xuICogVGhlIGRvY3VtZW50IG1hbmFnZXIgaXMgdXNlZCB0byByZWdpc3RlciBtb2RlbCBhbmQgd2lkZ2V0IGNyZWF0b3JzLFxuICogYW5kIHRoZSBmaWxlIGJyb3dzZXIgdXNlcyB0aGUgZG9jdW1lbnQgbWFuYWdlciB0byBjcmVhdGUgd2lkZ2V0cy4gVGhlXG4gKiBkb2N1bWVudCBtYW5hZ2VyIG1haW50YWlucyBhIGNvbnRleHQgZm9yIGVhY2ggcGF0aCBhbmQgbW9kZWwgdHlwZSB0aGF0IGlzXG4gKiBvcGVuLCBhbmQgYSBsaXN0IG9mIHdpZGdldHMgZm9yIGVhY2ggY29udGV4dC4gVGhlIGRvY3VtZW50IG1hbmFnZXIgaXMgaW5cbiAqIGNvbnRyb2wgb2YgdGhlIHByb3BlciBjbG9zaW5nIGFuZCBkaXNwb3NhbCBvZiB0aGUgd2lkZ2V0cyBhbmQgY29udGV4dHMuXG4gKi9cbmV4cG9ydCBjbGFzcyBEb2N1bWVudE1hbmFnZXIgaW1wbGVtZW50cyBJRG9jdW1lbnRNYW5hZ2VyIHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCBhIG5ldyBkb2N1bWVudCBtYW5hZ2VyLlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogRG9jdW1lbnRNYW5hZ2VyLklPcHRpb25zKSB7XG4gICAgdGhpcy50cmFuc2xhdG9yID0gb3B0aW9ucy50cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIHRoaXMucmVnaXN0cnkgPSBvcHRpb25zLnJlZ2lzdHJ5O1xuICAgIHRoaXMuc2VydmljZXMgPSBvcHRpb25zLm1hbmFnZXI7XG4gICAgdGhpcy5fY29sbGFib3JhdGl2ZSA9ICEhb3B0aW9ucy5jb2xsYWJvcmF0aXZlO1xuICAgIHRoaXMuX2RpYWxvZ3MgPSBvcHRpb25zLnNlc3Npb25EaWFsb2dzIHx8IHNlc3Npb25Db250ZXh0RGlhbG9ncztcbiAgICB0aGlzLl9kb2NQcm92aWRlckZhY3RvcnkgPSBvcHRpb25zLmRvY1Byb3ZpZGVyRmFjdG9yeTtcbiAgICB0aGlzLl9pc0Nvbm5lY3RlZENhbGxiYWNrID0gb3B0aW9ucy5pc0Nvbm5lY3RlZENhbGxiYWNrIHx8ICgoKSA9PiB0cnVlKTtcblxuICAgIHRoaXMuX29wZW5lciA9IG9wdGlvbnMub3BlbmVyO1xuICAgIHRoaXMuX3doZW4gPSBvcHRpb25zLndoZW4gfHwgb3B0aW9ucy5tYW5hZ2VyLnJlYWR5O1xuXG4gICAgY29uc3Qgd2lkZ2V0TWFuYWdlciA9IG5ldyBEb2N1bWVudFdpZGdldE1hbmFnZXIoe1xuICAgICAgcmVnaXN0cnk6IHRoaXMucmVnaXN0cnksXG4gICAgICB0cmFuc2xhdG9yOiB0aGlzLnRyYW5zbGF0b3JcbiAgICB9KTtcbiAgICB3aWRnZXRNYW5hZ2VyLmFjdGl2YXRlUmVxdWVzdGVkLmNvbm5lY3QodGhpcy5fb25BY3RpdmF0ZVJlcXVlc3RlZCwgdGhpcyk7XG4gICAgdGhpcy5fd2lkZ2V0TWFuYWdlciA9IHdpZGdldE1hbmFnZXI7XG4gICAgdGhpcy5fc2V0QnVzeSA9IG9wdGlvbnMuc2V0QnVzeTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgcmVnaXN0cnkgdXNlZCBieSB0aGUgbWFuYWdlci5cbiAgICovXG4gIHJlYWRvbmx5IHJlZ2lzdHJ5OiBEb2N1bWVudFJlZ2lzdHJ5O1xuXG4gIC8qKlxuICAgKiBUaGUgc2VydmljZSBtYW5hZ2VyIHVzZWQgYnkgdGhlIG1hbmFnZXIuXG4gICAqL1xuICByZWFkb25seSBzZXJ2aWNlczogU2VydmljZU1hbmFnZXIuSU1hbmFnZXI7XG5cbiAgLyoqXG4gICAqIEEgc2lnbmFsIGVtaXR0ZWQgd2hlbiBvbmUgb2YgdGhlIGRvY3VtZW50cyBpcyBhY3RpdmF0ZWQuXG4gICAqL1xuICBnZXQgYWN0aXZhdGVSZXF1ZXN0ZWQoKTogSVNpZ25hbDx0aGlzLCBzdHJpbmc+IHtcbiAgICByZXR1cm4gdGhpcy5fYWN0aXZhdGVSZXF1ZXN0ZWQ7XG4gIH1cblxuICAvKipcbiAgICogV2hldGhlciB0byBhdXRvc2F2ZSBkb2N1bWVudHMuXG4gICAqL1xuICBnZXQgYXV0b3NhdmUoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuX2F1dG9zYXZlO1xuICB9XG5cbiAgc2V0IGF1dG9zYXZlKHZhbHVlOiBib29sZWFuKSB7XG4gICAgdGhpcy5fYXV0b3NhdmUgPSB2YWx1ZTtcblxuICAgIC8vIEZvciBlYWNoIGV4aXN0aW5nIGNvbnRleHQsIHN0YXJ0L3N0b3AgdGhlIGF1dG9zYXZlIGhhbmRsZXIgYXMgbmVlZGVkLlxuICAgIHRoaXMuX2NvbnRleHRzLmZvckVhY2goY29udGV4dCA9PiB7XG4gICAgICBjb25zdCBoYW5kbGVyID0gUHJpdmF0ZS5zYXZlSGFuZGxlclByb3BlcnR5LmdldChjb250ZXh0KTtcbiAgICAgIGlmICghaGFuZGxlcikge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICBpZiAodmFsdWUgPT09IHRydWUgJiYgIWhhbmRsZXIuaXNBY3RpdmUpIHtcbiAgICAgICAgaGFuZGxlci5zdGFydCgpO1xuICAgICAgfSBlbHNlIGlmICh2YWx1ZSA9PT0gZmFsc2UgJiYgaGFuZGxlci5pc0FjdGl2ZSkge1xuICAgICAgICBoYW5kbGVyLnN0b3AoKTtcbiAgICAgIH1cbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBEZXRlcm1pbmVzIHRoZSB0aW1lIGludGVydmFsIGZvciBhdXRvc2F2ZSBpbiBzZWNvbmRzLlxuICAgKi9cbiAgZ2V0IGF1dG9zYXZlSW50ZXJ2YWwoKTogbnVtYmVyIHtcbiAgICByZXR1cm4gdGhpcy5fYXV0b3NhdmVJbnRlcnZhbDtcbiAgfVxuXG4gIHNldCBhdXRvc2F2ZUludGVydmFsKHZhbHVlOiBudW1iZXIpIHtcbiAgICB0aGlzLl9hdXRvc2F2ZUludGVydmFsID0gdmFsdWU7XG5cbiAgICAvLyBGb3IgZWFjaCBleGlzdGluZyBjb250ZXh0LCBzZXQgdGhlIHNhdmUgaW50ZXJ2YWwgYXMgbmVlZGVkLlxuICAgIHRoaXMuX2NvbnRleHRzLmZvckVhY2goY29udGV4dCA9PiB7XG4gICAgICBjb25zdCBoYW5kbGVyID0gUHJpdmF0ZS5zYXZlSGFuZGxlclByb3BlcnR5LmdldChjb250ZXh0KTtcbiAgICAgIGlmICghaGFuZGxlcikge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICBoYW5kbGVyLnNhdmVJbnRlcnZhbCA9IHZhbHVlIHx8IDEyMDtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBEZWZpbmVzIG1heCBhY2NlcHRhYmxlIGRpZmZlcmVuY2UsIGluIG1pbGxpc2Vjb25kcywgYmV0d2VlbiBsYXN0IG1vZGlmaWVkIHRpbWVzdGFtcHMgb24gZGlzayBhbmQgY2xpZW50XG4gICAqL1xuICBnZXQgbGFzdE1vZGlmaWVkQ2hlY2tNYXJnaW4oKTogbnVtYmVyIHtcbiAgICByZXR1cm4gdGhpcy5fbGFzdE1vZGlmaWVkQ2hlY2tNYXJnaW47XG4gIH1cblxuICBzZXQgbGFzdE1vZGlmaWVkQ2hlY2tNYXJnaW4odmFsdWU6IG51bWJlcikge1xuICAgIHRoaXMuX2xhc3RNb2RpZmllZENoZWNrTWFyZ2luID0gdmFsdWU7XG5cbiAgICAvLyBGb3IgZWFjaCBleGlzdGluZyBjb250ZXh0LCB1cGRhdGUgdGhlIG1hcmdpbiB2YWx1ZS5cbiAgICB0aGlzLl9jb250ZXh0cy5mb3JFYWNoKGNvbnRleHQgPT4ge1xuICAgICAgY29udGV4dC5sYXN0TW9kaWZpZWRDaGVja01hcmdpbiA9IHZhbHVlO1xuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIFdoZXRoZXIgdG8gYXNrIHRoZSB1c2VyIHRvIHJlbmFtZSB1bnRpdGxlZCBmaWxlIG9uIGZpcnN0IG1hbnVhbCBzYXZlLlxuICAgKi9cbiAgZ2V0IHJlbmFtZVVudGl0bGVkRmlsZU9uU2F2ZSgpOiBib29sZWFuIHtcbiAgICByZXR1cm4gdGhpcy5fcmVuYW1lVW50aXRsZWRGaWxlT25TYXZlO1xuICB9XG5cbiAgc2V0IHJlbmFtZVVudGl0bGVkRmlsZU9uU2F2ZSh2YWx1ZTogYm9vbGVhbikge1xuICAgIHRoaXMuX3JlbmFtZVVudGl0bGVkRmlsZU9uU2F2ZSA9IHZhbHVlO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB3aGV0aGVyIHRoZSBkb2N1bWVudCBtYW5hZ2VyIGhhcyBiZWVuIGRpc3Bvc2VkLlxuICAgKi9cbiAgZ2V0IGlzRGlzcG9zZWQoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuX2lzRGlzcG9zZWQ7XG4gIH1cblxuICAvKipcbiAgICogRGlzcG9zZSBvZiB0aGUgcmVzb3VyY2VzIGhlbGQgYnkgdGhlIGRvY3VtZW50IG1hbmFnZXIuXG4gICAqL1xuICBkaXNwb3NlKCk6IHZvaWQge1xuICAgIGlmICh0aGlzLmlzRGlzcG9zZWQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgdGhpcy5faXNEaXNwb3NlZCA9IHRydWU7XG5cbiAgICAvLyBDbGVhciBhbnkgbGlzdGVuZXJzIGZvciBvdXIgc2lnbmFscy5cbiAgICBTaWduYWwuY2xlYXJEYXRhKHRoaXMpO1xuXG4gICAgLy8gQ2xvc2UgYWxsIHRoZSB3aWRnZXRzIGZvciBvdXIgY29udGV4dHMgYW5kIGRpc3Bvc2UgdGhlIHdpZGdldCBtYW5hZ2VyLlxuICAgIHRoaXMuX2NvbnRleHRzLmZvckVhY2goY29udGV4dCA9PiB7XG4gICAgICByZXR1cm4gdGhpcy5fd2lkZ2V0TWFuYWdlci5jbG9zZVdpZGdldHMoY29udGV4dCk7XG4gICAgfSk7XG4gICAgdGhpcy5fd2lkZ2V0TWFuYWdlci5kaXNwb3NlKCk7XG5cbiAgICAvLyBDbGVhciB0aGUgY29udGV4dCBsaXN0LlxuICAgIHRoaXMuX2NvbnRleHRzLmxlbmd0aCA9IDA7XG4gIH1cblxuICAvKipcbiAgICogQ2xvbmUgYSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgLSBUaGUgc291cmNlIHdpZGdldC5cbiAgICpcbiAgICogQHJldHVybnMgQSBuZXcgd2lkZ2V0IG9yIGB1bmRlZmluZWRgLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqICBVc2VzIHRoZSBzYW1lIHdpZGdldCBmYWN0b3J5IGFuZCBjb250ZXh0IGFzIHRoZSBzb3VyY2UsIG9yIHJldHVybnNcbiAgICogIGB1bmRlZmluZWRgIGlmIHRoZSBzb3VyY2Ugd2lkZ2V0IGlzIG5vdCBtYW5hZ2VkIGJ5IHRoaXMgbWFuYWdlci5cbiAgICovXG4gIGNsb25lV2lkZ2V0KHdpZGdldDogV2lkZ2V0KTogSURvY3VtZW50V2lkZ2V0IHwgdW5kZWZpbmVkIHtcbiAgICByZXR1cm4gdGhpcy5fd2lkZ2V0TWFuYWdlci5jbG9uZVdpZGdldCh3aWRnZXQpO1xuICB9XG5cbiAgLyoqXG4gICAqIENsb3NlIGFsbCBvZiB0aGUgb3BlbiBkb2N1bWVudHMuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSByZXNvbHZpbmcgd2hlbiB0aGUgd2lkZ2V0cyBhcmUgY2xvc2VkLlxuICAgKi9cbiAgY2xvc2VBbGwoKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgcmV0dXJuIFByb21pc2UuYWxsKFxuICAgICAgdGhpcy5fY29udGV4dHMubWFwKGNvbnRleHQgPT4gdGhpcy5fd2lkZ2V0TWFuYWdlci5jbG9zZVdpZGdldHMoY29udGV4dCkpXG4gICAgKS50aGVuKCgpID0+IHVuZGVmaW5lZCk7XG4gIH1cblxuICAvKipcbiAgICogQ2xvc2UgdGhlIHdpZGdldHMgYXNzb2NpYXRlZCB3aXRoIGEgZ2l2ZW4gcGF0aC5cbiAgICpcbiAgICogQHBhcmFtIHBhdGggLSBUaGUgdGFyZ2V0IHBhdGguXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSByZXNvbHZpbmcgd2hlbiB0aGUgd2lkZ2V0cyBhcmUgY2xvc2VkLlxuICAgKi9cbiAgY2xvc2VGaWxlKHBhdGg6IHN0cmluZyk6IFByb21pc2U8dm9pZD4ge1xuICAgIGNvbnN0IGNsb3NlID0gdGhpcy5fY29udGV4dHNGb3JQYXRoKHBhdGgpLm1hcChjID0+XG4gICAgICB0aGlzLl93aWRnZXRNYW5hZ2VyLmNsb3NlV2lkZ2V0cyhjKVxuICAgICk7XG4gICAgcmV0dXJuIFByb21pc2UuYWxsKGNsb3NlKS50aGVuKHggPT4gdW5kZWZpbmVkKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgdGhlIGRvY3VtZW50IGNvbnRleHQgZm9yIGEgd2lkZ2V0LlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IC0gVGhlIHdpZGdldCBvZiBpbnRlcmVzdC5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIGNvbnRleHQgYXNzb2NpYXRlZCB3aXRoIHRoZSB3aWRnZXQsIG9yIGB1bmRlZmluZWRgIGlmIG5vIHN1Y2hcbiAgICogY29udGV4dCBleGlzdHMuXG4gICAqL1xuICBjb250ZXh0Rm9yV2lkZ2V0KHdpZGdldDogV2lkZ2V0KTogRG9jdW1lbnRSZWdpc3RyeS5Db250ZXh0IHwgdW5kZWZpbmVkIHtcbiAgICByZXR1cm4gdGhpcy5fd2lkZ2V0TWFuYWdlci5jb250ZXh0Rm9yV2lkZ2V0KHdpZGdldCk7XG4gIH1cblxuICAvKipcbiAgICogQ29weSBhIGZpbGUuXG4gICAqXG4gICAqIEBwYXJhbSBmcm9tRmlsZSAtIFRoZSBmdWxsIHBhdGggb2YgdGhlIG9yaWdpbmFsIGZpbGUuXG4gICAqXG4gICAqIEBwYXJhbSB0b0RpciAtIFRoZSBmdWxsIHBhdGggdG8gdGhlIHRhcmdldCBkaXJlY3RvcnkuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB3aGljaCByZXNvbHZlcyB0byB0aGUgY29udGVudHMgb2YgdGhlIGZpbGUuXG4gICAqL1xuICBjb3B5KGZyb21GaWxlOiBzdHJpbmcsIHRvRGlyOiBzdHJpbmcpOiBQcm9taXNlPENvbnRlbnRzLklNb2RlbD4ge1xuICAgIHJldHVybiB0aGlzLnNlcnZpY2VzLmNvbnRlbnRzLmNvcHkoZnJvbUZpbGUsIHRvRGlyKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBDcmVhdGUgYSBuZXcgZmlsZSBhbmQgcmV0dXJuIHRoZSB3aWRnZXQgdXNlZCB0byB2aWV3IGl0LlxuICAgKlxuICAgKiBAcGFyYW0gcGF0aCAtIFRoZSBmaWxlIHBhdGggdG8gY3JlYXRlLlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0TmFtZSAtIFRoZSBuYW1lIG9mIHRoZSB3aWRnZXQgZmFjdG9yeSB0byB1c2UuICdkZWZhdWx0JyB3aWxsIHVzZSB0aGUgZGVmYXVsdCB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSBrZXJuZWwgLSBBbiBvcHRpb25hbCBrZXJuZWwgbmFtZS9pZCB0byBvdmVycmlkZSB0aGUgZGVmYXVsdC5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIGNyZWF0ZWQgd2lkZ2V0LCBvciBgdW5kZWZpbmVkYC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGlzIGZ1bmN0aW9uIHdpbGwgcmV0dXJuIGB1bmRlZmluZWRgIGlmIGEgdmFsaWQgd2lkZ2V0IGZhY3RvcnlcbiAgICogY2Fubm90IGJlIGZvdW5kLlxuICAgKi9cbiAgY3JlYXRlTmV3KFxuICAgIHBhdGg6IHN0cmluZyxcbiAgICB3aWRnZXROYW1lID0gJ2RlZmF1bHQnLFxuICAgIGtlcm5lbD86IFBhcnRpYWw8S2VybmVsLklNb2RlbD5cbiAgKTogV2lkZ2V0IHwgdW5kZWZpbmVkIHtcbiAgICByZXR1cm4gdGhpcy5fY3JlYXRlT3JPcGVuRG9jdW1lbnQoJ2NyZWF0ZScsIHBhdGgsIHdpZGdldE5hbWUsIGtlcm5lbCk7XG4gIH1cblxuICAvKipcbiAgICogRGVsZXRlIGEgZmlsZS5cbiAgICpcbiAgICogQHBhcmFtIHBhdGggLSBUaGUgZnVsbCBwYXRoIHRvIHRoZSBmaWxlIHRvIGJlIGRlbGV0ZWQuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB3aGljaCByZXNvbHZlcyB3aGVuIHRoZSBmaWxlIGlzIGRlbGV0ZWQuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogSWYgdGhlcmUgaXMgYSBydW5uaW5nIHNlc3Npb24gYXNzb2NpYXRlZCB3aXRoIHRoZSBmaWxlIGFuZCBubyBvdGhlclxuICAgKiBzZXNzaW9ucyBhcmUgdXNpbmcgdGhlIGtlcm5lbCwgdGhlIHNlc3Npb24gd2lsbCBiZSBzaHV0IGRvd24uXG4gICAqL1xuICBkZWxldGVGaWxlKHBhdGg6IHN0cmluZyk6IFByb21pc2U8dm9pZD4ge1xuICAgIHJldHVybiB0aGlzLnNlcnZpY2VzLnNlc3Npb25zXG4gICAgICAuc3RvcElmTmVlZGVkKHBhdGgpXG4gICAgICAudGhlbigoKSA9PiB7XG4gICAgICAgIHJldHVybiB0aGlzLnNlcnZpY2VzLmNvbnRlbnRzLmRlbGV0ZShwYXRoKTtcbiAgICAgIH0pXG4gICAgICAudGhlbigoKSA9PiB7XG4gICAgICAgIHRoaXMuX2NvbnRleHRzRm9yUGF0aChwYXRoKS5mb3JFYWNoKGNvbnRleHQgPT5cbiAgICAgICAgICB0aGlzLl93aWRnZXRNYW5hZ2VyLmRlbGV0ZVdpZGdldHMoY29udGV4dClcbiAgICAgICAgKTtcbiAgICAgICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZSh2b2lkIDApO1xuICAgICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogRHVwbGljYXRlIGEgZmlsZS5cbiAgICpcbiAgICogQHBhcmFtIHBhdGggLSBUaGUgZnVsbCBwYXRoIHRvIHRoZSBmaWxlIHRvIGJlIGR1cGxpY2F0ZWQuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB3aGljaCByZXNvbHZlcyB3aGVuIHRoZSBmaWxlIGlzIGR1cGxpY2F0ZWQuXG4gICAqL1xuICBkdXBsaWNhdGUocGF0aDogc3RyaW5nKTogUHJvbWlzZTxDb250ZW50cy5JTW9kZWw+IHtcbiAgICBjb25zdCBiYXNlUGF0aCA9IFBhdGhFeHQuZGlybmFtZShwYXRoKTtcbiAgICByZXR1cm4gdGhpcy5zZXJ2aWNlcy5jb250ZW50cy5jb3B5KHBhdGgsIGJhc2VQYXRoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZWUgaWYgYSB3aWRnZXQgYWxyZWFkeSBleGlzdHMgZm9yIHRoZSBnaXZlbiBwYXRoIGFuZCB3aWRnZXQgbmFtZS5cbiAgICpcbiAgICogQHBhcmFtIHBhdGggLSBUaGUgZmlsZSBwYXRoIHRvIHVzZS5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldE5hbWUgLSBUaGUgbmFtZSBvZiB0aGUgd2lkZ2V0IGZhY3RvcnkgdG8gdXNlLiAnZGVmYXVsdCcgd2lsbCB1c2UgdGhlIGRlZmF1bHQgd2lkZ2V0LlxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgZm91bmQgd2lkZ2V0LCBvciBgdW5kZWZpbmVkYC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGlzIGNhbiBiZSB1c2VkIHRvIGZpbmQgYW4gZXhpc3Rpbmcgd2lkZ2V0IGluc3RlYWQgb2Ygb3BlbmluZ1xuICAgKiBhIG5ldyB3aWRnZXQuXG4gICAqL1xuICBmaW5kV2lkZ2V0KFxuICAgIHBhdGg6IHN0cmluZyxcbiAgICB3aWRnZXROYW1lOiBzdHJpbmcgfCBudWxsID0gJ2RlZmF1bHQnXG4gICk6IElEb2N1bWVudFdpZGdldCB8IHVuZGVmaW5lZCB7XG4gICAgY29uc3QgbmV3UGF0aCA9IFBhdGhFeHQubm9ybWFsaXplKHBhdGgpO1xuICAgIGxldCB3aWRnZXROYW1lcyA9IFt3aWRnZXROYW1lXTtcbiAgICBpZiAod2lkZ2V0TmFtZSA9PT0gJ2RlZmF1bHQnKSB7XG4gICAgICBjb25zdCBmYWN0b3J5ID0gdGhpcy5yZWdpc3RyeS5kZWZhdWx0V2lkZ2V0RmFjdG9yeShuZXdQYXRoKTtcbiAgICAgIGlmICghZmFjdG9yeSkge1xuICAgICAgICByZXR1cm4gdW5kZWZpbmVkO1xuICAgICAgfVxuICAgICAgd2lkZ2V0TmFtZXMgPSBbZmFjdG9yeS5uYW1lXTtcbiAgICB9IGVsc2UgaWYgKHdpZGdldE5hbWUgPT09IG51bGwpIHtcbiAgICAgIHdpZGdldE5hbWVzID0gdGhpcy5yZWdpc3RyeVxuICAgICAgICAucHJlZmVycmVkV2lkZ2V0RmFjdG9yaWVzKG5ld1BhdGgpXG4gICAgICAgIC5tYXAoZiA9PiBmLm5hbWUpO1xuICAgIH1cblxuICAgIGZvciAoY29uc3QgY29udGV4dCBvZiB0aGlzLl9jb250ZXh0c0ZvclBhdGgobmV3UGF0aCkpIHtcbiAgICAgIGZvciAoY29uc3Qgd2lkZ2V0TmFtZSBvZiB3aWRnZXROYW1lcykge1xuICAgICAgICBpZiAod2lkZ2V0TmFtZSAhPT0gbnVsbCkge1xuICAgICAgICAgIGNvbnN0IHdpZGdldCA9IHRoaXMuX3dpZGdldE1hbmFnZXIuZmluZFdpZGdldChjb250ZXh0LCB3aWRnZXROYW1lKTtcbiAgICAgICAgICBpZiAod2lkZ2V0KSB7XG4gICAgICAgICAgICByZXR1cm4gd2lkZ2V0O1xuICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgfVxuICAgIH1cbiAgICByZXR1cm4gdW5kZWZpbmVkO1xuICB9XG5cbiAgLyoqXG4gICAqIENyZWF0ZSBhIG5ldyB1bnRpdGxlZCBmaWxlLlxuICAgKlxuICAgKiBAcGFyYW0gb3B0aW9ucyAtIFRoZSBmaWxlIGNvbnRlbnQgY3JlYXRpb24gb3B0aW9ucy5cbiAgICovXG4gIG5ld1VudGl0bGVkKG9wdGlvbnM6IENvbnRlbnRzLklDcmVhdGVPcHRpb25zKTogUHJvbWlzZTxDb250ZW50cy5JTW9kZWw+IHtcbiAgICBpZiAob3B0aW9ucy50eXBlID09PSAnZmlsZScpIHtcbiAgICAgIG9wdGlvbnMuZXh0ID0gb3B0aW9ucy5leHQgfHwgJy50eHQnO1xuICAgIH1cbiAgICByZXR1cm4gdGhpcy5zZXJ2aWNlcy5jb250ZW50cy5uZXdVbnRpdGxlZChvcHRpb25zKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBPcGVuIGEgZmlsZSBhbmQgcmV0dXJuIHRoZSB3aWRnZXQgdXNlZCB0byB2aWV3IGl0LlxuICAgKlxuICAgKiBAcGFyYW0gcGF0aCAtIFRoZSBmaWxlIHBhdGggdG8gb3Blbi5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldE5hbWUgLSBUaGUgbmFtZSBvZiB0aGUgd2lkZ2V0IGZhY3RvcnkgdG8gdXNlLiAnZGVmYXVsdCcgd2lsbCB1c2UgdGhlIGRlZmF1bHQgd2lkZ2V0LlxuICAgKlxuICAgKiBAcGFyYW0ga2VybmVsIC0gQW4gb3B0aW9uYWwga2VybmVsIG5hbWUvaWQgdG8gb3ZlcnJpZGUgdGhlIGRlZmF1bHQuXG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSBjcmVhdGVkIHdpZGdldCwgb3IgYHVuZGVmaW5lZGAuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBmdW5jdGlvbiB3aWxsIHJldHVybiBgdW5kZWZpbmVkYCBpZiBhIHZhbGlkIHdpZGdldCBmYWN0b3J5XG4gICAqIGNhbm5vdCBiZSBmb3VuZC5cbiAgICovXG4gIG9wZW4oXG4gICAgcGF0aDogc3RyaW5nLFxuICAgIHdpZGdldE5hbWUgPSAnZGVmYXVsdCcsXG4gICAga2VybmVsPzogUGFydGlhbDxLZXJuZWwuSU1vZGVsPixcbiAgICBvcHRpb25zPzogRG9jdW1lbnRSZWdpc3RyeS5JT3Blbk9wdGlvbnNcbiAgKTogSURvY3VtZW50V2lkZ2V0IHwgdW5kZWZpbmVkIHtcbiAgICByZXR1cm4gdGhpcy5fY3JlYXRlT3JPcGVuRG9jdW1lbnQoXG4gICAgICAnb3BlbicsXG4gICAgICBwYXRoLFxuICAgICAgd2lkZ2V0TmFtZSxcbiAgICAgIGtlcm5lbCxcbiAgICAgIG9wdGlvbnNcbiAgICApO1xuICB9XG5cbiAgLyoqXG4gICAqIE9wZW4gYSBmaWxlIGFuZCByZXR1cm4gdGhlIHdpZGdldCB1c2VkIHRvIHZpZXcgaXQuXG4gICAqIFJldmVhbHMgYW4gYWxyZWFkeSBleGlzdGluZyBlZGl0b3IuXG4gICAqXG4gICAqIEBwYXJhbSBwYXRoIC0gVGhlIGZpbGUgcGF0aCB0byBvcGVuLlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0TmFtZSAtIFRoZSBuYW1lIG9mIHRoZSB3aWRnZXQgZmFjdG9yeSB0byB1c2UuICdkZWZhdWx0JyB3aWxsIHVzZSB0aGUgZGVmYXVsdCB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSBrZXJuZWwgLSBBbiBvcHRpb25hbCBrZXJuZWwgbmFtZS9pZCB0byBvdmVycmlkZSB0aGUgZGVmYXVsdC5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIGNyZWF0ZWQgd2lkZ2V0LCBvciBgdW5kZWZpbmVkYC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGlzIGZ1bmN0aW9uIHdpbGwgcmV0dXJuIGB1bmRlZmluZWRgIGlmIGEgdmFsaWQgd2lkZ2V0IGZhY3RvcnlcbiAgICogY2Fubm90IGJlIGZvdW5kLlxuICAgKi9cbiAgb3Blbk9yUmV2ZWFsKFxuICAgIHBhdGg6IHN0cmluZyxcbiAgICB3aWRnZXROYW1lID0gJ2RlZmF1bHQnLFxuICAgIGtlcm5lbD86IFBhcnRpYWw8S2VybmVsLklNb2RlbD4sXG4gICAgb3B0aW9ucz86IERvY3VtZW50UmVnaXN0cnkuSU9wZW5PcHRpb25zXG4gICk6IElEb2N1bWVudFdpZGdldCB8IHVuZGVmaW5lZCB7XG4gICAgY29uc3Qgd2lkZ2V0ID0gdGhpcy5maW5kV2lkZ2V0KHBhdGgsIHdpZGdldE5hbWUpO1xuICAgIGlmICh3aWRnZXQpIHtcbiAgICAgIHRoaXMuX29wZW5lci5vcGVuKHdpZGdldCwge1xuICAgICAgICB0eXBlOiB3aWRnZXROYW1lLFxuICAgICAgICAuLi5vcHRpb25zXG4gICAgICB9KTtcbiAgICAgIHJldHVybiB3aWRnZXQ7XG4gICAgfVxuICAgIHJldHVybiB0aGlzLm9wZW4ocGF0aCwgd2lkZ2V0TmFtZSwga2VybmVsLCBvcHRpb25zID8/IHt9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBPdmVyd3JpdGUgYSBmaWxlLlxuICAgKlxuICAgKiBAcGFyYW0gb2xkUGF0aCAtIFRoZSBmdWxsIHBhdGggdG8gdGhlIG9yaWdpbmFsIGZpbGUuXG4gICAqXG4gICAqIEBwYXJhbSBuZXdQYXRoIC0gVGhlIGZ1bGwgcGF0aCB0byB0aGUgbmV3IGZpbGUuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSBjb250YWluaW5nIHRoZSBuZXcgZmlsZSBjb250ZW50cyBtb2RlbC5cbiAgICovXG4gIG92ZXJ3cml0ZShvbGRQYXRoOiBzdHJpbmcsIG5ld1BhdGg6IHN0cmluZyk6IFByb21pc2U8Q29udGVudHMuSU1vZGVsPiB7XG4gICAgLy8gQ2xlYW5seSBvdmVyd3JpdGUgdGhlIGZpbGUgYnkgbW92aW5nIGl0LCBtYWtpbmcgc3VyZSB0aGUgb3JpZ2luYWwgZG9lc1xuICAgIC8vIG5vdCBleGlzdCwgYW5kIHRoZW4gcmVuYW1pbmcgdG8gdGhlIG5ldyBwYXRoLlxuICAgIGNvbnN0IHRlbXBQYXRoID0gYCR7bmV3UGF0aH0uJHtVVUlELnV1aWQ0KCl9YDtcbiAgICBjb25zdCBjYiA9ICgpID0+IHRoaXMucmVuYW1lKHRlbXBQYXRoLCBuZXdQYXRoKTtcbiAgICByZXR1cm4gdGhpcy5yZW5hbWUob2xkUGF0aCwgdGVtcFBhdGgpXG4gICAgICAudGhlbigoKSA9PiB7XG4gICAgICAgIHJldHVybiB0aGlzLmRlbGV0ZUZpbGUobmV3UGF0aCk7XG4gICAgICB9KVxuICAgICAgLnRoZW4oY2IsIGNiKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5hbWUgYSBmaWxlIG9yIGRpcmVjdG9yeS5cbiAgICpcbiAgICogQHBhcmFtIG9sZFBhdGggLSBUaGUgZnVsbCBwYXRoIHRvIHRoZSBvcmlnaW5hbCBmaWxlLlxuICAgKlxuICAgKiBAcGFyYW0gbmV3UGF0aCAtIFRoZSBmdWxsIHBhdGggdG8gdGhlIG5ldyBmaWxlLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2UgY29udGFpbmluZyB0aGUgbmV3IGZpbGUgY29udGVudHMgbW9kZWwuICBUaGUgcHJvbWlzZVxuICAgKiB3aWxsIHJlamVjdCBpZiB0aGUgbmV3UGF0aCBhbHJlYWR5IGV4aXN0cy4gIFVzZSBbW292ZXJ3cml0ZV1dIHRvIG92ZXJ3cml0ZVxuICAgKiBhIGZpbGUuXG4gICAqL1xuICByZW5hbWUob2xkUGF0aDogc3RyaW5nLCBuZXdQYXRoOiBzdHJpbmcpOiBQcm9taXNlPENvbnRlbnRzLklNb2RlbD4ge1xuICAgIHJldHVybiB0aGlzLnNlcnZpY2VzLmNvbnRlbnRzLnJlbmFtZShvbGRQYXRoLCBuZXdQYXRoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBGaW5kIGEgY29udGV4dCBmb3IgYSBnaXZlbiBwYXRoIGFuZCBmYWN0b3J5IG5hbWUuXG4gICAqL1xuICBwcml2YXRlIF9maW5kQ29udGV4dChcbiAgICBwYXRoOiBzdHJpbmcsXG4gICAgZmFjdG9yeU5hbWU6IHN0cmluZ1xuICApOiBQcml2YXRlLklDb250ZXh0IHwgdW5kZWZpbmVkIHtcbiAgICBjb25zdCBub3JtYWxpemVkUGF0aCA9IHRoaXMuc2VydmljZXMuY29udGVudHMubm9ybWFsaXplKHBhdGgpO1xuICAgIHJldHVybiBmaW5kKHRoaXMuX2NvbnRleHRzLCBjb250ZXh0ID0+IHtcbiAgICAgIHJldHVybiAoXG4gICAgICAgIGNvbnRleHQucGF0aCA9PT0gbm9ybWFsaXplZFBhdGggJiYgY29udGV4dC5mYWN0b3J5TmFtZSA9PT0gZmFjdG9yeU5hbWVcbiAgICAgICk7XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogR2V0IHRoZSBjb250ZXh0cyBmb3IgYSBnaXZlbiBwYXRoLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoZXJlIG1heSBiZSBtb3JlIHRoYW4gb25lIGNvbnRleHQgZm9yIGEgZ2l2ZW4gcGF0aCBpZiB0aGUgcGF0aCBpcyBvcGVuXG4gICAqIHdpdGggbXVsdGlwbGUgbW9kZWwgZmFjdG9yaWVzIChmb3IgZXhhbXBsZSwgYSBub3RlYm9vayBjYW4gYmUgb3BlbiB3aXRoIGFcbiAgICogbm90ZWJvb2sgbW9kZWwgZmFjdG9yeSBhbmQgYSB0ZXh0IG1vZGVsIGZhY3RvcnkpLlxuICAgKi9cbiAgcHJpdmF0ZSBfY29udGV4dHNGb3JQYXRoKHBhdGg6IHN0cmluZyk6IFByaXZhdGUuSUNvbnRleHRbXSB7XG4gICAgY29uc3Qgbm9ybWFsaXplZFBhdGggPSB0aGlzLnNlcnZpY2VzLmNvbnRlbnRzLm5vcm1hbGl6ZShwYXRoKTtcbiAgICByZXR1cm4gdGhpcy5fY29udGV4dHMuZmlsdGVyKGNvbnRleHQgPT4gY29udGV4dC5wYXRoID09PSBub3JtYWxpemVkUGF0aCk7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGEgY29udGV4dCBmcm9tIGEgcGF0aCBhbmQgYSBtb2RlbCBmYWN0b3J5LlxuICAgKi9cbiAgcHJpdmF0ZSBfY3JlYXRlQ29udGV4dChcbiAgICBwYXRoOiBzdHJpbmcsXG4gICAgZmFjdG9yeTogRG9jdW1lbnRSZWdpc3RyeS5Nb2RlbEZhY3RvcnksXG4gICAga2VybmVsUHJlZmVyZW5jZT86IElTZXNzaW9uQ29udGV4dC5JS2VybmVsUHJlZmVyZW5jZVxuICApOiBQcml2YXRlLklDb250ZXh0IHtcbiAgICAvLyBUT0RPOiBNYWtlIGl0IGltcG9zc2libGUgdG8gb3BlbiB0d28gZGlmZmVyZW50IGNvbnRleHRzIGZvciB0aGUgc2FtZVxuICAgIC8vIHBhdGguIE9yIGF0IGxlYXN0IHByb21wdCB0aGUgY2xvc2luZyBvZiBhbGwgd2lkZ2V0cyBhc3NvY2lhdGVkIHdpdGggdGhlXG4gICAgLy8gb2xkIGNvbnRleHQgYmVmb3JlIG9wZW5pbmcgdGhlIG5ldyBjb250ZXh0LiBUaGlzIHdpbGwgbWFrZSB0aGluZ3MgbXVjaFxuICAgIC8vIG1vcmUgY29uc2lzdGVudCBmb3IgdGhlIHVzZXJzLCBhdCB0aGUgY29zdCBvZiBzb21lIGNvbmZ1c2lvbiBhYm91dCB3aGF0XG4gICAgLy8gbW9kZWxzIGFyZSBhbmQgd2h5IHNvbWV0aW1lcyB0aGV5IGNhbm5vdCBvcGVuIHRoZSBzYW1lIGZpbGUgaW4gZGlmZmVyZW50XG4gICAgLy8gd2lkZ2V0cyB0aGF0IGhhdmUgZGlmZmVyZW50IG1vZGVscy5cblxuICAgIC8vIEFsbG93IG9wdGlvbnMgdG8gYmUgcGFzc2VkIHdoZW4gYWRkaW5nIGEgc2libGluZy5cbiAgICBjb25zdCBhZG9wdGVyID0gKFxuICAgICAgd2lkZ2V0OiBJRG9jdW1lbnRXaWRnZXQsXG4gICAgICBvcHRpb25zPzogRG9jdW1lbnRSZWdpc3RyeS5JT3Blbk9wdGlvbnNcbiAgICApID0+IHtcbiAgICAgIHRoaXMuX3dpZGdldE1hbmFnZXIuYWRvcHRXaWRnZXQoY29udGV4dCwgd2lkZ2V0KTtcbiAgICAgIC8vIFRPRE8gc2hvdWxkIHdlIHBhc3MgdGhlIHR5cGUgZm9yIGxheW91dCBjdXN0b21pemF0aW9uXG4gICAgICB0aGlzLl9vcGVuZXIub3Blbih3aWRnZXQsIG9wdGlvbnMpO1xuICAgIH07XG4gICAgY29uc3QgbW9kZWxEQkZhY3RvcnkgPVxuICAgICAgdGhpcy5zZXJ2aWNlcy5jb250ZW50cy5nZXRNb2RlbERCRmFjdG9yeShwYXRoKSB8fCB1bmRlZmluZWQ7XG4gICAgY29uc3QgY29udGV4dCA9IG5ldyBDb250ZXh0KHtcbiAgICAgIG9wZW5lcjogYWRvcHRlcixcbiAgICAgIG1hbmFnZXI6IHRoaXMuc2VydmljZXMsXG4gICAgICBmYWN0b3J5LFxuICAgICAgcGF0aCxcbiAgICAgIGtlcm5lbFByZWZlcmVuY2UsXG4gICAgICBtb2RlbERCRmFjdG9yeSxcbiAgICAgIHNldEJ1c3k6IHRoaXMuX3NldEJ1c3ksXG4gICAgICBzZXNzaW9uRGlhbG9nczogdGhpcy5fZGlhbG9ncyxcbiAgICAgIGNvbGxhYm9yYXRpdmU6IHRoaXMuX2NvbGxhYm9yYXRpdmUsXG4gICAgICBkb2NQcm92aWRlckZhY3Rvcnk6IHRoaXMuX2RvY1Byb3ZpZGVyRmFjdG9yeSxcbiAgICAgIGxhc3RNb2RpZmllZENoZWNrTWFyZ2luOiB0aGlzLl9sYXN0TW9kaWZpZWRDaGVja01hcmdpbixcbiAgICAgIHRyYW5zbGF0b3I6IHRoaXMudHJhbnNsYXRvclxuICAgIH0pO1xuICAgIGNvbnN0IGhhbmRsZXIgPSBuZXcgU2F2ZUhhbmRsZXIoe1xuICAgICAgY29udGV4dCxcbiAgICAgIGlzQ29ubmVjdGVkQ2FsbGJhY2s6IHRoaXMuX2lzQ29ubmVjdGVkQ2FsbGJhY2ssXG4gICAgICBzYXZlSW50ZXJ2YWw6IHRoaXMuYXV0b3NhdmVJbnRlcnZhbFxuICAgIH0pO1xuICAgIFByaXZhdGUuc2F2ZUhhbmRsZXJQcm9wZXJ0eS5zZXQoY29udGV4dCwgaGFuZGxlcik7XG4gICAgdm9pZCBjb250ZXh0LnJlYWR5LnRoZW4oKCkgPT4ge1xuICAgICAgaWYgKHRoaXMuYXV0b3NhdmUpIHtcbiAgICAgICAgaGFuZGxlci5zdGFydCgpO1xuICAgICAgfVxuICAgIH0pO1xuICAgIGNvbnRleHQuZGlzcG9zZWQuY29ubmVjdCh0aGlzLl9vbkNvbnRleHREaXNwb3NlZCwgdGhpcyk7XG4gICAgdGhpcy5fY29udGV4dHMucHVzaChjb250ZXh0KTtcbiAgICByZXR1cm4gY29udGV4dDtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSBjb250ZXh0IGRpc3Bvc2FsLlxuICAgKi9cbiAgcHJpdmF0ZSBfb25Db250ZXh0RGlzcG9zZWQoY29udGV4dDogUHJpdmF0ZS5JQ29udGV4dCk6IHZvaWQge1xuICAgIEFycmF5RXh0LnJlbW92ZUZpcnN0T2YodGhpcy5fY29udGV4dHMsIGNvbnRleHQpO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgd2lkZ2V0IGZhY3RvcnkgZm9yIGEgZ2l2ZW4gd2lkZ2V0IG5hbWUuXG4gICAqL1xuICBwcml2YXRlIF93aWRnZXRGYWN0b3J5Rm9yKFxuICAgIHBhdGg6IHN0cmluZyxcbiAgICB3aWRnZXROYW1lOiBzdHJpbmdcbiAgKTogRG9jdW1lbnRSZWdpc3RyeS5XaWRnZXRGYWN0b3J5IHwgdW5kZWZpbmVkIHtcbiAgICBjb25zdCB7IHJlZ2lzdHJ5IH0gPSB0aGlzO1xuICAgIGlmICh3aWRnZXROYW1lID09PSAnZGVmYXVsdCcpIHtcbiAgICAgIGNvbnN0IGZhY3RvcnkgPSByZWdpc3RyeS5kZWZhdWx0V2lkZ2V0RmFjdG9yeShwYXRoKTtcbiAgICAgIGlmICghZmFjdG9yeSkge1xuICAgICAgICByZXR1cm4gdW5kZWZpbmVkO1xuICAgICAgfVxuICAgICAgd2lkZ2V0TmFtZSA9IGZhY3RvcnkubmFtZTtcbiAgICB9XG4gICAgcmV0dXJuIHJlZ2lzdHJ5LmdldFdpZGdldEZhY3Rvcnkod2lkZ2V0TmFtZSk7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlcyBhIG5ldyBkb2N1bWVudCwgb3IgbG9hZHMgb25lIGZyb20gZGlzaywgZGVwZW5kaW5nIG9uIHRoZSBgd2hpY2hgIGFyZ3VtZW50LlxuICAgKiBJZiBgd2hpY2g9PT0nY3JlYXRlJ2AsIHRoZW4gaXQgY3JlYXRlcyBhIG5ldyBkb2N1bWVudC4gSWYgYHdoaWNoPT09J29wZW4nYCxcbiAgICogdGhlbiBpdCBsb2FkcyB0aGUgZG9jdW1lbnQgZnJvbSBkaXNrLlxuICAgKlxuICAgKiBUaGUgdHdvIGNhc2VzIGRpZmZlciBpbiBob3cgdGhlIGRvY3VtZW50IGNvbnRleHQgaXMgaGFuZGxlZCwgYnV0IHRoZSBjcmVhdGlvblxuICAgKiBvZiB0aGUgd2lkZ2V0IGFuZCBsYXVuY2hpbmcgb2YgdGhlIGtlcm5lbCBhcmUgaWRlbnRpY2FsLlxuICAgKi9cbiAgcHJpdmF0ZSBfY3JlYXRlT3JPcGVuRG9jdW1lbnQoXG4gICAgd2hpY2g6ICdvcGVuJyB8ICdjcmVhdGUnLFxuICAgIHBhdGg6IHN0cmluZyxcbiAgICB3aWRnZXROYW1lID0gJ2RlZmF1bHQnLFxuICAgIGtlcm5lbD86IFBhcnRpYWw8S2VybmVsLklNb2RlbD4sXG4gICAgb3B0aW9ucz86IERvY3VtZW50UmVnaXN0cnkuSU9wZW5PcHRpb25zXG4gICk6IElEb2N1bWVudFdpZGdldCB8IHVuZGVmaW5lZCB7XG4gICAgY29uc3Qgd2lkZ2V0RmFjdG9yeSA9IHRoaXMuX3dpZGdldEZhY3RvcnlGb3IocGF0aCwgd2lkZ2V0TmFtZSk7XG4gICAgaWYgKCF3aWRnZXRGYWN0b3J5KSB7XG4gICAgICByZXR1cm4gdW5kZWZpbmVkO1xuICAgIH1cbiAgICBjb25zdCBtb2RlbE5hbWUgPSB3aWRnZXRGYWN0b3J5Lm1vZGVsTmFtZSB8fCAndGV4dCc7XG4gICAgY29uc3QgZmFjdG9yeSA9IHRoaXMucmVnaXN0cnkuZ2V0TW9kZWxGYWN0b3J5KG1vZGVsTmFtZSk7XG4gICAgaWYgKCFmYWN0b3J5KSB7XG4gICAgICByZXR1cm4gdW5kZWZpbmVkO1xuICAgIH1cblxuICAgIC8vIEhhbmRsZSB0aGUga2VybmVsIHByZWZlcmVuY2UuXG4gICAgY29uc3QgcHJlZmVyZW5jZSA9IHRoaXMucmVnaXN0cnkuZ2V0S2VybmVsUHJlZmVyZW5jZShcbiAgICAgIHBhdGgsXG4gICAgICB3aWRnZXRGYWN0b3J5Lm5hbWUsXG4gICAgICBrZXJuZWxcbiAgICApO1xuXG4gICAgbGV0IGNvbnRleHQ6IFByaXZhdGUuSUNvbnRleHQgfCBudWxsO1xuICAgIGxldCByZWFkeTogUHJvbWlzZTx2b2lkPiA9IFByb21pc2UucmVzb2x2ZSh1bmRlZmluZWQpO1xuXG4gICAgLy8gSGFuZGxlIHRoZSBsb2FkLWZyb20tZGlzayBjYXNlXG4gICAgaWYgKHdoaWNoID09PSAnb3BlbicpIHtcbiAgICAgIC8vIFVzZSBhbiBleGlzdGluZyBjb250ZXh0IGlmIGF2YWlsYWJsZS5cbiAgICAgIGNvbnRleHQgPSB0aGlzLl9maW5kQ29udGV4dChwYXRoLCBmYWN0b3J5Lm5hbWUpIHx8IG51bGw7XG4gICAgICBpZiAoIWNvbnRleHQpIHtcbiAgICAgICAgY29udGV4dCA9IHRoaXMuX2NyZWF0ZUNvbnRleHQocGF0aCwgZmFjdG9yeSwgcHJlZmVyZW5jZSk7XG4gICAgICAgIC8vIFBvcHVsYXRlIHRoZSBtb2RlbCwgZWl0aGVyIGZyb20gZGlzayBvciBhXG4gICAgICAgIC8vIG1vZGVsIGJhY2tlbmQuXG4gICAgICAgIHJlYWR5ID0gdGhpcy5fd2hlbi50aGVuKCgpID0+IGNvbnRleHQhLmluaXRpYWxpemUoZmFsc2UpKTtcbiAgICAgIH1cbiAgICB9IGVsc2UgaWYgKHdoaWNoID09PSAnY3JlYXRlJykge1xuICAgICAgY29udGV4dCA9IHRoaXMuX2NyZWF0ZUNvbnRleHQocGF0aCwgZmFjdG9yeSwgcHJlZmVyZW5jZSk7XG4gICAgICAvLyBJbW1lZGlhdGVseSBzYXZlIHRoZSBjb250ZW50cyB0byBkaXNrLlxuICAgICAgcmVhZHkgPSB0aGlzLl93aGVuLnRoZW4oKCkgPT4gY29udGV4dCEuaW5pdGlhbGl6ZSh0cnVlKSk7XG4gICAgfSBlbHNlIHtcbiAgICAgIHRocm93IG5ldyBFcnJvcihgSW52YWxpZCBhcmd1bWVudCAnd2hpY2gnOiAke3doaWNofWApO1xuICAgIH1cblxuICAgIGNvbnN0IHdpZGdldCA9IHRoaXMuX3dpZGdldE1hbmFnZXIuY3JlYXRlV2lkZ2V0KHdpZGdldEZhY3RvcnksIGNvbnRleHQpO1xuICAgIHRoaXMuX29wZW5lci5vcGVuKHdpZGdldCwgeyB0eXBlOiB3aWRnZXRGYWN0b3J5Lm5hbWUsIC4uLm9wdGlvbnMgfSk7XG5cbiAgICAvLyBJZiB0aGUgaW5pdGlhbCBvcGVuaW5nIG9mIHRoZSBjb250ZXh0IGZhaWxzLCBkaXNwb3NlIG9mIHRoZSB3aWRnZXQuXG4gICAgcmVhZHkuY2F0Y2goZXJyID0+IHtcbiAgICAgIGNvbnNvbGUuZXJyb3IoXG4gICAgICAgIGBGYWlsZWQgdG8gaW5pdGlhbGl6ZSB0aGUgY29udGV4dCB3aXRoICcke2ZhY3RvcnkubmFtZX0nIGZvciAke3BhdGh9YCxcbiAgICAgICAgZXJyXG4gICAgICApO1xuICAgICAgd2lkZ2V0LmNsb3NlKCk7XG4gICAgfSk7XG5cbiAgICByZXR1cm4gd2lkZ2V0O1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBhbiBhY3RpdmF0ZVJlcXVlc3RlZCBzaWduYWwgZnJvbSB0aGUgd2lkZ2V0IG1hbmFnZXIuXG4gICAqL1xuICBwcml2YXRlIF9vbkFjdGl2YXRlUmVxdWVzdGVkKFxuICAgIHNlbmRlcjogRG9jdW1lbnRXaWRnZXRNYW5hZ2VyLFxuICAgIGFyZ3M6IHN0cmluZ1xuICApOiB2b2lkIHtcbiAgICB0aGlzLl9hY3RpdmF0ZVJlcXVlc3RlZC5lbWl0KGFyZ3MpO1xuICB9XG5cbiAgcHJvdGVjdGVkIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yO1xuICBwcml2YXRlIF9hY3RpdmF0ZVJlcXVlc3RlZCA9IG5ldyBTaWduYWw8dGhpcywgc3RyaW5nPih0aGlzKTtcbiAgcHJpdmF0ZSBfY29udGV4dHM6IFByaXZhdGUuSUNvbnRleHRbXSA9IFtdO1xuICBwcml2YXRlIF9vcGVuZXI6IERvY3VtZW50TWFuYWdlci5JV2lkZ2V0T3BlbmVyO1xuICBwcml2YXRlIF93aWRnZXRNYW5hZ2VyOiBEb2N1bWVudFdpZGdldE1hbmFnZXI7XG4gIHByaXZhdGUgX2lzRGlzcG9zZWQgPSBmYWxzZTtcbiAgcHJpdmF0ZSBfYXV0b3NhdmUgPSB0cnVlO1xuICBwcml2YXRlIF9hdXRvc2F2ZUludGVydmFsID0gMTIwO1xuICBwcml2YXRlIF9sYXN0TW9kaWZpZWRDaGVja01hcmdpbiA9IDUwMDtcbiAgcHJpdmF0ZSBfcmVuYW1lVW50aXRsZWRGaWxlT25TYXZlID0gdHJ1ZTtcbiAgcHJpdmF0ZSBfd2hlbjogUHJvbWlzZTx2b2lkPjtcbiAgcHJpdmF0ZSBfc2V0QnVzeTogKCgpID0+IElEaXNwb3NhYmxlKSB8IHVuZGVmaW5lZDtcbiAgcHJpdmF0ZSBfZGlhbG9nczogSVNlc3Npb25Db250ZXh0LklEaWFsb2dzO1xuICBwcml2YXRlIF9kb2NQcm92aWRlckZhY3Rvcnk6IElEb2N1bWVudFByb3ZpZGVyRmFjdG9yeSB8IHVuZGVmaW5lZDtcbiAgcHJpdmF0ZSBfY29sbGFib3JhdGl2ZTogYm9vbGVhbjtcbiAgcHJpdmF0ZSBfaXNDb25uZWN0ZWRDYWxsYmFjazogKCkgPT4gYm9vbGVhbjtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgZG9jdW1lbnQgbWFuYWdlciBzdGF0aWNzLlxuICovXG5leHBvcnQgbmFtZXNwYWNlIERvY3VtZW50TWFuYWdlciB7XG4gIC8qKlxuICAgKiBUaGUgb3B0aW9ucyB1c2VkIHRvIGluaXRpYWxpemUgYSBkb2N1bWVudCBtYW5hZ2VyLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogQSBkb2N1bWVudCByZWdpc3RyeSBpbnN0YW5jZS5cbiAgICAgKi9cbiAgICByZWdpc3RyeTogRG9jdW1lbnRSZWdpc3RyeTtcblxuICAgIC8qKlxuICAgICAqIEEgc2VydmljZSBtYW5hZ2VyIGluc3RhbmNlLlxuICAgICAqL1xuICAgIG1hbmFnZXI6IFNlcnZpY2VNYW5hZ2VyLklNYW5hZ2VyO1xuXG4gICAgLyoqXG4gICAgICogQSB3aWRnZXQgb3BlbmVyIGZvciBzaWJsaW5nIHdpZGdldHMuXG4gICAgICovXG4gICAgb3BlbmVyOiBJV2lkZ2V0T3BlbmVyO1xuXG4gICAgLyoqXG4gICAgICogQSBwcm9taXNlIGZvciB3aGVuIHRvIHN0YXJ0IHVzaW5nIHRoZSBtYW5hZ2VyLlxuICAgICAqL1xuICAgIHdoZW4/OiBQcm9taXNlPHZvaWQ+O1xuXG4gICAgLyoqXG4gICAgICogQSBmdW5jdGlvbiBjYWxsZWQgd2hlbiBhIGtlcm5lbCBpcyBidXN5LlxuICAgICAqL1xuICAgIHNldEJ1c3k/OiAoKSA9PiBJRGlzcG9zYWJsZTtcblxuICAgIC8qKlxuICAgICAqIFRoZSBwcm92aWRlciBmb3Igc2Vzc2lvbiBkaWFsb2dzLlxuICAgICAqL1xuICAgIHNlc3Npb25EaWFsb2dzPzogSVNlc3Npb25Db250ZXh0LklEaWFsb2dzO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGFwcGxpY2F0aW9uIGxhbmd1YWdlIHRyYW5zbGF0b3IuXG4gICAgICovXG4gICAgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yO1xuXG4gICAgLyoqXG4gICAgICogQSBmYWN0b3J5IG1ldGhvZCBmb3IgdGhlIGRvY3VtZW50IHByb3ZpZGVyLlxuICAgICAqL1xuICAgIGRvY1Byb3ZpZGVyRmFjdG9yeT86IElEb2N1bWVudFByb3ZpZGVyRmFjdG9yeTtcblxuICAgIC8qKlxuICAgICAqIFdoZXRoZXIgdGhlIGNvbnRleHQgc2hvdWxkIGJlIGNvbGxhYm9yYXRpdmUuXG4gICAgICogSWYgdHJ1ZSwgdGhlIGNvbnRleHQgd2lsbCBjb25uZWN0IHRocm91Z2ggeWpzX3dzX3NlcnZlciB0byBzaGFyZSBpbmZvcm1hdGlvbiBpZiBwb3NzaWJsZS5cbiAgICAgKi9cbiAgICBjb2xsYWJvcmF0aXZlPzogYm9vbGVhbjtcblxuICAgIC8qKlxuICAgICAqIEF1dG9zYXZpbmcgc2hvdWxkIGJlIHBhdXNlZCB3aGlsZSB0aGlzIGNhbGxiYWNrIGZ1bmN0aW9uIHJldHVybnMgYGZhbHNlYC5cbiAgICAgKiBCeSBkZWZhdWx0LCBpdCBhbHdheXMgcmV0dXJucyBgdHJ1ZWAuXG4gICAgICovXG4gICAgaXNDb25uZWN0ZWRDYWxsYmFjaz86ICgpID0+IGJvb2xlYW47XG4gIH1cblxuICAvKipcbiAgICogQW4gaW50ZXJmYWNlIGZvciBhIHdpZGdldCBvcGVuZXIuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElXaWRnZXRPcGVuZXIge1xuICAgIC8qKlxuICAgICAqIE9wZW4gdGhlIGdpdmVuIHdpZGdldC5cbiAgICAgKi9cbiAgICBvcGVuKFxuICAgICAgd2lkZ2V0OiBJRG9jdW1lbnRXaWRnZXQsXG4gICAgICBvcHRpb25zPzogRG9jdW1lbnRSZWdpc3RyeS5JT3Blbk9wdGlvbnNcbiAgICApOiB2b2lkO1xuICB9XG59XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIHByaXZhdGUgZGF0YS5cbiAqL1xubmFtZXNwYWNlIFByaXZhdGUge1xuICAvKipcbiAgICogQW4gYXR0YWNoZWQgcHJvcGVydHkgZm9yIGEgY29udGV4dCBzYXZlIGhhbmRsZXIuXG4gICAqL1xuICBleHBvcnQgY29uc3Qgc2F2ZUhhbmRsZXJQcm9wZXJ0eSA9IG5ldyBBdHRhY2hlZFByb3BlcnR5PFxuICAgIERvY3VtZW50UmVnaXN0cnkuQ29udGV4dCxcbiAgICBTYXZlSGFuZGxlciB8IHVuZGVmaW5lZFxuICA+KHtcbiAgICBuYW1lOiAnc2F2ZUhhbmRsZXInLFxuICAgIGNyZWF0ZTogKCkgPT4gdW5kZWZpbmVkXG4gIH0pO1xuXG4gIC8qKlxuICAgKiBBIHR5cGUgYWxpYXMgZm9yIGEgc3RhbmRhcmQgY29udGV4dC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBXZSBkZWZpbmUgdGhpcyBhcyBhbiBpbnRlcmZhY2Ugb2YgYSBzcGVjaWZpYyBpbXBsZW1lbnRhdGlvbiBzbyB0aGF0IHdlIGNhblxuICAgKiB1c2UgdGhlIGltcGxlbWVudGF0aW9uLXNwZWNpZmljIGZ1bmN0aW9ucy5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUNvbnRleHQgZXh0ZW5kcyBDb250ZXh0PERvY3VtZW50UmVnaXN0cnkuSU1vZGVsPiB7XG4gICAgLyogbm8gb3AgKi9cbiAgfVxufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBQYXRoRXh0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29yZXV0aWxzJztcbmltcG9ydCB7IERvY3VtZW50UmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9kb2NyZWdpc3RyeSc7XG5pbXBvcnQgeyBUZXh0SXRlbSB9IGZyb20gJ0BqdXB5dGVybGFiL3N0YXR1c2Jhcic7XG5pbXBvcnQgeyBWRG9tTW9kZWwsIFZEb21SZW5kZXJlciB9IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0IHsgVGl0bGUsIFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0IHsgSURvY3VtZW50TWFuYWdlciB9IGZyb20gJy4vdG9rZW5zJztcblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgUGF0aFN0YXR1c0NvbXBvbmVudCBzdGF0aWNzLlxuICovXG5uYW1lc3BhY2UgUGF0aFN0YXR1c0NvbXBvbmVudCB7XG4gIC8qKlxuICAgKiBUaGUgcHJvcHMgZm9yIHJlbmRlcmluZyBhIFBhdGhTdGF0dXNDb21wb25lbnQuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElQcm9wcyB7XG4gICAgLyoqXG4gICAgICogVGhlIGZ1bGwgcGF0aCBmb3IgYSBkb2N1bWVudC5cbiAgICAgKi9cbiAgICBmdWxsUGF0aDogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogVGhlIHNob3J0ZXIgbmFtZSBmb3IgYSBkb2N1bWVudCBvciBhY3Rpdml0eS5cbiAgICAgKi9cbiAgICBuYW1lOiBzdHJpbmc7XG4gIH1cbn1cblxuLyoqXG4gKiBBIHB1cmUgY29tcG9uZW50IGZvciByZW5kZXJpbmcgYSBmaWxlIHBhdGggKG9yIGFjdGl2aXR5IG5hbWUpLlxuICpcbiAqIEBwYXJhbSBwcm9wcyAtIHRoZSBwcm9wcyBmb3IgdGhlIGNvbXBvbmVudC5cbiAqXG4gKiBAcmV0dXJucyBhIHRzeCBjb21wb25lbnQgZm9yIGEgZmlsZSBwYXRoLlxuICovXG5mdW5jdGlvbiBQYXRoU3RhdHVzQ29tcG9uZW50KFxuICBwcm9wczogUGF0aFN0YXR1c0NvbXBvbmVudC5JUHJvcHNcbik6IFJlYWN0LlJlYWN0RWxlbWVudDxQYXRoU3RhdHVzQ29tcG9uZW50LklQcm9wcz4ge1xuICByZXR1cm4gPFRleHRJdGVtIHNvdXJjZT17cHJvcHMubmFtZX0gdGl0bGU9e3Byb3BzLmZ1bGxQYXRofSAvPjtcbn1cblxuLyoqXG4gKiBBIHN0YXR1cyBiYXIgaXRlbSBmb3IgdGhlIGN1cnJlbnQgZmlsZSBwYXRoIChvciBhY3Rpdml0eSBuYW1lKS5cbiAqL1xuZXhwb3J0IGNsYXNzIFBhdGhTdGF0dXMgZXh0ZW5kcyBWRG9tUmVuZGVyZXI8UGF0aFN0YXR1cy5Nb2RlbD4ge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IFBhdGhTdGF0dXMgc3RhdHVzIGl0ZW0uXG4gICAqL1xuICBjb25zdHJ1Y3RvcihvcHRzOiBQYXRoU3RhdHVzLklPcHRpb25zKSB7XG4gICAgc3VwZXIobmV3IFBhdGhTdGF0dXMuTW9kZWwob3B0cy5kb2NNYW5hZ2VyKSk7XG4gICAgdGhpcy5ub2RlLnRpdGxlID0gdGhpcy5tb2RlbC5wYXRoO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlbmRlciB0aGUgc3RhdHVzIGl0ZW0uXG4gICAqL1xuICByZW5kZXIoKTogSlNYLkVsZW1lbnQge1xuICAgIHJldHVybiAoXG4gICAgICA8UGF0aFN0YXR1c0NvbXBvbmVudFxuICAgICAgICBmdWxsUGF0aD17dGhpcy5tb2RlbCEucGF0aH1cbiAgICAgICAgbmFtZT17dGhpcy5tb2RlbCEubmFtZSF9XG4gICAgICAvPlxuICAgICk7XG4gIH1cbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgUGF0aFN0YXR1cyBzdGF0aWNzLlxuICovXG5leHBvcnQgbmFtZXNwYWNlIFBhdGhTdGF0dXMge1xuICAvKipcbiAgICogQSBWRG9tTW9kZWwgZm9yIHJlbmRlcmluZyB0aGUgUGF0aFN0YXR1cyBzdGF0dXMgaXRlbS5cbiAgICovXG4gIGV4cG9ydCBjbGFzcyBNb2RlbCBleHRlbmRzIFZEb21Nb2RlbCB7XG4gICAgLyoqXG4gICAgICogQ29uc3RydWN0IGEgbmV3IG1vZGVsLlxuICAgICAqXG4gICAgICogQHBhcmFtIGRvY01hbmFnZXI6IHRoZSBhcHBsaWNhdGlvbiBkb2N1bWVudCBtYW5hZ2VyLiBVc2VkIHRvIGNoZWNrXG4gICAgICogICB3aGV0aGVyIHRoZSBjdXJyZW50IHdpZGdldCBpcyBhIGRvY3VtZW50LlxuICAgICAqL1xuICAgIGNvbnN0cnVjdG9yKGRvY01hbmFnZXI6IElEb2N1bWVudE1hbmFnZXIpIHtcbiAgICAgIHN1cGVyKCk7XG4gICAgICB0aGlzLl9kb2NNYW5hZ2VyID0gZG9jTWFuYWdlcjtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBUaGUgY3VycmVudCBwYXRoIGZvciB0aGUgYXBwbGljYXRpb24uXG4gICAgICovXG4gICAgZ2V0IHBhdGgoKTogc3RyaW5nIHtcbiAgICAgIHJldHVybiB0aGlzLl9wYXRoO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIFRoZSBuYW1lIG9mIHRoZSBjdXJyZW50IGFjdGl2aXR5LlxuICAgICAqL1xuICAgIGdldCBuYW1lKCk6IHN0cmluZyB7XG4gICAgICByZXR1cm4gdGhpcy5fbmFtZTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBUaGUgY3VycmVudCB3aWRnZXQgZm9yIHRoZSBhcHBsaWNhdGlvbi5cbiAgICAgKi9cbiAgICBnZXQgd2lkZ2V0KCk6IFdpZGdldCB8IG51bGwge1xuICAgICAgcmV0dXJuIHRoaXMuX3dpZGdldDtcbiAgICB9XG4gICAgc2V0IHdpZGdldCh3aWRnZXQ6IFdpZGdldCB8IG51bGwpIHtcbiAgICAgIGNvbnN0IG9sZFdpZGdldCA9IHRoaXMuX3dpZGdldDtcbiAgICAgIGlmIChvbGRXaWRnZXQgIT09IG51bGwpIHtcbiAgICAgICAgY29uc3Qgb2xkQ29udGV4dCA9IHRoaXMuX2RvY01hbmFnZXIuY29udGV4dEZvcldpZGdldChvbGRXaWRnZXQpO1xuICAgICAgICBpZiAob2xkQ29udGV4dCkge1xuICAgICAgICAgIG9sZENvbnRleHQucGF0aENoYW5nZWQuZGlzY29ubmVjdCh0aGlzLl9vblBhdGhDaGFuZ2UpO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIG9sZFdpZGdldC50aXRsZS5jaGFuZ2VkLmRpc2Nvbm5lY3QodGhpcy5fb25UaXRsZUNoYW5nZSk7XG4gICAgICAgIH1cbiAgICAgIH1cblxuICAgICAgY29uc3Qgb2xkU3RhdGUgPSB0aGlzLl9nZXRBbGxTdGF0ZSgpO1xuICAgICAgdGhpcy5fd2lkZ2V0ID0gd2lkZ2V0O1xuICAgICAgaWYgKHRoaXMuX3dpZGdldCA9PT0gbnVsbCkge1xuICAgICAgICB0aGlzLl9wYXRoID0gJyc7XG4gICAgICAgIHRoaXMuX25hbWUgPSAnJztcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIGNvbnN0IHdpZGdldENvbnRleHQgPSB0aGlzLl9kb2NNYW5hZ2VyLmNvbnRleHRGb3JXaWRnZXQodGhpcy5fd2lkZ2V0KTtcbiAgICAgICAgaWYgKHdpZGdldENvbnRleHQpIHtcbiAgICAgICAgICB0aGlzLl9wYXRoID0gd2lkZ2V0Q29udGV4dC5wYXRoO1xuICAgICAgICAgIHRoaXMuX25hbWUgPSBQYXRoRXh0LmJhc2VuYW1lKHdpZGdldENvbnRleHQucGF0aCk7XG5cbiAgICAgICAgICB3aWRnZXRDb250ZXh0LnBhdGhDaGFuZ2VkLmNvbm5lY3QodGhpcy5fb25QYXRoQ2hhbmdlKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICB0aGlzLl9wYXRoID0gJyc7XG4gICAgICAgICAgdGhpcy5fbmFtZSA9IHRoaXMuX3dpZGdldC50aXRsZS5sYWJlbDtcblxuICAgICAgICAgIHRoaXMuX3dpZGdldC50aXRsZS5jaGFuZ2VkLmNvbm5lY3QodGhpcy5fb25UaXRsZUNoYW5nZSk7XG4gICAgICAgIH1cbiAgICAgIH1cblxuICAgICAgdGhpcy5fdHJpZ2dlckNoYW5nZShvbGRTdGF0ZSwgdGhpcy5fZ2V0QWxsU3RhdGUoKSk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogUmVhY3QgdG8gYSB0aXRsZSBjaGFuZ2UgZm9yIHRoZSBjdXJyZW50IHdpZGdldC5cbiAgICAgKi9cbiAgICBwcml2YXRlIF9vblRpdGxlQ2hhbmdlID0gKHRpdGxlOiBUaXRsZTxXaWRnZXQ+KSA9PiB7XG4gICAgICBjb25zdCBvbGRTdGF0ZSA9IHRoaXMuX2dldEFsbFN0YXRlKCk7XG4gICAgICB0aGlzLl9uYW1lID0gdGl0bGUubGFiZWw7XG4gICAgICB0aGlzLl90cmlnZ2VyQ2hhbmdlKG9sZFN0YXRlLCB0aGlzLl9nZXRBbGxTdGF0ZSgpKTtcbiAgICB9O1xuXG4gICAgLyoqXG4gICAgICogUmVhY3QgdG8gYSBwYXRoIGNoYW5nZSBmb3IgdGhlIGN1cnJlbnQgZG9jdW1lbnQuXG4gICAgICovXG4gICAgcHJpdmF0ZSBfb25QYXRoQ2hhbmdlID0gKFxuICAgICAgX2RvY3VtZW50TW9kZWw6IERvY3VtZW50UmVnaXN0cnkuSUNvbnRleHQ8RG9jdW1lbnRSZWdpc3RyeS5JTW9kZWw+LFxuICAgICAgbmV3UGF0aDogc3RyaW5nXG4gICAgKSA9PiB7XG4gICAgICBjb25zdCBvbGRTdGF0ZSA9IHRoaXMuX2dldEFsbFN0YXRlKCk7XG4gICAgICB0aGlzLl9wYXRoID0gbmV3UGF0aDtcbiAgICAgIHRoaXMuX25hbWUgPSBQYXRoRXh0LmJhc2VuYW1lKG5ld1BhdGgpO1xuXG4gICAgICB0aGlzLl90cmlnZ2VyQ2hhbmdlKG9sZFN0YXRlLCB0aGlzLl9nZXRBbGxTdGF0ZSgpKTtcbiAgICB9O1xuXG4gICAgLyoqXG4gICAgICogR2V0IHRoZSBjdXJyZW50IHN0YXRlIG9mIHRoZSBtb2RlbC5cbiAgICAgKi9cbiAgICBwcml2YXRlIF9nZXRBbGxTdGF0ZSgpOiBbc3RyaW5nLCBzdHJpbmddIHtcbiAgICAgIHJldHVybiBbdGhpcy5fcGF0aCwgdGhpcy5fbmFtZV07XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogVHJpZ2dlciBhIHN0YXRlIGNoYW5nZSB0byByZXJlbmRlci5cbiAgICAgKi9cbiAgICBwcml2YXRlIF90cmlnZ2VyQ2hhbmdlKFxuICAgICAgb2xkU3RhdGU6IFtzdHJpbmcsIHN0cmluZ10sXG4gICAgICBuZXdTdGF0ZTogW3N0cmluZywgc3RyaW5nXVxuICAgICkge1xuICAgICAgaWYgKG9sZFN0YXRlWzBdICE9PSBuZXdTdGF0ZVswXSB8fCBvbGRTdGF0ZVsxXSAhPT0gbmV3U3RhdGVbMV0pIHtcbiAgICAgICAgdGhpcy5zdGF0ZUNoYW5nZWQuZW1pdCh2b2lkIDApO1xuICAgICAgfVxuICAgIH1cblxuICAgIHByaXZhdGUgX3BhdGg6IHN0cmluZyA9ICcnO1xuICAgIHByaXZhdGUgX25hbWU6IHN0cmluZyA9ICcnO1xuICAgIHByaXZhdGUgX3dpZGdldDogV2lkZ2V0IHwgbnVsbCA9IG51bGw7XG4gICAgcHJpdmF0ZSBfZG9jTWFuYWdlcjogSURvY3VtZW50TWFuYWdlcjtcbiAgfVxuXG4gIC8qKlxuICAgKiBPcHRpb25zIGZvciBjcmVhdGluZyB0aGUgUGF0aFN0YXR1cyB3aWRnZXQuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElPcHRpb25zIHtcbiAgICAvKipcbiAgICAgKiBUaGUgYXBwbGljYXRpb24gZG9jdW1lbnQgbWFuYWdlci5cbiAgICAgKi9cbiAgICBkb2NNYW5hZ2VyOiBJRG9jdW1lbnRNYW5hZ2VyO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IERvY3VtZW50UmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9kb2NyZWdpc3RyeSc7XG5pbXBvcnQgeyBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5cbi8qKlxuICogQSBjbGFzcyB0aGF0IG1hbmFnZXMgdGhlIGF1dG8gc2F2aW5nIG9mIGEgZG9jdW1lbnQuXG4gKlxuICogIyMjIyBOb3Rlc1xuICogSW1wbGVtZW50cyBodHRwczovL2dpdGh1Yi5jb20vaXB5dGhvbi9pcHl0aG9uL3dpa2kvSVBFUC0xNTotQXV0b3NhdmluZy10aGUtSVB5dGhvbi1Ob3RlYm9vay5cbiAqL1xuZXhwb3J0IGNsYXNzIFNhdmVIYW5kbGVyIGltcGxlbWVudHMgSURpc3Bvc2FibGUge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IHNhdmUgaGFuZGxlci5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IFNhdmVIYW5kbGVyLklPcHRpb25zKSB7XG4gICAgdGhpcy5fY29udGV4dCA9IG9wdGlvbnMuY29udGV4dDtcbiAgICB0aGlzLl9pc0Nvbm5lY3RlZENhbGxiYWNrID0gb3B0aW9ucy5pc0Nvbm5lY3RlZENhbGxiYWNrIHx8ICgoKSA9PiB0cnVlKTtcbiAgICBjb25zdCBpbnRlcnZhbCA9IG9wdGlvbnMuc2F2ZUludGVydmFsIHx8IDEyMDtcbiAgICB0aGlzLl9taW5JbnRlcnZhbCA9IGludGVydmFsICogMTAwMDtcbiAgICB0aGlzLl9pbnRlcnZhbCA9IHRoaXMuX21pbkludGVydmFsO1xuICAgIC8vIFJlc3RhcnQgdGhlIHRpbWVyIHdoZW4gdGhlIGNvbnRlbnRzIG1vZGVsIGlzIHVwZGF0ZWQuXG4gICAgdGhpcy5fY29udGV4dC5maWxlQ2hhbmdlZC5jb25uZWN0KHRoaXMuX3NldFRpbWVyLCB0aGlzKTtcbiAgICB0aGlzLl9jb250ZXh0LmRpc3Bvc2VkLmNvbm5lY3QodGhpcy5kaXNwb3NlLCB0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgc2F2ZSBpbnRlcnZhbCB1c2VkIGJ5IHRoZSB0aW1lciAoaW4gc2Vjb25kcykuXG4gICAqL1xuICBnZXQgc2F2ZUludGVydmFsKCk6IG51bWJlciB7XG4gICAgcmV0dXJuIHRoaXMuX2ludGVydmFsIC8gMTAwMDtcbiAgfVxuICBzZXQgc2F2ZUludGVydmFsKHZhbHVlOiBudW1iZXIpIHtcbiAgICB0aGlzLl9taW5JbnRlcnZhbCA9IHRoaXMuX2ludGVydmFsID0gdmFsdWUgKiAxMDAwO1xuICAgIGlmICh0aGlzLl9pc0FjdGl2ZSkge1xuICAgICAgdGhpcy5fc2V0VGltZXIoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogR2V0IHdoZXRoZXIgdGhlIGhhbmRsZXIgaXMgYWN0aXZlLlxuICAgKi9cbiAgZ2V0IGlzQWN0aXZlKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiB0aGlzLl9pc0FjdGl2ZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgd2hldGhlciB0aGUgc2F2ZSBoYW5kbGVyIGlzIGRpc3Bvc2VkLlxuICAgKi9cbiAgZ2V0IGlzRGlzcG9zZWQoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuX2lzRGlzcG9zZWQ7XG4gIH1cblxuICAvKipcbiAgICogRGlzcG9zZSBvZiB0aGUgcmVzb3VyY2VzIHVzZWQgYnkgdGhlIHNhdmUgaGFuZGxlci5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICB0aGlzLl9pc0Rpc3Bvc2VkID0gdHJ1ZTtcbiAgICBjbGVhclRpbWVvdXQodGhpcy5fYXV0b3NhdmVUaW1lcik7XG4gICAgU2lnbmFsLmNsZWFyRGF0YSh0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTdGFydCB0aGUgYXV0b3NhdmVyLlxuICAgKi9cbiAgc3RhcnQoKTogdm9pZCB7XG4gICAgdGhpcy5faXNBY3RpdmUgPSB0cnVlO1xuICAgIHRoaXMuX3NldFRpbWVyKCk7XG4gIH1cblxuICAvKipcbiAgICogU3RvcCB0aGUgYXV0b3NhdmVyLlxuICAgKi9cbiAgc3RvcCgpOiB2b2lkIHtcbiAgICB0aGlzLl9pc0FjdGl2ZSA9IGZhbHNlO1xuICAgIGNsZWFyVGltZW91dCh0aGlzLl9hdXRvc2F2ZVRpbWVyKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZXQgdGhlIHRpbWVyLlxuICAgKi9cbiAgcHJpdmF0ZSBfc2V0VGltZXIoKTogdm9pZCB7XG4gICAgY2xlYXJUaW1lb3V0KHRoaXMuX2F1dG9zYXZlVGltZXIpO1xuICAgIGlmICghdGhpcy5faXNBY3RpdmUpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgdGhpcy5fYXV0b3NhdmVUaW1lciA9IHdpbmRvdy5zZXRUaW1lb3V0KCgpID0+IHtcbiAgICAgIGlmICh0aGlzLl9pc0Nvbm5lY3RlZENhbGxiYWNrKCkpIHtcbiAgICAgICAgdGhpcy5fc2F2ZSgpO1xuICAgICAgfVxuICAgIH0sIHRoaXMuX2ludGVydmFsKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYW4gYXV0b3NhdmUgdGltZW91dC5cbiAgICovXG4gIHByaXZhdGUgX3NhdmUoKTogdm9pZCB7XG4gICAgY29uc3QgY29udGV4dCA9IHRoaXMuX2NvbnRleHQ7XG5cbiAgICAvLyBUcmlnZ2VyIHRoZSBuZXh0IHVwZGF0ZS5cbiAgICB0aGlzLl9zZXRUaW1lcigpO1xuXG4gICAgaWYgKCFjb250ZXh0KSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgLy8gQmFpbCBpZiB0aGUgbW9kZWwgaXMgbm90IGRpcnR5IG9yIHRoZSBmaWxlIGlzIG5vdCB3cml0YWJsZSwgb3IgdGhlIGRpYWxvZ1xuICAgIC8vIGlzIGFscmVhZHkgc2hvd2luZy5cbiAgICBjb25zdCB3cml0YWJsZSA9IGNvbnRleHQuY29udGVudHNNb2RlbCAmJiBjb250ZXh0LmNvbnRlbnRzTW9kZWwud3JpdGFibGU7XG4gICAgaWYgKCF3cml0YWJsZSB8fCAhY29udGV4dC5tb2RlbC5kaXJ0eSB8fCB0aGlzLl9pbkRpYWxvZykge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIGNvbnN0IHN0YXJ0ID0gbmV3IERhdGUoKS5nZXRUaW1lKCk7XG4gICAgY29udGV4dFxuICAgICAgLnNhdmUoKVxuICAgICAgLnRoZW4oKCkgPT4ge1xuICAgICAgICBpZiAodGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IGR1cmF0aW9uID0gbmV3IERhdGUoKS5nZXRUaW1lKCkgLSBzdGFydDtcbiAgICAgICAgLy8gTmV3IHNhdmUgaW50ZXJ2YWw6IGhpZ2hlciBvZiAxMHggc2F2ZSBkdXJhdGlvbiBvciBtaW4gaW50ZXJ2YWwuXG4gICAgICAgIHRoaXMuX2ludGVydmFsID0gTWF0aC5tYXgoXG4gICAgICAgICAgdGhpcy5fbXVsdGlwbGllciAqIGR1cmF0aW9uLFxuICAgICAgICAgIHRoaXMuX21pbkludGVydmFsXG4gICAgICAgICk7XG4gICAgICAgIC8vIFJlc3RhcnQgdGhlIHVwZGF0ZSB0byBwaWNrIHVwIHRoZSBuZXcgaW50ZXJ2YWwuXG4gICAgICAgIHRoaXMuX3NldFRpbWVyKCk7XG4gICAgICB9KVxuICAgICAgLmNhdGNoKGVyciA9PiB7XG4gICAgICAgIC8vIElmIHRoZSB1c2VyIGNhbmNlbGVkIHRoZSBzYXZlLCBkbyBub3RoaW5nLlxuICAgICAgICBjb25zdCB7IG5hbWUgfSA9IGVycjtcbiAgICAgICAgaWYgKG5hbWUgPT09ICdNb2RhbENhbmNlbEVycm9yJyB8fCBuYW1lID09PSAnTW9kYWxEdXBsaWNhdGVFcnJvcicpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cbiAgICAgICAgLy8gT3RoZXJ3aXNlLCBsb2cgdGhlIGVycm9yLlxuICAgICAgICBjb25zb2xlLmVycm9yKCdFcnJvciBpbiBBdXRvLVNhdmUnLCBlcnIubWVzc2FnZSk7XG4gICAgICB9KTtcbiAgfVxuXG4gIHByaXZhdGUgX2F1dG9zYXZlVGltZXIgPSAtMTtcbiAgcHJpdmF0ZSBfbWluSW50ZXJ2YWwgPSAtMTtcbiAgcHJpdmF0ZSBfaW50ZXJ2YWwgPSAtMTtcbiAgcHJpdmF0ZSBfY29udGV4dDogRG9jdW1lbnRSZWdpc3RyeS5Db250ZXh0O1xuICBwcml2YXRlIF9pc0Nvbm5lY3RlZENhbGxiYWNrOiAoKSA9PiBib29sZWFuO1xuICBwcml2YXRlIF9pc0FjdGl2ZSA9IGZhbHNlO1xuICBwcml2YXRlIF9pbkRpYWxvZyA9IGZhbHNlO1xuICBwcml2YXRlIF9pc0Rpc3Bvc2VkID0gZmFsc2U7XG4gIHByaXZhdGUgX211bHRpcGxpZXIgPSAxMDtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgYFNhdmVIYW5kbGVyYCBzdGF0aWNzLlxuICovXG5leHBvcnQgbmFtZXNwYWNlIFNhdmVIYW5kbGVyIHtcbiAgLyoqXG4gICAqIFRoZSBvcHRpb25zIHVzZWQgdG8gY3JlYXRlIGEgc2F2ZSBoYW5kbGVyLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIGNvbnRleHQgYXNzb2NpYXRlZCB3aXRoIHRoZSBmaWxlLlxuICAgICAqL1xuICAgIGNvbnRleHQ6IERvY3VtZW50UmVnaXN0cnkuQ29udGV4dDtcblxuICAgIC8qKlxuICAgICAqIEF1dG9zYXZpbmcgc2hvdWxkIGJlIHBhdXNlZCB3aGlsZSB0aGlzIGNhbGxiYWNrIGZ1bmN0aW9uIHJldHVybnMgYGZhbHNlYC5cbiAgICAgKiBCeSBkZWZhdWx0LCBpdCBhbHdheXMgcmV0dXJucyBgdHJ1ZWAuXG4gICAgICovXG4gICAgaXNDb25uZWN0ZWRDYWxsYmFjaz86ICgpID0+IGJvb2xlYW47XG5cbiAgICAvKipcbiAgICAgKiBUaGUgbWluaW11bSBzYXZlIGludGVydmFsIGluIHNlY29uZHMgKGRlZmF1bHQgaXMgdHdvIG1pbnV0ZXMpLlxuICAgICAqL1xuICAgIHNhdmVJbnRlcnZhbD86IG51bWJlcjtcbiAgfVxufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBEb2N1bWVudFJlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jcmVnaXN0cnknO1xuaW1wb3J0IHsgVGV4dEl0ZW0gfSBmcm9tICdAanVweXRlcmxhYi9zdGF0dXNiYXInO1xuaW1wb3J0IHsgSVRyYW5zbGF0b3IsIG51bGxUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgVkRvbU1vZGVsLCBWRG9tUmVuZGVyZXIgfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0IHsgSURvY3VtZW50TWFuYWdlciB9IGZyb20gJy4vdG9rZW5zJztcblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgU2F2aW5nU3RhdHVzQ29tcG9uZW50IHN0YXRpY3MuXG4gKi9cbm5hbWVzcGFjZSBTYXZpbmdTdGF0dXNDb21wb25lbnQge1xuICAvKipcbiAgICogVGhlIHByb3BzIGZvciB0aGUgU2F2aW5nU3RhdHVzQ29tcG9uZW50LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJUHJvcHMge1xuICAgIC8qKlxuICAgICAqIFRoZSBjdXJyZW50IHNhdmluZyBzdGF0dXMsIGFmdGVyIHRyYW5zbGF0aW9uLlxuICAgICAqL1xuICAgIGZpbGVTdGF0dXM6IHN0cmluZztcbiAgfVxufVxuXG4vKipcbiAqIEEgcHVyZSBmdW5jdGlvbmFsIGNvbXBvbmVudCBmb3IgYSBTYXZpbmcgc3RhdHVzIGl0ZW0uXG4gKlxuICogQHBhcmFtIHByb3BzIC0gdGhlIHByb3BzIGZvciB0aGUgY29tcG9uZW50LlxuICpcbiAqIEByZXR1cm5zIGEgdHN4IGNvbXBvbmVudCBmb3IgcmVuZGVyaW5nIHRoZSBzYXZpbmcgc3RhdGUuXG4gKi9cbmZ1bmN0aW9uIFNhdmluZ1N0YXR1c0NvbXBvbmVudChcbiAgcHJvcHM6IFNhdmluZ1N0YXR1c0NvbXBvbmVudC5JUHJvcHNcbik6IFJlYWN0LlJlYWN0RWxlbWVudDxTYXZpbmdTdGF0dXNDb21wb25lbnQuSVByb3BzPiB7XG4gIHJldHVybiA8VGV4dEl0ZW0gc291cmNlPXtwcm9wcy5maWxlU3RhdHVzfSAvPjtcbn1cblxuLyoqXG4gKiBUaGUgYW1vdW50IG9mIHRpbWUgKGluIG1zKSB0byByZXRhaW4gdGhlIHNhdmluZyBjb21wbGV0ZWQgbWVzc2FnZVxuICogYmVmb3JlIGhpZGluZyB0aGUgc3RhdHVzIGl0ZW0uXG4gKi9cbmNvbnN0IFNBVklOR19DT01QTEVURV9NRVNTQUdFX01JTExJUyA9IDIwMDA7XG5cbi8qKlxuICogQSBWRG9tUmVuZGVyZXIgZm9yIGEgc2F2aW5nIHN0YXR1cyBpdGVtLlxuICovXG5leHBvcnQgY2xhc3MgU2F2aW5nU3RhdHVzIGV4dGVuZHMgVkRvbVJlbmRlcmVyPFNhdmluZ1N0YXR1cy5Nb2RlbD4ge1xuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IFNhdmluZ1N0YXR1cyBpdGVtLlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0czogU2F2aW5nU3RhdHVzLklPcHRpb25zKSB7XG4gICAgc3VwZXIobmV3IFNhdmluZ1N0YXR1cy5Nb2RlbChvcHRzLmRvY01hbmFnZXIpKTtcbiAgICBjb25zdCB0cmFuc2xhdG9yID0gb3B0cy50cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgdGhpcy5fc3RhdHVzTWFwID0ge1xuICAgICAgY29tcGxldGVkOiB0cmFucy5fXygnU2F2aW5nIGNvbXBsZXRlZCcpLFxuICAgICAgc3RhcnRlZDogdHJhbnMuX18oJ1NhdmluZyBzdGFydGVkJyksXG4gICAgICBmYWlsZWQ6IHRyYW5zLl9fKCdTYXZpbmcgZmFpbGVkJylcbiAgICB9O1xuICB9XG5cbiAgLyoqXG4gICAqIFJlbmRlciB0aGUgU2F2aW5nU3RhdHVzIGl0ZW0uXG4gICAqL1xuICByZW5kZXIoKTogSlNYLkVsZW1lbnQgfCBudWxsIHtcbiAgICBpZiAodGhpcy5tb2RlbCA9PT0gbnVsbCB8fCB0aGlzLm1vZGVsLnN0YXR1cyA9PT0gbnVsbCkge1xuICAgICAgcmV0dXJuIG51bGw7XG4gICAgfSBlbHNlIHtcbiAgICAgIHJldHVybiAoXG4gICAgICAgIDxTYXZpbmdTdGF0dXNDb21wb25lbnRcbiAgICAgICAgICBmaWxlU3RhdHVzPXt0aGlzLl9zdGF0dXNNYXBbdGhpcy5tb2RlbC5zdGF0dXNdfVxuICAgICAgICAvPlxuICAgICAgKTtcbiAgICB9XG4gIH1cblxuICBwcml2YXRlIF9zdGF0dXNNYXA6IFJlY29yZDxEb2N1bWVudFJlZ2lzdHJ5LlNhdmVTdGF0ZSwgc3RyaW5nPjtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgU2F2aW5nU3RhdHVzIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgU2F2aW5nU3RhdHVzIHtcbiAgLyoqXG4gICAqIEEgVkRvbU1vZGVsIGZvciB0aGUgU2F2aW5nU3RhdHVzIGl0ZW0uXG4gICAqL1xuICBleHBvcnQgY2xhc3MgTW9kZWwgZXh0ZW5kcyBWRG9tTW9kZWwge1xuICAgIC8qKlxuICAgICAqIENyZWF0ZSBhIG5ldyBTYXZpbmdTdGF0dXMgbW9kZWwuXG4gICAgICovXG4gICAgY29uc3RydWN0b3IoZG9jTWFuYWdlcjogSURvY3VtZW50TWFuYWdlcikge1xuICAgICAgc3VwZXIoKTtcblxuICAgICAgdGhpcy5fc3RhdHVzID0gbnVsbDtcbiAgICAgIHRoaXMud2lkZ2V0ID0gbnVsbDtcbiAgICAgIHRoaXMuX2RvY01hbmFnZXIgPSBkb2NNYW5hZ2VyO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIFRoZSBjdXJyZW50IHN0YXR1cyBvZiB0aGUgbW9kZWwuXG4gICAgICovXG4gICAgZ2V0IHN0YXR1cygpOiBEb2N1bWVudFJlZ2lzdHJ5LlNhdmVTdGF0ZSB8IG51bGwge1xuICAgICAgcmV0dXJuIHRoaXMuX3N0YXR1cyE7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogVGhlIGN1cnJlbnQgd2lkZ2V0IGZvciB0aGUgbW9kZWwuIEFueSB3aWRnZXQgY2FuIGJlIGFzc2lnbmVkLFxuICAgICAqIGJ1dCBpdCBvbmx5IGhhcyBhbnkgZWZmZWN0IGlmIHRoZSB3aWRnZXQgaXMgYW4gSURvY3VtZW50IHdpZGdldFxuICAgICAqIGtub3duIHRvIHRoZSBhcHBsaWNhdGlvbiBkb2N1bWVudCBtYW5hZ2VyLlxuICAgICAqL1xuICAgIGdldCB3aWRnZXQoKTogV2lkZ2V0IHwgbnVsbCB7XG4gICAgICByZXR1cm4gdGhpcy5fd2lkZ2V0O1xuICAgIH1cbiAgICBzZXQgd2lkZ2V0KHdpZGdldDogV2lkZ2V0IHwgbnVsbCkge1xuICAgICAgY29uc3Qgb2xkV2lkZ2V0ID0gdGhpcy5fd2lkZ2V0O1xuICAgICAgaWYgKG9sZFdpZGdldCAhPT0gbnVsbCkge1xuICAgICAgICBjb25zdCBvbGRDb250ZXh0ID0gdGhpcy5fZG9jTWFuYWdlci5jb250ZXh0Rm9yV2lkZ2V0KG9sZFdpZGdldCk7XG4gICAgICAgIGlmIChvbGRDb250ZXh0KSB7XG4gICAgICAgICAgb2xkQ29udGV4dC5zYXZlU3RhdGUuZGlzY29ubmVjdCh0aGlzLl9vblN0YXR1c0NoYW5nZSk7XG4gICAgICAgIH0gZWxzZSBpZiAoKHRoaXMuX3dpZGdldCBhcyBhbnkpLmNvbnRlbnQ/LnNhdmVTdGF0ZUNoYW5nZWQpIHtcbiAgICAgICAgICAodGhpcy5fd2lkZ2V0IGFzIGFueSkuY29udGVudC5zYXZlU3RhdGVDaGFuZ2VkLmRpc2Nvbm5lY3QoXG4gICAgICAgICAgICB0aGlzLl9vblN0YXR1c0NoYW5nZVxuICAgICAgICAgICk7XG4gICAgICAgIH1cbiAgICAgIH1cblxuICAgICAgdGhpcy5fd2lkZ2V0ID0gd2lkZ2V0O1xuICAgICAgaWYgKHRoaXMuX3dpZGdldCA9PT0gbnVsbCkge1xuICAgICAgICB0aGlzLl9zdGF0dXMgPSBudWxsO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0Q29udGV4dCA9IHRoaXMuX2RvY01hbmFnZXIuY29udGV4dEZvcldpZGdldCh0aGlzLl93aWRnZXQpO1xuICAgICAgICBpZiAod2lkZ2V0Q29udGV4dCkge1xuICAgICAgICAgIHdpZGdldENvbnRleHQuc2F2ZVN0YXRlLmNvbm5lY3QodGhpcy5fb25TdGF0dXNDaGFuZ2UpO1xuICAgICAgICB9IGVsc2UgaWYgKCh0aGlzLl93aWRnZXQgYXMgYW55KS5jb250ZW50Py5zYXZlU3RhdGVDaGFuZ2VkKSB7XG4gICAgICAgICAgKHRoaXMuX3dpZGdldCBhcyBhbnkpLmNvbnRlbnQuc2F2ZVN0YXRlQ2hhbmdlZC5jb25uZWN0KFxuICAgICAgICAgICAgdGhpcy5fb25TdGF0dXNDaGFuZ2VcbiAgICAgICAgICApO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogUmVhY3QgdG8gYSBzYXZpbmcgc3RhdHVzIGNoYW5nZSBmcm9tIHRoZSBjdXJyZW50IGRvY3VtZW50IHdpZGdldC5cbiAgICAgKi9cbiAgICBwcml2YXRlIF9vblN0YXR1c0NoYW5nZSA9IChcbiAgICAgIF86IGFueSxcbiAgICAgIG5ld1N0YXR1czogRG9jdW1lbnRSZWdpc3RyeS5TYXZlU3RhdGVcbiAgICApID0+IHtcbiAgICAgIHRoaXMuX3N0YXR1cyA9IG5ld1N0YXR1cztcblxuICAgICAgaWYgKHRoaXMuX3N0YXR1cyA9PT0gJ2NvbXBsZXRlZCcpIHtcbiAgICAgICAgc2V0VGltZW91dCgoKSA9PiB7XG4gICAgICAgICAgdGhpcy5fc3RhdHVzID0gbnVsbDtcbiAgICAgICAgICB0aGlzLnN0YXRlQ2hhbmdlZC5lbWl0KHZvaWQgMCk7XG4gICAgICAgIH0sIFNBVklOR19DT01QTEVURV9NRVNTQUdFX01JTExJUyk7XG4gICAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQodm9pZCAwKTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQodm9pZCAwKTtcbiAgICAgIH1cbiAgICB9O1xuXG4gICAgcHJpdmF0ZSBfc3RhdHVzOiBEb2N1bWVudFJlZ2lzdHJ5LlNhdmVTdGF0ZSB8IG51bGwgPSBudWxsO1xuICAgIHByaXZhdGUgX3dpZGdldDogV2lkZ2V0IHwgbnVsbCA9IG51bGw7XG4gICAgcHJpdmF0ZSBfZG9jTWFuYWdlcjogSURvY3VtZW50TWFuYWdlcjtcbiAgfVxuXG4gIC8qKlxuICAgKiBPcHRpb25zIGZvciBjcmVhdGluZyBhIG5ldyBTYXZlU3RhdHVzIGl0ZW1cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMge1xuICAgIC8qKlxuICAgICAqIFRoZSBhcHBsaWNhdGlvbiBkb2N1bWVudCBtYW5hZ2VyLlxuICAgICAqL1xuICAgIGRvY01hbmFnZXI6IElEb2N1bWVudE1hbmFnZXI7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgYXBwbGljYXRpb24gbGFuZ3VhZ2UgdHJhbnNsYXRvci5cbiAgICAgKi9cbiAgICB0cmFuc2xhdG9yPzogSVRyYW5zbGF0b3I7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgRG9jdW1lbnRSZWdpc3RyeSwgSURvY3VtZW50V2lkZ2V0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jcmVnaXN0cnknO1xuaW1wb3J0IHsgQ29udGVudHMsIEtlcm5lbCwgU2VydmljZU1hbmFnZXIgfSBmcm9tICdAanVweXRlcmxhYi9zZXJ2aWNlcyc7XG5pbXBvcnQgeyBUb2tlbiB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IElEaXNwb3NhYmxlIH0gZnJvbSAnQGx1bWluby9kaXNwb3NhYmxlJztcbmltcG9ydCB7IElTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuXG4vKipcbiAqIFRoZSBkb2N1bWVudCByZWdpc3RyeSB0b2tlbi5cbiAqL1xuZXhwb3J0IGNvbnN0IElEb2N1bWVudE1hbmFnZXIgPSBuZXcgVG9rZW48SURvY3VtZW50TWFuYWdlcj4oXG4gICdAanVweXRlcmxhYi9kb2NtYW5hZ2VyOklEb2N1bWVudE1hbmFnZXInXG4pO1xuXG4vKipcbiAqIFRoZSBpbnRlcmZhY2UgZm9yIGEgZG9jdW1lbnQgbWFuYWdlci5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJRG9jdW1lbnRNYW5hZ2VyIGV4dGVuZHMgSURpc3Bvc2FibGUge1xuICAvKipcbiAgICogVGhlIHJlZ2lzdHJ5IHVzZWQgYnkgdGhlIG1hbmFnZXIuXG4gICAqL1xuICByZWFkb25seSByZWdpc3RyeTogRG9jdW1lbnRSZWdpc3RyeTtcblxuICAvKipcbiAgICogVGhlIHNlcnZpY2UgbWFuYWdlciB1c2VkIGJ5IHRoZSBtYW5hZ2VyLlxuICAgKi9cbiAgcmVhZG9ubHkgc2VydmljZXM6IFNlcnZpY2VNYW5hZ2VyLklNYW5hZ2VyO1xuXG4gIC8qKlxuICAgKiBBIHNpZ25hbCBlbWl0dGVkIHdoZW4gb25lIG9mIHRoZSBkb2N1bWVudHMgaXMgYWN0aXZhdGVkLlxuICAgKi9cbiAgcmVhZG9ubHkgYWN0aXZhdGVSZXF1ZXN0ZWQ6IElTaWduYWw8dGhpcywgc3RyaW5nPjtcblxuICAvKipcbiAgICogV2hldGhlciB0byBhdXRvc2F2ZSBkb2N1bWVudHMuXG4gICAqL1xuICBhdXRvc2F2ZTogYm9vbGVhbjtcblxuICAvKipcbiAgICogRGV0ZXJtaW5lcyB0aGUgdGltZSBpbnRlcnZhbCBmb3IgYXV0b3NhdmUgaW4gc2Vjb25kcy5cbiAgICovXG4gIGF1dG9zYXZlSW50ZXJ2YWw6IG51bWJlcjtcblxuICAvKipcbiAgICogRGVmaW5lcyBtYXggYWNjZXB0YWJsZSBkaWZmZXJlbmNlLCBpbiBtaWxsaXNlY29uZHMsIGJldHdlZW4gbGFzdCBtb2RpZmllZCB0aW1lc3RhbXBzIG9uIGRpc2sgYW5kIGNsaWVudC5cbiAgICovXG4gIGxhc3RNb2RpZmllZENoZWNrTWFyZ2luOiBudW1iZXI7XG5cbiAgLyoqXG4gICAqIFdoZXRoZXIgdG8gYXNrIHRoZSB1c2VyIHRvIHJlbmFtZSB1bnRpdGxlZCBmaWxlIG9uIGZpcnN0IG1hbnVhbCBzYXZlLlxuICAgKi9cbiAgcmVuYW1lVW50aXRsZWRGaWxlT25TYXZlOiBib29sZWFuO1xuXG4gIC8qKlxuICAgKiBDbG9uZSBhIHdpZGdldC5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldCAtIFRoZSBzb3VyY2Ugd2lkZ2V0LlxuICAgKlxuICAgKiBAcmV0dXJucyBBIG5ldyB3aWRnZXQgb3IgYHVuZGVmaW5lZGAuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogIFVzZXMgdGhlIHNhbWUgd2lkZ2V0IGZhY3RvcnkgYW5kIGNvbnRleHQgYXMgdGhlIHNvdXJjZSwgb3IgcmV0dXJuc1xuICAgKiAgYHVuZGVmaW5lZGAgaWYgdGhlIHNvdXJjZSB3aWRnZXQgaXMgbm90IG1hbmFnZWQgYnkgdGhpcyBtYW5hZ2VyLlxuICAgKi9cbiAgY2xvbmVXaWRnZXQod2lkZ2V0OiBXaWRnZXQpOiBJRG9jdW1lbnRXaWRnZXQgfCB1bmRlZmluZWQ7XG5cbiAgLyoqXG4gICAqIENsb3NlIGFsbCBvZiB0aGUgb3BlbiBkb2N1bWVudHMuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSByZXNvbHZpbmcgd2hlbiB0aGUgd2lkZ2V0cyBhcmUgY2xvc2VkLlxuICAgKi9cbiAgY2xvc2VBbGwoKTogUHJvbWlzZTx2b2lkPjtcblxuICAvKipcbiAgICogQ2xvc2UgdGhlIHdpZGdldHMgYXNzb2NpYXRlZCB3aXRoIGEgZ2l2ZW4gcGF0aC5cbiAgICpcbiAgICogQHBhcmFtIHBhdGggLSBUaGUgdGFyZ2V0IHBhdGguXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSByZXNvbHZpbmcgd2hlbiB0aGUgd2lkZ2V0cyBhcmUgY2xvc2VkLlxuICAgKi9cbiAgY2xvc2VGaWxlKHBhdGg6IHN0cmluZyk6IFByb21pc2U8dm9pZD47XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgZG9jdW1lbnQgY29udGV4dCBmb3IgYSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgLSBUaGUgd2lkZ2V0IG9mIGludGVyZXN0LlxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgY29udGV4dCBhc3NvY2lhdGVkIHdpdGggdGhlIHdpZGdldCwgb3IgYHVuZGVmaW5lZGAgaWYgbm8gc3VjaFxuICAgKiBjb250ZXh0IGV4aXN0cy5cbiAgICovXG4gIGNvbnRleHRGb3JXaWRnZXQod2lkZ2V0OiBXaWRnZXQpOiBEb2N1bWVudFJlZ2lzdHJ5LkNvbnRleHQgfCB1bmRlZmluZWQ7XG5cbiAgLyoqXG4gICAqIENvcHkgYSBmaWxlLlxuICAgKlxuICAgKiBAcGFyYW0gZnJvbUZpbGUgLSBUaGUgZnVsbCBwYXRoIG9mIHRoZSBvcmlnaW5hbCBmaWxlLlxuICAgKlxuICAgKiBAcGFyYW0gdG9EaXIgLSBUaGUgZnVsbCBwYXRoIHRvIHRoZSB0YXJnZXQgZGlyZWN0b3J5LlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2Ugd2hpY2ggcmVzb2x2ZXMgdG8gdGhlIGNvbnRlbnRzIG9mIHRoZSBmaWxlLlxuICAgKi9cbiAgY29weShmcm9tRmlsZTogc3RyaW5nLCB0b0Rpcjogc3RyaW5nKTogUHJvbWlzZTxDb250ZW50cy5JTW9kZWw+O1xuXG4gIC8qKlxuICAgKiBDcmVhdGUgYSBuZXcgZmlsZSBhbmQgcmV0dXJuIHRoZSB3aWRnZXQgdXNlZCB0byB2aWV3IGl0LlxuICAgKlxuICAgKiBAcGFyYW0gcGF0aCAtIFRoZSBmaWxlIHBhdGggdG8gY3JlYXRlLlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0TmFtZSAtIFRoZSBuYW1lIG9mIHRoZSB3aWRnZXQgZmFjdG9yeSB0byB1c2UuICdkZWZhdWx0JyB3aWxsIHVzZSB0aGUgZGVmYXVsdCB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSBrZXJuZWwgLSBBbiBvcHRpb25hbCBrZXJuZWwgbmFtZS9pZCB0byBvdmVycmlkZSB0aGUgZGVmYXVsdC5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIGNyZWF0ZWQgd2lkZ2V0LCBvciBgdW5kZWZpbmVkYC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGlzIGZ1bmN0aW9uIHdpbGwgcmV0dXJuIGB1bmRlZmluZWRgIGlmIGEgdmFsaWQgd2lkZ2V0IGZhY3RvcnlcbiAgICogY2Fubm90IGJlIGZvdW5kLlxuICAgKi9cbiAgY3JlYXRlTmV3KFxuICAgIHBhdGg6IHN0cmluZyxcbiAgICB3aWRnZXROYW1lPzogc3RyaW5nLFxuICAgIGtlcm5lbD86IFBhcnRpYWw8S2VybmVsLklNb2RlbD5cbiAgKTogV2lkZ2V0IHwgdW5kZWZpbmVkO1xuXG4gIC8qKlxuICAgKiBEZWxldGUgYSBmaWxlLlxuICAgKlxuICAgKiBAcGFyYW0gcGF0aCAtIFRoZSBmdWxsIHBhdGggdG8gdGhlIGZpbGUgdG8gYmUgZGVsZXRlZC5cbiAgICpcbiAgICogQHJldHVybnMgQSBwcm9taXNlIHdoaWNoIHJlc29sdmVzIHdoZW4gdGhlIGZpbGUgaXMgZGVsZXRlZC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBJZiB0aGVyZSBpcyBhIHJ1bm5pbmcgc2Vzc2lvbiBhc3NvY2lhdGVkIHdpdGggdGhlIGZpbGUgYW5kIG5vIG90aGVyXG4gICAqIHNlc3Npb25zIGFyZSB1c2luZyB0aGUga2VybmVsLCB0aGUgc2Vzc2lvbiB3aWxsIGJlIHNodXQgZG93bi5cbiAgICovXG4gIGRlbGV0ZUZpbGUocGF0aDogc3RyaW5nKTogUHJvbWlzZTx2b2lkPjtcblxuICAvKipcbiAgICogRHVwbGljYXRlIGEgZmlsZS5cbiAgICpcbiAgICogQHBhcmFtIHBhdGggLSBUaGUgZnVsbCBwYXRoIHRvIHRoZSBmaWxlIHRvIGJlIGR1cGxpY2F0ZWQuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB3aGljaCByZXNvbHZlcyB3aGVuIHRoZSBmaWxlIGlzIGR1cGxpY2F0ZWQuXG4gICAqXG4gICAqL1xuICBkdXBsaWNhdGUocGF0aDogc3RyaW5nKTogUHJvbWlzZTxDb250ZW50cy5JTW9kZWw+O1xuXG4gIC8qKlxuICAgKiBTZWUgaWYgYSB3aWRnZXQgYWxyZWFkeSBleGlzdHMgZm9yIHRoZSBnaXZlbiBwYXRoIGFuZCB3aWRnZXQgbmFtZS5cbiAgICpcbiAgICogQHBhcmFtIHBhdGggLSBUaGUgZmlsZSBwYXRoIHRvIHVzZS5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldE5hbWUgLSBUaGUgbmFtZSBvZiB0aGUgd2lkZ2V0IGZhY3RvcnkgdG8gdXNlLiAnZGVmYXVsdCcgd2lsbCB1c2UgdGhlIGRlZmF1bHQgd2lkZ2V0LlxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgZm91bmQgd2lkZ2V0LCBvciBgdW5kZWZpbmVkYC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGlzIGNhbiBiZSB1c2VkIHRvIGZpbmQgYW4gZXhpc3Rpbmcgd2lkZ2V0IGluc3RlYWQgb2Ygb3BlbmluZ1xuICAgKiBhIG5ldyB3aWRnZXQuXG4gICAqL1xuICBmaW5kV2lkZ2V0KFxuICAgIHBhdGg6IHN0cmluZyxcbiAgICB3aWRnZXROYW1lPzogc3RyaW5nIHwgbnVsbFxuICApOiBJRG9jdW1lbnRXaWRnZXQgfCB1bmRlZmluZWQ7XG5cbiAgLyoqXG4gICAqIENyZWF0ZSBhIG5ldyB1bnRpdGxlZCBmaWxlLlxuICAgKlxuICAgKiBAcGFyYW0gb3B0aW9ucyAtIFRoZSBmaWxlIGNvbnRlbnQgY3JlYXRpb24gb3B0aW9ucy5cbiAgICovXG4gIG5ld1VudGl0bGVkKG9wdGlvbnM6IENvbnRlbnRzLklDcmVhdGVPcHRpb25zKTogUHJvbWlzZTxDb250ZW50cy5JTW9kZWw+O1xuXG4gIC8qKlxuICAgKiBPcGVuIGEgZmlsZSBhbmQgcmV0dXJuIHRoZSB3aWRnZXQgdXNlZCB0byB2aWV3IGl0LlxuICAgKlxuICAgKiBAcGFyYW0gcGF0aCAtIFRoZSBmaWxlIHBhdGggdG8gb3Blbi5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldE5hbWUgLSBUaGUgbmFtZSBvZiB0aGUgd2lkZ2V0IGZhY3RvcnkgdG8gdXNlLiAnZGVmYXVsdCcgd2lsbCB1c2UgdGhlIGRlZmF1bHQgd2lkZ2V0LlxuICAgKlxuICAgKiBAcGFyYW0ga2VybmVsIC0gQW4gb3B0aW9uYWwga2VybmVsIG5hbWUvaWQgdG8gb3ZlcnJpZGUgdGhlIGRlZmF1bHQuXG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSBjcmVhdGVkIHdpZGdldCwgb3IgYHVuZGVmaW5lZGAuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBmdW5jdGlvbiB3aWxsIHJldHVybiBgdW5kZWZpbmVkYCBpZiBhIHZhbGlkIHdpZGdldCBmYWN0b3J5XG4gICAqIGNhbm5vdCBiZSBmb3VuZC5cbiAgICovXG4gIG9wZW4oXG4gICAgcGF0aDogc3RyaW5nLFxuICAgIHdpZGdldE5hbWU/OiBzdHJpbmcsXG4gICAga2VybmVsPzogUGFydGlhbDxLZXJuZWwuSU1vZGVsPixcbiAgICBvcHRpb25zPzogRG9jdW1lbnRSZWdpc3RyeS5JT3Blbk9wdGlvbnNcbiAgKTogSURvY3VtZW50V2lkZ2V0IHwgdW5kZWZpbmVkO1xuXG4gIC8qKlxuICAgKiBPcGVuIGEgZmlsZSBhbmQgcmV0dXJuIHRoZSB3aWRnZXQgdXNlZCB0byB2aWV3IGl0LlxuICAgKiBSZXZlYWxzIGFuIGFscmVhZHkgZXhpc3RpbmcgZWRpdG9yLlxuICAgKlxuICAgKiBAcGFyYW0gcGF0aCAtIFRoZSBmaWxlIHBhdGggdG8gb3Blbi5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldE5hbWUgLSBUaGUgbmFtZSBvZiB0aGUgd2lkZ2V0IGZhY3RvcnkgdG8gdXNlLiAnZGVmYXVsdCcgd2lsbCB1c2UgdGhlIGRlZmF1bHQgd2lkZ2V0LlxuICAgKlxuICAgKiBAcGFyYW0ga2VybmVsIC0gQW4gb3B0aW9uYWwga2VybmVsIG5hbWUvaWQgdG8gb3ZlcnJpZGUgdGhlIGRlZmF1bHQuXG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSBjcmVhdGVkIHdpZGdldCwgb3IgYHVuZGVmaW5lZGAuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBmdW5jdGlvbiB3aWxsIHJldHVybiBgdW5kZWZpbmVkYCBpZiBhIHZhbGlkIHdpZGdldCBmYWN0b3J5XG4gICAqIGNhbm5vdCBiZSBmb3VuZC5cbiAgICovXG4gIG9wZW5PclJldmVhbChcbiAgICBwYXRoOiBzdHJpbmcsXG4gICAgd2lkZ2V0TmFtZT86IHN0cmluZyxcbiAgICBrZXJuZWw/OiBQYXJ0aWFsPEtlcm5lbC5JTW9kZWw+LFxuICAgIG9wdGlvbnM/OiBEb2N1bWVudFJlZ2lzdHJ5LklPcGVuT3B0aW9uc1xuICApOiBJRG9jdW1lbnRXaWRnZXQgfCB1bmRlZmluZWQ7XG5cbiAgLyoqXG4gICAqIE92ZXJ3cml0ZSBhIGZpbGUuXG4gICAqXG4gICAqIEBwYXJhbSBvbGRQYXRoIC0gVGhlIGZ1bGwgcGF0aCB0byB0aGUgb3JpZ2luYWwgZmlsZS5cbiAgICpcbiAgICogQHBhcmFtIG5ld1BhdGggLSBUaGUgZnVsbCBwYXRoIHRvIHRoZSBuZXcgZmlsZS5cbiAgICpcbiAgICogQHJldHVybnMgQSBwcm9taXNlIGNvbnRhaW5pbmcgdGhlIG5ldyBmaWxlIGNvbnRlbnRzIG1vZGVsLlxuICAgKi9cbiAgb3ZlcndyaXRlKG9sZFBhdGg6IHN0cmluZywgbmV3UGF0aDogc3RyaW5nKTogUHJvbWlzZTxDb250ZW50cy5JTW9kZWw+O1xuXG4gIC8qKlxuICAgKiBSZW5hbWUgYSBmaWxlIG9yIGRpcmVjdG9yeS5cbiAgICpcbiAgICogQHBhcmFtIG9sZFBhdGggLSBUaGUgZnVsbCBwYXRoIHRvIHRoZSBvcmlnaW5hbCBmaWxlLlxuICAgKlxuICAgKiBAcGFyYW0gbmV3UGF0aCAtIFRoZSBmdWxsIHBhdGggdG8gdGhlIG5ldyBmaWxlLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2UgY29udGFpbmluZyB0aGUgbmV3IGZpbGUgY29udGVudHMgbW9kZWwuICBUaGUgcHJvbWlzZVxuICAgKiB3aWxsIHJlamVjdCBpZiB0aGUgbmV3UGF0aCBhbHJlYWR5IGV4aXN0cy4gIFVzZSBbW292ZXJ3cml0ZV1dIHRvIG92ZXJ3cml0ZVxuICAgKiBhIGZpbGUuXG4gICAqL1xuICByZW5hbWUob2xkUGF0aDogc3RyaW5nLCBuZXdQYXRoOiBzdHJpbmcpOiBQcm9taXNlPENvbnRlbnRzLklNb2RlbD47XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IERpYWxvZywgc2hvd0RpYWxvZyB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IFRpbWUgfSBmcm9tICdAanVweXRlcmxhYi9jb3JldXRpbHMnO1xuaW1wb3J0IHsgRG9jdW1lbnRSZWdpc3RyeSwgSURvY3VtZW50V2lkZ2V0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jcmVnaXN0cnknO1xuaW1wb3J0IHsgQ29udGVudHMgfSBmcm9tICdAanVweXRlcmxhYi9zZXJ2aWNlcyc7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciwgbnVsbFRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQgeyBBcnJheUV4dCwgZWFjaCwgZmlsdGVyLCBmaW5kLCBtYXAsIHRvQXJyYXkgfSBmcm9tICdAbHVtaW5vL2FsZ29yaXRobSc7XG5pbXBvcnQgeyBEaXNwb3NhYmxlU2V0LCBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBJTWVzc2FnZUhhbmRsZXIsIE1lc3NhZ2UsIE1lc3NhZ2VMb29wIH0gZnJvbSAnQGx1bWluby9tZXNzYWdpbmcnO1xuaW1wb3J0IHsgQXR0YWNoZWRQcm9wZXJ0eSB9IGZyb20gJ0BsdW1pbm8vcHJvcGVydGllcyc7XG5pbXBvcnQgeyBJU2lnbmFsLCBTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIGRvY3VtZW50IHdpZGdldHMuXG4gKi9cbmNvbnN0IERPQ1VNRU5UX0NMQVNTID0gJ2pwLURvY3VtZW50JztcblxuLyoqXG4gKiBBIGNsYXNzIHRoYXQgbWFpbnRhaW5zIHRoZSBsaWZlY3ljbGUgb2YgZmlsZS1iYWNrZWQgd2lkZ2V0cy5cbiAqL1xuZXhwb3J0IGNsYXNzIERvY3VtZW50V2lkZ2V0TWFuYWdlciBpbXBsZW1lbnRzIElEaXNwb3NhYmxlIHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCBhIG5ldyBkb2N1bWVudCB3aWRnZXQgbWFuYWdlci5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IERvY3VtZW50V2lkZ2V0TWFuYWdlci5JT3B0aW9ucykge1xuICAgIHRoaXMuX3JlZ2lzdHJ5ID0gb3B0aW9ucy5yZWdpc3RyeTtcbiAgICB0aGlzLnRyYW5zbGF0b3IgPSBvcHRpb25zLnRyYW5zbGF0b3IgfHwgbnVsbFRyYW5zbGF0b3I7XG4gIH1cblxuICAvKipcbiAgICogQSBzaWduYWwgZW1pdHRlZCB3aGVuIG9uZSBvZiB0aGUgZG9jdW1lbnRzIGlzIGFjdGl2YXRlZC5cbiAgICovXG4gIGdldCBhY3RpdmF0ZVJlcXVlc3RlZCgpOiBJU2lnbmFsPHRoaXMsIHN0cmluZz4ge1xuICAgIHJldHVybiB0aGlzLl9hY3RpdmF0ZVJlcXVlc3RlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBUZXN0IHdoZXRoZXIgdGhlIGRvY3VtZW50IHdpZGdldCBtYW5hZ2VyIGlzIGRpc3Bvc2VkLlxuICAgKi9cbiAgZ2V0IGlzRGlzcG9zZWQoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuX2lzRGlzcG9zZWQ7XG4gIH1cblxuICAvKipcbiAgICogRGlzcG9zZSBvZiB0aGUgcmVzb3VyY2VzIHVzZWQgYnkgdGhlIHdpZGdldCBtYW5hZ2VyLlxuICAgKi9cbiAgZGlzcG9zZSgpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIHRoaXMuX2lzRGlzcG9zZWQgPSB0cnVlO1xuICAgIFNpZ25hbC5kaXNjb25uZWN0UmVjZWl2ZXIodGhpcyk7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGEgd2lkZ2V0IGZvciBhIGRvY3VtZW50IGFuZCBoYW5kbGUgaXRzIGxpZmVjeWNsZS5cbiAgICpcbiAgICogQHBhcmFtIGZhY3RvcnkgLSBUaGUgd2lkZ2V0IGZhY3RvcnkuXG4gICAqXG4gICAqIEBwYXJhbSBjb250ZXh0IC0gVGhlIGRvY3VtZW50IGNvbnRleHQgb2JqZWN0LlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHdpZGdldCBjcmVhdGVkIGJ5IHRoZSBmYWN0b3J5LlxuICAgKlxuICAgKiBAdGhyb3dzIElmIHRoZSBmYWN0b3J5IGlzIG5vdCByZWdpc3RlcmVkLlxuICAgKi9cbiAgY3JlYXRlV2lkZ2V0KFxuICAgIGZhY3Rvcnk6IERvY3VtZW50UmVnaXN0cnkuV2lkZ2V0RmFjdG9yeSxcbiAgICBjb250ZXh0OiBEb2N1bWVudFJlZ2lzdHJ5LkNvbnRleHRcbiAgKTogSURvY3VtZW50V2lkZ2V0IHtcbiAgICBjb25zdCB3aWRnZXQgPSBmYWN0b3J5LmNyZWF0ZU5ldyhjb250ZXh0KTtcbiAgICB0aGlzLl9pbml0aWFsaXplV2lkZ2V0KHdpZGdldCwgZmFjdG9yeSwgY29udGV4dCk7XG4gICAgcmV0dXJuIHdpZGdldDtcbiAgfVxuXG4gIC8qKlxuICAgKiBXaGVuIGEgbmV3IHdpZGdldCBpcyBjcmVhdGVkLCB3ZSBuZWVkIHRvIGhvb2sgaXQgdXBcbiAgICogd2l0aCBzb21lIHNpZ25hbHMsIHVwZGF0ZSB0aGUgd2lkZ2V0IGV4dGVuc2lvbnMgKGZvclxuICAgKiB0aGlzIGtpbmQgb2Ygd2lkZ2V0KSBpbiB0aGUgZG9jcmVnaXN0cnksIGFtb25nXG4gICAqIG90aGVyIHRoaW5ncy5cbiAgICovXG4gIHByaXZhdGUgX2luaXRpYWxpemVXaWRnZXQoXG4gICAgd2lkZ2V0OiBJRG9jdW1lbnRXaWRnZXQsXG4gICAgZmFjdG9yeTogRG9jdW1lbnRSZWdpc3RyeS5XaWRnZXRGYWN0b3J5LFxuICAgIGNvbnRleHQ6IERvY3VtZW50UmVnaXN0cnkuQ29udGV4dFxuICApIHtcbiAgICBQcml2YXRlLmZhY3RvcnlQcm9wZXJ0eS5zZXQod2lkZ2V0LCBmYWN0b3J5KTtcbiAgICAvLyBIYW5kbGUgd2lkZ2V0IGV4dGVuc2lvbnMuXG4gICAgY29uc3QgZGlzcG9zYWJsZXMgPSBuZXcgRGlzcG9zYWJsZVNldCgpO1xuICAgIGVhY2godGhpcy5fcmVnaXN0cnkud2lkZ2V0RXh0ZW5zaW9ucyhmYWN0b3J5Lm5hbWUpLCBleHRlbmRlciA9PiB7XG4gICAgICBjb25zdCBkaXNwb3NhYmxlID0gZXh0ZW5kZXIuY3JlYXRlTmV3KHdpZGdldCwgY29udGV4dCk7XG4gICAgICBpZiAoZGlzcG9zYWJsZSkge1xuICAgICAgICBkaXNwb3NhYmxlcy5hZGQoZGlzcG9zYWJsZSk7XG4gICAgICB9XG4gICAgfSk7XG4gICAgUHJpdmF0ZS5kaXNwb3NhYmxlc1Byb3BlcnR5LnNldCh3aWRnZXQsIGRpc3Bvc2FibGVzKTtcbiAgICB3aWRnZXQuZGlzcG9zZWQuY29ubmVjdCh0aGlzLl9vbldpZGdldERpc3Bvc2VkLCB0aGlzKTtcblxuICAgIHRoaXMuYWRvcHRXaWRnZXQoY29udGV4dCwgd2lkZ2V0KTtcbiAgICBjb250ZXh0LmZpbGVDaGFuZ2VkLmNvbm5lY3QodGhpcy5fb25GaWxlQ2hhbmdlZCwgdGhpcyk7XG4gICAgY29udGV4dC5wYXRoQ2hhbmdlZC5jb25uZWN0KHRoaXMuX29uUGF0aENoYW5nZWQsIHRoaXMpO1xuICAgIHZvaWQgY29udGV4dC5yZWFkeS50aGVuKCgpID0+IHtcbiAgICAgIHZvaWQgdGhpcy5zZXRDYXB0aW9uKHdpZGdldCk7XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogSW5zdGFsbCB0aGUgbWVzc2FnZSBob29rIGZvciB0aGUgd2lkZ2V0IGFuZCBhZGQgdG8gbGlzdFxuICAgKiBvZiBrbm93biB3aWRnZXRzLlxuICAgKlxuICAgKiBAcGFyYW0gY29udGV4dCAtIFRoZSBkb2N1bWVudCBjb250ZXh0IG9iamVjdC5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldCAtIFRoZSB3aWRnZXQgdG8gYWRvcHQuXG4gICAqL1xuICBhZG9wdFdpZGdldChcbiAgICBjb250ZXh0OiBEb2N1bWVudFJlZ2lzdHJ5LkNvbnRleHQsXG4gICAgd2lkZ2V0OiBJRG9jdW1lbnRXaWRnZXRcbiAgKTogdm9pZCB7XG4gICAgY29uc3Qgd2lkZ2V0cyA9IFByaXZhdGUud2lkZ2V0c1Byb3BlcnR5LmdldChjb250ZXh0KTtcbiAgICB3aWRnZXRzLnB1c2god2lkZ2V0KTtcbiAgICBNZXNzYWdlTG9vcC5pbnN0YWxsTWVzc2FnZUhvb2sod2lkZ2V0LCB0aGlzKTtcbiAgICB3aWRnZXQuYWRkQ2xhc3MoRE9DVU1FTlRfQ0xBU1MpO1xuICAgIHdpZGdldC50aXRsZS5jbG9zYWJsZSA9IHRydWU7XG4gICAgd2lkZ2V0LmRpc3Bvc2VkLmNvbm5lY3QodGhpcy5fd2lkZ2V0RGlzcG9zZWQsIHRoaXMpO1xuICAgIFByaXZhdGUuY29udGV4dFByb3BlcnR5LnNldCh3aWRnZXQsIGNvbnRleHQpO1xuICB9XG5cbiAgLyoqXG4gICAqIFNlZSBpZiBhIHdpZGdldCBhbHJlYWR5IGV4aXN0cyBmb3IgdGhlIGdpdmVuIGNvbnRleHQgYW5kIHdpZGdldCBuYW1lLlxuICAgKlxuICAgKiBAcGFyYW0gY29udGV4dCAtIFRoZSBkb2N1bWVudCBjb250ZXh0IG9iamVjdC5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIGZvdW5kIHdpZGdldCwgb3IgYHVuZGVmaW5lZGAuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBjYW4gYmUgdXNlZCB0byB1c2UgYW4gZXhpc3Rpbmcgd2lkZ2V0IGluc3RlYWQgb2Ygb3BlbmluZ1xuICAgKiBhIG5ldyB3aWRnZXQuXG4gICAqL1xuICBmaW5kV2lkZ2V0KFxuICAgIGNvbnRleHQ6IERvY3VtZW50UmVnaXN0cnkuQ29udGV4dCxcbiAgICB3aWRnZXROYW1lOiBzdHJpbmdcbiAgKTogSURvY3VtZW50V2lkZ2V0IHwgdW5kZWZpbmVkIHtcbiAgICBjb25zdCB3aWRnZXRzID0gUHJpdmF0ZS53aWRnZXRzUHJvcGVydHkuZ2V0KGNvbnRleHQpO1xuICAgIGlmICghd2lkZ2V0cykge1xuICAgICAgcmV0dXJuIHVuZGVmaW5lZDtcbiAgICB9XG4gICAgcmV0dXJuIGZpbmQod2lkZ2V0cywgd2lkZ2V0ID0+IHtcbiAgICAgIGNvbnN0IGZhY3RvcnkgPSBQcml2YXRlLmZhY3RvcnlQcm9wZXJ0eS5nZXQod2lkZ2V0KTtcbiAgICAgIGlmICghZmFjdG9yeSkge1xuICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICB9XG4gICAgICByZXR1cm4gZmFjdG9yeS5uYW1lID09PSB3aWRnZXROYW1lO1xuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgZG9jdW1lbnQgY29udGV4dCBmb3IgYSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgLSBUaGUgd2lkZ2V0IG9mIGludGVyZXN0LlxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgY29udGV4dCBhc3NvY2lhdGVkIHdpdGggdGhlIHdpZGdldCwgb3IgYHVuZGVmaW5lZGAuXG4gICAqL1xuICBjb250ZXh0Rm9yV2lkZ2V0KHdpZGdldDogV2lkZ2V0KTogRG9jdW1lbnRSZWdpc3RyeS5Db250ZXh0IHwgdW5kZWZpbmVkIHtcbiAgICByZXR1cm4gUHJpdmF0ZS5jb250ZXh0UHJvcGVydHkuZ2V0KHdpZGdldCk7XG4gIH1cblxuICAvKipcbiAgICogQ2xvbmUgYSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgLSBUaGUgc291cmNlIHdpZGdldC5cbiAgICpcbiAgICogQHJldHVybnMgQSBuZXcgd2lkZ2V0IG9yIGB1bmRlZmluZWRgLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqICBVc2VzIHRoZSBzYW1lIHdpZGdldCBmYWN0b3J5IGFuZCBjb250ZXh0IGFzIHRoZSBzb3VyY2UsIG9yIHRocm93c1xuICAgKiAgaWYgdGhlIHNvdXJjZSB3aWRnZXQgaXMgbm90IG1hbmFnZWQgYnkgdGhpcyBtYW5hZ2VyLlxuICAgKi9cbiAgY2xvbmVXaWRnZXQod2lkZ2V0OiBXaWRnZXQpOiBJRG9jdW1lbnRXaWRnZXQgfCB1bmRlZmluZWQge1xuICAgIGNvbnN0IGNvbnRleHQgPSBQcml2YXRlLmNvbnRleHRQcm9wZXJ0eS5nZXQod2lkZ2V0KTtcbiAgICBpZiAoIWNvbnRleHQpIHtcbiAgICAgIHJldHVybiB1bmRlZmluZWQ7XG4gICAgfVxuICAgIGNvbnN0IGZhY3RvcnkgPSBQcml2YXRlLmZhY3RvcnlQcm9wZXJ0eS5nZXQod2lkZ2V0KTtcbiAgICBpZiAoIWZhY3RvcnkpIHtcbiAgICAgIHJldHVybiB1bmRlZmluZWQ7XG4gICAgfVxuICAgIGNvbnN0IG5ld1dpZGdldCA9IGZhY3RvcnkuY3JlYXRlTmV3KGNvbnRleHQsIHdpZGdldCBhcyBJRG9jdW1lbnRXaWRnZXQpO1xuICAgIHRoaXMuX2luaXRpYWxpemVXaWRnZXQobmV3V2lkZ2V0LCBmYWN0b3J5LCBjb250ZXh0KTtcbiAgICByZXR1cm4gbmV3V2lkZ2V0O1xuICB9XG5cbiAgLyoqXG4gICAqIENsb3NlIHRoZSB3aWRnZXRzIGFzc29jaWF0ZWQgd2l0aCBhIGdpdmVuIGNvbnRleHQuXG4gICAqXG4gICAqIEBwYXJhbSBjb250ZXh0IC0gVGhlIGRvY3VtZW50IGNvbnRleHQgb2JqZWN0LlxuICAgKi9cbiAgY2xvc2VXaWRnZXRzKGNvbnRleHQ6IERvY3VtZW50UmVnaXN0cnkuQ29udGV4dCk6IFByb21pc2U8dm9pZD4ge1xuICAgIGNvbnN0IHdpZGdldHMgPSBQcml2YXRlLndpZGdldHNQcm9wZXJ0eS5nZXQoY29udGV4dCk7XG4gICAgcmV0dXJuIFByb21pc2UuYWxsKFxuICAgICAgdG9BcnJheShtYXAod2lkZ2V0cywgd2lkZ2V0ID0+IHRoaXMub25DbG9zZSh3aWRnZXQpKSlcbiAgICApLnRoZW4oKCkgPT4gdW5kZWZpbmVkKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIG9mIHRoZSB3aWRnZXRzIGFzc29jaWF0ZWQgd2l0aCBhIGdpdmVuIGNvbnRleHRcbiAgICogcmVnYXJkbGVzcyBvZiB0aGUgd2lkZ2V0J3MgZGlydHkgc3RhdGUuXG4gICAqXG4gICAqIEBwYXJhbSBjb250ZXh0IC0gVGhlIGRvY3VtZW50IGNvbnRleHQgb2JqZWN0LlxuICAgKi9cbiAgZGVsZXRlV2lkZ2V0cyhjb250ZXh0OiBEb2N1bWVudFJlZ2lzdHJ5LkNvbnRleHQpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBjb25zdCB3aWRnZXRzID0gUHJpdmF0ZS53aWRnZXRzUHJvcGVydHkuZ2V0KGNvbnRleHQpO1xuICAgIHJldHVybiBQcm9taXNlLmFsbChcbiAgICAgIHRvQXJyYXkobWFwKHdpZGdldHMsIHdpZGdldCA9PiB0aGlzLm9uRGVsZXRlKHdpZGdldCkpKVxuICAgICkudGhlbigoKSA9PiB1bmRlZmluZWQpO1xuICB9XG5cbiAgLyoqXG4gICAqIEZpbHRlciBhIG1lc3NhZ2Ugc2VudCB0byBhIG1lc3NhZ2UgaGFuZGxlci5cbiAgICpcbiAgICogQHBhcmFtIGhhbmRsZXIgLSBUaGUgdGFyZ2V0IGhhbmRsZXIgb2YgdGhlIG1lc3NhZ2UuXG4gICAqXG4gICAqIEBwYXJhbSBtc2cgLSBUaGUgbWVzc2FnZSBkaXNwYXRjaGVkIHRvIHRoZSBoYW5kbGVyLlxuICAgKlxuICAgKiBAcmV0dXJucyBgZmFsc2VgIGlmIHRoZSBtZXNzYWdlIHNob3VsZCBiZSBmaWx0ZXJlZCwgb2YgYHRydWVgXG4gICAqICAgaWYgdGhlIG1lc3NhZ2Ugc2hvdWxkIGJlIGRpc3BhdGNoZWQgdG8gdGhlIGhhbmRsZXIgYXMgbm9ybWFsLlxuICAgKi9cbiAgbWVzc2FnZUhvb2soaGFuZGxlcjogSU1lc3NhZ2VIYW5kbGVyLCBtc2c6IE1lc3NhZ2UpOiBib29sZWFuIHtcbiAgICBzd2l0Y2ggKG1zZy50eXBlKSB7XG4gICAgICBjYXNlICdjbG9zZS1yZXF1ZXN0JzpcbiAgICAgICAgdm9pZCB0aGlzLm9uQ2xvc2UoaGFuZGxlciBhcyBXaWRnZXQpO1xuICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICBjYXNlICdhY3RpdmF0ZS1yZXF1ZXN0Jzoge1xuICAgICAgICBjb25zdCBjb250ZXh0ID0gdGhpcy5jb250ZXh0Rm9yV2lkZ2V0KGhhbmRsZXIgYXMgV2lkZ2V0KTtcbiAgICAgICAgaWYgKGNvbnRleHQpIHtcbiAgICAgICAgICB0aGlzLl9hY3RpdmF0ZVJlcXVlc3RlZC5lbWl0KGNvbnRleHQucGF0aCk7XG4gICAgICAgIH1cbiAgICAgICAgYnJlYWs7XG4gICAgICB9XG4gICAgICBkZWZhdWx0OlxuICAgICAgICBicmVhaztcbiAgICB9XG4gICAgcmV0dXJuIHRydWU7XG4gIH1cblxuICAvKipcbiAgICogU2V0IHRoZSBjYXB0aW9uIGZvciB3aWRnZXQgdGl0bGUuXG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgLSBUaGUgdGFyZ2V0IHdpZGdldC5cbiAgICovXG4gIHByb3RlY3RlZCBhc3luYyBzZXRDYXB0aW9uKHdpZGdldDogV2lkZ2V0KTogUHJvbWlzZTx2b2lkPiB7XG4gICAgY29uc3QgdHJhbnMgPSB0aGlzLnRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IGNvbnRleHQgPSBQcml2YXRlLmNvbnRleHRQcm9wZXJ0eS5nZXQod2lkZ2V0KTtcbiAgICBpZiAoIWNvbnRleHQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgY29uc3QgbW9kZWwgPSBjb250ZXh0LmNvbnRlbnRzTW9kZWw7XG4gICAgaWYgKCFtb2RlbCkge1xuICAgICAgd2lkZ2V0LnRpdGxlLmNhcHRpb24gPSAnJztcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgcmV0dXJuIGNvbnRleHRcbiAgICAgIC5saXN0Q2hlY2twb2ludHMoKVxuICAgICAgLnRoZW4oKGNoZWNrcG9pbnRzOiBDb250ZW50cy5JQ2hlY2twb2ludE1vZGVsW10pID0+IHtcbiAgICAgICAgaWYgKHdpZGdldC5pc0Rpc3Bvc2VkKSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IGxhc3QgPSBjaGVja3BvaW50c1tjaGVja3BvaW50cy5sZW5ndGggLSAxXTtcbiAgICAgICAgY29uc3QgY2hlY2twb2ludCA9IGxhc3QgPyBUaW1lLmZvcm1hdChsYXN0Lmxhc3RfbW9kaWZpZWQpIDogJ05vbmUnO1xuICAgICAgICBsZXQgY2FwdGlvbiA9IHRyYW5zLl9fKFxuICAgICAgICAgICdOYW1lOiAlMVxcblBhdGg6ICUyXFxuJyxcbiAgICAgICAgICBtb2RlbCEubmFtZSxcbiAgICAgICAgICBtb2RlbCEucGF0aFxuICAgICAgICApO1xuICAgICAgICBpZiAoY29udGV4dCEubW9kZWwucmVhZE9ubHkpIHtcbiAgICAgICAgICBjYXB0aW9uICs9IHRyYW5zLl9fKCdSZWFkLW9ubHknKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICBjYXB0aW9uICs9XG4gICAgICAgICAgICB0cmFucy5fXygnTGFzdCBTYXZlZDogJTFcXG4nLCBUaW1lLmZvcm1hdChtb2RlbCEubGFzdF9tb2RpZmllZCkpICtcbiAgICAgICAgICAgIHRyYW5zLl9fKCdMYXN0IENoZWNrcG9pbnQ6ICUxJywgY2hlY2twb2ludCk7XG4gICAgICAgIH1cbiAgICAgICAgd2lkZ2V0LnRpdGxlLmNhcHRpb24gPSBjYXB0aW9uO1xuICAgICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGAnY2xvc2UtcmVxdWVzdCdgIG1lc3NhZ2VzLlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IC0gVGhlIHRhcmdldCB3aWRnZXQuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB0aGF0IHJlc29sdmVzIHdpdGggd2hldGhlciB0aGUgd2lkZ2V0IHdhcyBjbG9zZWQuXG4gICAqL1xuICBwcm90ZWN0ZWQgYXN5bmMgb25DbG9zZSh3aWRnZXQ6IFdpZGdldCk6IFByb21pc2U8Ym9vbGVhbj4ge1xuICAgIC8vIEhhbmRsZSBkaXJ0eSBzdGF0ZS5cbiAgICBjb25zdCBbc2hvdWxkQ2xvc2UsIGlnbm9yZVNhdmVdID0gYXdhaXQgdGhpcy5fbWF5YmVDbG9zZShcbiAgICAgIHdpZGdldCxcbiAgICAgIHRoaXMudHJhbnNsYXRvclxuICAgICk7XG4gICAgaWYgKHdpZGdldC5pc0Rpc3Bvc2VkKSB7XG4gICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9XG4gICAgaWYgKHNob3VsZENsb3NlKSB7XG4gICAgICBpZiAoIWlnbm9yZVNhdmUpIHtcbiAgICAgICAgY29uc3QgY29udGV4dCA9IFByaXZhdGUuY29udGV4dFByb3BlcnR5LmdldCh3aWRnZXQpO1xuICAgICAgICBpZiAoIWNvbnRleHQpIHtcbiAgICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgICAgfVxuICAgICAgICBpZiAoY29udGV4dC5jb250ZW50c01vZGVsPy53cml0YWJsZSkge1xuICAgICAgICAgIGF3YWl0IGNvbnRleHQuc2F2ZSgpO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIGF3YWl0IGNvbnRleHQuc2F2ZUFzKCk7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICAgIGlmICh3aWRnZXQuaXNEaXNwb3NlZCkge1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH1cbiAgICAgIHdpZGdldC5kaXNwb3NlKCk7XG4gICAgfVxuICAgIHJldHVybiBzaG91bGRDbG9zZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIG9mIHdpZGdldCByZWdhcmRsZXNzIG9mIHdpZGdldCdzIGRpcnR5IHN0YXRlLlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IC0gVGhlIHRhcmdldCB3aWRnZXQuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25EZWxldGUod2lkZ2V0OiBXaWRnZXQpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICB3aWRnZXQuZGlzcG9zZSgpO1xuICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUodm9pZCAwKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBc2sgdGhlIHVzZXIgd2hldGhlciB0byBjbG9zZSBhbiB1bnNhdmVkIGZpbGUuXG4gICAqL1xuICBwcml2YXRlIF9tYXliZUNsb3NlKFxuICAgIHdpZGdldDogV2lkZ2V0LFxuICAgIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvclxuICApOiBQcm9taXNlPFtib29sZWFuLCBib29sZWFuXT4ge1xuICAgIHRyYW5zbGF0b3IgPSB0cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgLy8gQmFpbCBpZiB0aGUgbW9kZWwgaXMgbm90IGRpcnR5IG9yIG90aGVyIHdpZGdldHMgYXJlIHVzaW5nIHRoZSBtb2RlbC4pXG4gICAgY29uc3QgY29udGV4dCA9IFByaXZhdGUuY29udGV4dFByb3BlcnR5LmdldCh3aWRnZXQpO1xuICAgIGlmICghY29udGV4dCkge1xuICAgICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShbdHJ1ZSwgdHJ1ZV0pO1xuICAgIH1cbiAgICBsZXQgd2lkZ2V0cyA9IFByaXZhdGUud2lkZ2V0c1Byb3BlcnR5LmdldChjb250ZXh0KTtcbiAgICBpZiAoIXdpZGdldHMpIHtcbiAgICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUoW3RydWUsIHRydWVdKTtcbiAgICB9XG4gICAgLy8gRmlsdGVyIGJ5IHdoZXRoZXIgdGhlIGZhY3RvcmllcyBhcmUgcmVhZCBvbmx5LlxuICAgIHdpZGdldHMgPSB0b0FycmF5KFxuICAgICAgZmlsdGVyKHdpZGdldHMsIHdpZGdldCA9PiB7XG4gICAgICAgIGNvbnN0IGZhY3RvcnkgPSBQcml2YXRlLmZhY3RvcnlQcm9wZXJ0eS5nZXQod2lkZ2V0KTtcbiAgICAgICAgaWYgKCFmYWN0b3J5KSB7XG4gICAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiBmYWN0b3J5LnJlYWRPbmx5ID09PSBmYWxzZTtcbiAgICAgIH0pXG4gICAgKTtcbiAgICBjb25zdCBmYWN0b3J5ID0gUHJpdmF0ZS5mYWN0b3J5UHJvcGVydHkuZ2V0KHdpZGdldCk7XG4gICAgaWYgKCFmYWN0b3J5KSB7XG4gICAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKFt0cnVlLCB0cnVlXSk7XG4gICAgfVxuICAgIGNvbnN0IG1vZGVsID0gY29udGV4dC5tb2RlbDtcbiAgICBpZiAoIW1vZGVsLmRpcnR5IHx8IHdpZGdldHMubGVuZ3RoID4gMSB8fCBmYWN0b3J5LnJlYWRPbmx5KSB7XG4gICAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKFt0cnVlLCB0cnVlXSk7XG4gICAgfVxuICAgIGNvbnN0IGZpbGVOYW1lID0gd2lkZ2V0LnRpdGxlLmxhYmVsO1xuICAgIGNvbnN0IHNhdmVMYWJlbCA9IGNvbnRleHQuY29udGVudHNNb2RlbD8ud3JpdGFibGVcbiAgICAgID8gdHJhbnMuX18oJ1NhdmUnKVxuICAgICAgOiB0cmFucy5fXygnU2F2ZSBhcycpO1xuICAgIHJldHVybiBzaG93RGlhbG9nKHtcbiAgICAgIHRpdGxlOiB0cmFucy5fXygnU2F2ZSB5b3VyIHdvcmsnKSxcbiAgICAgIGJvZHk6IHRyYW5zLl9fKCdTYXZlIGNoYW5nZXMgaW4gXCIlMVwiIGJlZm9yZSBjbG9zaW5nPycsIGZpbGVOYW1lKSxcbiAgICAgIGJ1dHRvbnM6IFtcbiAgICAgICAgRGlhbG9nLmNhbmNlbEJ1dHRvbigpLFxuICAgICAgICBEaWFsb2cud2FybkJ1dHRvbih7IGxhYmVsOiB0cmFucy5fXygnRGlzY2FyZCcpIH0pLFxuICAgICAgICBEaWFsb2cub2tCdXR0b24oeyBsYWJlbDogc2F2ZUxhYmVsIH0pXG4gICAgICBdXG4gICAgfSkudGhlbihyZXN1bHQgPT4ge1xuICAgICAgcmV0dXJuIFtyZXN1bHQuYnV0dG9uLmFjY2VwdCwgcmVzdWx0LmJ1dHRvbi5kaXNwbGF5VHlwZSA9PT0gJ3dhcm4nXTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIGRpc3Bvc2FsIG9mIGEgd2lkZ2V0LlxuICAgKi9cbiAgcHJpdmF0ZSBfd2lkZ2V0RGlzcG9zZWQod2lkZ2V0OiBXaWRnZXQpOiB2b2lkIHtcbiAgICBjb25zdCBjb250ZXh0ID0gUHJpdmF0ZS5jb250ZXh0UHJvcGVydHkuZ2V0KHdpZGdldCk7XG4gICAgaWYgKCFjb250ZXh0KSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbnN0IHdpZGdldHMgPSBQcml2YXRlLndpZGdldHNQcm9wZXJ0eS5nZXQoY29udGV4dCk7XG4gICAgaWYgKCF3aWRnZXRzKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIC8vIFJlbW92ZSB0aGUgd2lkZ2V0LlxuICAgIEFycmF5RXh0LnJlbW92ZUZpcnN0T2Yod2lkZ2V0cywgd2lkZ2V0KTtcbiAgICAvLyBEaXNwb3NlIG9mIHRoZSBjb250ZXh0IGlmIHRoaXMgaXMgdGhlIGxhc3Qgd2lkZ2V0IHVzaW5nIGl0LlxuICAgIGlmICghd2lkZ2V0cy5sZW5ndGgpIHtcbiAgICAgIGNvbnRleHQuZGlzcG9zZSgpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIGRpc3Bvc2FsIG9mIGEgd2lkZ2V0LlxuICAgKi9cbiAgcHJpdmF0ZSBfb25XaWRnZXREaXNwb3NlZCh3aWRnZXQ6IFdpZGdldCk6IHZvaWQge1xuICAgIGNvbnN0IGRpc3Bvc2FibGVzID0gUHJpdmF0ZS5kaXNwb3NhYmxlc1Byb3BlcnR5LmdldCh3aWRnZXQpO1xuICAgIGRpc3Bvc2FibGVzLmRpc3Bvc2UoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSBmaWxlIGNoYW5nZWQgc2lnbmFsIGZvciBhIGNvbnRleHQuXG4gICAqL1xuICBwcml2YXRlIF9vbkZpbGVDaGFuZ2VkKGNvbnRleHQ6IERvY3VtZW50UmVnaXN0cnkuQ29udGV4dCk6IHZvaWQge1xuICAgIGNvbnN0IHdpZGdldHMgPSBQcml2YXRlLndpZGdldHNQcm9wZXJ0eS5nZXQoY29udGV4dCk7XG4gICAgZWFjaCh3aWRnZXRzLCB3aWRnZXQgPT4ge1xuICAgICAgdm9pZCB0aGlzLnNldENhcHRpb24od2lkZ2V0KTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSBwYXRoIGNoYW5nZWQgc2lnbmFsIGZvciBhIGNvbnRleHQuXG4gICAqL1xuICBwcml2YXRlIF9vblBhdGhDaGFuZ2VkKGNvbnRleHQ6IERvY3VtZW50UmVnaXN0cnkuQ29udGV4dCk6IHZvaWQge1xuICAgIGNvbnN0IHdpZGdldHMgPSBQcml2YXRlLndpZGdldHNQcm9wZXJ0eS5nZXQoY29udGV4dCk7XG4gICAgZWFjaCh3aWRnZXRzLCB3aWRnZXQgPT4ge1xuICAgICAgdm9pZCB0aGlzLnNldENhcHRpb24od2lkZ2V0KTtcbiAgICB9KTtcbiAgfVxuXG4gIHByb3RlY3RlZCB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcjtcbiAgcHJpdmF0ZSBfcmVnaXN0cnk6IERvY3VtZW50UmVnaXN0cnk7XG4gIHByaXZhdGUgX2FjdGl2YXRlUmVxdWVzdGVkID0gbmV3IFNpZ25hbDx0aGlzLCBzdHJpbmc+KHRoaXMpO1xuICBwcml2YXRlIF9pc0Rpc3Bvc2VkID0gZmFsc2U7XG59XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIGRvY3VtZW50IHdpZGdldCBtYW5hZ2VyIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgRG9jdW1lbnRXaWRnZXRNYW5hZ2VyIHtcbiAgLyoqXG4gICAqIFRoZSBvcHRpb25zIHVzZWQgdG8gaW5pdGlhbGl6ZSBhIGRvY3VtZW50IHdpZGdldCBtYW5hZ2VyLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogQSBkb2N1bWVudCByZWdpc3RyeSBpbnN0YW5jZS5cbiAgICAgKi9cbiAgICByZWdpc3RyeTogRG9jdW1lbnRSZWdpc3RyeTtcblxuICAgIC8qKlxuICAgICAqIFRoZSBhcHBsaWNhdGlvbiBsYW5ndWFnZSB0cmFuc2xhdG9yLlxuICAgICAqL1xuICAgIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvcjtcbiAgfVxufVxuXG4vKipcbiAqIEEgcHJpdmF0ZSBuYW1lc3BhY2UgZm9yIERvY3VtZW50TWFuYWdlciBkYXRhLlxuICovXG5uYW1lc3BhY2UgUHJpdmF0ZSB7XG4gIC8qKlxuICAgKiBBIHByaXZhdGUgYXR0YWNoZWQgcHJvcGVydHkgZm9yIGEgd2lkZ2V0IGNvbnRleHQuXG4gICAqL1xuICBleHBvcnQgY29uc3QgY29udGV4dFByb3BlcnR5ID0gbmV3IEF0dGFjaGVkUHJvcGVydHk8XG4gICAgV2lkZ2V0LFxuICAgIERvY3VtZW50UmVnaXN0cnkuQ29udGV4dCB8IHVuZGVmaW5lZFxuICA+KHtcbiAgICBuYW1lOiAnY29udGV4dCcsXG4gICAgY3JlYXRlOiAoKSA9PiB1bmRlZmluZWRcbiAgfSk7XG5cbiAgLyoqXG4gICAqIEEgcHJpdmF0ZSBhdHRhY2hlZCBwcm9wZXJ0eSBmb3IgYSB3aWRnZXQgZmFjdG9yeS5cbiAgICovXG4gIGV4cG9ydCBjb25zdCBmYWN0b3J5UHJvcGVydHkgPSBuZXcgQXR0YWNoZWRQcm9wZXJ0eTxcbiAgICBXaWRnZXQsXG4gICAgRG9jdW1lbnRSZWdpc3RyeS5XaWRnZXRGYWN0b3J5IHwgdW5kZWZpbmVkXG4gID4oe1xuICAgIG5hbWU6ICdmYWN0b3J5JyxcbiAgICBjcmVhdGU6ICgpID0+IHVuZGVmaW5lZFxuICB9KTtcblxuICAvKipcbiAgICogQSBwcml2YXRlIGF0dGFjaGVkIHByb3BlcnR5IGZvciB0aGUgd2lkZ2V0cyBhc3NvY2lhdGVkIHdpdGggYSBjb250ZXh0LlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IHdpZGdldHNQcm9wZXJ0eSA9IG5ldyBBdHRhY2hlZFByb3BlcnR5PFxuICAgIERvY3VtZW50UmVnaXN0cnkuQ29udGV4dCxcbiAgICBJRG9jdW1lbnRXaWRnZXRbXVxuICA+KHtcbiAgICBuYW1lOiAnd2lkZ2V0cycsXG4gICAgY3JlYXRlOiAoKSA9PiBbXVxuICB9KTtcblxuICAvKipcbiAgICogQSBwcml2YXRlIGF0dGFjaGVkIHByb3BlcnR5IGZvciBhIHdpZGdldCdzIGRpc3Bvc2FibGVzLlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IGRpc3Bvc2FibGVzUHJvcGVydHkgPSBuZXcgQXR0YWNoZWRQcm9wZXJ0eTxcbiAgICBXaWRnZXQsXG4gICAgRGlzcG9zYWJsZVNldFxuICA+KHtcbiAgICBuYW1lOiAnZGlzcG9zYWJsZXMnLFxuICAgIGNyZWF0ZTogKCkgPT4gbmV3IERpc3Bvc2FibGVTZXQoKVxuICB9KTtcbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==