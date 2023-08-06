"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_tooltip-extension_lib_index_js-_85e00"],{

/***/ "../../packages/tooltip-extension/lib/index.js":
/*!*****************************************************!*\
  !*** ../../packages/tooltip-extension/lib/index.js ***!
  \*****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_console__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/console */ "webpack/sharing/consume/default/@jupyterlab/console/@jupyterlab/console");
/* harmony import */ var _jupyterlab_console__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_console__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/fileeditor */ "webpack/sharing/consume/default/@jupyterlab/fileeditor/@jupyterlab/fileeditor");
/* harmony import */ var _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_tooltip__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/tooltip */ "webpack/sharing/consume/default/@jupyterlab/tooltip/@jupyterlab/tooltip");
/* harmony import */ var _jupyterlab_tooltip__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_tooltip__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_8__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module tooltip-extension
 */









/**
 * The command IDs used by the tooltip plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.dismiss = 'tooltip:dismiss';
    CommandIDs.launchConsole = 'tooltip:launch-console';
    CommandIDs.launchNotebook = 'tooltip:launch-notebook';
    CommandIDs.launchFile = 'tooltip:launch-file';
})(CommandIDs || (CommandIDs = {}));
/**
 * The main tooltip manager plugin.
 */
const manager = {
    id: '@jupyterlab/tooltip-extension:manager',
    autoStart: true,
    optional: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.ITranslator],
    provides: _jupyterlab_tooltip__WEBPACK_IMPORTED_MODULE_5__.ITooltipManager,
    activate: (app, translator) => {
        const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.nullTranslator).load('jupyterlab');
        let tooltip = null;
        // Add tooltip dismiss command.
        app.commands.addCommand(CommandIDs.dismiss, {
            label: trans.__('Dismiss the tooltip'),
            execute: () => {
                if (tooltip) {
                    tooltip.dispose();
                    tooltip = null;
                }
            }
        });
        return {
            invoke(options) {
                const detail = 0;
                const { anchor, editor, kernel, rendermime } = options;
                if (tooltip) {
                    tooltip.dispose();
                    tooltip = null;
                }
                return Private.fetch({ detail, editor, kernel })
                    .then(bundle => {
                    tooltip = new _jupyterlab_tooltip__WEBPACK_IMPORTED_MODULE_5__.Tooltip({ anchor, bundle, editor, rendermime });
                    _lumino_widgets__WEBPACK_IMPORTED_MODULE_8__.Widget.attach(tooltip, document.body);
                })
                    .catch(() => {
                    /* Fails silently. */
                });
            }
        };
    }
};
/**
 * The console tooltip plugin.
 */
const consoles = {
    id: '@jupyterlab/tooltip-extension:consoles',
    autoStart: true,
    optional: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.ITranslator],
    requires: [_jupyterlab_tooltip__WEBPACK_IMPORTED_MODULE_5__.ITooltipManager, _jupyterlab_console__WEBPACK_IMPORTED_MODULE_0__.IConsoleTracker],
    activate: (app, manager, consoles, translator) => {
        const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.nullTranslator).load('jupyterlab');
        // Add tooltip launch command.
        app.commands.addCommand(CommandIDs.launchConsole, {
            label: trans.__('Open the tooltip'),
            execute: () => {
                var _a, _b;
                const parent = consoles.currentWidget;
                if (!parent) {
                    return;
                }
                const anchor = parent.console;
                const editor = (_a = anchor.promptCell) === null || _a === void 0 ? void 0 : _a.editor;
                const kernel = (_b = anchor.sessionContext.session) === null || _b === void 0 ? void 0 : _b.kernel;
                const rendermime = anchor.rendermime;
                // If all components necessary for rendering exist, create a tooltip.
                if (!!editor && !!kernel && !!rendermime) {
                    return manager.invoke({ anchor, editor, kernel, rendermime });
                }
            }
        });
    }
};
/**
 * The notebook tooltip plugin.
 */
const notebooks = {
    id: '@jupyterlab/tooltip-extension:notebooks',
    autoStart: true,
    optional: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.ITranslator],
    requires: [_jupyterlab_tooltip__WEBPACK_IMPORTED_MODULE_5__.ITooltipManager, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__.INotebookTracker],
    activate: (app, manager, notebooks, translator) => {
        const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.nullTranslator).load('jupyterlab');
        // Add tooltip launch command.
        app.commands.addCommand(CommandIDs.launchNotebook, {
            label: trans.__('Open the tooltip'),
            execute: () => {
                var _a, _b;
                const parent = notebooks.currentWidget;
                if (!parent) {
                    return;
                }
                const anchor = parent.content;
                const editor = (_a = anchor.activeCell) === null || _a === void 0 ? void 0 : _a.editor;
                const kernel = (_b = parent.sessionContext.session) === null || _b === void 0 ? void 0 : _b.kernel;
                const rendermime = anchor.rendermime;
                // If all components necessary for rendering exist, create a tooltip.
                if (!!editor && !!kernel && !!rendermime) {
                    return manager.invoke({ anchor, editor, kernel, rendermime });
                }
            }
        });
    }
};
/**
 * The file editor tooltip plugin.
 */
