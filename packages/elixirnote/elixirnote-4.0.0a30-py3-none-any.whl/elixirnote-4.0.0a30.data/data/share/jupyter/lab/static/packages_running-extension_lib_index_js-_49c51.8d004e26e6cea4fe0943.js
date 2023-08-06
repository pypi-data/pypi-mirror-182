"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_running-extension_lib_index_js-_49c51"],{

/***/ "../../packages/running-extension/lib/index.js":
/*!*****************************************************!*\
  !*** ../../packages/running-extension/lib/index.js ***!
  \*****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_running__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/running */ "webpack/sharing/consume/default/@jupyterlab/running/@jupyterlab/running");
/* harmony import */ var _jupyterlab_running__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_running__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _kernels__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./kernels */ "../../packages/running-extension/lib/kernels.js");
/* harmony import */ var _opentabs__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./opentabs */ "../../packages/running-extension/lib/opentabs.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module running-extension
 */






/**
 * The command IDs used by the running plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.showPanel = 'running:show-panel';
})(CommandIDs || (CommandIDs = {}));
/**
 * The default running sessions extension.
 */
const plugin = {
    activate,
    id: '@jupyterlab/running-extension:plugin',
    provides: _jupyterlab_running__WEBPACK_IMPORTED_MODULE_1__.IRunningSessionManagers,
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.ITranslator],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell],
    autoStart: true
};
/**
 * Export the plugin as default.
 */
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);
/**
 * Activate the running plugin.
 */
function activate(app, translator, restorer, labShell) {
    const trans = translator.load('jupyterlab');
    const runningSessionManagers = new _jupyterlab_running__WEBPACK_IMPORTED_MODULE_1__.RunningSessionManagers();
    const running = new _jupyterlab_running__WEBPACK_IMPORTED_MODULE_1__.RunningSessions(runningSessionManagers, translator);
    running.id = 'jp-running-sessions';
    running.title.caption = trans.__('Running Terminals and Kernels');
    running.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.runningIcon;
    running.node.setAttribute('role', 'region');
    running.node.setAttribute('aria-label', trans.__('Running Sessions section'));
    // Let the application restorer track the running panel for restoration of
    // application state (e.g. setting the running panel as the current side bar
    // widget).
    if (restorer) {
        restorer.add(running, 'running-sessions');
    }
    if (labShell) {
        (0,_opentabs__WEBPACK_IMPORTED_MODULE_4__.addOpenTabsSessionManager)(runningSessionManagers, translator, labShell);
    }
    (0,_kernels__WEBPACK_IMPORTED_MODULE_5__.addKernelRunningSessionManager)(runningSessionManagers, translator, app);
    // Rank has been chosen somewhat arbitrarily to give priority to the running
    // sessions widget in the sidebar.
    app.shell.add(running, 'left', { rank: 200, type: 'Sessions and Tabs' });
    app.commands.addCommand(CommandIDs.showPanel, {
        label: trans.__('Sessions and Tabs'),
        execute: () => {
            app.shell.activateById(running.id);
        }
    });
    return runningSessionManagers;
}


/***/ }),

/***/ "../../packages/running-extension/lib/kernels.js":
/*!*******************************************************!*\
  !*** ../../packages/running-extension/lib/kernels.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "addKernelRunningSessionManager": () => (/* binding */ addKernelRunningSessionManager)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/**
 * Add the running kernel manager (notebooks & consoles) to the running panel.
 */
function addKernelRunningSessionManager(managers, translator, app) {
    const trans = translator.load('jupyterlab');
    const manager = app.serviceManager.sessions;
    const specsManager = app.serviceManager.kernelspecs;
    function filterSessions(m) {
        return !!((m.name || _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.PathExt.basename(m.path)).indexOf('.') !== -1 || m.name);
    }
    managers.add({
        name: trans.__('Kernels'),
        running: () => {
            return (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__.toArray)(manager.running())
                .filter(filterSessions)
                .map(model => new RunningKernel(model));
        },
        shutdownAll: () => manager.shutdownAll(),
        refreshRunning: () => manager.refreshRunning(),
        runningChanged: manager.runningChanged,
        shutdownLabel: trans.__('Shut Down'),
        shutdownAllLabel: trans.__('Shut Down All'),
        shutdownAllConfirmationText: trans.__('Are you sure you want to permanently shut down all running kernels?')
    });
    class RunningKernel {
        constructor(model) {
            this._model = model;
        }
        open() {
            const { path, type } = this._model;
            if (type.toLowerCase() === 'console') {
                void app.commands.execute('console:open', { path });
            }
            else {
                void app.commands.execute('docmanager:open', { path });
            }
        }
        shutdown() {
            return manager.shutdown(this._model.id);
        }
        icon() {
            const { name, path, type } = this._model;
            if ((name || _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.PathExt.basename(path)).indexOf('.ipynb') !== -1) {
                return _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.notebookIcon;
            }
            else if (type.toLowerCase() === 'console') {
                return _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.consoleIcon;
            }
            return _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.fileIcon;
        }
        label() {
            return this._model.name || _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.PathExt.basename(this._model.path);
        }
        labelTitle() {
            const { kernel, path } = this._model;
            let kernelName = kernel === null || kernel === void 0 ? void 0 : kernel.name;
            if (kernelName && specsManager.specs) {
                const spec = specsManager.specs.kernelspecs[kernelName];
                kernelName = spec ? spec.display_name : 'unknown';
            }
            return trans.__('Path: %1\nKernel: %2', path, kernelName);
        }
    }
}


/***/ }),

/***/ "../../packages/running-extension/lib/opentabs.js":
/*!********************************************************!*\
  !*** ../../packages/running-extension/lib/opentabs.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "addOpenTabsSessionManager": () => (/* binding */ addOpenTabsSessionManager)
/* harmony export */ });
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/docregistry */ "webpack/sharing/consume/default/@jupyterlab/docregistry/@jupyterlab/docregistry");
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_3__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




/**
 * A class used to consolidate the signals used to rerender the open tabs section.
 */
class OpenTabsSignaler {
    constructor(labShell) {
        this._tabsChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal(this);
        this._widgets = [];
        this._labShell = labShell;
        this._labShell.layoutModified.connect(this._emitTabsChanged, this);
    }
    /**
     * A signal that fires when the open tabs section should be rerendered.
     */
    get tabsChanged() {
        return this._tabsChanged;
    }
    /**
     * Add a widget to watch for title changing.
     *
     * @param widget A widget whose title may change.
     */
    addWidget(widget) {
        widget.title.changed.connect(this._emitTabsChanged, this);
        this._widgets.push(widget);
    }
    /**
     * Emit the main signal that indicates the open tabs should be rerendered.
     */
    _emitTabsChanged() {
        this._widgets.forEach(widget => {
            widget.title.changed.disconnect(this._emitTabsChanged, this);
        });
        this._widgets = [];
        this._tabsChanged.emit(void 0);
    }
}
/**
 * Add the open tabs section to the running panel.
 *
 * @param managers - The IRunningSessionManagers used to register this section.
 * @param translator - The translator to use.
 * @param labShell - The ILabShell.
 */
