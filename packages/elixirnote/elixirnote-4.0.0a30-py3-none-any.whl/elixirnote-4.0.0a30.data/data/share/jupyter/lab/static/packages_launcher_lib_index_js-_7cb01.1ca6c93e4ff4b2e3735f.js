"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_launcher_lib_index_js-_7cb01"],{

/***/ "../../packages/launcher/lib/index.js":
/*!********************************************!*\
  !*** ../../packages/launcher/lib/index.js ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ILauncher": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_0__.ILauncher),
/* harmony export */   "Launcher": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_1__.Launcher),
/* harmony export */   "LauncherModel": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_1__.LauncherModel)
/* harmony export */ });
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./tokens */ "../../packages/launcher/lib/tokens.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./widget */ "../../packages/launcher/lib/widget.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module launcher
 */




/***/ }),

/***/ "../../packages/launcher/lib/tokens.js":
/*!*********************************************!*\
  !*** ../../packages/launcher/lib/tokens.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ILauncher": () => (/* binding */ ILauncher)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/**
 * The launcher token.
 */
const ILauncher = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/launcher:ILauncher');


/***/ }),

/***/ "../../packages/launcher/lib/widget.js":
/*!*********************************************!*\
  !*** ../../packages/launcher/lib/widget.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Launcher": () => (/* binding */ Launcher),
/* harmony export */   "LauncherModel": () => (/* binding */ LauncherModel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_properties__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/properties */ "webpack/sharing/consume/default/@lumino/properties/@lumino/properties");
/* harmony import */ var _lumino_properties__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_properties__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_7__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.








/**
 * The class name added to Launcher instances.
 */
const LAUNCHER_CLASS = 'jp-Launcher';
/**
 * LauncherModel keeps track of the path to working directory and has a list of
 * LauncherItems, which the Launcher will render.
 */
class LauncherModel extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.VDomModel {
    constructor() {
        super(...arguments);
        this.itemsList = [];
    }
    /**
     * Add a command item to the launcher, and trigger re-render event for parent
     * widget.
     *
     * @param options - The specification options for a launcher item.
     *
     * @returns A disposable that will remove the item from Launcher, and trigger
     * re-render event for parent widget.
     *
     */
    add(options) {
        // Create a copy of the options to circumvent mutations to the original.
        const item = Private.createItem(options);
        this.itemsList.push(item);
        this.stateChanged.emit(void 0);
        return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_4__.DisposableDelegate(() => {
            _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.ArrayExt.removeFirstOf(this.itemsList, item);
            this.stateChanged.emit(void 0);
        });
    }
    /**
     * Return an iterator of launcher items.
     */
    items() {
        return new _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.ArrayIterator(this.itemsList);
    }
}
/**
 * A virtual-DOM-based widget for the Launcher.
 */
class Launcher extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.VDomRenderer {
    /**
     * Construct a new launcher widget.
     */
    constructor(options) {
        super(options.model);
        this._pending = false;
        this._cwd = '';
        this._cwd = options.cwd;
        this.translator = options.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.nullTranslator;
        this._trans = this.translator.load('jupyterlab');
        this._callback = options.callback;
        this._commands = options.commands;
        this.addClass(LAUNCHER_CLASS);
    }
    /**
     * The cwd of the launcher.
     */
    get cwd() {
        return this._cwd;
    }
    set cwd(value) {
        this._cwd = value;
        this.update();
    }
    /**
     * Whether there is a pending item being launched.
     */
    get pending() {
        return this._pending;
    }
    set pending(value) {
        this._pending = value;
    }
    /**
     * Render the launcher to virtual DOM nodes.
     */
    render() {
        // Bail if there is no model.
        if (!this.model) {
            return null;
        }
        const knownCategories = [
            this._trans.__('Notebook'),
            this._trans.__('Console'),
            this._trans.__('Other')
        ];
        const kernelCategories = [
            this._trans.__('Notebook'),
            this._trans.__('Console')
        ];
        // First group-by categories
        const categories = Object.create(null);
        (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.each)(this.model.items(), (item, index) => {
            const cat = item.category || this._trans.__('Other');
            if (cat != 'Console') {
                if (!(cat in categories)) {
                    categories[cat] = [];
                }
                categories[cat].push(item);
            }
        });
        // Within each category sort by rank
        for (const cat in categories) {
            categories[cat] = categories[cat].sort((a, b) => {
                return Private.sortCmp(a, b, this._cwd, this._commands);
            });
        }
        // Variable to help create sections
        const sections = [];
        let section;
        // Assemble the final ordered list of categories, beginning with
        // KNOWN_CATEGORIES.
        const orderedCategories = [];
        (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.each)(knownCategories, (cat, index) => {
            orderedCategories.push(cat);
        });
        for (const cat in categories) {
            if (knownCategories.indexOf(cat) === -1) {
                orderedCategories.push(cat);
            }
        }
        // Now create the sections for each category
        orderedCategories.forEach(cat => {
            if (!categories[cat]) {
                return;
            }
            const kernel = kernelCategories.indexOf(cat) > -1;
            if (cat in categories) {
                section = (react__WEBPACK_IMPORTED_MODULE_7__.createElement("div", { className: "jp-Launcher-section", key: cat },
                    react__WEBPACK_IMPORTED_MODULE_7__.createElement("div", { className: "jp-Launcher-sectionHeader" },
                        react__WEBPACK_IMPORTED_MODULE_7__.createElement("h2", { className: "jp-Launcher-sectionTitle" }, cat)),
                    react__WEBPACK_IMPORTED_MODULE_7__.createElement("div", { className: "jp-Launcher-cardContainer" }, (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.toArray)((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.map)(categories[cat], (item) => {
                        return Card(kernel, item, this, this._commands, this._trans, this._callback);
                    })))));
                sections.push(section);
            }
        });
        // Wrap the sections in body and content divs.
        return (react__WEBPACK_IMPORTED_MODULE_7__.createElement("div", { className: "jp-Launcher-body" },
            react__WEBPACK_IMPORTED_MODULE_7__.createElement("div", { className: "jp-Launcher-content" },
                react__WEBPACK_IMPORTED_MODULE_7__.createElement("div", { className: "jp-Launcher-cwd" },
                    react__WEBPACK_IMPORTED_MODULE_7__.createElement("h3", null, this.cwd)),
                sections)));
    }
}
/**
 * A pure tsx component for a launcher card.
 *
 * @param kernel - whether the item takes uses a kernel.
 *
 * @param item - the launcher item to render.
 *
 * @param launcher - the Launcher instance to which this is added.
 *
 * @param commands - the command registry holding the command of item.
 *
 * @param trans - the translation bundle.
 *
 * @returns a vdom `VirtualElement` for the launcher card.
 */
