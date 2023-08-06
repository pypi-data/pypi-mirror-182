"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_toc-extension_lib_index_js"],{

/***/ "../../packages/toc-extension/lib/index.js":
/*!*************************************************!*\
  !*** ../../packages/toc-extension/lib/index.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/toc */ "webpack/sharing/consume/default/@jupyterlab/toc/@jupyterlab/toc");
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_toc__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_5__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module toc-extension
 */






/**
 * A namespace for command IDs of table of contents plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.displayNumbering = 'toc:display-numbering';
    CommandIDs.displayH1Numbering = 'toc:display-h1-numbering';
    CommandIDs.displayOutputNumbering = 'toc:display-outputs-numbering';
    CommandIDs.showPanel = 'toc:show-panel';
    CommandIDs.toggleCollapse = 'toc:toggle-collapse';
})(CommandIDs || (CommandIDs = {}));
/**
 * Activates the ToC extension.
 *
 * @private
 * @param app - Jupyter application
 * @param registry - Table of contents registry
 * @param translator - translator
 * @param restorer - application layout restorer
 * @param labShell - Jupyter lab shell
 * @param settingRegistry - setting registry
 * @returns table of contents registry
 */
async function activateTOC(app, tocRegistry, translator, restorer, labShell, settingRegistry) {
    const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__.nullTranslator).load('jupyterlab');
    let configuration = Object.assign({}, _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_2__.TableOfContents.defaultConfig);
    // Create the ToC widget:
    const toc = new _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_2__.TableOfContentsPanel(translator !== null && translator !== void 0 ? translator : undefined);
    toc.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.tocIcon;
    toc.title.caption = trans.__('Table of Contents');
    toc.id = 'table-of-contents';
    toc.node.setAttribute('role', 'region');
    toc.node.setAttribute('aria-label', trans.__('Table of Contents section'));
    app.commands.addCommand(CommandIDs.displayH1Numbering, {
        label: trans.__('Show first-level heading number'),
        execute: () => {
            if (toc.model) {
                toc.model.setConfiguration({
                    numberingH1: !toc.model.configuration.numberingH1
                });
            }
        },
        isEnabled: () => { var _a, _b; return (_b = (_a = toc.model) === null || _a === void 0 ? void 0 : _a.supportedOptions.includes('numberingH1')) !== null && _b !== void 0 ? _b : false; },
        isToggled: () => { var _a, _b; return (_b = (_a = toc.model) === null || _a === void 0 ? void 0 : _a.configuration.numberingH1) !== null && _b !== void 0 ? _b : false; }
    });
    app.commands.addCommand(CommandIDs.displayNumbering, {
        label: trans.__('Show heading number in the document'),
        icon: args => (args.toolbar ? _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.numberingIcon : undefined),
        execute: () => {
            if (toc.model) {
                toc.model.setConfiguration({
                    numberHeaders: !toc.model.configuration.numberHeaders
                });
                app.commands.notifyCommandChanged(CommandIDs.displayNumbering);
            }
        },
        isEnabled: () => { var _a, _b; return (_b = (_a = toc.model) === null || _a === void 0 ? void 0 : _a.supportedOptions.includes('numberHeaders')) !== null && _b !== void 0 ? _b : false; },
        isToggled: () => { var _a, _b; return (_b = (_a = toc.model) === null || _a === void 0 ? void 0 : _a.configuration.numberHeaders) !== null && _b !== void 0 ? _b : false; }
    });
    app.commands.addCommand(CommandIDs.displayOutputNumbering, {
        label: trans.__('Show output headings'),
        execute: () => {
            if (toc.model) {
                toc.model.setConfiguration({
                    includeOutput: !toc.model.configuration.includeOutput
                });
            }
        },
        isEnabled: () => { var _a, _b; return (_b = (_a = toc.model) === null || _a === void 0 ? void 0 : _a.supportedOptions.includes('includeOutput')) !== null && _b !== void 0 ? _b : false; },
        isToggled: () => { var _a, _b; return (_b = (_a = toc.model) === null || _a === void 0 ? void 0 : _a.configuration.includeOutput) !== null && _b !== void 0 ? _b : false; }
    });
    app.commands.addCommand(CommandIDs.showPanel, {
        label: trans.__('Table of Contents'),
        execute: () => {
            app.shell.activateById(toc.id);
        }
    });
    function someExpanded(model) {
        return model.headings.some(h => { var _a; return !((_a = h.collapsed) !== null && _a !== void 0 ? _a : false); });
    }
    app.commands.addCommand(CommandIDs.toggleCollapse, {
        label: () => toc.model && !someExpanded(toc.model)
            ? trans.__('Expand All Headings')
            : trans.__('Collapse All Headings'),
        icon: args => args.toolbar
            ? toc.model && !someExpanded(toc.model)
                ? _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.expandAllIcon
                : _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.collapseAllIcon
            : undefined,
        execute: () => {
            if (toc.model) {
                if (someExpanded(toc.model)) {
                    toc.model.toggleCollapse({ collapsed: true });
                }
                else {
                    toc.model.toggleCollapse({ collapsed: false });
                }
            }
        },
        isEnabled: () => toc.model !== null
    });
    const tracker = new _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_2__.TableOfContentsTracker();
    if (restorer) {
        // Add the ToC widget to the application restorer:
        restorer.add(toc, '@jupyterlab/toc:plugin');
    }
    // Attempt to load plugin settings:
    let settings;
    if (settingRegistry) {
        try {
            settings = await settingRegistry.load(registry.id);
            const updateSettings = (plugin) => {
                const composite = plugin.composite;
                for (const key of [...Object.keys(configuration)]) {
                    const value = composite[key];
                    if (value !== undefined) {
                        configuration[key] = value;
                    }
                }
                if (labShell) {
                    (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_5__.toArray)(labShell.widgets('main')).forEach(widget => {
                        const model = tracker.get(widget);
                        if (model) {
                            model.setConfiguration(configuration);
                        }
                    });
                }
                else {
                    if (app.shell.currentWidget) {
                        const model = tracker.get(app.shell.currentWidget);
                        if (model) {
                            model.setConfiguration(configuration);
                        }
                    }
                }
            };
            if (settings) {
                settings.changed.connect(updateSettings);
                updateSettings(settings);
            }
        }
        catch (error) {
            console.error(`Failed to load settings for the Table of Contents extension.\n\n${error}`);
        }
    }
    // Set up the panel toolbar
    const numbering = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.CommandToolbarButton({
        commands: app.commands,
        id: CommandIDs.displayNumbering,
        args: {
            toolbar: true
        },
        label: ''
    });
    numbering.addClass('jp-toc-numberingButton');
    toc.toolbar.addItem('display-numbering', numbering);
    toc.toolbar.addItem('spacer', _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.Toolbar.createSpacerItem());
    toc.toolbar.addItem('collapse-all', new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.CommandToolbarButton({
        commands: app.commands,
        id: CommandIDs.toggleCollapse,
        args: {
            toolbar: true
        },
        label: ''
    }));
    const toolbarMenu = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.MenuSvg({ commands: app.commands });
    toolbarMenu.addItem({
        command: CommandIDs.displayH1Numbering
    });
    toolbarMenu.addItem({
        command: CommandIDs.displayOutputNumbering
    });
    const menuButton = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.ToolbarButton({
        tooltip: trans.__('More actions…'),
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.ellipsesIcon,
        actualOnClick: true,
        onClick: () => {
            const bbox = menuButton.node.getBoundingClientRect();
            toolbarMenu.open(bbox.x, bbox.bottom);
        }
    });
    toc.toolbar.addItem('submenu', menuButton);
    // Add the ToC to the left area:
    app.shell.add(toc, 'left', { rank: 10, type: 'Table of Contents' });
    // Update the ToC when the active widget changes:
    if (labShell) {
        labShell.currentChanged.connect(onConnect);
    }
    // Connect to current widget
    void app.restored.then(() => {
        onConnect();
    });
    return tracker;
    /**
     * Callback invoked when the active widget changes.
     *
     * @private
     */
    function onConnect() {
        var _a, _b;
        let widget = app.shell.currentWidget;
        if (!widget) {
            return;
        }
        let model = tracker.get(widget);
        if (!model) {
            model = (_a = tocRegistry.getModel(widget, configuration)) !== null && _a !== void 0 ? _a : null;
            if (model) {
                tracker.add(widget, model);
            }
            widget.disposed.connect(() => {
                model === null || model === void 0 ? void 0 : model.dispose();
            });
        }
        if (toc.model) {
            toc.model.collapseChanged.disconnect(onCollapseChange);
        }
        toc.model = model;
        (_b = toc.model) === null || _b === void 0 ? void 0 : _b.collapseChanged.connect(onCollapseChange);
        setToolbarButtonsState();
    }
    function setToolbarButtonsState() {
        app.commands.notifyCommandChanged(CommandIDs.displayNumbering);
        app.commands.notifyCommandChanged(CommandIDs.toggleCollapse);
    }
    function onCollapseChange() {
        app.commands.notifyCommandChanged(CommandIDs.toggleCollapse);
    }
}
/**
 * Table of contents registry plugin.
 */
