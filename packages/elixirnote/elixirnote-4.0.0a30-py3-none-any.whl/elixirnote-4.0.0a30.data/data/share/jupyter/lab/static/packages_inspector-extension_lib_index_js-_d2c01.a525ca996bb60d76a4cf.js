"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_inspector-extension_lib_index_js-_d2c01"],{

/***/ "../../packages/inspector-extension/lib/index.js":
/*!*******************************************************!*\
  !*** ../../packages/inspector-extension/lib/index.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_console__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/console */ "webpack/sharing/consume/default/@jupyterlab/console/@jupyterlab/console");
/* harmony import */ var _jupyterlab_console__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_console__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_inspector__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/inspector */ "webpack/sharing/consume/default/@jupyterlab/inspector/@jupyterlab/inspector");
/* harmony import */ var _jupyterlab_inspector__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_inspector__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module inspector-extension
 */








/**
 * The command IDs used by the inspector plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.open = 'inspector:open';
    CommandIDs.close = 'inspector:close';
    CommandIDs.toggle = 'inspector:toggle';
})(CommandIDs || (CommandIDs = {}));
/**
 * A service providing code introspection.
 */
const inspector = {
    id: '@jupyterlab/inspector-extension:inspector',
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.ITranslator],
    optional: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette, _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4__.ILauncher, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer],
    provides: _jupyterlab_inspector__WEBPACK_IMPORTED_MODULE_3__.IInspector,
    autoStart: true,
    activate: (app, translator, palette, launcher, restorer) => {
        const trans = translator.load('jupyterlab');
        const { commands, shell } = app;
        const caption = trans.__('Live updating code documentation from the active kernel');
        const openedLabel = trans.__('Contextual Help');
        const namespace = 'inspector';
        const datasetKey = 'jpInspector';
        const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
            namespace
        });
        function isInspectorOpen() {
            return inspector && !inspector.isDisposed;
        }
        let source = null;
        let inspector;
        function openInspector(args) {
            var _a;
            if (!isInspectorOpen()) {
                inspector = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget({
                    content: new _jupyterlab_inspector__WEBPACK_IMPORTED_MODULE_3__.InspectorPanel({ translator })
                });
                inspector.id = 'jp-inspector';
                inspector.title.label = openedLabel;
                inspector.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7__.inspectorIcon;
                void tracker.add(inspector);
                source = source && !source.isDisposed ? source : null;
                inspector.content.source = source;
                (_a = inspector.content.source) === null || _a === void 0 ? void 0 : _a.onEditorChange(args);
            }
            if (!inspector.isAttached) {
                shell.add(inspector, 'main', {
                    activate: false,
                    mode: 'split-right',
                    type: 'Inspector'
                });
            }
            shell.activateById(inspector.id);
            document.body.dataset[datasetKey] = 'open';
            return inspector;
        }
        function closeInspector() {
            inspector.dispose();
            delete document.body.dataset[datasetKey];
        }
        // Add inspector:open command to registry.
        const showLabel = trans.__('Show Contextual Help');
        commands.addCommand(CommandIDs.open, {
            caption,
            isEnabled: () => !inspector ||
                inspector.isDisposed ||
                !inspector.isAttached ||
                !inspector.isVisible,
            label: showLabel,
            icon: args => (args.isLauncher ? _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7__.inspectorIcon : undefined),
            execute: args => {
                var _a;
                const text = args && args.text;
                const refresh = args && args.refresh;
                // if inspector is open, see if we need a refresh
                if (isInspectorOpen() && refresh)
                    (_a = inspector.content.source) === null || _a === void 0 ? void 0 : _a.onEditorChange(text);
                else
                    openInspector(text);
            }
        });
        // Add inspector:close command to registry.
        const closeLabel = trans.__('Hide Contextual Help');
        commands.addCommand(CommandIDs.close, {
            caption,
            isEnabled: () => isInspectorOpen(),
            label: closeLabel,
            icon: args => (args.isLauncher ? _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7__.inspectorIcon : undefined),
            execute: () => closeInspector()
        });
        // Add inspector:toggle command to registry.
        const toggleLabel = trans.__('Show Contextual Help');
        commands.addCommand(CommandIDs.toggle, {
            caption,
            label: toggleLabel,
            isToggled: () => isInspectorOpen(),
            execute: args => {
                if (isInspectorOpen()) {
                    closeInspector();
                }
                else {
                    const text = args && args.text;
                    openInspector(text);
                }
            }
        });
        // Add open command to launcher if possible.
        // if (launcher) {
        //   launcher.add({ command: CommandIDs.open, args: { isLauncher: true } });
        // }
        // Add toggle command to command palette if possible.
        if (palette) {
            palette.addItem({ command: CommandIDs.toggle, category: toggleLabel });
        }
        // Handle state restoration.
        if (restorer) {
            void restorer.restore(tracker, {
                command: CommandIDs.toggle,
                name: () => 'inspector'
            });
        }
        // Create a proxy to pass the `source` to the current inspector.
        const proxy = Object.defineProperty({}, 'source', {
            get: () => !inspector || inspector.isDisposed ? null : inspector.content.source,
            set: (src) => {
                source = src && !src.isDisposed ? src : null;
                if (inspector && !inspector.isDisposed) {
                    inspector.content.source = source;
                }
            }
        });
        return proxy;
    }
};
/**
 * An extension that registers consoles for inspection.
 */