function addOpenTabsSessionManager(managers, translator, labShell) {
    const signaler = new OpenTabsSignaler(labShell);
    const trans = translator.load('jupyterlab');
    managers.add({
        name: trans.__('Open Tabs'),
        running: () => {
            return (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__.toArray)(labShell.widgets('main')).map((widget) => {
                signaler.addWidget(widget);
                return new OpenTab(widget);
            });
        },
        shutdownAll: () => {
            (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__.toArray)(labShell.widgets('main')).forEach((widget) => {
                widget.close();
            });
        },
        refreshRunning: () => {
            return void 0;
        },
        runningChanged: signaler.tabsChanged,
        shutdownLabel: trans.__('Close'),
        shutdownAllLabel: trans.__('Close All'),
        shutdownAllConfirmationText: trans.__('Are you sure you want to close all open tabs?')
    });
    class OpenTab {
        constructor(widget) {
            this._widget = widget;
        }
        open() {
            labShell.activateById(this._widget.id);
        }
        shutdown() {
            this._widget.close();
        }
        icon() {
            const widgetIcon = this._widget.title.icon;
            return widgetIcon instanceof _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.LabIcon ? widgetIcon : _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.fileIcon;
        }
        label() {
            return this._widget.title.label;
        }
        labelTitle() {
            let labelTitle;
            if (this._widget instanceof _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_0__.DocumentWidget) {
                labelTitle = this._widget.context.path;
            }
            else {
                labelTitle = this._widget.title.label;
            }
            return labelTitle;
        }
    }
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfcnVubmluZy1leHRlbnNpb25fbGliX2luZGV4X2pzLV80OWM1MS44ZDAwNGUyNmU2Y2VhNGZlMDk0My5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBTzhCO0FBS0o7QUFDeUI7QUFDRTtBQUNHO0FBQ0o7QUFFdkQ7O0dBRUc7QUFDSCxJQUFVLFVBQVUsQ0FFbkI7QUFGRCxXQUFVLFVBQVU7SUFDTCxvQkFBUyxHQUFHLG9CQUFvQixDQUFDO0FBQ2hELENBQUMsRUFGUyxVQUFVLEtBQVYsVUFBVSxRQUVuQjtBQUVEOztHQUVHO0FBQ0gsTUFBTSxNQUFNLEdBQW1EO0lBQzdELFFBQVE7SUFDUixFQUFFLEVBQUUsc0NBQXNDO0lBQzFDLFFBQVEsRUFBRSx3RUFBdUI7SUFDakMsUUFBUSxFQUFFLENBQUMsZ0VBQVcsQ0FBQztJQUN2QixRQUFRLEVBQUUsQ0FBQyxvRUFBZSxFQUFFLDhEQUFTLENBQUM7SUFDdEMsU0FBUyxFQUFFLElBQUk7Q0FDaEIsQ0FBQztBQUVGOztHQUVHO0FBQ0gsaUVBQWUsTUFBTSxFQUFDO0FBRXRCOztHQUVHO0FBQ0gsU0FBUyxRQUFRLENBQ2YsR0FBb0IsRUFDcEIsVUFBdUIsRUFDdkIsUUFBZ0MsRUFDaEMsUUFBMEI7SUFFMUIsTUFBTSxLQUFLLEdBQUcsVUFBVSxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUMsQ0FBQztJQUM1QyxNQUFNLHNCQUFzQixHQUFHLElBQUksdUVBQXNCLEVBQUUsQ0FBQztJQUM1RCxNQUFNLE9BQU8sR0FBRyxJQUFJLGdFQUFlLENBQUMsc0JBQXNCLEVBQUUsVUFBVSxDQUFDLENBQUM7SUFDeEUsT0FBTyxDQUFDLEVBQUUsR0FBRyxxQkFBcUIsQ0FBQztJQUNuQyxPQUFPLENBQUMsS0FBSyxDQUFDLE9BQU8sR0FBRyxLQUFLLENBQUMsRUFBRSxDQUFDLCtCQUErQixDQUFDLENBQUM7SUFDbEUsT0FBTyxDQUFDLEtBQUssQ0FBQyxJQUFJLEdBQUcsa0VBQVcsQ0FBQztJQUNqQyxPQUFPLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FBQyxNQUFNLEVBQUUsUUFBUSxDQUFDLENBQUM7SUFDNUMsT0FBTyxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUMsWUFBWSxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsMEJBQTBCLENBQUMsQ0FBQyxDQUFDO0lBRTlFLDBFQUEwRTtJQUMxRSw0RUFBNEU7SUFDNUUsV0FBVztJQUNYLElBQUksUUFBUSxFQUFFO1FBQ1osUUFBUSxDQUFDLEdBQUcsQ0FBQyxPQUFPLEVBQUUsa0JBQWtCLENBQUMsQ0FBQztLQUMzQztJQUNELElBQUksUUFBUSxFQUFFO1FBQ1osb0VBQXlCLENBQUMsc0JBQXNCLEVBQUUsVUFBVSxFQUFFLFFBQVEsQ0FBQyxDQUFDO0tBQ3pFO0lBQ0Qsd0VBQThCLENBQUMsc0JBQXNCLEVBQUUsVUFBVSxFQUFFLEdBQUcsQ0FBQyxDQUFDO0lBQ3hFLDRFQUE0RTtJQUM1RSxrQ0FBa0M7SUFDbEMsR0FBRyxDQUFDLEtBQUssQ0FBQyxHQUFHLENBQUMsT0FBTyxFQUFFLE1BQU0sRUFBRSxFQUFFLElBQUksRUFBRSxHQUFHLEVBQUUsSUFBSSxFQUFFLG1CQUFtQixFQUFFLENBQUMsQ0FBQztJQUV6RSxHQUFHLENBQUMsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsU0FBUyxFQUFFO1FBQzVDLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLG1CQUFtQixDQUFDO1FBQ3BDLE9BQU8sRUFBRSxHQUFHLEVBQUU7WUFDWixHQUFHLENBQUMsS0FBSyxDQUFDLFlBQVksQ0FBQyxPQUFPLENBQUMsRUFBRSxDQUFDLENBQUM7UUFDckMsQ0FBQztLQUNGLENBQUMsQ0FBQztJQUVILE9BQU8sc0JBQXNCLENBQUM7QUFDaEMsQ0FBQzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDdkZELDBDQUEwQztBQUMxQywyREFBMkQ7QUFHWDtBQUlnQztBQUNwQztBQUU1Qzs7R0FFRztBQUNJLFNBQVMsOEJBQThCLENBQzVDLFFBQWlDLEVBQ2pDLFVBQXVCLEVBQ3ZCLEdBQW9CO0lBRXBCLE1BQU0sS0FBSyxHQUFHLFVBQVUsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUM7SUFDNUMsTUFBTSxPQUFPLEdBQUcsR0FBRyxDQUFDLGNBQWMsQ0FBQyxRQUFRLENBQUM7SUFDNUMsTUFBTSxZQUFZLEdBQUcsR0FBRyxDQUFDLGNBQWMsQ0FBQyxXQUFXLENBQUM7SUFDcEQsU0FBUyxjQUFjLENBQUMsQ0FBaUI7UUFDdkMsT0FBTyxDQUFDLENBQUMsQ0FDUCxDQUFDLENBQUMsQ0FBQyxJQUFJLElBQUksbUVBQWdCLENBQUMsQ0FBQyxDQUFDLElBQUksQ0FBQyxDQUFDLENBQUMsT0FBTyxDQUFDLEdBQUcsQ0FBQyxLQUFLLENBQUMsQ0FBQyxJQUFJLENBQUMsQ0FBQyxJQUFJLENBQ25FLENBQUM7SUFDSixDQUFDO0lBRUQsUUFBUSxDQUFDLEdBQUcsQ0FBQztRQUNYLElBQUksRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLFNBQVMsQ0FBQztRQUN6QixPQUFPLEVBQUUsR0FBRyxFQUFFO1lBQ1osT0FBTywwREFBTyxDQUFDLE9BQU8sQ0FBQyxPQUFPLEVBQUUsQ0FBQztpQkFDOUIsTUFBTSxDQUFDLGNBQWMsQ0FBQztpQkFDdEIsR0FBRyxDQUFDLEtBQUssQ0FBQyxFQUFFLENBQUMsSUFBSSxhQUFhLENBQUMsS0FBSyxDQUFDLENBQUMsQ0FBQztRQUM1QyxDQUFDO1FBQ0QsV0FBVyxFQUFFLEdBQUcsRUFBRSxDQUFDLE9BQU8sQ0FBQyxXQUFXLEVBQUU7UUFDeEMsY0FBYyxFQUFFLEdBQUcsRUFBRSxDQUFDLE9BQU8sQ0FBQyxjQUFjLEVBQUU7UUFDOUMsY0FBYyxFQUFFLE9BQU8sQ0FBQyxjQUFjO1FBQ3RDLGFBQWEsRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLFdBQVcsQ0FBQztRQUNwQyxnQkFBZ0IsRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLGVBQWUsQ0FBQztRQUMzQywyQkFBMkIsRUFBRSxLQUFLLENBQUMsRUFBRSxDQUNuQyxxRUFBcUUsQ0FDdEU7S0FDRixDQUFDLENBQUM7SUFFSCxNQUFNLGFBQWE7UUFDakIsWUFBWSxLQUFxQjtZQUMvQixJQUFJLENBQUMsTUFBTSxHQUFHLEtBQUssQ0FBQztRQUN0QixDQUFDO1FBQ0QsSUFBSTtZQUNGLE1BQU0sRUFBRSxJQUFJLEVBQUUsSUFBSSxFQUFFLEdBQUcsSUFBSSxDQUFDLE1BQU0sQ0FBQztZQUNuQyxJQUFJLElBQUksQ0FBQyxXQUFXLEVBQUUsS0FBSyxTQUFTLEVBQUU7Z0JBQ3BDLEtBQUssR0FBRyxDQUFDLFFBQVEsQ0FBQyxPQUFPLENBQUMsY0FBYyxFQUFFLEVBQUUsSUFBSSxFQUFFLENBQUMsQ0FBQzthQUNyRDtpQkFBTTtnQkFDTCxLQUFLLEdBQUcsQ0FBQyxRQUFRLENBQUMsT0FBTyxDQUFDLGlCQUFpQixFQUFFLEVBQUUsSUFBSSxFQUFFLENBQUMsQ0FBQzthQUN4RDtRQUNILENBQUM7UUFDRCxRQUFRO1lBQ04sT0FBTyxPQUFPLENBQUMsUUFBUSxDQUFDLElBQUksQ0FBQyxNQUFNLENBQUMsRUFBRSxDQUFDLENBQUM7UUFDMUMsQ0FBQztRQUNELElBQUk7WUFDRixNQUFNLEVBQUUsSUFBSSxFQUFFLElBQUksRUFBRSxJQUFJLEVBQUUsR0FBRyxJQUFJLENBQUMsTUFBTSxDQUFDO1lBQ3pDLElBQUksQ0FBQyxJQUFJLElBQUksbUVBQWdCLENBQUMsSUFBSSxDQUFDLENBQUMsQ0FBQyxPQUFPLENBQUMsUUFBUSxDQUFDLEtBQUssQ0FBQyxDQUFDLEVBQUU7Z0JBQzdELE9BQU8sbUVBQVksQ0FBQzthQUNyQjtpQkFBTSxJQUFJLElBQUksQ0FBQyxXQUFXLEVBQUUsS0FBSyxTQUFTLEVBQUU7Z0JBQzNDLE9BQU8sa0VBQVcsQ0FBQzthQUNwQjtZQUNELE9BQU8sK0RBQVEsQ0FBQztRQUNsQixDQUFDO1FBQ0QsS0FBSztZQUNILE9BQU8sSUFBSSxDQUFDLE1BQU0sQ0FBQyxJQUFJLElBQUksbUVBQWdCLENBQUMsSUFBSSxDQUFDLE1BQU0sQ0FBQyxJQUFJLENBQUMsQ0FBQztRQUNoRSxDQUFDO1FBQ0QsVUFBVTtZQUNSLE1BQU0sRUFBRSxNQUFNLEVBQUUsSUFBSSxFQUFFLEdBQUcsSUFBSSxDQUFDLE1BQU0sQ0FBQztZQUNyQyxJQUFJLFVBQVUsR0FBRyxNQUFNLGFBQU4sTUFBTSx1QkFBTixNQUFNLENBQUUsSUFBSSxDQUFDO1lBQzlCLElBQUksVUFBVSxJQUFJLFlBQVksQ0FBQyxLQUFLLEVBQUU7Z0JBQ3BDLE1BQU0sSUFBSSxHQUFHLFlBQVksQ0FBQyxLQUFLLENBQUMsV0FBVyxDQUFDLFVBQVUsQ0FBQyxDQUFDO2dCQUN4RCxVQUFVLEdBQUcsSUFBSSxDQUFDLENBQUMsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUMsQ0FBQyxTQUFTLENBQUM7YUFDbkQ7WUFDRCxPQUFPLEtBQUssQ0FBQyxFQUFFLENBQUMsc0JBQXNCLEVBQUUsSUFBSSxFQUFFLFVBQVUsQ0FBQyxDQUFDO1FBQzVELENBQUM7S0FHRjtBQUNILENBQUM7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDcEZELDBDQUEwQztBQUMxQywyREFBMkQ7QUFHRjtBQUdLO0FBQ2xCO0FBQ1E7QUFHcEQ7O0dBRUc7QUFDSCxNQUFNLGdCQUFnQjtJQUNwQixZQUFZLFFBQW1CO1FBaUN2QixpQkFBWSxHQUFHLElBQUkscURBQU0sQ0FBYSxJQUFJLENBQUMsQ0FBQztRQUU1QyxhQUFRLEdBQWEsRUFBRSxDQUFDO1FBbEM5QixJQUFJLENBQUMsU0FBUyxHQUFHLFFBQVEsQ0FBQztRQUMxQixJQUFJLENBQUMsU0FBUyxDQUFDLGNBQWMsQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLGdCQUFnQixFQUFFLElBQUksQ0FBQyxDQUFDO0lBQ3JFLENBQUM7SUFFRDs7T0FFRztJQUNILElBQUksV0FBVztRQUNiLE9BQU8sSUFBSSxDQUFDLFlBQVksQ0FBQztJQUMzQixDQUFDO0lBRUQ7Ozs7T0FJRztJQUNILFNBQVMsQ0FBQyxNQUFjO1FBQ3RCLE1BQU0sQ0FBQyxLQUFLLENBQUMsT0FBTyxDQUFDLE9BQU8sQ0FBQyxJQUFJLENBQUMsZ0JBQWdCLEVBQUUsSUFBSSxDQUFDLENBQUM7UUFDMUQsSUFBSSxDQUFDLFFBQVEsQ0FBQyxJQUFJLENBQUMsTUFBTSxDQUFDLENBQUM7SUFDN0IsQ0FBQztJQUVEOztPQUVHO0lBQ0ssZ0JBQWdCO1FBQ3RCLElBQUksQ0FBQyxRQUFRLENBQUMsT0FBTyxDQUFDLE1BQU0sQ0FBQyxFQUFFO1lBQzdCLE1BQU0sQ0FBQyxLQUFLLENBQUMsT0FBTyxDQUFDLFVBQVUsQ0FBQyxJQUFJLENBQUMsZ0JBQWdCLEVBQUUsSUFBSSxDQUFDLENBQUM7UUFDL0QsQ0FBQyxDQUFDLENBQUM7UUFDSCxJQUFJLENBQUMsUUFBUSxHQUFHLEVBQUUsQ0FBQztRQUNuQixJQUFJLENBQUMsWUFBWSxDQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsQ0FBQyxDQUFDO0lBQ2pDLENBQUM7Q0FLRjtBQUVEOzs7Ozs7R0FNRztBQUNJLFNBQVMseUJBQXlCLENBQ3ZDLFFBQWlDLEVBQ2pDLFVBQXVCLEVBQ3ZCLFFBQW1CO0lBRW5CLE1BQU0sUUFBUSxHQUFHLElBQUksZ0JBQWdCLENBQUMsUUFBUSxDQUFDLENBQUM7SUFDaEQsTUFBTSxLQUFLLEdBQUcsVUFBVSxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUMsQ0FBQztJQUU1QyxRQUFRLENBQUMsR0FBRyxDQUFDO1FBQ1gsSUFBSSxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsV0FBVyxDQUFDO1FBQzNCLE9BQU8sRUFBRSxHQUFHLEVBQUU7WUFDWixPQUFPLDBEQUFPLENBQUMsUUFBUSxDQUFDLE9BQU8sQ0FBQyxNQUFNLENBQUMsQ0FBQyxDQUFDLEdBQUcsQ0FBQyxDQUFDLE1BQWMsRUFBRSxFQUFFO2dCQUM5RCxRQUFRLENBQUMsU0FBUyxDQUFDLE1BQU0sQ0FBQyxDQUFDO2dCQUMzQixPQUFPLElBQUksT0FBTyxDQUFDLE1BQU0sQ0FBQyxDQUFDO1lBQzdCLENBQUMsQ0FBQyxDQUFDO1FBQ0wsQ0FBQztRQUNELFdBQVcsRUFBRSxHQUFHLEVBQUU7WUFDaEIsMERBQU8sQ0FBQyxRQUFRLENBQUMsT0FBTyxDQUFDLE1BQU0sQ0FBQyxDQUFDLENBQUMsT0FBTyxDQUFDLENBQUMsTUFBYyxFQUFFLEVBQUU7Z0JBQzNELE1BQU0sQ0FBQyxLQUFLLEVBQUUsQ0FBQztZQUNqQixDQUFDLENBQUMsQ0FBQztRQUNMLENBQUM7UUFDRCxjQUFjLEVBQUUsR0FBRyxFQUFFO1lBQ25CLE9BQU8sS0FBSyxDQUFDLENBQUM7UUFDaEIsQ0FBQztRQUNELGNBQWMsRUFBRSxRQUFRLENBQUMsV0FBVztRQUNwQyxhQUFhLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxPQUFPLENBQUM7UUFDaEMsZ0JBQWdCLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxXQUFXLENBQUM7UUFDdkMsMkJBQTJCLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FDbkMsK0NBQStDLENBQ2hEO0tBQ0YsQ0FBQyxDQUFDO0lBRUgsTUFBTSxPQUFPO1FBQ1gsWUFBWSxNQUFjO1lBQ3hCLElBQUksQ0FBQyxPQUFPLEdBQUcsTUFBTSxDQUFDO1FBQ3hCLENBQUM7UUFDRCxJQUFJO1lBQ0YsUUFBUSxDQUFDLFlBQVksQ0FBQyxJQUFJLENBQUMsT0FBTyxDQUFDLEVBQUUsQ0FBQyxDQUFDO1FBQ3pDLENBQUM7UUFDRCxRQUFRO1lBQ04sSUFBSSxDQUFDLE9BQU8sQ0FBQyxLQUFLLEVBQUUsQ0FBQztRQUN2QixDQUFDO1FBQ0QsSUFBSTtZQUNGLE1BQU0sVUFBVSxHQUFHLElBQUksQ0FBQyxPQUFPLENBQUMsS0FBSyxDQUFDLElBQUksQ0FBQztZQUMzQyxPQUFPLFVBQVUsWUFBWSw4REFBTyxDQUFDLENBQUMsQ0FBQyxVQUFVLENBQUMsQ0FBQyxDQUFDLCtEQUFRLENBQUM7UUFDL0QsQ0FBQztRQUNELEtBQUs7WUFDSCxPQUFPLElBQUksQ0FBQyxPQUFPLENBQUMsS0FBSyxDQUFDLEtBQUssQ0FBQztRQUNsQyxDQUFDO1FBQ0QsVUFBVTtZQUNSLElBQUksVUFBa0IsQ0FBQztZQUN2QixJQUFJLElBQUksQ0FBQyxPQUFPLFlBQVksbUVBQWMsRUFBRTtnQkFDMUMsVUFBVSxHQUFHLElBQUksQ0FBQyxPQUFPLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQzthQUN4QztpQkFBTTtnQkFDTCxVQUFVLEdBQUcsSUFBSSxDQUFDLE9BQU8sQ0FBQyxLQUFLLENBQUMsS0FBSyxDQUFDO2FBQ3ZDO1lBQ0QsT0FBTyxVQUFVLENBQUM7UUFDcEIsQ0FBQztLQUdGO0FBQ0gsQ0FBQyIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9ydW5uaW5nLWV4dGVuc2lvbi9zcmMvaW5kZXgudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3J1bm5pbmctZXh0ZW5zaW9uL3NyYy9rZXJuZWxzLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9ydW5uaW5nLWV4dGVuc2lvbi9zcmMvb3BlbnRhYnMudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgcnVubmluZy1leHRlbnNpb25cbiAqL1xuXG5pbXBvcnQge1xuICBJTGFiU2hlbGwsXG4gIElMYXlvdXRSZXN0b3JlcixcbiAgSnVweXRlckZyb250RW5kLFxuICBKdXB5dGVyRnJvbnRFbmRQbHVnaW5cbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24nO1xuaW1wb3J0IHtcbiAgSVJ1bm5pbmdTZXNzaW9uTWFuYWdlcnMsXG4gIFJ1bm5pbmdTZXNzaW9uTWFuYWdlcnMsXG4gIFJ1bm5pbmdTZXNzaW9uc1xufSBmcm9tICdAanVweXRlcmxhYi9ydW5uaW5nJztcbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgcnVubmluZ0ljb24gfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IGFkZEtlcm5lbFJ1bm5pbmdTZXNzaW9uTWFuYWdlciB9IGZyb20gJy4va2VybmVscyc7XG5pbXBvcnQgeyBhZGRPcGVuVGFic1Nlc3Npb25NYW5hZ2VyIH0gZnJvbSAnLi9vcGVudGFicyc7XG5cbi8qKlxuICogVGhlIGNvbW1hbmQgSURzIHVzZWQgYnkgdGhlIHJ1bm5pbmcgcGx1Z2luLlxuICovXG5uYW1lc3BhY2UgQ29tbWFuZElEcyB7XG4gIGV4cG9ydCBjb25zdCBzaG93UGFuZWwgPSAncnVubmluZzpzaG93LXBhbmVsJztcbn1cblxuLyoqXG4gKiBUaGUgZGVmYXVsdCBydW5uaW5nIHNlc3Npb25zIGV4dGVuc2lvbi5cbiAqL1xuY29uc3QgcGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SVJ1bm5pbmdTZXNzaW9uTWFuYWdlcnM+ID0ge1xuICBhY3RpdmF0ZSxcbiAgaWQ6ICdAanVweXRlcmxhYi9ydW5uaW5nLWV4dGVuc2lvbjpwbHVnaW4nLFxuICBwcm92aWRlczogSVJ1bm5pbmdTZXNzaW9uTWFuYWdlcnMsXG4gIHJlcXVpcmVzOiBbSVRyYW5zbGF0b3JdLFxuICBvcHRpb25hbDogW0lMYXlvdXRSZXN0b3JlciwgSUxhYlNoZWxsXSxcbiAgYXV0b1N0YXJ0OiB0cnVlXG59O1xuXG4vKipcbiAqIEV4cG9ydCB0aGUgcGx1Z2luIGFzIGRlZmF1bHQuXG4gKi9cbmV4cG9ydCBkZWZhdWx0IHBsdWdpbjtcblxuLyoqXG4gKiBBY3RpdmF0ZSB0aGUgcnVubmluZyBwbHVnaW4uXG4gKi9cbmZ1bmN0aW9uIGFjdGl2YXRlKFxuICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gIHJlc3RvcmVyOiBJTGF5b3V0UmVzdG9yZXIgfCBudWxsLFxuICBsYWJTaGVsbDogSUxhYlNoZWxsIHwgbnVsbFxuKTogSVJ1bm5pbmdTZXNzaW9uTWFuYWdlcnMge1xuICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICBjb25zdCBydW5uaW5nU2Vzc2lvbk1hbmFnZXJzID0gbmV3IFJ1bm5pbmdTZXNzaW9uTWFuYWdlcnMoKTtcbiAgY29uc3QgcnVubmluZyA9IG5ldyBSdW5uaW5nU2Vzc2lvbnMocnVubmluZ1Nlc3Npb25NYW5hZ2VycywgdHJhbnNsYXRvcik7XG4gIHJ1bm5pbmcuaWQgPSAnanAtcnVubmluZy1zZXNzaW9ucyc7XG4gIHJ1bm5pbmcudGl0bGUuY2FwdGlvbiA9IHRyYW5zLl9fKCdSdW5uaW5nIFRlcm1pbmFscyBhbmQgS2VybmVscycpO1xuICBydW5uaW5nLnRpdGxlLmljb24gPSBydW5uaW5nSWNvbjtcbiAgcnVubmluZy5ub2RlLnNldEF0dHJpYnV0ZSgncm9sZScsICdyZWdpb24nKTtcbiAgcnVubmluZy5ub2RlLnNldEF0dHJpYnV0ZSgnYXJpYS1sYWJlbCcsIHRyYW5zLl9fKCdSdW5uaW5nIFNlc3Npb25zIHNlY3Rpb24nKSk7XG5cbiAgLy8gTGV0IHRoZSBhcHBsaWNhdGlvbiByZXN0b3JlciB0cmFjayB0aGUgcnVubmluZyBwYW5lbCBmb3IgcmVzdG9yYXRpb24gb2ZcbiAgLy8gYXBwbGljYXRpb24gc3RhdGUgKGUuZy4gc2V0dGluZyB0aGUgcnVubmluZyBwYW5lbCBhcyB0aGUgY3VycmVudCBzaWRlIGJhclxuICAvLyB3aWRnZXQpLlxuICBpZiAocmVzdG9yZXIpIHtcbiAgICByZXN0b3Jlci5hZGQocnVubmluZywgJ3J1bm5pbmctc2Vzc2lvbnMnKTtcbiAgfVxuICBpZiAobGFiU2hlbGwpIHtcbiAgICBhZGRPcGVuVGFic1Nlc3Npb25NYW5hZ2VyKHJ1bm5pbmdTZXNzaW9uTWFuYWdlcnMsIHRyYW5zbGF0b3IsIGxhYlNoZWxsKTtcbiAgfVxuICBhZGRLZXJuZWxSdW5uaW5nU2Vzc2lvbk1hbmFnZXIocnVubmluZ1Nlc3Npb25NYW5hZ2VycywgdHJhbnNsYXRvciwgYXBwKTtcbiAgLy8gUmFuayBoYXMgYmVlbiBjaG9zZW4gc29tZXdoYXQgYXJiaXRyYXJpbHkgdG8gZ2l2ZSBwcmlvcml0eSB0byB0aGUgcnVubmluZ1xuICAvLyBzZXNzaW9ucyB3aWRnZXQgaW4gdGhlIHNpZGViYXIuXG4gIGFwcC5zaGVsbC5hZGQocnVubmluZywgJ2xlZnQnLCB7IHJhbms6IDIwMCwgdHlwZTogJ1Nlc3Npb25zIGFuZCBUYWJzJyB9KTtcblxuICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnNob3dQYW5lbCwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnU2Vzc2lvbnMgYW5kIFRhYnMnKSxcbiAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICBhcHAuc2hlbGwuYWN0aXZhdGVCeUlkKHJ1bm5pbmcuaWQpO1xuICAgIH1cbiAgfSk7XG5cbiAgcmV0dXJuIHJ1bm5pbmdTZXNzaW9uTWFuYWdlcnM7XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IEp1cHl0ZXJGcm9udEVuZCB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7IFBhdGhFeHQgfSBmcm9tICdAanVweXRlcmxhYi9jb3JldXRpbHMnO1xuaW1wb3J0IHsgSVJ1bm5pbmdTZXNzaW9uTWFuYWdlcnMsIElSdW5uaW5nU2Vzc2lvbnMgfSBmcm9tICdAanVweXRlcmxhYi9ydW5uaW5nJztcbmltcG9ydCB7IFNlc3Npb24gfSBmcm9tICdAanVweXRlcmxhYi9zZXJ2aWNlcyc7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IGNvbnNvbGVJY29uLCBmaWxlSWNvbiwgbm90ZWJvb2tJY29uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyB0b0FycmF5IH0gZnJvbSAnQGx1bWluby9hbGdvcml0aG0nO1xuXG4vKipcbiAqIEFkZCB0aGUgcnVubmluZyBrZXJuZWwgbWFuYWdlciAobm90ZWJvb2tzICYgY29uc29sZXMpIHRvIHRoZSBydW5uaW5nIHBhbmVsLlxuICovXG5leHBvcnQgZnVuY3Rpb24gYWRkS2VybmVsUnVubmluZ1Nlc3Npb25NYW5hZ2VyKFxuICBtYW5hZ2VyczogSVJ1bm5pbmdTZXNzaW9uTWFuYWdlcnMsXG4gIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICBhcHA6IEp1cHl0ZXJGcm9udEVuZFxuKTogdm9pZCB7XG4gIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gIGNvbnN0IG1hbmFnZXIgPSBhcHAuc2VydmljZU1hbmFnZXIuc2Vzc2lvbnM7XG4gIGNvbnN0IHNwZWNzTWFuYWdlciA9IGFwcC5zZXJ2aWNlTWFuYWdlci5rZXJuZWxzcGVjcztcbiAgZnVuY3Rpb24gZmlsdGVyU2Vzc2lvbnMobTogU2Vzc2lvbi5JTW9kZWwpIHtcbiAgICByZXR1cm4gISEoXG4gICAgICAobS5uYW1lIHx8IFBhdGhFeHQuYmFzZW5hbWUobS5wYXRoKSkuaW5kZXhPZignLicpICE9PSAtMSB8fCBtLm5hbWVcbiAgICApO1xuICB9XG5cbiAgbWFuYWdlcnMuYWRkKHtcbiAgICBuYW1lOiB0cmFucy5fXygnS2VybmVscycpLFxuICAgIHJ1bm5pbmc6ICgpID0+IHtcbiAgICAgIHJldHVybiB0b0FycmF5KG1hbmFnZXIucnVubmluZygpKVxuICAgICAgICAuZmlsdGVyKGZpbHRlclNlc3Npb25zKVxuICAgICAgICAubWFwKG1vZGVsID0+IG5ldyBSdW5uaW5nS2VybmVsKG1vZGVsKSk7XG4gICAgfSxcbiAgICBzaHV0ZG93bkFsbDogKCkgPT4gbWFuYWdlci5zaHV0ZG93bkFsbCgpLFxuICAgIHJlZnJlc2hSdW5uaW5nOiAoKSA9PiBtYW5hZ2VyLnJlZnJlc2hSdW5uaW5nKCksXG4gICAgcnVubmluZ0NoYW5nZWQ6IG1hbmFnZXIucnVubmluZ0NoYW5nZWQsXG4gICAgc2h1dGRvd25MYWJlbDogdHJhbnMuX18oJ1NodXQgRG93bicpLFxuICAgIHNodXRkb3duQWxsTGFiZWw6IHRyYW5zLl9fKCdTaHV0IERvd24gQWxsJyksXG4gICAgc2h1dGRvd25BbGxDb25maXJtYXRpb25UZXh0OiB0cmFucy5fXyhcbiAgICAgICdBcmUgeW91IHN1cmUgeW91IHdhbnQgdG8gcGVybWFuZW50bHkgc2h1dCBkb3duIGFsbCBydW5uaW5nIGtlcm5lbHM/J1xuICAgIClcbiAgfSk7XG5cbiAgY2xhc3MgUnVubmluZ0tlcm5lbCBpbXBsZW1lbnRzIElSdW5uaW5nU2Vzc2lvbnMuSVJ1bm5pbmdJdGVtIHtcbiAgICBjb25zdHJ1Y3Rvcihtb2RlbDogU2Vzc2lvbi5JTW9kZWwpIHtcbiAgICAgIHRoaXMuX21vZGVsID0gbW9kZWw7XG4gICAgfVxuICAgIG9wZW4oKSB7XG4gICAgICBjb25zdCB7IHBhdGgsIHR5cGUgfSA9IHRoaXMuX21vZGVsO1xuICAgICAgaWYgKHR5cGUudG9Mb3dlckNhc2UoKSA9PT0gJ2NvbnNvbGUnKSB7XG4gICAgICAgIHZvaWQgYXBwLmNvbW1hbmRzLmV4ZWN1dGUoJ2NvbnNvbGU6b3BlbicsIHsgcGF0aCB9KTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIHZvaWQgYXBwLmNvbW1hbmRzLmV4ZWN1dGUoJ2RvY21hbmFnZXI6b3BlbicsIHsgcGF0aCB9KTtcbiAgICAgIH1cbiAgICB9XG4gICAgc2h1dGRvd24oKSB7XG4gICAgICByZXR1cm4gbWFuYWdlci5zaHV0ZG93bih0aGlzLl9tb2RlbC5pZCk7XG4gICAgfVxuICAgIGljb24oKSB7XG4gICAgICBjb25zdCB7IG5hbWUsIHBhdGgsIHR5cGUgfSA9IHRoaXMuX21vZGVsO1xuICAgICAgaWYgKChuYW1lIHx8IFBhdGhFeHQuYmFzZW5hbWUocGF0aCkpLmluZGV4T2YoJy5pcHluYicpICE9PSAtMSkge1xuICAgICAgICByZXR1cm4gbm90ZWJvb2tJY29uO1xuICAgICAgfSBlbHNlIGlmICh0eXBlLnRvTG93ZXJDYXNlKCkgPT09ICdjb25zb2xlJykge1xuICAgICAgICByZXR1cm4gY29uc29sZUljb247XG4gICAgICB9XG4gICAgICByZXR1cm4gZmlsZUljb247XG4gICAgfVxuICAgIGxhYmVsKCkge1xuICAgICAgcmV0dXJuIHRoaXMuX21vZGVsLm5hbWUgfHwgUGF0aEV4dC5iYXNlbmFtZSh0aGlzLl9tb2RlbC5wYXRoKTtcbiAgICB9XG4gICAgbGFiZWxUaXRsZSgpIHtcbiAgICAgIGNvbnN0IHsga2VybmVsLCBwYXRoIH0gPSB0aGlzLl9tb2RlbDtcbiAgICAgIGxldCBrZXJuZWxOYW1lID0ga2VybmVsPy5uYW1lO1xuICAgICAgaWYgKGtlcm5lbE5hbWUgJiYgc3BlY3NNYW5hZ2VyLnNwZWNzKSB7XG4gICAgICAgIGNvbnN0IHNwZWMgPSBzcGVjc01hbmFnZXIuc3BlY3Mua2VybmVsc3BlY3Nba2VybmVsTmFtZV07XG4gICAgICAgIGtlcm5lbE5hbWUgPSBzcGVjID8gc3BlYy5kaXNwbGF5X25hbWUgOiAndW5rbm93bic7XG4gICAgICB9XG4gICAgICByZXR1cm4gdHJhbnMuX18oJ1BhdGg6ICUxXFxuS2VybmVsOiAlMicsIHBhdGgsIGtlcm5lbE5hbWUpO1xuICAgIH1cblxuICAgIHByaXZhdGUgX21vZGVsOiBTZXNzaW9uLklNb2RlbDtcbiAgfVxufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBJTGFiU2hlbGwgfSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQgeyBEb2N1bWVudFdpZGdldCB9IGZyb20gJ0BqdXB5dGVybGFiL2RvY3JlZ2lzdHJ5JztcbmltcG9ydCB7IElSdW5uaW5nU2Vzc2lvbk1hbmFnZXJzLCBJUnVubmluZ1Nlc3Npb25zIH0gZnJvbSAnQGp1cHl0ZXJsYWIvcnVubmluZyc7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IGZpbGVJY29uLCBMYWJJY29uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyB0b0FycmF5IH0gZnJvbSAnQGx1bWluby9hbGdvcml0aG0nO1xuaW1wb3J0IHsgSVNpZ25hbCwgU2lnbmFsIH0gZnJvbSAnQGx1bWluby9zaWduYWxpbmcnO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcblxuLyoqXG4gKiBBIGNsYXNzIHVzZWQgdG8gY29uc29saWRhdGUgdGhlIHNpZ25hbHMgdXNlZCB0byByZXJlbmRlciB0aGUgb3BlbiB0YWJzIHNlY3Rpb24uXG4gKi9cbmNsYXNzIE9wZW5UYWJzU2lnbmFsZXIge1xuICBjb25zdHJ1Y3RvcihsYWJTaGVsbDogSUxhYlNoZWxsKSB7XG4gICAgdGhpcy5fbGFiU2hlbGwgPSBsYWJTaGVsbDtcbiAgICB0aGlzLl9sYWJTaGVsbC5sYXlvdXRNb2RpZmllZC5jb25uZWN0KHRoaXMuX2VtaXRUYWJzQ2hhbmdlZCwgdGhpcyk7XG4gIH1cblxuICAvKipcbiAgICogQSBzaWduYWwgdGhhdCBmaXJlcyB3aGVuIHRoZSBvcGVuIHRhYnMgc2VjdGlvbiBzaG91bGQgYmUgcmVyZW5kZXJlZC5cbiAgICovXG4gIGdldCB0YWJzQ2hhbmdlZCgpOiBJU2lnbmFsPHRoaXMsIHZvaWQ+IHtcbiAgICByZXR1cm4gdGhpcy5fdGFic0NoYW5nZWQ7XG4gIH1cblxuICAvKipcbiAgICogQWRkIGEgd2lkZ2V0IHRvIHdhdGNoIGZvciB0aXRsZSBjaGFuZ2luZy5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldCBBIHdpZGdldCB3aG9zZSB0aXRsZSBtYXkgY2hhbmdlLlxuICAgKi9cbiAgYWRkV2lkZ2V0KHdpZGdldDogV2lkZ2V0KTogdm9pZCB7XG4gICAgd2lkZ2V0LnRpdGxlLmNoYW5nZWQuY29ubmVjdCh0aGlzLl9lbWl0VGFic0NoYW5nZWQsIHRoaXMpO1xuICAgIHRoaXMuX3dpZGdldHMucHVzaCh3aWRnZXQpO1xuICB9XG5cbiAgLyoqXG4gICAqIEVtaXQgdGhlIG1haW4gc2lnbmFsIHRoYXQgaW5kaWNhdGVzIHRoZSBvcGVuIHRhYnMgc2hvdWxkIGJlIHJlcmVuZGVyZWQuXG4gICAqL1xuICBwcml2YXRlIF9lbWl0VGFic0NoYW5nZWQoKTogdm9pZCB7XG4gICAgdGhpcy5fd2lkZ2V0cy5mb3JFYWNoKHdpZGdldCA9PiB7XG4gICAgICB3aWRnZXQudGl0bGUuY2hhbmdlZC5kaXNjb25uZWN0KHRoaXMuX2VtaXRUYWJzQ2hhbmdlZCwgdGhpcyk7XG4gICAgfSk7XG4gICAgdGhpcy5fd2lkZ2V0cyA9IFtdO1xuICAgIHRoaXMuX3RhYnNDaGFuZ2VkLmVtaXQodm9pZCAwKTtcbiAgfVxuXG4gIHByaXZhdGUgX3RhYnNDaGFuZ2VkID0gbmV3IFNpZ25hbDx0aGlzLCB2b2lkPih0aGlzKTtcbiAgcHJpdmF0ZSBfbGFiU2hlbGw6IElMYWJTaGVsbDtcbiAgcHJpdmF0ZSBfd2lkZ2V0czogV2lkZ2V0W10gPSBbXTtcbn1cblxuLyoqXG4gKiBBZGQgdGhlIG9wZW4gdGFicyBzZWN0aW9uIHRvIHRoZSBydW5uaW5nIHBhbmVsLlxuICpcbiAqIEBwYXJhbSBtYW5hZ2VycyAtIFRoZSBJUnVubmluZ1Nlc3Npb25NYW5hZ2VycyB1c2VkIHRvIHJlZ2lzdGVyIHRoaXMgc2VjdGlvbi5cbiAqIEBwYXJhbSB0cmFuc2xhdG9yIC0gVGhlIHRyYW5zbGF0b3IgdG8gdXNlLlxuICogQHBhcmFtIGxhYlNoZWxsIC0gVGhlIElMYWJTaGVsbC5cbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIGFkZE9wZW5UYWJzU2Vzc2lvbk1hbmFnZXIoXG4gIG1hbmFnZXJzOiBJUnVubmluZ1Nlc3Npb25NYW5hZ2VycyxcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gIGxhYlNoZWxsOiBJTGFiU2hlbGxcbik6IHZvaWQge1xuICBjb25zdCBzaWduYWxlciA9IG5ldyBPcGVuVGFic1NpZ25hbGVyKGxhYlNoZWxsKTtcbiAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcblxuICBtYW5hZ2Vycy5hZGQoe1xuICAgIG5hbWU6IHRyYW5zLl9fKCdPcGVuIFRhYnMnKSxcbiAgICBydW5uaW5nOiAoKSA9PiB7XG4gICAgICByZXR1cm4gdG9BcnJheShsYWJTaGVsbC53aWRnZXRzKCdtYWluJykpLm1hcCgod2lkZ2V0OiBXaWRnZXQpID0+IHtcbiAgICAgICAgc2lnbmFsZXIuYWRkV2lkZ2V0KHdpZGdldCk7XG4gICAgICAgIHJldHVybiBuZXcgT3BlblRhYih3aWRnZXQpO1xuICAgICAgfSk7XG4gICAgfSxcbiAgICBzaHV0ZG93bkFsbDogKCkgPT4ge1xuICAgICAgdG9BcnJheShsYWJTaGVsbC53aWRnZXRzKCdtYWluJykpLmZvckVhY2goKHdpZGdldDogV2lkZ2V0KSA9PiB7XG4gICAgICAgIHdpZGdldC5jbG9zZSgpO1xuICAgICAgfSk7XG4gICAgfSxcbiAgICByZWZyZXNoUnVubmluZzogKCkgPT4ge1xuICAgICAgcmV0dXJuIHZvaWQgMDtcbiAgICB9LFxuICAgIHJ1bm5pbmdDaGFuZ2VkOiBzaWduYWxlci50YWJzQ2hhbmdlZCxcbiAgICBzaHV0ZG93bkxhYmVsOiB0cmFucy5fXygnQ2xvc2UnKSxcbiAgICBzaHV0ZG93bkFsbExhYmVsOiB0cmFucy5fXygnQ2xvc2UgQWxsJyksXG4gICAgc2h1dGRvd25BbGxDb25maXJtYXRpb25UZXh0OiB0cmFucy5fXyhcbiAgICAgICdBcmUgeW91IHN1cmUgeW91IHdhbnQgdG8gY2xvc2UgYWxsIG9wZW4gdGFicz8nXG4gICAgKVxuICB9KTtcblxuICBjbGFzcyBPcGVuVGFiIGltcGxlbWVudHMgSVJ1bm5pbmdTZXNzaW9ucy5JUnVubmluZ0l0ZW0ge1xuICAgIGNvbnN0cnVjdG9yKHdpZGdldDogV2lkZ2V0KSB7XG4gICAgICB0aGlzLl93aWRnZXQgPSB3aWRnZXQ7XG4gICAgfVxuICAgIG9wZW4oKSB7XG4gICAgICBsYWJTaGVsbC5hY3RpdmF0ZUJ5SWQodGhpcy5fd2lkZ2V0LmlkKTtcbiAgICB9XG4gICAgc2h1dGRvd24oKSB7XG4gICAgICB0aGlzLl93aWRnZXQuY2xvc2UoKTtcbiAgICB9XG4gICAgaWNvbigpIHtcbiAgICAgIGNvbnN0IHdpZGdldEljb24gPSB0aGlzLl93aWRnZXQudGl0bGUuaWNvbjtcbiAgICAgIHJldHVybiB3aWRnZXRJY29uIGluc3RhbmNlb2YgTGFiSWNvbiA/IHdpZGdldEljb24gOiBmaWxlSWNvbjtcbiAgICB9XG4gICAgbGFiZWwoKSB7XG4gICAgICByZXR1cm4gdGhpcy5fd2lkZ2V0LnRpdGxlLmxhYmVsO1xuICAgIH1cbiAgICBsYWJlbFRpdGxlKCkge1xuICAgICAgbGV0IGxhYmVsVGl0bGU6IHN0cmluZztcbiAgICAgIGlmICh0aGlzLl93aWRnZXQgaW5zdGFuY2VvZiBEb2N1bWVudFdpZGdldCkge1xuICAgICAgICBsYWJlbFRpdGxlID0gdGhpcy5fd2lkZ2V0LmNvbnRleHQucGF0aDtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIGxhYmVsVGl0bGUgPSB0aGlzLl93aWRnZXQudGl0bGUubGFiZWw7XG4gICAgICB9XG4gICAgICByZXR1cm4gbGFiZWxUaXRsZTtcbiAgICB9XG5cbiAgICBwcml2YXRlIF93aWRnZXQ6IFdpZGdldDtcbiAgfVxufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9