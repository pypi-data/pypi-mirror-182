"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_json-extension_lib_index_js"],{

/***/ "../../packages/json-extension/lib/component.js":
/*!******************************************************!*\
  !*** ../../packages/json-extension/lib/component.js ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Component": () => (/* binding */ Component)
/* harmony export */ });
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_highlighter__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-highlighter */ "webpack/sharing/consume/default/react-highlighter/react-highlighter");
/* harmony import */ var react_highlighter__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_highlighter__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var react_json_tree__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react-json-tree */ "webpack/sharing/consume/default/react-json-tree/react-json-tree");
/* harmony import */ var react_json_tree__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(react_json_tree__WEBPACK_IMPORTED_MODULE_5__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.






/**
 * A component that renders JSON data as a collapsible tree.
 */
class Component extends react__WEBPACK_IMPORTED_MODULE_3__.Component {
    constructor() {
        super(...arguments);
        this.state = { filter: '', value: '' };
        this.timer = 0;
        this.handleChange = (event) => {
            const { value } = event.target;
            this.setState({ value });
            window.clearTimeout(this.timer);
            this.timer = window.setTimeout(() => {
                this.setState({ filter: value });
            }, 300);
        };
    }
    render() {
        const translator = this.props.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator;
        const trans = translator.load('jupyterlab');
        const { data, metadata } = this.props;
        const root = metadata && metadata.root ? metadata.root : 'root';
        const keyPaths = this.state.filter
            ? filterPaths(data, this.state.filter, [root])
            : [root];
        return (react__WEBPACK_IMPORTED_MODULE_3__.createElement("div", { className: "container" },
            react__WEBPACK_IMPORTED_MODULE_3__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.InputGroup, { className: "filter", type: "text", placeholder: trans.__('Filter…'), onChange: this.handleChange, value: this.state.value, rightIcon: "ui-components:search" }),
            react__WEBPACK_IMPORTED_MODULE_3__.createElement(react_json_tree__WEBPACK_IMPORTED_MODULE_5__.JSONTree, { data: data, collectionLimit: 100, theme: {
                    extend: theme,
                    valueLabel: 'cm-variable',
                    valueText: 'cm-string',
                    nestedNodeItemString: 'cm-comment'
                }, invertTheme: false, keyPath: [root], getItemString: (type, data, itemType, itemString) => Array.isArray(data) ? (
                // Always display array type and the number of items i.e. "[] 2 items".
                react__WEBPACK_IMPORTED_MODULE_3__.createElement("span", null,
                    itemType,
                    " ",
                    itemString)) : Object.keys(data).length === 0 ? (
                // Only display object type when it's empty i.e. "{}".
                react__WEBPACK_IMPORTED_MODULE_3__.createElement("span", null, itemType)) : (null // Upstream typings don't accept null, but it should be ok
                ), labelRenderer: ([label, type]) => {
                    // let className = 'cm-variable';
                    // if (type === 'root') {
                    //   className = 'cm-variable-2';
                    // }
                    // if (type === 'array') {
                    //   className = 'cm-variable-2';
                    // }
                    // if (type === 'Object') {
                    //   className = 'cm-variable-3';
                    // }
                    return (react__WEBPACK_IMPORTED_MODULE_3__.createElement("span", { className: "cm-keyword" },
                        react__WEBPACK_IMPORTED_MODULE_3__.createElement((react_highlighter__WEBPACK_IMPORTED_MODULE_4___default()), { search: this.state.filter, matchStyle: { backgroundColor: 'yellow' } }, `${label}: `)));
                }, valueRenderer: raw => {
                    let className = 'cm-string';
                    if (typeof raw === 'number') {
                        className = 'cm-number';
                    }
                    if (raw === 'true' || raw === 'false') {
                        className = 'cm-keyword';
                    }
                    return (react__WEBPACK_IMPORTED_MODULE_3__.createElement("span", { className: className },
                        react__WEBPACK_IMPORTED_MODULE_3__.createElement((react_highlighter__WEBPACK_IMPORTED_MODULE_4___default()), { search: this.state.filter, matchStyle: { backgroundColor: 'yellow' } }, `${raw}`)));
                }, shouldExpandNode: (keyPath, data, level) => metadata && metadata.expanded
                    ? true
                    : keyPaths.join(',').includes(keyPath.join(',')) })));
    }
}
// Provide an invalid theme object (this is on purpose!) to invalidate the
// react-json-tree's inline styles that override CodeMirror CSS classes
const theme = {
    scheme: 'jupyter',
    base00: 'invalid',
    base01: 'invalid',
    base02: 'invalid',
    base03: 'invalid',
    base04: 'invalid',
    base05: 'invalid',
    base06: 'invalid',
    base07: 'invalid',
    base08: 'invalid',
    base09: 'invalid',
    base0A: 'invalid',
    base0B: 'invalid',
    base0C: 'invalid',
    base0D: 'invalid',
    base0E: 'invalid',
    base0F: 'invalid',
    author: 'invalid'
};
function objectIncludes(data, query) {
    return JSON.stringify(data).includes(query);
}
function filterPaths(data, query, parent = ['root']) {
    if (_lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__.JSONExt.isArray(data)) {
        return data.reduce((result, item, index) => {
            if (item && typeof item === 'object' && objectIncludes(item, query)) {
                return [
                    ...result,
                    [index, ...parent].join(','),
                    ...filterPaths(item, query, [index, ...parent])
                ];
            }
            return result;
        }, []);
    }
    if (_lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__.JSONExt.isObject(data)) {
        return Object.keys(data).reduce((result, key) => {
            const item = data[key];
            if (item &&
                typeof item === 'object' &&
                (key.includes(query) || objectIncludes(item, query))) {
                return [
                    ...result,
                    [key, ...parent].join(','),
                    ...filterPaths(item, query, [key, ...parent])
                ];
            }
            return result;
        }, []);
    }
    return [];
}


