"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_shared-models_lib_index_js"],{

/***/ "../../packages/shared-models/lib/index.js":
/*!*************************************************!*\
  !*** ../../packages/shared-models/lib/index.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "YBaseCell": () => (/* reexport safe */ _ymodels__WEBPACK_IMPORTED_MODULE_0__.YBaseCell),
/* harmony export */   "YCodeCell": () => (/* reexport safe */ _ymodels__WEBPACK_IMPORTED_MODULE_0__.YCodeCell),
/* harmony export */   "YDocument": () => (/* reexport safe */ _ymodels__WEBPACK_IMPORTED_MODULE_0__.YDocument),
/* harmony export */   "YFile": () => (/* reexport safe */ _ymodels__WEBPACK_IMPORTED_MODULE_0__.YFile),
/* harmony export */   "YMarkdownCell": () => (/* reexport safe */ _ymodels__WEBPACK_IMPORTED_MODULE_0__.YMarkdownCell),
/* harmony export */   "YNotebook": () => (/* reexport safe */ _ymodels__WEBPACK_IMPORTED_MODULE_0__.YNotebook),
/* harmony export */   "YRawCell": () => (/* reexport safe */ _ymodels__WEBPACK_IMPORTED_MODULE_0__.YRawCell),
/* harmony export */   "convertYMapEventToMapChange": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_1__.convertYMapEventToMapChange),
/* harmony export */   "createCellModelFromSharedType": () => (/* reexport safe */ _ymodels__WEBPACK_IMPORTED_MODULE_0__.createCellModelFromSharedType),
/* harmony export */   "createMutex": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_1__.createMutex),
/* harmony export */   "createStandaloneCell": () => (/* reexport safe */ _ymodels__WEBPACK_IMPORTED_MODULE_0__.createStandaloneCell)
/* harmony export */ });
/* harmony import */ var _ymodels__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./ymodels */ "../../packages/shared-models/lib/ymodels.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./utils */ "../../packages/shared-models/lib/utils.js");
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module shared-models
 */





/***/ }),

/***/ "../../packages/shared-models/lib/utils.js":
/*!*************************************************!*\
  !*** ../../packages/shared-models/lib/utils.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "convertYMapEventToMapChange": () => (/* binding */ convertYMapEventToMapChange),
/* harmony export */   "createMutex": () => (/* binding */ createMutex)
/* harmony export */ });
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
function convertYMapEventToMapChange(event) {
    let changes = new Map();
    event.changes.keys.forEach((event, key) => {
        changes.set(key, {
            action: event.action,
            oldValue: event.oldValue,
            newValue: this.ymeta.get(key)
        });
    });
    return changes;
}
/**
 * Creates a mutual exclude function with the following property:
 *
 * ```js
 * const mutex = createMutex()
 * mutex(() => {
 *   // This function is immediately executed
 *   mutex(() => {
 *     // This function is not executed, as the mutex is already active.
 *   })
 * })
 * ```
 */
const createMutex = () => {
    let token = true;
    return (f) => {
        if (token) {
            token = false;
            try {
                f();
            }
            finally {
                token = true;
            }
        }
    };
};


/***/ }),

/***/ "../../packages/shared-models/lib/ymodels.js":
/*!***************************************************!*\
  !*** ../../packages/shared-models/lib/ymodels.js ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "YBaseCell": () => (/* binding */ YBaseCell),
/* harmony export */   "YCodeCell": () => (/* binding */ YCodeCell),
/* harmony export */   "YDocument": () => (/* binding */ YDocument),
/* harmony export */   "YFile": () => (/* binding */ YFile),
/* harmony export */   "YMarkdownCell": () => (/* binding */ YMarkdownCell),
/* harmony export */   "YNotebook": () => (/* binding */ YNotebook),
/* harmony export */   "YRawCell": () => (/* binding */ YRawCell),
/* harmony export */   "createCellModelFromSharedType": () => (/* binding */ createCellModelFromSharedType),
/* harmony export */   "createStandaloneCell": () => (/* binding */ createStandaloneCell),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var y_protocols_awareness__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! y-protocols/awareness */ "../../node_modules/y-protocols/awareness.js");
/* harmony import */ var yjs__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! yjs */ "webpack/sharing/consume/default/yjs/yjs");
/* harmony import */ var yjs__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(yjs__WEBPACK_IMPORTED_MODULE_3__);
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/




const deepCopy = (o) => JSON.parse(JSON.stringify(o));
class YDocument {
    constructor() {
        this.isDisposed = false;
        this.ydoc = new yjs__WEBPACK_IMPORTED_MODULE_3__.Doc();
        this.source = this.ydoc.getText('source');
        this.ystate = this.ydoc.getMap('state');
        this.undoManager = new yjs__WEBPACK_IMPORTED_MODULE_3__.UndoManager([this.source], {
            trackedOrigins: new Set([this])
        });
        this.awareness = new y_protocols_awareness__WEBPACK_IMPORTED_MODULE_2__.Awareness(this.ydoc);
        this._changed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
    }
    /**
     * Perform a transaction. While the function f is called, all changes to the shared
     * document are bundled into a single event.
     */
    transact(f, undoable = true) {
        this.ydoc.transact(f, undoable ? this : null);
    }
    /**
     * Dispose of the resources.
     */
    dispose() {
        this.isDisposed = true;
        this.ydoc.destroy();
    }
    /**
     * Whether the object can undo changes.
     */
    canUndo() {
        return this.undoManager.undoStack.length > 0;
    }
    /**
     * Whether the object can redo changes.
     */
    canRedo() {
        return this.undoManager.redoStack.length > 0;
    }
    /**
     * Undo an operation.
     */
    undo() {
        this.undoManager.undo();
    }
    /**
     * Redo an operation.
     */
    redo() {
        this.undoManager.redo();
    }
    /**
     * Clear the change stack.
     */
    clearUndoHistory() {
        this.undoManager.clear();
    }
    /**
     * The changed signal.
     */
    get changed() {
        return this._changed;
    }
}
class YFile extends YDocument {
    constructor() {
        super();
        /**
         * Handle a change to the ymodel.
         */
        this._modelObserver = (event) => {
            const changes = {};
            changes.sourceChange = event.changes.delta;
            this._changed.emit(changes);
        };
        /**
         * Handle a change to the ystate.
         */
        this._onStateChanged = (event) => {
            const stateChange = [];
            event.keysChanged.forEach(key => {
                const change = event.changes.keys.get(key);
                if (change) {
                    stateChange.push({
                        name: key,
                        oldValue: change.oldValue,
                        newValue: this.ystate.get(key)
                    });
                }
            });
            this._changed.emit({ stateChange });
        };
        this.ysource = this.ydoc.getText('source');
        this.ysource.observe(this._modelObserver);
        this.ystate.observe(this._onStateChanged);
    }
    /**
     * Dispose of the resources.
     */
    dispose() {
        this.ysource.unobserve(this._modelObserver);
        this.ystate.unobserve(this._onStateChanged);
    }
    static create() {
        const model = new YFile();
        return model;
    }
    /**
     * Gets cell's source.
     *
     * @returns Cell's source.
     */
    getSource() {
        return this.ysource.toString();
    }
    /**
     * Sets cell's source.
     *
     * @param value: New source.
     */
    setSource(value) {
        this.transact(() => {
            const ytext = this.ysource;
            ytext.delete(0, ytext.length);
            ytext.insert(0, value);
        });
    }
    /**
     * Replace content from `start' to `end` with `value`.
     *
     * @param start: The start index of the range to replace (inclusive).
     *
     * @param end: The end index of the range to replace (exclusive).
     *
     * @param value: New source (optional).
     */
    updateSource(start, end, value = '') {
        this.transact(() => {
            const ysource = this.ysource;
            // insert and then delete.
            // This ensures that the cursor position is adjusted after the replaced content.
            ysource.insert(start, value);
            ysource.delete(start + value.length, end - start);
        });
    }
}
/**
 * Shared implementation of the Shared Document types.
 *
 * Shared cells can be inserted into a SharedNotebook.
 * Shared cells only start emitting events when they are connected to a SharedNotebook.
 *
 * "Standalone" cells must not be inserted into a (Shared)Notebook.
 * Standalone cells emit events immediately after they have been created, but they must not
 * be included into a (Shared)Notebook.
 */
class YNotebook extends YDocument {
    constructor(options) {
        super();
        /**
         * Handle a change to the list of cells.
         */
        this._onYCellsChanged = (event) => {
            // update the type⇔cell mapping by iterating through the added/removed types
            event.changes.added.forEach(item => {
                const type = item.content.type;
                if (!this._ycellMapping.has(type)) {
                    this._ycellMapping.set(type, createCellModelFromSharedType(type));
                }
                const cell = this._ycellMapping.get(type);
                cell._notebook = this;
                if (!this.disableDocumentWideUndoRedo) {
                    cell._undoManager = this.undoManager;
                }
                else {
                    cell._undoManager = new yjs__WEBPACK_IMPORTED_MODULE_3__.UndoManager([cell.ymodel], {});
                }
            });
            event.changes.deleted.forEach(item => {
                const type = item.content.type;
                const model = this._ycellMapping.get(type);
                if (model) {
                    model.dispose();
                    this._ycellMapping.delete(type);
                }
            });
            let index = 0;
            // this reflects the event.changes.delta, but replaces the content of delta.insert with ycells
            const cellsChange = [];
            event.changes.delta.forEach((d) => {
                if (d.insert != null) {
                    const insertedCells = d.insert.map((ycell) => this._ycellMapping.get(ycell));
                    cellsChange.push({ insert: insertedCells });
                    this.cells.splice(index, 0, ...insertedCells);
                    index += d.insert.length;
                }
                else if (d.delete != null) {
                    cellsChange.push(d);
                    this.cells.splice(index, d.delete);
                }
                else if (d.retain != null) {
                    cellsChange.push(d);
                    index += d.retain;
                }
            });
            this._changed.emit({
                cellsChange: cellsChange
            });
        };
        /**
         * Handle a change to the ystate.
         */
        this._onMetaChanged = (event) => {
            if (event.keysChanged.has('metadata')) {
                const change = event.changes.keys.get('metadata');
                const metadataChange = {
                    oldValue: (change === null || change === void 0 ? void 0 : change.oldValue) ? change.oldValue : undefined,
                    newValue: this.getMetadata()
                };
                this._changed.emit({ metadataChange });
            }
            if (event.keysChanged.has('nbformat')) {
                const change = event.changes.keys.get('nbformat');
                const nbformatChanged = {
                    key: 'nbformat',
                    oldValue: (change === null || change === void 0 ? void 0 : change.oldValue) ? change.oldValue : undefined,
                    newValue: this.nbformat
                };
                this._changed.emit({ nbformatChanged });
            }
            if (event.keysChanged.has('nbformat_minor')) {
                const change = event.changes.keys.get('nbformat_minor');
                const nbformatChanged = {
                    key: 'nbformat_minor',
                    oldValue: (change === null || change === void 0 ? void 0 : change.oldValue) ? change.oldValue : undefined,
                    newValue: this.nbformat_minor
                };
                this._changed.emit({ nbformatChanged });
            }
        };
        /**
         * Handle a change to the ystate.
         */
        this._onStateChanged = (event) => {
            const stateChange = [];
            event.keysChanged.forEach(key => {
                const change = event.changes.keys.get(key);
                if (change) {
                    stateChange.push({
                        name: key,
                        oldValue: change.oldValue,
                        newValue: this.ystate.get(key)
                    });
                }
            });
            this._changed.emit({ stateChange });
        };
        this.ycells = this.ydoc.getArray('cells');
        this.ymeta = this.ydoc.getMap('meta');
        this.ymodel = this.ydoc.getMap('model');
        this.undoManager = new yjs__WEBPACK_IMPORTED_MODULE_3__.UndoManager([this.ycells], {
            trackedOrigins: new Set([this])
        });
        this._ycellMapping = new Map();
        this._disableDocumentWideUndoRedo = options.disableDocumentWideUndoRedo;
        this.ycells.observe(this._onYCellsChanged);
        this.cells = this.ycells.toArray().map(ycell => {
            if (!this._ycellMapping.has(ycell)) {
                this._ycellMapping.set(ycell, createCellModelFromSharedType(ycell));
            }
            return this._ycellMapping.get(ycell);
        });
        this.ymeta.observe(this._onMetaChanged);
        this.ystate.observe(this._onStateChanged);
    }
    get nbformat() {
        return this.ymeta.get('nbformat');
    }
    set nbformat(value) {
        this.transact(() => {
            this.ymeta.set('nbformat', value);
        }, false);
    }
    get nbformat_minor() {
        return this.ymeta.get('nbformat_minor');
    }
    set nbformat_minor(value) {
        this.transact(() => {
            this.ymeta.set('nbformat_minor', value);
        }, false);
    }
    /**
     * Dispose of the resources.
     */
    dispose() {
        this.ycells.unobserve(this._onYCellsChanged);
        this.ymeta.unobserve(this._onMetaChanged);
        this.ystate.unobserve(this._onStateChanged);
    }
    /**
     * Get a shared cell by index.
     *
     * @param index: Cell's position.
     *
     * @returns The requested shared cell.
     */
    getCell(index) {
        return this.cells[index];
    }
    /**
     * Insert a shared cell into a specific position.
     *
     * @param index: Cell's position.
     *
     * @param cell: Cell to insert.
     */
    insertCell(index, cell) {
        this.insertCells(index, [cell]);
    }
    /**
     * Insert a list of shared cells into a specific position.
     *
     * @param index: Position to insert the cells.
     *
     * @param cells: Array of shared cells to insert.
     */
    insertCells(index, cells) {
        cells.forEach(cell => {
            this._ycellMapping.set(cell.ymodel, cell);
            if (!this.disableDocumentWideUndoRedo) {
                cell.undoManager = this.undoManager;
            }
        });
        this.transact(() => {
            this.ycells.insert(index, cells.map(cell => cell.ymodel));
        });
    }
    /**
     * Move a cell.
     *
     * @param fromIndex: Index of the cell to move.
     *
     * @param toIndex: New position of the cell.
     */
    moveCell(fromIndex, toIndex) {
        this.transact(() => {
            const fromCell = this.getCell(fromIndex).clone();
            this.deleteCell(fromIndex);
            this.insertCell(toIndex, fromCell);
        });
    }
    /**
     * Remove a cell.
     *
     * @param index: Index of the cell to remove.
     */
    deleteCell(index) {
        this.deleteCellRange(index, index + 1);
    }
    /**
     * Remove a range of cells.
     *
     * @param from: The start index of the range to remove (inclusive).
     *
     * @param to: The end index of the range to remove (exclusive).
     */
    deleteCellRange(from, to) {
        this.transact(() => {
            this.ycells.delete(from, to - from);
        });
    }
    /**
     * Returns the metadata associated with the notebook.
     *
     * @returns Notebook's metadata.
     */
    getMetadata() {
        const meta = this.ymeta.get('metadata');
        return meta ? deepCopy(meta) : {};
    }
    /**
     * Sets the metadata associated with the notebook.
     *
     * @param metadata: Notebook's metadata.
     */
    setMetadata(value) {
        this.ymeta.set('metadata', deepCopy(value));
    }
    /**
     * Updates the metadata associated with the notebook.
     *
     * @param value: Metadata's attribute to update.
     */
    updateMetadata(value) {
        // TODO: Maybe modify only attributes instead of replacing the whole metadata?
        this.ymeta.set('metadata', Object.assign({}, this.getMetadata(), value));
    }
    /**
     * Create a new YNotebook.
     */
    static create(disableDocumentWideUndoRedo) {
        const model = new YNotebook({ disableDocumentWideUndoRedo });
        return model;
    }
    /**
     * Wether the the undo/redo logic should be
     * considered on the full document across all cells.
     *
     * @returns The disableDocumentWideUndoRedo setting.
     */
    get disableDocumentWideUndoRedo() {
        return this._disableDocumentWideUndoRedo;
    }
}
/**
 * Create a new shared cell model given the YJS shared type.
 */
