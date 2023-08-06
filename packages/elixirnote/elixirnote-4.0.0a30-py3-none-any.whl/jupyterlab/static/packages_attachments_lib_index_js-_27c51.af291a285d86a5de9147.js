"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_attachments_lib_index_js-_27c51"],{

/***/ "../../packages/attachments/lib/index.js":
/*!***********************************************!*\
  !*** ../../packages/attachments/lib/index.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "AttachmentsModel": () => (/* reexport safe */ _model__WEBPACK_IMPORTED_MODULE_0__.AttachmentsModel),
/* harmony export */   "AttachmentsResolver": () => (/* reexport safe */ _model__WEBPACK_IMPORTED_MODULE_0__.AttachmentsResolver)
/* harmony export */ });
/* harmony import */ var _model__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./model */ "../../packages/attachments/lib/model.js");
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module attachments
 */



/***/ }),

/***/ "../../packages/attachments/lib/model.js":
/*!***********************************************!*\
  !*** ../../packages/attachments/lib/model.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "AttachmentsModel": () => (/* binding */ AttachmentsModel),
/* harmony export */   "AttachmentsResolver": () => (/* binding */ AttachmentsResolver)
/* harmony export */ });
/* harmony import */ var _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/observables */ "webpack/sharing/consume/default/@jupyterlab/observables/@jupyterlab/observables");
/* harmony import */ var _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_observables__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_2__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/**
 * The default implementation of the IAttachmentsModel.
 */
class AttachmentsModel {
    /**
     * Construct a new observable outputs instance.
     */
    constructor(options = {}) {
        this._map = new _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_0__.ObservableMap();
        this._isDisposed = false;
        this._stateChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
        this._changed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
        this._modelDB = null;
        this._serialized = null;
        this._changeGuard = false;
        this.contentFactory =
            options.contentFactory || AttachmentsModel.defaultContentFactory;
        if (options.values) {
            for (const key of Object.keys(options.values)) {
                if (options.values[key] !== undefined) {
                    this.set(key, options.values[key]);
                }
            }
        }
        this._map.changed.connect(this._onMapChanged, this);
        // If we are given a IModelDB, keep an up-to-date
        // serialized copy of the AttachmentsModel in it.
        if (options.modelDB) {
            this._modelDB = options.modelDB;
            this._serialized = this._modelDB.createValue('attachments');
            if (this._serialized.get()) {
                this.fromJSON(this._serialized.get());
            }
            else {
                this._serialized.set(this.toJSON());
            }
            this._serialized.changed.connect(this._onSerializedChanged, this);
        }
    }
    /**
     * A signal emitted when the model state changes.
     */
    get stateChanged() {
        return this._stateChanged;
    }
    /**
     * A signal emitted when the model changes.
     */
    get changed() {
        return this._changed;
    }
    /**
     * The keys of the attachments in the model.
     */
    get keys() {
        return this._map.keys();
    }
    /**
     * Get the length of the items in the model.
     */
    get length() {
        return this._map.keys().length;
    }
    /**
     * Test whether the model is disposed.
     */
    get isDisposed() {
        return this._isDisposed;
    }
    /**
     * Dispose of the resources used by the model.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        this._isDisposed = true;
        this._map.dispose();
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal.clearData(this);
    }
    /**
     * Whether the specified key is set.
     */
    has(key) {
        return this._map.has(key);
    }
    /**
     * Get an item at the specified key.
     */
    get(key) {
        return this._map.get(key);
    }
    /**
     * Set the value at the specified key.
     */
    set(key, value) {
        // Normalize stream data.
        const item = this._createItem({ value });
        this._map.set(key, item);
    }
    /**
     * Remove the attachment whose name is the specified key
     */
    remove(key) {
        this._map.delete(key);
    }
    /**
     * Clear all of the attachments.
     */
    clear() {
        this._map.values().forEach((item) => {
            item.dispose();
        });
        this._map.clear();
    }
    /**
     * Deserialize the model from JSON.
     *
     * #### Notes
     * This will clear any existing data.
     */
    fromJSON(values) {
        this.clear();
        Object.keys(values).forEach(key => {
            if (values[key] !== undefined) {
                this.set(key, values[key]);
            }
        });
    }
    /**
     * Serialize the model to JSON.
     */
    toJSON() {
        const ret = {};
        for (const key of this._map.keys()) {
            ret[key] = this._map.get(key).toJSON();
        }
        return ret;
    }
    /**
     * Create an attachment item and hook up its signals.
     */
    _createItem(options) {
        const factory = this.contentFactory;
        const item = factory.createAttachmentModel(options);
        item.changed.connect(this._onGenericChange, this);
        return item;
    }
    /**
     * Handle a change to the list.
     */
    _onMapChanged(sender, args) {
        if (this._serialized && !this._changeGuard) {
            this._changeGuard = true;
            this._serialized.set(this.toJSON());
            this._changeGuard = false;
        }
        this._changed.emit(args);
        this._stateChanged.emit(void 0);
    }
    /**
     * If the serialized version of the outputs have changed due to a remote
     * action, then update the model accordingly.
     */
    _onSerializedChanged(sender, args) {
        if (!this._changeGuard) {
            this._changeGuard = true;
            this.fromJSON(args.newValue);
            this._changeGuard = false;
        }
    }
    /**
     * Handle a change to an item.
     */
    _onGenericChange() {
        this._stateChanged.emit(void 0);
    }
}
/**
 * The namespace for AttachmentsModel class statics.
 */