const files = {
    id: '@jupyterlab/tooltip-extension:files',
    autoStart: true,
    optional: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.ITranslator],
    requires: [_jupyterlab_tooltip__WEBPACK_IMPORTED_MODULE_5__.ITooltipManager, _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_2__.IEditorTracker, _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__.IRenderMimeRegistry],
    activate: (app, manager, editorTracker, rendermime, translator) => {
        const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.nullTranslator).load('jupyterlab');
        // Keep a list of active ISessions so that we can
        // clean them up when they are no longer needed.
        const activeSessions = {};
        const sessions = app.serviceManager.sessions;
        // When the list of running sessions changes,
        // check to see if there are any kernels with a
        // matching path for the file editors.
        const onRunningChanged = (sender, models) => {
            editorTracker.forEach(file => {
                const model = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_7__.find)(models, m => file.context.path === m.path);
                if (model) {
                    const oldSession = activeSessions[file.id];
                    // If there is a matching path, but it is the same
                    // session as we previously had, do nothing.
                    if (oldSession && oldSession.id === model.id) {
                        return;
                    }
                    // Otherwise, dispose of the old session and reset to
                    // a new CompletionConnector.
                    if (oldSession) {
                        delete activeSessions[file.id];
                        oldSession.dispose();
                    }
                    const session = sessions.connectTo({ model });
                    activeSessions[file.id] = session;
                }
                else {
                    const session = activeSessions[file.id];
                    if (session) {
                        session.dispose();
                        delete activeSessions[file.id];
                    }
                }
            });
        };
        onRunningChanged(sessions, (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_7__.toArray)(sessions.running()));
        sessions.runningChanged.connect(onRunningChanged);
        // Clean up after a widget when it is disposed
        editorTracker.widgetAdded.connect((sender, widget) => {
            widget.disposed.connect(w => {
                const session = activeSessions[w.id];
                if (session) {
                    session.dispose();
                    delete activeSessions[w.id];
                }
            });
        });
        // Add tooltip launch command.
        app.commands.addCommand(CommandIDs.launchFile, {
            label: trans.__('Open the tooltip'),
            execute: async () => {
                const parent = editorTracker.currentWidget;
                const kernel = parent &&
                    activeSessions[parent.id] &&
                    activeSessions[parent.id].kernel;
                if (!kernel) {
                    return;
                }
                const anchor = parent.content;
                const editor = anchor === null || anchor === void 0 ? void 0 : anchor.editor;
                // If all components necessary for rendering exist, create a tooltip.
                if (!!editor && !!kernel && !!rendermime) {
                    return manager.invoke({ anchor, editor, kernel, rendermime });
                }
            }
        });
    }
};
/**
 * Export the plugins as default.
 */
const plugins = [
    manager,
    consoles,
    notebooks,
    files
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);
/**
 * A namespace for private data.
 */