const createCellModelFromSharedType = (type) => {
    switch (type.get('cell_type')) {
        case 'code':
            return new YCodeCell(type);
        case 'markdown':
            return new YMarkdownCell(type);
        case 'raw':
            return new YRawCell(type);
        default:
            throw new Error('Found unknown cell type');
    }
};
/**
 * Create a new standalone cell given the type.
 */
const createStandaloneCell = (cellType, id) => {
    switch (cellType) {
        case 'markdown':
            return YMarkdownCell.createStandalone(id);
        case 'code':
            return YCodeCell.createStandalone(id);
        default:
            // raw
            return YRawCell.createStandalone(id);
    }
};
class YBaseCell {
    constructor(ymodel) {
        /**
         * The notebook that this cell belongs to.
         */
        this._notebook = null;
        /**
         * Whether the cell is standalone or not.
         *
         * If the cell is standalone. It cannot be
         * inserted into a YNotebook because the Yjs model is already
         * attached to an anonymous Y.Doc instance.
         */
        this.isStandalone = false;
        /**
         * Handle a change to the ymodel.
         */
        this._modelObserver = (events) => {
            const changes = {};
            const sourceEvent = events.find(event => event.target === this.ymodel.get('source'));
            if (sourceEvent) {
                changes.sourceChange = sourceEvent.changes.delta;
            }
            const outputEvent = events.find(event => event.target === this.ymodel.get('outputs'));
            if (outputEvent) {
                changes.outputsChange = outputEvent.changes.delta;
            }
            const modelEvent = events.find(event => event.target === this.ymodel);
            if (modelEvent && modelEvent.keysChanged.has('metadata')) {
                const change = modelEvent.changes.keys.get('metadata');
                changes.metadataChange = {
                    oldValue: (change === null || change === void 0 ? void 0 : change.oldValue) ? change.oldValue : undefined,
                    newValue: this.getMetadata()
                };
            }
            if (modelEvent && modelEvent.keysChanged.has('execution_count')) {
                const change = modelEvent.changes.keys.get('execution_count');
                changes.executionCountChange = {
                    oldValue: change.oldValue,
                    newValue: this.ymodel.get('execution_count')
                };
            }
            // The model allows us to replace the complete source with a new string. We express this in the Delta format
            // as a replace of the complete string.
            const ysource = this.ymodel.get('source');
            if (modelEvent && modelEvent.keysChanged.has('source')) {
                changes.sourceChange = [
                    { delete: this._prevSourceLength },
                    { insert: ysource.toString() }
                ];
            }
            this._prevSourceLength = ysource.length;
            this._changed.emit(changes);
        };
        this.isDisposed = false;
        this._undoManager = null;
        this._changed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
        this.ymodel = ymodel;
        const ysource = ymodel.get('source');
        this._prevSourceLength = ysource ? ysource.length : 0;
        this.ymodel.observeDeep(this._modelObserver);
        this._awareness = null;
    }
    get ysource() {
        return this.ymodel.get('source');
    }
    get awareness() {
        var _a, _b, _c;
        return (_c = (_a = this._awareness) !== null && _a !== void 0 ? _a : (_b = this.notebook) === null || _b === void 0 ? void 0 : _b.awareness) !== null && _c !== void 0 ? _c : null;
    }
    /**
     * Perform a transaction. While the function f is called, all changes to the shared
     * document are bundled into a single event.
     */
    transact(f, undoable = true) {
        this.notebook && undoable
            ? this.notebook.transact(f)
            : this.ymodel.doc.transact(f, this);
    }
    /**
     * The notebook that this cell belongs to.
     */
    get undoManager() {
        var _a;
        if (!this.notebook) {
            return this._undoManager;
        }
        return ((_a = this.notebook) === null || _a === void 0 ? void 0 : _a.disableDocumentWideUndoRedo)
            ? this._undoManager
            : this.notebook.undoManager;
    }
    /**
     * Set the undoManager when adding new cells.
     */
    set undoManager(undoManager) {
        this._undoManager = undoManager;
    }
    /**
     * Undo an operation.
     */
    undo() {
        var _a;
        (_a = this.undoManager) === null || _a === void 0 ? void 0 : _a.undo();
    }
    /**
     * Redo an operation.
     */
    redo() {
        var _a;
        (_a = this.undoManager) === null || _a === void 0 ? void 0 : _a.redo();
    }
    /**
     * Whether the object can undo changes.
     */
    canUndo() {
        return !!this.undoManager && this.undoManager.undoStack.length > 0;
    }
    /**
     * Whether the object can redo changes.
     */
    canRedo() {
        return !!this.undoManager && this.undoManager.redoStack.length > 0;
    }
    /**
     * Clear the change stack.
     */
    clearUndoHistory() {
        var _a;
        (_a = this.undoManager) === null || _a === void 0 ? void 0 : _a.clear();
    }
    /**
     * The notebook that this cell belongs to.
     */
    get notebook() {
        return this._notebook;
    }
    /**
     * Create a new YRawCell that can be inserted into a YNotebook
     */
    static create(id = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.UUID.uuid4()) {
        const ymodel = new yjs__WEBPACK_IMPORTED_MODULE_3__.Map();
        const ysource = new yjs__WEBPACK_IMPORTED_MODULE_3__.Text();
        ymodel.set('source', ysource);
        ymodel.set('metadata', {});
        ymodel.set('cell_type', this.prototype.cell_type);
        ymodel.set('id', id);
        return new this(ymodel);
    }
    /**
     * Create a new YRawCell that works standalone. It cannot be
     * inserted into a YNotebook because the Yjs model is already
     * attached to an anonymous Y.Doc instance.
     */
    static createStandalone(id) {
        const cell = this.create(id);
        cell.isStandalone = true;
        const doc = new yjs__WEBPACK_IMPORTED_MODULE_3__.Doc();
        doc.getArray().insert(0, [cell.ymodel]);
        cell._awareness = new y_protocols_awareness__WEBPACK_IMPORTED_MODULE_2__.Awareness(doc);
        cell._undoManager = new yjs__WEBPACK_IMPORTED_MODULE_3__.UndoManager([cell.ymodel], {
            trackedOrigins: new Set([cell])
        });
        return cell;
    }
    /**
     * Clone the cell.
     *
     * @todo clone should only be available in the specific implementations i.e. ISharedCodeCell
     */
    clone() {
        const ymodel = new yjs__WEBPACK_IMPORTED_MODULE_3__.Map();
        const ysource = new yjs__WEBPACK_IMPORTED_MODULE_3__.Text(this.getSource());
        ymodel.set('source', ysource);
        ymodel.set('metadata', this.getMetadata());
        ymodel.set('cell_type', this.cell_type);
        ymodel.set('id', this.getId());
        const Self = this.constructor;
        const clone = new Self(ymodel);
        // TODO The assignment of the undoManager does not work for a clone.
        // See https://github.com/jupyterlab/jupyterlab/issues/11035
        clone._undoManager = this.undoManager;
        return clone;
    }
    /**
     * The changed signal.
     */
    get changed() {
        return this._changed;
    }
    /**
     * Dispose of the resources.
     */
    dispose() {
        this.ymodel.unobserveDeep(this._modelObserver);
        if (this._awareness) {
            this._awareness.destroy();
        }
        if (!this.notebook && this._undoManager) {
            this._undoManager.destroy();
        }
    }
    /**
     * Gets the cell attachments.
     *
     * @returns The cell attachments.
     */
    getAttachments() {
        return this.ymodel.get('attachments');
    }
    /**
     * Sets the cell attachments
     *
     * @param attachments: The cell attachments.
     */
    setAttachments(attachments) {
        this.transact(() => {
            if (attachments == null) {
                this.ymodel.delete('attachments');
            }
            else {
                this.ymodel.set('attachments', attachments);
            }
        });
    }
    /**
     * Get cell id.
     *
     * @returns Cell id
     */
    getId() {
        return this.ymodel.get('id');
    }
    /**
     * Gets cell's source.
     *
     * @returns Cell's source.
     */
    getSource() {
        return this.ymodel.get('source').toString();
    }
    /**
     * Sets cell's source.
     *
     * @param value: New source.
     */
    setSource(value) {
        const ytext = this.ymodel.get('source');
        this.transact(() => {
            ytext.delete(0, ytext.length);
            ytext.insert(0, value);
        });
        // @todo Do we need proper replace semantic? This leads to issues in editor bindings because they don't switch source.
        // this.ymodel.set('source', new Y.Text(value));
    }
    /**
     * Replace content from `start' to `end` with `value`.
     *
     * @param start: The start index of the range to replace (inclusive).
     *
     * @param end: The end index of the range to replace (exclusive).
     *
     * @param value: New source (optional).
     */
    updateSource(start, end, value = '') {
        this.transact(() => {
            const ysource = this.ysource;
            // insert and then delete.
            // This ensures that the cursor position is adjusted after the replaced content.
            ysource.insert(start, value);
            ysource.delete(start + value.length, end - start);
        });
    }
    /**
     * The type of the cell.
     */
    get cell_type() {
        throw new Error('A YBaseCell must not be constructed');
    }
    /**
     * Returns the metadata associated with the notebook.
     *
     * @returns Notebook's metadata.
     */
    getMetadata() {
        return deepCopy(this.ymodel.get('metadata'));
    }
    /**
     * Sets the metadata associated with the notebook.
     *
     * @param metadata: Notebook's metadata.
     */
    setMetadata(value) {
        this.transact(() => {
            this.ymodel.set('metadata', deepCopy(value));
        });
    }
    /**
     * Serialize the model to JSON.
     */
    toJSON() {
        return {
            id: this.getId(),
            cell_type: this.cell_type,
            source: this.getSource(),
            metadata: this.getMetadata()
        };
    }
}
class YCodeCell extends YBaseCell {
    /**
     * The type of the cell.
     */
    get cell_type() {
        return 'code';
    }
    /**
     * The code cell's prompt number. Will be null if the cell has not been run.
     */
    get execution_count() {
        return this.ymodel.get('execution_count');
    }
    /**
     * The code cell's prompt number. Will be null if the cell has not been run.
     */
    set execution_count(count) {
        this.transact(() => {
            this.ymodel.set('execution_count', count);
        });
    }
    /**
     * Execution, display, or stream outputs.
     */
    getOutputs() {
        return deepCopy(this.ymodel.get('outputs').toArray());
    }
    /**
     * Replace all outputs.
     */
    setOutputs(outputs) {
        const youtputs = this.ymodel.get('outputs');
        this.transact(() => {
            youtputs.delete(0, youtputs.length);
            youtputs.insert(0, outputs);
        }, false);
    }
    /**
     * Replace content from `start' to `end` with `outputs`.
     *
     * @param start: The start index of the range to replace (inclusive).
     *
     * @param end: The end index of the range to replace (exclusive).
     *
     * @param outputs: New outputs (optional).
     */
    updateOutputs(start, end, outputs = []) {
        const youtputs = this.ymodel.get('outputs');
        const fin = end < youtputs.length ? end - start : youtputs.length - start;
        this.transact(() => {
            youtputs.delete(start, fin);
            youtputs.insert(start, outputs);
        }, false);
    }
    /**
     * Create a new YCodeCell that can be inserted into a YNotebook
     */
    static create(id) {
        const cell = super.create(id);
        cell.ymodel.set('execution_count', 0); // for some default value
        cell.ymodel.set('outputs', new yjs__WEBPACK_IMPORTED_MODULE_3__.Array());
        return cell;
    }
    /**
     * Create a new YCodeCell that works standalone. It cannot be
     * inserted into a YNotebook because the Yjs model is already
     * attached to an anonymous Y.Doc instance.
     */
    static createStandalone(id) {
        const cell = super.createStandalone(id);
        cell.ymodel.set('execution_count', null); // for some default value
        cell.ymodel.set('outputs', new yjs__WEBPACK_IMPORTED_MODULE_3__.Array());
        return cell;
    }
    /**
     * Create a new YCodeCell that can be inserted into a YNotebook
     *
     * @todo clone should only be available in the specific implementations i.e. ISharedCodeCell
     */
    clone() {
        const cell = super.clone();
        const youtputs = new yjs__WEBPACK_IMPORTED_MODULE_3__.Array();
        youtputs.insert(0, this.getOutputs());
        cell.ymodel.set('execution_count', this.execution_count); // for some default value
        cell.ymodel.set('outputs', youtputs);
        return cell;
    }
    /**
     * Serialize the model to JSON.
     */
    toJSON() {
        return {
            id: this.getId(),
            cell_type: 'code',
            source: this.getSource(),
            metadata: this.getMetadata(),
            outputs: this.getOutputs(),
            execution_count: this.execution_count
        };
    }
}
class YRawCell extends YBaseCell {
    /**
     * Create a new YRawCell that can be inserted into a YNotebook
     */
    static create(id) {
        return super.create(id);
    }
    /**
     * Create a new YRawCell that works standalone. It cannot be
     * inserted into a YNotebook because the Yjs model is already
     * attached to an anonymous Y.Doc instance.
     */
    static createStandalone(id) {
        return super.createStandalone(id);
    }
    /**
     * String identifying the type of cell.
     */
    get cell_type() {
        return 'raw';
    }
    /**
     * Serialize the model to JSON.
     */
    toJSON() {
        return {
            id: this.getId(),
            cell_type: 'raw',
            source: this.getSource(),
            metadata: this.getMetadata(),
            attachments: this.getAttachments()
        };
    }
}
class YMarkdownCell extends YBaseCell {
    /**
     * Create a new YMarkdownCell that can be inserted into a YNotebook
     */
    static create(id) {
        return super.create(id);
    }
    /**
     * Create a new YMarkdownCell that works standalone. It cannot be
     * inserted into a YNotebook because the Yjs model is already
     * attached to an anonymous Y.Doc instance.
     */
    static createStandalone(id) {
        return super.createStandalone(id);
    }
    /**
     * String identifying the type of cell.
     */
    get cell_type() {
        return 'markdown';
    }
    /**
     * Serialize the model to JSON.
     */
    toJSON() {
        return {
            id: this.getId(),
            cell_type: 'markdown',
            source: this.getSource(),
            metadata: this.getMetadata(),
            attachments: this.getAttachments()
        };
    }
}
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (YNotebook);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfc2hhcmVkLW1vZGVsc19saWJfaW5kZXhfanMuYTVlNDg4N2IyMmQyZGUwMGNhMjYuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBOzs7K0VBRytFO0FBQy9FOzs7R0FHRztBQUVtQjtBQUNJO0FBQ0Y7Ozs7Ozs7Ozs7Ozs7Ozs7QUNYeEI7OzsrRUFHK0U7QUFLeEUsU0FBUywyQkFBMkIsQ0FDekMsS0FBdUI7SUFFdkIsSUFBSSxPQUFPLEdBQUcsSUFBSSxHQUFHLEVBQUUsQ0FBQztJQUN4QixLQUFLLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxPQUFPLENBQUMsQ0FBQyxLQUFLLEVBQUUsR0FBRyxFQUFFLEVBQUU7UUFDeEMsT0FBTyxDQUFDLEdBQUcsQ0FBQyxHQUFHLEVBQUU7WUFDZixNQUFNLEVBQUUsS0FBSyxDQUFDLE1BQU07WUFDcEIsUUFBUSxFQUFFLEtBQUssQ0FBQyxRQUFRO1lBQ3hCLFFBQVEsRUFBRSxJQUFJLENBQUMsS0FBSyxDQUFDLEdBQUcsQ0FBQyxHQUFHLENBQUM7U0FDOUIsQ0FBQyxDQUFDO0lBQ0wsQ0FBQyxDQUFDLENBQUM7SUFDSCxPQUFPLE9BQU8sQ0FBQztBQUNqQixDQUFDO0FBRUQ7Ozs7Ozs7Ozs7OztHQVlHO0FBQ0ksTUFBTSxXQUFXLEdBQUcsR0FBOEIsRUFBRTtJQUN6RCxJQUFJLEtBQUssR0FBRyxJQUFJLENBQUM7SUFDakIsT0FBTyxDQUFDLENBQU0sRUFBUSxFQUFFO1FBQ3RCLElBQUksS0FBSyxFQUFFO1lBQ1QsS0FBSyxHQUFHLEtBQUssQ0FBQztZQUNkLElBQUk7Z0JBQ0YsQ0FBQyxFQUFFLENBQUM7YUFDTDtvQkFBUztnQkFDUixLQUFLLEdBQUcsSUFBSSxDQUFDO2FBQ2Q7U0FDRjtJQUNILENBQUMsQ0FBQztBQUNKLENBQUMsQ0FBQzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQy9DRjs7OytFQUcrRTtBQUd0QztBQUNXO0FBQ0Y7QUFDekI7QUFJekIs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QixXQUFXLEVBQUUsSUFBSSxDQUFDLGNBQWMsRUFBRTtTQUNuQyxDQUFDO0lBQ0osQ0FBQztDQUNGO0FBRU0sTUFBTSxhQUNYLFNBQVEsU0FBeUM7SUFHakQ7O09BRUc7SUFDSSxNQUFNLENBQUMsTUFBTSxDQUFDLEVBQVc7UUFDOUIsT0FBTyxLQUFLLENBQUMsTUFBTSxDQUFDLEVBQUUsQ0FBUSxDQUFDO0lBQ2pDLENBQUM7SUFFRDs7OztPQUlHO0lBQ0ksTUFBTSxDQUFDLGdCQUFnQixDQUFDLEVBQVc7UUFDeEMsT0FBTyxLQUFLLENBQUMsZ0JBQWdCLENBQUMsRUFBRSxDQUFRLENBQUM7SUFDM0MsQ0FBQztJQUVEOztPQUVHO0lBQ0gsSUFBSSxTQUFTO1FBQ1gsT0FBTyxVQUFVLENBQUM7SUFDcEIsQ0FBQztJQUVEOztPQUVHO0lBQ0gsTUFBTTtRQUNKLE9BQU87WUFDTCxFQUFFLEVBQUUsSUFBSSxDQUFDLEtBQUssRUFBRTtZQUNoQixTQUFTLEVBQUUsVUFBVTtZQUNyQixNQUFNLEVBQUUsSUFBSSxDQUFDLFNBQVMsRUFBRTtZQUN4QixRQUFRLEVBQUUsSUFBSSxDQUFDLFdBQVcsRUFBRTtZQUM1QixXQUFXLEVBQUUsSUFBSSxDQUFDLGNBQWMsRUFBRTtTQUNuQyxDQUFDO0lBQ0osQ0FBQztDQUNGO0FBRUQsaUVBQWUsU0FBUyxFQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3NoYXJlZC1tb2RlbHMvc3JjL2luZGV4LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9zaGFyZWQtbW9kZWxzL3NyYy91dGlscy50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvc2hhcmVkLW1vZGVscy9zcmMveW1vZGVscy50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvKiAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxufCBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbnwgRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbnwtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIHNoYXJlZC1tb2RlbHNcbiAqL1xuXG5leHBvcnQgKiBmcm9tICcuL2FwaSc7XG5leHBvcnQgKiBmcm9tICcuL3ltb2RlbHMnO1xuZXhwb3J0ICogZnJvbSAnLi91dGlscyc7XG4iLCIvKiAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxufCBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbnwgRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbnwtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuaW1wb3J0ICogYXMgWSBmcm9tICd5anMnO1xuaW1wb3J0ICogYXMgbW9kZWxzIGZyb20gJy4vYXBpJztcblxuZXhwb3J0IGZ1bmN0aW9uIGNvbnZlcnRZTWFwRXZlbnRUb01hcENoYW5nZShcbiAgZXZlbnQ6IFkuWU1hcEV2ZW50PGFueT5cbik6IG1vZGVscy5NYXBDaGFuZ2Uge1xuICBsZXQgY2hhbmdlcyA9IG5ldyBNYXAoKTtcbiAgZXZlbnQuY2hhbmdlcy5rZXlzLmZvckVhY2goKGV2ZW50LCBrZXkpID0+IHtcbiAgICBjaGFuZ2VzLnNldChrZXksIHtcbiAgICAgIGFjdGlvbjogZXZlbnQuYWN0aW9uLFxuICAgICAgb2xkVmFsdWU6IGV2ZW50Lm9sZFZhbHVlLFxuICAgICAgbmV3VmFsdWU6IHRoaXMueW1ldGEuZ2V0KGtleSlcbiAgICB9KTtcbiAgfSk7XG4gIHJldHVybiBjaGFuZ2VzO1xufVxuXG4vKipcbiAqIENyZWF0ZXMgYSBtdXR1YWwgZXhjbHVkZSBmdW5jdGlvbiB3aXRoIHRoZSBmb2xsb3dpbmcgcHJvcGVydHk6XG4gKlxuICogYGBganNcbiAqIGNvbnN0IG11dGV4ID0gY3JlYXRlTXV0ZXgoKVxuICogbXV0ZXgoKCkgPT4ge1xuICogICAvLyBUaGlzIGZ1bmN0aW9uIGlzIGltbWVkaWF0ZWx5IGV4ZWN1dGVkXG4gKiAgIG11dGV4KCgpID0+IHtcbiAqICAgICAvLyBUaGlzIGZ1bmN0aW9uIGlzIG5vdCBleGVjdXRlZCwgYXMgdGhlIG11dGV4IGlzIGFscmVhZHkgYWN0aXZlLlxuICogICB9KVxuICogfSlcbiAqIGBgYFxuICovXG5leHBvcnQgY29uc3QgY3JlYXRlTXV0ZXggPSAoKTogKChmOiAoKSA9PiB2b2lkKSA9PiB2b2lkKSA9PiB7XG4gIGxldCB0b2tlbiA9IHRydWU7XG4gIHJldHVybiAoZjogYW55KTogdm9pZCA9PiB7XG4gICAgaWYgKHRva2VuKSB7XG4gICAgICB0b2tlbiA9IGZhbHNlO1xuICAgICAgdHJ5IHtcbiAgICAgICAgZigpO1xuICAgICAgfSBmaW5hbGx5IHtcbiAgICAgICAgdG9rZW4gPSB0cnVlO1xuICAgICAgfVxuICAgIH1cbiAgfTtcbn07XG4iLCIvKiAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxufCBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbnwgRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbnwtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cblxuaW1wb3J0ICogYXMgbmJmb3JtYXQgZnJvbSAnQGp1cHl0ZXJsYWIvbmJmb3JtYXQnO1xuaW1wb3J0IHsgVVVJRCB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IElTaWduYWwsIFNpZ25hbCB9IGZyb20gJ0BsdW1pbm8vc2lnbmFsaW5nJztcbmltcG9ydCB7IEF3YXJlbmVzcyB9IGZyb20gJ3ktcHJvdG9jb2xzL2F3YXJlbmVzcyc7XG5pbXBvcnQgKiBhcyBZIGZyb20gJ3lqcyc7XG5pbXBvcnQgKiBhcyBtb2RlbHMgZnJvbSAnLi9hcGknO1xuaW1wb3J0IHsgRGVsdGEsIElTaGFyZWROb3RlYm9vayB9IGZyb20gJy4vYXBpJztcblxuY29uc3QgZGVlcENvcHkgPSAobzogYW55KSA9PiBKU09OLnBhcnNlKEpTT04uc3RyaW5naWZ5KG8pKTtcblxuLyoqXG4gKiBBYnN0cmFjdCBpbnRlcmZhY2UgdG8gZGVmaW5lIFNoYXJlZCBNb2RlbHMgdGhhdCBjYW4gYmUgYm91bmQgdG8gYSB0ZXh0IGVkaXRvciB1c2luZyBhbnkgZXhpc3RpbmdcbiAqIFlqcy1iYXNlZCBlZGl0b3IgYmluZGluZy5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJWVRleHQgZXh0ZW5kcyBtb2RlbHMuSVNoYXJlZFRleHQge1xuICByZWFkb25seSB5c291cmNlOiBZLlRleHQ7XG4gIHJlYWRvbmx5IGF3YXJlbmVzczogQXdhcmVuZXNzIHwgbnVsbDtcbiAgcmVhZG9ubHkgdW5kb01hbmFnZXI6IFkuVW5kb01hbmFnZXIgfCBudWxsO1xufVxuXG5leHBvcnQgdHlwZSBZQ2VsbFR5cGUgPSBZUmF3Q2VsbCB8IFlDb2RlQ2VsbCB8IFlNYXJrZG93bkNlbGw7XG5cbmV4cG9ydCBjbGFzcyBZRG9jdW1lbnQ8VD4gaW1wbGVtZW50cyBtb2RlbHMuSVNoYXJlZERvY3VtZW50IHtcbiAgLyoqXG4gICAqIFBlcmZvcm0gYSB0cmFuc2FjdGlvbi4gV2hpbGUgdGhlIGZ1bmN0aW9uIGYgaXMgY2FsbGVkLCBhbGwgY2hhbmdlcyB0byB0aGUgc2hhcmVkXG4gICAqIGRvY3VtZW50IGFyZSBidW5kbGVkIGludG8gYSBzaW5nbGUgZXZlbnQuXG4gICAqL1xuICB0cmFuc2FjdChmOiAoKSA9PiB2b2lkLCB1bmRvYWJsZSA9IHRydWUpOiB2b2lkIHtcbiAgICB0aGlzLnlkb2MudHJhbnNhY3QoZiwgdW5kb2FibGUgPyB0aGlzIDogbnVsbCk7XG4gIH1cbiAgLyoqXG4gICAqIERpc3Bvc2Ugb2YgdGhlIHJlc291cmNlcy5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgdGhpcy5pc0Rpc3Bvc2VkID0gdHJ1ZTtcbiAgICB0aGlzLnlkb2MuZGVzdHJveSgpO1xuICB9XG5cbiAgLyoqXG4gICAqIFdoZXRoZXIgdGhlIG9iamVjdCBjYW4gdW5kbyBjaGFuZ2VzLlxuICAgKi9cbiAgY2FuVW5kbygpOiBib29sZWFuIHtcbiAgICByZXR1cm4gdGhpcy51bmRvTWFuYWdlci51bmRvU3RhY2subGVuZ3RoID4gMDtcbiAgfVxuXG4gIC8qKlxuICAgKiBXaGV0aGVyIHRoZSBvYmplY3QgY2FuIHJlZG8gY2hhbmdlcy5cbiAgICovXG4gIGNhblJlZG8oKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMudW5kb01hbmFnZXIucmVkb1N0YWNrLmxlbmd0aCA+IDA7XG4gIH1cblxuICAvKipcbiAgICogVW5kbyBhbiBvcGVyYXRpb24uXG4gICAqL1xuICB1bmRvKCk6IHZvaWQge1xuICAgIHRoaXMudW5kb01hbmFnZXIudW5kbygpO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlZG8gYW4gb3BlcmF0aW9uLlxuICAgKi9cbiAgcmVkbygpOiB2b2lkIHtcbiAgICB0aGlzLnVuZG9NYW5hZ2VyLnJlZG8oKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBDbGVhciB0aGUgY2hhbmdlIHN0YWNrLlxuICAgKi9cbiAgY2xlYXJVbmRvSGlzdG9yeSgpOiB2b2lkIHtcbiAgICB0aGlzLnVuZG9NYW5hZ2VyLmNsZWFyKCk7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGNoYW5nZWQgc2lnbmFsLlxuICAgKi9cbiAgZ2V0IGNoYW5nZWQoKTogSVNpZ25hbDx0aGlzLCBUPiB7XG4gICAgcmV0dXJuIHRoaXMuX2NoYW5nZWQ7XG4gIH1cblxuICBwdWJsaWMgaXNEaXNwb3NlZCA9IGZhbHNlO1xuICBwdWJsaWMgeWRvYyA9IG5ldyBZLkRvYygpO1xuICBwdWJsaWMgc291cmNlID0gdGhpcy55ZG9jLmdldFRleHQoJ3NvdXJjZScpO1xuICBwdWJsaWMgeXN0YXRlOiBZLk1hcDxhbnk+ID0gdGhpcy55ZG9jLmdldE1hcCgnc3RhdGUnKTtcbiAgcHVibGljIHVuZG9NYW5hZ2VyID0gbmV3IFkuVW5kb01hbmFnZXIoW3RoaXMuc291cmNlXSwge1xuICAgIHRyYWNrZWRPcmlnaW5zOiBuZXcgU2V0KFt0aGlzXSlcbiAgfSk7XG4gIHB1YmxpYyBhd2FyZW5lc3MgPSBuZXcgQXdhcmVuZXNzKHRoaXMueWRvYyk7XG4gIHByb3RlY3RlZCBfY2hhbmdlZCA9IG5ldyBTaWduYWw8dGhpcywgVD4odGhpcyk7XG59XG5cbmV4cG9ydCBjbGFzcyBZRmlsZVxuICBleHRlbmRzIFlEb2N1bWVudDxtb2RlbHMuRmlsZUNoYW5nZT5cbiAgaW1wbGVtZW50cyBtb2RlbHMuSVNoYXJlZEZpbGUsIG1vZGVscy5JU2hhcmVkVGV4dCwgSVlUZXh0XG57XG4gIGNvbnN0cnVjdG9yKCkge1xuICAgIHN1cGVyKCk7XG4gICAgdGhpcy55c291cmNlLm9ic2VydmUodGhpcy5fbW9kZWxPYnNlcnZlcik7XG4gICAgdGhpcy55c3RhdGUub2JzZXJ2ZSh0aGlzLl9vblN0YXRlQ2hhbmdlZCk7XG4gIH1cblxuICAvKipcbiAgICogRGlzcG9zZSBvZiB0aGUgcmVzb3VyY2VzLlxuICAgKi9cbiAgZGlzcG9zZSgpOiB2b2lkIHtcbiAgICB0aGlzLnlzb3VyY2UudW5vYnNlcnZlKHRoaXMuX21vZGVsT2JzZXJ2ZXIpO1xuICAgIHRoaXMueXN0YXRlLnVub2JzZXJ2ZSh0aGlzLl9vblN0YXRlQ2hhbmdlZCk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGEgY2hhbmdlIHRvIHRoZSB5bW9kZWwuXG4gICAqL1xuICBwcml2YXRlIF9tb2RlbE9ic2VydmVyID0gKGV2ZW50OiBZLllUZXh0RXZlbnQpID0+IHtcbiAgICBjb25zdCBjaGFuZ2VzOiBtb2RlbHMuRmlsZUNoYW5nZSA9IHt9O1xuICAgIGNoYW5nZXMuc291cmNlQ2hhbmdlID0gZXZlbnQuY2hhbmdlcy5kZWx0YSBhcyBhbnk7XG4gICAgdGhpcy5fY2hhbmdlZC5lbWl0KGNoYW5nZXMpO1xuICB9O1xuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSBjaGFuZ2UgdG8gdGhlIHlzdGF0ZS5cbiAgICovXG4gIHByaXZhdGUgX29uU3RhdGVDaGFuZ2VkID0gKGV2ZW50OiBZLllNYXBFdmVudDxhbnk+KSA9PiB7XG4gICAgY29uc3Qgc3RhdGVDaGFuZ2U6IGFueSA9IFtdO1xuXG4gICAgZXZlbnQua2V5c0NoYW5nZWQuZm9yRWFjaChrZXkgPT4ge1xuICAgICAgY29uc3QgY2hhbmdlID0gZXZlbnQuY2hhbmdlcy5rZXlzLmdldChrZXkpO1xuICAgICAgaWYgKGNoYW5nZSkge1xuICAgICAgICBzdGF0ZUNoYW5nZS5wdXNoKHtcbiAgICAgICAgICBuYW1lOiBrZXksXG4gICAgICAgICAgb2xkVmFsdWU6IGNoYW5nZS5vbGRWYWx1ZSxcbiAgICAgICAgICBuZXdWYWx1ZTogdGhpcy55c3RhdGUuZ2V0KGtleSlcbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICB0aGlzLl9jaGFuZ2VkLmVtaXQoeyBzdGF0ZUNoYW5nZSB9KTtcbiAgfTtcblxuICBwdWJsaWMgc3RhdGljIGNyZWF0ZSgpOiBZRmlsZSB7XG4gICAgY29uc3QgbW9kZWwgPSBuZXcgWUZpbGUoKTtcbiAgICByZXR1cm4gbW9kZWw7XG4gIH1cblxuICAvKipcbiAgICogR2V0cyBjZWxsJ3Mgc291cmNlLlxuICAgKlxuICAgKiBAcmV0dXJucyBDZWxsJ3Mgc291cmNlLlxuICAgKi9cbiAgcHVibGljIGdldFNvdXJjZSgpOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLnlzb3VyY2UudG9TdHJpbmcoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZXRzIGNlbGwncyBzb3VyY2UuXG4gICAqXG4gICAqIEBwYXJhbSB2YWx1ZTogTmV3IHNvdXJjZS5cbiAgICovXG4gIHB1YmxpYyBzZXRTb3VyY2UodmFsdWU6IHN0cmluZyk6IHZvaWQge1xuICAgIHRoaXMudHJhbnNhY3QoKCkgPT4ge1xuICAgICAgY29uc3QgeXRleHQgPSB0aGlzLnlzb3VyY2U7XG4gICAgICB5dGV4dC5kZWxldGUoMCwgeXRleHQubGVuZ3RoKTtcbiAgICAgIHl0ZXh0Lmluc2VydCgwLCB2YWx1ZSk7XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogUmVwbGFjZSBjb250ZW50IGZyb20gYHN0YXJ0JyB0byBgZW5kYCB3aXRoIGB2YWx1ZWAuXG4gICAqXG4gICAqIEBwYXJhbSBzdGFydDogVGhlIHN0YXJ0IGluZGV4IG9mIHRoZSByYW5nZSB0byByZXBsYWNlIChpbmNsdXNpdmUpLlxuICAgKlxuICAgKiBAcGFyYW0gZW5kOiBUaGUgZW5kIGluZGV4IG9mIHRoZSByYW5nZSB0byByZXBsYWNlIChleGNsdXNpdmUpLlxuICAgKlxuICAgKiBAcGFyYW0gdmFsdWU6IE5ldyBzb3VyY2UgKG9wdGlvbmFsKS5cbiAgICovXG4gIHB1YmxpYyB1cGRhdGVTb3VyY2Uoc3RhcnQ6IG51bWJlciwgZW5kOiBudW1iZXIsIHZhbHVlID0gJycpOiB2b2lkIHtcbiAgICB0aGlzLnRyYW5zYWN0KCgpID0+IHtcbiAgICAgIGNvbnN0IHlzb3VyY2UgPSB0aGlzLnlzb3VyY2U7XG4gICAgICAvLyBpbnNlcnQgYW5kIHRoZW4gZGVsZXRlLlxuICAgICAgLy8gVGhpcyBlbnN1cmVzIHRoYXQgdGhlIGN1cnNvciBwb3NpdGlvbiBpcyBhZGp1c3RlZCBhZnRlciB0aGUgcmVwbGFjZWQgY29udGVudC5cbiAgICAgIHlzb3VyY2UuaW5zZXJ0KHN0YXJ0LCB2YWx1ZSk7XG4gICAgICB5c291cmNlLmRlbGV0ZShzdGFydCArIHZhbHVlLmxlbmd0aCwgZW5kIC0gc3RhcnQpO1xuICAgIH0pO1xuICB9XG5cbiAgcHVibGljIHlzb3VyY2UgPSB0aGlzLnlkb2MuZ2V0VGV4dCgnc291cmNlJyk7XG59XG5cbi8qKlxuICogU2hhcmVkIGltcGxlbWVudGF0aW9uIG9mIHRoZSBTaGFyZWQgRG9jdW1lbnQgdHlwZXMuXG4gKlxuICogU2hhcmVkIGNlbGxzIGNhbiBiZSBpbnNlcnRlZCBpbnRvIGEgU2hhcmVkTm90ZWJvb2suXG4gKiBTaGFyZWQgY2VsbHMgb25seSBzdGFydCBlbWl0dGluZyBldmVudHMgd2hlbiB0aGV5IGFyZSBjb25uZWN0ZWQgdG8gYSBTaGFyZWROb3RlYm9vay5cbiAqXG4gKiBcIlN0YW5kYWxvbmVcIiBjZWxscyBtdXN0IG5vdCBiZSBpbnNlcnRlZCBpbnRvIGEgKFNoYXJlZClOb3RlYm9vay5cbiAqIFN0YW5kYWxvbmUgY2VsbHMgZW1pdCBldmVudHMgaW1tZWRpYXRlbHkgYWZ0ZXIgdGhleSBoYXZlIGJlZW4gY3JlYXRlZCwgYnV0IHRoZXkgbXVzdCBub3RcbiAqIGJlIGluY2x1ZGVkIGludG8gYSAoU2hhcmVkKU5vdGVib29rLlxuICovXG5leHBvcnQgY2xhc3MgWU5vdGVib29rXG4gIGV4dGVuZHMgWURvY3VtZW50PG1vZGVscy5Ob3RlYm9va0NoYW5nZT5cbiAgaW1wbGVtZW50cyBtb2RlbHMuSVNoYXJlZE5vdGVib29rXG57XG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IElTaGFyZWROb3RlYm9vay5JT3B0aW9ucykge1xuICAgIHN1cGVyKCk7XG4gICAgdGhpcy5fZGlzYWJsZURvY3VtZW50V2lkZVVuZG9SZWRvID0gb3B0aW9ucy5kaXNhYmxlRG9jdW1lbnRXaWRlVW5kb1JlZG87XG4gICAgdGhpcy55Y2VsbHMub2JzZXJ2ZSh0aGlzLl9vbllDZWxsc0NoYW5nZWQpO1xuICAgIHRoaXMuY2VsbHMgPSB0aGlzLnljZWxscy50b0FycmF5KCkubWFwKHljZWxsID0+IHtcbiAgICAgIGlmICghdGhpcy5feWNlbGxNYXBwaW5nLmhhcyh5Y2VsbCkpIHtcbiAgICAgICAgdGhpcy5feWNlbGxNYXBwaW5nLnNldCh5Y2VsbCwgY3JlYXRlQ2VsbE1vZGVsRnJvbVNoYXJlZFR5cGUoeWNlbGwpKTtcbiAgICAgIH1cbiAgICAgIHJldHVybiB0aGlzLl95Y2VsbE1hcHBpbmcuZ2V0KHljZWxsKSBhcyBZQ2VsbFR5cGU7XG4gICAgfSk7XG5cbiAgICB0aGlzLnltZXRhLm9ic2VydmUodGhpcy5fb25NZXRhQ2hhbmdlZCk7XG4gICAgdGhpcy55c3RhdGUub2JzZXJ2ZSh0aGlzLl9vblN0YXRlQ2hhbmdlZCk7XG4gIH1cblxuICBnZXQgbmJmb3JtYXQoKTogbnVtYmVyIHtcbiAgICByZXR1cm4gdGhpcy55bWV0YS5nZXQoJ25iZm9ybWF0Jyk7XG4gIH1cblxuICBzZXQgbmJmb3JtYXQodmFsdWU6IG51bWJlcikge1xuICAgIHRoaXMudHJhbnNhY3QoKCkgPT4ge1xuICAgICAgdGhpcy55bWV0YS5zZXQoJ25iZm9ybWF0JywgdmFsdWUpO1xuICAgIH0sIGZhbHNlKTtcbiAgfVxuXG4gIGdldCBuYmZvcm1hdF9taW5vcigpOiBudW1iZXIge1xuICAgIHJldHVybiB0aGlzLnltZXRhLmdldCgnbmJmb3JtYXRfbWlub3InKTtcbiAgfVxuXG4gIHNldCBuYmZvcm1hdF9taW5vcih2YWx1ZTogbnVtYmVyKSB7XG4gICAgdGhpcy50cmFuc2FjdCgoKSA9PiB7XG4gICAgICB0aGlzLnltZXRhLnNldCgnbmJmb3JtYXRfbWlub3InLCB2YWx1ZSk7XG4gICAgfSwgZmFsc2UpO1xuICB9XG5cbiAgLyoqXG4gICAqIERpc3Bvc2Ugb2YgdGhlIHJlc291cmNlcy5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgdGhpcy55Y2VsbHMudW5vYnNlcnZlKHRoaXMuX29uWUNlbGxzQ2hhbmdlZCk7XG4gICAgdGhpcy55bWV0YS51bm9ic2VydmUodGhpcy5fb25NZXRhQ2hhbmdlZCk7XG4gICAgdGhpcy55c3RhdGUudW5vYnNlcnZlKHRoaXMuX29uU3RhdGVDaGFuZ2VkKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgYSBzaGFyZWQgY2VsbCBieSBpbmRleC5cbiAgICpcbiAgICogQHBhcmFtIGluZGV4OiBDZWxsJ3MgcG9zaXRpb24uXG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSByZXF1ZXN0ZWQgc2hhcmVkIGNlbGwuXG4gICAqL1xuICBnZXRDZWxsKGluZGV4OiBudW1iZXIpOiBZQ2VsbFR5cGUge1xuICAgIHJldHVybiB0aGlzLmNlbGxzW2luZGV4XTtcbiAgfVxuXG4gIC8qKlxuICAgKiBJbnNlcnQgYSBzaGFyZWQgY2VsbCBpbnRvIGEgc3BlY2lmaWMgcG9zaXRpb24uXG4gICAqXG4gICAqIEBwYXJhbSBpbmRleDogQ2VsbCdzIHBvc2l0aW9uLlxuICAgKlxuICAgKiBAcGFyYW0gY2VsbDogQ2VsbCB0byBpbnNlcnQuXG4gICAqL1xuICBpbnNlcnRDZWxsKGluZGV4OiBudW1iZXIsIGNlbGw6IFlDZWxsVHlwZSk6IHZvaWQge1xuICAgIHRoaXMuaW5zZXJ0Q2VsbHMoaW5kZXgsIFtjZWxsXSk7XG4gIH1cblxuICAvKipcbiAgICogSW5zZXJ0IGEgbGlzdCBvZiBzaGFyZWQgY2VsbHMgaW50byBhIHNwZWNpZmljIHBvc2l0aW9uLlxuICAgKlxuICAgKiBAcGFyYW0gaW5kZXg6IFBvc2l0aW9uIHRvIGluc2VydCB0aGUgY2VsbHMuXG4gICAqXG4gICAqIEBwYXJhbSBjZWxsczogQXJyYXkgb2Ygc2hhcmVkIGNlbGxzIHRvIGluc2VydC5cbiAgICovXG4gIGluc2VydENlbGxzKGluZGV4OiBudW1iZXIsIGNlbGxzOiBZQ2VsbFR5cGVbXSk6IHZvaWQge1xuICAgIGNlbGxzLmZvckVhY2goY2VsbCA9PiB7XG4gICAgICB0aGlzLl95Y2VsbE1hcHBpbmcuc2V0KGNlbGwueW1vZGVsLCBjZWxsKTtcbiAgICAgIGlmICghdGhpcy5kaXNhYmxlRG9jdW1lbnRXaWRlVW5kb1JlZG8pIHtcbiAgICAgICAgY2VsbC51bmRvTWFuYWdlciA9IHRoaXMudW5kb01hbmFnZXI7XG4gICAgICB9XG4gICAgfSk7XG4gICAgdGhpcy50cmFuc2FjdCgoKSA9PiB7XG4gICAgICB0aGlzLnljZWxscy5pbnNlcnQoXG4gICAgICAgIGluZGV4LFxuICAgICAgICBjZWxscy5tYXAoY2VsbCA9PiBjZWxsLnltb2RlbClcbiAgICAgICk7XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogTW92ZSBhIGNlbGwuXG4gICAqXG4gICAqIEBwYXJhbSBmcm9tSW5kZXg6IEluZGV4IG9mIHRoZSBjZWxsIHRvIG1vdmUuXG4gICAqXG4gICAqIEBwYXJhbSB0b0luZGV4OiBOZXcgcG9zaXRpb24gb2YgdGhlIGNlbGwuXG4gICAqL1xuICBtb3ZlQ2VsbChmcm9tSW5kZXg6IG51bWJlciwgdG9JbmRleDogbnVtYmVyKTogdm9pZCB7XG4gICAgdGhpcy50cmFuc2FjdCgoKSA9PiB7XG4gICAgICBjb25zdCBmcm9tQ2VsbDogYW55ID0gdGhpcy5nZXRDZWxsKGZyb21JbmRleCkuY2xvbmUoKTtcbiAgICAgIHRoaXMuZGVsZXRlQ2VsbChmcm9tSW5kZXgpO1xuICAgICAgdGhpcy5pbnNlcnRDZWxsKHRvSW5kZXgsIGZyb21DZWxsKTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW1vdmUgYSBjZWxsLlxuICAgKlxuICAgKiBAcGFyYW0gaW5kZXg6IEluZGV4IG9mIHRoZSBjZWxsIHRvIHJlbW92ZS5cbiAgICovXG4gIGRlbGV0ZUNlbGwoaW5kZXg6IG51bWJlcik6IHZvaWQge1xuICAgIHRoaXMuZGVsZXRlQ2VsbFJhbmdlKGluZGV4LCBpbmRleCArIDEpO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlbW92ZSBhIHJhbmdlIG9mIGNlbGxzLlxuICAgKlxuICAgKiBAcGFyYW0gZnJvbTogVGhlIHN0YXJ0IGluZGV4IG9mIHRoZSByYW5nZSB0byByZW1vdmUgKGluY2x1c2l2ZSkuXG4gICAqXG4gICAqIEBwYXJhbSB0bzogVGhlIGVuZCBpbmRleCBvZiB0aGUgcmFuZ2UgdG8gcmVtb3ZlIChleGNsdXNpdmUpLlxuICAgKi9cbiAgZGVsZXRlQ2VsbFJhbmdlKGZyb206IG51bWJlciwgdG86IG51bWJlcik6IHZvaWQge1xuICAgIHRoaXMudHJhbnNhY3QoKCkgPT4ge1xuICAgICAgdGhpcy55Y2VsbHMuZGVsZXRlKGZyb20sIHRvIC0gZnJvbSk7XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogUmV0dXJucyB0aGUgbWV0YWRhdGEgYXNzb2NpYXRlZCB3aXRoIHRoZSBub3RlYm9vay5cbiAgICpcbiAgICogQHJldHVybnMgTm90ZWJvb2sncyBtZXRhZGF0YS5cbiAgICovXG4gIGdldE1ldGFkYXRhKCk6IG5iZm9ybWF0LklOb3RlYm9va01ldGFkYXRhIHtcbiAgICBjb25zdCBtZXRhID0gdGhpcy55bWV0YS5nZXQoJ21ldGFkYXRhJyk7XG4gICAgcmV0dXJuIG1ldGEgPyBkZWVwQ29weShtZXRhKSA6IHt9O1xuICB9XG5cbiAgLyoqXG4gICAqIFNldHMgdGhlIG1ldGFkYXRhIGFzc29jaWF0ZWQgd2l0aCB0aGUgbm90ZWJvb2suXG4gICAqXG4gICAqIEBwYXJhbSBtZXRhZGF0YTogTm90ZWJvb2sncyBtZXRhZGF0YS5cbiAgICovXG4gIHNldE1ldGFkYXRhKHZhbHVlOiBuYmZvcm1hdC5JTm90ZWJvb2tNZXRhZGF0YSk6IHZvaWQge1xuICAgIHRoaXMueW1ldGEuc2V0KCdtZXRhZGF0YScsIGRlZXBDb3B5KHZhbHVlKSk7XG4gIH1cblxuICAvKipcbiAgICogVXBkYXRlcyB0aGUgbWV0YWRhdGEgYXNzb2NpYXRlZCB3aXRoIHRoZSBub3RlYm9vay5cbiAgICpcbiAgICogQHBhcmFtIHZhbHVlOiBNZXRhZGF0YSdzIGF0dHJpYnV0ZSB0byB1cGRhdGUuXG4gICAqL1xuICB1cGRhdGVNZXRhZGF0YSh2YWx1ZTogUGFydGlhbDxuYmZvcm1hdC5JTm90ZWJvb2tNZXRhZGF0YT4pOiB2b2lkIHtcbiAgICAvLyBUT0RPOiBNYXliZSBtb2RpZnkgb25seSBhdHRyaWJ1dGVzIGluc3RlYWQgb2YgcmVwbGFjaW5nIHRoZSB3aG9sZSBtZXRhZGF0YT9cbiAgICB0aGlzLnltZXRhLnNldCgnbWV0YWRhdGEnLCBPYmplY3QuYXNzaWduKHt9LCB0aGlzLmdldE1ldGFkYXRhKCksIHZhbHVlKSk7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IFlOb3RlYm9vay5cbiAgICovXG4gIHB1YmxpYyBzdGF0aWMgY3JlYXRlKFxuICAgIGRpc2FibGVEb2N1bWVudFdpZGVVbmRvUmVkbzogYm9vbGVhblxuICApOiBtb2RlbHMuSVNoYXJlZE5vdGVib29rIHtcbiAgICBjb25zdCBtb2RlbCA9IG5ldyBZTm90ZWJvb2soeyBkaXNhYmxlRG9jdW1lbnRXaWRlVW5kb1JlZG8gfSk7XG4gICAgcmV0dXJuIG1vZGVsO1xuICB9XG5cbiAgLyoqXG4gICAqIFdldGhlciB0aGUgdGhlIHVuZG8vcmVkbyBsb2dpYyBzaG91bGQgYmVcbiAgICogY29uc2lkZXJlZCBvbiB0aGUgZnVsbCBkb2N1bWVudCBhY3Jvc3MgYWxsIGNlbGxzLlxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgZGlzYWJsZURvY3VtZW50V2lkZVVuZG9SZWRvIHNldHRpbmcuXG4gICAqL1xuICBnZXQgZGlzYWJsZURvY3VtZW50V2lkZVVuZG9SZWRvKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiB0aGlzLl9kaXNhYmxlRG9jdW1lbnRXaWRlVW5kb1JlZG87XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGEgY2hhbmdlIHRvIHRoZSBsaXN0IG9mIGNlbGxzLlxuICAgKi9cbiAgcHJpdmF0ZSBfb25ZQ2VsbHNDaGFuZ2VkID0gKGV2ZW50OiBZLllBcnJheUV2ZW50PFkuTWFwPGFueT4+KSA9PiB7XG4gICAgLy8gdXBkYXRlIHRoZSB0eXBl4oeUY2VsbCBtYXBwaW5nIGJ5IGl0ZXJhdGluZyB0aHJvdWdoIHRoZSBhZGRlZC9yZW1vdmVkIHR5cGVzXG4gICAgZXZlbnQuY2hhbmdlcy5hZGRlZC5mb3JFYWNoKGl0ZW0gPT4ge1xuICAgICAgY29uc3QgdHlwZSA9IChpdGVtLmNvbnRlbnQgYXMgWS5Db250ZW50VHlwZSkudHlwZSBhcyBZLk1hcDxhbnk+O1xuICAgICAgaWYgKCF0aGlzLl95Y2VsbE1hcHBpbmcuaGFzKHR5cGUpKSB7XG4gICAgICAgIHRoaXMuX3ljZWxsTWFwcGluZy5zZXQodHlwZSwgY3JlYXRlQ2VsbE1vZGVsRnJvbVNoYXJlZFR5cGUodHlwZSkpO1xuICAgICAgfVxuICAgICAgY29uc3QgY2VsbCA9IHRoaXMuX3ljZWxsTWFwcGluZy5nZXQodHlwZSkgYXMgYW55O1xuICAgICAgY2VsbC5fbm90ZWJvb2sgPSB0aGlzO1xuICAgICAgaWYgKCF0aGlzLmRpc2FibGVEb2N1bWVudFdpZGVVbmRvUmVkbykge1xuICAgICAgICBjZWxsLl91bmRvTWFuYWdlciA9IHRoaXMudW5kb01hbmFnZXI7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICBjZWxsLl91bmRvTWFuYWdlciA9IG5ldyBZLlVuZG9NYW5hZ2VyKFtjZWxsLnltb2RlbF0sIHt9KTtcbiAgICAgIH1cbiAgICB9KTtcbiAgICBldmVudC5jaGFuZ2VzLmRlbGV0ZWQuZm9yRWFjaChpdGVtID0+IHtcbiAgICAgIGNvbnN0IHR5cGUgPSAoaXRlbS5jb250ZW50IGFzIFkuQ29udGVudFR5cGUpLnR5cGUgYXMgWS5NYXA8YW55PjtcbiAgICAgIGNvbnN0IG1vZGVsID0gdGhpcy5feWNlbGxNYXBwaW5nLmdldCh0eXBlKTtcbiAgICAgIGlmIChtb2RlbCkge1xuICAgICAgICBtb2RlbC5kaXNwb3NlKCk7XG4gICAgICAgIHRoaXMuX3ljZWxsTWFwcGluZy5kZWxldGUodHlwZSk7XG4gICAgICB9XG4gICAgfSk7XG4gICAgbGV0IGluZGV4ID0gMDtcbiAgICAvLyB0aGlzIHJlZmxlY3RzIHRoZSBldmVudC5jaGFuZ2VzLmRlbHRhLCBidXQgcmVwbGFjZXMgdGhlIGNvbnRlbnQgb2YgZGVsdGEuaW5zZXJ0IHdpdGggeWNlbGxzXG4gICAgY29uc3QgY2VsbHNDaGFuZ2U6IERlbHRhPG1vZGVscy5JU2hhcmVkQ2VsbFtdPiA9IFtdO1xuICAgIGV2ZW50LmNoYW5nZXMuZGVsdGEuZm9yRWFjaCgoZDogYW55KSA9PiB7XG4gICAgICBpZiAoZC5pbnNlcnQgIT0gbnVsbCkge1xuICAgICAgICBjb25zdCBpbnNlcnRlZENlbGxzID0gZC5pbnNlcnQubWFwKCh5Y2VsbDogWS5NYXA8YW55PikgPT5cbiAgICAgICAgICB0aGlzLl95Y2VsbE1hcHBpbmcuZ2V0KHljZWxsKVxuICAgICAgICApO1xuICAgICAgICBjZWxsc0NoYW5nZS5wdXNoKHsgaW5zZXJ0OiBpbnNlcnRlZENlbGxzIH0pO1xuICAgICAgICB0aGlzLmNlbGxzLnNwbGljZShpbmRleCwgMCwgLi4uaW5zZXJ0ZWRDZWxscyk7XG4gICAgICAgIGluZGV4ICs9IGQuaW5zZXJ0Lmxlbmd0aDtcbiAgICAgIH0gZWxzZSBpZiAoZC5kZWxldGUgIT0gbnVsbCkge1xuICAgICAgICBjZWxsc0NoYW5nZS5wdXNoKGQpO1xuICAgICAgICB0aGlzLmNlbGxzLnNwbGljZShpbmRleCwgZC5kZWxldGUpO1xuICAgICAgfSBlbHNlIGlmIChkLnJldGFpbiAhPSBudWxsKSB7XG4gICAgICAgIGNlbGxzQ2hhbmdlLnB1c2goZCk7XG4gICAgICAgIGluZGV4ICs9IGQucmV0YWluO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgdGhpcy5fY2hhbmdlZC5lbWl0KHtcbiAgICAgIGNlbGxzQ2hhbmdlOiBjZWxsc0NoYW5nZVxuICAgIH0pO1xuICB9O1xuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSBjaGFuZ2UgdG8gdGhlIHlzdGF0ZS5cbiAgICovXG4gIHByaXZhdGUgX29uTWV0YUNoYW5nZWQgPSAoZXZlbnQ6IFkuWU1hcEV2ZW50PGFueT4pID0+IHtcbiAgICBpZiAoZXZlbnQua2V5c0NoYW5nZWQuaGFzKCdtZXRhZGF0YScpKSB7XG4gICAgICBjb25zdCBjaGFuZ2UgPSBldmVudC5jaGFuZ2VzLmtleXMuZ2V0KCdtZXRhZGF0YScpO1xuICAgICAgY29uc3QgbWV0YWRhdGFDaGFuZ2UgPSB7XG4gICAgICAgIG9sZFZhbHVlOiBjaGFuZ2U/Lm9sZFZhbHVlID8gY2hhbmdlIS5vbGRWYWx1ZSA6IHVuZGVmaW5lZCxcbiAgICAgICAgbmV3VmFsdWU6IHRoaXMuZ2V0TWV0YWRhdGEoKVxuICAgICAgfTtcbiAgICAgIHRoaXMuX2NoYW5nZWQuZW1pdCh7IG1ldGFkYXRhQ2hhbmdlIH0pO1xuICAgIH1cblxuICAgIGlmIChldmVudC5rZXlzQ2hhbmdlZC5oYXMoJ25iZm9ybWF0JykpIHtcbiAgICAgIGNvbnN0IGNoYW5nZSA9IGV2ZW50LmNoYW5nZXMua2V5cy5nZXQoJ25iZm9ybWF0Jyk7XG4gICAgICBjb25zdCBuYmZvcm1hdENoYW5nZWQgPSB7XG4gICAgICAgIGtleTogJ25iZm9ybWF0JyxcbiAgICAgICAgb2xkVmFsdWU6IGNoYW5nZT8ub2xkVmFsdWUgPyBjaGFuZ2UhLm9sZFZhbHVlIDogdW5kZWZpbmVkLFxuICAgICAgICBuZXdWYWx1ZTogdGhpcy5uYmZvcm1hdFxuICAgICAgfTtcbiAgICAgIHRoaXMuX2NoYW5nZWQuZW1pdCh7IG5iZm9ybWF0Q2hhbmdlZCB9KTtcbiAgICB9XG5cbiAgICBpZiAoZXZlbnQua2V5c0NoYW5nZWQuaGFzKCduYmZvcm1hdF9taW5vcicpKSB7XG4gICAgICBjb25zdCBjaGFuZ2UgPSBldmVudC5jaGFuZ2VzLmtleXMuZ2V0KCduYmZvcm1hdF9taW5vcicpO1xuICAgICAgY29uc3QgbmJmb3JtYXRDaGFuZ2VkID0ge1xuICAgICAgICBrZXk6ICduYmZvcm1hdF9taW5vcicsXG4gICAgICAgIG9sZFZhbHVlOiBjaGFuZ2U/Lm9sZFZhbHVlID8gY2hhbmdlIS5vbGRWYWx1ZSA6IHVuZGVmaW5lZCxcbiAgICAgICAgbmV3VmFsdWU6IHRoaXMubmJmb3JtYXRfbWlub3JcbiAgICAgIH07XG4gICAgICB0aGlzLl9jaGFuZ2VkLmVtaXQoeyBuYmZvcm1hdENoYW5nZWQgfSk7XG4gICAgfVxuICB9O1xuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSBjaGFuZ2UgdG8gdGhlIHlzdGF0ZS5cbiAgICovXG4gIHByaXZhdGUgX29uU3RhdGVDaGFuZ2VkID0gKGV2ZW50OiBZLllNYXBFdmVudDxhbnk+KSA9PiB7XG4gICAgY29uc3Qgc3RhdGVDaGFuZ2U6IGFueSA9IFtdO1xuICAgIGV2ZW50LmtleXNDaGFuZ2VkLmZvckVhY2goa2V5ID0+IHtcbiAgICAgIGNvbnN0IGNoYW5nZSA9IGV2ZW50LmNoYW5nZXMua2V5cy5nZXQoa2V5KTtcbiAgICAgIGlmIChjaGFuZ2UpIHtcbiAgICAgICAgc3RhdGVDaGFuZ2UucHVzaCh7XG4gICAgICAgICAgbmFtZToga2V5LFxuICAgICAgICAgIG9sZFZhbHVlOiBjaGFuZ2Uub2xkVmFsdWUsXG4gICAgICAgICAgbmV3VmFsdWU6IHRoaXMueXN0YXRlLmdldChrZXkpXG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgdGhpcy5fY2hhbmdlZC5lbWl0KHsgc3RhdGVDaGFuZ2UgfSk7XG4gIH07XG5cbiAgcHVibGljIHljZWxsczogWS5BcnJheTxZLk1hcDxhbnk+PiA9IHRoaXMueWRvYy5nZXRBcnJheSgnY2VsbHMnKTtcbiAgcHVibGljIHltZXRhOiBZLk1hcDxhbnk+ID0gdGhpcy55ZG9jLmdldE1hcCgnbWV0YScpO1xuICBwdWJsaWMgeW1vZGVsOiBZLk1hcDxhbnk+ID0gdGhpcy55ZG9jLmdldE1hcCgnbW9kZWwnKTtcbiAgcHVibGljIHVuZG9NYW5hZ2VyID0gbmV3IFkuVW5kb01hbmFnZXIoW3RoaXMueWNlbGxzXSwge1xuICAgIHRyYWNrZWRPcmlnaW5zOiBuZXcgU2V0KFt0aGlzXSlcbiAgfSk7XG4gIHByaXZhdGUgX2Rpc2FibGVEb2N1bWVudFdpZGVVbmRvUmVkbzogYm9vbGVhbjtcbiAgcHJpdmF0ZSBfeWNlbGxNYXBwaW5nOiBNYXA8WS5NYXA8YW55PiwgWUNlbGxUeXBlPiA9IG5ldyBNYXAoKTtcbiAgcHVibGljIGNlbGxzOiBZQ2VsbFR5cGVbXTtcbn1cblxuLyoqXG4gKiBDcmVhdGUgYSBuZXcgc2hhcmVkIGNlbGwgbW9kZWwgZ2l2ZW4gdGhlIFlKUyBzaGFyZWQgdHlwZS5cbiAqL1xuZXhwb3J0IGNvbnN0IGNyZWF0ZUNlbGxNb2RlbEZyb21TaGFyZWRUeXBlID0gKHR5cGU6IFkuTWFwPGFueT4pOiBZQ2VsbFR5cGUgPT4ge1xuICBzd2l0Y2ggKHR5cGUuZ2V0KCdjZWxsX3R5cGUnKSkge1xuICAgIGNhc2UgJ2NvZGUnOlxuICAgICAgcmV0dXJuIG5ldyBZQ29kZUNlbGwodHlwZSk7XG4gICAgY2FzZSAnbWFya2Rvd24nOlxuICAgICAgcmV0dXJuIG5ldyBZTWFya2Rvd25DZWxsKHR5cGUpO1xuICAgIGNhc2UgJ3Jhdyc6XG4gICAgICByZXR1cm4gbmV3IFlSYXdDZWxsKHR5cGUpO1xuICAgIGRlZmF1bHQ6XG4gICAgICB0aHJvdyBuZXcgRXJyb3IoJ0ZvdW5kIHVua25vd24gY2VsbCB0eXBlJyk7XG4gIH1cbn07XG5cbi8qKlxuICogQ3JlYXRlIGEgbmV3IHN0YW5kYWxvbmUgY2VsbCBnaXZlbiB0aGUgdHlwZS5cbiAqL1xuZXhwb3J0IGNvbnN0IGNyZWF0ZVN0YW5kYWxvbmVDZWxsID0gKFxuICBjZWxsVHlwZTogJ3JhdycgfCAnY29kZScgfCAnbWFya2Rvd24nLFxuICBpZD86IHN0cmluZ1xuKTogWUNlbGxUeXBlID0+IHtcbiAgc3dpdGNoIChjZWxsVHlwZSkge1xuICAgIGNhc2UgJ21hcmtkb3duJzpcbiAgICAgIHJldHVybiBZTWFya2Rvd25DZWxsLmNyZWF0ZVN0YW5kYWxvbmUoaWQpO1xuICAgIGNhc2UgJ2NvZGUnOlxuICAgICAgcmV0dXJuIFlDb2RlQ2VsbC5jcmVhdGVTdGFuZGFsb25lKGlkKTtcbiAgICBkZWZhdWx0OlxuICAgICAgLy8gcmF3XG4gICAgICByZXR1cm4gWVJhd0NlbGwuY3JlYXRlU3RhbmRhbG9uZShpZCk7XG4gIH1cbn07XG5cbmV4cG9ydCBjbGFzcyBZQmFzZUNlbGw8TWV0YWRhdGEgZXh0ZW5kcyBtb2RlbHMuSVNoYXJlZEJhc2VDZWxsTWV0YWRhdGE+XG4gIGltcGxlbWVudHMgbW9kZWxzLklTaGFyZWRCYXNlQ2VsbDxNZXRhZGF0YT4sIElZVGV4dFxue1xuICBjb25zdHJ1Y3Rvcih5bW9kZWw6IFkuTWFwPGFueT4pIHtcbiAgICB0aGlzLnltb2RlbCA9IHltb2RlbDtcbiAgICBjb25zdCB5c291cmNlID0geW1vZGVsLmdldCgnc291cmNlJyk7XG4gICAgdGhpcy5fcHJldlNvdXJjZUxlbmd0aCA9IHlzb3VyY2UgPyB5c291cmNlLmxlbmd0aCA6IDA7XG4gICAgdGhpcy55bW9kZWwub2JzZXJ2ZURlZXAodGhpcy5fbW9kZWxPYnNlcnZlcik7XG4gICAgdGhpcy5fYXdhcmVuZXNzID0gbnVsbDtcbiAgfVxuXG4gIGdldCB5c291cmNlKCk6IFkuVGV4dCB7XG4gICAgcmV0dXJuIHRoaXMueW1vZGVsLmdldCgnc291cmNlJyk7XG4gIH1cblxuICBnZXQgYXdhcmVuZXNzKCk6IEF3YXJlbmVzcyB8IG51bGwge1xuICAgIHJldHVybiB0aGlzLl9hd2FyZW5lc3MgPz8gdGhpcy5ub3RlYm9vaz8uYXdhcmVuZXNzID8/IG51bGw7XG4gIH1cblxuICAvKipcbiAgICogUGVyZm9ybSBhIHRyYW5zYWN0aW9uLiBXaGlsZSB0aGUgZnVuY3Rpb24gZiBpcyBjYWxsZWQsIGFsbCBjaGFuZ2VzIHRvIHRoZSBzaGFyZWRcbiAgICogZG9jdW1lbnQgYXJlIGJ1bmRsZWQgaW50byBhIHNpbmdsZSBldmVudC5cbiAgICovXG4gIHRyYW5zYWN0KGY6ICgpID0+IHZvaWQsIHVuZG9hYmxlID0gdHJ1ZSk6IHZvaWQge1xuICAgIHRoaXMubm90ZWJvb2sgJiYgdW5kb2FibGVcbiAgICAgID8gdGhpcy5ub3RlYm9vay50cmFuc2FjdChmKVxuICAgICAgOiB0aGlzLnltb2RlbC5kb2MhLnRyYW5zYWN0KGYsIHRoaXMpO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBub3RlYm9vayB0aGF0IHRoaXMgY2VsbCBiZWxvbmdzIHRvLlxuICAgKi9cbiAgZ2V0IHVuZG9NYW5hZ2VyKCk6IFkuVW5kb01hbmFnZXIgfCBudWxsIHtcbiAgICBpZiAoIXRoaXMubm90ZWJvb2spIHtcbiAgICAgIHJldHVybiB0aGlzLl91bmRvTWFuYWdlcjtcbiAgICB9XG4gICAgcmV0dXJuIHRoaXMubm90ZWJvb2s/LmRpc2FibGVEb2N1bWVudFdpZGVVbmRvUmVkb1xuICAgICAgPyB0aGlzLl91bmRvTWFuYWdlclxuICAgICAgOiB0aGlzLm5vdGVib29rLnVuZG9NYW5hZ2VyO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldCB0aGUgdW5kb01hbmFnZXIgd2hlbiBhZGRpbmcgbmV3IGNlbGxzLlxuICAgKi9cbiAgc2V0IHVuZG9NYW5hZ2VyKHVuZG9NYW5hZ2VyOiBZLlVuZG9NYW5hZ2VyIHwgbnVsbCkge1xuICAgIHRoaXMuX3VuZG9NYW5hZ2VyID0gdW5kb01hbmFnZXI7XG4gIH1cblxuICAvKipcbiAgICogVW5kbyBhbiBvcGVyYXRpb24uXG4gICAqL1xuICB1bmRvKCk6IHZvaWQge1xuICAgIHRoaXMudW5kb01hbmFnZXI/LnVuZG8oKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZWRvIGFuIG9wZXJhdGlvbi5cbiAgICovXG4gIHJlZG8oKTogdm9pZCB7XG4gICAgdGhpcy51bmRvTWFuYWdlcj8ucmVkbygpO1xuICB9XG5cbiAgLyoqXG4gICAqIFdoZXRoZXIgdGhlIG9iamVjdCBjYW4gdW5kbyBjaGFuZ2VzLlxuICAgKi9cbiAgY2FuVW5kbygpOiBib29sZWFuIHtcbiAgICByZXR1cm4gISF0aGlzLnVuZG9NYW5hZ2VyICYmIHRoaXMudW5kb01hbmFnZXIudW5kb1N0YWNrLmxlbmd0aCA+IDA7XG4gIH1cblxuICAvKipcbiAgICogV2hldGhlciB0aGUgb2JqZWN0IGNhbiByZWRvIGNoYW5nZXMuXG4gICAqL1xuICBjYW5SZWRvKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiAhIXRoaXMudW5kb01hbmFnZXIgJiYgdGhpcy51bmRvTWFuYWdlci5yZWRvU3RhY2subGVuZ3RoID4gMDtcbiAgfVxuXG4gIC8qKlxuICAgKiBDbGVhciB0aGUgY2hhbmdlIHN0YWNrLlxuICAgKi9cbiAgY2xlYXJVbmRvSGlzdG9yeSgpOiB2b2lkIHtcbiAgICB0aGlzLnVuZG9NYW5hZ2VyPy5jbGVhcigpO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBub3RlYm9vayB0aGF0IHRoaXMgY2VsbCBiZWxvbmdzIHRvLlxuICAgKi9cbiAgZ2V0IG5vdGVib29rKCk6IFlOb3RlYm9vayB8IG51bGwge1xuICAgIHJldHVybiB0aGlzLl9ub3RlYm9vaztcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgbm90ZWJvb2sgdGhhdCB0aGlzIGNlbGwgYmVsb25ncyB0by5cbiAgICovXG4gIHByb3RlY3RlZCBfbm90ZWJvb2s6IFlOb3RlYm9vayB8IG51bGwgPSBudWxsO1xuXG4gIC8qKlxuICAgKiBXaGV0aGVyIHRoZSBjZWxsIGlzIHN0YW5kYWxvbmUgb3Igbm90LlxuICAgKlxuICAgKiBJZiB0aGUgY2VsbCBpcyBzdGFuZGFsb25lLiBJdCBjYW5ub3QgYmVcbiAgICogaW5zZXJ0ZWQgaW50byBhIFlOb3RlYm9vayBiZWNhdXNlIHRoZSBZanMgbW9kZWwgaXMgYWxyZWFkeVxuICAgKiBhdHRhY2hlZCB0byBhbiBhbm9ueW1vdXMgWS5Eb2MgaW5zdGFuY2UuXG4gICAqL1xuICBpc1N0YW5kYWxvbmUgPSBmYWxzZTtcblxuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IFlSYXdDZWxsIHRoYXQgY2FuIGJlIGluc2VydGVkIGludG8gYSBZTm90ZWJvb2tcbiAgICovXG4gIHB1YmxpYyBzdGF0aWMgY3JlYXRlKGlkID0gVVVJRC51dWlkNCgpKTogWUJhc2VDZWxsPGFueT4ge1xuICAgIGNvbnN0IHltb2RlbCA9IG5ldyBZLk1hcCgpO1xuICAgIGNvbnN0IHlzb3VyY2UgPSBuZXcgWS5UZXh0KCk7XG4gICAgeW1vZGVsLnNldCgnc291cmNlJywgeXNvdXJjZSk7XG4gICAgeW1vZGVsLnNldCgnbWV0YWRhdGEnLCB7fSk7XG4gICAgeW1vZGVsLnNldCgnY2VsbF90eXBlJywgdGhpcy5wcm90b3R5cGUuY2VsbF90eXBlKTtcbiAgICB5bW9kZWwuc2V0KCdpZCcsIGlkKTtcbiAgICByZXR1cm4gbmV3IHRoaXMoeW1vZGVsKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBDcmVhdGUgYSBuZXcgWVJhd0NlbGwgdGhhdCB3b3JrcyBzdGFuZGFsb25lLiBJdCBjYW5ub3QgYmVcbiAgICogaW5zZXJ0ZWQgaW50byBhIFlOb3RlYm9vayBiZWNhdXNlIHRoZSBZanMgbW9kZWwgaXMgYWxyZWFkeVxuICAgKiBhdHRhY2hlZCB0byBhbiBhbm9ueW1vdXMgWS5Eb2MgaW5zdGFuY2UuXG4gICAqL1xuICBwdWJsaWMgc3RhdGljIGNyZWF0ZVN0YW5kYWxvbmUoaWQ/OiBzdHJpbmcpOiBZQmFzZUNlbGw8YW55PiB7XG4gICAgY29uc3QgY2VsbCA9IHRoaXMuY3JlYXRlKGlkKTtcbiAgICBjZWxsLmlzU3RhbmRhbG9uZSA9IHRydWU7XG4gICAgY29uc3QgZG9jID0gbmV3IFkuRG9jKCk7XG4gICAgZG9jLmdldEFycmF5KCkuaW5zZXJ0KDAsIFtjZWxsLnltb2RlbF0pO1xuICAgIGNlbGwuX2F3YXJlbmVzcyA9IG5ldyBBd2FyZW5lc3MoZG9jKTtcbiAgICBjZWxsLl91bmRvTWFuYWdlciA9IG5ldyBZLlVuZG9NYW5hZ2VyKFtjZWxsLnltb2RlbF0sIHtcbiAgICAgIHRyYWNrZWRPcmlnaW5zOiBuZXcgU2V0KFtjZWxsXSlcbiAgICB9KTtcbiAgICByZXR1cm4gY2VsbDtcbiAgfVxuXG4gIC8qKlxuICAgKiBDbG9uZSB0aGUgY2VsbC5cbiAgICpcbiAgICogQHRvZG8gY2xvbmUgc2hvdWxkIG9ubHkgYmUgYXZhaWxhYmxlIGluIHRoZSBzcGVjaWZpYyBpbXBsZW1lbnRhdGlvbnMgaS5lLiBJU2hhcmVkQ29kZUNlbGxcbiAgICovXG4gIHB1YmxpYyBjbG9uZSgpOiBZQmFzZUNlbGw8YW55PiB7XG4gICAgY29uc3QgeW1vZGVsID0gbmV3IFkuTWFwKCk7XG4gICAgY29uc3QgeXNvdXJjZSA9IG5ldyBZLlRleHQodGhpcy5nZXRTb3VyY2UoKSk7XG4gICAgeW1vZGVsLnNldCgnc291cmNlJywgeXNvdXJjZSk7XG4gICAgeW1vZGVsLnNldCgnbWV0YWRhdGEnLCB0aGlzLmdldE1ldGFkYXRhKCkpO1xuICAgIHltb2RlbC5zZXQoJ2NlbGxfdHlwZScsIHRoaXMuY2VsbF90eXBlKTtcbiAgICB5bW9kZWwuc2V0KCdpZCcsIHRoaXMuZ2V0SWQoKSk7XG4gICAgY29uc3QgU2VsZjogYW55ID0gdGhpcy5jb25zdHJ1Y3RvcjtcbiAgICBjb25zdCBjbG9uZSA9IG5ldyBTZWxmKHltb2RlbCk7XG4gICAgLy8gVE9ETyBUaGUgYXNzaWdubWVudCBvZiB0aGUgdW5kb01hbmFnZXIgZG9lcyBub3Qgd29yayBmb3IgYSBjbG9uZS5cbiAgICAvLyBTZWUgaHR0cHM6Ly9naXRodWIuY29tL2p1cHl0ZXJsYWIvanVweXRlcmxhYi9pc3N1ZXMvMTEwMzVcbiAgICBjbG9uZS5fdW5kb01hbmFnZXIgPSB0aGlzLnVuZG9NYW5hZ2VyO1xuICAgIHJldHVybiBjbG9uZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSBjaGFuZ2UgdG8gdGhlIHltb2RlbC5cbiAgICovXG4gIHByaXZhdGUgX21vZGVsT2JzZXJ2ZXIgPSAoZXZlbnRzOiBZLllFdmVudDxhbnk+W10pID0+IHtcbiAgICBjb25zdCBjaGFuZ2VzOiBtb2RlbHMuQ2VsbENoYW5nZTxNZXRhZGF0YT4gPSB7fTtcbiAgICBjb25zdCBzb3VyY2VFdmVudCA9IGV2ZW50cy5maW5kKFxuICAgICAgZXZlbnQgPT4gZXZlbnQudGFyZ2V0ID09PSB0aGlzLnltb2RlbC5nZXQoJ3NvdXJjZScpXG4gICAgKTtcbiAgICBpZiAoc291cmNlRXZlbnQpIHtcbiAgICAgIGNoYW5nZXMuc291cmNlQ2hhbmdlID0gc291cmNlRXZlbnQuY2hhbmdlcy5kZWx0YSBhcyBhbnk7XG4gICAgfVxuXG4gICAgY29uc3Qgb3V0cHV0RXZlbnQgPSBldmVudHMuZmluZChcbiAgICAgIGV2ZW50ID0+IGV2ZW50LnRhcmdldCA9PT0gdGhpcy55bW9kZWwuZ2V0KCdvdXRwdXRzJylcbiAgICApO1xuICAgIGlmIChvdXRwdXRFdmVudCkge1xuICAgICAgY2hhbmdlcy5vdXRwdXRzQ2hhbmdlID0gb3V0cHV0RXZlbnQuY2hhbmdlcy5kZWx0YSBhcyBhbnk7XG4gICAgfVxuXG4gICAgY29uc3QgbW9kZWxFdmVudCA9IGV2ZW50cy5maW5kKGV2ZW50ID0+IGV2ZW50LnRhcmdldCA9PT0gdGhpcy55bW9kZWwpIGFzXG4gICAgICB8IHVuZGVmaW5lZFxuICAgICAgfCBZLllNYXBFdmVudDxhbnk+O1xuICAgIGlmIChtb2RlbEV2ZW50ICYmIG1vZGVsRXZlbnQua2V5c0NoYW5nZWQuaGFzKCdtZXRhZGF0YScpKSB7XG4gICAgICBjb25zdCBjaGFuZ2UgPSBtb2RlbEV2ZW50LmNoYW5nZXMua2V5cy5nZXQoJ21ldGFkYXRhJyk7XG4gICAgICBjaGFuZ2VzLm1ldGFkYXRhQ2hhbmdlID0ge1xuICAgICAgICBvbGRWYWx1ZTogY2hhbmdlPy5vbGRWYWx1ZSA/IGNoYW5nZSEub2xkVmFsdWUgOiB1bmRlZmluZWQsXG4gICAgICAgIG5ld1ZhbHVlOiB0aGlzLmdldE1ldGFkYXRhKClcbiAgICAgIH07XG4gICAgfVxuXG4gICAgaWYgKG1vZGVsRXZlbnQgJiYgbW9kZWxFdmVudC5rZXlzQ2hhbmdlZC5oYXMoJ2V4ZWN1dGlvbl9jb3VudCcpKSB7XG4gICAgICBjb25zdCBjaGFuZ2UgPSBtb2RlbEV2ZW50LmNoYW5nZXMua2V5cy5nZXQoJ2V4ZWN1dGlvbl9jb3VudCcpO1xuICAgICAgY2hhbmdlcy5leGVjdXRpb25Db3VudENoYW5nZSA9IHtcbiAgICAgICAgb2xkVmFsdWU6IGNoYW5nZSEub2xkVmFsdWUsXG4gICAgICAgIG5ld1ZhbHVlOiB0aGlzLnltb2RlbC5nZXQoJ2V4ZWN1dGlvbl9jb3VudCcpXG4gICAgICB9O1xuICAgIH1cblxuICAgIC8vIFRoZSBtb2RlbCBhbGxvd3MgdXMgdG8gcmVwbGFjZSB0aGUgY29tcGxldGUgc291cmNlIHdpdGggYSBuZXcgc3RyaW5nLiBXZSBleHByZXNzIHRoaXMgaW4gdGhlIERlbHRhIGZvcm1hdFxuICAgIC8vIGFzIGEgcmVwbGFjZSBvZiB0aGUgY29tcGxldGUgc3RyaW5nLlxuICAgIGNvbnN0IHlzb3VyY2UgPSB0aGlzLnltb2RlbC5nZXQoJ3NvdXJjZScpO1xuICAgIGlmIChtb2RlbEV2ZW50ICYmIG1vZGVsRXZlbnQua2V5c0NoYW5nZWQuaGFzKCdzb3VyY2UnKSkge1xuICAgICAgY2hhbmdlcy5zb3VyY2VDaGFuZ2UgPSBbXG4gICAgICAgIHsgZGVsZXRlOiB0aGlzLl9wcmV2U291cmNlTGVuZ3RoIH0sXG4gICAgICAgIHsgaW5zZXJ0OiB5c291cmNlLnRvU3RyaW5nKCkgfVxuICAgICAgXTtcbiAgICB9XG4gICAgdGhpcy5fcHJldlNvdXJjZUxlbmd0aCA9IHlzb3VyY2UubGVuZ3RoO1xuICAgIHRoaXMuX2NoYW5nZWQuZW1pdChjaGFuZ2VzKTtcbiAgfTtcblxuICAvKipcbiAgICogVGhlIGNoYW5nZWQgc2lnbmFsLlxuICAgKi9cbiAgZ2V0IGNoYW5nZWQoKTogSVNpZ25hbDx0aGlzLCBtb2RlbHMuQ2VsbENoYW5nZTxNZXRhZGF0YT4+IHtcbiAgICByZXR1cm4gdGhpcy5fY2hhbmdlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIG9mIHRoZSByZXNvdXJjZXMuXG4gICAqL1xuICBkaXNwb3NlKCk6IHZvaWQge1xuICAgIHRoaXMueW1vZGVsLnVub2JzZXJ2ZURlZXAodGhpcy5fbW9kZWxPYnNlcnZlcik7XG4gICAgaWYgKHRoaXMuX2F3YXJlbmVzcykge1xuICAgICAgdGhpcy5fYXdhcmVuZXNzLmRlc3Ryb3koKTtcbiAgICB9XG4gICAgaWYgKCF0aGlzLm5vdGVib29rICYmIHRoaXMuX3VuZG9NYW5hZ2VyKSB7XG4gICAgICB0aGlzLl91bmRvTWFuYWdlci5kZXN0cm95KCk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEdldHMgdGhlIGNlbGwgYXR0YWNobWVudHMuXG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSBjZWxsIGF0dGFjaG1lbnRzLlxuICAgKi9cbiAgcHVibGljIGdldEF0dGFjaG1lbnRzKCk6IG5iZm9ybWF0LklBdHRhY2htZW50cyB8IHVuZGVmaW5lZCB7XG4gICAgcmV0dXJuIHRoaXMueW1vZGVsLmdldCgnYXR0YWNobWVudHMnKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZXRzIHRoZSBjZWxsIGF0dGFjaG1lbnRzXG4gICAqXG4gICAqIEBwYXJhbSBhdHRhY2htZW50czogVGhlIGNlbGwgYXR0YWNobWVudHMuXG4gICAqL1xuICBwdWJsaWMgc2V0QXR0YWNobWVudHMoYXR0YWNobWVudHM6IG5iZm9ybWF0LklBdHRhY2htZW50cyB8IHVuZGVmaW5lZCk6IHZvaWQge1xuICAgIHRoaXMudHJhbnNhY3QoKCkgPT4ge1xuICAgICAgaWYgKGF0dGFjaG1lbnRzID09IG51bGwpIHtcbiAgICAgICAgdGhpcy55bW9kZWwuZGVsZXRlKCdhdHRhY2htZW50cycpO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgdGhpcy55bW9kZWwuc2V0KCdhdHRhY2htZW50cycsIGF0dGFjaG1lbnRzKTtcbiAgICAgIH1cbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgY2VsbCBpZC5cbiAgICpcbiAgICogQHJldHVybnMgQ2VsbCBpZFxuICAgKi9cbiAgcHVibGljIGdldElkKCk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMueW1vZGVsLmdldCgnaWQnKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXRzIGNlbGwncyBzb3VyY2UuXG4gICAqXG4gICAqIEByZXR1cm5zIENlbGwncyBzb3VyY2UuXG4gICAqL1xuICBwdWJsaWMgZ2V0U291cmNlKCk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMueW1vZGVsLmdldCgnc291cmNlJykudG9TdHJpbmcoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZXRzIGNlbGwncyBzb3VyY2UuXG4gICAqXG4gICAqIEBwYXJhbSB2YWx1ZTogTmV3IHNvdXJjZS5cbiAgICovXG4gIHB1YmxpYyBzZXRTb3VyY2UodmFsdWU6IHN0cmluZyk6IHZvaWQge1xuICAgIGNvbnN0IHl0ZXh0ID0gdGhpcy55bW9kZWwuZ2V0KCdzb3VyY2UnKTtcbiAgICB0aGlzLnRyYW5zYWN0KCgpID0+IHtcbiAgICAgIHl0ZXh0LmRlbGV0ZSgwLCB5dGV4dC5sZW5ndGgpO1xuICAgICAgeXRleHQuaW5zZXJ0KDAsIHZhbHVlKTtcbiAgICB9KTtcbiAgICAvLyBAdG9kbyBEbyB3ZSBuZWVkIHByb3BlciByZXBsYWNlIHNlbWFudGljPyBUaGlzIGxlYWRzIHRvIGlzc3VlcyBpbiBlZGl0b3IgYmluZGluZ3MgYmVjYXVzZSB0aGV5IGRvbid0IHN3aXRjaCBzb3VyY2UuXG4gICAgLy8gdGhpcy55bW9kZWwuc2V0KCdzb3VyY2UnLCBuZXcgWS5UZXh0KHZhbHVlKSk7XG4gIH1cblxuICAvKipcbiAgICogUmVwbGFjZSBjb250ZW50IGZyb20gYHN0YXJ0JyB0byBgZW5kYCB3aXRoIGB2YWx1ZWAuXG4gICAqXG4gICAqIEBwYXJhbSBzdGFydDogVGhlIHN0YXJ0IGluZGV4IG9mIHRoZSByYW5nZSB0byByZXBsYWNlIChpbmNsdXNpdmUpLlxuICAgKlxuICAgKiBAcGFyYW0gZW5kOiBUaGUgZW5kIGluZGV4IG9mIHRoZSByYW5nZSB0byByZXBsYWNlIChleGNsdXNpdmUpLlxuICAgKlxuICAgKiBAcGFyYW0gdmFsdWU6IE5ldyBzb3VyY2UgKG9wdGlvbmFsKS5cbiAgICovXG4gIHB1YmxpYyB1cGRhdGVTb3VyY2Uoc3RhcnQ6IG51bWJlciwgZW5kOiBudW1iZXIsIHZhbHVlID0gJycpOiB2b2lkIHtcbiAgICB0aGlzLnRyYW5zYWN0KCgpID0+IHtcbiAgICAgIGNvbnN0IHlzb3VyY2UgPSB0aGlzLnlzb3VyY2U7XG4gICAgICAvLyBpbnNlcnQgYW5kIHRoZW4gZGVsZXRlLlxuICAgICAgLy8gVGhpcyBlbnN1cmVzIHRoYXQgdGhlIGN1cnNvciBwb3NpdGlvbiBpcyBhZGp1c3RlZCBhZnRlciB0aGUgcmVwbGFjZWQgY29udGVudC5cbiAgICAgIHlzb3VyY2UuaW5zZXJ0KHN0YXJ0LCB2YWx1ZSk7XG4gICAgICB5c291cmNlLmRlbGV0ZShzdGFydCArIHZhbHVlLmxlbmd0aCwgZW5kIC0gc3RhcnQpO1xuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSB0eXBlIG9mIHRoZSBjZWxsLlxuICAgKi9cbiAgZ2V0IGNlbGxfdHlwZSgpOiBhbnkge1xuICAgIHRocm93IG5ldyBFcnJvcignQSBZQmFzZUNlbGwgbXVzdCBub3QgYmUgY29uc3RydWN0ZWQnKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZXR1cm5zIHRoZSBtZXRhZGF0YSBhc3NvY2lhdGVkIHdpdGggdGhlIG5vdGVib29rLlxuICAgKlxuICAgKiBAcmV0dXJucyBOb3RlYm9vaydzIG1ldGFkYXRhLlxuICAgKi9cbiAgZ2V0TWV0YWRhdGEoKTogUGFydGlhbDxNZXRhZGF0YT4ge1xuICAgIHJldHVybiBkZWVwQ29weSh0aGlzLnltb2RlbC5nZXQoJ21ldGFkYXRhJykpO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldHMgdGhlIG1ldGFkYXRhIGFzc29jaWF0ZWQgd2l0aCB0aGUgbm90ZWJvb2suXG4gICAqXG4gICAqIEBwYXJhbSBtZXRhZGF0YTogTm90ZWJvb2sncyBtZXRhZGF0YS5cbiAgICovXG4gIHNldE1ldGFkYXRhKHZhbHVlOiBQYXJ0aWFsPE1ldGFkYXRhPik6IHZvaWQge1xuICAgIHRoaXMudHJhbnNhY3QoKCkgPT4ge1xuICAgICAgdGhpcy55bW9kZWwuc2V0KCdtZXRhZGF0YScsIGRlZXBDb3B5KHZhbHVlKSk7XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogU2VyaWFsaXplIHRoZSBtb2RlbCB0byBKU09OLlxuICAgKi9cbiAgdG9KU09OKCk6IG5iZm9ybWF0LklCYXNlQ2VsbCB7XG4gICAgcmV0dXJuIHtcbiAgICAgIGlkOiB0aGlzLmdldElkKCksXG4gICAgICBjZWxsX3R5cGU6IHRoaXMuY2VsbF90eXBlLFxuICAgICAgc291cmNlOiB0aGlzLmdldFNvdXJjZSgpLFxuICAgICAgbWV0YWRhdGE6IHRoaXMuZ2V0TWV0YWRhdGEoKVxuICAgIH07XG4gIH1cblxuICBwdWJsaWMgaXNEaXNwb3NlZCA9IGZhbHNlO1xuICBwdWJsaWMgeW1vZGVsOiBZLk1hcDxhbnk+O1xuICBwcml2YXRlIF91bmRvTWFuYWdlcjogWS5VbmRvTWFuYWdlciB8IG51bGwgPSBudWxsO1xuICBwcml2YXRlIF9jaGFuZ2VkID0gbmV3IFNpZ25hbDx0aGlzLCBtb2RlbHMuQ2VsbENoYW5nZTxNZXRhZGF0YT4+KHRoaXMpO1xuICBwcml2YXRlIF9wcmV2U291cmNlTGVuZ3RoOiBudW1iZXI7XG4gIHByaXZhdGUgX2F3YXJlbmVzczogQXdhcmVuZXNzIHwgbnVsbDtcbn1cblxuZXhwb3J0IGNsYXNzIFlDb2RlQ2VsbFxuICBleHRlbmRzIFlCYXNlQ2VsbDxtb2RlbHMuSVNoYXJlZEJhc2VDZWxsTWV0YWRhdGE+XG4gIGltcGxlbWVudHMgbW9kZWxzLklTaGFyZWRDb2RlQ2VsbFxue1xuICAvKipcbiAgICogVGhlIHR5cGUgb2YgdGhlIGNlbGwuXG4gICAqL1xuICBnZXQgY2VsbF90eXBlKCk6ICdjb2RlJyB7XG4gICAgcmV0dXJuICdjb2RlJztcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgY29kZSBjZWxsJ3MgcHJvbXB0IG51bWJlci4gV2lsbCBiZSBudWxsIGlmIHRoZSBjZWxsIGhhcyBub3QgYmVlbiBydW4uXG4gICAqL1xuICBnZXQgZXhlY3V0aW9uX2NvdW50KCk6IG51bWJlciB8IG51bGwge1xuICAgIHJldHVybiB0aGlzLnltb2RlbC5nZXQoJ2V4ZWN1dGlvbl9jb3VudCcpO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBjb2RlIGNlbGwncyBwcm9tcHQgbnVtYmVyLiBXaWxsIGJlIG51bGwgaWYgdGhlIGNlbGwgaGFzIG5vdCBiZWVuIHJ1bi5cbiAgICovXG4gIHNldCBleGVjdXRpb25fY291bnQoY291bnQ6IG51bWJlciB8IG51bGwpIHtcbiAgICB0aGlzLnRyYW5zYWN0KCgpID0+IHtcbiAgICAgIHRoaXMueW1vZGVsLnNldCgnZXhlY3V0aW9uX2NvdW50JywgY291bnQpO1xuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIEV4ZWN1dGlvbiwgZGlzcGxheSwgb3Igc3RyZWFtIG91dHB1dHMuXG4gICAqL1xuICBnZXRPdXRwdXRzKCk6IEFycmF5PG5iZm9ybWF0LklPdXRwdXQ+IHtcbiAgICByZXR1cm4gZGVlcENvcHkodGhpcy55bW9kZWwuZ2V0KCdvdXRwdXRzJykudG9BcnJheSgpKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZXBsYWNlIGFsbCBvdXRwdXRzLlxuICAgKi9cbiAgc2V0T3V0cHV0cyhvdXRwdXRzOiBBcnJheTxuYmZvcm1hdC5JT3V0cHV0Pik6IHZvaWQge1xuICAgIGNvbnN0IHlvdXRwdXRzID0gdGhpcy55bW9kZWwuZ2V0KCdvdXRwdXRzJykgYXMgWS5BcnJheTxuYmZvcm1hdC5JT3V0cHV0PjtcbiAgICB0aGlzLnRyYW5zYWN0KCgpID0+IHtcbiAgICAgIHlvdXRwdXRzLmRlbGV0ZSgwLCB5b3V0cHV0cy5sZW5ndGgpO1xuICAgICAgeW91dHB1dHMuaW5zZXJ0KDAsIG91dHB1dHMpO1xuICAgIH0sIGZhbHNlKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZXBsYWNlIGNvbnRlbnQgZnJvbSBgc3RhcnQnIHRvIGBlbmRgIHdpdGggYG91dHB1dHNgLlxuICAgKlxuICAgKiBAcGFyYW0gc3RhcnQ6IFRoZSBzdGFydCBpbmRleCBvZiB0aGUgcmFuZ2UgdG8gcmVwbGFjZSAoaW5jbHVzaXZlKS5cbiAgICpcbiAgICogQHBhcmFtIGVuZDogVGhlIGVuZCBpbmRleCBvZiB0aGUgcmFuZ2UgdG8gcmVwbGFjZSAoZXhjbHVzaXZlKS5cbiAgICpcbiAgICogQHBhcmFtIG91dHB1dHM6IE5ldyBvdXRwdXRzIChvcHRpb25hbCkuXG4gICAqL1xuICB1cGRhdGVPdXRwdXRzKFxuICAgIHN0YXJ0OiBudW1iZXIsXG4gICAgZW5kOiBudW1iZXIsXG4gICAgb3V0cHV0czogQXJyYXk8bmJmb3JtYXQuSU91dHB1dD4gPSBbXVxuICApOiB2b2lkIHtcbiAgICBjb25zdCB5b3V0cHV0cyA9IHRoaXMueW1vZGVsLmdldCgnb3V0cHV0cycpIGFzIFkuQXJyYXk8bmJmb3JtYXQuSU91dHB1dD47XG4gICAgY29uc3QgZmluID0gZW5kIDwgeW91dHB1dHMubGVuZ3RoID8gZW5kIC0gc3RhcnQgOiB5b3V0cHV0cy5sZW5ndGggLSBzdGFydDtcbiAgICB0aGlzLnRyYW5zYWN0KCgpID0+IHtcbiAgICAgIHlvdXRwdXRzLmRlbGV0ZShzdGFydCwgZmluKTtcbiAgICAgIHlvdXRwdXRzLmluc2VydChzdGFydCwgb3V0cHV0cyk7XG4gICAgfSwgZmFsc2UpO1xuICB9XG5cbiAgLyoqXG4gICAqIENyZWF0ZSBhIG5ldyBZQ29kZUNlbGwgdGhhdCBjYW4gYmUgaW5zZXJ0ZWQgaW50byBhIFlOb3RlYm9va1xuICAgKi9cbiAgcHVibGljIHN0YXRpYyBjcmVhdGUoaWQ/OiBzdHJpbmcpOiBZQ29kZUNlbGwge1xuICAgIGNvbnN0IGNlbGwgPSBzdXBlci5jcmVhdGUoaWQpO1xuICAgIGNlbGwueW1vZGVsLnNldCgnZXhlY3V0aW9uX2NvdW50JywgMCk7IC8vIGZvciBzb21lIGRlZmF1bHQgdmFsdWVcbiAgICBjZWxsLnltb2RlbC5zZXQoJ291dHB1dHMnLCBuZXcgWS5BcnJheTxuYmZvcm1hdC5JT3V0cHV0PigpKTtcbiAgICByZXR1cm4gY2VsbCBhcyBhbnk7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IFlDb2RlQ2VsbCB0aGF0IHdvcmtzIHN0YW5kYWxvbmUuIEl0IGNhbm5vdCBiZVxuICAgKiBpbnNlcnRlZCBpbnRvIGEgWU5vdGVib29rIGJlY2F1c2UgdGhlIFlqcyBtb2RlbCBpcyBhbHJlYWR5XG4gICAqIGF0dGFjaGVkIHRvIGFuIGFub255bW91cyBZLkRvYyBpbnN0YW5jZS5cbiAgICovXG4gIHB1YmxpYyBzdGF0aWMgY3JlYXRlU3RhbmRhbG9uZShpZD86IHN0cmluZyk6IFlDb2RlQ2VsbCB7XG4gICAgY29uc3QgY2VsbCA9IHN1cGVyLmNyZWF0ZVN0YW5kYWxvbmUoaWQpO1xuICAgIGNlbGwueW1vZGVsLnNldCgnZXhlY3V0aW9uX2NvdW50JywgbnVsbCk7IC8vIGZvciBzb21lIGRlZmF1bHQgdmFsdWVcbiAgICBjZWxsLnltb2RlbC5zZXQoJ291dHB1dHMnLCBuZXcgWS5BcnJheTxuYmZvcm1hdC5JT3V0cHV0PigpKTtcbiAgICByZXR1cm4gY2VsbCBhcyBhbnk7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IFlDb2RlQ2VsbCB0aGF0IGNhbiBiZSBpbnNlcnRlZCBpbnRvIGEgWU5vdGVib29rXG4gICAqXG4gICAqIEB0b2RvIGNsb25lIHNob3VsZCBvbmx5IGJlIGF2YWlsYWJsZSBpbiB0aGUgc3BlY2lmaWMgaW1wbGVtZW50YXRpb25zIGkuZS4gSVNoYXJlZENvZGVDZWxsXG4gICAqL1xuICBwdWJsaWMgY2xvbmUoKTogWUNvZGVDZWxsIHtcbiAgICBjb25zdCBjZWxsID0gc3VwZXIuY2xvbmUoKTtcbiAgICBjb25zdCB5b3V0cHV0cyA9IG5ldyBZLkFycmF5PG5iZm9ybWF0LklPdXRwdXQ+KCk7XG4gICAgeW91dHB1dHMuaW5zZXJ0KDAsIHRoaXMuZ2V0T3V0cHV0cygpKTtcbiAgICBjZWxsLnltb2RlbC5zZXQoJ2V4ZWN1dGlvbl9jb3VudCcsIHRoaXMuZXhlY3V0aW9uX2NvdW50KTsgLy8gZm9yIHNvbWUgZGVmYXVsdCB2YWx1ZVxuICAgIGNlbGwueW1vZGVsLnNldCgnb3V0cHV0cycsIHlvdXRwdXRzKTtcbiAgICByZXR1cm4gY2VsbCBhcyBhbnk7XG4gIH1cblxuICAvKipcbiAgICogU2VyaWFsaXplIHRoZSBtb2RlbCB0byBKU09OLlxuICAgKi9cbiAgdG9KU09OKCk6IG5iZm9ybWF0LklDb2RlQ2VsbCB7XG4gICAgcmV0dXJuIHtcbiAgICAgIGlkOiB0aGlzLmdldElkKCksXG4gICAgICBjZWxsX3R5cGU6ICdjb2RlJyxcbiAgICAgIHNvdXJjZTogdGhpcy5nZXRTb3VyY2UoKSxcbiAgICAgIG1ldGFkYXRhOiB0aGlzLmdldE1ldGFkYXRhKCksXG4gICAgICBvdXRwdXRzOiB0aGlzLmdldE91dHB1dHMoKSxcbiAgICAgIGV4ZWN1dGlvbl9jb3VudDogdGhpcy5leGVjdXRpb25fY291bnRcbiAgICB9O1xuICB9XG59XG5cbmV4cG9ydCBjbGFzcyBZUmF3Q2VsbFxuICBleHRlbmRzIFlCYXNlQ2VsbDxtb2RlbHMuSVNoYXJlZEJhc2VDZWxsTWV0YWRhdGE+XG4gIGltcGxlbWVudHMgbW9kZWxzLklTaGFyZWRSYXdDZWxsXG57XG4gIC8qKlxuICAgKiBDcmVhdGUgYSBuZXcgWVJhd0NlbGwgdGhhdCBjYW4gYmUgaW5zZXJ0ZWQgaW50byBhIFlOb3RlYm9va1xuICAgKi9cbiAgcHVibGljIHN0YXRpYyBjcmVhdGUoaWQ/OiBzdHJpbmcpOiBZUmF3Q2VsbCB7XG4gICAgcmV0dXJuIHN1cGVyLmNyZWF0ZShpZCkgYXMgYW55O1xuICB9XG5cbiAgLyoqXG4gICAqIENyZWF0ZSBhIG5ldyBZUmF3Q2VsbCB0aGF0IHdvcmtzIHN0YW5kYWxvbmUuIEl0IGNhbm5vdCBiZVxuICAgKiBpbnNlcnRlZCBpbnRvIGEgWU5vdGVib29rIGJlY2F1c2UgdGhlIFlqcyBtb2RlbCBpcyBhbHJlYWR5XG4gICAqIGF0dGFjaGVkIHRvIGFuIGFub255bW91cyBZLkRvYyBpbnN0YW5jZS5cbiAgICovXG4gIHB1YmxpYyBzdGF0aWMgY3JlYXRlU3RhbmRhbG9uZShpZD86IHN0cmluZyk6IFlSYXdDZWxsIHtcbiAgICByZXR1cm4gc3VwZXIuY3JlYXRlU3RhbmRhbG9uZShpZCkgYXMgYW55O1xuICB9XG5cbiAgLyoqXG4gICAqIFN0cmluZyBpZGVudGlmeWluZyB0aGUgdHlwZSBvZiBjZWxsLlxuICAgKi9cbiAgZ2V0IGNlbGxfdHlwZSgpOiAncmF3JyB7XG4gICAgcmV0dXJuICdyYXcnO1xuICB9XG5cbiAgLyoqXG4gICAqIFNlcmlhbGl6ZSB0aGUgbW9kZWwgdG8gSlNPTi5cbiAgICovXG4gIHRvSlNPTigpOiBuYmZvcm1hdC5JUmF3Q2VsbCB7XG4gICAgcmV0dXJuIHtcbiAgICAgIGlkOiB0aGlzLmdldElkKCksXG4gICAgICBjZWxsX3R5cGU6ICdyYXcnLFxuICAgICAgc291cmNlOiB0aGlzLmdldFNvdXJjZSgpLFxuICAgICAgbWV0YWRhdGE6IHRoaXMuZ2V0TWV0YWRhdGEoKSxcbiAgICAgIGF0dGFjaG1lbnRzOiB0aGlzLmdldEF0dGFjaG1lbnRzKClcbiAgICB9O1xuICB9XG59XG5cbmV4cG9ydCBjbGFzcyBZTWFya2Rvd25DZWxsXG4gIGV4dGVuZHMgWUJhc2VDZWxsPG1vZGVscy5JU2hhcmVkQmFzZUNlbGxNZXRhZGF0YT5cbiAgaW1wbGVtZW50cyBtb2RlbHMuSVNoYXJlZE1hcmtkb3duQ2VsbFxue1xuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IFlNYXJrZG93bkNlbGwgdGhhdCBjYW4gYmUgaW5zZXJ0ZWQgaW50byBhIFlOb3RlYm9va1xuICAgKi9cbiAgcHVibGljIHN0YXRpYyBjcmVhdGUoaWQ/OiBzdHJpbmcpOiBZTWFya2Rvd25DZWxsIHtcbiAgICByZXR1cm4gc3VwZXIuY3JlYXRlKGlkKSBhcyBhbnk7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IFlNYXJrZG93bkNlbGwgdGhhdCB3b3JrcyBzdGFuZGFsb25lLiBJdCBjYW5ub3QgYmVcbiAgICogaW5zZXJ0ZWQgaW50byBhIFlOb3RlYm9vayBiZWNhdXNlIHRoZSBZanMgbW9kZWwgaXMgYWxyZWFkeVxuICAgKiBhdHRhY2hlZCB0byBhbiBhbm9ueW1vdXMgWS5Eb2MgaW5zdGFuY2UuXG4gICAqL1xuICBwdWJsaWMgc3RhdGljIGNyZWF0ZVN0YW5kYWxvbmUoaWQ/OiBzdHJpbmcpOiBZTWFya2Rvd25DZWxsIHtcbiAgICByZXR1cm4gc3VwZXIuY3JlYXRlU3RhbmRhbG9uZShpZCkgYXMgYW55O1xuICB9XG5cbiAgLyoqXG4gICAqIFN0cmluZyBpZGVudGlmeWluZyB0aGUgdHlwZSBvZiBjZWxsLlxuICAgKi9cbiAgZ2V0IGNlbGxfdHlwZSgpOiAnbWFya2Rvd24nIHtcbiAgICByZXR1cm4gJ21hcmtkb3duJztcbiAgfVxuXG4gIC8qKlxuICAgKiBTZXJpYWxpemUgdGhlIG1vZGVsIHRvIEpTT04uXG4gICAqL1xuICB0b0pTT04oKTogbmJmb3JtYXQuSU1hcmtkb3duQ2VsbCB7XG4gICAgcmV0dXJuIHtcbiAgICAgIGlkOiB0aGlzLmdldElkKCksXG4gICAgICBjZWxsX3R5cGU6ICdtYXJrZG93bicsXG4gICAgICBzb3VyY2U6IHRoaXMuZ2V0U291cmNlKCksXG4gICAgICBtZXRhZGF0YTogdGhpcy5nZXRNZXRhZGF0YSgpLFxuICAgICAgYXR0YWNobWVudHM6IHRoaXMuZ2V0QXR0YWNobWVudHMoKVxuICAgIH07XG4gIH1cbn1cblxuZXhwb3J0IGRlZmF1bHQgWU5vdGVib29rO1xuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9