function Card(kernel, item, launcher, commands, trans, launcherCallback) {
    // Get some properties of the command
    const command = item.command;
    const args = Object.assign(Object.assign({}, item.args), { cwd: launcher.cwd });
    const caption = commands.caption(command, args);
    const label = commands.label(command, args);
    const title = kernel ? label : caption || label;
    // Build the onclick handler.
    const onclick = () => {
        // If an item has already been launched,
        // don't try to launch another.
        if (launcher.pending === true) {
            return;
        }
        launcher.pending = true;
        void commands
            .execute(command, Object.assign(Object.assign({}, item.args), { cwd: launcher.cwd }))
            .then(value => {
            launcher.pending = false;
            if (value instanceof _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Widget) {
                launcherCallback(value);
            }
        })
            .catch(err => {
            console.error(err);
            launcher.pending = false;
            void (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showErrorMessage)(trans._p('Error', 'Launcher Error'), err);
        });
    };
    // With tabindex working, you can now pick a kernel by tabbing around and
    // pressing Enter.
    const onkeypress = (event) => {
        if (event.key === 'Enter') {
            onclick();
        }
    };
    // Return the VDOM element.
    return (react__WEBPACK_IMPORTED_MODULE_7__.createElement("div", { className: "jp-LauncherCard", title: title, onClick: onclick, onKeyPress: onkeypress, tabIndex: 0, "data-category": item.category || trans.__('Other'), key: Private.keyProperty.get(item) },
        react__WEBPACK_IMPORTED_MODULE_7__.createElement("div", { className: "jp-LauncherCard-label", title: title },
            react__WEBPACK_IMPORTED_MODULE_7__.createElement("p", null,
                "New ",
                label,
                "..."))));
}
/**
 * The namespace for module private data.
 */