const consoles = {
    id: '@jupyterlab/inspector-extension:consoles',
    requires: [_jupyterlab_inspector__WEBPACK_IMPORTED_MODULE_3__.IInspector, _jupyterlab_console__WEBPACK_IMPORTED_MODULE_2__.IConsoleTracker, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell],
    autoStart: true,
    activate: (app, manager, consoles, labShell, translator) => {
        // Maintain association of new consoles with their respective handlers.
        const handlers = {};
        // Create a handler for each console that is created.
        consoles.widgetAdded.connect((sender, parent) => {
            const sessionContext = parent.console.sessionContext;
            const rendermime = parent.console.rendermime;
            const connector = new _jupyterlab_inspector__WEBPACK_IMPORTED_MODULE_3__.KernelConnector({ sessionContext });
            const handler = new _jupyterlab_inspector__WEBPACK_IMPORTED_MODULE_3__.InspectionHandler({ connector, rendermime });
            // Associate the handler to the widget.
            handlers[parent.id] = handler;
            // Set the initial editor.
            const cell = parent.console.promptCell;
            handler.editor = cell && cell.editor;
            // Listen for prompt creation.
            parent.console.promptCellCreated.connect((sender, cell) => {
                handler.editor = cell && cell.editor;
            });
            // Listen for parent disposal.
            parent.disposed.connect(() => {
                delete handlers[parent.id];
                handler.dispose();
            });
        });
        // Keep track of console instances and set inspector source.
        labShell.currentChanged.connect((_, args) => {
            const widget = args.newValue;
            if (!widget || !consoles.has(widget)) {
                return;
            }
            const source = handlers[widget.id];
            if (source) {
                manager.source = source;
            }
        });
    }
};
/**
 * An extension that registers notebooks for inspection.
 */
const notebooks = {
    id: '@jupyterlab/inspector-extension:notebooks',
    requires: [_jupyterlab_inspector__WEBPACK_IMPORTED_MODULE_3__.IInspector, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_5__.INotebookTracker, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell],
    autoStart: true,
    activate: (app, manager, notebooks, labShell) => {
        // Maintain association of new notebooks with their respective handlers.
        const handlers = {};
        // Create a handler for each notebook that is created.
        notebooks.widgetAdded.connect((sender, parent) => {
            const sessionContext = parent.sessionContext;
            const rendermime = parent.content.rendermime;
            const connector = new _jupyterlab_inspector__WEBPACK_IMPORTED_MODULE_3__.KernelConnector({ sessionContext });
            const handler = new _jupyterlab_inspector__WEBPACK_IMPORTED_MODULE_3__.InspectionHandler({ connector, rendermime });
            // Associate the handler to the widget.
            handlers[parent.id] = handler;
            // Set the initial editor.
            const cell = parent.content.activeCell;
            handler.editor = cell && cell.editor;
            // Listen for active cell changes.
            parent.content.activeCellChanged.connect((sender, cell) => {
                handler.editor = cell && cell.editor;
            });
            // Listen for parent disposal.
            parent.disposed.connect(() => {
                delete handlers[parent.id];
                handler.dispose();
            });
        });
        // Keep track of notebook instances and set inspector source.
        labShell.currentChanged.connect((sender, args) => {
            const widget = args.newValue;
            if (!widget || !notebooks.has(widget)) {
                return;
            }
            const source = handlers[widget.id];
            if (source) {
                manager.source = source;
            }
        });
    }
};
/**
 * Export the plugins as default.
 */
