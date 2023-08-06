"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_cell-toolbar_lib_index_js"],{

/***/ "../../packages/cell-toolbar/lib/celltoolbartracker.js":
/*!*************************************************************!*\
  !*** ../../packages/cell-toolbar/lib/celltoolbartracker.js ***!
  \*************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CellBarExtension": () => (/* binding */ CellBarExtension),
/* harmony export */   "CellToolbarTracker": () => (/* binding */ CellToolbarTracker)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/observables */ "webpack/sharing/consume/default/@jupyterlab/observables/@jupyterlab/observables");
/* harmony import */ var _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_observables__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_4__);
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/





/*
 * Text mime types
 */
const TEXT_MIME_TYPES = [
    'text/plain',
    'application/vnd.jupyter.stdout',
    'application/vnd.jupyter.stderr'
];
/**
 * Widget cell toolbar classes
 */
const CELL_TOOLBAR_CLASS = 'jp-cell-toolbar';
const CELL_MENU_CLASS = 'jp-cell-menu';
/**
 * Class for a cell whose contents overlap with the cell toolbar
 */
const TOOLBAR_OVERLAP_CLASS = 'jp-toolbar-overlap';
/**
 * Watch a notebook so that a cell toolbar appears on the active cell
 */
class CellToolbarTracker {
    constructor(panel, toolbar) {
        this._isDisposed = false;
        this._panel = panel;
        this._previousActiveCell = this._panel.content.activeCell;
        this._toolbar = toolbar;
        this._onToolbarChanged();
        this._toolbar.changed.connect(this._onToolbarChanged, this);
        // Only add the toolbar to the notebook's active cell (if any) once it has fully rendered and been revealed.
        void panel.revealed.then(() => this._onActiveCellChanged(panel.content));
        // Check whether the toolbar should be rendered upon a layout change
        panel.content.renderingLayoutChanged.connect(this._onActiveCellChanged, this);
        // Handle subsequent changes of active cell.
        panel.content.activeCellChanged.connect(this._onActiveCellChanged, this);
    }
    _onActiveCellChanged(notebook) {
        if (this._previousActiveCell) {
            this._removeToolbar(this._previousActiveCell.model);
        }
        const activeCell = notebook.activeCell;
        if (!activeCell) {
            return;
        }
        this._addToolbar(activeCell.model);
        this._previousActiveCell = activeCell;
        this._updateCellForToolbarOverlap(activeCell);
    }
    get isDisposed() {
        return this._isDisposed;
    }
    dispose() {
        var _a;
        if (this.isDisposed) {
            return;
        }
        this._isDisposed = true;
        this._toolbar.changed.disconnect(this._onToolbarChanged, this);
        const cells = (_a = this._panel) === null || _a === void 0 ? void 0 : _a.context.model.cells;
        if (cells) {
            (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.each)(cells.iter(), model => this._removeToolbar(model));
        }
        this._panel = null;
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__.Signal.clearData(this);
    }
    _addToolbar(model) {
        const cell = this._getCell(model);
        if (cell) {
            const toolbarWidget = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.Toolbar();
            toolbarWidget.addClass(CELL_MENU_CLASS);
            (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.toArray)(this._toolbar).forEach(({ name, widget }) => {
                toolbarWidget.addItem(name, widget);
            });
            toolbarWidget.addClass(CELL_TOOLBAR_CLASS);
            cell.layout.insertWidget(0, toolbarWidget);
            // For rendered markdown, watch for resize events.
            cell.displayChanged.connect(this._resizeEventCallback, this);
            // Watch for changes in the cell's contents.
            cell.model.contentChanged.connect(this._changedEventCallback, this);
        }
    }
    _getCell(model) {
        var _a;
        return (_a = this._panel) === null || _a === void 0 ? void 0 : _a.content.widgets.find(widget => widget.model === model);
    }
    _findToolbarWidgets(cell) {
        const widgets = cell.layout.widgets;
        // Search for header using the CSS class or use the first one if not found.
        return widgets.filter(widget => widget.hasClass(CELL_TOOLBAR_CLASS)) || [];
    }
    _removeToolbar(model) {
        const cell = this._getCell(model);
        if (cell) {
            this._findToolbarWidgets(cell).forEach(widget => widget.dispose());
            // Attempt to remove the resize and changed event handlers.
            cell.displayChanged.disconnect(this._resizeEventCallback, this);
        }
        model.contentChanged.disconnect(this._changedEventCallback, this);
    }
    /**
     * Call back on settings changes
     */
    _onToolbarChanged() {
        var _a;
        // Reset toolbar when settings changes
        const activeCell = (_a = this._panel) === null || _a === void 0 ? void 0 : _a.content.activeCell;
        if (activeCell) {
            this._removeToolbar(activeCell.model);
            this._addToolbar(activeCell.model);
        }
    }
    _changedEventCallback() {
        var _a;
        const activeCell = (_a = this._panel) === null || _a === void 0 ? void 0 : _a.content.activeCell;
        if (activeCell === null || activeCell === undefined) {
            return;
        }
        this._updateCellForToolbarOverlap(activeCell);
    }
    _resizeEventCallback() {
        var _a;
        const activeCell = (_a = this._panel) === null || _a === void 0 ? void 0 : _a.content.activeCell;
        if (activeCell === null || activeCell === undefined) {
            return;
        }
        this._updateCellForToolbarOverlap(activeCell);
    }
    _updateCellForToolbarOverlap(activeCell) {
        // Remove the "toolbar overlap" class from the cell, rendering the cell's toolbar
        const activeCellElement = activeCell.node;
        activeCellElement.classList.remove(TOOLBAR_OVERLAP_CLASS);
        if (this._cellToolbarOverlapsContents(activeCell)) {
            // Add the "toolbar overlap" class to the cell, completely concealing the toolbar,
            // if the first line of the content overlaps with it at all
            activeCellElement.classList.add(TOOLBAR_OVERLAP_CLASS);
        }
    }
    _cellToolbarOverlapsContents(activeCell) {
        var _a;
        const cellType = activeCell.model.type;
        // If the toolbar is too large for the current cell, hide it.
        const cellLeft = this._cellEditorWidgetLeft(activeCell);
        const cellRight = this._cellEditorWidgetRight(activeCell);
        const toolbarLeft = this._cellToolbarLeft(activeCell);
        if (toolbarLeft === null) {
            return false;
        }
        // The toolbar should not take up more than 50% of the cell.
        if ((cellLeft + cellRight) / 2 > toolbarLeft) {
            return true;
        }
        if (cellType === 'markdown' && activeCell.rendered) {
            // Check for overlap in rendered markdown content
            return this._markdownOverlapsToolbar(activeCell);
        }
        // Check for overlap in code content
        if (((_a = this._panel) === null || _a === void 0 ? void 0 : _a.content.renderingLayout) === 'default') {
            return this._codeOverlapsToolbar(activeCell);
        }
        else {
            return this._outputOverlapsToolbar(activeCell);
        }
    }
    /**
     * Check for overlap between rendered Markdown and the cell toolbar
     *
     * @param activeCell A rendered MarkdownCell
     * @returns `true` if the first line of the output overlaps with the cell toolbar, `false` otherwise
     */
    _markdownOverlapsToolbar(activeCell) {
        const markdownOutput = activeCell.inputArea; // Rendered markdown appears in the input area
        // Get the rendered markdown as a widget.
        const markdownOutputWidget = markdownOutput.renderedInput;
        const markdownOutputElement = markdownOutputWidget.node;
        const firstOutputElementChild = markdownOutputElement.firstElementChild;
        if (firstOutputElementChild === null) {
            return false;
        }
        // Temporarily set the element's max width so that the bounding client rectangle only encompasses the content.
        const oldMaxWidth = firstOutputElementChild.style.maxWidth;
        firstOutputElementChild.style.maxWidth = 'max-content';
        const lineRight = firstOutputElementChild.getBoundingClientRect().right;
        // Reinstate the old max width.
        firstOutputElementChild.style.maxWidth = oldMaxWidth;
        const toolbarLeft = this._cellToolbarLeft(activeCell);
        return toolbarLeft === null ? false : lineRight > toolbarLeft;
    }
    _outputOverlapsToolbar(activeCell) {
        const outputArea = activeCell.outputArea.node;
        if (outputArea) {
            const outputs = outputArea.querySelectorAll('[data-mime-type]');
            const toolbarRect = this._cellToolbarRect(activeCell);
            if (toolbarRect) {
                const { left: toolbarLeft, bottom: toolbarBottom } = toolbarRect;
                return Array.from(outputs).some(output => {
                    const node = output.firstElementChild;
                    if (node) {
                        const range = new Range();
                        if (TEXT_MIME_TYPES.includes(output.getAttribute('data-mime-type') || '')) {
                            // If the node is plain text, it's in a <pre>. To get the true bounding box of the
                            // text, the node contents need to be selected.
                            range.selectNodeContents(node);
                        }
                        else {
                            range.selectNode(node);
                        }
                        const { right: nodeRight, top: nodeTop } = range.getBoundingClientRect();
                        // Note: y-coordinate increases toward the bottom of page
                        return nodeRight > toolbarLeft && nodeTop < toolbarBottom;
                    }
                    return false;
                });
            }
        }
        return false;
    }
    _codeOverlapsToolbar(activeCell) {
        const editorWidget = activeCell.editorWidget;
        const editor = activeCell.editor;
        if (editor.lineCount < 1) {
            return false; // Nothing in the editor
        }
        const codeMirrorLines = editorWidget.node.getElementsByClassName('CodeMirror-line');
        if (codeMirrorLines.length < 1) {
            return false; // No lines present
        }
        const lineRight = codeMirrorLines[0].children[0] // First span under first pre
            .getBoundingClientRect().right;
        const toolbarLeft = this._cellToolbarLeft(activeCell);
        return toolbarLeft === null ? false : lineRight > toolbarLeft;
    }
    _cellEditorWidgetLeft(activeCell) {
        return activeCell.editorWidget.node.getBoundingClientRect().left;
    }
    _cellEditorWidgetRight(activeCell) {
        return activeCell.editorWidget.node.getBoundingClientRect().right;
    }
    _cellToolbarRect(activeCell) {
        const toolbarWidgets = this._findToolbarWidgets(activeCell);
        if (toolbarWidgets.length < 1) {
            return null;
        }
        const activeCellToolbar = toolbarWidgets[0].node;
        return activeCellToolbar.getBoundingClientRect();
    }
    _cellToolbarLeft(activeCell) {
        var _a;
        return ((_a = this._cellToolbarRect(activeCell)) === null || _a === void 0 ? void 0 : _a.left) || null;
    }
}
const defaultToolbarItems = [
    {
        command: 'notebook:run-cell',
        name: 'run-cell'
    },
    {
        command: 'notebook:duplicate-below',
        name: 'duplicate-cell'
    },
    {
        command: 'notebook:insert-cell-above',
        name: 'insert-cell-above'
    },
    {
        command: 'notebook:insert-cell-below',
        name: 'insert-cell-below'
    },
    {
        command: 'notebook:delete-cell',
        name: 'delete-cell'
    }
];
/**
 * Widget extension that creates a CellToolbarTracker each time a notebook is
 * created.
 */