/***/ }),

/***/ "../../packages/json-extension/lib/index.js":
/*!**************************************************!*\
  !*** ../../packages/json-extension/lib/index.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "MIME_TYPE": () => (/* binding */ MIME_TYPE),
/* harmony export */   "RenderedJSON": () => (/* binding */ RenderedJSON),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__),
/* harmony export */   "rendererFactory": () => (/* binding */ rendererFactory)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_dom__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-dom */ "webpack/sharing/consume/default/react-dom/react-dom");
/* harmony import */ var react_dom__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_dom__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./component */ "../../packages/json-extension/lib/component.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module json-extension
 */






/**
 * The CSS class to add to the JSON Widget.
 */
const CSS_CLASS = 'jp-RenderedJSON';
/**
 * The MIME type for JSON.
 */
const MIME_TYPE = 'application/json';
/**
 * A renderer for JSON data.
 */
class RenderedJSON extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Widget {
    /**
     * Create a new widget for rendering JSON.
     */
    constructor(options) {
        super();
        this.addClass(CSS_CLASS);
        this.addClass('CodeMirror');
        this.addClass('cm-s-jupyter');
        this._mimeType = options.mimeType;
        this.translator = options.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.nullTranslator;
    }
    [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Printing.symbol]() {
        return () => _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Printing.printWidget(this);
    }
    /**
     * Render JSON into this widget's node.
     */
    renderModel(model) {
        const data = (model.data[this._mimeType] || {});
        const metadata = (model.metadata[this._mimeType] || {});
        return new Promise((resolve, reject) => {
            react_dom__WEBPACK_IMPORTED_MODULE_4__.render(react__WEBPACK_IMPORTED_MODULE_3__.createElement(_component__WEBPACK_IMPORTED_MODULE_5__.Component, { data: data, metadata: metadata, translator: this.translator }), this.node, () => {
                resolve();
            });
        });
    }
    /**
     * Called before the widget is detached from the DOM.
     */
    onBeforeDetach(msg) {
        // Unmount the component so it can tear down.
        react_dom__WEBPACK_IMPORTED_MODULE_4__.unmountComponentAtNode(this.node);
    }
}
/**
 * A mime renderer factory for JSON data.
 */