var Private;
(function (Private) {
    /**
     * An incrementing counter for keys.
     */
    let id = 0;
    /**
     * An attached property for an item's key.
     */
    Private.keyProperty = new _lumino_properties__WEBPACK_IMPORTED_MODULE_5__.AttachedProperty({
        name: 'key',
        create: () => id++
    });
    /**
     * Create a fully specified item given item options.
     */
    function createItem(options) {
        return Object.assign(Object.assign({}, options), { category: options.category || '', rank: options.rank !== undefined ? options.rank : Infinity });
    }
    Private.createItem = createItem;
    /**
     * A sort comparison function for a launcher item.
     */
    function sortCmp(a, b, cwd, commands) {
        // First, compare by rank.
        const r1 = a.rank;
        const r2 = b.rank;
        if (r1 !== r2 && r1 !== undefined && r2 !== undefined) {
            return r1 < r2 ? -1 : 1; // Infinity safe
        }
        // Finally, compare by display name.
        const aLabel = commands.label(a.command, Object.assign(Object.assign({}, a.args), { cwd }));
        const bLabel = commands.label(b.command, Object.assign(Object.assign({}, b.args), { cwd }));
        return aLabel.localeCompare(bLabel);
    }
    Private.sortCmp = sortCmp;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfbGF1bmNoZXJfbGliX2luZGV4X2pzLV83Y2IwMS4xY2E2YzkzZTRmZjRiMmUzNzM1Zi5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBRXNCO0FBQ0E7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDUnpCOzs7R0FHRztBQU0yRDtBQUk5RDs7R0FFRztBQUNJLE1BQU0sU0FBUyxHQUFHLElBQUksb0RBQUssQ0FBWSxnQ0FBZ0MsQ0FBQyxDQUFDOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQ2hCaEYsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUVIO0FBS3ZCO0FBQ21DO0FBUXpDO0FBRTBDO0FBQ2Y7QUFDYjtBQUNWO0FBRy9COztHQUVHO0FBQ0gsTUFBTSxjQUFjLEdBQUcsYUFBYSxDQUFDO0FBRXJDOzs7R0FHRztBQUNJLE1BQU0sYUFBYyxTQUFRLGdFQUFTO0lBQTVDOztRQStCWSxjQUFTLEdBQTZCLEVBQUUsQ0FBQztJQUNyRCxDQUFDO0lBL0JDOzs7Ozs7Ozs7T0FTRztJQUNILEdBQUcsQ0FBQyxPQUErQjtRQUNqQyx3RUFBd0U7UUFDeEUsTUFBTSxJQUFJLEdBQUcsT0FBTyxDQUFDLFVBQVUsQ0FBQyxPQUFPLENBQUMsQ0FBQztRQUV6QyxJQUFJLENBQUMsU0FBUyxDQUFDLElBQUksQ0FBQyxJQUFJLENBQUMsQ0FBQztRQUMxQixJQUFJLENBQUMsWUFBWSxDQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsQ0FBQyxDQUFDO1FBRS9CLE9BQU8sSUFBSSxrRUFBa0IsQ0FBQyxHQUFHLEVBQUU7WUFDakMscUVBQXNCLENBQUMsSUFBSSxDQUFDLFNBQVMsRUFBRSxJQUFJLENBQUMsQ0FBQztZQUM3QyxJQUFJLENBQUMsWUFBWSxDQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsQ0FBQyxDQUFDO1FBQ2pDLENBQUMsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztJQUVEOztPQUVHO0lBQ0gs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RSxHQUFHLENBQUMsQ0FBQyxJQUFJLENBQUM7UUFDbEIsSUFBSSxFQUFFLEtBQUssRUFBRSxJQUFJLEVBQUUsS0FBSyxTQUFTLElBQUksRUFBRSxLQUFLLFNBQVMsRUFBRTtZQUNyRCxPQUFPLEVBQUUsR0FBRyxFQUFFLENBQUMsQ0FBQyxDQUFDLENBQUMsQ0FBQyxDQUFDLENBQUMsQ0FBQyxDQUFDLENBQUMsQ0FBQyxnQkFBZ0I7U0FDMUM7UUFFRCxvQ0FBb0M7UUFDcEMsTUFBTSxNQUFNLEdBQUcsUUFBUSxDQUFDLEtBQUssQ0FBQyxDQUFDLENBQUMsT0FBTyxrQ0FBTyxDQUFDLENBQUMsSUFBSSxLQUFFLEdBQUcsSUFBRyxDQUFDO1FBQzdELE1BQU0sTUFBTSxHQUFHLFFBQVEsQ0FBQyxLQUFLLENBQUMsQ0FBQyxDQUFDLE9BQU8sa0NBQU8sQ0FBQyxDQUFDLElBQUksS0FBRSxHQUFHLElBQUcsQ0FBQztRQUM3RCxPQUFPLE1BQU0sQ0FBQyxhQUFhLENBQUMsTUFBTSxDQUFDLENBQUM7SUFDdEMsQ0FBQztJQWpCZSxlQUFPLFVBaUJ0QjtBQUNILENBQUMsRUFuRFMsT0FBTyxLQUFQLE9BQU8sUUFtRGhCIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2xhdW5jaGVyL3NyYy9pbmRleC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvbGF1bmNoZXIvc3JjL3Rva2Vucy50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvbGF1bmNoZXIvc3JjL3dpZGdldC50c3giXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgbGF1bmNoZXJcbiAqL1xuXG5leHBvcnQgKiBmcm9tICcuL3Rva2Vucyc7XG5leHBvcnQgKiBmcm9tICcuL3dpZGdldCc7XG4iLCIvKlxuICogQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4gKiBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuICovXG5cbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgVkRvbVJlbmRlcmVyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBJSXRlcmF0b3IgfSBmcm9tICdAbHVtaW5vL2FsZ29yaXRobSc7XG5pbXBvcnQgeyBDb21tYW5kUmVnaXN0cnkgfSBmcm9tICdAbHVtaW5vL2NvbW1hbmRzJztcbmltcG9ydCB7IFJlYWRvbmx5SlNPTk9iamVjdCwgVG9rZW4gfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuXG4vKipcbiAqIFRoZSBsYXVuY2hlciB0b2tlbi5cbiAqL1xuZXhwb3J0IGNvbnN0IElMYXVuY2hlciA9IG5ldyBUb2tlbjxJTGF1bmNoZXI+KCdAanVweXRlcmxhYi9sYXVuY2hlcjpJTGF1bmNoZXInKTtcblxuLyoqXG4gKiBUaGUgbGF1bmNoZXIgaW50ZXJmYWNlLlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElMYXVuY2hlciB7XG4gIC8qKlxuICAgKiBBZGQgYSBjb21tYW5kIGl0ZW0gdG8gdGhlIGxhdW5jaGVyLCBhbmQgdHJpZ2dlciByZS1yZW5kZXIgZXZlbnQgZm9yIHBhcmVudFxuICAgKiB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSBvcHRpb25zIC0gVGhlIHNwZWNpZmljYXRpb24gb3B0aW9ucyBmb3IgYSBsYXVuY2hlciBpdGVtLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIGRpc3Bvc2FibGUgdGhhdCB3aWxsIHJlbW92ZSB0aGUgaXRlbSBmcm9tIExhdW5jaGVyLCBhbmQgdHJpZ2dlclxuICAgKiByZS1yZW5kZXIgZXZlbnQgZm9yIHBhcmVudCB3aWRnZXQuXG4gICAqXG4gICAqL1xuICBhZGQob3B0aW9uczogSUxhdW5jaGVyLklJdGVtT3B0aW9ucyk6IElEaXNwb3NhYmxlO1xufVxuXG4vKipcbiAqIFRoZSBuYW1lc3BhY2UgZm9yIGBJTGF1bmNoZXJgIGNsYXNzIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgSUxhdW5jaGVyIHtcbiAgLyoqXG4gICAqIEFuIGludGVyZmFjZSBmb3IgdGhlIGxhdW5jaGVyIG1vZGVsXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElNb2RlbCBleHRlbmRzIElMYXVuY2hlciwgVkRvbVJlbmRlcmVyLklNb2RlbCB7XG4gICAgLyoqXG4gICAgICogUmV0dXJuIGFuIGl0ZXJhdG9yIG9mIGxhdW5jaGVyIGl0ZW1zLlxuICAgICAqL1xuICAgIGl0ZW1zKCk6IElJdGVyYXRvcjxJTGF1bmNoZXIuSUl0ZW1PcHRpb25zPjtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgb3B0aW9ucyB1c2VkIHRvIGNyZWF0ZSBhIExhdW5jaGVyLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIG1vZGVsIG9mIHRoZSBsYXVuY2hlci5cbiAgICAgKi9cbiAgICBtb2RlbDogSU1vZGVsO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGN3ZCBvZiB0aGUgbGF1bmNoZXIuXG4gICAgICovXG4gICAgY3dkOiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgY29tbWFuZCByZWdpc3RyeSB1c2VkIGJ5IHRoZSBsYXVuY2hlci5cbiAgICAgKi9cbiAgICBjb21tYW5kczogQ29tbWFuZFJlZ2lzdHJ5O1xuXG4gICAgLyoqXG4gICAgICogVGhlIGFwcGxpY2F0aW9uIGxhbmd1YWdlIHRyYW5zbGF0aW9uLlxuICAgICAqL1xuICAgIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvcjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBjYWxsYmFjayB1c2VkIHdoZW4gYW4gaXRlbSBpcyBsYXVuY2hlZC5cbiAgICAgKi9cbiAgICBjYWxsYmFjazogKHdpZGdldDogV2lkZ2V0KSA9PiB2b2lkO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBvcHRpb25zIHVzZWQgdG8gY3JlYXRlIGEgbGF1bmNoZXIgaXRlbS5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUl0ZW1PcHRpb25zIHtcbiAgICAvKipcbiAgICAgKiBUaGUgY29tbWFuZCBJRCBmb3IgdGhlIGxhdW5jaGVyIGl0ZW0uXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogSWYgdGhlIGNvbW1hbmQncyBgZXhlY3V0ZWAgbWV0aG9kIHJldHVybnMgYSBgV2lkZ2V0YCBvclxuICAgICAqIGEgcHJvbWlzZSB0aGF0IHJlc29sdmVzIHdpdGggYSBgV2lkZ2V0YCwgdGhlbiB0aGF0IHdpZGdldCB3aWxsXG4gICAgICogcmVwbGFjZSB0aGUgbGF1bmNoZXIgaW4gdGhlIHNhbWUgbG9jYXRpb24gb2YgdGhlIGFwcGxpY2F0aW9uXG4gICAgICogc2hlbGwuIElmIHRoZSBgZXhlY3V0ZWAgbWV0aG9kIGRvZXMgc29tZXRoaW5nIGVsc2VcbiAgICAgKiAoaS5lLiwgY3JlYXRlIGEgbW9kYWwgZGlhbG9nKSwgdGhlbiB0aGUgbGF1bmNoZXIgd2lsbCBub3QgYmVcbiAgICAgKiBkaXNwb3NlZC5cbiAgICAgKi9cbiAgICBjb21tYW5kOiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgYXJndW1lbnRzIGdpdmVuIHRvIHRoZSBjb21tYW5kIGZvclxuICAgICAqIGNyZWF0aW5nIHRoZSBsYXVuY2hlciBpdGVtLlxuICAgICAqXG4gICAgICogIyMjIE5vdGVzXG4gICAgICogVGhlIGxhdW5jaGVyIHdpbGwgYWxzbyBhZGQgdGhlIGN1cnJlbnQgd29ya2luZ1xuICAgICAqIGRpcmVjdG9yeSBvZiB0aGUgZmlsZWJyb3dzZXIgaW4gdGhlIGBjd2RgIGZpZWxkXG4gICAgICogb2YgdGhlIGFyZ3MsIHdoaWNoIGEgY29tbWFuZCBtYXkgdXNlIHRvIGNyZWF0ZVxuICAgICAqIHRoZSBhY3Rpdml0eSB3aXRoIHJlc3BlY3QgdG8gdGhlIHJpZ2h0IGRpcmVjdG9yeS5cbiAgICAgKi9cbiAgICBhcmdzPzogUmVhZG9ubHlKU09OT2JqZWN0O1xuXG4gICAgLyoqXG4gICAgICogVGhlIGNhdGVnb3J5IGZvciB0aGUgbGF1bmNoZXIgaXRlbS5cbiAgICAgKlxuICAgICAqIFRoZSBkZWZhdWx0IHZhbHVlIGlzIGFuIGVtcHR5IHN0cmluZy5cbiAgICAgKi9cbiAgICBjYXRlZ29yeT86IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFRoZSByYW5rIGZvciB0aGUgbGF1bmNoZXIgaXRlbS5cbiAgICAgKlxuICAgICAqIFRoZSByYW5rIGlzIHVzZWQgd2hlbiBvcmRlcmluZyBsYXVuY2hlciBpdGVtcyBmb3IgZGlzcGxheS4gQWZ0ZXIgZ3JvdXBpbmdcbiAgICAgKiBpbnRvIGNhdGVnb3JpZXMsIGl0ZW1zIGFyZSBzb3J0ZWQgaW4gdGhlIGZvbGxvd2luZyBvcmRlcjpcbiAgICAgKiAgIDEuIFJhbmsgKGxvd2VyIGlzIGJldHRlcilcbiAgICAgKiAgIDMuIERpc3BsYXkgTmFtZSAobG9jYWxlIG9yZGVyKVxuICAgICAqXG4gICAgICogVGhlIGRlZmF1bHQgcmFuayBpcyBgSW5maW5pdHlgLlxuICAgICAqL1xuICAgIHJhbms/OiBudW1iZXI7XG5cbiAgICAvKipcbiAgICAgKiBGb3IgaXRlbXMgdGhhdCBoYXZlIGEga2VybmVsIGFzc29jaWF0ZWQgd2l0aCB0aGVtLCB0aGUgVVJMIG9mIHRoZSBrZXJuZWxcbiAgICAgKiBpY29uLlxuICAgICAqXG4gICAgICogVGhpcyBpcyBub3QgYSBDU1MgY2xhc3MsIGJ1dCB0aGUgVVJMIHRoYXQgcG9pbnRzIHRvIHRoZSBpY29uIGluIHRoZSBrZXJuZWxcbiAgICAgKiBzcGVjLlxuICAgICAqL1xuICAgIGtlcm5lbEljb25Vcmw/OiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBNZXRhZGF0YSBhYm91dCB0aGUgaXRlbS4gIFRoaXMgY2FuIGJlIHVzZWQgYnkgdGhlIGxhdW5jaGVyIHRvXG4gICAgICogYWZmZWN0IGhvdyB0aGUgaXRlbSBpcyBkaXNwbGF5ZWQuXG4gICAgICovXG4gICAgbWV0YWRhdGE/OiBSZWFkb25seUpTT05PYmplY3Q7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgc2hvd0Vycm9yTWVzc2FnZSB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7XG4gIElUcmFuc2xhdG9yLFxuICBudWxsVHJhbnNsYXRvcixcbiAgVHJhbnNsYXRpb25CdW5kbGVcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgVkRvbU1vZGVsLCBWRG9tUmVuZGVyZXIgfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7XG4gIEFycmF5RXh0LFxuICBBcnJheUl0ZXJhdG9yLFxuICBlYWNoLFxuICBJSXRlcmF0b3IsXG4gIG1hcCxcbiAgdG9BcnJheVxufSBmcm9tICdAbHVtaW5vL2FsZ29yaXRobSc7XG5pbXBvcnQgeyBDb21tYW5kUmVnaXN0cnkgfSBmcm9tICdAbHVtaW5vL2NvbW1hbmRzJztcbmltcG9ydCB7IERpc3Bvc2FibGVEZWxlZ2F0ZSwgSURpc3Bvc2FibGUgfSBmcm9tICdAbHVtaW5vL2Rpc3Bvc2FibGUnO1xuaW1wb3J0IHsgQXR0YWNoZWRQcm9wZXJ0eSB9IGZyb20gJ0BsdW1pbm8vcHJvcGVydGllcyc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0ICogYXMgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0IHsgSUxhdW5jaGVyIH0gZnJvbSAnLi90b2tlbnMnO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIExhdW5jaGVyIGluc3RhbmNlcy5cbiAqL1xuY29uc3QgTEFVTkNIRVJfQ0xBU1MgPSAnanAtTGF1bmNoZXInO1xuXG4vKipcbiAqIExhdW5jaGVyTW9kZWwga2VlcHMgdHJhY2sgb2YgdGhlIHBhdGggdG8gd29ya2luZyBkaXJlY3RvcnkgYW5kIGhhcyBhIGxpc3Qgb2ZcbiAqIExhdW5jaGVySXRlbXMsIHdoaWNoIHRoZSBMYXVuY2hlciB3aWxsIHJlbmRlci5cbiAqL1xuZXhwb3J0IGNsYXNzIExhdW5jaGVyTW9kZWwgZXh0ZW5kcyBWRG9tTW9kZWwgaW1wbGVtZW50cyBJTGF1bmNoZXIuSU1vZGVsIHtcbiAgLyoqXG4gICAqIEFkZCBhIGNvbW1hbmQgaXRlbSB0byB0aGUgbGF1bmNoZXIsIGFuZCB0cmlnZ2VyIHJlLXJlbmRlciBldmVudCBmb3IgcGFyZW50XG4gICAqIHdpZGdldC5cbiAgICpcbiAgICogQHBhcmFtIG9wdGlvbnMgLSBUaGUgc3BlY2lmaWNhdGlvbiBvcHRpb25zIGZvciBhIGxhdW5jaGVyIGl0ZW0uXG4gICAqXG4gICAqIEByZXR1cm5zIEEgZGlzcG9zYWJsZSB0aGF0IHdpbGwgcmVtb3ZlIHRoZSBpdGVtIGZyb20gTGF1bmNoZXIsIGFuZCB0cmlnZ2VyXG4gICAqIHJlLXJlbmRlciBldmVudCBmb3IgcGFyZW50IHdpZGdldC5cbiAgICpcbiAgICovXG4gIGFkZChvcHRpb25zOiBJTGF1bmNoZXIuSUl0ZW1PcHRpb25zKTogSURpc3Bvc2FibGUge1xuICAgIC8vIENyZWF0ZSBhIGNvcHkgb2YgdGhlIG9wdGlvbnMgdG8gY2lyY3VtdmVudCBtdXRhdGlvbnMgdG8gdGhlIG9yaWdpbmFsLlxuICAgIGNvbnN0IGl0ZW0gPSBQcml2YXRlLmNyZWF0ZUl0ZW0ob3B0aW9ucyk7XG5cbiAgICB0aGlzLml0ZW1zTGlzdC5wdXNoKGl0ZW0pO1xuICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQodm9pZCAwKTtcblxuICAgIHJldHVybiBuZXcgRGlzcG9zYWJsZURlbGVnYXRlKCgpID0+IHtcbiAgICAgIEFycmF5RXh0LnJlbW92ZUZpcnN0T2YodGhpcy5pdGVtc0xpc3QsIGl0ZW0pO1xuICAgICAgdGhpcy5zdGF0ZUNoYW5nZWQuZW1pdCh2b2lkIDApO1xuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIFJldHVybiBhbiBpdGVyYXRvciBvZiBsYXVuY2hlciBpdGVtcy5cbiAgICovXG4gIGl0ZW1zKCk6IElJdGVyYXRvcjxJTGF1bmNoZXIuSUl0ZW1PcHRpb25zPiB7XG4gICAgcmV0dXJuIG5ldyBBcnJheUl0ZXJhdG9yKHRoaXMuaXRlbXNMaXN0KTtcbiAgfVxuXG4gIHByb3RlY3RlZCBpdGVtc0xpc3Q6IElMYXVuY2hlci5JSXRlbU9wdGlvbnNbXSA9IFtdO1xufVxuXG4vKipcbiAqIEEgdmlydHVhbC1ET00tYmFzZWQgd2lkZ2V0IGZvciB0aGUgTGF1bmNoZXIuXG4gKi9cbmV4cG9ydCBjbGFzcyBMYXVuY2hlciBleHRlbmRzIFZEb21SZW5kZXJlcjxJTGF1bmNoZXIuSU1vZGVsPiB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgYSBuZXcgbGF1bmNoZXIgd2lkZ2V0LlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogSUxhdW5jaGVyLklPcHRpb25zKSB7XG4gICAgc3VwZXIob3B0aW9ucy5tb2RlbCk7XG4gICAgdGhpcy5fY3dkID0gb3B0aW9ucy5jd2Q7XG4gICAgdGhpcy50cmFuc2xhdG9yID0gb3B0aW9ucy50cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIHRoaXMuX3RyYW5zID0gdGhpcy50cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICB0aGlzLl9jYWxsYmFjayA9IG9wdGlvbnMuY2FsbGJhY2s7XG4gICAgdGhpcy5fY29tbWFuZHMgPSBvcHRpb25zLmNvbW1hbmRzO1xuICAgIHRoaXMuYWRkQ2xhc3MoTEFVTkNIRVJfQ0xBU1MpO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBjd2Qgb2YgdGhlIGxhdW5jaGVyLlxuICAgKi9cbiAgZ2V0IGN3ZCgpOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLl9jd2Q7XG4gIH1cbiAgc2V0IGN3ZCh2YWx1ZTogc3RyaW5nKSB7XG4gICAgdGhpcy5fY3dkID0gdmFsdWU7XG4gICAgdGhpcy51cGRhdGUoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBXaGV0aGVyIHRoZXJlIGlzIGEgcGVuZGluZyBpdGVtIGJlaW5nIGxhdW5jaGVkLlxuICAgKi9cbiAgZ2V0IHBlbmRpbmcoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuX3BlbmRpbmc7XG4gIH1cbiAgc2V0IHBlbmRpbmcodmFsdWU6IGJvb2xlYW4pIHtcbiAgICB0aGlzLl9wZW5kaW5nID0gdmFsdWU7XG4gIH1cblxuICAvKipcbiAgICogUmVuZGVyIHRoZSBsYXVuY2hlciB0byB2aXJ0dWFsIERPTSBub2Rlcy5cbiAgICovXG4gIHByb3RlY3RlZCByZW5kZXIoKTogUmVhY3QuUmVhY3RFbGVtZW50PGFueT4gfCBudWxsIHtcbiAgICAvLyBCYWlsIGlmIHRoZXJlIGlzIG5vIG1vZGVsLlxuICAgIGlmICghdGhpcy5tb2RlbCkge1xuICAgICAgcmV0dXJuIG51bGw7XG4gICAgfVxuXG4gICAgY29uc3Qga25vd25DYXRlZ29yaWVzID0gW1xuICAgICAgdGhpcy5fdHJhbnMuX18oJ05vdGVib29rJyksXG4gICAgICB0aGlzLl90cmFucy5fXygnQ29uc29sZScpLFxuICAgICAgdGhpcy5fdHJhbnMuX18oJ090aGVyJylcbiAgICBdO1xuICAgIGNvbnN0IGtlcm5lbENhdGVnb3JpZXMgPSBbXG4gICAgICB0aGlzLl90cmFucy5fXygnTm90ZWJvb2snKSxcbiAgICAgIHRoaXMuX3RyYW5zLl9fKCdDb25zb2xlJylcbiAgICBdO1xuXG4gICAgLy8gRmlyc3QgZ3JvdXAtYnkgY2F0ZWdvcmllc1xuICAgIGNvbnN0IGNhdGVnb3JpZXMgPSBPYmplY3QuY3JlYXRlKG51bGwpO1xuICAgIGVhY2godGhpcy5tb2RlbC5pdGVtcygpLCAoaXRlbSwgaW5kZXgpID0+IHtcbiAgICAgIGNvbnN0IGNhdCA9IGl0ZW0uY2F0ZWdvcnkgfHwgdGhpcy5fdHJhbnMuX18oJ090aGVyJyk7XG4gICAgICBpZiAoY2F0ICE9ICdDb25zb2xlJykge1xuICAgICAgICBpZiAoIShjYXQgaW4gY2F0ZWdvcmllcykpIHtcbiAgICAgICAgICBjYXRlZ29yaWVzW2NhdF0gPSBbXTtcbiAgICAgICAgfVxuICAgICAgICBjYXRlZ29yaWVzW2NhdF0ucHVzaChpdGVtKTtcbiAgICAgIH1cbiAgICB9KTtcbiAgICAvLyBXaXRoaW4gZWFjaCBjYXRlZ29yeSBzb3J0IGJ5IHJhbmtcbiAgICBmb3IgKGNvbnN0IGNhdCBpbiBjYXRlZ29yaWVzKSB7XG4gICAgICBjYXRlZ29yaWVzW2NhdF0gPSBjYXRlZ29yaWVzW2NhdF0uc29ydChcbiAgICAgICAgKGE6IElMYXVuY2hlci5JSXRlbU9wdGlvbnMsIGI6IElMYXVuY2hlci5JSXRlbU9wdGlvbnMpID0+IHtcbiAgICAgICAgICByZXR1cm4gUHJpdmF0ZS5zb3J0Q21wKGEsIGIsIHRoaXMuX2N3ZCwgdGhpcy5fY29tbWFuZHMpO1xuICAgICAgICB9XG4gICAgICApO1xuICAgIH1cblxuICAgIC8vIFZhcmlhYmxlIHRvIGhlbHAgY3JlYXRlIHNlY3Rpb25zXG4gICAgY29uc3Qgc2VjdGlvbnM6IFJlYWN0LlJlYWN0RWxlbWVudDxhbnk+W10gPSBbXTtcbiAgICBsZXQgc2VjdGlvbjogUmVhY3QuUmVhY3RFbGVtZW50PGFueT47XG5cbiAgICAvLyBBc3NlbWJsZSB0aGUgZmluYWwgb3JkZXJlZCBsaXN0IG9mIGNhdGVnb3JpZXMsIGJlZ2lubmluZyB3aXRoXG4gICAgLy8gS05PV05fQ0FURUdPUklFUy5cbiAgICBjb25zdCBvcmRlcmVkQ2F0ZWdvcmllczogc3RyaW5nW10gPSBbXTtcbiAgICBlYWNoKGtub3duQ2F0ZWdvcmllcywgKGNhdCwgaW5kZXgpID0+IHtcbiAgICAgIG9yZGVyZWRDYXRlZ29yaWVzLnB1c2goY2F0KTtcbiAgICB9KTtcbiAgICBmb3IgKGNvbnN0IGNhdCBpbiBjYXRlZ29yaWVzKSB7XG4gICAgICBpZiAoa25vd25DYXRlZ29yaWVzLmluZGV4T2YoY2F0KSA9PT0gLTEpIHtcbiAgICAgICAgb3JkZXJlZENhdGVnb3JpZXMucHVzaChjYXQpO1xuICAgICAgfVxuICAgIH1cblxuICAgIC8vIE5vdyBjcmVhdGUgdGhlIHNlY3Rpb25zIGZvciBlYWNoIGNhdGVnb3J5XG4gICAgb3JkZXJlZENhdGVnb3JpZXMuZm9yRWFjaChjYXQgPT4ge1xuICAgICAgaWYgKCFjYXRlZ29yaWVzW2NhdF0pIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgY29uc3Qga2VybmVsID0ga2VybmVsQ2F0ZWdvcmllcy5pbmRleE9mKGNhdCkgPiAtMTtcblxuICAgICAgaWYgKGNhdCBpbiBjYXRlZ29yaWVzKSB7XG4gICAgICAgIHNlY3Rpb24gPSAoXG4gICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJqcC1MYXVuY2hlci1zZWN0aW9uXCIga2V5PXtjYXR9PlxuICAgICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJqcC1MYXVuY2hlci1zZWN0aW9uSGVhZGVyXCI+XG4gICAgICAgICAgICAgIDxoMiBjbGFzc05hbWU9XCJqcC1MYXVuY2hlci1zZWN0aW9uVGl0bGVcIj57Y2F0fTwvaDI+XG4gICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPVwianAtTGF1bmNoZXItY2FyZENvbnRhaW5lclwiPlxuICAgICAgICAgICAgICB7dG9BcnJheShcbiAgICAgICAgICAgICAgICBtYXAoY2F0ZWdvcmllc1tjYXRdLCAoaXRlbTogSUxhdW5jaGVyLklJdGVtT3B0aW9ucykgPT4ge1xuICAgICAgICAgICAgICAgICAgcmV0dXJuIENhcmQoXG4gICAgICAgICAgICAgICAgICAgIGtlcm5lbCxcbiAgICAgICAgICAgICAgICAgICAgaXRlbSxcbiAgICAgICAgICAgICAgICAgICAgdGhpcyxcbiAgICAgICAgICAgICAgICAgICAgdGhpcy5fY29tbWFuZHMsXG4gICAgICAgICAgICAgICAgICAgIHRoaXMuX3RyYW5zLFxuICAgICAgICAgICAgICAgICAgICB0aGlzLl9jYWxsYmFja1xuICAgICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICB9KVxuICAgICAgICAgICAgICApfVxuICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgPC9kaXY+XG4gICAgICAgICk7XG4gICAgICAgIHNlY3Rpb25zLnB1c2goc2VjdGlvbik7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICAvLyBXcmFwIHRoZSBzZWN0aW9ucyBpbiBib2R5IGFuZCBjb250ZW50IGRpdnMuXG4gICAgcmV0dXJuIChcbiAgICAgIDxkaXYgY2xhc3NOYW1lPVwianAtTGF1bmNoZXItYm9keVwiPlxuICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImpwLUxhdW5jaGVyLWNvbnRlbnRcIj5cbiAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImpwLUxhdW5jaGVyLWN3ZFwiPlxuICAgICAgICAgICAgPGgzPnt0aGlzLmN3ZH08L2gzPlxuICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgIHtzZWN0aW9uc31cbiAgICAgICAgPC9kaXY+XG4gICAgICA8L2Rpdj5cbiAgICApO1xuICB9XG5cbiAgcHJvdGVjdGVkIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yO1xuICBwcml2YXRlIF90cmFuczogVHJhbnNsYXRpb25CdW5kbGU7XG4gIHByaXZhdGUgX2NvbW1hbmRzOiBDb21tYW5kUmVnaXN0cnk7XG4gIHByaXZhdGUgX2NhbGxiYWNrOiAod2lkZ2V0OiBXaWRnZXQpID0+IHZvaWQ7XG4gIHByaXZhdGUgX3BlbmRpbmcgPSBmYWxzZTtcbiAgcHJpdmF0ZSBfY3dkID0gJyc7XG59XG4vKipcbiAqIEEgcHVyZSB0c3ggY29tcG9uZW50IGZvciBhIGxhdW5jaGVyIGNhcmQuXG4gKlxuICogQHBhcmFtIGtlcm5lbCAtIHdoZXRoZXIgdGhlIGl0ZW0gdGFrZXMgdXNlcyBhIGtlcm5lbC5cbiAqXG4gKiBAcGFyYW0gaXRlbSAtIHRoZSBsYXVuY2hlciBpdGVtIHRvIHJlbmRlci5cbiAqXG4gKiBAcGFyYW0gbGF1bmNoZXIgLSB0aGUgTGF1bmNoZXIgaW5zdGFuY2UgdG8gd2hpY2ggdGhpcyBpcyBhZGRlZC5cbiAqXG4gKiBAcGFyYW0gY29tbWFuZHMgLSB0aGUgY29tbWFuZCByZWdpc3RyeSBob2xkaW5nIHRoZSBjb21tYW5kIG9mIGl0ZW0uXG4gKlxuICogQHBhcmFtIHRyYW5zIC0gdGhlIHRyYW5zbGF0aW9uIGJ1bmRsZS5cbiAqXG4gKiBAcmV0dXJucyBhIHZkb20gYFZpcnR1YWxFbGVtZW50YCBmb3IgdGhlIGxhdW5jaGVyIGNhcmQuXG4gKi9cbmZ1bmN0aW9uIENhcmQoXG4gIGtlcm5lbDogYm9vbGVhbixcbiAgaXRlbTogSUxhdW5jaGVyLklJdGVtT3B0aW9ucyxcbiAgbGF1bmNoZXI6IExhdW5jaGVyLFxuICBjb21tYW5kczogQ29tbWFuZFJlZ2lzdHJ5LFxuICB0cmFuczogVHJhbnNsYXRpb25CdW5kbGUsXG4gIGxhdW5jaGVyQ2FsbGJhY2s6ICh3aWRnZXQ6IFdpZGdldCkgPT4gdm9pZFxuKTogUmVhY3QuUmVhY3RFbGVtZW50PGFueT4ge1xuICAvLyBHZXQgc29tZSBwcm9wZXJ0aWVzIG9mIHRoZSBjb21tYW5kXG4gIGNvbnN0IGNvbW1hbmQgPSBpdGVtLmNvbW1hbmQ7XG4gIGNvbnN0IGFyZ3MgPSB7IC4uLml0ZW0uYXJncywgY3dkOiBsYXVuY2hlci5jd2QgfTtcbiAgY29uc3QgY2FwdGlvbiA9IGNvbW1hbmRzLmNhcHRpb24oY29tbWFuZCwgYXJncyk7XG4gIGNvbnN0IGxhYmVsID0gY29tbWFuZHMubGFiZWwoY29tbWFuZCwgYXJncyk7XG4gIGNvbnN0IHRpdGxlID0ga2VybmVsID8gbGFiZWwgOiBjYXB0aW9uIHx8IGxhYmVsO1xuXG4gIC8vIEJ1aWxkIHRoZSBvbmNsaWNrIGhhbmRsZXIuXG4gIGNvbnN0IG9uY2xpY2sgPSAoKSA9PiB7XG4gICAgLy8gSWYgYW4gaXRlbSBoYXMgYWxyZWFkeSBiZWVuIGxhdW5jaGVkLFxuICAgIC8vIGRvbid0IHRyeSB0byBsYXVuY2ggYW5vdGhlci5cbiAgICBpZiAobGF1bmNoZXIucGVuZGluZyA9PT0gdHJ1ZSkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBsYXVuY2hlci5wZW5kaW5nID0gdHJ1ZTtcbiAgICB2b2lkIGNvbW1hbmRzXG4gICAgICAuZXhlY3V0ZShjb21tYW5kLCB7XG4gICAgICAgIC4uLml0ZW0uYXJncyxcbiAgICAgICAgY3dkOiBsYXVuY2hlci5jd2RcbiAgICAgIH0pXG4gICAgICAudGhlbih2YWx1ZSA9PiB7XG4gICAgICAgIGxhdW5jaGVyLnBlbmRpbmcgPSBmYWxzZTtcbiAgICAgICAgaWYgKHZhbHVlIGluc3RhbmNlb2YgV2lkZ2V0KSB7XG4gICAgICAgICAgbGF1bmNoZXJDYWxsYmFjayh2YWx1ZSk7XG4gICAgICAgIH1cbiAgICAgIH0pXG4gICAgICAuY2F0Y2goZXJyID0+IHtcbiAgICAgICAgY29uc29sZS5lcnJvcihlcnIpO1xuICAgICAgICBsYXVuY2hlci5wZW5kaW5nID0gZmFsc2U7XG4gICAgICAgIHZvaWQgc2hvd0Vycm9yTWVzc2FnZSh0cmFucy5fcCgnRXJyb3InLCAnTGF1bmNoZXIgRXJyb3InKSwgZXJyKTtcbiAgICAgIH0pO1xuICB9O1xuXG4gIC8vIFdpdGggdGFiaW5kZXggd29ya2luZywgeW91IGNhbiBub3cgcGljayBhIGtlcm5lbCBieSB0YWJiaW5nIGFyb3VuZCBhbmRcbiAgLy8gcHJlc3NpbmcgRW50ZXIuXG4gIGNvbnN0IG9ua2V5cHJlc3MgPSAoZXZlbnQ6IFJlYWN0LktleWJvYXJkRXZlbnQpID0+IHtcbiAgICBpZiAoZXZlbnQua2V5ID09PSAnRW50ZXInKSB7XG4gICAgICBvbmNsaWNrKCk7XG4gICAgfVxuICB9O1xuXG4gIC8vIFJldHVybiB0aGUgVkRPTSBlbGVtZW50LlxuICByZXR1cm4gKFxuICAgIDxkaXZcbiAgICAgIGNsYXNzTmFtZT1cImpwLUxhdW5jaGVyQ2FyZFwiXG4gICAgICB0aXRsZT17dGl0bGV9XG4gICAgICBvbkNsaWNrPXtvbmNsaWNrfVxuICAgICAgb25LZXlQcmVzcz17b25rZXlwcmVzc31cbiAgICAgIHRhYkluZGV4PXswfVxuICAgICAgZGF0YS1jYXRlZ29yeT17aXRlbS5jYXRlZ29yeSB8fCB0cmFucy5fXygnT3RoZXInKX1cbiAgICAgIGtleT17UHJpdmF0ZS5rZXlQcm9wZXJ0eS5nZXQoaXRlbSl9XG4gICAgPlxuICAgICAgPGRpdiBjbGFzc05hbWU9XCJqcC1MYXVuY2hlckNhcmQtbGFiZWxcIiB0aXRsZT17dGl0bGV9PlxuICAgICAgICA8cD5OZXcge2xhYmVsfS4uLjwvcD5cbiAgICAgIDwvZGl2PlxuICAgIDwvZGl2PlxuICApO1xufVxuXG4vKipcbiAqIFRoZSBuYW1lc3BhY2UgZm9yIG1vZHVsZSBwcml2YXRlIGRhdGEuXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgLyoqXG4gICAqIEFuIGluY3JlbWVudGluZyBjb3VudGVyIGZvciBrZXlzLlxuICAgKi9cbiAgbGV0IGlkID0gMDtcblxuICAvKipcbiAgICogQW4gYXR0YWNoZWQgcHJvcGVydHkgZm9yIGFuIGl0ZW0ncyBrZXkuXG4gICAqL1xuICBleHBvcnQgY29uc3Qga2V5UHJvcGVydHkgPSBuZXcgQXR0YWNoZWRQcm9wZXJ0eTxcbiAgICBJTGF1bmNoZXIuSUl0ZW1PcHRpb25zLFxuICAgIG51bWJlclxuICA+KHtcbiAgICBuYW1lOiAna2V5JyxcbiAgICBjcmVhdGU6ICgpID0+IGlkKytcbiAgfSk7XG5cbiAgLyoqXG4gICAqIENyZWF0ZSBhIGZ1bGx5IHNwZWNpZmllZCBpdGVtIGdpdmVuIGl0ZW0gb3B0aW9ucy5cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBjcmVhdGVJdGVtKFxuICAgIG9wdGlvbnM6IElMYXVuY2hlci5JSXRlbU9wdGlvbnNcbiAgKTogSUxhdW5jaGVyLklJdGVtT3B0aW9ucyB7XG4gICAgcmV0dXJuIHtcbiAgICAgIC4uLm9wdGlvbnMsXG4gICAgICBjYXRlZ29yeTogb3B0aW9ucy5jYXRlZ29yeSB8fCAnJyxcbiAgICAgIHJhbms6IG9wdGlvbnMucmFuayAhPT0gdW5kZWZpbmVkID8gb3B0aW9ucy5yYW5rIDogSW5maW5pdHlcbiAgICB9O1xuICB9XG5cbiAgLyoqXG4gICAqIEEgc29ydCBjb21wYXJpc29uIGZ1bmN0aW9uIGZvciBhIGxhdW5jaGVyIGl0ZW0uXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gc29ydENtcChcbiAgICBhOiBJTGF1bmNoZXIuSUl0ZW1PcHRpb25zLFxuICAgIGI6IElMYXVuY2hlci5JSXRlbU9wdGlvbnMsXG4gICAgY3dkOiBzdHJpbmcsXG4gICAgY29tbWFuZHM6IENvbW1hbmRSZWdpc3RyeVxuICApOiBudW1iZXIge1xuICAgIC8vIEZpcnN0LCBjb21wYXJlIGJ5IHJhbmsuXG4gICAgY29uc3QgcjEgPSBhLnJhbms7XG4gICAgY29uc3QgcjIgPSBiLnJhbms7XG4gICAgaWYgKHIxICE9PSByMiAmJiByMSAhPT0gdW5kZWZpbmVkICYmIHIyICE9PSB1bmRlZmluZWQpIHtcbiAgICAgIHJldHVybiByMSA8IHIyID8gLTEgOiAxOyAvLyBJbmZpbml0eSBzYWZlXG4gICAgfVxuXG4gICAgLy8gRmluYWxseSwgY29tcGFyZSBieSBkaXNwbGF5IG5hbWUuXG4gICAgY29uc3QgYUxhYmVsID0gY29tbWFuZHMubGFiZWwoYS5jb21tYW5kLCB7IC4uLmEuYXJncywgY3dkIH0pO1xuICAgIGNvbnN0IGJMYWJlbCA9IGNvbW1hbmRzLmxhYmVsKGIuY29tbWFuZCwgeyAuLi5iLmFyZ3MsIGN3ZCB9KTtcbiAgICByZXR1cm4gYUxhYmVsLmxvY2FsZUNvbXBhcmUoYkxhYmVsKTtcbiAgfVxufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9