(function (AttachmentsModel) {
    /**
     * The default implementation of a `IAttachmentsModel.IContentFactory`.
     */
    class ContentFactory {
        /**
         * Create an attachment model.
         */
        createAttachmentModel(options) {
            return new _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__.AttachmentModel(options);
        }
    }
    AttachmentsModel.ContentFactory = ContentFactory;
    /**
     * The default attachment model factory.
     */
    AttachmentsModel.defaultContentFactory = new ContentFactory();
})(AttachmentsModel || (AttachmentsModel = {}));
/**
 * A resolver for cell attachments 'attachment:filename'.
 *
 * Will resolve to a data: url.
 */
class AttachmentsResolver {
    /**
     * Create an attachments resolver object.
     */
    constructor(options) {
        this._parent = options.parent || null;
        this._model = options.model;
    }
    /**
     * Resolve a relative url to a correct server path.
     */
    async resolveUrl(url) {
        if (this._parent && !url.startsWith('attachment:')) {
            return this._parent.resolveUrl(url);
        }
        return url;
    }
    /**
     * Get the download url of a given absolute server path.
     *
     * #### Notes
     * The returned URL may include a query parameter.
     */
    async getDownloadUrl(path) {
        if (this._parent && !path.startsWith('attachment:')) {
            return this._parent.getDownloadUrl(path);
        }
        // Return a data URL with the data of the url
        const key = path.slice('attachment:'.length);
        const attachment = this._model.get(key);
        if (attachment === undefined) {
            // Resolve with unprocessed path, to show as broken image
            return path;
        }
        const { data } = attachment;
        const mimeType = Object.keys(data)[0];
        // Only support known safe types:
        if (mimeType === undefined ||
            _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__.imageRendererFactory.mimeTypes.indexOf(mimeType) === -1) {
            throw new Error(`Cannot render unknown image mime type "${mimeType}".`);
        }
        const dataUrl = `data:${mimeType};base64,${data[mimeType]}`;
        return dataUrl;
    }
    /**
     * Whether the URL should be handled by the resolver
     * or not.
     */
    isLocal(url) {
        var _a, _b, _c;
        if (this._parent && !url.startsWith('attachment:')) {
            return (_c = (_b = (_a = this._parent).isLocal) === null || _b === void 0 ? void 0 : _b.call(_a, url)) !== null && _c !== void 0 ? _c : true;
        }
        return true;
    }
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfYXR0YWNobWVudHNfbGliX2luZGV4X2pzLV8yN2M1MS5hZjI5MWEyODVkODZhNWRlOTE0Ny5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7QUFBQTs7OytFQUcrRTtBQUMvRTs7O0dBR0c7QUFFcUI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUNUeEIsMENBQTBDO0FBQzFDLDJEQUEyRDtBQVMxQjtBQUtEO0FBR29CO0FBaUhwRDs7R0FFRztBQUNJLE1BQU0sZ0JBQWdCO0lBQzNCOztPQUVHO0lBQ0gsWUFBWSxVQUFzQyxFQUFFO1FBZ001QyxTQUFJLEdBQUcsSUFBSSxrRUFBYSxFQUFvQixDQUFDO1FBQzdDLGdCQUFXLEdBQUcsS0FBSyxDQUFDO1FBQ3BCLGtCQUFhLEdBQUcsSUFBSSxxREFBTSxDQUEwQixJQUFJLENBQUMsQ0FBQztRQUMxRCxhQUFRLEdBQUcsSUFBSSxxREFBTSxDQUFzQyxJQUFJLENBQUMsQ0FBQztRQUNqRSxhQUFRLEdBQW9CLElBQUksQ0FBQztRQUNqQyxnQkFBVyxHQUE0QixJQUFJLENBQUM7UUFDNUMsaUJBQVksR0FBRyxLQUFLLENBQUM7UUFyTTNCLElBQUksQ0FBQyxjQUFjO1lBQ2pCLE9BQU8sQ0FBQyxjQUFjLElBQUksZ0JBQWdCLENBQUMscUJBQXFCLENBQUM7UUFDbkUsSUFBSSxPQUFPLENBQUMsTUFBTSxFQUFFO1lBQ2xCLEtBQUssTUFBTSxHQUFHLElBQUksTUFBTSxDQUFDLElBQUksQ0FBQyxPQUFPLENBQUMsTUFBTSxDQUFDLEVBQUU7Z0JBQzdDLElBQUksT0FBTyxDQUFDLE1BQU0sQ0FBQyxHQUFHLENBQUMsS0FBSyxTQUFTLEVBQUU7b0JBQ3JDLElBQUksQ0FBQyxHQUFHLENBQUMsR0FBRyxFQUFFLE9BQU8sQ0FBQyxNQUFNLENBQUMsR0FBRyxDQUFFLENBQUMsQ0FBQztpQkFDckM7YUFDRjtTQUNGO1FBQ0QsSUFBSSxDQUFDLElBQUksQ0FBQyxPQUFPLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxh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LENBQUMsRUFBRSxDQUFDO1FBQzVELE9BQU8sT0FBTyxDQUFDO0lBQ2pCLENBQUM7SUFFRDs7O09BR0c7SUFDSCxPQUFPLENBQUMsR0FBVzs7UUFDakIsSUFBSSxJQUFJLENBQUMsT0FBTyxJQUFJLENBQUMsR0FBRyxDQUFDLFVBQVUsQ0FBQyxhQUFhLENBQUMsRUFBRTtZQUNsRCxPQUFPLHNCQUFJLENBQUMsT0FBTyxFQUFDLE9BQU8sbURBQUcsR0FBRyxDQUFDLG1DQUFJLElBQUksQ0FBQztTQUM1QztRQUNELE9BQU8sSUFBSSxDQUFDO0lBQ2QsQ0FBQztDQUlGIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2F0dGFjaG1lbnRzL3NyYy9pbmRleC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvYXR0YWNobWVudHMvc3JjL21vZGVsLnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8qIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG58IENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxufCBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxufC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgYXR0YWNobWVudHNcbiAqL1xuXG5leHBvcnQgKiBmcm9tICcuL21vZGVsJztcbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0ICogYXMgbmJmb3JtYXQgZnJvbSAnQGp1cHl0ZXJsYWIvbmJmb3JtYXQnO1xuaW1wb3J0IHtcbiAgSU1vZGVsREIsXG4gIElPYnNlcnZhYmxlTWFwLFxuICBJT2JzZXJ2YWJsZVZhbHVlLFxuICBPYnNlcnZhYmxlTWFwLFxuICBPYnNlcnZhYmxlVmFsdWVcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvb2JzZXJ2YWJsZXMnO1xuaW1wb3J0IHtcbiAgQXR0YWNobWVudE1vZGVsLFxuICBJQXR0YWNobWVudE1vZGVsLFxuICBpbWFnZVJlbmRlcmVyRmFjdG9yeVxufSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lJztcbmltcG9ydCB7IElSZW5kZXJNaW1lIH0gZnJvbSAnQGp1cHl0ZXJsYWIvcmVuZGVybWltZS1pbnRlcmZhY2VzJztcbmltcG9ydCB7IElEaXNwb3NhYmxlIH0gZnJvbSAnQGx1bWluby9kaXNwb3NhYmxlJztcbmltcG9ydCB7IElTaWduYWwsIFNpZ25hbCB9IGZyb20gJ0BsdW1pbm8vc2lnbmFsaW5nJztcblxuLyoqXG4gKiBUaGUgbW9kZWwgZm9yIGF0dGFjaG1lbnRzLlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElBdHRhY2htZW50c01vZGVsIGV4dGVuZHMgSURpc3Bvc2FibGUge1xuICAvKipcbiAgICogQSBzaWduYWwgZW1pdHRlZCB3aGVuIHRoZSBtb2RlbCBzdGF0ZSBjaGFuZ2VzLlxuICAgKi9cbiAgcmVhZG9ubHkgc3RhdGVDaGFuZ2VkOiBJU2lnbmFsPElBdHRhY2htZW50c01vZGVsLCB2b2lkPjtcblxuICAvKipcbiAgICogQSBzaWduYWwgZW1pdHRlZCB3aGVuIHRoZSBtb2RlbCBjaGFuZ2VzLlxuICAgKi9cbiAgcmVhZG9ubHkgY2hhbmdlZDogSVNpZ25hbDxJQXR0YWNobWVudHNNb2RlbCwgSUF0dGFjaG1lbnRzTW9kZWwuQ2hhbmdlZEFyZ3M+O1xuXG4gIC8qKlxuICAgKiBUaGUgbGVuZ3RoIG9mIHRoZSBpdGVtcyBpbiB0aGUgbW9kZWwuXG4gICAqL1xuICByZWFkb25seSBsZW5ndGg6IG51bWJlcjtcblxuICAvKipcbiAgICogVGhlIGtleXMgb2YgdGhlIGF0dGFjaG1lbnRzIGluIHRoZSBtb2RlbC5cbiAgICovXG4gIHJlYWRvbmx5IGtleXM6IFJlYWRvbmx5QXJyYXk8c3RyaW5nPjtcblxuICAvKipcbiAgICogVGhlIGF0dGFjaG1lbnQgY29udGVudCBmYWN0b3J5IHVzZWQgYnkgdGhlIG1vZGVsLlxuICAgKi9cbiAgcmVhZG9ubHkgY29udGVudEZhY3Rvcnk6IElBdHRhY2htZW50c01vZGVsLklDb250ZW50RmFjdG9yeTtcblxuICAvKipcbiAgICogV2hldGhlciB0aGUgc3BlY2lmaWVkIGtleSBpcyBzZXQuXG4gICAqL1xuICBoYXMoa2V5OiBzdHJpbmcpOiBib29sZWFuO1xuXG4gIC8qKlxuICAgKiBHZXQgYW4gaXRlbSBmb3IgdGhlIHNwZWNpZmllZCBrZXkuXG4gICAqL1xuICBnZXQoa2V5OiBzdHJpbmcpOiBJQXR0YWNobWVudE1vZGVsIHwgdW5kZWZpbmVkO1xuXG4gIC8qKlxuICAgKiBTZXQgdGhlIHZhbHVlIG9mIHRoZSBzcGVjaWZpZWQga2V5LlxuICAgKi9cbiAgc2V0KGtleTogc3RyaW5nLCBhdHRhY2htZW50OiBuYmZvcm1hdC5JTWltZUJ1bmRsZSk6IHZvaWQ7XG5cbiAgLyoqXG4gICAqIFJlbW92ZSB0aGUgYXR0YWNobWVudCB3aG9zZSBuYW1lIGlzIHRoZSBzcGVjaWZpZWQga2V5LlxuICAgKiBOb3RlIHRoYXQgdGhpcyBpcyBvcHRpb25hbCBvbmx5IHVudGlsIEp1cHl0ZXJsYWIgMi4wIHJlbGVhc2UuXG4gICAqL1xuICByZW1vdmU6IChrZXk6IHN0cmluZykgPT4gdm9pZDtcblxuICAvKipcbiAgICogQ2xlYXIgYWxsIG9mIHRoZSBhdHRhY2htZW50cy5cbiAgICovXG4gIGNsZWFyKCk6IHZvaWQ7XG5cbiAgLyoqXG4gICAqIERlc2VyaWFsaXplIHRoZSBtb2RlbCBmcm9tIEpTT04uXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyB3aWxsIGNsZWFyIGFueSBleGlzdGluZyBkYXRhLlxuICAgKi9cbiAgZnJvbUpTT04odmFsdWVzOiBuYmZvcm1hdC5JQXR0YWNobWVudHMpOiB2b2lkO1xuXG4gIC8qKlxuICAgKiBTZXJpYWxpemUgdGhlIG1vZGVsIHRvIEpTT04uXG4gICAqL1xuICB0b0pTT04oKTogbmJmb3JtYXQuSUF0dGFjaG1lbnRzO1xufVxuXG4vKipcbiAqIFRoZSBuYW1lc3BhY2UgZm9yIElBdHRhY2htZW50c01vZGVsIGludGVyZmFjZXMuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgSUF0dGFjaG1lbnRzTW9kZWwge1xuICAvKipcbiAgICogVGhlIG9wdGlvbnMgdXNlZCB0byBjcmVhdGUgYSBhdHRhY2htZW50cyBtb2RlbC5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMge1xuICAgIC8qKlxuICAgICAqIFRoZSBpbml0aWFsIHZhbHVlcyBmb3IgdGhlIG1vZGVsLlxuICAgICAqL1xuICAgIHZhbHVlcz86IG5iZm9ybWF0LklBdHRhY2htZW50cztcblxuICAgIC8qKlxuICAgICAqIFRoZSBhdHRhY2htZW50IGNvbnRlbnQgZmFjdG9yeSB1c2VkIGJ5IHRoZSBtb2RlbC5cbiAgICAgKlxuICAgICAqIElmIG5vdCBnaXZlbiwgYSBkZWZhdWx0IGZhY3Rvcnkgd2lsbCBiZSB1c2VkLlxuICAgICAqL1xuICAgIGNvbnRlbnRGYWN0b3J5PzogSUNvbnRlbnRGYWN0b3J5O1xuXG4gICAgLyoqXG4gICAgICogQW4gb3B0aW9uYWwgSU1vZGVsREIgdG8gc3RvcmUgdGhlIGF0dGFjaG1lbnRzIG1vZGVsLlxuICAgICAqL1xuICAgIG1vZGVsREI/OiBJTW9kZWxEQjtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIHR5cGUgYWxpYXMgZm9yIGNoYW5nZWQgYXJncy5cbiAgICovXG4gIGV4cG9ydCB0eXBlIENoYW5nZWRBcmdzID0gSU9ic2VydmFibGVNYXAuSUNoYW5nZWRBcmdzPElBdHRhY2htZW50TW9kZWw+O1xuXG4gIC8qKlxuICAgKiBUaGUgaW50ZXJmYWNlIGZvciBhbiBhdHRhY2htZW50IGNvbnRlbnQgZmFjdG9yeS5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUNvbnRlbnRGYWN0b3J5IHtcbiAgICAvKipcbiAgICAgKiBDcmVhdGUgYW4gYXR0YWNobWVudCBtb2RlbC5cbiAgICAgKi9cbiAgICBjcmVhdGVBdHRhY2htZW50TW9kZWwob3B0aW9uczogSUF0dGFjaG1lbnRNb2RlbC5JT3B0aW9ucyk6IElBdHRhY2htZW50TW9kZWw7XG4gIH1cbn1cblxuLyoqXG4gKiBUaGUgZGVmYXVsdCBpbXBsZW1lbnRhdGlvbiBvZiB0aGUgSUF0dGFjaG1lbnRzTW9kZWwuXG4gKi9cbmV4cG9ydCBjbGFzcyBBdHRhY2htZW50c01vZGVsIGltcGxlbWVudHMgSUF0dGFjaG1lbnRzTW9kZWwge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IG9ic2VydmFibGUgb3V0cHV0cyBpbnN0YW5jZS5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IElBdHRhY2htZW50c01vZGVsLklPcHRpb25zID0ge30pIHtcbiAgICB0aGlzLmNvbnRlbnRGYWN0b3J5ID1cbiAgICAgIG9wdGlvbnMuY29udGVudEZhY3RvcnkgfHwgQXR0YWNobWVudHNNb2RlbC5kZWZhdWx0Q29udGVudEZhY3Rvcnk7XG4gICAgaWYgKG9wdGlvbnMudmFsdWVzKSB7XG4gICAgICBmb3IgKGNvbnN0IGtleSBvZiBPYmplY3Qua2V5cyhvcHRpb25zLnZhbHVlcykpIHtcbiAgICAgICAgaWYgKG9wdGlvbnMudmFsdWVzW2tleV0gIT09IHVuZGVmaW5lZCkge1xuICAgICAgICAgIHRoaXMuc2V0KGtleSwgb3B0aW9ucy52YWx1ZXNba2V5XSEpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfVxuICAgIHRoaXMuX21hcC5jaGFuZ2VkLmNvbm5lY3QodGhpcy5fb25NYXBDaGFuZ2VkLCB0aGlzKTtcblxuICAgIC8vIElmIHdlIGFyZSBnaXZlbiBhIElNb2RlbERCLCBrZWVwIGFuIHVwLXRvLWRhdGVcbiAgICAvLyBzZXJpYWxpemVkIGNvcHkgb2YgdGhlIEF0dGFjaG1lbnRzTW9kZWwgaW4gaXQuXG4gICAgaWYgKG9wdGlvbnMubW9kZWxEQikge1xuICAgICAgdGhpcy5fbW9kZWxEQiA9IG9wdGlvbnMubW9kZWxEQjtcbiAgICAgIHRoaXMuX3NlcmlhbGl6ZWQgPSB0aGlzLl9tb2RlbERCLmNyZWF0ZVZhbHVlKCdhdHRhY2htZW50cycpO1xuICAgICAgaWYgKHRoaXMuX3NlcmlhbGl6ZWQuZ2V0KCkpIHtcbiAgICAgICAgdGhpcy5mcm9tSlNPTih0aGlzLl9zZXJpYWxpemVkLmdldCgpIGFzIG5iZm9ybWF0LklBdHRhY2htZW50cyk7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICB0aGlzLl9zZXJpYWxpemVkLnNldCh0aGlzLnRvSlNPTigpKTtcbiAgICAgIH1cbiAgICAgIHRoaXMuX3NlcmlhbGl6ZWQuY2hhbmdlZC5jb25uZWN0KHRoaXMuX29uU2VyaWFsaXplZENoYW5nZWQsIHRoaXMpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBBIHNpZ25hbCBlbWl0dGVkIHdoZW4gdGhlIG1vZGVsIHN0YXRlIGNoYW5nZXMuXG4gICAqL1xuICBnZXQgc3RhdGVDaGFuZ2VkKCk6IElTaWduYWw8SUF0dGFjaG1lbnRzTW9kZWwsIHZvaWQ+IHtcbiAgICByZXR1cm4gdGhpcy5fc3RhdGVDaGFuZ2VkO1xuICB9XG5cbiAgLyoqXG4gICAqIEEgc2lnbmFsIGVtaXR0ZWQgd2hlbiB0aGUgbW9kZWwgY2hhbmdlcy5cbiAgICovXG4gIGdldCBjaGFuZ2VkKCk6IElTaWduYWw8dGhpcywgSUF0dGFjaG1lbnRzTW9kZWwuQ2hhbmdlZEFyZ3M+IHtcbiAgICByZXR1cm4gdGhpcy5fY2hhbmdlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUga2V5cyBvZiB0aGUgYXR0YWNobWVudHMgaW4gdGhlIG1vZGVsLlxuICAgKi9cbiAgZ2V0IGtleXMoKTogUmVhZG9ubHlBcnJheTxzdHJpbmc+IHtcbiAgICByZXR1cm4gdGhpcy5fbWFwLmtleXMoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgdGhlIGxlbmd0aCBvZiB0aGUgaXRlbXMgaW4gdGhlIG1vZGVsLlxuICAgKi9cbiAgZ2V0IGxlbmd0aCgpOiBudW1iZXIge1xuICAgIHJldHVybiB0aGlzLl9tYXAua2V5cygpLmxlbmd0aDtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgYXR0YWNobWVudCBjb250ZW50IGZhY3RvcnkgdXNlZCBieSB0aGUgbW9kZWwuXG4gICAqL1xuICByZWFkb25seSBjb250ZW50RmFjdG9yeTogSUF0dGFjaG1lbnRzTW9kZWwuSUNvbnRlbnRGYWN0b3J5O1xuXG4gIC8qKlxuICAgKiBUZXN0IHdoZXRoZXIgdGhlIG1vZGVsIGlzIGRpc3Bvc2VkLlxuICAgKi9cbiAgZ2V0IGlzRGlzcG9zZWQoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuX2lzRGlzcG9zZWQ7XG4gIH1cblxuICAvKipcbiAgICogRGlzcG9zZSBvZiB0aGUgcmVzb3VyY2VzIHVzZWQgYnkgdGhlIG1vZGVsLlxuICAgKi9cbiAgZGlzcG9zZSgpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIHRoaXMuX2lzRGlzcG9zZWQgPSB0cnVlO1xuICAgIHRoaXMuX21hcC5kaXNwb3NlKCk7XG4gICAgU2lnbmFsLmNsZWFyRGF0YSh0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBXaGV0aGVyIHRoZSBzcGVjaWZpZWQga2V5IGlzIHNldC5cbiAgICovXG4gIGhhcyhrZXk6IHN0cmluZyk6IGJvb2xlYW4ge1xuICAgIHJldHVybiB0aGlzLl9tYXAuaGFzKGtleSk7XG4gIH1cblxuICAvKipcbiAgICogR2V0IGFuIGl0ZW0gYXQgdGhlIHNwZWNpZmllZCBrZXkuXG4gICAqL1xuICBnZXQoa2V5OiBzdHJpbmcpOiBJQXR0YWNobWVudE1vZGVsIHwgdW5kZWZpbmVkIHtcbiAgICByZXR1cm4gdGhpcy5fbWFwLmdldChrZXkpO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldCB0aGUgdmFsdWUgYXQgdGhlIHNwZWNpZmllZCBrZXkuXG4gICAqL1xuICBzZXQoa2V5OiBzdHJpbmcsIHZhbHVlOiBuYmZvcm1hdC5JTWltZUJ1bmRsZSk6IHZvaWQge1xuICAgIC8vIE5vcm1hbGl6ZSBzdHJlYW0gZGF0YS5cbiAgICBjb25zdCBpdGVtID0gdGhpcy5fY3JlYXRlSXRlbSh7IHZhbHVlIH0pO1xuICAgIHRoaXMuX21hcC5zZXQoa2V5LCBpdGVtKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW1vdmUgdGhlIGF0dGFjaG1lbnQgd2hvc2UgbmFtZSBpcyB0aGUgc3BlY2lmaWVkIGtleVxuICAgKi9cbiAgcmVtb3ZlKGtleTogc3RyaW5nKTogdm9pZCB7XG4gICAgdGhpcy5fbWFwLmRlbGV0ZShrZXkpO1xuICB9XG5cbiAgLyoqXG4gICAqIENsZWFyIGFsbCBvZiB0aGUgYXR0YWNobWVudHMuXG4gICAqL1xuICBjbGVhcigpOiB2b2lkIHtcbiAgICB0aGlzLl9tYXAudmFsdWVzKCkuZm9yRWFjaCgoaXRlbTogSUF0dGFjaG1lbnRNb2RlbCkgPT4ge1xuICAgICAgaXRlbS5kaXNwb3NlKCk7XG4gICAgfSk7XG4gICAgdGhpcy5fbWFwLmNsZWFyKCk7XG4gIH1cblxuICAvKipcbiAgICogRGVzZXJpYWxpemUgdGhlIG1vZGVsIGZyb20gSlNPTi5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGlzIHdpbGwgY2xlYXIgYW55IGV4aXN0aW5nIGRhdGEuXG4gICAqL1xuICBmcm9tSlNPTih2YWx1ZXM6IG5iZm9ybWF0LklBdHRhY2htZW50cyk6IHZvaWQge1xuICAgIHRoaXMuY2xlYXIoKTtcbiAgICBPYmplY3Qua2V5cyh2YWx1ZXMpLmZvckVhY2goa2V5ID0+IHtcbiAgICAgIGlmICh2YWx1ZXNba2V5XSAhPT0gdW5kZWZpbmVkKSB7XG4gICAgICAgIHRoaXMuc2V0KGtleSwgdmFsdWVzW2tleV0hKTtcbiAgICAgIH1cbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZXJpYWxpemUgdGhlIG1vZGVsIHRvIEpTT04uXG4gICAqL1xuICB0b0pTT04oKTogbmJmb3JtYXQuSUF0dGFjaG1lbnRzIHtcbiAgICBjb25zdCByZXQ6IG5iZm9ybWF0LklBdHRhY2htZW50cyA9IHt9O1xuICAgIGZvciAoY29uc3Qga2V5IG9mIHRoaXMuX21hcC5rZXlzKCkpIHtcbiAgICAgIHJldFtrZXldID0gdGhpcy5fbWFwLmdldChrZXkpIS50b0pTT04oKTtcbiAgICB9XG4gICAgcmV0dXJuIHJldDtcbiAgfVxuXG4gIC8qKlxuICAgKiBDcmVhdGUgYW4gYXR0YWNobWVudCBpdGVtIGFuZCBob29rIHVwIGl0cyBzaWduYWxzLlxuICAgKi9cbiAgcHJpdmF0ZSBfY3JlYXRlSXRlbShvcHRpb25zOiBJQXR0YWNobWVudE1vZGVsLklPcHRpb25zKTogSUF0dGFjaG1lbnRNb2RlbCB7XG4gICAgY29uc3QgZmFjdG9yeSA9IHRoaXMuY29udGVudEZhY3Rvcnk7XG4gICAgY29uc3QgaXRlbSA9IGZhY3RvcnkuY3JlYXRlQXR0YWNobWVudE1vZGVsKG9wdGlvbnMpO1xuICAgIGl0ZW0uY2hhbmdlZC5jb25uZWN0KHRoaXMuX29uR2VuZXJpY0NoYW5nZSwgdGhpcyk7XG4gICAgcmV0dXJuIGl0ZW07XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGEgY2hhbmdlIHRvIHRoZSBsaXN0LlxuICAgKi9cbiAgcHJpdmF0ZSBfb25NYXBDaGFuZ2VkKFxuICAgIHNlbmRlcjogSU9ic2VydmFibGVNYXA8SUF0dGFjaG1lbnRNb2RlbD4sXG4gICAgYXJnczogSU9ic2VydmFibGVNYXAuSUNoYW5nZWRBcmdzPElBdHRhY2htZW50TW9kZWw+XG4gICkge1xuICAgIGlmICh0aGlzLl9zZXJpYWxpemVkICYmICF0aGlzLl9jaGFuZ2VHdWFyZCkge1xuICAgICAgdGhpcy5fY2hhbmdlR3VhcmQgPSB0cnVlO1xuICAgICAgdGhpcy5fc2VyaWFsaXplZC5zZXQodGhpcy50b0pTT04oKSk7XG4gICAgICB0aGlzLl9jaGFuZ2VHdWFyZCA9IGZhbHNlO1xuICAgIH1cbiAgICB0aGlzLl9jaGFuZ2VkLmVtaXQoYXJncyk7XG4gICAgdGhpcy5fc3RhdGVDaGFuZ2VkLmVtaXQodm9pZCAwKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBJZiB0aGUgc2VyaWFsaXplZCB2ZXJzaW9uIG9mIHRoZSBvdXRwdXRzIGhhdmUgY2hhbmdlZCBkdWUgdG8gYSByZW1vdGVcbiAgICogYWN0aW9uLCB0aGVuIHVwZGF0ZSB0aGUgbW9kZWwgYWNjb3JkaW5nbHkuXG4gICAqL1xuICBwcml2YXRlIF9vblNlcmlhbGl6ZWRDaGFuZ2VkKFxuICAgIHNlbmRlcjogSU9ic2VydmFibGVWYWx1ZSxcbiAgICBhcmdzOiBPYnNlcnZhYmxlVmFsdWUuSUNoYW5nZWRBcmdzXG4gICkge1xuICAgIGlmICghdGhpcy5fY2hhbmdlR3VhcmQpIHtcbiAgICAgIHRoaXMuX2NoYW5nZUd1YXJkID0gdHJ1ZTtcbiAgICAgIHRoaXMuZnJvbUpTT04oYXJncy5uZXdWYWx1ZSBhcyBuYmZvcm1hdC5JQXR0YWNobWVudHMpO1xuICAgICAgdGhpcy5fY2hhbmdlR3VhcmQgPSBmYWxzZTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGEgY2hhbmdlIHRvIGFuIGl0ZW0uXG4gICAqL1xuICBwcml2YXRlIF9vbkdlbmVyaWNDaGFuZ2UoKTogdm9pZCB7XG4gICAgdGhpcy5fc3RhdGVDaGFuZ2VkLmVtaXQodm9pZCAwKTtcbiAgfVxuXG4gIHByaXZhdGUgX21hcCA9IG5ldyBPYnNlcnZhYmxlTWFwPElBdHRhY2htZW50TW9kZWw+KCk7XG4gIHByaXZhdGUgX2lzRGlzcG9zZWQgPSBmYWxzZTtcbiAgcHJpdmF0ZSBfc3RhdGVDaGFuZ2VkID0gbmV3IFNpZ25hbDxJQXR0YWNobWVudHNNb2RlbCwgdm9pZD4odGhpcyk7XG4gIHByaXZhdGUgX2NoYW5nZWQgPSBuZXcgU2lnbmFsPHRoaXMsIElBdHRhY2htZW50c01vZGVsLkNoYW5nZWRBcmdzPih0aGlzKTtcbiAgcHJpdmF0ZSBfbW9kZWxEQjogSU1vZGVsREIgfCBudWxsID0gbnVsbDtcbiAgcHJpdmF0ZSBfc2VyaWFsaXplZDogSU9ic2VydmFibGVWYWx1ZSB8IG51bGwgPSBudWxsO1xuICBwcml2YXRlIF9jaGFuZ2VHdWFyZCA9IGZhbHNlO1xufVxuXG4vKipcbiAqIFRoZSBuYW1lc3BhY2UgZm9yIEF0dGFjaG1lbnRzTW9kZWwgY2xhc3Mgc3RhdGljcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBBdHRhY2htZW50c01vZGVsIHtcbiAgLyoqXG4gICAqIFRoZSBkZWZhdWx0IGltcGxlbWVudGF0aW9uIG9mIGEgYElBdHRhY2htZW50c01vZGVsLklDb250ZW50RmFjdG9yeWAuXG4gICAqL1xuICBleHBvcnQgY2xhc3MgQ29udGVudEZhY3RvcnkgaW1wbGVtZW50cyBJQXR0YWNobWVudHNNb2RlbC5JQ29udGVudEZhY3Rvcnkge1xuICAgIC8qKlxuICAgICAqIENyZWF0ZSBhbiBhdHRhY2htZW50IG1vZGVsLlxuICAgICAqL1xuICAgIGNyZWF0ZUF0dGFjaG1lbnRNb2RlbChcbiAgICAgIG9wdGlvbnM6IElBdHRhY2htZW50TW9kZWwuSU9wdGlvbnNcbiAgICApOiBJQXR0YWNobWVudE1vZGVsIHtcbiAgICAgIHJldHVybiBuZXcgQXR0YWNobWVudE1vZGVsKG9wdGlvbnMpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgZGVmYXVsdCBhdHRhY2htZW50IG1vZGVsIGZhY3RvcnkuXG4gICAqL1xuICBleHBvcnQgY29uc3QgZGVmYXVsdENvbnRlbnRGYWN0b3J5ID0gbmV3IENvbnRlbnRGYWN0b3J5KCk7XG59XG5cbi8qKlxuICogQSByZXNvbHZlciBmb3IgY2VsbCBhdHRhY2htZW50cyAnYXR0YWNobWVudDpmaWxlbmFtZScuXG4gKlxuICogV2lsbCByZXNvbHZlIHRvIGEgZGF0YTogdXJsLlxuICovXG5leHBvcnQgY2xhc3MgQXR0YWNobWVudHNSZXNvbHZlciBpbXBsZW1lbnRzIElSZW5kZXJNaW1lLklSZXNvbHZlciB7XG4gIC8qKlxuICAgKiBDcmVhdGUgYW4gYXR0YWNobWVudHMgcmVzb2x2ZXIgb2JqZWN0LlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogQXR0YWNobWVudHNSZXNvbHZlci5JT3B0aW9ucykge1xuICAgIHRoaXMuX3BhcmVudCA9IG9wdGlvbnMucGFyZW50IHx8IG51bGw7XG4gICAgdGhpcy5fbW9kZWwgPSBvcHRpb25zLm1vZGVsO1xuICB9XG4gIC8qKlxuICAgKiBSZXNvbHZlIGEgcmVsYXRpdmUgdXJsIHRvIGEgY29ycmVjdCBzZXJ2ZXIgcGF0aC5cbiAgICovXG4gIGFzeW5jIHJlc29sdmVVcmwodXJsOiBzdHJpbmcpOiBQcm9taXNlPHN0cmluZz4ge1xuICAgIGlmICh0aGlzLl9wYXJlbnQgJiYgIXVybC5zdGFydHNXaXRoKCdhdHRhY2htZW50OicpKSB7XG4gICAgICByZXR1cm4gdGhpcy5fcGFyZW50LnJlc29sdmVVcmwodXJsKTtcbiAgICB9XG4gICAgcmV0dXJuIHVybDtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgdGhlIGRvd25sb2FkIHVybCBvZiBhIGdpdmVuIGFic29sdXRlIHNlcnZlciBwYXRoLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoZSByZXR1cm5lZCBVUkwgbWF5IGluY2x1ZGUgYSBxdWVyeSBwYXJhbWV0ZXIuXG4gICAqL1xuICBhc3luYyBnZXREb3dubG9hZFVybChwYXRoOiBzdHJpbmcpOiBQcm9taXNlPHN0cmluZz4ge1xuICAgIGlmICh0aGlzLl9wYXJlbnQgJiYgIXBhdGguc3RhcnRzV2l0aCgnYXR0YWNobWVudDonKSkge1xuICAgICAgcmV0dXJuIHRoaXMuX3BhcmVudC5nZXREb3dubG9hZFVybChwYXRoKTtcbiAgICB9XG4gICAgLy8gUmV0dXJuIGEgZGF0YSBVUkwgd2l0aCB0aGUgZGF0YSBvZiB0aGUgdXJsXG4gICAgY29uc3Qga2V5ID0gcGF0aC5zbGljZSgnYXR0YWNobWVudDonLmxlbmd0aCk7XG4gICAgY29uc3QgYXR0YWNobWVudCA9IHRoaXMuX21vZGVsLmdldChrZXkpO1xuICAgIGlmIChhdHRhY2htZW50ID09PSB1bmRlZmluZWQpIHtcbiAgICAgIC8vIFJlc29sdmUgd2l0aCB1bnByb2Nlc3NlZCBwYXRoLCB0byBzaG93IGFzIGJyb2tlbiBpbWFnZVxuICAgICAgcmV0dXJuIHBhdGg7XG4gICAgfVxuICAgIGNvbnN0IHsgZGF0YSB9ID0gYXR0YWNobWVudDtcbiAgICBjb25zdCBtaW1lVHlwZSA9IE9iamVjdC5rZXlzKGRhdGEpWzBdO1xuICAgIC8vIE9ubHkgc3VwcG9ydCBrbm93biBzYWZlIHR5cGVzOlxuICAgIGlmIChcbiAgICAgIG1pbWVUeXBlID09PSB1bmRlZmluZWQgfHxcbiAgICAgIGltYWdlUmVuZGVyZXJGYWN0b3J5Lm1pbWVUeXBlcy5pbmRleE9mKG1pbWVUeXBlKSA9PT0gLTFcbiAgICApIHtcbiAgICAgIHRocm93IG5ldyBFcnJvcihgQ2Fubm90IHJlbmRlciB1bmtub3duIGltYWdlIG1pbWUgdHlwZSBcIiR7bWltZVR5cGV9XCIuYCk7XG4gICAgfVxuICAgIGNvbnN0IGRhdGFVcmwgPSBgZGF0YToke21pbWVUeXBlfTtiYXNlNjQsJHtkYXRhW21pbWVUeXBlXX1gO1xuICAgIHJldHVybiBkYXRhVXJsO1xuICB9XG5cbiAgLyoqXG4gICAqIFdoZXRoZXIgdGhlIFVSTCBzaG91bGQgYmUgaGFuZGxlZCBieSB0aGUgcmVzb2x2ZXJcbiAgICogb3Igbm90LlxuICAgKi9cbiAgaXNMb2NhbCh1cmw6IHN0cmluZyk6IGJvb2xlYW4ge1xuICAgIGlmICh0aGlzLl9wYXJlbnQgJiYgIXVybC5zdGFydHNXaXRoKCdhdHRhY2htZW50OicpKSB7XG4gICAgICByZXR1cm4gdGhpcy5fcGFyZW50LmlzTG9jYWw/Lih1cmwpID8/IHRydWU7XG4gICAgfVxuICAgIHJldHVybiB0cnVlO1xuICB9XG5cbiAgcHJpdmF0ZSBfbW9kZWw6IElBdHRhY2htZW50c01vZGVsO1xuICBwcml2YXRlIF9wYXJlbnQ6IElSZW5kZXJNaW1lLklSZXNvbHZlciB8IG51bGw7XG59XG5cbi8qKlxuICogVGhlIG5hbWVzcGFjZSBmb3IgYEF0dGFjaG1lbnRzUmVzb2x2ZXJgIGNsYXNzIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgQXR0YWNobWVudHNSZXNvbHZlciB7XG4gIC8qKlxuICAgKiBUaGUgb3B0aW9ucyB1c2VkIHRvIGNyZWF0ZSBhbiBBdHRhY2htZW50c1Jlc29sdmVyLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIGF0dGFjaG1lbnRzIG1vZGVsIHRvIHJlc29sdmUgYWdhaW5zdC5cbiAgICAgKi9cbiAgICBtb2RlbDogSUF0dGFjaG1lbnRzTW9kZWw7XG5cbiAgICAvKipcbiAgICAgKiBBIHBhcmVudCByZXNvbHZlciB0byB1c2UgaWYgdGhlIFVSTC9wYXRoIGlzIG5vdCBmb3IgYW4gYXR0YWNobWVudC5cbiAgICAgKi9cbiAgICBwYXJlbnQ/OiBJUmVuZGVyTWltZS5JUmVzb2x2ZXI7XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==