const rendererFactory = {
    safe: true,
    mimeTypes: [MIME_TYPE],
    createRenderer: options => new RenderedJSON(options)
};
const extensions = [
    {
        id: '@jupyterlab/json-extension:factory',
        rendererFactory,
        rank: 0,
        dataType: 'json',
        documentWidgetFactoryOptions: {
            name: 'JSON',
            // TODO: how to translate label of the factory?
            primaryFileType: 'json',
            fileTypes: ['json', 'notebook', 'geojson'],
            defaultFor: ['json']
        }
    }
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extensions);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfanNvbi1leHRlbnNpb25fbGliX2luZGV4X2pzLjQ4YjI4NTA1ODZiZGRhMGU3OGFlLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQSwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBRVc7QUFDZjtBQUN1QjtBQUMvQztBQUNXO0FBQ0M7QUF1QjNDOztHQUVHO0FBQ0ksTUFBTSxTQUFVLFNBQVEsNENBQStCO0lBQTlEOztRQUNFLFVBQUssR0FBRyxFQUFFLE1BQU0sRUFBRSxFQUFFLEVBQUUsS0FBSyxFQUFFLEVBQUUsRUFBRSxDQUFDO1FBRWxDLFVBQUssR0FBVyxDQUFDLENBQUM7UUFFbEIsaUJBQVksR0FBRyxDQUFDLEtBQTBDLEVBQVEsRUFBRTtZQUNsRSxNQUFNLEVBQUUsS0FBSyxFQUFFLEdBQUcsS0FBSyxDQUFDLE1BQU0sQ0FBQztZQUMvQixJQUFJLENBQUMsUUFBUSxDQUFDLEVBQUUsS0FBSyxFQUFFLENBQUMsQ0FBQztZQUN6QixNQUFNLENBQUMsWUFBWSxDQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsQ0FBQztZQUNoQyxJQUFJLENBQUMsS0FBSyxHQUFHLE1BQU0sQ0FBQyxVQUFVLENBQUMsR0FBRyxFQUFFO2dCQUNsQyxJQUFJLENBQUMsUUFBUSxDQUFDLEVBQUUsTUFBTSxFQUFFLEtBQUssRUFBRSxDQUFDLENBQUM7WUFDbkMsQ0FBQyxFQUFFLEdBQUcsQ0FBQyxDQUFDO1FBQ1YsQ0FBQyxDQUFDO0lBK0ZKLENBQUM7SUE3RkMsTUFBTTtRQUNKLE1BQU0sVUFBVSxHQUFHLElBQUksQ0FBQyxLQUFLLENBQUMsVUFBVSxJQUFJLG1FQUFjLENBQUM7UUFDM0QsTUFBTSxLQUFLLEdBQUcsVUFBVSxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUMsQ0FBQztRQUU1QyxNQUFNLEVBQUUsSUFBSSxFQUFFLFFBQVEsRUFBRSxHQUFHLElBQUksQ0FBQyxLQUFLLENBQUM7UUFDdEMsTUFBTSxJQUFJLEdBQUcsUUFBUSxJQUFJ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LENBQUMsT0FBTyxFQUFFLE1BQU0sRUFBRSxFQUFFO1lBQzNDLDZDQUFlLENBQ2IsaURBQUMsaURBQVMsSUFDUixJQUFJLEVBQUUsSUFBSSxFQUNWLFFBQVEsRUFBRSxRQUFRLEVBQ2xCLFVBQVUsRUFBRSxJQUFJLENBQUMsVUFBVSxHQUMzQixFQUNGLElBQUksQ0FBQyxJQUFJLEVBQ1QsR0FBRyxFQUFFO2dCQUNILE9BQU8sRUFBRSxDQUFDO1lBQ1osQ0FBQyxDQUNGLENBQUM7UUFDSixDQUFDLENBQUMsQ0FBQztJQUNMLENBQUM7SUFFRDs7T0FFRztJQUNPLGNBQWMsQ0FBQyxHQUFZO1FBQ25DLDZDQUE2QztRQUM3Qyw2REFBK0IsQ0FBQyxJQUFJLENBQUMsSUFBSSxDQUFDLENBQUM7SUFDN0MsQ0FBQztDQUlGO0FBRUQ7O0dBRUc7QUFDSSxNQUFNLGVBQWUsR0FBaUM7SUFDM0QsSUFBSSxFQUFFLElBQUk7SUFDVixTQUFTLEVBQUUsQ0FBQyxTQUFTLENBQUM7SUFDdEIsY0FBYyxFQUFFLE9BQU8sQ0FBQyxFQUFFLENBQUMsSUFBSSxZQUFZLENBQUMsT0FBTyxDQUFDO0NBQ3JELENBQUM7QUFFRixNQUFNLFVBQVUsR0FBc0Q7SUFDcEU7UUFDRSxFQUFFLEVBQUUsb0NBQW9DO1FBQ3hDLGVBQWU7UUFDZixJQUFJLEVBQUUsQ0FBQztRQUNQLFFBQVEsRUFBRSxNQUFNO1FBQ2hCLDRCQUE0QixFQUFFO1lBQzVCLElBQUksRUFBRSxNQUFNO1lBQ1osK0NBQStDO1lBQy9DLGVBQWUsRUFBRSxNQUFNO1lBQ3ZCLFNBQVMsRUFBRSxDQUFDLE1BQU0sRUFBRSxVQUFVLEVBQUUsU0FBUyxDQUFDO1lBQzFDLFVBQVUsRUFBRSxDQUFDLE1BQU0sQ0FBQztTQUNyQjtLQUNGO0NBQ0YsQ0FBQztBQUVGLGlFQUFlLFVBQVUsRUFBQyIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9qc29uLWV4dGVuc2lvbi9zcmMvY29tcG9uZW50LnRzeCIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvanNvbi1leHRlbnNpb24vc3JjL2luZGV4LnRzeCJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElUcmFuc2xhdG9yLCBudWxsVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IElucHV0R3JvdXAgfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IEpTT05BcnJheSwgSlNPTkV4dCwgSlNPTk9iamVjdCwgSlNPTlZhbHVlIH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0ICogYXMgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0IEhpZ2hsaWdodCBmcm9tICdyZWFjdC1oaWdobGlnaHRlcic7XG5pbXBvcnQgeyBKU09OVHJlZSB9IGZyb20gJ3JlYWN0LWpzb24tdHJlZSc7XG5cbi8qKlxuICogVGhlIHByb3BlcnRpZXMgZm9yIHRoZSBKU09OIHRyZWUgY29tcG9uZW50LlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElQcm9wcyB7XG4gIGRhdGE6IE5vbk51bGxhYmxlPEpTT05WYWx1ZT47XG4gIG1ldGFkYXRhPzogSlNPTk9iamVjdDtcblxuICAvKipcbiAgICogVGhlIGFwcGxpY2F0aW9uIGxhbmd1YWdlIHRyYW5zbGF0b3IuXG4gICAqL1xuICB0cmFuc2xhdG9yPzogSVRyYW5zbGF0b3I7XG59XG5cbi8qKlxuICogVGhlIHN0YXRlIG9mIHRoZSBKU09OIHRyZWUgY29tcG9uZW50LlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElTdGF0ZSB7XG4gIGZpbHRlcj86IHN0cmluZztcbiAgdmFsdWU6IHN0cmluZztcbn1cblxuLyoqXG4gKiBBIGNvbXBvbmVudCB0aGF0IHJlbmRlcnMgSlNPTiBkYXRhIGFzIGEgY29sbGFwc2libGUgdHJlZS5cbiAqL1xuZXhwb3J0IGNsYXNzIENvbXBvbmVudCBleHRlbmRzIFJlYWN0LkNvbXBvbmVudDxJUHJvcHMsIElTdGF0ZT4ge1xuICBzdGF0ZSA9IHsgZmlsdGVyOiAnJywgdmFsdWU6ICcnIH07XG5cbiAgdGltZXI6IG51bWJlciA9IDA7XG5cbiAgaGFuZGxlQ2hhbmdlID0gKGV2ZW50OiBSZWFjdC5DaGFuZ2VFdmVudDxIVE1MSW5wdXRFbGVtZW50Pik6IHZvaWQgPT4ge1xuICAgIGNvbnN0IHsgdmFsdWUgfSA9IGV2ZW50LnRhcmdldDtcbiAgICB0aGlzLnNldFN0YXRlKHsgdmFsdWUgfSk7XG4gICAgd2luZG93LmNsZWFyVGltZW91dCh0aGlzLnRpbWVyKTtcbiAgICB0aGlzLnRpbWVyID0gd2luZG93LnNldFRpbWVvdXQoKCkgPT4ge1xuICAgICAgdGhpcy5zZXRTdGF0ZSh7IGZpbHRlcjogdmFsdWUgfSk7XG4gICAgfSwgMzAwKTtcbiAgfTtcblxuICByZW5kZXIoKTogSlNYLkVsZW1lbnQge1xuICAgIGNvbnN0IHRyYW5zbGF0b3IgPSB0aGlzLnByb3BzLnRyYW5zbGF0b3IgfHwgbnVsbFRyYW5zbGF0b3I7XG4gICAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcblxuICAgIGNvbnN0IHsgZGF0YSwgbWV0YWRhdGEgfSA9IHRoaXMucHJvcHM7XG4gICAgY29uc3Qgcm9vdCA9IG1ldGFkYXRhICYmIG1ldGFkYXRhLnJvb3QgPyAobWV0YWRhdGEucm9vdCBhcyBzdHJpbmcpIDogJ3Jvb3QnO1xuICAgIGNvbnN0IGtleVBhdGhzID0gdGhpcy5zdGF0ZS5maWx0ZXJcbiAgICAgID8gZmlsdGVyUGF0aHMoZGF0YSwgdGhpcy5zdGF0ZS5maWx0ZXIsIFtyb290XSlcbiAgICAgIDogW3Jvb3RdO1xuICAgIHJldHVybiAoXG4gICAgICA8ZGl2IGNsYXNzTmFtZT1cImNvbnRhaW5lclwiPlxuICAgICAgICA8SW5wdXRHcm91cFxuICAgICAgICAgIGNsYXNzTmFtZT1cImZpbHRlclwiXG4gICAgICAgICAgdHlwZT1cInRleHRcIlxuICAgICAgICAgIHBsYWNlaG9sZGVyPXt0cmFucy5fXygnRmlsdGVy4oCmJyl9XG4gICAgICAgICAgb25DaGFuZ2U9e3RoaXMuaGFuZGxlQ2hhbmdlfVxuICAgICAgICAgIHZhbHVlPXt0aGlzLnN0YXRlLnZhbHVlfVxuICAgICAgICAgIHJpZ2h0SWNvbj1cInVpLWNvbXBvbmVudHM6c2VhcmNoXCJcbiAgICAgICAgLz5cbiAgICAgICAgPEpTT05UcmVlXG4gICAgICAgICAgZGF0YT17ZGF0YX1cbiAgICAgICAgICBjb2xsZWN0aW9uTGltaXQ9ezEwMH1cbiAgICAgICAgICB0aGVtZT17e1xuICAgICAgICAgICAgZXh0ZW5kOiB0aGVtZSxcbiAgICAgICAgICAgIHZhbHVlTGFiZWw6ICdjbS12YXJpYWJsZScsXG4gICAgICAgICAgICB2YWx1ZVRleHQ6ICdjbS1zdHJpbmcnLFxuICAgICAgICAgICAgbmVzdGVkTm9kZUl0ZW1TdHJpbmc6ICdjbS1jb21tZW50J1xuICAgICAgICAgIH19XG4gICAgICAgICAgaW52ZXJ0VGhlbWU9e2ZhbHNlfVxuICAgICAgICAgIGtleVBhdGg9e1tyb290XX1cbiAgICAgICAgICBnZXRJdGVtU3RyaW5nPXsodHlwZSwgZGF0YSwgaXRlbVR5cGUsIGl0ZW1TdHJpbmcpID0+XG4gICAgICAgICAgICBBcnJheS5pc0FycmF5KGRhdGEpID8gKFxuICAgICAgICAgICAgICAvLyBBbHdheXMgZGlzcGxheSBhcnJheSB0eXBlIGFuZCB0aGUgbnVtYmVyIG9mIGl0ZW1zIGkuZS4gXCJbXSAyIGl0ZW1zXCIuXG4gICAgICAgICAgICAgIDxzcGFuPlxuICAgICAgICAgICAgICAgIHtpdGVtVHlwZX0ge2l0ZW1TdHJpbmd9XG4gICAgICAgICAgICAgIDwvc3Bhbj5cbiAgICAgICAgICAgICkgOiBPYmplY3Qua2V5cyhkYXRhKS5sZW5ndGggPT09IDAgPyAoXG4gICAgICAgICAgICAgIC8vIE9ubHkgZGlzcGxheSBvYmplY3QgdHlwZSB3aGVuIGl0J3MgZW1wdHkgaS5lLiBcInt9XCIuXG4gICAgICAgICAgICAgIDxzcGFuPntpdGVtVHlwZX08L3NwYW4+XG4gICAgICAgICAgICApIDogKFxuICAgICAgICAgICAgICBudWxsISAvLyBVcHN0cmVhbSB0eXBpbmdzIGRvbid0IGFjY2VwdCBudWxsLCBidXQgaXQgc2hvdWxkIGJlIG9rXG4gICAgICAgICAgICApXG4gICAgICAgICAgfVxuICAgICAgICAgIGxhYmVsUmVuZGVyZXI9eyhbbGFiZWwsIHR5cGVdKSA9PiB7XG4gICAgICAgICAgICAvLyBsZXQgY2xhc3NOYW1lID0gJ2NtLXZhcmlhYmxlJztcbiAgICAgICAgICAgIC8vIGlmICh0eXBlID09PSAncm9vdCcpIHtcbiAgICAgICAgICAgIC8vICAgY2xhc3NOYW1lID0gJ2NtLXZhcmlhYmxlLTInO1xuICAgICAgICAgICAgLy8gfVxuICAgICAgICAgICAgLy8gaWYgKHR5cGUgPT09ICdhcnJheScpIHtcbiAgICAgICAgICAgIC8vICAgY2xhc3NOYW1lID0gJ2NtLXZhcmlhYmxlLTInO1xuICAgICAgICAgICAgLy8gfVxuICAgICAgICAgICAgLy8gaWYgKHR5cGUgPT09ICdPYmplY3QnKSB7XG4gICAgICAgICAgICAvLyAgIGNsYXNzTmFtZSA9ICdjbS12YXJpYWJsZS0zJztcbiAgICAgICAgICAgIC8vIH1cbiAgICAgICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICAgIDxzcGFuIGNsYXNzTmFtZT1cImNtLWtleXdvcmRcIj5cbiAgICAgICAgICAgICAgICA8SGlnaGxpZ2h0XG4gICAgICAgICAgICAgICAgICBzZWFyY2g9e3RoaXMuc3RhdGUuZmlsdGVyfVxuICAgICAgICAgICAgICAgICAgbWF0Y2hTdHlsZT17eyBiYWNrZ3JvdW5kQ29sb3I6ICd5ZWxsb3cnIH19XG4gICAgICAgICAgICAgICAgPlxuICAgICAgICAgICAgICAgICAge2Ake2xhYmVsfTogYH1cbiAgICAgICAgICAgICAgICA8L0hpZ2hsaWdodD5cbiAgICAgICAgICAgICAgPC9zcGFuPlxuICAgICAgICAgICAgKTtcbiAgICAgICAgICB9fVxuICAgICAgICAgIHZhbHVlUmVuZGVyZXI9e3JhdyA9PiB7XG4gICAgICAgICAgICBsZXQgY2xhc3NOYW1lID0gJ2NtLXN0cmluZyc7XG4gICAgICAgICAgICBpZiAodHlwZW9mIHJhdyA9PT0gJ251bWJlcicpIHtcbiAgICAgICAgICAgICAgY2xhc3NOYW1lID0gJ2NtLW51bWJlcic7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgICBpZiAocmF3ID09PSAndHJ1ZScgfHwgcmF3ID09PSAnZmFsc2UnKSB7XG4gICAgICAgICAgICAgIGNsYXNzTmFtZSA9ICdjbS1rZXl3b3JkJztcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICAgIDxzcGFuIGNsYXNzTmFtZT17Y2xhc3NOYW1lfT5cbiAgICAgICAgICAgICAgICA8SGlnaGxpZ2h0XG4gICAgICAgICAgICAgICAgICBzZWFyY2g9e3RoaXMuc3RhdGUuZmlsdGVyfVxuICAgICAgICAgICAgICAgICAgbWF0Y2hTdHlsZT17eyBiYWNrZ3JvdW5kQ29sb3I6ICd5ZWxsb3cnIH19XG4gICAgICAgICAgICAgICAgPlxuICAgICAgICAgICAgICAgICAge2Ake3Jhd31gfVxuICAgICAgICAgICAgICAgIDwvSGlnaGxpZ2h0PlxuICAgICAgICAgICAgICA8L3NwYW4+XG4gICAgICAgICAgICApO1xuICAgICAgICAgIH19XG4gICAgICAgICAgc2hvdWxkRXhwYW5kTm9kZT17KGtleVBhdGgsIGRhdGEsIGxldmVsKSA9PlxuICAgICAgICAgICAgbWV0YWRhdGEgJiYgbWV0YWRhdGEuZXhwYW5kZWRcbiAgICAgICAgICAgICAgPyB0cnVlXG4gICAgICAgICAgICAgIDoga2V5UGF0aHMuam9pbignLCcpLmluY2x1ZGVzKGtleVBhdGguam9pbignLCcpKVxuICAgICAgICAgIH1cbiAgICAgICAgLz5cbiAgICAgIDwvZGl2PlxuICAgICk7XG4gIH1cbn1cblxuLy8gUHJvdmlkZSBhbiBpbnZhbGlkIHRoZW1lIG9iamVjdCAodGhpcyBpcyBvbiBwdXJwb3NlISkgdG8gaW52YWxpZGF0ZSB0aGVcbi8vIHJlYWN0LWpzb24tdHJlZSdzIGlubGluZSBzdHlsZXMgdGhhdCBvdmVycmlkZSBDb2RlTWlycm9yIENTUyBjbGFzc2VzXG5jb25zdCB0aGVtZSA9IHtcbiAgc2NoZW1lOiAnanVweXRlcicsXG4gIGJhc2UwMDogJ2ludmFsaWQnLFxuICBiYXNlMDE6ICdpbnZhbGlkJyxcbiAgYmFzZTAyOiAnaW52YWxpZCcsXG4gIGJhc2UwMzogJ2ludmFsaWQnLFxuICBiYXNlMDQ6ICdpbnZhbGlkJyxcbiAgYmFzZTA1OiAnaW52YWxpZCcsXG4gIGJhc2UwNjogJ2ludmFsaWQnLFxuICBiYXNlMDc6ICdpbnZhbGlkJyxcbiAgYmFzZTA4OiAnaW52YWxpZCcsXG4gIGJhc2UwOTogJ2ludmFsaWQnLFxuICBiYXNlMEE6ICdpbnZhbGlkJyxcbiAgYmFzZTBCOiAnaW52YWxpZCcsXG4gIGJhc2UwQzogJ2ludmFsaWQnLFxuICBiYXNlMEQ6ICdpbnZhbGlkJyxcbiAgYmFzZTBFOiAnaW52YWxpZCcsXG4gIGJhc2UwRjogJ2ludmFsaWQnLFxuICBhdXRob3I6ICdpbnZhbGlkJ1xufTtcblxuZnVuY3Rpb24gb2JqZWN0SW5jbHVkZXMoZGF0YTogSlNPTlZhbHVlLCBxdWVyeTogc3RyaW5nKTogYm9vbGVhbiB7XG4gIHJldHVybiBKU09OLnN0cmluZ2lmeShkYXRhKS5pbmNsdWRlcyhxdWVyeSk7XG59XG5cbmZ1bmN0aW9uIGZpbHRlclBhdGhzKFxuICBkYXRhOiBOb25OdWxsYWJsZTxKU09OVmFsdWU+LFxuICBxdWVyeTogc3RyaW5nLFxuICBwYXJlbnQ6IEpTT05BcnJheSA9IFsncm9vdCddXG4pOiBKU09OQXJyYXkge1xuICBpZiAoSlNPTkV4dC5pc0FycmF5KGRhdGEpKSB7XG4gICAgcmV0dXJuIGRhdGEucmVkdWNlKChyZXN1bHQ6IEpTT05BcnJheSwgaXRlbTogSlNPTlZhbHVlLCBpbmRleDogbnVtYmVyKSA9PiB7XG4gICAgICBpZiAoaXRlbSAmJiB0eXBlb2YgaXRlbSA9PT0gJ29iamVjdCcgJiYgb2JqZWN0SW5jbHVkZXMoaXRlbSwgcXVlcnkpKSB7XG4gICAgICAgIHJldHVybiBbXG4gICAgICAgICAgLi4ucmVzdWx0LFxuICAgICAgICAgIFtpbmRleCwgLi4ucGFyZW50XS5qb2luKCcsJyksXG4gICAgICAgICAgLi4uZmlsdGVyUGF0aHMoaXRlbSwgcXVlcnksIFtpbmRleCwgLi4ucGFyZW50XSlcbiAgICAgICAgXTtcbiAgICAgIH1cbiAgICAgIHJldHVybiByZXN1bHQ7XG4gICAgfSwgW10pIGFzIEpTT05BcnJheTtcbiAgfVxuICBpZiAoSlNPTkV4dC5pc09iamVjdChkYXRhKSkge1xuICAgIHJldHVybiBPYmplY3Qua2V5cyhkYXRhKS5yZWR1Y2UoKHJlc3VsdDogSlNPTkFycmF5LCBrZXk6IHN0cmluZykgPT4ge1xuICAgICAgY29uc3QgaXRlbSA9IGRhdGFba2V5XTtcbiAgICAgIGlmIChcbiAgICAgICAgaXRlbSAmJlxuICAgICAgICB0eXBlb2YgaXRlbSA9PT0gJ29iamVjdCcgJiZcbiAgICAgICAgKGtleS5pbmNsdWRlcyhxdWVyeSkgfHwgb2JqZWN0SW5jbHVkZXMoaXRlbSwgcXVlcnkpKVxuICAgICAgKSB7XG4gICAgICAgIHJldHVybiBbXG4gICAgICAgICAgLi4ucmVzdWx0LFxuICAgICAgICAgIFtrZXksIC4uLnBhcmVudF0uam9pbignLCcpLFxuICAgICAgICAgIC4uLmZpbHRlclBhdGhzKGl0ZW0sIHF1ZXJ5LCBba2V5LCAuLi5wYXJlbnRdKVxuICAgICAgICBdO1xuICAgICAgfVxuICAgICAgcmV0dXJuIHJlc3VsdDtcbiAgICB9LCBbXSk7XG4gIH1cbiAgcmV0dXJuIFtdO1xufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUganNvbi1leHRlbnNpb25cbiAqL1xuXG5pbXBvcnQgeyBQcmludGluZyB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IElSZW5kZXJNaW1lIH0gZnJvbSAnQGp1cHl0ZXJsYWIvcmVuZGVybWltZS1pbnRlcmZhY2VzJztcbmltcG9ydCB7IElUcmFuc2xhdG9yLCBudWxsVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IEpTT05PYmplY3QsIEpTT05WYWx1ZSB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IE1lc3NhZ2UgfSBmcm9tICdAbHVtaW5vL21lc3NhZ2luZyc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0ICogYXMgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0ICogYXMgUmVhY3RET00gZnJvbSAncmVhY3QtZG9tJztcbmltcG9ydCB7IENvbXBvbmVudCB9IGZyb20gJy4vY29tcG9uZW50JztcblxuLyoqXG4gKiBUaGUgQ1NTIGNsYXNzIHRvIGFkZCB0byB0aGUgSlNPTiBXaWRnZXQuXG4gKi9cbmNvbnN0IENTU19DTEFTUyA9ICdqcC1SZW5kZXJlZEpTT04nO1xuXG4vKipcbiAqIFRoZSBNSU1FIHR5cGUgZm9yIEpTT04uXG4gKi9cbmV4cG9ydCBjb25zdCBNSU1FX1RZUEUgPSAnYXBwbGljYXRpb24vanNvbic7XG5cbi8qKlxuICogQSByZW5kZXJlciBmb3IgSlNPTiBkYXRhLlxuICovXG5leHBvcnQgY2xhc3MgUmVuZGVyZWRKU09OXG4gIGV4dGVuZHMgV2lkZ2V0XG4gIGltcGxlbWVudHMgSVJlbmRlck1pbWUuSVJlbmRlcmVyLCBQcmludGluZy5JUHJpbnRhYmxlXG57XG4gIC8qKlxuICAgKiBDcmVhdGUgYSBuZXcgd2lkZ2V0IGZvciByZW5kZXJpbmcgSlNPTi5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IElSZW5kZXJNaW1lLklSZW5kZXJlck9wdGlvbnMpIHtcbiAgICBzdXBlcigpO1xuICAgIHRoaXMuYWRkQ2xhc3MoQ1NTX0NMQVNTKTtcbiAgICB0aGlzLmFkZENsYXNzKCdDb2RlTWlycm9yJyk7XG4gICAgdGhpcy5hZGRDbGFzcygnY20tcy1qdXB5dGVyJyk7XG4gICAgdGhpcy5fbWltZVR5cGUgPSBvcHRpb25zLm1pbWVUeXBlO1xuICAgIHRoaXMudHJhbnNsYXRvciA9IG9wdGlvbnMudHJhbnNsYXRvciB8fCBudWxsVHJhbnNsYXRvcjtcbiAgfVxuXG4gIFtQcmludGluZy5zeW1ib2xdKCkge1xuICAgIHJldHVybiAoKTogUHJvbWlzZTx2b2lkPiA9PiBQcmludGluZy5wcmludFdpZGdldCh0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5kZXIgSlNPTiBpbnRvIHRoaXMgd2lkZ2V0J3Mgbm9kZS5cbiAgICovXG4gIHJlbmRlck1vZGVsKG1vZGVsOiBJUmVuZGVyTWltZS5JTWltZU1vZGVsKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgY29uc3QgZGF0YSA9IChtb2RlbC5kYXRhW3RoaXMuX21pbWVUeXBlXSB8fCB7fSkgYXMgTm9uTnVsbGFibGU8SlNPTlZhbHVlPjtcbiAgICBjb25zdCBtZXRhZGF0YSA9IChtb2RlbC5tZXRhZGF0YVt0aGlzLl9taW1lVHlwZV0gfHwge30pIGFzIEpTT05PYmplY3Q7XG4gICAgcmV0dXJuIG5ldyBQcm9taXNlPHZvaWQ+KChyZXNvbHZlLCByZWplY3QpID0+IHtcbiAgICAgIFJlYWN0RE9NLnJlbmRlcihcbiAgICAgICAgPENvbXBvbmVudFxuICAgICAgICAgIGRhdGE9e2RhdGF9XG4gICAgICAgICAgbWV0YWRhdGE9e21ldGFkYXRhfVxuICAgICAgICAgIHRyYW5zbGF0b3I9e3RoaXMudHJhbnNsYXRvcn1cbiAgICAgICAgLz4sXG4gICAgICAgIHRoaXMubm9kZSxcbiAgICAgICAgKCkgPT4ge1xuICAgICAgICAgIHJlc29sdmUoKTtcbiAgICAgICAgfVxuICAgICAgKTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBDYWxsZWQgYmVmb3JlIHRoZSB3aWRnZXQgaXMgZGV0YWNoZWQgZnJvbSB0aGUgRE9NLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQmVmb3JlRGV0YWNoKG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIC8vIFVubW91bnQgdGhlIGNvbXBvbmVudCBzbyBpdCBjYW4gdGVhciBkb3duLlxuICAgIFJlYWN0RE9NLnVubW91bnRDb21wb25lbnRBdE5vZGUodGhpcy5ub2RlKTtcbiAgfVxuXG4gIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yO1xuICBwcml2YXRlIF9taW1lVHlwZTogc3RyaW5nO1xufVxuXG4vKipcbiAqIEEgbWltZSByZW5kZXJlciBmYWN0b3J5IGZvciBKU09OIGRhdGEuXG4gKi9cbmV4cG9ydCBjb25zdCByZW5kZXJlckZhY3Rvcnk6IElSZW5kZXJNaW1lLklSZW5kZXJlckZhY3RvcnkgPSB7XG4gIHNhZmU6IHRydWUsXG4gIG1pbWVUeXBlczogW01JTUVfVFlQRV0sXG4gIGNyZWF0ZVJlbmRlcmVyOiBvcHRpb25zID0+IG5ldyBSZW5kZXJlZEpTT04ob3B0aW9ucylcbn07XG5cbmNvbnN0IGV4dGVuc2lvbnM6IElSZW5kZXJNaW1lLklFeHRlbnNpb24gfCBJUmVuZGVyTWltZS5JRXh0ZW5zaW9uW10gPSBbXG4gIHtcbiAgICBpZDogJ0BqdXB5dGVybGFiL2pzb24tZXh0ZW5zaW9uOmZhY3RvcnknLFxuICAgIHJlbmRlcmVyRmFjdG9yeSxcbiAgICByYW5rOiAwLFxuICAgIGRhdGFUeXBlOiAnanNvbicsXG4gICAgZG9jdW1lbnRXaWRnZXRGYWN0b3J5T3B0aW9uczoge1xuICAgICAgbmFtZTogJ0pTT04nLFxuICAgICAgLy8gVE9ETzogaG93IHRvIHRyYW5zbGF0ZSBsYWJlbCBvZiB0aGUgZmFjdG9yeT9cbiAgICAgIHByaW1hcnlGaWxlVHlwZTogJ2pzb24nLFxuICAgICAgZmlsZVR5cGVzOiBbJ2pzb24nLCAnbm90ZWJvb2snLCAnZ2VvanNvbiddLFxuICAgICAgZGVmYXVsdEZvcjogWydqc29uJ11cbiAgICB9XG4gIH1cbl07XG5cbmV4cG9ydCBkZWZhdWx0IGV4dGVuc2lvbnM7XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=