class CellBarExtension {
    constructor(commands, toolbarFactory) {
        this._commands = commands;
        this._toolbarFactory = toolbarFactory !== null && toolbarFactory !== void 0 ? toolbarFactory : this.defaultToolbarFactory;
    }
    get defaultToolbarFactory() {
        const itemFactory = (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.createDefaultFactory)(this._commands);
        return (widget) => new _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_1__.ObservableList({
            values: defaultToolbarItems.map(item => {
                return {
                    name: item.name,
                    widget: itemFactory(CellBarExtension.FACTORY_NAME, widget, item)
                };
            })
        });
    }
    createNew(panel) {
        return new CellToolbarTracker(panel, this._toolbarFactory(panel));
    }
}
CellBarExtension.FACTORY_NAME = 'Cell';


/***/ }),

/***/ "../../packages/cell-toolbar/lib/index.js":
/*!************************************************!*\
  !*** ../../packages/cell-toolbar/lib/index.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CellBarExtension": () => (/* reexport safe */ _celltoolbartracker__WEBPACK_IMPORTED_MODULE_0__.CellBarExtension),
/* harmony export */   "CellToolbarTracker": () => (/* reexport safe */ _celltoolbartracker__WEBPACK_IMPORTED_MODULE_0__.CellToolbarTracker)
/* harmony export */ });
/* harmony import */ var _celltoolbartracker__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./celltoolbartracker */ "../../packages/cell-toolbar/lib/celltoolbartracker.js");
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module cell-toolbar
 */