var Private;
(function (Private) {
    /**
     * A counter for outstanding requests.
     */
    let pending = 0;
    /**
     * Fetch a tooltip's content from the API server.
     */
    function fetch(options) {
        const { detail, editor, kernel } = options;
        const code = editor.model.value.text;
        const position = editor.getCursorPosition();
        const offset = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.Text.jsIndexToCharIndex(editor.getOffsetAt(position), code);
        // Clear hints if the new text value is empty or kernel is unavailable.
        if (!code || !kernel) {
            return Promise.reject(void 0);
        }
        const contents = {
            code,
            cursor_pos: offset,
            detail_level: detail || 0
        };
        const current = ++pending;
        return kernel.requestInspect(contents).then(msg => {
            const value = msg.content;
            // If a newer request is pending, bail.
            if (current !== pending) {
                return Promise.reject(void 0);
            }
            // If request fails or returns negative results, bail.
            if (value.status !== 'ok' || !value.found) {
                return Promise.reject(void 0);
            }
            return Promise.resolve(value.data);
        });
    }
    Private.fetch = fetch;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdG9vbHRpcC1leHRlbnNpb25fbGliX2luZGV4X2pzLV84NWUwMC43NDFjM2I0OTZmODE2ZGMwNTNmMS5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFPbUQ7QUFDVDtBQUNXO0FBQ0E7QUFDSztBQUVFO0FBQ087QUFDcEI7QUFFVDtBQUV6Qzs7R0FFRztBQUNILElBQVUsVUFBVSxDQVFuQjtBQVJELFdBQVUsVUFBVTtJQUNMLGtCQUFPLEdBQUcsaUJBQWlCLENBQUM7SUFFNUIsd0JBQWEsR0FBRyx3QkFBd0IsQ0FBQztJQUV6Qyx5QkFBYyxHQUFHLHlCQUF5QixDQUFDO0lBRTNDLHFCQUFVLEdBQUcscUJBQXFCLENBQUM7QUFDbEQsQ0FBQyxFQVJTLFVBQVUsS0FBVixVQUFVLFFBUW5CO0FBRUQ7O0dBRUc7QUFDSCxNQUFNLE9BQU8sR0FBMkM7SUFDdEQsRUFBRSxFQUFFLHVDQUF1QztJQUMzQyxTQUFTLEVBQUUsSUFBSTtJQUNmLFFBQVEsRUFBRSxDQUFDLGdFQUFXLENBQUM7SUFDdkIsUUFBUSxFQUFFLGdFQUFlO0lBQ3pCLFFBQVEsRUFBRSxDQUNSLEdBQW9CLEVBQ3BCLFVBQThCLEVBQ2IsRUFBRTtRQUNuQixNQUFNLEtBQUssR0FBRyxDQUFDLFVBQVUsYUFBVixVQUFVLGNBQVYsVUFBVSxHQUFJLG1FQUFjLENBQUMsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUM7UUFDaEUsSUFBSSxPQUFPLEdBQW1CLElBQUksQ0FBQztRQUVuQywrQkFBK0I7UUFDL0IsR0FBRyxDQUFDLFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLE9BQU8sRUFBRTtZQUMxQyxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxxQkFBcUIsQ0FBQztZQUN0QyxPQUFPLEVBQUUsR0FBRyxFQUFFO2dCQUNaLElBQUksT0FBTyxFQUFFO29CQUNYLE9B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Q0FBQyxFQWhFUyxPQUFPLEtBQVAsT0FBTyxRQWdFaEIiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvdG9vbHRpcC1leHRlbnNpb24vc3JjL2luZGV4LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIHRvb2x0aXAtZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSnVweXRlckZyb250RW5kLFxuICBKdXB5dGVyRnJvbnRFbmRQbHVnaW5cbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24nO1xuaW1wb3J0IHsgQ29kZUVkaXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL2NvZGVlZGl0b3InO1xuaW1wb3J0IHsgSUNvbnNvbGVUcmFja2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29uc29sZSc7XG5pbXBvcnQgeyBUZXh0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29yZXV0aWxzJztcbmltcG9ydCB7IElFZGl0b3JUcmFja2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvZmlsZWVkaXRvcic7XG5pbXBvcnQgeyBJTm90ZWJvb2tUcmFja2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvbm90ZWJvb2snO1xuaW1wb3J0IHsgSVJlbmRlck1pbWVSZWdpc3RyeSB9IGZyb20gJ0BqdXB5dGVybGFiL3JlbmRlcm1pbWUnO1xuaW1wb3J0IHsgS2VybmVsLCBLZXJuZWxNZXNzYWdlLCBTZXNzaW9uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2VydmljZXMnO1xuaW1wb3J0IHsgSVRvb2x0aXBNYW5hZ2VyLCBUb29sdGlwIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdG9vbHRpcCc7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciwgbnVsbFRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQgeyBmaW5kLCB0b0FycmF5IH0gZnJvbSAnQGx1bWluby9hbGdvcml0aG0nO1xuaW1wb3J0IHsgSlNPTk9iamVjdCB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5cbi8qKlxuICogVGhlIGNvbW1hbmQgSURzIHVzZWQgYnkgdGhlIHRvb2x0aXAgcGx1Z2luLlxuICovXG5uYW1lc3BhY2UgQ29tbWFuZElEcyB7XG4gIGV4cG9ydCBjb25zdCBkaXNtaXNzID0gJ3Rvb2x0aXA6ZGlzbWlzcyc7XG5cbiAgZXhwb3J0IGNvbnN0IGxhdW5jaENvbnNvbGUgPSAndG9vbHRpcDpsYXVuY2gtY29uc29sZSc7XG5cbiAgZXhwb3J0IGNvbnN0IGxhdW5jaE5vdGVib29rID0gJ3Rvb2x0aXA6bGF1bmNoLW5vdGVib29rJztcblxuICBleHBvcnQgY29uc3QgbGF1bmNoRmlsZSA9ICd0b29sdGlwOmxhdW5jaC1maWxlJztcbn1cblxuLyoqXG4gKiBUaGUgbWFpbiB0b29sdGlwIG1hbmFnZXIgcGx1Z2luLlxuICovXG5jb25zdCBtYW5hZ2VyOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SVRvb2x0aXBNYW5hZ2VyPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi90b29sdGlwLWV4dGVuc2lvbjptYW5hZ2VyJyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBvcHRpb25hbDogW0lUcmFuc2xhdG9yXSxcbiAgcHJvdmlkZXM6IElUb29sdGlwTWFuYWdlcixcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvciB8IG51bGxcbiAgKTogSVRvb2x0aXBNYW5hZ2VyID0+IHtcbiAgICBjb25zdCB0cmFucyA9ICh0cmFuc2xhdG9yID8/IG51bGxUcmFuc2xhdG9yKS5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgbGV0IHRvb2x0aXA6IFRvb2x0aXAgfCBudWxsID0gbnVsbDtcblxuICAgIC8vIEFkZCB0b29sdGlwIGRpc21pc3MgY29tbWFuZC5cbiAgICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmRpc21pc3MsIHtcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnRGlzbWlzcyB0aGUgdG9vbHRpcCcpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICBpZiAodG9vbHRpcCkge1xuICAgICAgICAgIHRvb2x0aXAuZGlzcG9zZSgpO1xuICAgICAgICAgIHRvb2x0aXAgPSBudWxsO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICByZXR1cm4ge1xuICAgICAgaW52b2tlKG9wdGlvbnM6IElUb29sdGlwTWFuYWdlci5JT3B0aW9ucyk6IFByb21pc2U8dm9pZD4ge1xuICAgICAgICBjb25zdCBkZXRhaWw6IDAgfCAxID0gMDtcbiAgICAgICAgY29uc3QgeyBhbmNob3IsIGVkaXRvciwga2VybmVsLCByZW5kZXJtaW1lIH0gPSBvcHRpb25zO1xuXG4gICAgICAgIGlmICh0b29sdGlwKSB7XG4gICAgICAgICAgdG9vbHRpcC5kaXNwb3NlKCk7XG4gICAgICAgICAgdG9vbHRpcCA9IG51bGw7XG4gICAgICAgIH1cblxuICAgICAgICByZXR1cm4gUHJpdmF0ZS5mZXRjaCh7IGRldGFpbCwgZWRpdG9yLCBrZXJuZWwgfSlcbiAgICAgICAgICAudGhlbihidW5kbGUgPT4ge1xuICAgICAgICAgICAgdG9vbHRpcCA9IG5ldyBUb29sdGlwKHsgYW5jaG9yLCBidW5kbGUsIGVkaXRvciwgcmVuZGVybWltZSB9KTtcbiAgICAgICAgICAgIFdpZGdldC5hdHRhY2godG9vbHRpcCwgZG9jdW1lbnQuYm9keSk7XG4gICAgICAgICAgfSlcbiAgICAgICAgICAuY2F0Y2goKCkgPT4ge1xuICAgICAgICAgICAgLyogRmFpbHMgc2lsZW50bHkuICovXG4gICAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfTtcbiAgfVxufTtcblxuLyoqXG4gKiBUaGUgY29uc29sZSB0b29sdGlwIHBsdWdpbi5cbiAqL1xuY29uc3QgY29uc29sZXM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi90b29sdGlwLWV4dGVuc2lvbjpjb25zb2xlcycsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgb3B0aW9uYWw6IFtJVHJhbnNsYXRvcl0sXG4gIHJlcXVpcmVzOiBbSVRvb2x0aXBNYW5hZ2VyLCBJQ29uc29sZVRyYWNrZXJdLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIG1hbmFnZXI6IElUb29sdGlwTWFuYWdlcixcbiAgICBjb25zb2xlczogSUNvbnNvbGVUcmFja2VyLFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yIHwgbnVsbFxuICApOiB2b2lkID0+IHtcbiAgICBjb25zdCB0cmFucyA9ICh0cmFuc2xhdG9yID8/IG51bGxUcmFuc2xhdG9yKS5sb2FkKCdqdXB5dGVybGFiJyk7XG5cbiAgICAvLyBBZGQgdG9vbHRpcCBsYXVuY2ggY29tbWFuZC5cbiAgICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmxhdW5jaENvbnNvbGUsIHtcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnT3BlbiB0aGUgdG9vbHRpcCcpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICBjb25zdCBwYXJlbnQgPSBjb25zb2xlcy5jdXJyZW50V2lkZ2V0O1xuXG4gICAgICAgIGlmICghcGFyZW50KSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG5cbiAgICAgICAgY29uc3QgYW5jaG9yID0gcGFyZW50LmNvbnNvbGU7XG4gICAgICAgIGNvbnN0IGVkaXRvciA9IGFuY2hvci5wcm9tcHRDZWxsPy5lZGl0b3I7XG4gICAgICAgIGNvbnN0IGtlcm5lbCA9IGFuY2hvci5zZXNzaW9uQ29udGV4dC5zZXNzaW9uPy5rZXJuZWw7XG4gICAgICAgIGNvbnN0IHJlbmRlcm1pbWUgPSBhbmNob3IucmVuZGVybWltZTtcblxuICAgICAgICAvLyBJZiBhbGwgY29tcG9uZW50cyBuZWNlc3NhcnkgZm9yIHJlbmRlcmluZyBleGlzdCwgY3JlYXRlIGEgdG9vbHRpcC5cbiAgICAgICAgaWYgKCEhZWRpdG9yICYmICEha2VybmVsICYmICEhcmVuZGVybWltZSkge1xuICAgICAgICAgIHJldHVybiBtYW5hZ2VyLmludm9rZSh7IGFuY2hvciwgZWRpdG9yLCBrZXJuZWwsIHJlbmRlcm1pbWUgfSk7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9KTtcbiAgfVxufTtcblxuLyoqXG4gKiBUaGUgbm90ZWJvb2sgdG9vbHRpcCBwbHVnaW4uXG4gKi9cbmNvbnN0IG5vdGVib29rczogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL3Rvb2x0aXAtZXh0ZW5zaW9uOm5vdGVib29rcycsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgb3B0aW9uYWw6IFtJVHJhbnNsYXRvcl0sXG4gIHJlcXVpcmVzOiBbSVRvb2x0aXBNYW5hZ2VyLCBJTm90ZWJvb2tUcmFja2VyXSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICBtYW5hZ2VyOiBJVG9vbHRpcE1hbmFnZXIsXG4gICAgbm90ZWJvb2tzOiBJTm90ZWJvb2tUcmFja2VyLFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yIHwgbnVsbFxuICApOiB2b2lkID0+IHtcbiAgICBjb25zdCB0cmFucyA9ICh0cmFuc2xhdG9yID8/IG51bGxUcmFuc2xhdG9yKS5sb2FkKCdqdXB5dGVybGFiJyk7XG5cbiAgICAvLyBBZGQgdG9vbHRpcCBsYXVuY2ggY29tbWFuZC5cbiAgICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmxhdW5jaE5vdGVib29rLCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ09wZW4gdGhlIHRvb2x0aXAnKSxcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgY29uc3QgcGFyZW50ID0gbm90ZWJvb2tzLmN1cnJlbnRXaWRnZXQ7XG5cbiAgICAgICAgaWYgKCFwYXJlbnQpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cblxuICAgICAgICBjb25zdCBhbmNob3IgPSBwYXJlbnQuY29udGVudDtcbiAgICAgICAgY29uc3QgZWRpdG9yID0gYW5jaG9yLmFjdGl2ZUNlbGw/LmVkaXRvcjtcbiAgICAgICAgY29uc3Qga2VybmVsID0gcGFyZW50LnNlc3Npb25Db250ZXh0LnNlc3Npb24/Lmtlcm5lbDtcbiAgICAgICAgY29uc3QgcmVuZGVybWltZSA9IGFuY2hvci5yZW5kZXJtaW1lO1xuXG4gICAgICAgIC8vIElmIGFsbCBjb21wb25lbnRzIG5lY2Vzc2FyeSBmb3IgcmVuZGVyaW5nIGV4aXN0LCBjcmVhdGUgYSB0b29sdGlwLlxuICAgICAgICBpZiAoISFlZGl0b3IgJiYgISFrZXJuZWwgJiYgISFyZW5kZXJtaW1lKSB7XG4gICAgICAgICAgcmV0dXJuIG1hbmFnZXIuaW52b2tlKHsgYW5jaG9yLCBlZGl0b3IsIGtlcm5lbCwgcmVuZGVybWltZSB9KTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH0pO1xuICB9XG59O1xuXG4vKipcbiAqIFRoZSBmaWxlIGVkaXRvciB0b29sdGlwIHBsdWdpbi5cbiAqL1xuY29uc3QgZmlsZXM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi90b29sdGlwLWV4dGVuc2lvbjpmaWxlcycsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgb3B0aW9uYWw6IFtJVHJhbnNsYXRvcl0sXG4gIHJlcXVpcmVzOiBbSVRvb2x0aXBNYW5hZ2VyLCBJRWRpdG9yVHJhY2tlciwgSVJlbmRlck1pbWVSZWdpc3RyeV0sXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgbWFuYWdlcjogSVRvb2x0aXBNYW5hZ2VyLFxuICAgIGVkaXRvclRyYWNrZXI6IElFZGl0b3JUcmFja2VyLFxuICAgIHJlbmRlcm1pbWU6IElSZW5kZXJNaW1lUmVnaXN0cnksXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IgfCBudWxsXG4gICk6IHZvaWQgPT4ge1xuICAgIGNvbnN0IHRyYW5zID0gKHRyYW5zbGF0b3IgPz8gbnVsbFRyYW5zbGF0b3IpLmxvYWQoJ2p1cHl0ZXJsYWInKTtcblxuICAgIC8vIEtlZXAgYSBsaXN0IG9mIGFjdGl2ZSBJU2Vzc2lvbnMgc28gdGhhdCB3ZSBjYW5cbiAgICAvLyBjbGVhbiB0aGVtIHVwIHdoZW4gdGhleSBhcmUgbm8gbG9uZ2VyIG5lZWRlZC5cbiAgICBjb25zdCBhY3RpdmVTZXNzaW9uczoge1xuICAgICAgW2lkOiBzdHJpbmddOiBTZXNzaW9uLklTZXNzaW9uQ29ubmVjdGlvbjtcbiAgICB9ID0ge307XG5cbiAgICBjb25zdCBzZXNzaW9ucyA9IGFwcC5zZXJ2aWNlTWFuYWdlci5zZXNzaW9ucztcbiAgICAvLyBXaGVuIHRoZSBsaXN0IG9mIHJ1bm5pbmcgc2Vzc2lvbnMgY2hhbmdlcyxcbiAgICAvLyBjaGVjayB0byBzZWUgaWYgdGhlcmUgYXJlIGFueSBrZXJuZWxzIHdpdGggYVxuICAgIC8vIG1hdGNoaW5nIHBhdGggZm9yIHRoZSBmaWxlIGVkaXRvcnMuXG4gICAgY29uc3Qgb25SdW5uaW5nQ2hhbmdlZCA9IChcbiAgICAgIHNlbmRlcjogU2Vzc2lvbi5JTWFuYWdlcixcbiAgICAgIG1vZGVsczogU2Vzc2lvbi5JTW9kZWxbXVxuICAgICkgPT4ge1xuICAgICAgZWRpdG9yVHJhY2tlci5mb3JFYWNoKGZpbGUgPT4ge1xuICAgICAgICBjb25zdCBtb2RlbCA9IGZpbmQobW9kZWxzLCBtID0+IGZpbGUuY29udGV4dC5wYXRoID09PSBtLnBhdGgpO1xuICAgICAgICBpZiAobW9kZWwpIHtcbiAgICAgICAgICBjb25zdCBvbGRTZXNzaW9uID0gYWN0aXZlU2Vzc2lvbnNbZmlsZS5pZF07XG4gICAgICAgICAgLy8gSWYgdGhlcmUgaXMgYSBtYXRjaGluZyBwYXRoLCBidXQgaXQgaXMgdGhlIHNhbWVcbiAgICAgICAgICAvLyBzZXNzaW9uIGFzIHdlIHByZXZpb3VzbHkgaGFkLCBkbyBub3RoaW5nLlxuICAgICAgICAgIGlmIChvbGRTZXNzaW9uICYmIG9sZFNlc3Npb24uaWQgPT09IG1vZGVsLmlkKSB7XG4gICAgICAgICAgICByZXR1cm47XG4gICAgICAgICAgfVxuICAgICAgICAgIC8vIE90aGVyd2lzZSwgZGlzcG9zZSBvZiB0aGUgb2xkIHNlc3Npb24gYW5kIHJlc2V0IHRvXG4gICAgICAgICAgLy8gYSBuZXcgQ29tcGxldGlvbkNvbm5lY3Rvci5cbiAgICAgICAgICBpZiAob2xkU2Vzc2lvbikge1xuICAgICAgICAgICAgZGVsZXRlIGFjdGl2ZVNlc3Npb25zW2ZpbGUuaWRdO1xuICAgICAgICAgICAgb2xkU2Vzc2lvbi5kaXNwb3NlKCk7XG4gICAgICAgICAgfVxuICAgICAgICAgIGNvbnN0IHNlc3Npb24gPSBzZXNzaW9ucy5jb25uZWN0VG8oeyBtb2RlbCB9KTtcbiAgICAgICAgICBhY3RpdmVTZXNzaW9uc1tmaWxlLmlkXSA9IHNlc3Npb247XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgY29uc3Qgc2Vzc2lvbiA9IGFjdGl2ZVNlc3Npb25zW2ZpbGUuaWRdO1xuICAgICAgICAgIGlmIChzZXNzaW9uKSB7XG4gICAgICAgICAgICBzZXNzaW9uLmRpc3Bvc2UoKTtcbiAgICAgICAgICAgIGRlbGV0ZSBhY3RpdmVTZXNzaW9uc1tmaWxlLmlkXTtcbiAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICAgIH0pO1xuICAgIH07XG4gICAgb25SdW5uaW5nQ2hhbmdlZChzZXNzaW9ucywgdG9BcnJheShzZXNzaW9ucy5ydW5uaW5nKCkpKTtcbiAgICBzZXNzaW9ucy5ydW5uaW5nQ2hhbmdlZC5jb25uZWN0KG9uUnVubmluZ0NoYW5nZWQpO1xuXG4gICAgLy8gQ2xlYW4gdXAgYWZ0ZXIgYSB3aWRnZXQgd2hlbiBpdCBpcyBkaXNwb3NlZFxuICAgIGVkaXRvclRyYWNrZXIud2lkZ2V0QWRkZWQuY29ubmVjdCgoc2VuZGVyLCB3aWRnZXQpID0+IHtcbiAgICAgIHdpZGdldC5kaXNwb3NlZC5jb25uZWN0KHcgPT4ge1xuICAgICAgICBjb25zdCBzZXNzaW9uID0gYWN0aXZlU2Vzc2lvbnNbdy5pZF07XG4gICAgICAgIGlmIChzZXNzaW9uKSB7XG4gICAgICAgICAgc2Vzc2lvbi5kaXNwb3NlKCk7XG4gICAgICAgICAgZGVsZXRlIGFjdGl2ZVNlc3Npb25zW3cuaWRdO1xuICAgICAgICB9XG4gICAgICB9KTtcbiAgICB9KTtcblxuICAgIC8vIEFkZCB0b29sdGlwIGxhdW5jaCBjb21tYW5kLlxuICAgIGFwcC5jb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMubGF1bmNoRmlsZSwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdPcGVuIHRoZSB0b29sdGlwJyksXG4gICAgICBleGVjdXRlOiBhc3luYyAoKSA9PiB7XG4gICAgICAgIGNvbnN0IHBhcmVudCA9IGVkaXRvclRyYWNrZXIuY3VycmVudFdpZGdldDtcbiAgICAgICAgY29uc3Qga2VybmVsID1cbiAgICAgICAgICBwYXJlbnQgJiZcbiAgICAgICAgICBhY3RpdmVTZXNzaW9uc1twYXJlbnQuaWRdICYmXG4gICAgICAgICAgYWN0aXZlU2Vzc2lvbnNbcGFyZW50LmlkXS5rZXJuZWw7XG4gICAgICAgIGlmICgha2VybmVsKSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IGFuY2hvciA9IHBhcmVudCEuY29udGVudDtcbiAgICAgICAgY29uc3QgZWRpdG9yID0gYW5jaG9yPy5lZGl0b3I7XG5cbiAgICAgICAgLy8gSWYgYWxsIGNvbXBvbmVudHMgbmVjZXNzYXJ5IGZvciByZW5kZXJpbmcgZXhpc3QsIGNyZWF0ZSBhIHRvb2x0aXAuXG4gICAgICAgIGlmICghIWVkaXRvciAmJiAhIWtlcm5lbCAmJiAhIXJlbmRlcm1pbWUpIHtcbiAgICAgICAgICByZXR1cm4gbWFuYWdlci5pbnZva2UoeyBhbmNob3IsIGVkaXRvciwga2VybmVsLCByZW5kZXJtaW1lIH0pO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG4gIH1cbn07XG5cbi8qKlxuICogRXhwb3J0IHRoZSBwbHVnaW5zIGFzIGRlZmF1bHQuXG4gKi9cbmNvbnN0IHBsdWdpbnM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxhbnk+W10gPSBbXG4gIG1hbmFnZXIsXG4gIGNvbnNvbGVzLFxuICBub3RlYm9va3MsXG4gIGZpbGVzXG5dO1xuZXhwb3J0IGRlZmF1bHQgcGx1Z2lucztcblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgcHJpdmF0ZSBkYXRhLlxuICovXG5uYW1lc3BhY2UgUHJpdmF0ZSB7XG4gIC8qKlxuICAgKiBBIGNvdW50ZXIgZm9yIG91dHN0YW5kaW5nIHJlcXVlc3RzLlxuICAgKi9cbiAgbGV0IHBlbmRpbmcgPSAwO1xuXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUZldGNoT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIGRldGFpbCBsZXZlbCByZXF1ZXN0ZWQgZnJvbSB0aGUgQVBJLlxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIFRoZSBvbmx5IGFjY2VwdGFibGUgdmFsdWVzIGFyZSAwIGFuZCAxLiBUaGUgZGVmYXVsdCB2YWx1ZSBpcyAwLlxuICAgICAqIEBzZWUgaHR0cDovL2p1cHl0ZXItY2xpZW50LnJlYWR0aGVkb2NzLmlvL2VuL2xhdGVzdC9tZXNzYWdpbmcuaHRtbCNpbnRyb3NwZWN0aW9uXG4gICAgICovXG4gICAgZGV0YWlsPzogMCB8IDE7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgcmVmZXJlbnQgZWRpdG9yIGZvciB0aGUgdG9vbHRpcC5cbiAgICAgKi9cbiAgICBlZGl0b3I6IENvZGVFZGl0b3IuSUVkaXRvcjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBrZXJuZWwgYWdhaW5zdCB3aGljaCB0aGUgQVBJIHJlcXVlc3Qgd2lsbCBiZSBtYWRlLlxuICAgICAqL1xuICAgIGtlcm5lbDogS2VybmVsLklLZXJuZWxDb25uZWN0aW9uO1xuICB9XG5cbiAgLyoqXG4gICAqIEZldGNoIGEgdG9vbHRpcCdzIGNvbnRlbnQgZnJvbSB0aGUgQVBJIHNlcnZlci5cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBmZXRjaChvcHRpb25zOiBJRmV0Y2hPcHRpb25zKTogUHJvbWlzZTxKU09OT2JqZWN0PiB7XG4gICAgY29uc3QgeyBkZXRhaWwsIGVkaXRvciwga2VybmVsIH0gPSBvcHRpb25zO1xuICAgIGNvbnN0IGNvZGUgPSBlZGl0b3IubW9kZWwudmFsdWUudGV4dDtcbiAgICBjb25zdCBwb3NpdGlvbiA9IGVkaXRvci5nZXRDdXJzb3JQb3NpdGlvbigpO1xuICAgIGNvbnN0IG9mZnNldCA9IFRleHQuanNJbmRleFRvQ2hhckluZGV4KGVkaXRvci5nZXRPZmZzZXRBdChwb3NpdGlvbiksIGNvZGUpO1xuXG4gICAgLy8gQ2xlYXIgaGludHMgaWYgdGhlIG5ldyB0ZXh0IHZhbHVlIGlzIGVtcHR5IG9yIGtlcm5lbCBpcyB1bmF2YWlsYWJsZS5cbiAgICBpZiAoIWNvZGUgfHwgIWtlcm5lbCkge1xuICAgICAgcmV0dXJuIFByb21pc2UucmVqZWN0KHZvaWQgMCk7XG4gICAgfVxuXG4gICAgY29uc3QgY29udGVudHM6IEtlcm5lbE1lc3NhZ2UuSUluc3BlY3RSZXF1ZXN0TXNnWydjb250ZW50J10gPSB7XG4gICAgICBjb2RlLFxuICAgICAgY3Vyc29yX3Bvczogb2Zmc2V0LFxuICAgICAgZGV0YWlsX2xldmVsOiBkZXRhaWwgfHwgMFxuICAgIH07XG4gICAgY29uc3QgY3VycmVudCA9ICsrcGVuZGluZztcblxuICAgIHJldHVybiBrZXJuZWwucmVxdWVzdEluc3BlY3QoY29udGVudHMpLnRoZW4obXNnID0+IHtcbiAgICAgIGNvbnN0IHZhbHVlID0gbXNnLmNvbnRlbnQ7XG5cbiAgICAgIC8vIElmIGEgbmV3ZXIgcmVxdWVzdCBpcyBwZW5kaW5nLCBiYWlsLlxuICAgICAgaWYgKGN1cnJlbnQgIT09IHBlbmRpbmcpIHtcbiAgICAgICAgcmV0dXJuIFByb21pc2UucmVqZWN0KHZvaWQgMCkgYXMgUHJvbWlzZTxKU09OT2JqZWN0PjtcbiAgICAgIH1cblxuICAgICAgLy8gSWYgcmVxdWVzdCBmYWlscyBvciByZXR1cm5zIG5lZ2F0aXZlIHJlc3VsdHMsIGJhaWwuXG4gICAgICBpZiAodmFsdWUuc3RhdHVzICE9PSAnb2snIHx8ICF2YWx1ZS5mb3VuZCkge1xuICAgICAgICByZXR1cm4gUHJvbWlzZS5yZWplY3Qodm9pZCAwKSBhcyBQcm9taXNlPEpTT05PYmplY3Q+O1xuICAgICAgfVxuXG4gICAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKHZhbHVlLmRhdGEpO1xuICAgIH0pO1xuICB9XG59XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=