const plugins = [inspector, consoles, notebooks];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfaW5zcGVjdG9yLWV4dGVuc2lvbl9saWJfaW5kZXhfanMtX2QyYzAxLmE1MjVjYTk5NmJiNjBkNzZhNGNmLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFPOEI7QUFLSDtBQUN3QjtBQU12QjtBQUNrQjtBQUNPO0FBQ0Y7QUFDSTtBQUUxRDs7R0FFRztBQUNILElBQVUsVUFBVSxDQUluQjtBQUpELFdBQVUsVUFBVTtJQUNMLGVBQUksR0FBRyxnQkFBZ0IsQ0FBQztJQUN4QixnQkFBSyxHQUFHLGlCQUFpQixDQUFDO0lBQzFCLGlCQUFNLEdBQUcsa0JBQWtCLENBQUM7QUFDM0MsQ0FBQyxFQUpTLFVBQVUsS0FBVixVQUFVLFFBSW5CO0FBRUQ7O0dBRUc7QUFDSCxNQUFNLFNBQVMsR0FBc0M7SUFDbkQsRUFBRSxFQUFFLDJDQUEyQztJQUMvQyxRQUFRLEVBQUUsQ0FBQyxnRUFBVyxDQUFDO0lBQ3ZCLFFBQVEsRUFBRSxDQUFDLGlFQUFlLEVBQUUsMkRBQVMsRUFBRSxvRUFBZSxDQUFDO0lBQ3ZELFFBQVEsRUFBRSw2REFBVTtJQUNwQixTQUFTLEVBQUUsSUFBSTtJQUNmLFFBQVEsRUFBRSxDQUNSLEdBQW9CLEVBQ3BCLFVBQXVCLEVBQ3ZCLE9BQStCLEVBQy9CLFFBQTBCLEVBQzFCLFFBQWdDLEVBQ3BCLEVBQUU7UUFDZCxNQUFNLEtBQUssR0FBRyxVQUFVLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FBQyxDQUFDO1FBQzVDLE1BQU0sRUFBRSxRQUFRLEVBQUUsS0FBSyxFQUFFLEdBQUcsR0FBRyxDQUFDO1FBQ2hDLE1BQU0sT0FBTyxHQUFHLEtBQUssQ0FBQyxFQUFFLENBQ3RCLHlEQUF5RCxDQUMxRCxDQUFDO1FBQ0YsTUFBTSxXQUFXLEdBQUcsS0FBSyxDQUFDLEVBQUUsQ0FBQyxpQkFBaUIsQ0FBQyxDQUFDO1FBQ2hELE1BQU0sU0FBUyxHQUFH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LE1BQU0sQ0FBQzthQUN6QjtRQUNILENBQUMsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztDQUNGLENBQUM7QUFFRjs7R0FFRztBQUNILE1BQU0sT0FBTyxHQUFpQyxDQUFDLFNBQVMsRUFBRSxRQUFRLEVBQUUsU0FBUyxDQUFDLENBQUM7QUFDL0UsaUVBQWUsT0FBTyxFQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2luc3BlY3Rvci1leHRlbnNpb24vc3JjL2luZGV4LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGluc3BlY3Rvci1leHRlbnNpb25cbiAqL1xuXG5pbXBvcnQge1xuICBJTGFiU2hlbGwsXG4gIElMYXlvdXRSZXN0b3JlcixcbiAgSnVweXRlckZyb250RW5kLFxuICBKdXB5dGVyRnJvbnRFbmRQbHVnaW5cbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24nO1xuaW1wb3J0IHtcbiAgSUNvbW1hbmRQYWxldHRlLFxuICBNYWluQXJlYVdpZGdldCxcbiAgV2lkZ2V0VHJhY2tlclxufSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBJQ29uc29sZVRyYWNrZXIgfSBmcm9tICdAanVweXRlcmxhYi9jb25zb2xlJztcbmltcG9ydCB7XG4gIElJbnNwZWN0b3IsXG4gIEluc3BlY3Rpb25IYW5kbGVyLFxuICBJbnNwZWN0b3JQYW5lbCxcbiAgS2VybmVsQ29ubmVjdG9yXG59IGZyb20gJ0BqdXB5dGVybGFiL2luc3BlY3Rvcic7XG5pbXBvcnQgeyBJTGF1bmNoZXIgfSBmcm9tICdAanVweXRlcmxhYi9sYXVuY2hlcic7XG5pbXBvcnQgeyBJTm90ZWJvb2tUcmFja2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvbm90ZWJvb2snO1xuaW1wb3J0IHsgSVRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQgeyBpbnNwZWN0b3JJY29uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5cbi8qKlxuICogVGhlIGNvbW1hbmQgSURzIHVzZWQgYnkgdGhlIGluc3BlY3RvciBwbHVnaW4uXG4gKi9cbm5hbWVzcGFjZSBDb21tYW5kSURzIHtcbiAgZXhwb3J0IGNvbnN0IG9wZW4gPSAnaW5zcGVjdG9yOm9wZW4nO1xuICBleHBvcnQgY29uc3QgY2xvc2UgPSAnaW5zcGVjdG9yOmNsb3NlJztcbiAgZXhwb3J0IGNvbnN0IHRvZ2dsZSA9ICdpbnNwZWN0b3I6dG9nZ2xlJztcbn1cblxuLyoqXG4gKiBBIHNlcnZpY2UgcHJvdmlkaW5nIGNvZGUgaW50cm9zcGVjdGlvbi5cbiAqL1xuY29uc3QgaW5zcGVjdG9yOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SUluc3BlY3Rvcj4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvaW5zcGVjdG9yLWV4dGVuc2lvbjppbnNwZWN0b3InLFxuICByZXF1aXJlczogW0lUcmFuc2xhdG9yXSxcbiAgb3B0aW9uYWw6IFtJQ29tbWFuZFBhbGV0dGUsIElMYXVuY2hlciwgSUxheW91dFJlc3RvcmVyXSxcbiAgcHJvdmlkZXM6IElJbnNwZWN0b3IsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcixcbiAgICBwYWxldHRlOiBJQ29tbWFuZFBhbGV0dGUgfCBudWxsLFxuICAgIGxhdW5jaGVyOiBJTGF1bmNoZXIgfCBudWxsLFxuICAgIHJlc3RvcmVyOiBJTGF5b3V0UmVzdG9yZXIgfCBudWxsXG4gICk6IElJbnNwZWN0b3IgPT4ge1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgY29uc3QgeyBjb21tYW5kcywgc2hlbGwgfSA9IGFwcDtcbiAgICBjb25zdCBjYXB0aW9uID0gdHJhbnMuX18oXG4gICAgICAnTGl2ZSB1cGRhdGluZyBjb2RlIGRvY3VtZW50YXRpb24gZnJvbSB0aGUgYWN0aXZlIGtlcm5lbCdcbiAgICApO1xuICAgIGNvbnN0IG9wZW5lZExhYmVsID0gdHJhbnMuX18oJ0NvbnRleHR1YWwgSGVscCcpO1xuICAgIGNvbnN0IG5hbWVzcGFjZSA9ICdpbnNwZWN0b3InO1xuICAgIGNvbnN0IGRhdGFzZXRLZXkgPSAnanBJbnNwZWN0b3InO1xuICAgIGNvbnN0IHRyYWNrZXIgPSBuZXcgV2lkZ2V0VHJhY2tlcjxNYWluQXJlYVdpZGdldDxJbnNwZWN0b3JQYW5lbD4+KHtcbiAgICAgIG5hbWVzcGFjZVxuICAgIH0pO1xuXG4gICAgZnVuY3Rpb24gaXNJbnNwZWN0b3JPcGVuKCkge1xuICAgICAgcmV0dXJuIGluc3BlY3RvciAmJiAhaW5zcGVjdG9yLmlzRGlzcG9zZWQ7XG4gICAgfVxuXG4gICAgbGV0IHNvdXJjZTogSUluc3BlY3Rvci5JSW5zcGVjdGFibGUgfCBudWxsID0gbnVsbDtcbiAgICBsZXQgaW5zcGVjdG9yOiBNYWluQXJlYVdpZGdldDxJbnNwZWN0b3JQYW5lbD47XG4gICAgZnVuY3Rpb24gb3Blbkluc3BlY3RvcihhcmdzOiBzdHJpbmcpOiBNYWluQXJlYVdpZGdldDxJbnNwZWN0b3JQYW5lbD4ge1xuICAgICAgaWYgKCFpc0luc3BlY3Rvck9wZW4oKSkge1xuICAgICAgICBpbnNwZWN0b3IgPSBuZXcgTWFpbkFyZWFXaWRnZXQoe1xuICAgICAgICAgIGNvbnRlbnQ6IG5ldyBJbnNwZWN0b3JQYW5lbCh7IHRyYW5zbGF0b3IgfSlcbiAgICAgICAgfSk7XG4gICAgICAgIGluc3BlY3Rvci5pZCA9ICdqcC1pbnNwZWN0b3InO1xuICAgICAgICBpbnNwZWN0b3IudGl0bGUubGFiZWwgPSBvcGVuZWRMYWJlbDtcbiAgICAgICAgaW5zcGVjdG9yLnRpdGxlLmljb24gPSBpbnNwZWN0b3JJY29uO1xuICAgICAgICB2b2lkIHRyYWNrZXIuYWRkKGluc3BlY3Rvcik7XG4gICAgICAgIHNvdXJjZSA9IHNvdXJjZSAmJiAhc291cmNlLmlzRGlzcG9zZWQgPyBzb3VyY2UgOiBudWxsO1xuICAgICAgICBpbnNwZWN0b3IuY29udGVudC5zb3VyY2UgPSBzb3VyY2U7XG4gICAgICAgIGluc3BlY3Rvci5jb250ZW50LnNvdXJjZT8ub25FZGl0b3JDaGFuZ2UoYXJncyk7XG4gICAgICB9XG4gICAgICBpZiAoIWluc3BlY3Rvci5pc0F0dGFjaGVkKSB7XG4gICAgICAgIHNoZWxsLmFkZChpbnNwZWN0b3IsICdtYWluJywge1xuICAgICAgICAgIGFjdGl2YXRlOiBmYWxzZSxcbiAgICAgICAgICBtb2RlOiAnc3BsaXQtcmlnaHQnLFxuICAgICAgICAgIHR5cGU6ICdJbnNwZWN0b3InXG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgICAgc2hlbGwuYWN0aXZhdGVCeUlkKGluc3BlY3Rvci5pZCk7XG4gICAgICBkb2N1bWVudC5ib2R5LmRhdGFzZXRbZGF0YXNldEtleV0gPSAnb3Blbic7XG4gICAgICByZXR1cm4gaW5zcGVjdG9yO1xuICAgIH1cbiAgICBmdW5jdGlvbiBjbG9zZUluc3BlY3RvcigpOiB2b2lkIHtcbiAgICAgIGluc3BlY3Rvci5kaXNwb3NlKCk7XG4gICAgICBkZWxldGUgZG9jdW1lbnQuYm9keS5kYXRhc2V0W2RhdGFzZXRLZXldO1xuICAgIH1cblxuICAgIC8vIEFkZCBpbnNwZWN0b3I6b3BlbiBjb21tYW5kIHRvIHJlZ2lzdHJ5LlxuICAgIGNvbnN0IHNob3dMYWJlbCA9IHRyYW5zLl9fKCdTaG93IENvbnRleHR1YWwgSGVscCcpO1xuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5vcGVuLCB7XG4gICAgICBjYXB0aW9uLFxuICAgICAgaXNFbmFibGVkOiAoKSA9PlxuICAgICAgICAhaW5zcGVjdG9yIHx8XG4gICAgICAgIGluc3BlY3Rvci5pc0Rpc3Bvc2VkIHx8XG4gICAgICAgICFpbnNwZWN0b3IuaXNBdHRhY2hlZCB8fFxuICAgICAgICAhaW5zcGVjdG9yLmlzVmlzaWJsZSxcbiAgICAgIGxhYmVsOiBzaG93TGFiZWwsXG4gICAgICBpY29uOiBhcmdzID0+IChhcmdzLmlzTGF1bmNoZXIgPyBpbnNwZWN0b3JJY29uIDogdW5kZWZpbmVkKSxcbiAgICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgICBjb25zdCB0ZXh0ID0gYXJncyAmJiAoYXJncy50ZXh0IGFzIHN0cmluZyk7XG4gICAgICAgIGNvbnN0IHJlZnJlc2ggPSBhcmdzICYmIChhcmdzLnJlZnJlc2ggYXMgYm9vbGVhbik7XG4gICAgICAgIC8vIGlmIGluc3BlY3RvciBpcyBvcGVuLCBzZWUgaWYgd2UgbmVlZCBhIHJlZnJlc2hcbiAgICAgICAgaWYgKGlzSW5zcGVjdG9yT3BlbigpICYmIHJlZnJlc2gpXG4gICAgICAgICAgaW5zcGVjdG9yLmNvbnRlbnQuc291cmNlPy5vbkVkaXRvckNoYW5nZSh0ZXh0KTtcbiAgICAgICAgZWxzZSBvcGVuSW5zcGVjdG9yKHRleHQpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgLy8gQWRkIGluc3BlY3RvcjpjbG9zZSBjb21tYW5kIHRvIHJlZ2lzdHJ5LlxuICAgIGNvbnN0IGNsb3NlTGFiZWwgPSB0cmFucy5fXygnSGlkZSBDb250ZXh0dWFsIEhlbHAnKTtcbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY2xvc2UsIHtcbiAgICAgIGNhcHRpb24sXG4gICAgICBpc0VuYWJsZWQ6ICgpID0+IGlzSW5zcGVjdG9yT3BlbigpLFxuICAgICAgbGFiZWw6IGNsb3NlTGFiZWwsXG4gICAgICBpY29uOiBhcmdzID0+IChhcmdzLmlzTGF1bmNoZXIgPyBpbnNwZWN0b3JJY29uIDogdW5kZWZpbmVkKSxcbiAgICAgIGV4ZWN1dGU6ICgpID0+IGNsb3NlSW5zcGVjdG9yKClcbiAgICB9KTtcblxuICAgIC8vIEFkZCBpbnNwZWN0b3I6dG9nZ2xlIGNvbW1hbmQgdG8gcmVnaXN0cnkuXG4gICAgY29uc3QgdG9nZ2xlTGFiZWwgPSB0cmFucy5fXygnU2hvdyBDb250ZXh0dWFsIEhlbHAnKTtcbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMudG9nZ2xlLCB7XG4gICAgICBjYXB0aW9uLFxuICAgICAgbGFiZWw6IHRvZ2dsZUxhYmVsLFxuICAgICAgaXNUb2dnbGVkOiAoKSA9PiBpc0luc3BlY3Rvck9wZW4oKSxcbiAgICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgICBpZiAoaXNJbnNwZWN0b3JPcGVuKCkpIHtcbiAgICAgICAgICBjbG9zZUluc3BlY3RvcigpO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIGNvbnN0IHRleHQgPSBhcmdzICYmIChhcmdzLnRleHQgYXMgc3RyaW5nKTtcbiAgICAgICAgICBvcGVuSW5zcGVjdG9yKHRleHQpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICAvLyBBZGQgb3BlbiBjb21tYW5kIHRvIGxhdW5jaGVyIGlmIHBvc3NpYmxlLlxuICAgIC8vIGlmIChsYXVuY2hlcikge1xuICAgIC8vICAgbGF1bmNoZXIuYWRkKHsgY29tbWFuZDogQ29tbWFuZElEcy5vcGVuLCBhcmdzOiB7IGlzTGF1bmNoZXI6IHRydWUgfSB9KTtcbiAgICAvLyB9XG5cbiAgICAvLyBBZGQgdG9nZ2xlIGNvbW1hbmQgdG8gY29tbWFuZCBwYWxldHRlIGlmIHBvc3NpYmxlLlxuICAgIGlmIChwYWxldHRlKSB7XG4gICAgICBwYWxldHRlLmFkZEl0ZW0oeyBjb21tYW5kOiBDb21tYW5kSURzLnRvZ2dsZSwgY2F0ZWdvcnk6IHRvZ2dsZUxhYmVsIH0pO1xuICAgIH1cblxuICAgIC8vIEhhbmRsZSBzdGF0ZSByZXN0b3JhdGlvbi5cbiAgICBpZiAocmVzdG9yZXIpIHtcbiAgICAgIHZvaWQgcmVzdG9yZXIucmVzdG9yZSh0cmFja2VyLCB7XG4gICAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMudG9nZ2xlLFxuICAgICAgICBuYW1lOiAoKSA9PiAnaW5zcGVjdG9yJ1xuICAgICAgfSk7XG4gICAgfVxuXG4gICAgLy8gQ3JlYXRlIGEgcHJveHkgdG8gcGFzcyB0aGUgYHNvdXJjZWAgdG8gdGhlIGN1cnJlbnQgaW5zcGVjdG9yLlxuICAgIGNvbnN0IHByb3h5ID0gT2JqZWN0LmRlZmluZVByb3BlcnR5KHt9IGFzIElJbnNwZWN0b3IsICdzb3VyY2UnLCB7XG4gICAgICBnZXQ6ICgpOiBJSW5zcGVjdG9yLklJbnNwZWN0YWJsZSB8IG51bGwgPT5cbiAgICAgICAgIWluc3BlY3RvciB8fCBpbnNwZWN0b3IuaXNEaXNwb3NlZCA/IG51bGwgOiBpbnNwZWN0b3IuY29udGVudC5zb3VyY2UsXG4gICAgICBzZXQ6IChzcmM6IElJbnNwZWN0b3IuSUluc3BlY3RhYmxlIHwgbnVsbCkgPT4ge1xuICAgICAgICBzb3VyY2UgPSBzcmMgJiYgIXNyYy5pc0Rpc3Bvc2VkID8gc3JjIDogbnVsbDtcbiAgICAgICAgaWYgKGluc3BlY3RvciAmJiAhaW5zcGVjdG9yLmlzRGlzcG9zZWQpIHtcbiAgICAgICAgICBpbnNwZWN0b3IuY29udGVudC5zb3VyY2UgPSBzb3VyY2U7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9KTtcblxuICAgIHJldHVybiBwcm94eTtcbiAgfVxufTtcblxuLyoqXG4gKiBBbiBleHRlbnNpb24gdGhhdCByZWdpc3RlcnMgY29uc29sZXMgZm9yIGluc3BlY3Rpb24uXG4gKi9cbmNvbnN0IGNvbnNvbGVzOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvaW5zcGVjdG9yLWV4dGVuc2lvbjpjb25zb2xlcycsXG4gIHJlcXVpcmVzOiBbSUluc3BlY3RvciwgSUNvbnNvbGVUcmFja2VyLCBJTGFiU2hlbGxdLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgbWFuYWdlcjogSUluc3BlY3RvcixcbiAgICBjb25zb2xlczogSUNvbnNvbGVUcmFja2VyLFxuICAgIGxhYlNoZWxsOiBJTGFiU2hlbGwsXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3JcbiAgKTogdm9pZCA9PiB7XG4gICAgLy8gTWFpbnRhaW4gYXNzb2NpYXRpb24gb2YgbmV3IGNvbnNvbGVzIHdpdGggdGhlaXIgcmVzcGVjdGl2ZSBoYW5kbGVycy5cbiAgICBjb25zdCBoYW5kbGVyczogeyBbaWQ6IHN0cmluZ106IEluc3BlY3Rpb25IYW5kbGVyIH0gPSB7fTtcblxuICAgIC8vIENyZWF0ZSBhIGhhbmRsZXIgZm9yIGVhY2ggY29uc29sZSB0aGF0IGlzIGNyZWF0ZWQuXG4gICAgY29uc29sZXMud2lkZ2V0QWRkZWQuY29ubmVjdCgoc2VuZGVyLCBwYXJlbnQpID0+IHtcbiAgICAgIGNvbnN0IHNlc3Npb25Db250ZXh0ID0gcGFyZW50LmNvbnNvbGUuc2Vzc2lvbkNvbnRleHQ7XG4gICAgICBjb25zdCByZW5kZXJtaW1lID0gcGFyZW50LmNvbnNvbGUucmVuZGVybWltZTtcbiAgICAgIGNvbnN0IGNvbm5lY3RvciA9IG5ldyBLZXJuZWxDb25uZWN0b3IoeyBzZXNzaW9uQ29udGV4dCB9KTtcbiAgICAgIGNvbnN0IGhhbmRsZXIgPSBuZXcgSW5zcGVjdGlvbkhhbmRsZXIoeyBjb25uZWN0b3IsIHJlbmRlcm1pbWUgfSk7XG5cbiAgICAgIC8vIEFzc29jaWF0ZSB0aGUgaGFuZGxlciB0byB0aGUgd2lkZ2V0LlxuICAgICAgaGFuZGxlcnNbcGFyZW50LmlkXSA9IGhhbmRsZXI7XG5cbiAgICAgIC8vIFNldCB0aGUgaW5pdGlhbCBlZGl0b3IuXG4gICAgICBjb25zdCBjZWxsID0gcGFyZW50LmNvbnNvbGUucHJvbXB0Q2VsbDtcbiAgICAgIGhhbmRsZXIuZWRpdG9yID0gY2VsbCAmJiBjZWxsLmVkaXRvcjtcblxuICAgICAgLy8gTGlzdGVuIGZvciBwcm9tcHQgY3JlYXRpb24uXG4gICAgICBwYXJlbnQuY29uc29sZS5wcm9tcHRDZWxsQ3JlYXRlZC5jb25uZWN0KChzZW5kZXIsIGNlbGwpID0+IHtcbiAgICAgICAgaGFuZGxlci5lZGl0b3IgPSBjZWxsICYmIGNlbGwuZWRpdG9yO1xuICAgICAgfSk7XG5cbiAgICAgIC8vIExpc3RlbiBmb3IgcGFyZW50IGRpc3Bvc2FsLlxuICAgICAgcGFyZW50LmRpc3Bvc2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgICBkZWxldGUgaGFuZGxlcnNbcGFyZW50LmlkXTtcbiAgICAgICAgaGFuZGxlci5kaXNwb3NlKCk7XG4gICAgICB9KTtcbiAgICB9KTtcblxuICAgIC8vIEtlZXAgdHJhY2sgb2YgY29uc29sZSBpbnN0YW5jZXMgYW5kIHNldCBpbnNwZWN0b3Igc291cmNlLlxuICAgIGxhYlNoZWxsLmN1cnJlbnRDaGFuZ2VkLmNvbm5lY3QoKF8sIGFyZ3MpID0+IHtcbiAgICAgIGNvbnN0IHdpZGdldCA9IGFyZ3MubmV3VmFsdWU7XG4gICAgICBpZiAoIXdpZGdldCB8fCAhY29uc29sZXMuaGFzKHdpZGdldCkpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgY29uc3Qgc291cmNlID0gaGFuZGxlcnNbd2lkZ2V0LmlkXTtcbiAgICAgIGlmIChzb3VyY2UpIHtcbiAgICAgICAgbWFuYWdlci5zb3VyY2UgPSBzb3VyY2U7XG4gICAgICB9XG4gICAgfSk7XG4gIH1cbn07XG5cbi8qKlxuICogQW4gZXh0ZW5zaW9uIHRoYXQgcmVnaXN0ZXJzIG5vdGVib29rcyBmb3IgaW5zcGVjdGlvbi5cbiAqL1xuY29uc3Qgbm90ZWJvb2tzOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvaW5zcGVjdG9yLWV4dGVuc2lvbjpub3RlYm9va3MnLFxuICByZXF1aXJlczogW0lJbnNwZWN0b3IsIElOb3RlYm9va1RyYWNrZXIsIElMYWJTaGVsbF0sXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICBtYW5hZ2VyOiBJSW5zcGVjdG9yLFxuICAgIG5vdGVib29rczogSU5vdGVib29rVHJhY2tlcixcbiAgICBsYWJTaGVsbDogSUxhYlNoZWxsXG4gICk6IHZvaWQgPT4ge1xuICAgIC8vIE1haW50YWluIGFzc29jaWF0aW9uIG9mIG5ldyBub3RlYm9va3Mgd2l0aCB0aGVpciByZXNwZWN0aXZlIGhhbmRsZXJzLlxuICAgIGNvbnN0IGhhbmRsZXJzOiB7IFtpZDogc3RyaW5nXTogSW5zcGVjdGlvbkhhbmRsZXIgfSA9IHt9O1xuXG4gICAgLy8gQ3JlYXRlIGEgaGFuZGxlciBmb3IgZWFjaCBub3RlYm9vayB0aGF0IGlzIGNyZWF0ZWQuXG4gICAgbm90ZWJvb2tzLndpZGdldEFkZGVkLmNvbm5lY3QoKHNlbmRlciwgcGFyZW50KSA9PiB7XG4gICAgICBjb25zdCBzZXNzaW9uQ29udGV4dCA9IHBhcmVudC5zZXNzaW9uQ29udGV4dDtcbiAgICAgIGNvbnN0IHJlbmRlcm1pbWUgPSBwYXJlbnQuY29udGVudC5yZW5kZXJtaW1lO1xuICAgICAgY29uc3QgY29ubmVjdG9yID0gbmV3IEtlcm5lbENvbm5lY3Rvcih7IHNlc3Npb25Db250ZXh0IH0pO1xuICAgICAgY29uc3QgaGFuZGxlciA9IG5ldyBJbnNwZWN0aW9uSGFuZGxlcih7IGNvbm5lY3RvciwgcmVuZGVybWltZSB9KTtcblxuICAgICAgLy8gQXNzb2NpYXRlIHRoZSBoYW5kbGVyIHRvIHRoZSB3aWRnZXQuXG4gICAgICBoYW5kbGVyc1twYXJlbnQuaWRdID0gaGFuZGxlcjtcblxuICAgICAgLy8gU2V0IHRoZSBpbml0aWFsIGVkaXRvci5cbiAgICAgIGNvbnN0IGNlbGwgPSBwYXJlbnQuY29udGVudC5hY3RpdmVDZWxsO1xuICAgICAgaGFuZGxlci5lZGl0b3IgPSBjZWxsICYmIGNlbGwuZWRpdG9yO1xuXG4gICAgICAvLyBMaXN0ZW4gZm9yIGFjdGl2ZSBjZWxsIGNoYW5nZXMuXG4gICAgICBwYXJlbnQuY29udGVudC5hY3RpdmVDZWxsQ2hhbmdlZC5jb25uZWN0KChzZW5kZXIsIGNlbGwpID0+IHtcbiAgICAgICAgaGFuZGxlci5lZGl0b3IgPSBjZWxsICYmIGNlbGwuZWRpdG9yO1xuICAgICAgfSk7XG5cbiAgICAgIC8vIExpc3RlbiBmb3IgcGFyZW50IGRpc3Bvc2FsLlxuICAgICAgcGFyZW50LmRpc3Bvc2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgICBkZWxldGUgaGFuZGxlcnNbcGFyZW50LmlkXTtcbiAgICAgICAgaGFuZGxlci5kaXNwb3NlKCk7XG4gICAgICB9KTtcbiAgICB9KTtcblxuICAgIC8vIEtlZXAgdHJhY2sgb2Ygbm90ZWJvb2sgaW5zdGFuY2VzIGFuZCBzZXQgaW5zcGVjdG9yIHNvdXJjZS5cbiAgICBsYWJTaGVsbC5jdXJyZW50Q2hhbmdlZC5jb25uZWN0KChzZW5kZXIsIGFyZ3MpID0+IHtcbiAgICAgIGNvbnN0IHdpZGdldCA9IGFyZ3MubmV3VmFsdWU7XG4gICAgICBpZiAoIXdpZGdldCB8fCAhbm90ZWJvb2tzLmhhcyh3aWRnZXQpKSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGNvbnN0IHNvdXJjZSA9IGhhbmRsZXJzW3dpZGdldC5pZF07XG4gICAgICBpZiAoc291cmNlKSB7XG4gICAgICAgIG1hbmFnZXIuc291cmNlID0gc291cmNlO1xuICAgICAgfVxuICAgIH0pO1xuICB9XG59O1xuXG4vKipcbiAqIEV4cG9ydCB0aGUgcGx1Z2lucyBhcyBkZWZhdWx0LlxuICovXG5jb25zdCBwbHVnaW5zOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48YW55PltdID0gW2luc3BlY3RvciwgY29uc29sZXMsIG5vdGVib29rc107XG5leHBvcnQgZGVmYXVsdCBwbHVnaW5zO1xuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9