/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY2VsbC10b29sYmFyX2xpYl9pbmRleF9qcy4zNzBmNDMzMWM1MGIyZDllNDFiMi5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQTs7OytFQUcrRTtBQUNGO0FBSUg7QUFDdEI7QUFDRjtBQUdQO0FBRzNDOztHQUVHO0FBQ0gsTUFBTSxlQUFlLEdBQUc7SUFDdEIsWUFBWTtJQUNaLGdDQUFnQztJQUNoQyxnQ0FBZ0M7Q0FDakMsQ0FBQztBQUVGOztHQUVHO0FBQ0gsTUFBTSxrQkFBa0IsR0FBRyxpQkFBaUIsQ0FBQztBQUM3QyxNQUFNLGVBQWUsR0FBRyxjQUFjLENBQUM7QUFFdkM7O0dBRUc7QUFDSCxNQUFNLHFCQUFxQixHQUFHLG9CQUFvQixDQUFDO0FBRW5EOztHQUVHO0FBQ0ksTUFBTSxrQkFBa0I7SUFDN0IsWUFDRSxLQUFvQixFQUNwQixPQUFzRDtRQThSaEQsZ0JBQVcsR0FBRyxLQUFLLENBQUM7UUE1UjFCLElBQUksQ0FBQyxNQUFNLEdBQUcsS0FBSyxDQUFDO1FBQ3BCLElBQUksQ0FBQyxtQkFBbUIsR0FBRyxJQUFJLENBQUMsTUFBTSxDQUFDLE9BQU8sQ0FBQyxVQUFVLENBQUM7UUFDMUQsSUFBSSxDQUFDLFFBQVEsR0FBRyxPQUFPLENBQUM7UUFFeEIsSUFBSSxDQUFDLGlCQUFpQixFQUFFLENBQUM7UUFDekIsSUFBSSxDQUFDLFFBQVEsQ0FBQyxPQUFPLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxpQkFBaUIsRUFBRSxJQUFJLENBQUMsQ0FBQztRQUU1RCw0R0FBNEc7UUFDNUcsS0FBSyxLQUFLLENBQUMsUUFBUSxDQUFDLElBQUksQ0FBQyxHQUFHLEVBQUUsQ0FBQyxJQUFJLENBQUMsb0JBQW9CLENBQUMsS0FBSyxDQUFDLE9BQU8sQ0FBQyxDQUFDLENBQUM7UUFFekUsb0VBQW9FO1FBQ3BFLEtBQUssQ0FBQyxPQUFPLENBQUMsc0JBQXNCLENBQUMsT0FBTyxDQUMxQyxJQUFJLENBQUMsb0JBQW9C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QixJQUFJLENBQUMsZUFBZSxHQUFHLGNBQWMsYUFBZCxjQUFjLGNBQWQsY0FBYyxHQUFJLElBQUksQ0FBQyxxQkFBcUIsQ0FBQztJQUN0RSxDQUFDO0lBRUQsSUFBYyxxQkFBcUI7UUFHakMsTUFBTSxXQUFXLEdBQUcsMEVBQW9CLENBQUMsSUFBSSxDQUFDLFNBQVMsQ0FBQyxDQUFDO1FBQ3pELE9BQU8sQ0FBQyxNQUFjLEVBQUUsRUFBRSxDQUN4QixJQUFJLG1FQUFjLENBQUM7WUFDakIsTUFBTSxFQUFFLG1CQUFtQixDQUFDLEdBQUcsQ0FBQyxJQUFJLENBQUMsRUFBRTtnQkFDckMsT0FBTztvQkFDTCxJQUFJLEVBQUUsSUFBSSxDQUFDLElBQUk7b0JBQ2YsTUFBTSxFQUFFLFdBQVcsQ0FBQyxnQkFBZ0IsQ0FBQyxZQUFZLEVBQUUsTUFBTSxFQUFFLElBQUksQ0FBQztpQkFDakUsQ0FBQztZQUNKLENBQUMsQ0FBQztTQUNILENBQUMsQ0FBQztJQUNQLENBQUM7SUFFRCxTQUFTLENBQUMsS0FBb0I7UUFDNUIsT0FBTyxJQUFJLGtCQUFrQixDQUFDLEtBQUssRUFBRSxJQUFJLENBQUMsZUFBZSxDQUFDLEtBQUssQ0FBQyxDQUFDLENBQUM7SUFDcEUsQ0FBQzs7QUE3Qk0sNkJBQVksR0FBRyxNQUFNLENBQUM7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDMVcvQjs7OytFQUcrRTtBQUMvRTs7O0dBR0c7QUFDa0MiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY2VsbC10b29sYmFyL3NyYy9jZWxsdG9vbGJhcnRyYWNrZXIudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NlbGwtdG9vbGJhci9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLyogLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbnwgQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG58IERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG58LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5pbXBvcnQgeyBjcmVhdGVEZWZhdWx0RmFjdG9yeSwgVG9vbGJhclJlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgQ2VsbCwgQ29kZUNlbGwsIElDZWxsTW9kZWwsIE1hcmtkb3duQ2VsbCB9IGZyb20gJ0BqdXB5dGVybGFiL2NlbGxzJztcbmltcG9ydCB7IERvY3VtZW50UmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9kb2NyZWdpc3RyeSc7XG5pbXBvcnQgeyBOb3RlYm9vaywgTm90ZWJvb2tQYW5lbCB9IGZyb20gJ0BqdXB5dGVybGFiL25vdGVib29rJztcbmltcG9ydCB7IElPYnNlcnZhYmxlTGlzdCwgT2JzZXJ2YWJsZUxpc3QgfSBmcm9tICdAanVweXRlcmxhYi9vYnNlcnZhYmxlcyc7XG5pbXBvcnQgeyBUb29sYmFyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBlYWNoLCB0b0FycmF5IH0gZnJvbSAnQGx1bWluby9hbGdvcml0aG0nO1xuaW1wb3J0IHsgQ29tbWFuZFJlZ2lzdHJ5IH0gZnJvbSAnQGx1bWluby9jb21tYW5kcyc7XG5pbXBvcnQgeyBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBQYW5lbExheW91dCwgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcblxuLypcbiAqIFRleHQgbWltZSB0eXBlc1xuICovXG5jb25zdCBURVhUX01JTUVfVFlQRVMgPSBbXG4gICd0ZXh0L3BsYWluJyxcbiAgJ2FwcGxpY2F0aW9uL3ZuZC5qdXB5dGVyLnN0ZG91dCcsXG4gICdhcHBsaWNhdGlvbi92bmQuanVweXRlci5zdGRlcnInXG5dO1xuXG4vKipcbiAqIFdpZGdldCBjZWxsIHRvb2xiYXIgY2xhc3Nlc1xuICovXG5jb25zdCBDRUxMX1RPT0xCQVJfQ0xBU1MgPSAnanAtY2VsbC10b29sYmFyJztcbmNvbnN0IENFTExfTUVOVV9DTEFTUyA9ICdqcC1jZWxsLW1lbnUnO1xuXG4vKipcbiAqIENsYXNzIGZvciBhIGNlbGwgd2hvc2UgY29udGVudHMgb3ZlcmxhcCB3aXRoIHRoZSBjZWxsIHRvb2xiYXJcbiAqL1xuY29uc3QgVE9PTEJBUl9PVkVSTEFQX0NMQVNTID0gJ2pwLXRvb2xiYXItb3ZlcmxhcCc7XG5cbi8qKlxuICogV2F0Y2ggYSBub3RlYm9vayBzbyB0aGF0IGEgY2VsbCB0b29sYmFyIGFwcGVhcnMgb24gdGhlIGFjdGl2ZSBjZWxsXG4gKi9cbmV4cG9ydCBjbGFzcyBDZWxsVG9vbGJhclRyYWNrZXIgaW1wbGVtZW50cyBJRGlzcG9zYWJsZSB7XG4gIGNvbnN0cnVjdG9yKFxuICAgIHBhbmVsOiBOb3RlYm9va1BhbmVsLFxuICAgIHRvb2xiYXI6IElPYnNlcnZhYmxlTGlzdDxUb29sYmFyUmVnaXN0cnkuSVRvb2xiYXJJdGVtPlxuICApIHtcbiAgICB0aGlzLl9wYW5lbCA9IHBhbmVsO1xuICAgIHRoaXMuX3ByZXZpb3VzQWN0aXZlQ2VsbCA9IHRoaXMuX3BhbmVsLmNvbnRlbnQuYWN0aXZlQ2VsbDtcbiAgICB0aGlzLl90b29sYmFyID0gdG9vbGJhcjtcblxuICAgIHRoaXMuX29uVG9vbGJhckNoYW5nZWQoKTtcbiAgICB0aGlzLl90b29sYmFyLmNoYW5nZWQuY29ubmVjdCh0aGlzLl9vblRvb2xiYXJDaGFuZ2VkLCB0aGlzKTtcblxuICAgIC8vIE9ubHkgYWRkIHRoZSB0b29sYmFyIHRvIHRoZSBub3RlYm9vaydzIGFjdGl2ZSBjZWxsIChpZiBhbnkpIG9uY2UgaXQgaGFzIGZ1bGx5IHJlbmRlcmVkIGFuZCBiZWVuIHJldmVhbGVkLlxuICAgIHZvaWQgcGFuZWwucmV2ZWFsZWQudGhlbigoKSA9PiB0aGlzLl9vbkFjdGl2ZUNlbGxDaGFuZ2VkKHBhbmVsLmNvbnRlbnQpKTtcblxuICAgIC8vIENoZWNrIHdoZXRoZXIgdGhlIHRvb2xiYXIgc2hvdWxkIGJlIHJlbmRlcmVkIHVwb24gYSBsYXlvdXQgY2hhbmdlXG4gICAgcGFuZWwuY29udGVudC5yZW5kZXJpbmdMYXlvdXRDaGFuZ2VkLmNvbm5lY3QoXG4gICAgICB0aGlzLl9vbkFjdGl2ZUNlbGxDaGFuZ2VkLFxuICAgICAgdGhpc1xuICAgICk7XG5cbiAgICAvLyBIYW5kbGUgc3Vic2VxdWVudCBjaGFuZ2VzIG9mIGFjdGl2ZSBjZWxsLlxuICAgIHBhbmVsLmNvbnRlbnQuYWN0aXZlQ2VsbENoYW5nZWQuY29ubmVjdCh0aGlzLl9vbkFjdGl2ZUNlbGxDaGFuZ2VkLCB0aGlzKTtcbiAgfVxuXG4gIF9vbkFjdGl2ZUNlbGxDaGFuZ2VkKG5vdGVib29rOiBOb3RlYm9vayk6IHZvaWQge1xuICAgIGlmICh0aGlzLl9wcmV2aW91c0FjdGl2ZUNlbGwpIHtcbiAgICAgIHRoaXMuX3JlbW92ZVRvb2xiYXIodGhpcy5fcHJldmlvdXNBY3RpdmVDZWxsLm1vZGVsKTtcbiAgICB9XG5cbiAgICBjb25zdCBhY3RpdmVDZWxsID0gbm90ZWJvb2suYWN0aXZlQ2VsbDtcbiAgICBpZiAoIWFjdGl2ZUNlbGwpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICB0aGlzLl9hZGRUb29sYmFyKGFjdGl2ZUNlbGwubW9kZWwpO1xuICAgIHRoaXMuX3ByZXZpb3VzQWN0aXZlQ2VsbCA9IGFjdGl2ZUNlbGw7XG5cbiAgICB0aGlzLl91cGRhdGVDZWxsRm9yVG9vbGJhck92ZXJsYXAoYWN0aXZlQ2VsbCk7XG4gIH1cblxuICBnZXQgaXNEaXNwb3NlZCgpOiBib29sZWFuIHtcbiAgICByZXR1cm4gdGhpcy5faXNEaXNwb3NlZDtcbiAgfVxuXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICB0aGlzLl9pc0Rpc3Bvc2VkID0gdHJ1ZTtcblxuICAgIHRoaXMuX3Rvb2xiYXIuY2hhbmdlZC5kaXNjb25uZWN0KHRoaXMuX29uVG9vbGJhckNoYW5nZWQsIHRoaXMpO1xuXG4gICAgY29uc3QgY2VsbHMgPSB0aGlzLl9wYW5lbD8uY29udGV4dC5tb2RlbC5jZWxscztcbiAgICBpZiAoY2VsbHMpIHtcbiAgICAgIGVhY2goY2VsbHMuaXRlcigpLCBtb2RlbCA9PiB0aGlzLl9yZW1vdmVUb29sYmFyKG1vZGVsKSk7XG4gICAgfVxuXG4gICAgdGhpcy5fcGFuZWwgPSBudWxsO1xuXG4gICAgU2lnbmFsLmNsZWFyRGF0YSh0aGlzKTtcbiAgfVxuXG4gIHByaXZhdGUgX2FkZFRvb2xiYXIobW9kZWw6IElDZWxsTW9kZWwpOiB2b2lkIHtcbiAgICBjb25zdCBjZWxsID0gdGhpcy5fZ2V0Q2VsbChtb2RlbCk7XG5cbiAgICBpZiAoY2VsbCkge1xuICAgICAgY29uc3QgdG9vbGJhcldpZGdldCA9IG5ldyBUb29sYmFyKCk7XG4gICAgICB0b29sYmFyV2lkZ2V0LmFkZENsYXNzKENFTExfTUVOVV9DTEFTUyk7XG5cbiAgICAgIHRvQXJyYXkodGhpcy5fdG9vbGJhcikuZm9yRWFjaCgoeyBuYW1lLCB3aWRnZXQgfSkgPT4ge1xuICAgICAgICB0b29sYmFyV2lkZ2V0LmFkZEl0ZW0obmFtZSwgd2lkZ2V0KTtcbiAgICAgIH0pO1xuXG4gICAgICB0b29sYmFyV2lkZ2V0LmFkZENsYXNzKENFTExfVE9PTEJBUl9DTEFTUyk7XG4gICAgICAoY2VsbC5sYXlvdXQgYXMgUGFuZWxMYXlvdXQpLmluc2VydFdpZGdldCgwLCB0b29sYmFyV2lkZ2V0KTtcblxuICAgICAgLy8gRm9yIHJlbmRlcmVkIG1hcmtkb3duLCB3YXRjaCBmb3IgcmVzaXplIGV2ZW50cy5cbiAgICAgIGNlbGwuZGlzcGxheUNoYW5nZWQuY29ubmVjdCh0aGlzLl9yZXNpemVFdmVudENhbGxiYWNrLCB0aGlzKTtcblxuICAgICAgLy8gV2F0Y2ggZm9yIGNoYW5nZXMgaW4gdGhlIGNlbGwncyBjb250ZW50cy5cbiAgICAgIGNlbGwubW9kZWwuY29udGVudENoYW5nZWQuY29ubmVjdCh0aGlzLl9jaGFuZ2VkRXZlbnRDYWxsYmFjaywgdGhpcyk7XG4gICAgfVxuICB9XG5cbiAgcHJpdmF0ZSBfZ2V0Q2VsbChtb2RlbDogSUNlbGxNb2RlbCk6IENlbGwgfCB1bmRlZmluZWQge1xuICAgIHJldHVybiB0aGlzLl9wYW5lbD8uY29udGVudC53aWRnZXRzLmZpbmQod2lkZ2V0ID0+IHdpZGdldC5tb2RlbCA9PT0gbW9kZWwpO1xuICB9XG5cbiAgcHJpdmF0ZSBfZmluZFRvb2xiYXJXaWRnZXRzKGNlbGw6IENlbGwpOiBXaWRnZXRbXSB7XG4gICAgY29uc3Qgd2lkZ2V0cyA9IChjZWxsLmxheW91dCBhcyBQYW5lbExheW91dCkud2lkZ2V0cztcblxuICAgIC8vIFNlYXJjaCBmb3IgaGVhZGVyIHVzaW5nIHRoZSBDU1MgY2xhc3Mgb3IgdXNlIHRoZSBmaXJzdCBvbmUgaWYgbm90IGZvdW5kLlxuICAgIHJldHVybiB3aWRnZXRzLmZpbHRlcih3aWRnZXQgPT4gd2lkZ2V0Lmhhc0NsYXNzKENFTExfVE9PTEJBUl9DTEFTUykpIHx8IFtdO1xuICB9XG5cbiAgcHJpdmF0ZSBfcmVtb3ZlVG9vbGJhcihtb2RlbDogSUNlbGxNb2RlbCk6IHZvaWQge1xuICAgIGNvbnN0IGNlbGwgPSB0aGlzLl9nZXRDZWxsKG1vZGVsKTtcbiAgICBpZiAoY2VsbCkge1xuICAgICAgdGhpcy5fZmluZFRvb2xiYXJXaWRnZXRzKGNlbGwpLmZvckVhY2god2lkZ2V0ID0+IHdpZGdldC5kaXNwb3NlKCkpO1xuICAgICAgLy8gQXR0ZW1wdCB0byByZW1vdmUgdGhlIHJlc2l6ZSBhbmQgY2hhbmdlZCBldmVudCBoYW5kbGVycy5cbiAgICAgIGNlbGwuZGlzcGxheUNoYW5nZWQuZGlzY29ubmVjdCh0aGlzLl9yZXNpemVFdmVudENhbGxiYWNrLCB0aGlzKTtcbiAgICB9XG4gICAgbW9kZWwuY29udGVudENoYW5nZWQuZGlzY29ubmVjdCh0aGlzLl9jaGFuZ2VkRXZlbnRDYWxsYmFjaywgdGhpcyk7XG4gIH1cblxuICAvKipcbiAgICogQ2FsbCBiYWNrIG9uIHNldHRpbmdzIGNoYW5nZXNcbiAgICovXG4gIHByaXZhdGUgX29uVG9vbGJhckNoYW5nZWQoKTogdm9pZCB7XG4gICAgLy8gUmVzZXQgdG9vbGJhciB3aGVuIHNldHRpbmdzIGNoYW5nZXNcbiAgICBjb25zdCBhY3RpdmVDZWxsOiBDZWxsPElDZWxsTW9kZWw+IHwgbnVsbCB8IHVuZGVmaW5lZCA9XG4gICAgICB0aGlzLl9wYW5lbD8uY29udGVudC5hY3RpdmVDZWxsO1xuICAgIGlmIChhY3RpdmVDZWxsKSB7XG4gICAgICB0aGlzLl9yZW1vdmVUb29sYmFyKGFjdGl2ZUNlbGwubW9kZWwpO1xuICAgICAgdGhpcy5fYWRkVG9vbGJhcihhY3RpdmVDZWxsLm1vZGVsKTtcbiAgICB9XG4gIH1cblxuICBwcml2YXRlIF9jaGFuZ2VkRXZlbnRDYWxsYmFjaygpOiB2b2lkIHtcbiAgICBjb25zdCBhY3RpdmVDZWxsID0gdGhpcy5fcGFuZWw/LmNvbnRlbnQuYWN0aXZlQ2VsbDtcbiAgICBpZiAoYWN0aXZlQ2VsbCA9PT0gbnVsbCB8fCBhY3RpdmVDZWxsID09PSB1bmRlZmluZWQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICB0aGlzLl91cGRhdGVDZWxsRm9yVG9vbGJhck92ZXJsYXAoYWN0aXZlQ2VsbCk7XG4gIH1cblxuICBwcml2YXRlIF9yZXNpemVFdmVudENhbGxiYWNrKCk6IHZvaWQge1xuICAgIGNvbnN0IGFjdGl2ZUNlbGwgPSB0aGlzLl9wYW5lbD8uY29udGVudC5hY3RpdmVDZWxsO1xuICAgIGlmIChhY3RpdmVDZWxsID09PSBudWxsIHx8IGFjdGl2ZUNlbGwgPT09IHVuZGVmaW5lZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIHRoaXMuX3VwZGF0ZUNlbGxGb3JUb29sYmFyT3ZlcmxhcChhY3RpdmVDZWxsKTtcbiAgfVxuXG4gIHByaXZhdGUgX3VwZGF0ZUNlbGxGb3JUb29sYmFyT3ZlcmxhcChhY3RpdmVDZWxsOiBDZWxsPElDZWxsTW9kZWw+KSB7XG4gICAgLy8gUmVtb3ZlIHRoZSBcInRvb2xiYXIgb3ZlcmxhcFwiIGNsYXNzIGZyb20gdGhlIGNlbGwsIHJlbmRlcmluZyB0aGUgY2VsbCdzIHRvb2xiYXJcbiAgICBjb25zdCBhY3RpdmVDZWxsRWxlbWVudCA9IGFjdGl2ZUNlbGwubm9kZTtcbiAgICBhY3RpdmVDZWxsRWxlbWVudC5jbGFzc0xpc3QucmVtb3ZlKFRPT0xCQVJfT1ZFUkxBUF9DTEFTUyk7XG5cbiAgICBpZiAodGhpcy5fY2VsbFRvb2xiYXJPdmVybGFwc0NvbnRlbnRzKGFjdGl2ZUNlbGwpKSB7XG4gICAgICAvLyBBZGQgdGhlIFwidG9vbGJhciBvdmVybGFwXCIgY2xhc3MgdG8gdGhlIGNlbGwsIGNvbXBsZXRlbHkgY29uY2VhbGluZyB0aGUgdG9vbGJhcixcbiAgICAgIC8vIGlmIHRoZSBmaXJzdCBsaW5lIG9mIHRoZSBjb250ZW50IG92ZXJsYXBzIHdpdGggaXQgYXQgYWxsXG4gICAgICBhY3RpdmVDZWxsRWxlbWVudC5jbGFzc0xpc3QuYWRkKFRPT0xCQVJfT1ZFUkxBUF9DTEFTUyk7XG4gICAgfVxuICB9XG5cbiAgcHJpdmF0ZSBfY2VsbFRvb2xiYXJPdmVybGFwc0NvbnRlbnRzKGFjdGl2ZUNlbGw6IENlbGw8SUNlbGxNb2RlbD4pOiBib29sZWFuIHtcbiAgICBjb25zdCBjZWxsVHlwZSA9IGFjdGl2ZUNlbGwubW9kZWwudHlwZTtcblxuICAgIC8vIElmIHRoZSB0b29sYmFyIGlzIHRvbyBsYXJnZSBmb3IgdGhlIGN1cnJlbnQgY2VsbCwgaGlkZSBpdC5cbiAgICBjb25zdCBjZWxsTGVmdCA9IHRoaXMuX2NlbGxFZGl0b3JXaWRnZXRMZWZ0KGFjdGl2ZUNlbGwpO1xuICAgIGNvbnN0IGNlbGxSaWdodCA9IHRoaXMuX2NlbGxFZGl0b3JXaWRnZXRSaWdodChhY3RpdmVDZWxsKTtcbiAgICBjb25zdCB0b29sYmFyTGVmdCA9IHRoaXMuX2NlbGxUb29sYmFyTGVmdChhY3RpdmVDZWxsKTtcblxuICAgIGlmICh0b29sYmFyTGVmdCA9PT0gbnVsbCkge1xuICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH1cblxuICAgIC8vIFRoZSB0b29sYmFyIHNob3VsZCBub3QgdGFrZSB1cCBtb3JlIHRoYW4gNTAlIG9mIHRoZSBjZWxsLlxuICAgIGlmICgoY2VsbExlZnQgKyBjZWxsUmlnaHQpIC8gMiA+IHRvb2xiYXJMZWZ0KSB7XG4gICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9XG5cbiAgICBpZiAoY2VsbFR5cGUgPT09ICdtYXJrZG93bicgJiYgKGFjdGl2ZUNlbGwgYXMgTWFya2Rvd25DZWxsKS5yZW5kZXJlZCkge1xuICAgICAgLy8gQ2hlY2sgZm9yIG92ZXJsYXAgaW4gcmVuZGVyZWQgbWFya2Rvd24gY29udGVudFxuICAgICAgcmV0dXJuIHRoaXMuX21hcmtkb3duT3ZlcmxhcHNUb29sYmFyKGFjdGl2ZUNlbGwgYXMgTWFya2Rvd25DZWxsKTtcbiAgICB9XG5cbiAgICAvLyBDaGVjayBmb3Igb3ZlcmxhcCBpbiBjb2RlIGNvbnRlbnRcbiAgICBpZiAodGhpcy5fcGFuZWw/LmNvbnRlbnQucmVuZGVyaW5nTGF5b3V0ID09PSAnZGVmYXVsdCcpIHtcbiAgICAgIHJldHVybiB0aGlzLl9jb2RlT3ZlcmxhcHNUb29sYmFyKGFjdGl2ZUNlbGwpO1xuICAgIH0gZWxzZSB7XG4gICAgICByZXR1cm4gdGhpcy5fb3V0cHV0T3ZlcmxhcHNUb29sYmFyKGFjdGl2ZUNlbGwpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBDaGVjayBmb3Igb3ZlcmxhcCBiZXR3ZWVuIHJlbmRlcmVkIE1hcmtkb3duIGFuZCB0aGUgY2VsbCB0b29sYmFyXG4gICAqXG4gICAqIEBwYXJhbSBhY3RpdmVDZWxsIEEgcmVuZGVyZWQgTWFya2Rvd25DZWxsXG4gICAqIEByZXR1cm5zIGB0cnVlYCBpZiB0aGUgZmlyc3QgbGluZSBvZiB0aGUgb3V0cHV0IG92ZXJsYXBzIHdpdGggdGhlIGNlbGwgdG9vbGJhciwgYGZhbHNlYCBvdGhlcndpc2VcbiAgICovXG4gIHByaXZhdGUgX21hcmtkb3duT3ZlcmxhcHNUb29sYmFyKGFjdGl2ZUNlbGw6IE1hcmtkb3duQ2VsbCk6IGJvb2xlYW4ge1xuICAgIGNvbnN0IG1hcmtkb3duT3V0cHV0ID0gYWN0aXZlQ2VsbC5pbnB1dEFyZWE7IC8vIFJlbmRlcmVkIG1hcmtkb3duIGFwcGVhcnMgaW4gdGhlIGlucHV0IGFyZWFcblxuICAgIC8vIEdldCB0aGUgcmVuZGVyZWQgbWFya2Rvd24gYXMgYSB3aWRnZXQuXG4gICAgY29uc3QgbWFya2Rvd25PdXRwdXRXaWRnZXQgPSBtYXJrZG93bk91dHB1dC5yZW5kZXJlZElucHV0O1xuICAgIGNvbnN0IG1hcmtkb3duT3V0cHV0RWxlbWVudCA9IG1hcmtkb3duT3V0cHV0V2lkZ2V0Lm5vZGU7XG5cbiAgICBjb25zdCBmaXJzdE91dHB1dEVsZW1lbnRDaGlsZCA9XG4gICAgICBtYXJrZG93bk91dHB1dEVsZW1lbnQuZmlyc3RFbGVtZW50Q2hpbGQgYXMgSFRNTEVsZW1lbnQ7XG4gICAgaWYgKGZpcnN0T3V0cHV0RWxlbWVudENoaWxkID09PSBudWxsKSB7XG4gICAgICByZXR1cm4gZmFsc2U7XG4gICAgfVxuXG4gICAgLy8gVGVtcG9yYXJpbHkgc2V0IHRoZSBlbGVtZW50J3MgbWF4IHdpZHRoIHNvIHRoYXQgdGhlIGJvdW5kaW5nIGNsaWVudCByZWN0YW5nbGUgb25seSBlbmNvbXBhc3NlcyB0aGUgY29udGVudC5cbiAgICBjb25zdCBvbGRNYXhXaWR0aCA9IGZpcnN0T3V0cHV0RWxlbWVudENoaWxkLnN0eWxlLm1heFdpZHRoO1xuICAgIGZpcnN0T3V0cHV0RWxlbWVudENoaWxkLnN0eWxlLm1heFdpZHRoID0gJ21heC1jb250ZW50JztcblxuICAgIGNvbnN0IGxpbmVSaWdodCA9IGZpcnN0T3V0cHV0RWxlbWVudENoaWxkLmdldEJvdW5kaW5nQ2xpZW50UmVjdCgpLnJpZ2h0O1xuXG4gICAgLy8gUmVpbnN0YXRlIHRoZSBvbGQgbWF4IHdpZHRoLlxuICAgIGZpcnN0T3V0cHV0RWxlbWVudENoaWxkLnN0eWxlLm1heFdpZHRoID0gb2xkTWF4V2lkdGg7XG5cbiAgICBjb25zdCB0b29sYmFyTGVmdCA9IHRoaXMuX2NlbGxUb29sYmFyTGVmdChhY3RpdmVDZWxsKTtcblxuICAgIHJldHVybiB0b29sYmFyTGVmdCA9PT0gbnVsbCA/IGZhbHNlIDogbGluZVJpZ2h0ID4gdG9vbGJhckxlZnQ7XG4gIH1cblxuICBwcml2YXRlIF9vdXRwdXRPdmVybGFwc1Rvb2xiYXIoYWN0aXZlQ2VsbDogQ2VsbDxJQ2VsbE1vZGVsPik6IGJvb2xlYW4ge1xuICAgIGNvbnN0IG91dHB1dEFyZWEgPSAoYWN0aXZlQ2VsbCBhcyBDb2RlQ2VsbCkub3V0cHV0QXJlYS5ub2RlO1xuICAgIGlmIChvdXRwdXRBcmVhKSB7XG4gICAgICBjb25zdCBvdXRwdXRzID0gb3V0cHV0QXJlYS5xdWVyeVNlbGVjdG9yQWxsKCdbZGF0YS1taW1lLXR5cGVdJyk7XG4gICAgICBjb25zdCB0b29sYmFyUmVjdCA9IHRoaXMuX2NlbGxUb29sYmFyUmVjdChhY3RpdmVDZWxsKTtcbiAgICAgIGlmICh0b29sYmFyUmVjdCkge1xuICAgICAgICBjb25zdCB7IGxlZnQ6IHRvb2xiYXJMZWZ0LCBib3R0b206IHRvb2xiYXJCb3R0b20gfSA9IHRvb2xiYXJSZWN0O1xuICAgICAgICByZXR1cm4gQXJyYXkuZnJvbShvdXRwdXRzKS5zb21lKG91dHB1dCA9PiB7XG4gICAgICAgICAgY29uc3Qgbm9kZSA9IG91dHB1dC5maXJzdEVsZW1lbnRDaGlsZDtcbiAgICAgICAgICBpZiAobm9kZSkge1xuICAgICAgICAgICAgY29uc3QgcmFuZ2UgPSBuZXcgUmFuZ2UoKTtcbiAgICAgICAgICAgIGlmIChcbiAgICAgICAgICAgICAgVEVYVF9NSU1FX1RZUEVTLmluY2x1ZGVzKFxuICAgICAgICAgICAgICAgIG91dHB1dC5nZXRBdHRyaWJ1dGUoJ2RhdGEtbWltZS10eXBlJykgfHwgJydcbiAgICAgICAgICAgICAgKVxuICAgICAgICAgICAgKSB7XG4gICAgICAgICAgICAgIC8vIElmIHRoZSBub2RlIGlzIHBsYWluIHRleHQsIGl0J3MgaW4gYSA8cHJlPi4gVG8gZ2V0IHRoZSB0cnVlIGJvdW5kaW5nIGJveCBvZiB0aGVcbiAgICAgICAgICAgICAgLy8gdGV4dCwgdGhlIG5vZGUgY29udGVudHMgbmVlZCB0byBiZSBzZWxlY3RlZC5cbiAgICAgICAgICAgICAgcmFuZ2Uuc2VsZWN0Tm9kZUNvbnRlbnRzKG5vZGUpO1xuICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgcmFuZ2Uuc2VsZWN0Tm9kZShub2RlKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIGNvbnN0IHsgcmlnaHQ6IG5vZGVSaWdodCwgdG9wOiBub2RlVG9wIH0gPVxuICAgICAgICAgICAgICByYW5nZS5nZXRCb3VuZGluZ0NsaWVudFJlY3QoKTtcblxuICAgICAgICAgICAgLy8gTm90ZTogeS1jb29yZGluYXRlIGluY3JlYXNlcyB0b3dhcmQgdGhlIGJvdHRvbSBvZiBwYWdlXG4gICAgICAgICAgICByZXR1cm4gbm9kZVJpZ2h0ID4gdG9vbGJhckxlZnQgJiYgbm9kZVRvcCA8IHRvb2xiYXJCb3R0b207XG4gICAgICAgICAgfVxuICAgICAgICAgIHJldHVybiBmYWxzZTtcbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfVxuICAgIHJldHVybiBmYWxzZTtcbiAgfVxuXG4gIHByaXZhdGUgX2NvZGVPdmVybGFwc1Rvb2xiYXIoYWN0aXZlQ2VsbDogQ2VsbDxJQ2VsbE1vZGVsPik6IGJvb2xlYW4ge1xuICAgIGNvbnN0IGVkaXRvcldpZGdldCA9IGFjdGl2ZUNlbGwuZWRpdG9yV2lkZ2V0O1xuICAgIGNvbnN0IGVkaXRvciA9IGFjdGl2ZUNlbGwuZWRpdG9yO1xuICAgIGlmIChlZGl0b3IubGluZUNvdW50IDwgMSkge1xuICAgICAgcmV0dXJuIGZhbHNlOyAvLyBOb3RoaW5nIGluIHRoZSBlZGl0b3JcbiAgICB9XG5cbiAgICBjb25zdCBjb2RlTWlycm9yTGluZXMgPVxuICAgICAgZWRpdG9yV2lkZ2V0Lm5vZGUuZ2V0RWxlbWVudHNCeUNsYXNzTmFtZSgnQ29kZU1pcnJvci1saW5lJyk7XG4gICAgaWYgKGNvZGVNaXJyb3JMaW5lcy5sZW5ndGggPCAxKSB7XG4gICAgICByZXR1cm4gZmFsc2U7IC8vIE5vIGxpbmVzIHByZXNlbnRcbiAgICB9XG4gICAgY29uc3QgbGluZVJpZ2h0ID0gY29kZU1pcnJvckxpbmVzWzBdLmNoaWxkcmVuWzBdIC8vIEZpcnN0IHNwYW4gdW5kZXIgZmlyc3QgcHJlXG4gICAgICAuZ2V0Qm91bmRpbmdDbGllbnRSZWN0KCkucmlnaHQ7XG5cbiAgICBjb25zdCB0b29sYmFyTGVmdCA9IHRoaXMuX2NlbGxUb29sYmFyTGVmdChhY3RpdmVDZWxsKTtcblxuICAgIHJldHVybiB0b29sYmFyTGVmdCA9PT0gbnVsbCA/IGZhbHNlIDogbGluZVJpZ2h0ID4gdG9vbGJhckxlZnQ7XG4gIH1cblxuICBwcml2YXRlIF9jZWxsRWRpdG9yV2lkZ2V0TGVmdChhY3RpdmVDZWxsOiBDZWxsPElDZWxsTW9kZWw+KTogbnVtYmVyIHtcbiAgICByZXR1cm4gYWN0aXZlQ2VsbC5lZGl0b3JXaWRnZXQubm9kZS5nZXRCb3VuZGluZ0NsaWVudFJlY3QoKS5sZWZ0O1xuICB9XG5cbiAgcHJpdmF0ZSBfY2VsbEVkaXRvcldpZGdldFJpZ2h0KGFjdGl2ZUNlbGw6IENlbGw8SUNlbGxNb2RlbD4pOiBudW1iZXIge1xuICAgIHJldHVybiBhY3RpdmVDZWxsLmVkaXRvcldpZGdldC5ub2RlLmdldEJvdW5kaW5nQ2xpZW50UmVjdCgpLnJpZ2h0O1xuICB9XG5cbiAgcHJpdmF0ZSBfY2VsbFRvb2xiYXJSZWN0KGFjdGl2ZUNlbGw6IENlbGw8SUNlbGxNb2RlbD4pOiBET01SZWN0IHwgbnVsbCB7XG4gICAgY29uc3QgdG9vbGJhcldpZGdldHMgPSB0aGlzLl9maW5kVG9vbGJhcldpZGdldHMoYWN0aXZlQ2VsbCk7XG4gICAgaWYgKHRvb2xiYXJXaWRnZXRzLmxlbmd0aCA8IDEpIHtcbiAgICAgIHJldHVybiBudWxsO1xuICAgIH1cbiAgICBjb25zdCBhY3RpdmVDZWxsVG9vbGJhciA9IHRvb2xiYXJXaWRnZXRzWzBdLm5vZGU7XG5cbiAgICByZXR1cm4gYWN0aXZlQ2VsbFRvb2xiYXIuZ2V0Qm91bmRpbmdDbGllbnRSZWN0KCk7XG4gIH1cblxuICBwcml2YXRlIF9jZWxsVG9vbGJhckxlZnQoYWN0aXZlQ2VsbDogQ2VsbDxJQ2VsbE1vZGVsPik6IG51bWJlciB8IG51bGwge1xuICAgIHJldHVybiB0aGlzLl9jZWxsVG9vbGJhclJlY3QoYWN0aXZlQ2VsbCk/LmxlZnQgfHwgbnVsbDtcbiAgfVxuXG4gIHByaXZhdGUgX2lzRGlzcG9zZWQgPSBmYWxzZTtcbiAgcHJpdmF0ZSBfcGFuZWw6IE5vdGVib29rUGFuZWwgfCBudWxsO1xuICBwcml2YXRlIF9wcmV2aW91c0FjdGl2ZUNlbGw6IENlbGw8SUNlbGxNb2RlbD4gfCBudWxsO1xuICBwcml2YXRlIF90b29sYmFyOiBJT2JzZXJ2YWJsZUxpc3Q8VG9vbGJhclJlZ2lzdHJ5LklUb29sYmFySXRlbT47XG59XG5cbmNvbnN0IGRlZmF1bHRUb29sYmFySXRlbXM6IFRvb2xiYXJSZWdpc3RyeS5JV2lkZ2V0W10gPSBbXG4gIHtcbiAgICBjb21tYW5kOiAnbm90ZWJvb2s6cnVuLWNlbGwnLFxuICAgIG5hbWU6ICdydW4tY2VsbCdcbiAgfSxcbiAge1xuICAgIGNvbW1hbmQ6ICdub3RlYm9vazpkdXBsaWNhdGUtYmVsb3cnLFxuICAgIG5hbWU6ICdkdXBsaWNhdGUtY2VsbCdcbiAgfSxcbiAge1xuICAgIGNvbW1hbmQ6ICdub3RlYm9vazppbnNlcnQtY2VsbC1hYm92ZScsXG4gICAgbmFtZTogJ2luc2VydC1jZWxsLWFib3ZlJ1xuICB9LFxuICB7XG4gICAgY29tbWFuZDogJ25vdGVib29rOmluc2VydC1jZWxsLWJlbG93JyxcbiAgICBuYW1lOiAnaW5zZXJ0LWNlbGwtYmVsb3cnXG4gIH0sXG4gIHtcbiAgICBjb21tYW5kOiAnbm90ZWJvb2s6ZGVsZXRlLWNlbGwnLFxuICAgIG5hbWU6ICdkZWxldGUtY2VsbCdcbiAgfVxuXTtcblxuLyoqXG4gKiBXaWRnZXQgZXh0ZW5zaW9uIHRoYXQgY3JlYXRlcyBhIENlbGxUb29sYmFyVHJhY2tlciBlYWNoIHRpbWUgYSBub3RlYm9vayBpc1xuICogY3JlYXRlZC5cbiAqL1xuZXhwb3J0IGNsYXNzIENlbGxCYXJFeHRlbnNpb24gaW1wbGVtZW50cyBEb2N1bWVudFJlZ2lzdHJ5LldpZGdldEV4dGVuc2lvbiB7XG4gIHN0YXRpYyBGQUNUT1JZX05BTUUgPSAnQ2VsbCc7XG5cbiAgY29uc3RydWN0b3IoXG4gICAgY29tbWFuZHM6IENvbW1hbmRSZWdpc3RyeSxcbiAgICB0b29sYmFyRmFjdG9yeT86IChcbiAgICAgIHdpZGdldDogV2lkZ2V0XG4gICAgKSA9PiBJT2JzZXJ2YWJsZUxpc3Q8VG9vbGJhclJlZ2lzdHJ5LklUb29sYmFySXRlbT5cbiAgKSB7XG4gICAgdGhpcy5fY29tbWFuZHMgPSBjb21tYW5kcztcbiAgICB0aGlzLl90b29sYmFyRmFjdG9yeSA9IHRvb2xiYXJGYWN0b3J5ID8/IHRoaXMuZGVmYXVsdFRvb2xiYXJGYWN0b3J5O1xuICB9XG5cbiAgcHJvdGVjdGVkIGdldCBkZWZhdWx0VG9vbGJhckZhY3RvcnkoKTogKFxuICAgIHdpZGdldDogV2lkZ2V0XG4gICkgPT4gSU9ic2VydmFibGVMaXN0PFRvb2xiYXJSZWdpc3RyeS5JVG9vbGJhckl0ZW0+IHtcbiAgICBjb25zdCBpdGVtRmFjdG9yeSA9IGNyZWF0ZURlZmF1bHRGYWN0b3J5KHRoaXMuX2NvbW1hbmRzKTtcbiAgICByZXR1cm4gKHdpZGdldDogV2lkZ2V0KSA9PlxuICAgICAgbmV3IE9ic2VydmFibGVMaXN0KHtcbiAgICAgICAgdmFsdWVzOiBkZWZhdWx0VG9vbGJhckl0ZW1zLm1hcChpdGVtID0+IHtcbiAgICAgICAgICByZXR1cm4ge1xuICAgICAgICAgICAgbmFtZTogaXRlbS5uYW1lLFxuICAgICAgICAgICAgd2lkZ2V0OiBpdGVtRmFjdG9yeShDZWxsQmFyRXh0ZW5zaW9uLkZBQ1RPUllfTkFNRSwgd2lkZ2V0LCBpdGVtKVxuICAgICAgICAgIH07XG4gICAgICAgIH0pXG4gICAgICB9KTtcbiAgfVxuXG4gIGNyZWF0ZU5ldyhwYW5lbDogTm90ZWJvb2tQYW5lbCk6IElEaXNwb3NhYmxlIHtcbiAgICByZXR1cm4gbmV3IENlbGxUb29sYmFyVHJhY2tlcihwYW5lbCwgdGhpcy5fdG9vbGJhckZhY3RvcnkocGFuZWwpKTtcbiAgfVxuXG4gIHByaXZhdGUgX2NvbW1hbmRzOiBDb21tYW5kUmVnaXN0cnk7XG4gIHByaXZhdGUgX3Rvb2xiYXJGYWN0b3J5OiAoXG4gICAgd2lkZ2V0OiBXaWRnZXRcbiAgKSA9PiBJT2JzZXJ2YWJsZUxpc3Q8VG9vbGJhclJlZ2lzdHJ5LklUb29sYmFySXRlbT47XG59XG4iLCIvKiAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxufCBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbnwgRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbnwtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGNlbGwtdG9vbGJhclxuICovXG5leHBvcnQgKiBmcm9tICcuL2NlbGx0b29sYmFydHJhY2tlcic7XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=