const registry = {
    id: '@jupyterlab/toc-extension:registry',
    autoStart: true,
    provides: _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_2__.ITableOfContentsRegistry,
    activate: () => {
        // Create the ToC registry
        return new _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_2__.TableOfContentsRegistry();
    }
};
/**
 * Table of contents tracker plugin.
 */
const tracker = {
    id: '@jupyterlab/toc-extension:tracker',
    autoStart: true,
    provides: _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_2__.ITableOfContentsTracker,
    requires: [_jupyterlab_toc__WEBPACK_IMPORTED_MODULE_2__.ITableOfContentsRegistry],
    optional: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__.ITranslator, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__.ISettingRegistry],
    activate: activateTOC
};
/**
 * Exports.
 */
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ([registry, tracker]);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdG9jLWV4dGVuc2lvbl9saWJfaW5kZXhfanMuZjE3M2FkMWFlYzJmOGU1ZTM5MDcuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBTzhCO0FBQzhCO0FBUXRDO0FBQzZDO0FBV25DO0FBQ1M7QUFFNUM7O0dBRUc7QUFDSCxJQUFVLFVBQVUsQ0FVbkI7QUFWRCxXQUFVLFVBQVU7SUFDTCwyQkFBZ0IsR0FBRyx1QkFBdUIsQ0FBQztJQUUzQyw2QkFBa0IsR0FBRywwQkFBMEIsQ0FBQztJQUVoRCxpQ0FBc0IsR0FBRywrQkFBK0IsQ0FBQztJQUV6RCxvQkFBUyxHQUFHLGdCQUFnQixDQUFDO0lBRTdCLHlCQUFjLEdBQUcscUJBQXFCLENBQUM7QUFDdEQsQ0FBQyxFQVZTLFVBQVUsS0FBVixVQUFVLFFBVW5CO0FBRUQ7Ozs7Ozs7Ozs7O0dBV0c7QUFDSCxLQUFLLFVBQVUsV0FBVyxDQUN4QixHQUFvQixFQUNwQixXQUFxQyxFQUNyQyxVQUErQixFQUMvQixRQUFpQyxFQUNqQyxRQUEyQixFQUMzQixlQUF5QztJQUV6QyxNQUFNLEtBQUssR0FBRyxDQUFDLFVBQVUsYUFBVixVQUFVLGNBQVYsVUFBVSxHQUFJLG1FQUFjLENBQUMsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUM7SUFDaEUsSUFBSSxhQUFhLHFCQUFRLDBFQUE2QixDQUFFLENBQUM7SUFFekQseUJBQXlCO0lBQ3pCLE1BQU0sR0FBRyxHQUFHLElBQUksaUVBQW9CLENBQUMsVUFBVSxhQUFWLFVBQVUsY0FBVixVQUFVLEdBQUksU0FBUyxDQUFDLENBQUM7SUFDOUQsR0FBRyxDQUFDLEtBQUssQ0FBQyxJQUFJLEdBQUcsOERBQU8sQ0FBQztJQUN6QixHQUFHLENBQUMsS0FBSyxDQUFDLE9BQU8sR0FBRyxLQUFLLENBQUMsRUFBRSxDQUFDLG1CQUFtQixDQUFDLENBQUM7SUFDbEQsR0FBRyxD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LENBQUMsT0FBTyxDQUFDLGdCQUFnQixDQUFDLENBQUM7UUFDckQsc0JBQXNCLEVBQUUsQ0FBQztJQUMzQixDQUFDO0lBRUQsU0FBUyxzQkFBc0I7UUFDN0IsR0FBRyxDQUFDLFFBQVEsQ0FBQyxvQkFBb0IsQ0FBQyxVQUFVLENBQUMsZ0JBQWdCLENBQUMsQ0FBQztRQUMvRCxHQUFHLENBQUMsUUFBUSxDQUFDLG9CQUFvQixDQUFDLFVBQVUsQ0FBQyxjQUFjLENBQUMsQ0FBQztJQUMvRCxDQUFDO0lBRUQsU0FBUyxnQkFBZ0I7UUFDdkIsR0FBRyxDQUFDLFFBQVEsQ0FBQyxvQkFBb0IsQ0FBQyxVQUFVLENBQUMsY0FBYyxDQUFDLENBQUM7SUFDL0QsQ0FBQztBQUNILENBQUM7QUFFRDs7R0FFRztBQUNILE1BQU0sUUFBUSxHQUFvRDtJQUNoRSxFQUFFLEVBQUUsb0NBQW9DO0lBQ3hDLFNBQVMsRUFBRSxJQUFJO0lBQ2YsUUFBUSxFQUFFLHFFQUF3QjtJQUNsQyxRQUFRLEVBQUUsR0FBNkIsRUFBRTtRQUN2QywwQkFBMEI7UUFDMUIsT0FBTyxJQUFJLG9FQUF1QixFQUFFLENBQUM7SUFDdkMsQ0FBQztDQUNGLENBQUM7QUFFRjs7R0FFRztBQUNILE1BQU0sT0FBTyxHQUFtRDtJQUM5RCxFQUFFLEVBQUUsbUNBQW1DO0lBQ3ZDLFNBQVMsRUFBRSxJQUFJO0lBQ2YsUUFBUSxFQUFFLG9FQUF1QjtJQUNqQyxRQUFRLEVBQUUsQ0FBQyxxRUFBd0IsQ0FBQztJQUNwQyxRQUFRLEVBQUUsQ0FBQyxnRUFBVyxFQUFFLG9FQUFlLEVBQUUsOERBQVMsRUFBRSx5RUFBZ0IsQ0FBQztJQUNyRSxRQUFRLEVBQUUsV0FBVztDQUN0QixDQUFDO0FBRUY7O0dBRUc7QUFDSCxpRUFBZSxDQUFDLFFBQVEsRUFBRSxPQUFPLENBQUMsRUFBQyIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy90b2MtZXh0ZW5zaW9uL3NyYy9pbmRleC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSB0b2MtZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSUxhYlNoZWxsLFxuICBJTGF5b3V0UmVzdG9yZXIsXG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7IElTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHtcbiAgSVRhYmxlT2ZDb250ZW50c1JlZ2lzdHJ5LFxuICBJVGFibGVPZkNvbnRlbnRzVHJhY2tlcixcbiAgVGFibGVPZkNvbnRlbnRzLFxuICBUYWJsZU9mQ29udGVudHNQYW5lbCxcbiAgVGFibGVPZkNvbnRlbnRzUmVnaXN0cnksXG4gIFRhYmxlT2ZDb250ZW50c1RyYWNrZXJcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvdG9jJztcbmltcG9ydCB7IElUcmFuc2xhdG9yLCBudWxsVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7XG4gIGNvbGxhcHNlQWxsSWNvbixcbiAgQ29tbWFuZFRvb2xiYXJCdXR0b24sXG4gIGVsbGlwc2VzSWNvbixcbiAgZXhwYW5kQWxsSWNvbixcbiAgTWVudVN2ZyxcbiAgbnVtYmVyaW5nSWNvbixcbiAgdG9jSWNvbixcbiAgVG9vbGJhcixcbiAgVG9vbGJhckJ1dHRvblxufSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IHRvQXJyYXkgfSBmcm9tICdAbHVtaW5vL2FsZ29yaXRobSc7XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIGNvbW1hbmQgSURzIG9mIHRhYmxlIG9mIGNvbnRlbnRzIHBsdWdpbi5cbiAqL1xubmFtZXNwYWNlIENvbW1hbmRJRHMge1xuICBleHBvcnQgY29uc3QgZGlzcGxheU51bWJlcmluZyA9ICd0b2M6ZGlzcGxheS1udW1iZXJpbmcnO1xuXG4gIGV4cG9ydCBjb25zdCBkaXNwbGF5SDFOdW1iZXJpbmcgPSAndG9jOmRpc3BsYXktaDEtbnVtYmVyaW5nJztcblxuICBleHBvcnQgY29uc3QgZGlzcGxheU91dHB1dE51bWJlcmluZyA9ICd0b2M6ZGlzcGxheS1vdXRwdXRzLW51bWJlcmluZyc7XG5cbiAgZXhwb3J0IGNvbnN0IHNob3dQYW5lbCA9ICd0b2M6c2hvdy1wYW5lbCc7XG5cbiAgZXhwb3J0IGNvbnN0IHRvZ2dsZUNvbGxhcHNlID0gJ3RvYzp0b2dnbGUtY29sbGFwc2UnO1xufVxuXG4vKipcbiAqIEFjdGl2YXRlcyB0aGUgVG9DIGV4dGVuc2lvbi5cbiAqXG4gKiBAcHJpdmF0ZVxuICogQHBhcmFtIGFwcCAtIEp1cHl0ZXIgYXBwbGljYXRpb25cbiAqIEBwYXJhbSByZWdpc3RyeSAtIFRhYmxlIG9mIGNvbnRlbnRzIHJlZ2lzdHJ5XG4gKiBAcGFyYW0gdHJhbnNsYXRvciAtIHRyYW5zbGF0b3JcbiAqIEBwYXJhbSByZXN0b3JlciAtIGFwcGxpY2F0aW9uIGxheW91dCByZXN0b3JlclxuICogQHBhcmFtIGxhYlNoZWxsIC0gSnVweXRlciBsYWIgc2hlbGxcbiAqIEBwYXJhbSBzZXR0aW5nUmVnaXN0cnkgLSBzZXR0aW5nIHJlZ2lzdHJ5XG4gKiBAcmV0dXJucyB0YWJsZSBvZiBjb250ZW50cyByZWdpc3RyeVxuICovXG5hc3luYyBmdW5jdGlvbiBhY3RpdmF0ZVRPQyhcbiAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gIHRvY1JlZ2lzdHJ5OiBJVGFibGVPZkNvbnRlbnRzUmVnaXN0cnksXG4gIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvciB8IG51bGwsXG4gIHJlc3RvcmVyPzogSUxheW91dFJlc3RvcmVyIHwgbnVsbCxcbiAgbGFiU2hlbGw/OiBJTGFiU2hlbGwgfCBudWxsLFxuICBzZXR0aW5nUmVnaXN0cnk/OiBJU2V0dGluZ1JlZ2lzdHJ5IHwgbnVsbFxuKTogUHJvbWlzZTxJVGFibGVPZkNvbnRlbnRzVHJhY2tlcj4ge1xuICBjb25zdCB0cmFucyA9ICh0cmFuc2xhdG9yID8/IG51bGxUcmFuc2xhdG9yKS5sb2FkKCdqdXB5dGVybGFiJyk7XG4gIGxldCBjb25maWd1cmF0aW9uID0geyAuLi5UYWJsZU9mQ29udGVudHMuZGVmYXVsdENvbmZpZyB9O1xuXG4gIC8vIENyZWF0ZSB0aGUgVG9DIHdpZGdldDpcbiAgY29uc3QgdG9jID0gbmV3IFRhYmxlT2ZDb250ZW50c1BhbmVsKHRyYW5zbGF0b3IgPz8gdW5kZWZpbmVkKTtcbiAgdG9jLnRpdGxlLmljb24gPSB0b2NJY29uO1xuICB0b2MudGl0bGUuY2FwdGlvbiA9IHRyYW5zLl9fKCdUYWJsZSBvZiBDb250ZW50cycpO1xuICB0b2MuaWQgPSAndGFibGUtb2YtY29udGVudHMnO1xuICB0b2Mubm9kZS5zZXRBdHRyaWJ1dGUoJ3JvbGUnLCAncmVnaW9uJyk7XG4gIHRvYy5ub2RlLnNldEF0dHJpYnV0ZSgnYXJpYS1sYWJlbCcsIHRyYW5zLl9fKCdUYWJsZSBvZiBDb250ZW50cyBzZWN0aW9uJykpO1xuXG4gIGFwcC5jb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuZGlzcGxheUgxTnVtYmVyaW5nLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdTaG93IGZpcnN0LWxldmVsIGhlYWRpbmcgbnVtYmVyJyksXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgaWYgKHRvYy5tb2RlbCkge1xuICAgICAgICB0b2MubW9kZWwuc2V0Q29uZmlndXJhdGlvbih7XG4gICAgICAgICAgbnVtYmVyaW5nSDE6ICF0b2MubW9kZWwuY29uZmlndXJhdGlvbi5udW1iZXJpbmdIMVxuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9LFxuICAgIGlzRW5hYmxlZDogKCkgPT5cbiAgICAgIHRvYy5tb2RlbD8uc3VwcG9ydGVkT3B0aW9ucy5pbmNsdWRlcygnbnVtYmVyaW5nSDEnKSA/PyBmYWxzZSxcbiAgICBpc1RvZ2dsZWQ6ICgpID0+IHRvYy5tb2RlbD8uY29uZmlndXJhdGlvbi5udW1iZXJpbmdIMSA/PyBmYWxzZVxuICB9KTtcblxuICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmRpc3BsYXlOdW1iZXJpbmcsIHtcbiAgICBsYWJlbDogdHJhbnMuX18oJ1Nob3cgaGVhZGluZyBudW1iZXIgaW4gdGhlIGRvY3VtZW50JyksXG4gICAgaWNvbjogYXJncyA9PiAoYXJncy50b29sYmFyID8gbnVtYmVyaW5nSWNvbiA6IHVuZGVmaW5lZCksXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgaWYgKHRvYy5tb2RlbCkge1xuICAgICAgICB0b2MubW9kZWwuc2V0Q29uZmlndXJhdGlvbih7XG4gICAgICAgICAgbnVtYmVySGVhZGVyczogIXRvYy5tb2RlbC5jb25maWd1cmF0aW9uLm51bWJlckhlYWRlcnNcbiAgICAgICAgfSk7XG4gICAgICAgIGFwcC5jb21tYW5kcy5ub3RpZnlDb21tYW5kQ2hhbmdlZChDb21tYW5kSURzLmRpc3BsYXlOdW1iZXJpbmcpO1xuICAgICAgfVxuICAgIH0sXG4gICAgaXNFbmFibGVkOiAoKSA9PlxuICAgICAgdG9jLm1vZGVsPy5zdXBwb3J0ZWRPcHRpb25zLmluY2x1ZGVzKCdudW1iZXJIZWFkZXJzJykgPz8gZmFsc2UsXG4gICAgaXNUb2dnbGVkOiAoKSA9PiB0b2MubW9kZWw/LmNvbmZpZ3VyYXRpb24ubnVtYmVySGVhZGVycyA/PyBmYWxzZVxuICB9KTtcblxuICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmRpc3BsYXlPdXRwdXROdW1iZXJpbmcsIHtcbiAgICBsYWJlbDogdHJhbnMuX18oJ1Nob3cgb3V0cHV0IGhlYWRpbmdzJyksXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgaWYgKHRvYy5tb2RlbCkge1xuICAgICAgICB0b2MubW9kZWwuc2V0Q29uZmlndXJhdGlvbih7XG4gICAgICAgICAgaW5jbHVkZU91dHB1dDogIXRvYy5tb2RlbC5jb25maWd1cmF0aW9uLmluY2x1ZGVPdXRwdXRcbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfSxcbiAgICBpc0VuYWJsZWQ6ICgpID0+XG4gICAgICB0b2MubW9kZWw/LnN1cHBvcnRlZE9wdGlvbnMuaW5jbHVkZXMoJ2luY2x1ZGVPdXRwdXQnKSA/PyBmYWxzZSxcbiAgICBpc1RvZ2dsZWQ6ICgpID0+IHRvYy5tb2RlbD8uY29uZmlndXJhdGlvbi5pbmNsdWRlT3V0cHV0ID8/IGZhbHNlXG4gIH0pO1xuXG4gIGFwcC5jb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuc2hvd1BhbmVsLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdUYWJsZSBvZiBDb250ZW50cycpLFxuICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgIGFwcC5zaGVsbC5hY3RpdmF0ZUJ5SWQodG9jLmlkKTtcbiAgICB9XG4gIH0pO1xuXG4gIGZ1bmN0aW9uIHNvbWVFeHBhbmRlZChtb2RlbDogVGFibGVPZkNvbnRlbnRzLk1vZGVsKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIG1vZGVsLmhlYWRpbmdzLnNvbWUoaCA9PiAhKGguY29sbGFwc2VkID8/IGZhbHNlKSk7XG4gIH1cblxuICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnRvZ2dsZUNvbGxhcHNlLCB7XG4gICAgbGFiZWw6ICgpID0+XG4gICAgICB0b2MubW9kZWwgJiYgIXNvbWVFeHBhbmRlZCh0b2MubW9kZWwpXG4gICAgICAgID8gdHJhbnMuX18oJ0V4cGFuZCBBbGwgSGVhZGluZ3MnKVxuICAgICAgICA6IHRyYW5zLl9fKCdDb2xsYXBzZSBBbGwgSGVhZGluZ3MnKSxcbiAgICBpY29uOiBhcmdzID0+XG4gICAgICBhcmdzLnRvb2xiYXJcbiAgICAgICAgPyB0b2MubW9kZWwgJiYgIXNvbWVFeHBhbmRlZCh0b2MubW9kZWwpXG4gICAgICAgICAgPyBleHBhbmRBbGxJY29uXG4gICAgICAgICAgOiBjb2xsYXBzZUFsbEljb25cbiAgICAgICAgOiB1bmRlZmluZWQsXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgaWYgKHRvYy5tb2RlbCkge1xuICAgICAgICBpZiAoc29tZUV4cGFuZGVkKHRvYy5tb2RlbCkpIHtcbiAgICAgICAgICB0b2MubW9kZWwudG9nZ2xlQ29sbGFwc2UoeyBjb2xsYXBzZWQ6IHRydWUgfSk7XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgdG9jLm1vZGVsLnRvZ2dsZUNvbGxhcHNlKHsgY29sbGFwc2VkOiBmYWxzZSB9KTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH0sXG4gICAgaXNFbmFibGVkOiAoKSA9PiB0b2MubW9kZWwgIT09IG51bGxcbiAgfSk7XG5cbiAgY29uc3QgdHJhY2tlciA9IG5ldyBUYWJsZU9mQ29udGVudHNUcmFja2VyKCk7XG5cbiAgaWYgKHJlc3RvcmVyKSB7XG4gICAgLy8gQWRkIHRoZSBUb0Mgd2lkZ2V0IHRvIHRoZSBhcHBsaWNhdGlvbiByZXN0b3JlcjpcbiAgICByZXN0b3Jlci5hZGQodG9jLCAnQGp1cHl0ZXJsYWIvdG9jOnBsdWdpbicpO1xuICB9XG5cbiAgLy8gQXR0ZW1wdCB0byBsb2FkIHBsdWdpbiBzZXR0aW5nczpcbiAgbGV0IHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LklTZXR0aW5ncyB8IHVuZGVmaW5lZDtcbiAgaWYgKHNldHRpbmdSZWdpc3RyeSkge1xuICAgIHRyeSB7XG4gICAgICBzZXR0aW5ncyA9IGF3YWl0IHNldHRpbmdSZWdpc3RyeS5sb2FkKHJlZ2lzdHJ5LmlkKTtcbiAgICAgIGNvbnN0IHVwZGF0ZVNldHRpbmdzID0gKHBsdWdpbjogSVNldHRpbmdSZWdpc3RyeS5JU2V0dGluZ3MpID0+IHtcbiAgICAgICAgY29uc3QgY29tcG9zaXRlID0gcGx1Z2luLmNvbXBvc2l0ZTtcbiAgICAgICAgZm9yIChjb25zdCBrZXkgb2YgWy4uLk9iamVjdC5rZXlzKGNvbmZpZ3VyYXRpb24pXSkge1xuICAgICAgICAgIGNvbnN0IHZhbHVlID0gY29tcG9zaXRlW2tleV0gYXMgYW55O1xuICAgICAgICAgIGlmICh2YWx1ZSAhPT0gdW5kZWZpbmVkKSB7XG4gICAgICAgICAgICBjb25maWd1cmF0aW9uW2tleV0gPSB2YWx1ZTtcbiAgICAgICAgICB9XG4gICAgICAgIH1cblxuICAgICAgICBpZiAobGFiU2hlbGwpIHtcbiAgICAgICAgICB0b0FycmF5KGxhYlNoZWxsLndpZGdldHMoJ21haW4nKSkuZm9yRWFjaCh3aWRnZXQgPT4ge1xuICAgICAgICAgICAgY29uc3QgbW9kZWwgPSB0cmFja2VyLmdldCh3aWRnZXQpO1xuICAgICAgICAgICAgaWYgKG1vZGVsKSB7XG4gICAgICAgICAgICAgIG1vZGVsLnNldENvbmZpZ3VyYXRpb24oY29uZmlndXJhdGlvbik7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgfSk7XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgaWYgKGFwcC5zaGVsbC5jdXJyZW50V2lkZ2V0KSB7XG4gICAgICAgICAgICBjb25zdCBtb2RlbCA9IHRyYWNrZXIuZ2V0KGFwcC5zaGVsbC5jdXJyZW50V2lkZ2V0KTtcbiAgICAgICAgICAgIGlmIChtb2RlbCkge1xuICAgICAgICAgICAgICBtb2RlbC5zZXRDb25maWd1cmF0aW9uKGNvbmZpZ3VyYXRpb24pO1xuICAgICAgICAgICAgfVxuICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgfTtcbiAgICAgIGlmIChzZXR0aW5ncykge1xuICAgICAgICBzZXR0aW5ncy5jaGFuZ2VkLmNvbm5lY3QodXBkYXRlU2V0dGluZ3MpO1xuICAgICAgICB1cGRhdGVTZXR0aW5ncyhzZXR0aW5ncyk7XG4gICAgICB9XG4gICAgfSBjYXRjaCAoZXJyb3IpIHtcbiAgICAgIGNvbnNvbGUuZXJyb3IoXG4gICAgICAgIGBGYWlsZWQgdG8gbG9hZCBzZXR0aW5ncyBmb3IgdGhlIFRhYmxlIG9mIENvbnRlbnRzIGV4dGVuc2lvbi5cXG5cXG4ke2Vycm9yfWBcbiAgICAgICk7XG4gICAgfVxuICB9XG5cbiAgLy8gU2V0IHVwIHRoZSBwYW5lbCB0b29sYmFyXG4gIGNvbnN0IG51bWJlcmluZyA9IG5ldyBDb21tYW5kVG9vbGJhckJ1dHRvbih7XG4gICAgY29tbWFuZHM6IGFwcC5jb21tYW5kcyxcbiAgICBpZDogQ29tbWFuZElEcy5kaXNwbGF5TnVtYmVyaW5nLFxuICAgIGFyZ3M6IHtcbiAgICAgIHRvb2xiYXI6IHRydWVcbiAgICB9LFxuICAgIGxhYmVsOiAnJ1xuICB9KTtcbiAgbnVtYmVyaW5nLmFkZENsYXNzKCdqcC10b2MtbnVtYmVyaW5nQnV0dG9uJyk7XG4gIHRvYy50b29sYmFyLmFkZEl0ZW0oJ2Rpc3BsYXktbnVtYmVyaW5nJywgbnVtYmVyaW5nKTtcblxuICB0b2MudG9vbGJhci5hZGRJdGVtKCdzcGFjZXInLCBUb29sYmFyLmNyZWF0ZVNwYWNlckl0ZW0oKSk7XG5cbiAgdG9jLnRvb2xiYXIuYWRkSXRlbShcbiAgICAnY29sbGFwc2UtYWxsJyxcbiAgICBuZXcgQ29tbWFuZFRvb2xiYXJCdXR0b24oe1xuICAgICAgY29tbWFuZHM6IGFwcC5jb21tYW5kcyxcbiAgICAgIGlkOiBDb21tYW5kSURzLnRvZ2dsZUNvbGxhcHNlLFxuICAgICAgYXJnczoge1xuICAgICAgICB0b29sYmFyOiB0cnVlXG4gICAgICB9LFxuICAgICAgbGFiZWw6ICcnXG4gICAgfSlcbiAgKTtcblxuICBjb25zdCB0b29sYmFyTWVudSA9IG5ldyBNZW51U3ZnKHsgY29tbWFuZHM6IGFwcC5jb21tYW5kcyB9KTtcbiAgdG9vbGJhck1lbnUuYWRkSXRlbSh7XG4gICAgY29tbWFuZDogQ29tbWFuZElEcy5kaXNwbGF5SDFOdW1iZXJpbmdcbiAgfSk7XG4gIHRvb2xiYXJNZW51LmFkZEl0ZW0oe1xuICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMuZGlzcGxheU91dHB1dE51bWJlcmluZ1xuICB9KTtcbiAgY29uc3QgbWVudUJ1dHRvbiA9IG5ldyBUb29sYmFyQnV0dG9uKHtcbiAgICB0b29sdGlwOiB0cmFucy5fXygnTW9yZSBhY3Rpb25z4oCmJyksXG4gICAgaWNvbjogZWxsaXBzZXNJY29uLFxuICAgIGFjdHVhbE9uQ2xpY2s6IHRydWUsXG4gICAgb25DbGljazogKCkgPT4ge1xuICAgICAgY29uc3QgYmJveCA9IG1lbnVCdXR0b24ubm9kZS5nZXRCb3VuZGluZ0NsaWVudFJlY3QoKTtcbiAgICAgIHRvb2xiYXJNZW51Lm9wZW4oYmJveC54LCBiYm94LmJvdHRvbSk7XG4gICAgfVxuICB9KTtcbiAgdG9jLnRvb2xiYXIuYWRkSXRlbSgnc3VibWVudScsIG1lbnVCdXR0b24pO1xuXG4gIC8vIEFkZCB0aGUgVG9DIHRvIHRoZSBsZWZ0IGFyZWE6XG4gIGFwcC5zaGVsbC5hZGQodG9jLCAnbGVmdCcsIHsgcmFuazogMTAsIHR5cGU6ICdUYWJsZSBvZiBDb250ZW50cycgfSk7XG5cbiAgLy8gVXBkYXRlIHRoZSBUb0Mgd2hlbiB0aGUgYWN0aXZlIHdpZGdldCBjaGFuZ2VzOlxuICBpZiAobGFiU2hlbGwpIHtcbiAgICBsYWJTaGVsbC5jdXJyZW50Q2hhbmdlZC5jb25uZWN0KG9uQ29ubmVjdCk7XG4gIH1cblxuICAvLyBDb25uZWN0IHRvIGN1cnJlbnQgd2lkZ2V0XG4gIHZvaWQgYXBwLnJlc3RvcmVkLnRoZW4oKCkgPT4ge1xuICAgIG9uQ29ubmVjdCgpO1xuICB9KTtcblxuICByZXR1cm4gdHJhY2tlcjtcblxuICAvKipcbiAgICogQ2FsbGJhY2sgaW52b2tlZCB3aGVuIHRoZSBhY3RpdmUgd2lkZ2V0IGNoYW5nZXMuXG4gICAqXG4gICAqIEBwcml2YXRlXG4gICAqL1xuICBmdW5jdGlvbiBvbkNvbm5lY3QoKSB7XG4gICAgbGV0IHdpZGdldCA9IGFwcC5zaGVsbC5jdXJyZW50V2lkZ2V0O1xuICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGxldCBtb2RlbCA9IHRyYWNrZXIuZ2V0KHdpZGdldCk7XG4gICAgaWYgKCFtb2RlbCkge1xuICAgICAgbW9kZWwgPSB0b2NSZWdpc3RyeS5nZXRNb2RlbCh3aWRnZXQsIGNvbmZpZ3VyYXRpb24pID8/IG51bGw7XG4gICAgICBpZiAobW9kZWwpIHtcbiAgICAgICAgdHJhY2tlci5hZGQod2lkZ2V0LCBtb2RlbCk7XG4gICAgICB9XG5cbiAgICAgIHdpZGdldC5kaXNwb3NlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgICAgbW9kZWw/LmRpc3Bvc2UoKTtcbiAgICAgIH0pO1xuICAgIH1cblxuICAgIGlmICh0b2MubW9kZWwpIHtcbiAgICAgIHRvYy5tb2RlbC5jb2xsYXBzZUNoYW5nZWQuZGlzY29ubmVjdChvbkNvbGxhcHNlQ2hhbmdlKTtcbiAgICB9XG5cbiAgICB0b2MubW9kZWwgPSBtb2RlbDtcbiAgICB0b2MubW9kZWw/LmNvbGxhcHNlQ2hhbmdlZC5jb25uZWN0KG9uQ29sbGFwc2VDaGFuZ2UpO1xuICAgIHNldFRvb2xiYXJCdXR0b25zU3RhdGUoKTtcbiAgfVxuXG4gIGZ1bmN0aW9uIHNldFRvb2xiYXJCdXR0b25zU3RhdGUoKSB7XG4gICAgYXBwLmNvbW1hbmRzLm5vdGlmeUNvbW1hbmRDaGFuZ2VkKENvbW1hbmRJRHMuZGlzcGxheU51bWJlcmluZyk7XG4gICAgYXBwLmNvbW1hbmRzLm5vdGlmeUNvbW1hbmRDaGFuZ2VkKENvbW1hbmRJRHMudG9nZ2xlQ29sbGFwc2UpO1xuICB9XG5cbiAgZnVuY3Rpb24gb25Db2xsYXBzZUNoYW5nZSgpIHtcbiAgICBhcHAuY29tbWFuZHMubm90aWZ5Q29tbWFuZENoYW5nZWQoQ29tbWFuZElEcy50b2dnbGVDb2xsYXBzZSk7XG4gIH1cbn1cblxuLyoqXG4gKiBUYWJsZSBvZiBjb250ZW50cyByZWdpc3RyeSBwbHVnaW4uXG4gKi9cbmNvbnN0IHJlZ2lzdHJ5OiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SVRhYmxlT2ZDb250ZW50c1JlZ2lzdHJ5PiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi90b2MtZXh0ZW5zaW9uOnJlZ2lzdHJ5JyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBwcm92aWRlczogSVRhYmxlT2ZDb250ZW50c1JlZ2lzdHJ5LFxuICBhY3RpdmF0ZTogKCk6IElUYWJsZU9mQ29udGVudHNSZWdpc3RyeSA9PiB7XG4gICAgLy8gQ3JlYXRlIHRoZSBUb0MgcmVnaXN0cnlcbiAgICByZXR1cm4gbmV3IFRhYmxlT2ZDb250ZW50c1JlZ2lzdHJ5KCk7XG4gIH1cbn07XG5cbi8qKlxuICogVGFibGUgb2YgY29udGVudHMgdHJhY2tlciBwbHVnaW4uXG4gKi9cbmNvbnN0IHRyYWNrZXI6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJVGFibGVPZkNvbnRlbnRzVHJhY2tlcj4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvdG9jLWV4dGVuc2lvbjp0cmFja2VyJyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBwcm92aWRlczogSVRhYmxlT2ZDb250ZW50c1RyYWNrZXIsXG4gIHJlcXVpcmVzOiBbSVRhYmxlT2ZDb250ZW50c1JlZ2lzdHJ5XSxcbiAgb3B0aW9uYWw6IFtJVHJhbnNsYXRvciwgSUxheW91dFJlc3RvcmVyLCBJTGFiU2hlbGwsIElTZXR0aW5nUmVnaXN0cnldLFxuICBhY3RpdmF0ZTogYWN0aXZhdGVUT0Ncbn07XG5cbi8qKlxuICogRXhwb3J0cy5cbiAqL1xuZXhwb3J0IGRlZmF1bHQgW3JlZ2lzdHJ5LCB0cmFja2VyXTtcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==