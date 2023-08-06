"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_application-extension_lib_index_js"],{

/***/ "../../packages/application-extension/lib/index.js":
/*!*********************************************************!*\
  !*** ../../packages/application-extension/lib/index.js ***!
  \*********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "DEFAULT_CONTEXT_ITEM_RANK": () => (/* binding */ DEFAULT_CONTEXT_ITEM_RANK),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_property_inspector__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/property-inspector */ "webpack/sharing/consume/default/@jupyterlab/property-inspector/@jupyterlab/property-inspector");
/* harmony import */ var _jupyterlab_property_inspector__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_property_inspector__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/statedb */ "webpack/sharing/consume/default/@jupyterlab/statedb/@jupyterlab/statedb");
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _lumino_commands__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @lumino/commands */ "webpack/sharing/consume/default/@lumino/commands/@lumino/commands");
/* harmony import */ var _lumino_commands__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(_lumino_commands__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_12__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_13___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_13__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_14___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_14__);
/* harmony import */ var _topbar__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! ./topbar */ "../../packages/application-extension/lib/topbar.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module application-extension
 */
















/**
 * Default context menu item rank
 */
const DEFAULT_CONTEXT_ITEM_RANK = 100;
/**
 * The command IDs used by the application plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.activateNextTab = 'application:activate-next-tab';
    CommandIDs.activatePreviousTab = 'application:activate-previous-tab';
    CommandIDs.activateNextTabBar = 'application:activate-next-tab-bar';
    CommandIDs.activatePreviousTabBar = 'application:activate-previous-tab-bar';
    CommandIDs.close = 'application:close';
    CommandIDs.closeOtherTabs = 'application:close-other-tabs';
    CommandIDs.closeRightTabs = 'application:close-right-tabs';
    CommandIDs.closeAll = 'application:close-all';
    CommandIDs.setMode = 'application:set-mode';
    CommandIDs.showPropertyPanel = 'property-inspector:show-panel';
    CommandIDs.resetLayout = 'application:reset-layout';
    CommandIDs.toggleHeader = 'application:toggle-header';
    CommandIDs.toggleMode = 'application:toggle-mode';
    CommandIDs.toggleLeftArea = 'application:toggle-left-area';
    CommandIDs.toggleRightArea = 'application:toggle-right-area';
    CommandIDs.toggleSideTabBar = 'application:toggle-side-tabbar';
    CommandIDs.togglePresentationMode = 'application:toggle-presentation-mode';
    CommandIDs.tree = 'router:tree';
    CommandIDs.switchSidebar = 'sidebar:switch';
})(CommandIDs || (CommandIDs = {}));
/**
 * A plugin to register the commands for the main application.
 */
const mainCommands = {
    id: '@jupyterlab/application-extension:commands',
    autoStart: true,
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    activate: (app, translator, labShell, palette) => {
        const { commands, shell } = app;
        const trans = translator.load('jupyterlab');
        const category = trans.__('Main Area');
        // Add Command to override the JLab context menu.
        commands.addCommand(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterFrontEndContextMenu.contextMenu, {
            label: trans.__('Shift+Right Click for Browser Menu'),
            isEnabled: () => false,
            execute: () => void 0
        });
        // Returns the widget associated with the most recent contextmenu event.
        const contextMenuWidget = () => {
            const test = (node) => !!node.dataset.id;
            const node = app.contextMenuHitTest(test);
            if (!node) {
                // Fall back to active widget if path cannot be obtained from event.
                return shell.currentWidget;
            }
            const matches = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__.toArray)(shell.widgets('main')).filter(widget => widget.id === node.dataset.id);
            if (matches.length < 1) {
                return shell.currentWidget;
            }
            return matches[0];
        };
        // Closes an array of widgets.
        const closeWidgets = (widgets) => {
            widgets.forEach(widget => widget.close());
        };
        // Find the tab area for a widget within a specific dock area.
        const findTab = (area, widget) => {
            switch (area.type) {
                case 'split-area': {
                    const iterator = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__.iter)(area.children);
                    let tab = null;
                    let value;
                    do {
                        value = iterator.next();
                        if (value) {
                            tab = findTab(value, widget);
                        }
                    } while (!tab && value);
                    return tab;
                }
                case 'tab-area': {
                    const { id } = widget;
                    return area.widgets.some(widget => widget.id === id) ? area : null;
                }
                default:
                    return null;
            }
        };
        // Find the tab area for a widget within the main dock area.
        const tabAreaFor = (widget) => {
            var _a;
            const layout = labShell === null || labShell === void 0 ? void 0 : labShell.saveLayout();
            const mainArea = layout === null || layout === void 0 ? void 0 : layout.mainArea;
            if (!mainArea || _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getOption('mode') !== 'multiple-document') {
                return null;
            }
            const area = (_a = mainArea.dock) === null || _a === void 0 ? void 0 : _a.main;
            if (!area) {
                return null;
            }
            return findTab(area, widget);
        };
        // Returns an array of all widgets to the right of a widget in a tab area.
        const widgetsRightOf = (widget) => {
            const { id } = widget;
            const tabArea = tabAreaFor(widget);
            const widgets = tabArea ? tabArea.widgets || [] : [];
            const index = widgets.findIndex(widget => widget.id === id);
            if (index < 0) {
                return [];
            }
            return widgets.slice(index + 1);
        };
        commands.addCommand(CommandIDs.close, {
            label: () => trans.__('Close Tab'),
            isEnabled: () => {
                const widget = contextMenuWidget();
                return !!widget && widget.title.closable;
            },
            execute: () => {
                const widget = contextMenuWidget();
                if (widget) {
                    widget.close();
                }
            }
        });
        commands.addCommand(CommandIDs.closeOtherTabs, {
            label: () => trans.__('Close All Other Tabs'),
            isEnabled: () => {
                // Ensure there are at least two widgets.
                const iterator = shell.widgets('main');
                return !!iterator.next() && !!iterator.next();
            },
            execute: () => {
                const widget = contextMenuWidget();
                if (!widget) {
                    return;
                }
                const { id } = widget;
                const otherWidgets = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__.toArray)(shell.widgets('main')).filter(widget => widget.id !== id);
                closeWidgets(otherWidgets);
            }
        });
        commands.addCommand(CommandIDs.closeRightTabs, {
            label: () => trans.__('Close Tabs to Right'),
            isEnabled: () => !!contextMenuWidget() &&
                widgetsRightOf(contextMenuWidget()).length > 0,
            execute: () => {
                const widget = contextMenuWidget();
                if (!widget) {
                    return;
                }
                closeWidgets(widgetsRightOf(widget));
            }
        });
        if (labShell) {
            commands.addCommand(CommandIDs.activateNextTab, {
                label: trans.__('Activate Next Tab'),
                execute: () => {
                    labShell.activateNextTab();
                }
            });
            commands.addCommand(CommandIDs.activatePreviousTab, {
                label: trans.__('Activate Previous Tab'),
                execute: () => {
                    labShell.activatePreviousTab();
                }
            });
            commands.addCommand(CommandIDs.activateNextTabBar, {
                label: trans.__('Activate Next Tab Bar'),
                execute: () => {
                    labShell.activateNextTabBar();
                }
            });
            commands.addCommand(CommandIDs.activatePreviousTabBar, {
                label: trans.__('Activate Previous Tab Bar'),
                execute: () => {
                    labShell.activatePreviousTabBar();
                }
            });
            commands.addCommand(CommandIDs.closeAll, {
                label: trans.__('Close All Tabs'),
                execute: () => {
                    labShell.closeAll();
                }
            });
            commands.addCommand(CommandIDs.toggleHeader, {
                label: trans.__('Show Header'),
                execute: () => {
                    if (labShell.mode === 'single-document') {
                        labShell.toggleTopInSimpleModeVisibility();
                    }
                },
                isToggled: () => labShell.isTopInSimpleModeVisible(),
                isVisible: () => labShell.mode === 'single-document'
            });
            commands.addCommand(CommandIDs.toggleLeftArea, {
                label: trans.__('Show Left Sidebar'),
                execute: () => {
                    if (labShell.leftCollapsed) {
                        labShell.expandLeft();
                    }
                    else {
                        labShell.collapseLeft();
                        if (labShell.currentWidget) {
                            labShell.activateById(labShell.currentWidget.id);
                        }
                    }
                },
                isToggled: () => !labShell.leftCollapsed,
                isEnabled: () => !labShell.isEmpty('left')
            });
            // commands.addCommand(CommandIDs.toggleRightArea, {
            //   label: trans.__('Show Right Sidebar'),
            //   execute: () => {
            //     if (labShell.rightCollapsed) {
            //       labShell.expandRight();
            //     } else {
            //       labShell.collapseRight();
            //       if (labShell.currentWidget) {
            //         labShell.activateById(labShell.currentWidget.id);
            //       }
            //     }
            //   },
            //   isToggled: () => !labShell.rightCollapsed,
            //   isEnabled: () => !labShell.isEmpty('right')
            // });
            // commands.addCommand(CommandIDs.toggleSideTabBar, {
            //   label: args =>
            //     args.side === 'right'
            //       ? trans.__('Show Right Activity Bar')
            //       : trans.__('Show Left Activity Bar'),
            //   execute: args => {
            //     if (args.side === 'right') {
            //       labShell.toggleSideTabBarVisibility('right');
            //     } else {
            //       labShell.toggleSideTabBarVisibility('left');
            //     }
            //   },
            //   isToggled: args =>
            //     args.side === 'right'
            //       ? labShell.isSideTabBarVisible('right')
            //       : labShell.isSideTabBarVisible('left'),
            //   isEnabled: args =>
            //     args.side === 'right'
            //       ? !labShell.isEmpty('right')
            //       : !labShell.isEmpty('left')
            // });
            commands.addCommand(CommandIDs.togglePresentationMode, {
                label: () => trans.__('Presentation Mode'),
                execute: () => {
                    labShell.presentationMode = !labShell.presentationMode;
                },
                isToggled: () => labShell.presentationMode,
                isVisible: () => true
            });
            commands.addCommand(CommandIDs.setMode, {
                label: args => args['mode']
                    ? trans.__('Set %1 mode.', args['mode'])
                    : trans.__('Set the layout `mode`.'),
                caption: trans.__('The layout `mode` can be "single-document" or "multiple-document".'),
                isVisible: args => {
                    const mode = args['mode'];
                    return mode === 'single-document' || mode === 'multiple-document';
                },
                execute: args => {
                    const mode = args['mode'];
                    if (mode === 'single-document' || mode === 'multiple-document') {
                        labShell.mode = mode;
                        return;
                    }
                    throw new Error(`Unsupported application shell mode: ${mode}`);
                }
            });
            // commands.addCommand(CommandIDs.toggleMode, {
            //   label: trans.__('Simple Interface'),
            //   isToggled: () => labShell.mode === 'single-document',
            //   execute: () => {
            //     const args =
            //       labShell.mode === 'multiple-document'
            //         ? { mode: 'single-document' }
            //         : { mode: 'multiple-document' };
            //     return commands.execute(CommandIDs.setMode, args);
            //   }
            // });
            commands.addCommand(CommandIDs.resetLayout, {
                label: trans.__('Reset Default Layout'),
                execute: () => {
                    // Turn off presentation mode
                    if (labShell.presentationMode) {
                        commands
                            .execute(CommandIDs.togglePresentationMode)
                            .catch(reason => {
                            console.error('Failed to undo presentation mode.', reason);
                        });
                    }
                    // Display top header
                    if (labShell.mode === 'single-document' &&
                        !labShell.isTopInSimpleModeVisible()) {
                        commands.execute(CommandIDs.toggleHeader).catch(reason => {
                            console.error('Failed to display title header.', reason);
                        });
                    }
                    // Display side tabbar
                    ['left', 'right'].forEach(side => {
                        if (!labShell.isSideTabBarVisible(side) &&
                            !labShell.isEmpty(side)) {
                            commands
                                .execute(CommandIDs.toggleSideTabBar, { side })
                                .catch(reason => {
                                console.error(`Failed to show ${side} activity bar.`, reason);
                            });
                        }
                    });
                    // Some actions are also trigger indirectly
                    // - by listening to this command execution.
                }
            });
        }
        if (palette) {
            [
                CommandIDs.activateNextTab,
                CommandIDs.activatePreviousTab,
                CommandIDs.activateNextTabBar,
                CommandIDs.activatePreviousTabBar,
                CommandIDs.close,
                CommandIDs.closeAll,
                CommandIDs.closeOtherTabs,
                CommandIDs.closeRightTabs,
                CommandIDs.toggleHeader,
                CommandIDs.toggleLeftArea,
                CommandIDs.toggleRightArea,
                CommandIDs.togglePresentationMode,
                CommandIDs.toggleMode,
                CommandIDs.resetLayout
            ].forEach(command => palette.addItem({ command, category }));
            ['right', 'left'].forEach(side => {
                palette.addItem({
                    command: CommandIDs.toggleSideTabBar,
                    category,
                    args: { side }
                });
            });
        }
    }
};
/**
 * The main extension.
 */
const main = {
    id: '@jupyterlab/application-extension:main',
    requires: [
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.IRouter,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IWindowResolver,
        _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterFrontEnd.ITreeResolver
    ],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.IConnectionLost],
    provides: _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ITreePathUpdater,
    activate: (app, router, resolver, translator, treeResolver, connectionLost) => {
        const trans = translator.load('jupyterlab');
        if (!(app instanceof _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterLab)) {
            throw new Error(`${main.id} must be activated in Notebook.`);
        }
        // These two internal state variables are used to manage the two source
        // of the tree part of the URL being updated: 1) path of the active document,
        // 2) path of the default browser if the active main area widget isn't a document.
        let _docTreePath = '';
        let _defaultBrowserTreePath = '';
        function updateTreePath(treePath) {
            // Wait for tree resolver to finish before updating the path because it use the PageConfig['treePath']
            void treeResolver.paths.then(() => {
                _defaultBrowserTreePath = treePath;
                if (!_docTreePath) {
                    const url = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getUrl({ treePath });
                    const path = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.URLExt.parse(url).pathname;
                    router.navigate(path, { skipRouting: true });
                    // Persist the new tree path to PageConfig as it is used elsewhere at runtime.
                    _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.setOption('treePath', treePath);
                }
            });
        }
        // Requiring the window resolver guarantees that the application extension
        // only loads if there is a viable window name. Otherwise, the application
        // will short-circuit and ask the user to navigate away.
        const workspace = resolver.name;
        console.debug(`Starting application in workspace: "${workspace}"`);
        // If there were errors registering plugins, tell the user.
        if (app.registerPluginErrors.length !== 0) {
            const body = (react__WEBPACK_IMPORTED_MODULE_14__.createElement("pre", null, app.registerPluginErrors.map(e => e.message).join('\n')));
            void (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)(trans.__('Error Registering Plugins'), {
                message: body
            });
        }
        // If the application shell layout is modified,
        // trigger a refresh of the commands.
        app.shell.layoutModified.connect(() => {
            app.commands.notifyCommandChanged();
        });
        // Watch the mode and update the page URL to /lab or /doc to reflect the
        // change.
        app.shell.modeChanged.connect((_, args) => {
            const url = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getUrl({ mode: args });
            const path = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.URLExt.parse(url).pathname;
            router.navigate(path, { skipRouting: true });
            // Persist this mode change to PageConfig as it is used elsewhere at runtime.
            _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.setOption('mode', args);
        });
        // Wait for tree resolver to finish before updating the path because it use the PageConfig['treePath']
        void treeResolver.paths.then(() => {
            // Watch the path of the current widget in the main area and update the page
            // URL to reflect the change.
            app.shell.currentPathChanged.connect((_, args) => {
                const maybeTreePath = args.newValue;
                const treePath = maybeTreePath || _defaultBrowserTreePath;
                const url = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getUrl({ treePath: treePath });
                const path = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.URLExt.parse(url).pathname;
                router.navigate(path, { skipRouting: true });
                // Persist the new tree path to PageConfig as it is used elsewhere at runtime.
                _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.setOption('treePath', treePath);
                _docTreePath = maybeTreePath;
            });
        });
        // If the connection to the server is lost, handle it with the
        // connection lost handler.
        connectionLost = connectionLost || _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ConnectionLost;
        app.serviceManager.connectionFailure.connect((manager, error) => connectionLost(manager, error, translator));
        const builder = app.serviceManager.builder;
        const build = () => {
            return builder
                .build()
                .then(() => {
                return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                    title: trans.__('Build Complete'),
                    body: (react__WEBPACK_IMPORTED_MODULE_14__.createElement("div", null,
                        trans.__('Build successfully completed, reload page?'),
                        react__WEBPACK_IMPORTED_MODULE_14__.createElement("br", null),
                        trans.__('You will lose any unsaved changes.'))),
                    buttons: [
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton({
                            label: trans.__('Reload Without Saving'),
                            actions: ['reload']
                        }),
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton({ label: trans.__('Save and Reload') })
                    ],
                    hasClose: true
                });
            })
                .then(({ button: { accept, actions } }) => {
                if (accept) {
                    void app.commands
                        .execute('docmanager:save')
                        .then(() => {
                        router.reload();
                    })
                        .catch(err => {
                        void (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)(trans.__('Save Failed'), {
                            message: react__WEBPACK_IMPORTED_MODULE_14__.createElement("pre", null, err.message)
                        });
                    });
                }
                else if (actions.includes('reload')) {
                    router.reload();
                }
            })
                .catch(err => {
                void (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)(trans.__('Build Failed'), {
                    message: react__WEBPACK_IMPORTED_MODULE_14__.createElement("pre", null, err.message)
                });
            });
        };
        if (builder.isAvailable && builder.shouldCheck) {
            void builder.getStatus().then(response => {
                if (response.status === 'building') {
                    return build();
                }
                if (response.status !== 'needed') {
                    return;
                }
                const body = (react__WEBPACK_IMPORTED_MODULE_14__.createElement("div", null,
                    trans.__('Notebook build is suggested:'),
                    react__WEBPACK_IMPORTED_MODULE_14__.createElement("br", null),
                    react__WEBPACK_IMPORTED_MODULE_14__.createElement("pre", null, response.message)));
                void (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                    title: trans.__('Build Recommended'),
                    body,
                    buttons: [
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton(),
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton({ label: trans.__('Build') })
                    ]
                }).then(result => (result.button.accept ? build() : undefined));
            });
        }
        return updateTreePath;
    },
    autoStart: true
};
/**
 * Plugin to build the context menu from the settings.
 */
const contextMenuPlugin = {
    id: '@jupyterlab/application-extension:context-menu',
    autoStart: true,
    requires: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4__.ISettingRegistry, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    activate: (app, settingRegistry, translator) => {
        const trans = translator.load('jupyterlab');
        function createMenu(options) {
            const menu = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__.RankedMenu(Object.assign(Object.assign({}, options), { commands: app.commands }));
            if (options.label) {
                menu.title.label = trans.__(options.label);
            }
            return menu;
        }
        // Load the context menu lately so plugins are loaded.
        app.started
            .then(() => {
            return Private.loadSettingsContextMenu(app.contextMenu, settingRegistry, createMenu, translator);
        })
            .catch(reason => {
            console.error('Failed to load context menu items from settings registry.', reason);
        });
    }
};
/**
 * Check if the application is dirty before closing the browser tab.
 */
const dirty = {
    id: '@jupyterlab/application-extension:dirty',
    autoStart: true,
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    activate: (app, translator) => {
        if (!(app instanceof _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterLab)) {
            throw new Error(`${dirty.id} must be activated in JupyterLab.`);
        }
        const trans = translator.load('jupyterlab');
        const message = trans.__('Are you sure you want to exit Notebook?\n\nAny unsaved changes will be lost.');
        // The spec for the `beforeunload` event is implemented differently by
        // the different browser vendors. Consequently, the `event.returnValue`
        // attribute needs to set in addition to a return value being returned.
        // For more information, see:
        // https://developer.mozilla.org/en/docs/Web/Events/beforeunload
        window.addEventListener('beforeunload', event => {
            if (app.status.isDirty) {
                return (event.returnValue = message);
            }
        });
    }
};
/**
 * The default layout restorer provider.
 */
const layout = {
    id: '@jupyterlab/application-extension:layout',
    requires: [_jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_5__.IStateDB, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4__.ISettingRegistry],
    optional: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    activate: (app, state, labShell, settingRegistry, translator) => {
        const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.nullTranslator).load('jupyterlab');
        const first = app.started;
        const registry = app.commands;
        const restorer = new _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.LayoutRestorer({ connector: state, first, registry });
        settingRegistry
            .load(shell.id)
            .then(settings => {
            // Add a layer of customization to support app shell mode
            const customizedLayout = settings.composite['layout'];
            void restorer.fetch().then(saved => {
                var _a, _b;
                labShell.restoreLayout(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getOption('mode'), saved, {
                    'multiple-document': (_a = customizedLayout.multiple) !== null && _a !== void 0 ? _a : {},
                    'single-document': (_b = customizedLayout.single) !== null && _b !== void 0 ? _b : {}
                });
                labShell.layoutModified.connect(() => {
                    void restorer.save(labShell.saveLayout());
                });
                settings.changed.connect(onSettingsChanged);
                // Private.activateSidebarSwitcher(app, labShell, settings, trans);
            });
        })
            .catch(reason => {
            console.error('Fail to load settings for the layout restorer.');
            console.error(reason);
        });
        return restorer;
        async function onSettingsChanged(settings) {
            if (!_lumino_coreutils__WEBPACK_IMPORTED_MODULE_10__.JSONExt.deepEqual(settings.composite['layout'], {
                single: labShell.userLayout['single-document'],
                multiple: labShell.userLayout['multiple-document']
            })) {
                const result = await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                    title: trans.__('Information'),
                    body: trans.__('User layout customization has changed. You may need to reload JupyterLab to see the changes.'),
                    buttons: [
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton(),
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton({ label: trans.__('Reload') })
                    ]
                });
                if (result.button.accept) {
                    location.reload();
                }
            }
        }
    },
    autoStart: true,
    provides: _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer
};
/**
 * The default URL router provider.
 */
const router = {
    id: '@jupyterlab/application-extension:router',
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterFrontEnd.IPaths],
    activate: (app, paths) => {
        const { commands } = app;
        const base = paths.urls.base;
        const router = new _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.Router({ base, commands });
        void app.started.then(() => {
            // Route the very first request on load.
            void router.route();
            // Route all pop state events.
            window.addEventListener('popstate', () => {
                void router.route();
            });
        });
        return router;
    },
    autoStart: true,
    provides: _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.IRouter
};
/**
 * The default tree route resolver plugin.
 */
const tree = {
    id: '@jupyterlab/application-extension:tree-resolver',
    autoStart: true,
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.IRouter],
    provides: _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterFrontEnd.ITreeResolver,
    activate: (app, router) => {
        const { commands } = app;
        const set = new _lumino_disposable__WEBPACK_IMPORTED_MODULE_12__.DisposableSet();
        const delegate = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_10__.PromiseDelegate();
        const treePattern = new RegExp('/(lab|doc)(/workspaces/[a-zA-Z0-9-_]+)?(/tree/.*)?');
        set.add(commands.addCommand(CommandIDs.tree, {
            execute: async (args) => {
                var _a;
                if (set.isDisposed) {
                    return;
                }
                const query = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.URLExt.queryStringToObject((_a = args.search) !== null && _a !== void 0 ? _a : '');
                const browser = query['file-browser-path'] || '';
                // Remove the file browser path from the query string.
                delete query['file-browser-path'];
                // Clean up artifacts immediately upon routing.
                set.dispose();
                delegate.resolve({ browser, file: _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getOption('treePath') });
            }
        }));
        set.add(router.register({ command: CommandIDs.tree, pattern: treePattern }));
        // If a route is handled by the router without the tree command being
        // invoked, resolve to `null` and clean up artifacts.
        const listener = () => {
            if (set.isDisposed) {
                return;
            }
            set.dispose();
            delegate.resolve(null);
        };
        router.routed.connect(listener);
        set.add(new _lumino_disposable__WEBPACK_IMPORTED_MODULE_12__.DisposableDelegate(() => {
            router.routed.disconnect(listener);
        }));
        return { paths: delegate.promise };
    }
};
/**
 * The default URL not found extension.
 */
const notfound = {
    id: '@jupyterlab/application-extension:notfound',
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterFrontEnd.IPaths, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.IRouter, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    activate: (_, paths, router, translator) => {
        const trans = translator.load('jupyterlab');
        const bad = paths.urls.notFound;
        if (!bad) {
            return;
        }
        const base = router.base;
        const message = trans.__('The path: %1 was not found. JupyterLab redirected to: %2', bad, base);
        // Change the URL back to the base application URL.
        router.navigate('');
        void (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showErrorMessage)(trans.__('Path Not Found'), { message });
    },
    autoStart: true
};
/**
 * Change the favicon changing based on the busy status;
 */
const busy = {
    id: '@jupyterlab/application-extension:faviconbusy',
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabStatus],
    activate: async (_, status) => {
        status.busySignal.connect((_, isBusy) => {
            const favicon = document.querySelector(`link[rel="icon"]${isBusy ? '.idle.favicon' : '.busy.favicon'}`);
            if (!favicon) {
                return;
            }
            const newFavicon = document.querySelector(`link${isBusy ? '.busy.favicon' : '.idle.favicon'}`);
            if (!newFavicon) {
                return;
            }
            // If we have the two icons with the special classes, then toggle them.
            if (favicon !== newFavicon) {
                favicon.rel = '';
                newFavicon.rel = 'icon';
                // Firefox doesn't seem to recognize just changing rel, so we also
                // reinsert the link into the DOM.
                newFavicon.parentNode.replaceChild(newFavicon, newFavicon);
            }
        });
    },
    autoStart: true
};
/**
 * The default JupyterLab application shell.
 */
const shell = {
    id: '@jupyterlab/application-extension:shell',
    optional: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4__.ISettingRegistry],
    activate: (app, settingRegistry) => {
        if (!(app.shell instanceof _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.LabShell)) {
            throw new Error(`${shell.id} did not find a LabShell instance.`);
        }
        if (settingRegistry) {
            void settingRegistry.load(shell.id).then(settings => {
                app.shell.updateConfig(settings.composite);
                settings.changed.connect(() => {
                    app.shell.updateConfig(settings.composite);
                });
            });
        }
        return app.shell;
    },
    autoStart: true,
    provides: _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell
};
/**
 * The default JupyterLab application status provider.
 */
const status = {
    id: '@jupyterlab/application-extension:status',
    activate: (app) => {
        if (!(app instanceof _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterLab)) {
            throw new Error(`${status.id} must be activated in JupyterLab.`);
        }
        return app.status;
    },
    autoStart: true,
    provides: _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabStatus
};
/**
 * The default JupyterLab application-specific information provider.
 *
 * #### Notes
 * This plugin should only be used by plugins that specifically need to access
 * JupyterLab application information, e.g., listing extensions that have been
 * loaded or deferred within JupyterLab.
 */
const info = {
    id: '@jupyterlab/application-extension:info',
    activate: (app) => {
        if (!(app instanceof _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterLab)) {
            throw new Error(`${info.id} must be activated in JupyterLab.`);
        }
        return app.info;
    },
    autoStart: true,
    provides: _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterLab.IInfo
};
/**
 * The default JupyterLab paths dictionary provider.
 */
const paths = {
    id: '@jupyterlab/apputils-extension:paths',
    activate: (app) => {
        if (!(app instanceof _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterLab)) {
            throw new Error(`${paths.id} must be activated in JupyterLab.`);
        }
        return app.paths;
    },
    autoStart: true,
    provides: _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterFrontEnd.IPaths
};
/**
 * The default property inspector provider.
 */
const propertyInspector = {
    id: '@jupyterlab/application-extension:property-inspector',
    autoStart: true,
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer],
    provides: _jupyterlab_property_inspector__WEBPACK_IMPORTED_MODULE_3__.IPropertyInspectorProvider,
    activate: (app, labshell, translator, restorer) => {
        const trans = translator.load('jupyterlab');
        const widget = new _jupyterlab_property_inspector__WEBPACK_IMPORTED_MODULE_3__.SideBarPropertyInspectorProvider(labshell, undefined, translator);
        widget.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__.buildIcon;
        widget.title.caption = trans.__('Property Inspector');
        widget.id = 'jp-property-inspector';
        labshell.add(widget, 'left', { rank: 600, type: 'Property Inspector' });
        app.commands.addCommand(CommandIDs.showPropertyPanel, {
            label: trans.__('Property Inspector'),
            execute: () => {
                labshell.activateById(widget.id);
            }
        });
        if (restorer) {
            restorer.add(widget, 'jp-property-inspector');
        }
        return widget;
    }
};
const JupyterLogo = {
    id: '@jupyterlab/application-extension:logo',
    autoStart: true,
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell],
    activate: (app, shell) => {
        const logo = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_13__.Widget();
        _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__.jupyterIcon.element({
            container: logo.node,
            elementPosition: 'center',
            margin: '2px 2px 2px 2px',
            height: 'auto',
            width: '32px'
        });
        logo.id = 'jp-MainLogo';
        shell.add(logo, 'top', { rank: 0 });
    }
};
/**
 * The simple interface mode switch in the status bar.
 */
const modeSwitchPlugin = {
    id: '@jupyterlab/application-extension:mode-switch',
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    optional: [_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__.IStatusBar, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4__.ISettingRegistry],
    activate: (app, labShell, translator, statusBar, settingRegistry) => {
        if (statusBar === null) {
            // Bail early
            return;
        }
        const trans = translator.load('jupyterlab');
        const modeSwitch = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__.Switch();
        modeSwitch.id = 'jp-single-document-mode';
        modeSwitch.valueChanged.connect((_, args) => {
            labShell.mode = args.newValue ? 'single-document' : 'multiple-document';
        });
        labShell.modeChanged.connect((_, mode) => {
            modeSwitch.value = mode === 'single-document';
        });
        if (settingRegistry) {
            const loadSettings = settingRegistry.load(shell.id);
            const updateSettings = (settings) => {
                const startMode = settings.get('startMode').composite;
                if (startMode) {
                    labShell.mode =
                        startMode === 'single' ? 'single-document' : 'multiple-document';
                }
            };
            Promise.all([loadSettings, app.restored])
                .then(([settings]) => {
                updateSettings(settings);
            })
                .catch((reason) => {
                console.error(reason.message);
            });
        }
        modeSwitch.value = labShell.mode === 'single-document';
        // Show the current file browser shortcut in its title.
        const updateModeSwitchTitle = () => {
            const binding = app.commands.keyBindings.find(b => b.command === 'application:toggle-mode');
            if (binding) {
                const ks = _lumino_commands__WEBPACK_IMPORTED_MODULE_11__.CommandRegistry.formatKeystroke(binding.keys.join(' '));
                modeSwitch.caption = trans.__('Simple Interface (%1)', ks);
            }
            else {
                modeSwitch.caption = trans.__('Simple Interface');
            }
        };
        updateModeSwitchTitle();
        app.commands.keyBindingChanged.connect(() => {
            updateModeSwitchTitle();
        });
        modeSwitch.label = trans.__('Simple');
        statusBar.registerStatusItem(modeSwitchPlugin.id, {
            item: modeSwitch,
            align: 'left',
            rank: -1
        });
    },
    autoStart: true
};
/**
 * Export the plugins as default.
 */
const plugins = [
    contextMenuPlugin,
    dirty,
    main,
    mainCommands,
    layout,
    router,
    tree,
    notfound,
    busy,
    shell,
    status,
    info,
    paths,
    propertyInspector,
    JupyterLogo,
    _topbar__WEBPACK_IMPORTED_MODULE_15__.topbar
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);
var Private;
(function (Private) {
    async function displayInformation(trans) {
        const result = await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
            title: trans.__('Information'),
            body: trans.__('Context menu customization has changed. You will need to reload Notebook to see the changes.'),
            buttons: [
                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton(),
                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton({ label: trans.__('Reload') })
            ]
        });
        if (result.button.accept) {
            location.reload();
        }
    }
    async function loadSettingsContextMenu(contextMenu, registry, menuFactory, translator) {
        var _a;
        const trans = translator.load('jupyterlab');
        const pluginId = contextMenuPlugin.id;
        let canonical = null;
        let loaded = {};
        /**
         * Populate the plugin's schema defaults.
         *
         * We keep track of disabled entries in case the plugin is loaded
         * after the menu initialization.
         */
        function populate(schema) {
            var _a, _b;
            loaded = {};
            const pluginDefaults = Object.keys(registry.plugins)
                .map(plugin => {
                var _a, _b;
                const items = (_b = (_a = registry.plugins[plugin].schema['jupyter.lab.menus']) === null || _a === void 0 ? void 0 : _a.context) !== null && _b !== void 0 ? _b : [];
                loaded[plugin] = items;
                return items;
            })
                .concat([(_b = (_a = schema['jupyter.lab.menus']) === null || _a === void 0 ? void 0 : _a.context) !== null && _b !== void 0 ? _b : []])
                .reduceRight((acc, val) => _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4__.SettingRegistry.reconcileItems(acc, val, true), []);
            // Apply default value as last step to take into account overrides.json
            // The standard default being [] as the plugin must use `jupyter.lab.menus.context`
            // to define their default value.
            schema.properties.contextMenu.default = _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4__.SettingRegistry.reconcileItems(pluginDefaults, schema.properties.contextMenu.default, true)
                // flatten one level
                .sort((a, b) => { var _a, _b; return ((_a = a.rank) !== null && _a !== void 0 ? _a : Infinity) - ((_b = b.rank) !== null && _b !== void 0 ? _b : Infinity); });
        }
        // Transform the plugin object to return different schema than the default.
        registry.transform(pluginId, {
            compose: plugin => {
                var _a, _b, _c, _d;
                // Only override the canonical schema the first time.
                if (!canonical) {
                    canonical = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_10__.JSONExt.deepCopy(plugin.schema);
                    populate(canonical);
                }
                const defaults = (_c = (_b = (_a = canonical.properties) === null || _a === void 0 ? void 0 : _a.contextMenu) === null || _b === void 0 ? void 0 : _b.default) !== null && _c !== void 0 ? _c : [];
                const user = Object.assign(Object.assign({}, plugin.data.user), { contextMenu: (_d = plugin.data.user.contextMenu) !== null && _d !== void 0 ? _d : [] });
                const composite = Object.assign(Object.assign({}, plugin.data.composite), { contextMenu: _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4__.SettingRegistry.reconcileItems(defaults, user.contextMenu, false) });
                plugin.data = { composite, user };
                return plugin;
            },
            fetch: plugin => {
                // Only override the canonical schema the first time.
                if (!canonical) {
                    canonical = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_10__.JSONExt.deepCopy(plugin.schema);
                    populate(canonical);
                }
                return {
                    data: plugin.data,
                    id: plugin.id,
                    raw: plugin.raw,
                    schema: canonical,
                    version: plugin.version
                };
            }
        });
        // Repopulate the canonical variable after the setting registry has
        // preloaded all initial plugins.
        const settings = await registry.load(pluginId);
        const contextItems = (_a = settings.composite.contextMenu) !== null && _a !== void 0 ? _a : [];
        // Create menu item for non-disabled element
        _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4__.SettingRegistry.filterDisabledItems(contextItems).forEach(item => {
            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MenuFactory.addContextItem(Object.assign({ 
                // We have to set the default rank because Lumino is sorting the visible items
                rank: DEFAULT_CONTEXT_ITEM_RANK }, item), contextMenu, menuFactory);
        });
        settings.changed.connect(() => {
            var _a;
            // As extension may change the context menu through API,
            // prompt the user to reload if the menu has been updated.
            const newItems = (_a = settings.composite.contextMenu) !== null && _a !== void 0 ? _a : [];
            if (!_lumino_coreutils__WEBPACK_IMPORTED_MODULE_10__.JSONExt.deepEqual(contextItems, newItems)) {
                void displayInformation(trans);
            }
        });
        registry.pluginChanged.connect(async (sender, plugin) => {
            var _a, _b, _c, _d;
            if (plugin !== pluginId) {
                // If the plugin changed its menu.
                const oldItems = (_a = loaded[plugin]) !== null && _a !== void 0 ? _a : [];
                const newItems = (_c = (_b = registry.plugins[plugin].schema['jupyter.lab.menus']) === null || _b === void 0 ? void 0 : _b.context) !== null && _c !== void 0 ? _c : [];
                if (!_lumino_coreutils__WEBPACK_IMPORTED_MODULE_10__.JSONExt.deepEqual(oldItems, newItems)) {
                    if (loaded[plugin]) {
                        // The plugin has changed, request the user to reload the UI
                        await displayInformation(trans);
                    }
                    else {
                        // The plugin was not yet loaded when the menu was built => update the menu
                        loaded[plugin] = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_10__.JSONExt.deepCopy(newItems);
                        // Merge potential disabled state
                        const toAdd = (_d = _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4__.SettingRegistry.reconcileItems(newItems, contextItems, false, false)) !== null && _d !== void 0 ? _d : [];
                        _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_4__.SettingRegistry.filterDisabledItems(toAdd).forEach(item => {
                            _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MenuFactory.addContextItem(Object.assign({ 
                                // We have to set the default rank because Lumino is sorting the visible items
                                rank: DEFAULT_CONTEXT_ITEM_RANK }, item), contextMenu, menuFactory);
                        });
                    }
                }
            }
        });
    }
    Private.loadSettingsContextMenu = loadSettingsContextMenu;
    function activateSidebarSwitcher(app, labShell, settings, trans) {
        // Add a command to switch a side panels's side
        app.commands.addCommand(CommandIDs.switchSidebar, {
            label: trans.__('Switch Sidebar Side'),
            execute: () => {
                // First, try to find the correct panel based on the application
                // context menu click. Bail if we don't find a sidebar for the widget.
                const contextNode = app.contextMenuHitTest(node => !!node.dataset.id);
                if (!contextNode) {
                    return;
                }
                const id = contextNode.dataset['id'];
                const leftPanel = document.getElementById('jp-left-stack');
                const node = document.getElementById(id);
                let newLayout = null;
                // Move the panel to the other side.
                if (leftPanel && node && leftPanel.contains(node)) {
                    const widget = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__.find)(labShell.widgets('left'), w => w.id === id);
                    if (widget) {
                        newLayout = labShell.move(widget, 'right');
                        labShell.activateById(widget.id);
                    }
                }
                else {
                    const widget = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_9__.find)(labShell.widgets('right'), w => w.id === id);
                    if (widget) {
                        newLayout = labShell.move(widget, 'left');
                        labShell.activateById(widget.id);
                    }
                }
                if (newLayout) {
                    settings
                        .set('layout', {
                        single: newLayout['single-document'],
                        multiple: newLayout['multiple-document']
                    })
                        .catch(reason => {
                        console.error('Failed to save user layout customization.', reason);
                    });
                }
            }
        });
        app.commands.commandExecuted.connect((registry, executed) => {
            if (executed.id === CommandIDs.resetLayout) {
                settings.remove('layout').catch(reason => {
                    console.error('Failed to remove user layout customization.', reason);
                });
            }
        });
    }
    Private.activateSidebarSwitcher = activateSidebarSwitcher;
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/application-extension/lib/topbar.js":
/*!**********************************************************!*\
  !*** ../../packages/application-extension/lib/topbar.js ***!
  \**********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "topbar": () => (/* binding */ topbar)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__);
/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */




const TOPBAR_FACTORY = 'TopBar';
/**
 * A plugin adding a toolbar to the top area.
 */
const topbar = {
    id: '@jupyterlab/application-extension:top-bar',
    autoStart: true,
    requires: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__.ISettingRegistry, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.IToolbarWidgetRegistry],
    optional: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.ITranslator],
    activate: (app, settingRegistry, toolbarRegistry, translator) => {
        const toolbar = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.Toolbar();
        toolbar.id = 'jp-top-bar';
        // Set toolbar
        (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.setToolbar)(toolbar, (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.createToolbarFactory)(toolbarRegistry, settingRegistry, TOPBAR_FACTORY, topbar.id, translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.nullTranslator), toolbar);
        app.shell.add(toolbar, 'top', { rank: 900 });
    }
};


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfYXBwbGljYXRpb24tZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy4zYjY2NzlkZTk0MjNiNWUwMmI3Ni5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQSwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBQzNEOzs7R0FHRztBQWlCOEI7QUFRSDtBQUM2QjtBQUluQjtBQUN3QztBQUNqQztBQUNJO0FBS2xCO0FBT0U7QUFDcUI7QUFLN0I7QUFDd0I7QUFDb0I7QUFDUDtBQUNqQztBQUNHO0FBRWxDOztHQUVHO0FBQ0ksTUFBTSx5QkFBeUIsR0FBRyxHQUFHLENBQUM7QUFFN0M7O0dBRUc7QUFDSCxJQUFVLFVBQVUsQ0F5Q25CO0FBekNELFdBQVUsVUFBVTtJQUNMLDBCQUFlLEdBQVcsK0JBQStCLENBQUM7SUFFMUQsOEJBQW1CLEdBQzlCLG1DQUFtQyxDQUFDO0lBRXpCLDZCQUFrQixHQUFXLG1DQUFtQyxDQUFDO0lBRWpFLGlDQUFzQixHQUNqQyx1Q0FBdUMsQ0FBQztJQUU3QixnQkFBSyxHQUFHLG1CQUFtQixDQUFDO0lBRTVCLHlCQUFjLEdBQUcsOEJBQThCLENBQUM7SUFFaEQseUJBQWMsR0FBRyw4QkFBOEIsQ0FBQztJQUVoRCxtQkFBUSxHQUFXLHVCQUF1QixDQUFDO0lBRTNDLGtCQUFPLEdBQVcsc0JBQXNCLENBQUM7SUFFekMsNEJBQWlCLEdBQVcsK0JBQStCLENBQUM7SUFFNUQsc0JBQVcsR0FBVywwQkFBMEIsQ0FBQztJQUVqRCx1QkFBWSxHQUFXLDJCQUEyQixDQUFDO0lBRW5ELHFCQUFVLEdBQVcseUJBQXlCLENBQUM7SUFFL0MseUJBQWMsR0FBVyw4QkFBOEIsQ0FBQztJQUV4RCwwQkFBZSxHQUFXLCtCQUErQixDQUFDO0lBRTFELDJCQUFnQixHQUFXLGdDQUFnQyxDQUFDO0lBRTVELGlDQUFzQixHQUNqQyxzQ0FBc0MsQ0FBQztJQUU1QixlQUFJLEdBQVcsYUFBYSxDQUFDO0lB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QUFFLHdFQUFzQixDQUFDO0lBQ3BELFFBQVEsRUFBRSxDQUFDLGdFQUFXLENBQUM7SUFDdkIsUUFBUSxFQUFFLENBQ1IsR0FBb0IsRUFDcEIsZUFBaUMsRUFDakMsZUFBdUMsRUFDdkMsVUFBOEIsRUFDOUIsRUFBRTtRQUNGLE1BQU0sT0FBTyxHQUFHLElBQUksOERBQU8sRUFBRSxDQUFDO1FBQzlCLE9BQU8sQ0FBQyxFQUFFLEdBQUcsWUFBWSxDQUFDO1FBRTFCLGNBQWM7UUFDZCxnRUFBVSxDQUNSLE9BQU8sRUFDUCwwRUFBb0IsQ0FDbEIsZUFBZSxFQUNmLGVBQWUsRUFDZixjQUFjLEVBQ2QsTUFBTSxDQUFDLEVBQUUsRUFDVCxVQUFVLGFBQVYsVUFBVSxjQUFWLFVBQVUsR0FBSSxtRUFBYyxDQUM3QixFQUNELE9BQU8sQ0FDUixDQUFDO1FBRUYsR0FBRyxDQUFDLEtBQUssQ0FBQyxHQUFHLENBQUMsT0FBTyxFQUFFLEtBQUssRUFBRSxFQUFFLElBQUksRUFBRSxHQUFHLEVBQUUsQ0FBQyxDQUFDO0lBQy9DLENBQUM7Q0FDRixDQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2FwcGxpY2F0aW9uLWV4dGVuc2lvbi9zcmMvaW5kZXgudHN4Iiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9hcHBsaWNhdGlvbi1leHRlbnNpb24vc3JjL3RvcGJhci50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBhcHBsaWNhdGlvbi1leHRlbnNpb25cbiAqL1xuXG5pbXBvcnQge1xuICBDb25uZWN0aW9uTG9zdCxcbiAgSUNvbm5lY3Rpb25Mb3N0LFxuICBJTGFiU2hlbGwsXG4gIElMYWJTdGF0dXMsXG4gIElMYXlvdXRSZXN0b3JlcixcbiAgSVJvdXRlcixcbiAgSVRyZWVQYXRoVXBkYXRlcixcbiAgSnVweXRlckZyb250RW5kLFxuICBKdXB5dGVyRnJvbnRFbmRDb250ZXh0TWVudSxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luLFxuICBKdXB5dGVyTGFiLFxuICBMYWJTaGVsbCxcbiAgTGF5b3V0UmVzdG9yZXIsXG4gIFJvdXRlclxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQge1xuICBEaWFsb2csXG4gIElDb21tYW5kUGFsZXR0ZSxcbiAgSVdpbmRvd1Jlc29sdmVyLFxuICBNZW51RmFjdG9yeSxcbiAgc2hvd0RpYWxvZyxcbiAgc2hvd0Vycm9yTWVzc2FnZVxufSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBQYWdlQ29uZmlnLCBVUkxFeHQgfSBmcm9tICdAanVweXRlcmxhYi9jb3JldXRpbHMnO1xuaW1wb3J0IHtcbiAgSVByb3BlcnR5SW5zcGVjdG9yUHJvdmlkZXIsXG4gIFNpZGVCYXJQcm9wZXJ0eUluc3BlY3RvclByb3ZpZGVyXG59IGZyb20gJ0BqdXB5dGVybGFiL3Byb3BlcnR5LWluc3BlY3Rvcic7XG5pbXBvcnQgeyBJU2V0dGluZ1JlZ2lzdHJ5LCBTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHsgSVN0YXRlREIgfSBmcm9tICdAanVweXRlcmxhYi9zdGF0ZWRiJztcbmltcG9ydCB7IElTdGF0dXNCYXIgfSBmcm9tICdAanVweXRlcmxhYi9zdGF0dXNiYXInO1xuaW1wb3J0IHtcbiAgSVRyYW5zbGF0b3IsXG4gIG51bGxUcmFuc2xhdG9yLFxuICBUcmFuc2xhdGlvbkJ1bmRsZVxufSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQge1xuICBidWlsZEljb24sXG4gIENvbnRleHRNZW51U3ZnLFxuICBqdXB5dGVySWNvbixcbiAgUmFua2VkTWVudSxcbiAgU3dpdGNoXG59IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0IHsgZmluZCwgaXRlciwgdG9BcnJheSB9IGZyb20gJ0BsdW1pbm8vYWxnb3JpdGhtJztcbmltcG9ydCB7XG4gIEpTT05FeHQsXG4gIFByb21pc2VEZWxlZ2F0ZSxcbiAgUmVhZG9ubHlQYXJ0aWFsSlNPTlZhbHVlXG59IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IENvbW1hbmRSZWdpc3RyeSB9IGZyb20gJ0BsdW1pbm8vY29tbWFuZHMnO1xuaW1wb3J0IHsgRGlzcG9zYWJsZURlbGVnYXRlLCBEaXNwb3NhYmxlU2V0IH0gZnJvbSAnQGx1bWluby9kaXNwb3NhYmxlJztcbmltcG9ydCB7IERvY2tMYXlvdXQsIERvY2tQYW5lbCwgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCAqIGFzIFJlYWN0IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7IHRvcGJhciB9IGZyb20gJy4vdG9wYmFyJztcblxuLyoqXG4gKiBEZWZhdWx0IGNvbnRleHQgbWVudSBpdGVtIHJhbmtcbiAqL1xuZXhwb3J0IGNvbnN0IERFRkFVTFRfQ09OVEVYVF9JVEVNX1JBTksgPSAxMDA7XG5cbi8qKlxuICogVGhlIGNvbW1hbmQgSURzIHVzZWQgYnkgdGhlIGFwcGxpY2F0aW9uIHBsdWdpbi5cbiAqL1xubmFtZXNwYWNlIENvbW1hbmRJRHMge1xuICBleHBvcnQgY29uc3QgYWN0aXZhdGVOZXh0VGFiOiBzdHJpbmcgPSAnYXBwbGljYXRpb246YWN0aXZhdGUtbmV4dC10YWInO1xuXG4gIGV4cG9ydCBjb25zdCBhY3RpdmF0ZVByZXZpb3VzVGFiOiBzdHJpbmcgPVxuICAgICdhcHBsaWNhdGlvbjphY3RpdmF0ZS1wcmV2aW91cy10YWInO1xuXG4gIGV4cG9ydCBjb25zdCBhY3RpdmF0ZU5leHRUYWJCYXI6IHN0cmluZyA9ICdhcHBsaWNhdGlvbjphY3RpdmF0ZS1uZXh0LXRhYi1iYXInO1xuXG4gIGV4cG9ydCBjb25zdCBhY3RpdmF0ZVByZXZpb3VzVGFiQmFyOiBzdHJpbmcgPVxuICAgICdhcHBsaWNhdGlvbjphY3RpdmF0ZS1wcmV2aW91cy10YWItYmFyJztcblxuICBleHBvcnQgY29uc3QgY2xvc2UgPSAnYXBwbGljYXRpb246Y2xvc2UnO1xuXG4gIGV4cG9ydCBjb25zdCBjbG9zZU90aGVyVGFicyA9ICdhcHBsaWNhdGlvbjpjbG9zZS1vdGhlci10YWJzJztcblxuICBleHBvcnQgY29uc3QgY2xvc2VSaWdodFRhYnMgPSAnYXBwbGljYXRpb246Y2xvc2UtcmlnaHQtdGFicyc7XG5cbiAgZXhwb3J0IGNvbnN0IGNsb3NlQWxsOiBzdHJpbmcgPSAnYXBwbGljYXRpb246Y2xvc2UtYWxsJztcblxuICBleHBvcnQgY29uc3Qgc2V0TW9kZTogc3RyaW5nID0gJ2FwcGxpY2F0aW9uOnNldC1tb2RlJztcblxuICBleHBvcnQgY29uc3Qgc2hvd1Byb3BlcnR5UGFuZWw6IHN0cmluZyA9ICdwcm9wZXJ0eS1pbnNwZWN0b3I6c2hvdy1wYW5lbCc7XG5cbiAgZXhwb3J0IGNvbnN0IHJlc2V0TGF5b3V0OiBzdHJpbmcgPSAnYXBwbGljYXRpb246cmVzZXQtbGF5b3V0JztcblxuICBleHBvcnQgY29uc3QgdG9nZ2xlSGVhZGVyOiBzdHJpbmcgPSAnYXBwbGljYXRpb246dG9nZ2xlLWhlYWRlcic7XG5cbiAgZXhwb3J0IGNvbnN0IHRvZ2dsZU1vZGU6IHN0cmluZyA9ICdhcHBsaWNhdGlvbjp0b2dnbGUtbW9kZSc7XG5cbiAgZXhwb3J0IGNvbnN0IHRvZ2dsZUxlZnRBcmVhOiBzdHJpbmcgPSAnYXBwbGljYXRpb246dG9nZ2xlLWxlZnQtYXJlYSc7XG5cbiAgZXhwb3J0IGNvbnN0IHRvZ2dsZVJpZ2h0QXJlYTogc3RyaW5nID0gJ2FwcGxpY2F0aW9uOnRvZ2dsZS1yaWdodC1hcmVhJztcblxuICBleHBvcnQgY29uc3QgdG9nZ2xlU2lkZVRhYkJhcjogc3RyaW5nID0gJ2FwcGxpY2F0aW9uOnRvZ2dsZS1zaWRlLXRhYmJhcic7XG5cbiAgZXhwb3J0IGNvbnN0IHRvZ2dsZVByZXNlbnRhdGlvbk1vZGU6IHN0cmluZyA9XG4gICAgJ2FwcGxpY2F0aW9uOnRvZ2dsZS1wcmVzZW50YXRpb24tbW9kZSc7XG5cbiAgZXhwb3J0IGNvbnN0IHRyZWU6IHN0cmluZyA9ICdyb3V0ZXI6dHJlZSc7XG5cbiAgZXhwb3J0IGNvbnN0IHN3aXRjaFNpZGViYXIgPSAnc2lkZWJhcjpzd2l0Y2gnO1xufVxuXG4vKipcbiAqIEEgcGx1Z2luIHRvIHJlZ2lzdGVyIHRoZSBjb21tYW5kcyBmb3IgdGhlIG1haW4gYXBwbGljYXRpb24uXG4gKi9cbmNvbnN0IG1haW5Db21tYW5kczogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLWV4dGVuc2lvbjpjb21tYW5kcycsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcmVxdWlyZXM6IFtJVHJhbnNsYXRvcl0sXG4gIG9wdGlvbmFsOiBbSUxhYlNoZWxsLCBJQ29tbWFuZFBhbGV0dGVdLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICAgIGxhYlNoZWxsOiBJTGFiU2hlbGwgfCBudWxsLFxuICAgIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSB8IG51bGxcbiAgKSA9PiB7XG4gICAgY29uc3QgeyBjb21tYW5kcywgc2hlbGwgfSA9IGFwcDtcbiAgICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IGNhdGVnb3J5ID0gdHJhbnMuX18oJ01haW4gQXJlYScpO1xuXG4gICAgLy8gQWRkIENvbW1hbmQgdG8gb3ZlcnJpZGUgdGhlIEpMYWIgY29udGV4dCBtZW51LlxuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoSnVweXRlckZyb250RW5kQ29udGV4dE1lbnUuY29udGV4dE1lbnUsIHtcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnU2hpZnQrUmlnaHQgQ2xpY2sgZm9yIEJyb3dzZXIgTWVudScpLFxuICAgICAgaXNFbmFibGVkOiAoKSA9PiBmYWxzZSxcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHZvaWQgMFxuICAgIH0pO1xuXG4gICAgLy8gUmV0dXJucyB0aGUgd2lkZ2V0IGFzc29jaWF0ZWQgd2l0aCB0aGUgbW9zdCByZWNlbnQgY29udGV4dG1lbnUgZXZlbnQuXG4gICAgY29uc3QgY29udGV4dE1lbnVXaWRnZXQgPSAoKTogV2lkZ2V0IHwgbnVsbCA9PiB7XG4gICAgICBjb25zdCB0ZXN0ID0gKG5vZGU6IEhUTUxFbGVtZW50KSA9PiAhIW5vZGUuZGF0YXNldC5pZDtcbiAgICAgIGNvbnN0IG5vZGUgPSBhcHAuY29udGV4dE1lbnVIaXRUZXN0KHRlc3QpO1xuXG4gICAgICBpZiAoIW5vZGUpIHtcbiAgICAgICAgLy8gRmFsbCBiYWNrIHRvIGFjdGl2ZSB3aWRnZXQgaWYgcGF0aCBjYW5ub3QgYmUgb2J0YWluZWQgZnJvbSBldmVudC5cbiAgICAgICAgcmV0dXJuIHNoZWxsLmN1cnJlbnRXaWRnZXQ7XG4gICAgICB9XG5cbiAgICAgIGNvbnN0IG1hdGNoZXMgPSB0b0FycmF5KHNoZWxsLndpZGdldHMoJ21haW4nKSkuZmlsdGVyKFxuICAgICAgICB3aWRnZXQgPT4gd2lkZ2V0LmlkID09PSBub2RlLmRhdGFzZXQuaWRcbiAgICAgICk7XG5cbiAgICAgIGlmIChtYXRjaGVzLmxlbmd0aCA8IDEpIHtcbiAgICAgICAgcmV0dXJuIHNoZWxsLmN1cnJlbnRXaWRnZXQ7XG4gICAgICB9XG5cbiAgICAgIHJldHVybiBtYXRjaGVzWzBdO1xuICAgIH07XG5cbiAgICAvLyBDbG9zZXMgYW4gYXJyYXkgb2Ygd2lkZ2V0cy5cbiAgICBjb25zdCBjbG9zZVdpZGdldHMgPSAod2lkZ2V0czogQXJyYXk8V2lkZ2V0Pik6IHZvaWQgPT4ge1xuICAgICAgd2lkZ2V0cy5mb3JFYWNoKHdpZGdldCA9PiB3aWRnZXQuY2xvc2UoKSk7XG4gICAgfTtcblxuICAgIC8vIEZpbmQgdGhlIHRhYiBhcmVhIGZvciBhIHdpZGdldCB3aXRoaW4gYSBzcGVjaWZpYyBkb2NrIGFyZWEuXG4gICAgY29uc3QgZmluZFRhYiA9IChcbiAgICAgIGFyZWE6IERvY2tMYXlvdXQuQXJlYUNvbmZpZyxcbiAgICAgIHdpZGdldDogV2lkZ2V0XG4gICAgKTogRG9ja0xheW91dC5JVGFiQXJlYUNvbmZpZyB8IG51bGwgPT4ge1xuICAgICAgc3dpdGNoIChhcmVhLnR5cGUpIHtcbiAgICAgICAgY2FzZSAnc3BsaXQtYXJlYSc6IHtcbiAgICAgICAgICBjb25zdCBpdGVyYXRvciA9IGl0ZXIoYXJlYS5jaGlsZHJlbik7XG4gICAgICAgICAgbGV0IHRhYjogRG9ja0xheW91dC5JVGFiQXJlYUNvbmZpZyB8IG51bGwgPSBudWxsO1xuICAgICAgICAgIGxldCB2YWx1ZTogRG9ja0xheW91dC5BcmVhQ29uZmlnIHwgdW5kZWZpbmVkO1xuICAgICAgICAgIGRvIHtcbiAgICAgICAgICAgIHZhbHVlID0gaXRlcmF0b3IubmV4dCgpO1xuICAgICAgICAgICAgaWYgKHZhbHVlKSB7XG4gICAgICAgICAgICAgIHRhYiA9IGZpbmRUYWIodmFsdWUsIHdpZGdldCk7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgfSB3aGlsZSAoIXRhYiAmJiB2YWx1ZSk7XG4gICAgICAgICAgcmV0dXJuIHRhYjtcbiAgICAgICAgfVxuICAgICAgICBjYXNlICd0YWItYXJlYSc6IHtcbiAgICAgICAgICBjb25zdCB7IGlkIH0gPSB3aWRnZXQ7XG4gICAgICAgICAgcmV0dXJuIGFyZWEud2lkZ2V0cy5zb21lKHdpZGdldCA9PiB3aWRnZXQuaWQgPT09IGlkKSA/IGFyZWEgOiBudWxsO1xuICAgICAgICB9XG4gICAgICAgIGRlZmF1bHQ6XG4gICAgICAgICAgcmV0dXJuIG51bGw7XG4gICAgICB9XG4gICAgfTtcblxuICAgIC8vIEZpbmQgdGhlIHRhYiBhcmVhIGZvciBhIHdpZGdldCB3aXRoaW4gdGhlIG1haW4gZG9jayBhcmVhLlxuICAgIGNvbnN0IHRhYkFyZWFGb3IgPSAod2lkZ2V0OiBXaWRnZXQpOiBEb2NrTGF5b3V0LklUYWJBcmVhQ29uZmlnIHwgbnVsbCA9PiB7XG4gICAgICBjb25zdCBsYXlvdXQgPSBsYWJTaGVsbD8uc2F2ZUxheW91dCgpO1xuICAgICAgY29uc3QgbWFpbkFyZWEgPSBsYXlvdXQ/Lm1haW5BcmVhO1xuICAgICAgaWYgKCFtYWluQXJlYSB8fCBQYWdlQ29uZmlnLmdldE9wdGlvbignbW9kZScpICE9PSAnbXVsdGlwbGUtZG9jdW1lbnQnKSB7XG4gICAgICAgIHJldHVybiBudWxsO1xuICAgICAgfVxuICAgICAgY29uc3QgYXJlYSA9IG1haW5BcmVhLmRvY2s/Lm1haW47XG4gICAgICBpZiAoIWFyZWEpIHtcbiAgICAgICAgcmV0dXJuIG51bGw7XG4gICAgICB9XG4gICAgICByZXR1cm4gZmluZFRhYihhcmVhLCB3aWRnZXQpO1xuICAgIH07XG5cbiAgICAvLyBSZXR1cm5zIGFuIGFycmF5IG9mIGFsbCB3aWRnZXRzIHRvIHRoZSByaWdodCBvZiBhIHdpZGdldCBpbiBhIHRhYiBhcmVhLlxuICAgIGNvbnN0IHdpZGdldHNSaWdodE9mID0gKHdpZGdldDogV2lkZ2V0KTogQXJyYXk8V2lkZ2V0PiA9PiB7XG4gICAgICBjb25zdCB7IGlkIH0gPSB3aWRnZXQ7XG4gICAgICBjb25zdCB0YWJBcmVhID0gdGFiQXJlYUZvcih3aWRnZXQpO1xuICAgICAgY29uc3Qgd2lkZ2V0cyA9IHRhYkFyZWEgPyB0YWJBcmVhLndpZGdldHMgfHwgW10gOiBbXTtcbiAgICAgIGNvbnN0IGluZGV4ID0gd2lkZ2V0cy5maW5kSW5kZXgod2lkZ2V0ID0+IHdpZGdldC5pZCA9PT0gaWQpO1xuICAgICAgaWYgKGluZGV4IDwgMCkge1xuICAgICAgICByZXR1cm4gW107XG4gICAgICB9XG4gICAgICByZXR1cm4gd2lkZ2V0cy5zbGljZShpbmRleCArIDEpO1xuICAgIH07XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY2xvc2UsIHtcbiAgICAgIGxhYmVsOiAoKSA9PiB0cmFucy5fXygnQ2xvc2UgVGFiJyksXG4gICAgICBpc0VuYWJsZWQ6ICgpID0+IHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gY29udGV4dE1lbnVXaWRnZXQoKTtcbiAgICAgICAgcmV0dXJuICEhd2lkZ2V0ICYmIHdpZGdldC50aXRsZS5jbG9zYWJsZTtcbiAgICAgIH0sXG4gICAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAgIGNvbnN0IHdpZGdldCA9IGNvbnRleHRNZW51V2lkZ2V0KCk7XG4gICAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgICB3aWRnZXQuY2xvc2UoKTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH0pO1xuXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmNsb3NlT3RoZXJUYWJzLCB7XG4gICAgICBsYWJlbDogKCkgPT4gdHJhbnMuX18oJ0Nsb3NlIEFsbCBPdGhlciBUYWJzJyksXG4gICAgICBpc0VuYWJsZWQ6ICgpID0+IHtcbiAgICAgICAgLy8gRW5zdXJlIHRoZXJlIGFyZSBhdCBsZWFzdCB0d28gd2lkZ2V0cy5cbiAgICAgICAgY29uc3QgaXRlcmF0b3IgPSBzaGVsbC53aWRnZXRzKCdtYWluJyk7XG4gICAgICAgIHJldHVybiAhIWl0ZXJhdG9yLm5leHQoKSAmJiAhIWl0ZXJhdG9yLm5leHQoKTtcbiAgICAgIH0sXG4gICAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAgIGNvbnN0IHdpZGdldCA9IGNvbnRleHRNZW51V2lkZ2V0KCk7XG4gICAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IHsgaWQgfSA9IHdpZGdldDtcbiAgICAgICAgY29uc3Qgb3RoZXJXaWRnZXRzID0gdG9BcnJheShzaGVsbC53aWRnZXRzKCdtYWluJykpLmZpbHRlcihcbiAgICAgICAgICB3aWRnZXQgPT4gd2lkZ2V0LmlkICE9PSBpZFxuICAgICAgICApO1xuICAgICAgICBjbG9zZVdpZGdldHMob3RoZXJXaWRnZXRzKTtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5jbG9zZVJpZ2h0VGFicywge1xuICAgICAgbGFiZWw6ICgpID0+IHRyYW5zLl9fKCdDbG9zZSBUYWJzIHRvIFJpZ2h0JyksXG4gICAgICBpc0VuYWJsZWQ6ICgpID0+XG4gICAgICAgICEhY29udGV4dE1lbnVXaWRnZXQoKSAmJlxuICAgICAgICB3aWRnZXRzUmlnaHRPZihjb250ZXh0TWVudVdpZGdldCgpISkubGVuZ3RoID4gMCxcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gY29udGV4dE1lbnVXaWRnZXQoKTtcbiAgICAgICAgaWYgKCF3aWRnZXQpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cbiAgICAgICAgY2xvc2VXaWRnZXRzKHdpZGdldHNSaWdodE9mKHdpZGdldCkpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgaWYgKGxhYlNoZWxsKSB7XG4gICAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuYWN0aXZhdGVOZXh0VGFiLCB7XG4gICAgICAgIGxhYmVsOiB0cmFucy5fXygnQWN0aXZhdGUgTmV4dCBUYWInKSxcbiAgICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICAgIGxhYlNoZWxsLmFjdGl2YXRlTmV4dFRhYigpO1xuICAgICAgICB9XG4gICAgICB9KTtcblxuICAgICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmFjdGl2YXRlUHJldmlvdXNUYWIsIHtcbiAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdBY3RpdmF0ZSBQcmV2aW91cyBUYWInKSxcbiAgICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICAgIGxhYlNoZWxsLmFjdGl2YXRlUHJldmlvdXNUYWIoKTtcbiAgICAgICAgfVxuICAgICAgfSk7XG5cbiAgICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5hY3RpdmF0ZU5leHRUYWJCYXIsIHtcbiAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdBY3RpdmF0ZSBOZXh0IFRhYiBCYXInKSxcbiAgICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICAgIGxhYlNoZWxsLmFjdGl2YXRlTmV4dFRhYkJhcigpO1xuICAgICAgICB9XG4gICAgICB9KTtcblxuICAgICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmFjdGl2YXRlUHJldmlvdXNUYWJCYXIsIHtcbiAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdBY3RpdmF0ZSBQcmV2aW91cyBUYWIgQmFyJyksXG4gICAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgICBsYWJTaGVsbC5hY3RpdmF0ZVByZXZpb3VzVGFiQmFyKCk7XG4gICAgICAgIH1cbiAgICAgIH0pO1xuXG4gICAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY2xvc2VBbGwsIHtcbiAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdDbG9zZSBBbGwgVGFicycpLFxuICAgICAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAgICAgbGFiU2hlbGwuY2xvc2VBbGwoKTtcbiAgICAgICAgfVxuICAgICAgfSk7XG5cbiAgICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy50b2dnbGVIZWFkZXIsIHtcbiAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdTaG93IEhlYWRlcicpLFxuICAgICAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAgICAgaWYgKGxhYlNoZWxsLm1vZGUgPT09ICdzaW5nbGUtZG9jdW1lbnQnKSB7XG4gICAgICAgICAgICBsYWJTaGVsbC50b2dnbGVUb3BJblNpbXBsZU1vZGVWaXNpYmlsaXR5KCk7XG4gICAgICAgICAgfVxuICAgICAgICB9LFxuICAgICAgICBpc1RvZ2dsZWQ6ICgpID0+IGxhYlNoZWxsLmlzVG9wSW5TaW1wbGVNb2RlVmlzaWJsZSgpLFxuICAgICAgICBpc1Zpc2libGU6ICgpID0+IGxhYlNoZWxsLm1vZGUgPT09ICdzaW5nbGUtZG9jdW1lbnQnXG4gICAgICB9KTtcblxuICAgICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnRvZ2dsZUxlZnRBcmVhLCB7XG4gICAgICAgIGxhYmVsOiB0cmFucy5fXygnU2hvdyBMZWZ0IFNpZGViYXInKSxcbiAgICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICAgIGlmIChsYWJTaGVsbC5sZWZ0Q29sbGFwc2VkKSB7XG4gICAgICAgICAgICBsYWJTaGVsbC5leHBhbmRMZWZ0KCk7XG4gICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIGxhYlNoZWxsLmNvbGxhcHNlTGVmdCgpO1xuICAgICAgICAgICAgaWYgKGxhYlNoZWxsLmN1cnJlbnRXaWRnZXQpIHtcbiAgICAgICAgICAgICAgbGFiU2hlbGwuYWN0aXZhdGVCeUlkKGxhYlNoZWxsLmN1cnJlbnRXaWRnZXQuaWQpO1xuICAgICAgICAgICAgfVxuICAgICAgICAgIH1cbiAgICAgICAgfSxcbiAgICAgICAgaXNUb2dnbGVkOiAoKSA9PiAhbGFiU2hlbGwubGVmdENvbGxhcHNlZCxcbiAgICAgICAgaXNFbmFibGVkOiAoKSA9PiAhbGFiU2hlbGwuaXNFbXB0eSgnbGVmdCcpXG4gICAgICB9KTtcblxuICAgICAgLy8gY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnRvZ2dsZVJpZ2h0QXJlYSwge1xuICAgICAgLy8gICBsYWJlbDogdHJhbnMuX18oJ1Nob3cgUmlnaHQgU2lkZWJhcicpLFxuICAgICAgLy8gICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAvLyAgICAgaWYgKGxhYlNoZWxsLnJpZ2h0Q29sbGFwc2VkKSB7XG4gICAgICAvLyAgICAgICBsYWJTaGVsbC5leHBhbmRSaWdodCgpO1xuICAgICAgLy8gICAgIH0gZWxzZSB7XG4gICAgICAvLyAgICAgICBsYWJTaGVsbC5jb2xsYXBzZVJpZ2h0KCk7XG4gICAgICAvLyAgICAgICBpZiAobGFiU2hlbGwuY3VycmVudFdpZGdldCkge1xuICAgICAgLy8gICAgICAgICBsYWJTaGVsbC5hY3RpdmF0ZUJ5SWQobGFiU2hlbGwuY3VycmVudFdpZGdldC5pZCk7XG4gICAgICAvLyAgICAgICB9XG4gICAgICAvLyAgICAgfVxuICAgICAgLy8gICB9LFxuICAgICAgLy8gICBpc1RvZ2dsZWQ6ICgpID0+ICFsYWJTaGVsbC5yaWdodENvbGxhcHNlZCxcbiAgICAgIC8vICAgaXNFbmFibGVkOiAoKSA9PiAhbGFiU2hlbGwuaXNFbXB0eSgncmlnaHQnKVxuICAgICAgLy8gfSk7XG5cbiAgICAgIC8vIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy50b2dnbGVTaWRlVGFiQmFyLCB7XG4gICAgICAvLyAgIGxhYmVsOiBhcmdzID0+XG4gICAgICAvLyAgICAgYXJncy5zaWRlID09PSAncmlnaHQnXG4gICAgICAvLyAgICAgICA/IHRyYW5zLl9fKCdTaG93IFJpZ2h0IEFjdGl2aXR5IEJhcicpXG4gICAgICAvLyAgICAgICA6IHRyYW5zLl9fKCdTaG93IExlZnQgQWN0aXZpdHkgQmFyJyksXG4gICAgICAvLyAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgLy8gICAgIGlmIChhcmdzLnNpZGUgPT09ICdyaWdodCcpIHtcbiAgICAgIC8vICAgICAgIGxhYlNoZWxsLnRvZ2dsZVNpZGVUYWJCYXJWaXNpYmlsaXR5KCdyaWdodCcpO1xuICAgICAgLy8gICAgIH0gZWxzZSB7XG4gICAgICAvLyAgICAgICBsYWJTaGVsbC50b2dnbGVTaWRlVGFiQmFyVmlzaWJpbGl0eSgnbGVmdCcpO1xuICAgICAgLy8gICAgIH1cbiAgICAgIC8vICAgfSxcbiAgICAgIC8vICAgaXNUb2dnbGVkOiBhcmdzID0+XG4gICAgICAvLyAgICAgYXJncy5zaWRlID09PSAncmlnaHQnXG4gICAgICAvLyAgICAgICA/IGxhYlNoZWxsLmlzU2lkZVRhYkJhclZpc2libGUoJ3JpZ2h0JylcbiAgICAgIC8vICAgICAgIDogbGFiU2hlbGwuaXNTaWRlVGFiQmFyVmlzaWJsZSgnbGVmdCcpLFxuICAgICAgLy8gICBpc0VuYWJsZWQ6IGFyZ3MgPT5cbiAgICAgIC8vICAgICBhcmdzLnNpZGUgPT09ICdyaWdodCdcbiAgICAgIC8vICAgICAgID8gIWxhYlNoZWxsLmlzRW1wdHkoJ3JpZ2h0JylcbiAgICAgIC8vICAgICAgIDogIWxhYlNoZWxsLmlzRW1wdHkoJ2xlZnQnKVxuICAgICAgLy8gfSk7XG5cbiAgICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy50b2dnbGVQcmVzZW50YXRpb25Nb2RlLCB7XG4gICAgICAgIGxhYmVsOiAoKSA9PiB0cmFucy5fXygnUHJlc2VudGF0aW9uIE1vZGUnKSxcbiAgICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICAgIGxhYlNoZWxsLnByZXNlbnRhdGlvbk1vZGUgPSAhbGFiU2hlbGwucHJlc2VudGF0aW9uTW9kZTtcbiAgICAgICAgfSxcbiAgICAgICAgaXNUb2dnbGVkOiAoKSA9PiBsYWJTaGVsbC5wcmVzZW50YXRpb25Nb2RlLFxuICAgICAgICBpc1Zpc2libGU6ICgpID0+IHRydWVcbiAgICAgIH0pO1xuXG4gICAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuc2V0TW9kZSwge1xuICAgICAgICBsYWJlbDogYXJncyA9PlxuICAgICAgICAgIGFyZ3NbJ21vZGUnXVxuICAgICAgICAgICAgPyB0cmFucy5fXygnU2V0ICUxIG1vZGUuJywgYXJnc1snbW9kZSddKVxuICAgICAgICAgICAgOiB0cmFucy5fXygnU2V0IHRoZSBsYXlvdXQgYG1vZGVgLicpLFxuICAgICAgICBjYXB0aW9uOiB0cmFucy5fXyhcbiAgICAgICAgICAnVGhlIGxheW91dCBgbW9kZWAgY2FuIGJlIFwic2luZ2xlLWRvY3VtZW50XCIgb3IgXCJtdWx0aXBsZS1kb2N1bWVudFwiLidcbiAgICAgICAgKSxcbiAgICAgICAgaXNWaXNpYmxlOiBhcmdzID0+IHtcbiAgICAgICAgICBjb25zdCBtb2RlID0gYXJnc1snbW9kZSddIGFzIHN0cmluZztcbiAgICAgICAgICByZXR1cm4gbW9kZSA9PT0gJ3NpbmdsZS1kb2N1bWVudCcgfHwgbW9kZSA9PT0gJ211bHRpcGxlLWRvY3VtZW50JztcbiAgICAgICAgfSxcbiAgICAgICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICAgICAgY29uc3QgbW9kZSA9IGFyZ3NbJ21vZGUnXSBhcyBzdHJpbmc7XG4gICAgICAgICAgaWYgKG1vZGUgPT09ICdzaW5nbGUtZG9jdW1lbnQnIHx8IG1vZGUgPT09ICdtdWx0aXBsZS1kb2N1bWVudCcpIHtcbiAgICAgICAgICAgIGxhYlNoZWxsLm1vZGUgPSBtb2RlO1xuICAgICAgICAgICAgcmV0dXJuO1xuICAgICAgICAgIH1cbiAgICAgICAgICB0aHJvdyBuZXcgRXJyb3IoYFVuc3VwcG9ydGVkIGFwcGxpY2F0aW9uIHNoZWxsIG1vZGU6ICR7bW9kZX1gKTtcbiAgICAgICAgfVxuICAgICAgfSk7XG5cbiAgICAgIC8vIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy50b2dnbGVNb2RlLCB7XG4gICAgICAvLyAgIGxhYmVsOiB0cmFucy5fXygnU2ltcGxlIEludGVyZmFjZScpLFxuICAgICAgLy8gICBpc1RvZ2dsZWQ6ICgpID0+IGxhYlNoZWxsLm1vZGUgPT09ICdzaW5nbGUtZG9jdW1lbnQnLFxuICAgICAgLy8gICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAvLyAgICAgY29uc3QgYXJncyA9XG4gICAgICAvLyAgICAgICBsYWJTaGVsbC5tb2RlID09PSAnbXVsdGlwbGUtZG9jdW1lbnQnXG4gICAgICAvLyAgICAgICAgID8geyBtb2RlOiAnc2luZ2xlLWRvY3VtZW50JyB9XG4gICAgICAvLyAgICAgICAgIDogeyBtb2RlOiAnbXVsdGlwbGUtZG9jdW1lbnQnIH07XG4gICAgICAvLyAgICAgcmV0dXJuIGNvbW1hbmRzLmV4ZWN1dGUoQ29tbWFuZElEcy5zZXRNb2RlLCBhcmdzKTtcbiAgICAgIC8vICAgfVxuICAgICAgLy8gfSk7XG5cbiAgICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5yZXNldExheW91dCwge1xuICAgICAgICBsYWJlbDogdHJhbnMuX18oJ1Jlc2V0IERlZmF1bHQgTGF5b3V0JyksXG4gICAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgICAvLyBUdXJuIG9mZiBwcmVzZW50YXRpb24gbW9kZVxuICAgICAgICAgIGlmIChsYWJTaGVsbC5wcmVzZW50YXRpb25Nb2RlKSB7XG4gICAgICAgICAgICBjb21tYW5kc1xuICAgICAgICAgICAgICAuZXhlY3V0ZShDb21tYW5kSURzLnRvZ2dsZVByZXNlbnRhdGlvbk1vZGUpXG4gICAgICAgICAgICAgIC5jYXRjaChyZWFzb24gPT4ge1xuICAgICAgICAgICAgICAgIGNvbnNvbGUuZXJyb3IoJ0ZhaWxlZCB0byB1bmRvIHByZXNlbnRhdGlvbiBtb2RlLicsIHJlYXNvbik7XG4gICAgICAgICAgICAgIH0pO1xuICAgICAgICAgIH1cbiAgICAgICAgICAvLyBEaXNwbGF5IHRvcCBoZWFkZXJcbiAgICAgICAgICBpZiAoXG4gICAgICAgICAgICBsYWJTaGVsbC5tb2RlID09PSAnc2luZ2xlLWRvY3VtZW50JyAmJlxuICAgICAgICAgICAgIWxhYlNoZWxsLmlzVG9wSW5TaW1wbGVNb2RlVmlzaWJsZSgpXG4gICAgICAgICAgKSB7XG4gICAgICAgICAgICBjb21tYW5kcy5leGVjdXRlKENvbW1hbmRJRHMudG9nZ2xlSGVhZGVyKS5jYXRjaChyZWFzb24gPT4ge1xuICAgICAgICAgICAgICBjb25zb2xlLmVycm9yKCdGYWlsZWQgdG8gZGlzcGxheSB0aXRsZSBoZWFkZXIuJywgcmVhc29uKTtcbiAgICAgICAgICAgIH0pO1xuICAgICAgICAgIH1cbiAgICAgICAgICAvLyBEaXNwbGF5IHNpZGUgdGFiYmFyXG4gICAgICAgICAgKFsnbGVmdCcsICdyaWdodCddIGFzICgnbGVmdCcgfCAncmlnaHQnKVtdKS5mb3JFYWNoKHNpZGUgPT4ge1xuICAgICAgICAgICAgaWYgKFxuICAgICAgICAgICAgICAhbGFiU2hlbGwuaXNTaWRlVGFiQmFyVmlzaWJsZShzaWRlKSAmJlxuICAgICAgICAgICAgICAhbGFiU2hlbGwuaXNFbXB0eShzaWRlKVxuICAgICAgICAgICAgKSB7XG4gICAgICAgICAgICAgIGNvbW1hbmRzXG4gICAgICAgICAgICAgICAgLmV4ZWN1dGUoQ29tbWFuZElEcy50b2dnbGVTaWRlVGFiQmFyLCB7IHNpZGUgfSlcbiAgICAgICAgICAgICAgICAuY2F0Y2gocmVhc29uID0+IHtcbiAgICAgICAgICAgICAgICAgIGNvbnNvbGUuZXJyb3IoYEZhaWxlZCB0byBzaG93ICR7c2lkZX0gYWN0aXZpdHkgYmFyLmAsIHJlYXNvbik7XG4gICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgfSk7XG5cbiAgICAgICAgICAvLyBTb21lIGFjdGlvbnMgYXJlIGFsc28gdHJpZ2dlciBpbmRpcmVjdGx5XG4gICAgICAgICAgLy8gLSBieSBsaXN0ZW5pbmcgdG8gdGhpcyBjb21tYW5kIGV4ZWN1dGlvbi5cbiAgICAgICAgfVxuICAgICAgfSk7XG4gICAgfVxuXG4gICAgaWYgKHBhbGV0dGUpIHtcbiAgICAgIFtcbiAgICAgICAgQ29tbWFuZElEcy5hY3RpdmF0ZU5leHRUYWIsXG4gICAgICAgIENvbW1hbmRJRHMuYWN0aXZhdGVQcmV2aW91c1RhYixcbiAgICAgICAgQ29tbWFuZElEcy5hY3RpdmF0ZU5leHRUYWJCYXIsXG4gICAgICAgIENvbW1hbmRJRHMuYWN0aXZhdGVQcmV2aW91c1RhYkJhcixcbiAgICAgICAgQ29tbWFuZElEcy5jbG9zZSxcbiAgICAgICAgQ29tbWFuZElEcy5jbG9zZUFsbCxcbiAgICAgICAgQ29tbWFuZElEcy5jbG9zZU90aGVyVGFicyxcbiAgICAgICAgQ29tbWFuZElEcy5jbG9zZVJpZ2h0VGFicyxcbiAgICAgICAgQ29tbWFuZElEcy50b2dnbGVIZWFkZXIsXG4gICAgICAgIENvbW1hbmRJRHMudG9nZ2xlTGVmdEFyZWEsXG4gICAgICAgIENvbW1hbmRJRHMudG9nZ2xlUmlnaHRBcmVhLFxuICAgICAgICBDb21tYW5kSURzLnRvZ2dsZVByZXNlbnRhdGlvbk1vZGUsXG4gICAgICAgIENvbW1hbmRJRHMudG9nZ2xlTW9kZSxcbiAgICAgICAgQ29tbWFuZElEcy5yZXNldExheW91dFxuICAgICAgXS5mb3JFYWNoKGNvbW1hbmQgPT4gcGFsZXR0ZS5hZGRJdGVtKHsgY29tbWFuZCwgY2F0ZWdvcnkgfSkpO1xuXG4gICAgICBbJ3JpZ2h0JywgJ2xlZnQnXS5mb3JFYWNoKHNpZGUgPT4ge1xuICAgICAgICBwYWxldHRlLmFkZEl0ZW0oe1xuICAgICAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMudG9nZ2xlU2lkZVRhYkJhcixcbiAgICAgICAgICBjYXRlZ29yeSxcbiAgICAgICAgICBhcmdzOiB7IHNpZGUgfVxuICAgICAgICB9KTtcbiAgICAgIH0pO1xuICAgIH1cbiAgfVxufTtcblxuLyoqXG4gKiBUaGUgbWFpbiBleHRlbnNpb24uXG4gKi9cbmNvbnN0IG1haW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJVHJlZVBhdGhVcGRhdGVyPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbi1leHRlbnNpb246bWFpbicsXG4gIHJlcXVpcmVzOiBbXG4gICAgSVJvdXRlcixcbiAgICBJV2luZG93UmVzb2x2ZXIsXG4gICAgSVRyYW5zbGF0b3IsXG4gICAgSnVweXRlckZyb250RW5kLklUcmVlUmVzb2x2ZXJcbiAgXSxcbiAgb3B0aW9uYWw6IFtJQ29ubmVjdGlvbkxvc3RdLFxuICBwcm92aWRlczogSVRyZWVQYXRoVXBkYXRlcixcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICByb3V0ZXI6IElSb3V0ZXIsXG4gICAgcmVzb2x2ZXI6IElXaW5kb3dSZXNvbHZlcixcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcixcbiAgICB0cmVlUmVzb2x2ZXI6IEp1cHl0ZXJGcm9udEVuZC5JVHJlZVJlc29sdmVyLFxuICAgIGNvbm5lY3Rpb25Mb3N0OiBJQ29ubmVjdGlvbkxvc3QgfCBudWxsXG4gICkgPT4ge1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG5cbiAgICBpZiAoIShhcHAgaW5zdGFuY2VvZiBKdXB5dGVyTGFiKSkge1xuICAgICAgdGhyb3cgbmV3IEVycm9yKGAke21haW4uaWR9IG11c3QgYmUgYWN0aXZhdGVkIGluIE5vdGVib29rLmApO1xuICAgIH1cblxuICAgIC8vIFRoZXNlIHR3byBpbnRlcm5hbCBzdGF0ZSB2YXJpYWJsZXMgYXJlIHVzZWQgdG8gbWFuYWdlIHRoZSB0d28gc291cmNlXG4gICAgLy8gb2YgdGhlIHRyZWUgcGFydCBvZiB0aGUgVVJMIGJlaW5nIHVwZGF0ZWQ6IDEpIHBhdGggb2YgdGhlIGFjdGl2ZSBkb2N1bWVudCxcbiAgICAvLyAyKSBwYXRoIG9mIHRoZSBkZWZhdWx0IGJyb3dzZXIgaWYgdGhlIGFjdGl2ZSBtYWluIGFyZWEgd2lkZ2V0IGlzbid0IGEgZG9jdW1lbnQuXG4gICAgbGV0IF9kb2NUcmVlUGF0aCA9ICcnO1xuICAgIGxldCBfZGVmYXVsdEJyb3dzZXJUcmVlUGF0aCA9ICcnO1xuXG4gICAgZnVuY3Rpb24gdXBkYXRlVHJlZVBhdGgodHJlZVBhdGg6IHN0cmluZykge1xuICAgICAgLy8gV2FpdCBmb3IgdHJlZSByZXNvbHZlciB0byBmaW5pc2ggYmVmb3JlIHVwZGF0aW5nIHRoZSBwYXRoIGJlY2F1c2UgaXQgdXNlIHRoZSBQYWdlQ29uZmlnWyd0cmVlUGF0aCddXG4gICAgICB2b2lkIHRyZWVSZXNvbHZlci5wYXRocy50aGVuKCgpID0+IHtcbiAgICAgICAgX2RlZmF1bHRCcm93c2VyVHJlZVBhdGggPSB0cmVlUGF0aDtcbiAgICAgICAgaWYgKCFfZG9jVHJlZVBhdGgpIHtcbiAgICAgICAgICBjb25zdCB1cmwgPSBQYWdlQ29uZmlnLmdldFVybCh7IHRyZWVQYXRoIH0pO1xuICAgICAgICAgIGNvbnN0IHBhdGggPSBVUkxFeHQucGFyc2UodXJsKS5wYXRobmFtZTtcbiAgICAgICAgICByb3V0ZXIubmF2aWdhdGUocGF0aCwgeyBza2lwUm91dGluZzogdHJ1ZSB9KTtcbiAgICAgICAgICAvLyBQZXJzaXN0IHRoZSBuZXcgdHJlZSBwYXRoIHRvIFBhZ2VDb25maWcgYXMgaXQgaXMgdXNlZCBlbHNld2hlcmUgYXQgcnVudGltZS5cbiAgICAgICAgICBQYWdlQ29uZmlnLnNldE9wdGlvbigndHJlZVBhdGgnLCB0cmVlUGF0aCk7XG4gICAgICAgIH1cbiAgICAgIH0pO1xuICAgIH1cblxuICAgIC8vIFJlcXVpcmluZyB0aGUgd2luZG93IHJlc29sdmVyIGd1YXJhbnRlZXMgdGhhdCB0aGUgYXBwbGljYXRpb24gZXh0ZW5zaW9uXG4gICAgLy8gb25seSBsb2FkcyBpZiB0aGVyZSBpcyBhIHZpYWJsZSB3aW5kb3cgbmFtZS4gT3RoZXJ3aXNlLCB0aGUgYXBwbGljYXRpb25cbiAgICAvLyB3aWxsIHNob3J0LWNpcmN1aXQgYW5kIGFzayB0aGUgdXNlciB0byBuYXZpZ2F0ZSBhd2F5LlxuICAgIGNvbnN0IHdvcmtzcGFjZSA9IHJlc29sdmVyLm5hbWU7XG5cbiAgICBjb25zb2xlLmRlYnVnKGBTdGFydGluZyBhcHBsaWNhdGlvbiBpbiB3b3Jrc3BhY2U6IFwiJHt3b3Jrc3BhY2V9XCJgKTtcblxuICAgIC8vIElmIHRoZXJlIHdlcmUgZXJyb3JzIHJlZ2lzdGVyaW5nIHBsdWdpbnMsIHRlbGwgdGhlIHVzZXIuXG4gICAgaWYgKGFwcC5yZWdpc3RlclBsdWdpbkVycm9ycy5sZW5ndGggIT09IDApIHtcbiAgICAgIGNvbnN0IGJvZHkgPSAoXG4gICAgICAgIDxwcmU+e2FwcC5yZWdpc3RlclBsdWdpbkVycm9ycy5tYXAoZSA9PiBlLm1lc3NhZ2UpLmpvaW4oJ1xcbicpfTwvcHJlPlxuICAgICAgKTtcblxuICAgICAgdm9pZCBzaG93RXJyb3JNZXNzYWdlKHRyYW5zLl9fKCdFcnJvciBSZWdpc3RlcmluZyBQbHVnaW5zJyksIHtcbiAgICAgICAgbWVzc2FnZTogYm9keVxuICAgICAgfSk7XG4gICAgfVxuXG4gICAgLy8gSWYgdGhlIGFwcGxpY2F0aW9uIHNoZWxsIGxheW91dCBpcyBtb2RpZmllZCxcbiAgICAvLyB0cmlnZ2VyIGEgcmVmcmVzaCBvZiB0aGUgY29tbWFuZHMuXG4gICAgYXBwLnNoZWxsLmxheW91dE1vZGlmaWVkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgYXBwLmNvbW1hbmRzLm5vdGlmeUNvbW1hbmRDaGFuZ2VkKCk7XG4gICAgfSk7XG5cbiAgICAvLyBXYXRjaCB0aGUgbW9kZSBhbmQgdXBkYXRlIHRoZSBwYWdlIFVSTCB0byAvbGFiIG9yIC9kb2MgdG8gcmVmbGVjdCB0aGVcbiAgICAvLyBjaGFuZ2UuXG4gICAgYXBwLnNoZWxsLm1vZGVDaGFuZ2VkLmNvbm5lY3QoKF8sIGFyZ3M6IERvY2tQYW5lbC5Nb2RlKSA9PiB7XG4gICAgICBjb25zdCB1cmwgPSBQYWdlQ29uZmlnLmdldFVybCh7IG1vZGU6IGFyZ3MgYXMgc3RyaW5nIH0pO1xuICAgICAgY29uc3QgcGF0aCA9IFVSTEV4dC5wYXJzZSh1cmwpLnBhdGhuYW1lO1xuICAgICAgcm91dGVyLm5hdmlnYXRlKHBhdGgsIHsgc2tpcFJvdXRpbmc6IHRydWUgfSk7XG4gICAgICAvLyBQZXJzaXN0IHRoaXMgbW9kZSBjaGFuZ2UgdG8gUGFnZUNvbmZpZyBhcyBpdCBpcyB1c2VkIGVsc2V3aGVyZSBhdCBydW50aW1lLlxuICAgICAgUGFnZUNvbmZpZy5zZXRPcHRpb24oJ21vZGUnLCBhcmdzIGFzIHN0cmluZyk7XG4gICAgfSk7XG5cbiAgICAvLyBXYWl0IGZvciB0cmVlIHJlc29sdmVyIHRvIGZpbmlzaCBiZWZvcmUgdXBkYXRpbmcgdGhlIHBhdGggYmVjYXVzZSBpdCB1c2UgdGhlIFBhZ2VDb25maWdbJ3RyZWVQYXRoJ11cbiAgICB2b2lkIHRyZWVSZXNvbHZlci5wYXRocy50aGVuKCgpID0+IHtcbiAgICAgIC8vIFdhdGNoIHRoZSBwYXRoIG9mIHRoZSBjdXJyZW50IHdpZGdldCBpbiB0aGUgbWFpbiBhcmVhIGFuZCB1cGRhdGUgdGhlIHBhZ2VcbiAgICAgIC8vIFVSTCB0byByZWZsZWN0IHRoZSBjaGFuZ2UuXG4gICAgICBhcHAuc2hlbGwuY3VycmVudFBhdGhDaGFuZ2VkLmNvbm5lY3QoKF8sIGFyZ3MpID0+IHtcbiAgICAgICAgY29uc3QgbWF5YmVUcmVlUGF0aCA9IGFyZ3MubmV3VmFsdWUgYXMgc3RyaW5nO1xuICAgICAgICBjb25zdCB0cmVlUGF0aCA9IG1heWJlVHJlZVBhdGggfHwgX2RlZmF1bHRCcm93c2VyVHJlZVBhdGg7XG4gICAgICAgIGNvbnN0IHVybCA9IFBhZ2VDb25maWcuZ2V0VXJsKHsgdHJlZVBhdGg6IHRyZWVQYXRoIH0pO1xuICAgICAgICBjb25zdCBwYXRoID0gVVJMRXh0LnBhcnNlKHVybCkucGF0aG5hbWU7XG4gICAgICAgIHJvdXRlci5uYXZpZ2F0ZShwYXRoLCB7IHNraXBSb3V0aW5nOiB0cnVlIH0pO1xuICAgICAgICAvLyBQZXJzaXN0IHRoZSBuZXcgdHJlZSBwYXRoIHRvIFBhZ2VDb25maWcgYXMgaXQgaXMgdXNlZCBlbHNld2hlcmUgYXQgcnVudGltZS5cbiAgICAgICAgUGFnZUNvbmZpZy5zZXRPcHRpb24oJ3RyZWVQYXRoJywgdHJlZVBhdGgpO1xuICAgICAgICBfZG9jVHJlZVBhdGggPSBtYXliZVRyZWVQYXRoO1xuICAgICAgfSk7XG4gICAgfSk7XG5cbiAgICAvLyBJZiB0aGUgY29ubmVjdGlvbiB0byB0aGUgc2VydmVyIGlzIGxvc3QsIGhhbmRsZSBpdCB3aXRoIHRoZVxuICAgIC8vIGNvbm5lY3Rpb24gbG9zdCBoYW5kbGVyLlxuICAgIGNvbm5lY3Rpb25Mb3N0ID0gY29ubmVjdGlvbkxvc3QgfHwgQ29ubmVjdGlvbkxvc3Q7XG4gICAgYXBwLnNlcnZpY2VNYW5hZ2VyLmNvbm5lY3Rpb25GYWlsdXJlLmNvbm5lY3QoKG1hbmFnZXIsIGVycm9yKSA9PlxuICAgICAgY29ubmVjdGlvbkxvc3QhKG1hbmFnZXIsIGVycm9yLCB0cmFuc2xhdG9yKVxuICAgICk7XG5cbiAgICBjb25zdCBidWlsZGVyID0gYXBwLnNlcnZpY2VNYW5hZ2VyLmJ1aWxkZXI7XG4gICAgY29uc3QgYnVpbGQgPSAoKSA9PiB7XG4gICAgICByZXR1cm4gYnVpbGRlclxuICAgICAgICAuYnVpbGQoKVxuICAgICAgICAudGhlbigoKSA9PiB7XG4gICAgICAgICAgcmV0dXJuIHNob3dEaWFsb2coe1xuICAgICAgICAgICAgdGl0bGU6IHRyYW5zLl9fKCdCdWlsZCBDb21wbGV0ZScpLFxuICAgICAgICAgICAgYm9keTogKFxuICAgICAgICAgICAgICA8ZGl2PlxuICAgICAgICAgICAgICAgIHt0cmFucy5fXygnQnVpbGQgc3VjY2Vzc2Z1bGx5IGNvbXBsZXRlZCwgcmVsb2FkIHBhZ2U/Jyl9XG4gICAgICAgICAgICAgICAgPGJyIC8+XG4gICAgICAgICAgICAgICAge3RyYW5zLl9fKCdZb3Ugd2lsbCBsb3NlIGFueSB1bnNhdmVkIGNoYW5nZXMuJyl9XG4gICAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgICAgKSxcbiAgICAgICAgICAgIGJ1dHRvbnM6IFtcbiAgICAgICAgICAgICAgRGlhbG9nLmNhbmNlbEJ1dHRvbih7XG4gICAgICAgICAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdSZWxvYWQgV2l0aG91dCBTYXZpbmcnKSxcbiAgICAgICAgICAgICAgICBhY3Rpb25zOiBbJ3JlbG9hZCddXG4gICAgICAgICAgICAgIH0pLFxuICAgICAgICAgICAgICBEaWFsb2cub2tCdXR0b24oeyBsYWJlbDogdHJhbnMuX18oJ1NhdmUgYW5kIFJlbG9hZCcpIH0pXG4gICAgICAgICAgICBdLFxuICAgICAgICAgICAgaGFzQ2xvc2U6IHRydWVcbiAgICAgICAgICB9KTtcbiAgICAgICAgfSlcbiAgICAgICAgLnRoZW4oKHsgYnV0dG9uOiB7IGFjY2VwdCwgYWN0aW9ucyB9IH0pID0+IHtcbiAgICAgICAgICBpZiAoYWNjZXB0KSB7XG4gICAgICAgICAgICB2b2lkIGFwcC5jb21tYW5kc1xuICAgICAgICAgICAgICAuZXhlY3V0ZSgnZG9jbWFuYWdlcjpzYXZlJylcbiAgICAgICAgICAgICAgLnRoZW4oKCkgPT4ge1xuICAgICAgICAgICAgICAgIHJvdXRlci5yZWxvYWQoKTtcbiAgICAgICAgICAgICAgfSlcbiAgICAgICAgICAgICAgLmNhdGNoKGVyciA9PiB7XG4gICAgICAgICAgICAgICAgdm9pZCBzaG93RXJyb3JNZXNzYWdlKHRyYW5zLl9fKCdTYXZlIEZhaWxlZCcpLCB7XG4gICAgICAgICAgICAgICAgICBtZXNzYWdlOiA8cHJlPntlcnIubWVzc2FnZX08L3ByZT5cbiAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgfSBlbHNlIGlmIChhY3Rpb25zLmluY2x1ZGVzKCdyZWxvYWQnKSkge1xuICAgICAgICAgICAgcm91dGVyLnJlbG9hZCgpO1xuICAgICAgICAgIH1cbiAgICAgICAgfSlcbiAgICAgICAgLmNhdGNoKGVyciA9PiB7XG4gICAgICAgICAgdm9pZCBzaG93RXJyb3JNZXNzYWdlKHRyYW5zLl9fKCdCdWlsZCBGYWlsZWQnKSwge1xuICAgICAgICAgICAgbWVzc2FnZTogPHByZT57ZXJyLm1lc3NhZ2V9PC9wcmU+XG4gICAgICAgICAgfSk7XG4gICAgICAgIH0pO1xuICAgIH07XG5cbiAgICBpZiAoYnVpbGRlci5pc0F2YWlsYWJsZSAmJiBidWlsZGVyLnNob3VsZENoZWNrKSB7XG4gICAgICB2b2lkIGJ1aWxkZXIuZ2V0U3RhdHVzKCkudGhlbihyZXNwb25zZSA9PiB7XG4gICAgICAgIGlmIChyZXNwb25zZS5zdGF0dXMgPT09ICdidWlsZGluZycpIHtcbiAgICAgICAgICByZXR1cm4gYnVpbGQoKTtcbiAgICAgICAgfVxuXG4gICAgICAgIGlmIChyZXNwb25zZS5zdGF0dXMgIT09ICduZWVkZWQnKSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG5cbiAgICAgICAgY29uc3QgYm9keSA9IChcbiAgICAgICAgICA8ZGl2PlxuICAgICAgICAgICAge3RyYW5zLl9fKCdOb3RlYm9vayBidWlsZCBpcyBzdWdnZXN0ZWQ6Jyl9XG4gICAgICAgICAgICA8YnIgLz5cbiAgICAgICAgICAgIDxwcmU+e3Jlc3BvbnNlLm1lc3NhZ2V9PC9wcmU+XG4gICAgICAgICAgPC9kaXY+XG4gICAgICAgICk7XG5cbiAgICAgICAgdm9pZCBzaG93RGlhbG9nKHtcbiAgICAgICAgICB0aXRsZTogdHJhbnMuX18oJ0J1aWxkIFJlY29tbWVuZGVkJyksXG4gICAgICAgICAgYm9keSxcbiAgICAgICAgICBidXR0b25zOiBbXG4gICAgICAgICAgICBEaWFsb2cuY2FuY2VsQnV0dG9uKCksXG4gICAgICAgICAgICBEaWFsb2cub2tCdXR0b24oeyBsYWJlbDogdHJhbnMuX18oJ0J1aWxkJykgfSlcbiAgICAgICAgICBdXG4gICAgICAgIH0pLnRoZW4ocmVzdWx0ID0+IChyZXN1bHQuYnV0dG9uLmFjY2VwdCA/IGJ1aWxkKCkgOiB1bmRlZmluZWQpKTtcbiAgICAgIH0pO1xuICAgIH1cbiAgICByZXR1cm4gdXBkYXRlVHJlZVBhdGg7XG4gIH0sXG4gIGF1dG9TdGFydDogdHJ1ZVxufTtcblxuLyoqXG4gKiBQbHVnaW4gdG8gYnVpbGQgdGhlIGNvbnRleHQgbWVudSBmcm9tIHRoZSBzZXR0aW5ncy5cbiAqL1xuY29uc3QgY29udGV4dE1lbnVQbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbi1leHRlbnNpb246Y29udGV4dC1tZW51JyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICByZXF1aXJlczogW0lTZXR0aW5nUmVnaXN0cnksIElUcmFuc2xhdG9yXSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICBzZXR0aW5nUmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnksXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3JcbiAgKTogdm9pZCA9PiB7XG4gICAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcblxuICAgIGZ1bmN0aW9uIGNyZWF0ZU1lbnUob3B0aW9uczogSVNldHRpbmdSZWdpc3RyeS5JTWVudSk6IFJhbmtlZE1lbnUge1xuICAgICAgY29uc3QgbWVudSA9IG5ldyBSYW5rZWRNZW51KHsgLi4ub3B0aW9ucywgY29tbWFuZHM6IGFwcC5jb21tYW5kcyB9KTtcbiAgICAgIGlmIChvcHRpb25zLmxhYmVsKSB7XG4gICAgICAgIG1lbnUudGl0bGUubGFiZWwgPSB0cmFucy5fXyhvcHRpb25zLmxhYmVsKTtcbiAgICAgIH1cbiAgICAgIHJldHVybiBtZW51O1xuICAgIH1cblxuICAgIC8vIExvYWQgdGhlIGNvbnRleHQgbWVudSBsYXRlbHkgc28gcGx1Z2lucyBhcmUgbG9hZGVkLlxuICAgIGFwcC5zdGFydGVkXG4gICAgICAudGhlbigoKSA9PiB7XG4gICAgICAgIHJldHVybiBQcml2YXRlLmxvYWRTZXR0aW5nc0NvbnRleHRNZW51KFxuICAgICAgICAgIGFwcC5jb250ZXh0TWVudSxcbiAgICAgICAgICBzZXR0aW5nUmVnaXN0cnksXG4gICAgICAgICAgY3JlYXRlTWVudSxcbiAgICAgICAgICB0cmFuc2xhdG9yXG4gICAgICAgICk7XG4gICAgICB9KVxuICAgICAgLmNhdGNoKHJlYXNvbiA9PiB7XG4gICAgICAgIGNvbnNvbGUuZXJyb3IoXG4gICAgICAgICAgJ0ZhaWxlZCB0byBsb2FkIGNvbnRleHQgbWVudSBpdGVtcyBmcm9tIHNldHRpbmdzIHJlZ2lzdHJ5LicsXG4gICAgICAgICAgcmVhc29uXG4gICAgICAgICk7XG4gICAgICB9KTtcbiAgfVxufTtcblxuLyoqXG4gKiBDaGVjayBpZiB0aGUgYXBwbGljYXRpb24gaXMgZGlydHkgYmVmb3JlIGNsb3NpbmcgdGhlIGJyb3dzZXIgdGFiLlxuICovXG5jb25zdCBkaXJ0eTogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLWV4dGVuc2lvbjpkaXJ0eScsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcmVxdWlyZXM6IFtJVHJhbnNsYXRvcl0sXG4gIGFjdGl2YXRlOiAoYXBwOiBKdXB5dGVyRnJvbnRFbmQsIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yKTogdm9pZCA9PiB7XG4gICAgaWYgKCEoYXBwIGluc3RhbmNlb2YgSnVweXRlckxhYikpIHtcbiAgICAgIHRocm93IG5ldyBFcnJvcihgJHtkaXJ0eS5pZH0gbXVzdCBiZSBhY3RpdmF0ZWQgaW4gSnVweXRlckxhYi5gKTtcbiAgICB9XG4gICAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICBjb25zdCBtZXNzYWdlID0gdHJhbnMuX18oXG4gICAgICAnQXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIGV4aXQgTm90ZWJvb2s/XFxuXFxuQW55IHVuc2F2ZWQgY2hhbmdlcyB3aWxsIGJlIGxvc3QuJ1xuICAgICk7XG5cbiAgICAvLyBUaGUgc3BlYyBmb3IgdGhlIGBiZWZvcmV1bmxvYWRgIGV2ZW50IGlzIGltcGxlbWVudGVkIGRpZmZlcmVudGx5IGJ5XG4gICAgLy8gdGhlIGRpZmZlcmVudCBicm93c2VyIHZlbmRvcnMuIENvbnNlcXVlbnRseSwgdGhlIGBldmVudC5yZXR1cm5WYWx1ZWBcbiAgICAvLyBhdHRyaWJ1dGUgbmVlZHMgdG8gc2V0IGluIGFkZGl0aW9uIHRvIGEgcmV0dXJuIHZhbHVlIGJlaW5nIHJldHVybmVkLlxuICAgIC8vIEZvciBtb3JlIGluZm9ybWF0aW9uLCBzZWU6XG4gICAgLy8gaHR0cHM6Ly9kZXZlbG9wZXIubW96aWxsYS5vcmcvZW4vZG9jcy9XZWIvRXZlbnRzL2JlZm9yZXVubG9hZFxuICAgIHdpbmRvdy5hZGRFdmVudExpc3RlbmVyKCdiZWZvcmV1bmxvYWQnLCBldmVudCA9PiB7XG4gICAgICBpZiAoYXBwLnN0YXR1cy5pc0RpcnR5KSB7XG4gICAgICAgIHJldHVybiAoKGV2ZW50IGFzIGFueSkucmV0dXJuVmFsdWUgPSBtZXNzYWdlKTtcbiAgICAgIH1cbiAgICB9KTtcbiAgfVxufTtcblxuLyoqXG4gKiBUaGUgZGVmYXVsdCBsYXlvdXQgcmVzdG9yZXIgcHJvdmlkZXIuXG4gKi9cbmNvbnN0IGxheW91dDogSnVweXRlckZyb250RW5kUGx1Z2luPElMYXlvdXRSZXN0b3Jlcj4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tZXh0ZW5zaW9uOmxheW91dCcsXG4gIHJlcXVpcmVzOiBbSVN0YXRlREIsIElMYWJTaGVsbCwgSVNldHRpbmdSZWdpc3RyeV0sXG4gIG9wdGlvbmFsOiBbSVRyYW5zbGF0b3JdLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHN0YXRlOiBJU3RhdGVEQixcbiAgICBsYWJTaGVsbDogSUxhYlNoZWxsLFxuICAgIHNldHRpbmdSZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvciB8IG51bGxcbiAgKSA9PiB7XG4gICAgY29uc3QgdHJhbnMgPSAodHJhbnNsYXRvciA/PyBudWxsVHJhbnNsYXRvcikubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IGZpcnN0ID0gYXBwLnN0YXJ0ZWQ7XG4gICAgY29uc3QgcmVnaXN0cnkgPSBhcHAuY29tbWFuZHM7XG5cbiAgICBjb25zdCByZXN0b3JlciA9IG5ldyBMYXlvdXRSZXN0b3Jlcih7IGNvbm5lY3Rvcjogc3RhdGUsIGZpcnN0LCByZWdpc3RyeSB9KTtcblxuICAgIHNldHRpbmdSZWdpc3RyeVxuICAgICAgLmxvYWQoc2hlbGwuaWQpXG4gICAgICAudGhlbihzZXR0aW5ncyA9PiB7XG4gICAgICAgIC8vIEFkZCBhIGxheWVyIG9mIGN1c3RvbWl6YXRpb24gdG8gc3VwcG9ydCBhcHAgc2hlbGwgbW9kZVxuICAgICAgICBjb25zdCBjdXN0b21pemVkTGF5b3V0ID0gc2V0dGluZ3MuY29tcG9zaXRlWydsYXlvdXQnXSBhcyBhbnk7XG5cbiAgICAgICAgdm9pZCByZXN0b3Jlci5mZXRjaCgpLnRoZW4oc2F2ZWQgPT4ge1xuICAgICAgICAgIGxhYlNoZWxsLnJlc3RvcmVMYXlvdXQoXG4gICAgICAgICAgICBQYWdlQ29uZmlnLmdldE9wdGlvbignbW9kZScpIGFzIERvY2tQYW5lbC5Nb2RlLFxuICAgICAgICAgICAgc2F2ZWQsXG4gICAgICAgICAgICB7XG4gICAgICAgICAgICAgICdtdWx0aXBsZS1kb2N1bWVudCc6IGN1c3RvbWl6ZWRMYXlvdXQubXVsdGlwbGUgPz8ge30sXG4gICAgICAgICAgICAgICdzaW5nbGUtZG9jdW1lbnQnOiBjdXN0b21pemVkTGF5b3V0LnNpbmdsZSA/PyB7fVxuICAgICAgICAgICAgfVxuICAgICAgICAgICk7XG4gICAgICAgICAgbGFiU2hlbGwubGF5b3V0TW9kaWZpZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICAgICAgICB2b2lkIHJlc3RvcmVyLnNhdmUobGFiU2hlbGwuc2F2ZUxheW91dCgpKTtcbiAgICAgICAgICB9KTtcblxuICAgICAgICAgIHNldHRpbmdzLmNoYW5nZWQuY29ubmVjdChvblNldHRpbmdzQ2hhbmdlZCk7XG4gICAgICAgICAgLy8gUHJpdmF0ZS5hY3RpdmF0ZVNpZGViYXJTd2l0Y2hlcihhcHAsIGxhYlNoZWxsLCBzZXR0aW5ncywgdHJhbnMpO1xuICAgICAgICB9KTtcbiAgICAgIH0pXG4gICAgICAuY2F0Y2gocmVhc29uID0+IHtcbiAgICAgICAgY29uc29sZS5lcnJvcignRmFpbCB0byBsb2FkIHNldHRpbmdzIGZvciB0aGUgbGF5b3V0IHJlc3RvcmVyLicpO1xuICAgICAgICBjb25zb2xlLmVycm9yKHJlYXNvbik7XG4gICAgICB9KTtcblxuICAgIHJldHVybiByZXN0b3JlcjtcblxuICAgIGFzeW5jIGZ1bmN0aW9uIG9uU2V0dGluZ3NDaGFuZ2VkKFxuICAgICAgc2V0dGluZ3M6IElTZXR0aW5nUmVnaXN0cnkuSVNldHRpbmdzXG4gICAgKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgICBpZiAoXG4gICAgICAgICFKU09ORXh0LmRlZXBFcXVhbChcbiAgICAgICAgICBzZXR0aW5ncy5jb21wb3NpdGVbJ2xheW91dCddIGFzIFJlYWRvbmx5UGFydGlhbEpTT05WYWx1ZSxcbiAgICAgICAgICB7XG4gICAgICAgICAgICBzaW5nbGU6IGxhYlNoZWxsLnVzZXJMYXlvdXRbJ3NpbmdsZS1kb2N1bWVudCddLFxuICAgICAgICAgICAgbXVsdGlwbGU6IGxhYlNoZWxsLnVzZXJMYXlvdXRbJ211bHRpcGxlLWRvY3VtZW50J11cbiAgICAgICAgICB9IGFzIGFueVxuICAgICAgICApXG4gICAgICApIHtcbiAgICAgICAgY29uc3QgcmVzdWx0ID0gYXdhaXQgc2hvd0RpYWxvZyh7XG4gICAgICAgICAgdGl0bGU6IHRyYW5zLl9fKCdJbmZvcm1hdGlvbicpLFxuICAgICAgICAgIGJvZHk6IHRyYW5zLl9fKFxuICAgICAgICAgICAgJ1VzZXIgbGF5b3V0IGN1c3RvbWl6YXRpb24gaGFzIGNoYW5nZWQuIFlvdSBtYXkgbmVlZCB0byByZWxvYWQgSnVweXRlckxhYiB0byBzZWUgdGhlIGNoYW5nZXMuJ1xuICAgICAgICAgICksXG4gICAgICAgICAgYnV0dG9uczogW1xuICAgICAgICAgICAgRGlhbG9nLmNhbmNlbEJ1dHRvbigpLFxuICAgICAgICAgICAgRGlhbG9nLm9rQnV0dG9uKHsgbGFiZWw6IHRyYW5zLl9fKCdSZWxvYWQnKSB9KVxuICAgICAgICAgIF1cbiAgICAgICAgfSk7XG5cbiAgICAgICAgaWYgKHJlc3VsdC5idXR0b24uYWNjZXB0KSB7XG4gICAgICAgICAgbG9jYXRpb24ucmVsb2FkKCk7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9XG4gIH0sXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcHJvdmlkZXM6IElMYXlvdXRSZXN0b3JlclxufTtcblxuLyoqXG4gKiBUaGUgZGVmYXVsdCBVUkwgcm91dGVyIHByb3ZpZGVyLlxuICovXG5jb25zdCByb3V0ZXI6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJUm91dGVyPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbi1leHRlbnNpb246cm91dGVyJyxcbiAgcmVxdWlyZXM6IFtKdXB5dGVyRnJvbnRFbmQuSVBhdGhzXSxcbiAgYWN0aXZhdGU6IChhcHA6IEp1cHl0ZXJGcm9udEVuZCwgcGF0aHM6IEp1cHl0ZXJGcm9udEVuZC5JUGF0aHMpID0+IHtcbiAgICBjb25zdCB7IGNvbW1hbmRzIH0gPSBhcHA7XG4gICAgY29uc3QgYmFzZSA9IHBhdGhzLnVybHMuYmFzZTtcbiAgICBjb25zdCByb3V0ZXIgPSBuZXcgUm91dGVyKHsgYmFzZSwgY29tbWFuZHMgfSk7XG5cbiAgICB2b2lkIGFwcC5zdGFydGVkLnRoZW4oKCkgPT4ge1xuICAgICAgLy8gUm91dGUgdGhlIHZlcnkgZmlyc3QgcmVxdWVzdCBvbiBsb2FkLlxuICAgICAgdm9pZCByb3V0ZXIucm91dGUoKTtcblxuICAgICAgLy8gUm91dGUgYWxsIHBvcCBzdGF0ZSBldmVudHMuXG4gICAgICB3aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcigncG9wc3RhdGUnLCAoKSA9PiB7XG4gICAgICAgIHZvaWQgcm91dGVyLnJvdXRlKCk7XG4gICAgICB9KTtcbiAgICB9KTtcblxuICAgIHJldHVybiByb3V0ZXI7XG4gIH0sXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcHJvdmlkZXM6IElSb3V0ZXJcbn07XG5cbi8qKlxuICogVGhlIGRlZmF1bHQgdHJlZSByb3V0ZSByZXNvbHZlciBwbHVnaW4uXG4gKi9cbmNvbnN0IHRyZWU6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxKdXB5dGVyRnJvbnRFbmQuSVRyZWVSZXNvbHZlcj4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tZXh0ZW5zaW9uOnRyZWUtcmVzb2x2ZXInLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHJlcXVpcmVzOiBbSVJvdXRlcl0sXG4gIHByb3ZpZGVzOiBKdXB5dGVyRnJvbnRFbmQuSVRyZWVSZXNvbHZlcixcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICByb3V0ZXI6IElSb3V0ZXJcbiAgKTogSnVweXRlckZyb250RW5kLklUcmVlUmVzb2x2ZXIgPT4ge1xuICAgIGNvbnN0IHsgY29tbWFuZHMgfSA9IGFwcDtcbiAgICBjb25zdCBzZXQgPSBuZXcgRGlzcG9zYWJsZVNldCgpO1xuICAgIGNvbnN0IGRlbGVnYXRlID0gbmV3IFByb21pc2VEZWxlZ2F0ZTxKdXB5dGVyRnJvbnRFbmQuSVRyZWVSZXNvbHZlci5QYXRocz4oKTtcblxuICAgIGNvbnN0IHRyZWVQYXR0ZXJuID0gbmV3IFJlZ0V4cChcbiAgICAgICcvKGxhYnxkb2MpKC93b3Jrc3BhY2VzL1thLXpBLVowLTktX10rKT8oL3RyZWUvLiopPydcbiAgICApO1xuXG4gICAgc2V0LmFkZChcbiAgICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy50cmVlLCB7XG4gICAgICAgIGV4ZWN1dGU6IGFzeW5jIChhcmdzOiBJUm91dGVyLklMb2NhdGlvbikgPT4ge1xuICAgICAgICAgIGlmIChzZXQuaXNEaXNwb3NlZCkge1xuICAgICAgICAgICAgcmV0dXJuO1xuICAgICAgICAgIH1cblxuICAgICAgICAgIGNvbnN0IHF1ZXJ5ID0gVVJMRXh0LnF1ZXJ5U3RyaW5nVG9PYmplY3QoYXJncy5zZWFyY2ggPz8gJycpO1xuICAgICAgICAgIGNvbnN0IGJyb3dzZXIgPSBxdWVyeVsnZmlsZS1icm93c2VyLXBhdGgnXSB8fCAnJztcblxuICAgICAgICAgIC8vIFJlbW92ZSB0aGUgZmlsZSBicm93c2VyIHBhdGggZnJvbSB0aGUgcXVlcnkgc3RyaW5nLlxuICAgICAgICAgIGRlbGV0ZSBxdWVyeVsnZmlsZS1icm93c2VyLXBhdGgnXTtcblxuICAgICAgICAgIC8vIENsZWFuIHVwIGFydGlmYWN0cyBpbW1lZGlhdGVseSB1cG9uIHJvdXRpbmcuXG4gICAgICAgICAgc2V0LmRpc3Bvc2UoKTtcblxuICAgICAgICAgIGRlbGVnYXRlLnJlc29sdmUoeyBicm93c2VyLCBmaWxlOiBQYWdlQ29uZmlnLmdldE9wdGlvbigndHJlZVBhdGgnKSB9KTtcbiAgICAgICAgfVxuICAgICAgfSlcbiAgICApO1xuICAgIHNldC5hZGQoXG4gICAgICByb3V0ZXIucmVnaXN0ZXIoeyBjb21tYW5kOiBDb21tYW5kSURzLnRyZWUsIHBhdHRlcm46IHRyZWVQYXR0ZXJuIH0pXG4gICAgKTtcblxuICAgIC8vIElmIGEgcm91dGUgaXMgaGFuZGxlZCBieSB0aGUgcm91dGVyIHdpdGhvdXQgdGhlIHRyZWUgY29tbWFuZCBiZWluZ1xuICAgIC8vIGludm9rZWQsIHJlc29sdmUgdG8gYG51bGxgIGFuZCBjbGVhbiB1cCBhcnRpZmFjdHMuXG4gICAgY29uc3QgbGlzdGVuZXIgPSAoKSA9PiB7XG4gICAgICBpZiAoc2V0LmlzRGlzcG9zZWQpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgc2V0LmRpc3Bvc2UoKTtcbiAgICAgIGRlbGVnYXRlLnJlc29sdmUobnVsbCk7XG4gICAgfTtcbiAgICByb3V0ZXIucm91dGVkLmNvbm5lY3QobGlzdGVuZXIpO1xuICAgIHNldC5hZGQoXG4gICAgICBuZXcgRGlzcG9zYWJsZURlbGVnYXRlKCgpID0+IHtcbiAgICAgICAgcm91dGVyLnJvdXRlZC5kaXNjb25uZWN0KGxpc3RlbmVyKTtcbiAgICAgIH0pXG4gICAgKTtcblxuICAgIHJldHVybiB7IHBhdGhzOiBkZWxlZ2F0ZS5wcm9taXNlIH07XG4gIH1cbn07XG5cbi8qKlxuICogVGhlIGRlZmF1bHQgVVJMIG5vdCBmb3VuZCBleHRlbnNpb24uXG4gKi9cbmNvbnN0IG5vdGZvdW5kOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tZXh0ZW5zaW9uOm5vdGZvdW5kJyxcbiAgcmVxdWlyZXM6IFtKdXB5dGVyRnJvbnRFbmQuSVBhdGhzLCBJUm91dGVyLCBJVHJhbnNsYXRvcl0sXG4gIGFjdGl2YXRlOiAoXG4gICAgXzogSnVweXRlckZyb250RW5kLFxuICAgIHBhdGhzOiBKdXB5dGVyRnJvbnRFbmQuSVBhdGhzLFxuICAgIHJvdXRlcjogSVJvdXRlcixcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvclxuICApID0+IHtcbiAgICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IGJhZCA9IHBhdGhzLnVybHMubm90Rm91bmQ7XG5cbiAgICBpZiAoIWJhZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIGNvbnN0IGJhc2UgPSByb3V0ZXIuYmFzZTtcbiAgICBjb25zdCBtZXNzYWdlID0gdHJhbnMuX18oXG4gICAgICAnVGhlIHBhdGg6ICUxIHdhcyBub3QgZm91bmQuIEp1cHl0ZXJMYWIgcmVkaXJlY3RlZCB0bzogJTInLFxuICAgICAgYmFkLFxuICAgICAgYmFzZVxuICAgICk7XG5cbiAgICAvLyBDaGFuZ2UgdGhlIFVSTCBiYWNrIHRvIHRoZSBiYXNlIGFwcGxpY2F0aW9uIFVSTC5cbiAgICByb3V0ZXIubmF2aWdhdGUoJycpO1xuXG4gICAgdm9pZCBzaG93RXJyb3JNZXNzYWdlKHRyYW5zLl9fKCdQYXRoIE5vdCBGb3VuZCcpLCB7IG1lc3NhZ2UgfSk7XG4gIH0sXG4gIGF1dG9TdGFydDogdHJ1ZVxufTtcblxuLyoqXG4gKiBDaGFuZ2UgdGhlIGZhdmljb24gY2hhbmdpbmcgYmFzZWQgb24gdGhlIGJ1c3kgc3RhdHVzO1xuICovXG5jb25zdCBidXN5OiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tZXh0ZW5zaW9uOmZhdmljb25idXN5JyxcbiAgcmVxdWlyZXM6IFtJTGFiU3RhdHVzXSxcbiAgYWN0aXZhdGU6IGFzeW5jIChfOiBKdXB5dGVyRnJvbnRFbmQsIHN0YXR1czogSUxhYlN0YXR1cykgPT4ge1xuICAgIHN0YXR1cy5idXN5U2lnbmFsLmNvbm5lY3QoKF8sIGlzQnVzeSkgPT4ge1xuICAgICAgY29uc3QgZmF2aWNvbiA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoXG4gICAgICAgIGBsaW5rW3JlbD1cImljb25cIl0ke2lzQnVzeSA/ICcuaWRsZS5mYXZpY29uJyA6ICcuYnVzeS5mYXZpY29uJ31gXG4gICAgICApIGFzIEhUTUxMaW5rRWxlbWVudDtcbiAgICAgIGlmICghZmF2aWNvbikge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICBjb25zdCBuZXdGYXZpY29uID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcbiAgICAgICAgYGxpbmske2lzQnVzeSA/ICcuYnVzeS5mYXZpY29uJyA6ICcuaWRsZS5mYXZpY29uJ31gXG4gICAgICApIGFzIEhUTUxMaW5rRWxlbWVudDtcbiAgICAgIGlmICghbmV3RmF2aWNvbikge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICAvLyBJZiB3ZSBoYXZlIHRoZSB0d28gaWNvbnMgd2l0aCB0aGUgc3BlY2lhbCBjbGFzc2VzLCB0aGVuIHRvZ2dsZSB0aGVtLlxuICAgICAgaWYgKGZhdmljb24gIT09IG5ld0Zhdmljb24pIHtcbiAgICAgICAgZmF2aWNvbi5yZWwgPSAnJztcbiAgICAgICAgbmV3RmF2aWNvbi5yZWwgPSAnaWNvbic7XG5cbiAgICAgICAgLy8gRmlyZWZveCBkb2Vzbid0IHNlZW0gdG8gcmVjb2duaXplIGp1c3QgY2hhbmdpbmcgcmVsLCBzbyB3ZSBhbHNvXG4gICAgICAgIC8vIHJlaW5zZXJ0IHRoZSBsaW5rIGludG8gdGhlIERPTS5cbiAgICAgICAgbmV3RmF2aWNvbi5wYXJlbnROb2RlIS5yZXBsYWNlQ2hpbGQobmV3RmF2aWNvbiwgbmV3RmF2aWNvbik7XG4gICAgICB9XG4gICAgfSk7XG4gIH0sXG4gIGF1dG9TdGFydDogdHJ1ZVxufTtcblxuLyoqXG4gKiBUaGUgZGVmYXVsdCBKdXB5dGVyTGFiIGFwcGxpY2F0aW9uIHNoZWxsLlxuICovXG5jb25zdCBzaGVsbDogSnVweXRlckZyb250RW5kUGx1Z2luPElMYWJTaGVsbD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tZXh0ZW5zaW9uOnNoZWxsJyxcbiAgb3B0aW9uYWw6IFtJU2V0dGluZ1JlZ2lzdHJ5XSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICBzZXR0aW5nUmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnkgfCBudWxsXG4gICkgPT4ge1xuICAgIGlmICghKGFwcC5zaGVsbCBpbnN0YW5jZW9mIExhYlNoZWxsKSkge1xuICAgICAgdGhyb3cgbmV3IEVycm9yKGAke3NoZWxsLmlkfSBkaWQgbm90IGZpbmQgYSBMYWJTaGVsbCBpbnN0YW5jZS5gKTtcbiAgICB9XG4gICAgaWYgKHNldHRpbmdSZWdpc3RyeSkge1xuICAgICAgdm9pZCBzZXR0aW5nUmVnaXN0cnkubG9hZChzaGVsbC5pZCkudGhlbihzZXR0aW5ncyA9PiB7XG4gICAgICAgIChhcHAuc2hlbGwgYXMgTGFiU2hlbGwpLnVwZGF0ZUNvbmZpZyhzZXR0aW5ncy5jb21wb3NpdGUpO1xuICAgICAgICBzZXR0aW5ncy5jaGFuZ2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgICAgIChhcHAuc2hlbGwgYXMgTGFiU2hlbGwpLnVwZGF0ZUNvbmZpZyhzZXR0aW5ncy5jb21wb3NpdGUpO1xuICAgICAgICB9KTtcbiAgICAgIH0pO1xuICAgIH1cbiAgICByZXR1cm4gYXBwLnNoZWxsO1xuICB9LFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHByb3ZpZGVzOiBJTGFiU2hlbGxcbn07XG5cbi8qKlxuICogVGhlIGRlZmF1bHQgSnVweXRlckxhYiBhcHBsaWNhdGlvbiBzdGF0dXMgcHJvdmlkZXIuXG4gKi9cbmNvbnN0IHN0YXR1czogSnVweXRlckZyb250RW5kUGx1Z2luPElMYWJTdGF0dXM+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLWV4dGVuc2lvbjpzdGF0dXMnLFxuICBhY3RpdmF0ZTogKGFwcDogSnVweXRlckZyb250RW5kKSA9PiB7XG4gICAgaWYgKCEoYXBwIGluc3RhbmNlb2YgSnVweXRlckxhYikpIHtcbiAgICAgIHRocm93IG5ldyBFcnJvcihgJHtzdGF0dXMuaWR9IG11c3QgYmUgYWN0aXZhdGVkIGluIEp1cHl0ZXJMYWIuYCk7XG4gICAgfVxuICAgIHJldHVybiBhcHAuc3RhdHVzO1xuICB9LFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHByb3ZpZGVzOiBJTGFiU3RhdHVzXG59O1xuXG4vKipcbiAqIFRoZSBkZWZhdWx0IEp1cHl0ZXJMYWIgYXBwbGljYXRpb24tc3BlY2lmaWMgaW5mb3JtYXRpb24gcHJvdmlkZXIuXG4gKlxuICogIyMjIyBOb3Rlc1xuICogVGhpcyBwbHVnaW4gc2hvdWxkIG9ubHkgYmUgdXNlZCBieSBwbHVnaW5zIHRoYXQgc3BlY2lmaWNhbGx5IG5lZWQgdG8gYWNjZXNzXG4gKiBKdXB5dGVyTGFiIGFwcGxpY2F0aW9uIGluZm9ybWF0aW9uLCBlLmcuLCBsaXN0aW5nIGV4dGVuc2lvbnMgdGhhdCBoYXZlIGJlZW5cbiAqIGxvYWRlZCBvciBkZWZlcnJlZCB3aXRoaW4gSnVweXRlckxhYi5cbiAqL1xuY29uc3QgaW5mbzogSnVweXRlckZyb250RW5kUGx1Z2luPEp1cHl0ZXJMYWIuSUluZm8+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLWV4dGVuc2lvbjppbmZvJyxcbiAgYWN0aXZhdGU6IChhcHA6IEp1cHl0ZXJGcm9udEVuZCkgPT4ge1xuICAgIGlmICghKGFwcCBpbnN0YW5jZW9mIEp1cHl0ZXJMYWIpKSB7XG4gICAgICB0aHJvdyBuZXcgRXJyb3IoYCR7aW5mby5pZH0gbXVzdCBiZSBhY3RpdmF0ZWQgaW4gSnVweXRlckxhYi5gKTtcbiAgICB9XG4gICAgcmV0dXJuIGFwcC5pbmZvO1xuICB9LFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHByb3ZpZGVzOiBKdXB5dGVyTGFiLklJbmZvXG59O1xuXG4vKipcbiAqIFRoZSBkZWZhdWx0IEp1cHl0ZXJMYWIgcGF0aHMgZGljdGlvbmFyeSBwcm92aWRlci5cbiAqL1xuY29uc3QgcGF0aHM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxKdXB5dGVyRnJvbnRFbmQuSVBhdGhzPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9hcHB1dGlscy1leHRlbnNpb246cGF0aHMnLFxuICBhY3RpdmF0ZTogKGFwcDogSnVweXRlckZyb250RW5kKTogSnVweXRlckZyb250RW5kLklQYXRocyA9PiB7XG4gICAgaWYgKCEoYXBwIGluc3RhbmNlb2YgSnVweXRlckxhYikpIHtcbiAgICAgIHRocm93IG5ldyBFcnJvcihgJHtwYXRocy5pZH0gbXVzdCBiZSBhY3RpdmF0ZWQgaW4gSnVweXRlckxhYi5gKTtcbiAgICB9XG4gICAgcmV0dXJuIGFwcC5wYXRocztcbiAgfSxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBwcm92aWRlczogSnVweXRlckZyb250RW5kLklQYXRoc1xufTtcblxuLyoqXG4gKiBUaGUgZGVmYXVsdCBwcm9wZXJ0eSBpbnNwZWN0b3IgcHJvdmlkZXIuXG4gKi9cbmNvbnN0IHByb3BlcnR5SW5zcGVjdG9yOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SVByb3BlcnR5SW5zcGVjdG9yUHJvdmlkZXI+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLWV4dGVuc2lvbjpwcm9wZXJ0eS1pbnNwZWN0b3InLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHJlcXVpcmVzOiBbSUxhYlNoZWxsLCBJVHJhbnNsYXRvcl0sXG4gIG9wdGlvbmFsOiBbSUxheW91dFJlc3RvcmVyXSxcbiAgcHJvdmlkZXM6IElQcm9wZXJ0eUluc3BlY3RvclByb3ZpZGVyLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIGxhYnNoZWxsOiBJTGFiU2hlbGwsXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gICAgcmVzdG9yZXI6IElMYXlvdXRSZXN0b3JlciB8IG51bGxcbiAgKSA9PiB7XG4gICAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICBjb25zdCB3aWRnZXQgPSBuZXcgU2lkZUJhclByb3BlcnR5SW5zcGVjdG9yUHJvdmlkZXIoXG4gICAgICBsYWJzaGVsbCxcbiAgICAgIHVuZGVmaW5lZCxcbiAgICAgIHRyYW5zbGF0b3JcbiAgICApO1xuICAgIHdpZGdldC50aXRsZS5pY29uID0gYnVpbGRJY29uO1xuICAgIHdpZGdldC50aXRsZS5jYXB0aW9uID0gdHJhbnMuX18oJ1Byb3BlcnR5IEluc3BlY3RvcicpO1xuICAgIHdpZGdldC5pZCA9ICdqcC1wcm9wZXJ0eS1pbnNwZWN0b3InO1xuICAgIGxhYnNoZWxsLmFkZCh3aWRnZXQsICdsZWZ0JywgeyByYW5rOiA2MDAsIHR5cGU6ICdQcm9wZXJ0eSBJbnNwZWN0b3InIH0pO1xuXG4gICAgYXBwLmNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5zaG93UHJvcGVydHlQYW5lbCwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdQcm9wZXJ0eSBJbnNwZWN0b3InKSxcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgbGFic2hlbGwuYWN0aXZhdGVCeUlkKHdpZGdldC5pZCk7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICBpZiAocmVzdG9yZXIpIHtcbiAgICAgIHJlc3RvcmVyLmFkZCh3aWRnZXQsICdqcC1wcm9wZXJ0eS1pbnNwZWN0b3InKTtcbiAgICB9XG4gICAgcmV0dXJuIHdpZGdldDtcbiAgfVxufTtcblxuY29uc3QgSnVweXRlckxvZ286IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbi1leHRlbnNpb246bG9nbycsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcmVxdWlyZXM6IFtJTGFiU2hlbGxdLFxuICBhY3RpdmF0ZTogKGFwcDogSnVweXRlckZyb250RW5kLCBzaGVsbDogSUxhYlNoZWxsKSA9PiB7XG4gICAgY29uc3QgbG9nbyA9IG5ldyBXaWRnZXQoKTtcbiAgICBqdXB5dGVySWNvbi5lbGVtZW50KHtcbiAgICAgIGNvbnRhaW5lcjogbG9nby5ub2RlLFxuICAgICAgZWxlbWVudFBvc2l0aW9uOiAnY2VudGVyJyxcbiAgICAgIG1hcmdpbjogJzJweCAycHggMnB4IDJweCcsXG4gICAgICBoZWlnaHQ6ICdhdXRvJyxcbiAgICAgIHdpZHRoOiAnMzJweCdcbiAgICB9KTtcbiAgICBsb2dvLmlkID0gJ2pwLU1haW5Mb2dvJztcbiAgICBzaGVsbC5hZGQobG9nbywgJ3RvcCcsIHsgcmFuazogMCB9KTtcbiAgfVxufTtcblxuLyoqXG4gKiBUaGUgc2ltcGxlIGludGVyZmFjZSBtb2RlIHN3aXRjaCBpbiB0aGUgc3RhdHVzIGJhci5cbiAqL1xuY29uc3QgbW9kZVN3aXRjaFBsdWdpbjogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLWV4dGVuc2lvbjptb2RlLXN3aXRjaCcsXG4gIHJlcXVpcmVzOiBbSUxhYlNoZWxsLCBJVHJhbnNsYXRvcl0sXG4gIG9wdGlvbmFsOiBbSVN0YXR1c0JhciwgSVNldHRpbmdSZWdpc3RyeV0sXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgbGFiU2hlbGw6IElMYWJTaGVsbCxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcixcbiAgICBzdGF0dXNCYXI6IElTdGF0dXNCYXIgfCBudWxsLFxuICAgIHNldHRpbmdSZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSB8IG51bGxcbiAgKSA9PiB7XG4gICAgaWYgKHN0YXR1c0JhciA9PT0gbnVsbCkge1xuICAgICAgLy8gQmFpbCBlYXJseVxuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IG1vZGVTd2l0Y2ggPSBuZXcgU3dpdGNoKCk7XG4gICAgbW9kZVN3aXRjaC5pZCA9ICdqcC1zaW5nbGUtZG9jdW1lbnQtbW9kZSc7XG5cbiAgICBtb2RlU3dpdGNoLnZhbHVlQ2hhbmdlZC5jb25uZWN0KChfLCBhcmdzKSA9PiB7XG4gICAgICBsYWJTaGVsbC5tb2RlID0gYXJncy5uZXdWYWx1ZSA/ICdzaW5nbGUtZG9jdW1lbnQnIDogJ211bHRpcGxlLWRvY3VtZW50JztcbiAgICB9KTtcbiAgICBsYWJTaGVsbC5tb2RlQ2hhbmdlZC5jb25uZWN0KChfLCBtb2RlKSA9PiB7XG4gICAgICBtb2RlU3dpdGNoLnZhbHVlID0gbW9kZSA9PT0gJ3NpbmdsZS1kb2N1bWVudCc7XG4gICAgfSk7XG5cbiAgICBpZiAoc2V0dGluZ1JlZ2lzdHJ5KSB7XG4gICAgICBjb25zdCBsb2FkU2V0dGluZ3MgPSBzZXR0aW5nUmVnaXN0cnkubG9hZChzaGVsbC5pZCk7XG4gICAgICBjb25zdCB1cGRhdGVTZXR0aW5ncyA9IChzZXR0aW5nczogSVNldHRpbmdSZWdpc3RyeS5JU2V0dGluZ3MpOiB2b2lkID0+IHtcbiAgICAgICAgY29uc3Qgc3RhcnRNb2RlID0gc2V0dGluZ3MuZ2V0KCdzdGFydE1vZGUnKS5jb21wb3NpdGUgYXMgc3RyaW5nO1xuICAgICAgICBpZiAoc3RhcnRNb2RlKSB7XG4gICAgICAgICAgbGFiU2hlbGwubW9kZSA9XG4gICAgICAgICAgICBzdGFydE1vZGUgPT09ICdzaW5nbGUnID8gJ3NpbmdsZS1kb2N1bWVudCcgOiAnbXVsdGlwbGUtZG9jdW1lbnQnO1xuICAgICAgICB9XG4gICAgICB9O1xuXG4gICAgICBQcm9taXNlLmFsbChbbG9hZFNldHRpbmdzLCBhcHAucmVzdG9yZWRdKVxuICAgICAgICAudGhlbigoW3NldHRpbmdzXSkgPT4ge1xuICAgICAgICAgIHVwZGF0ZVNldHRpbmdzKHNldHRpbmdzKTtcbiAgICAgICAgfSlcbiAgICAgICAgLmNhdGNoKChyZWFzb246IEVycm9yKSA9PiB7XG4gICAgICAgICAgY29uc29sZS5lcnJvcihyZWFzb24ubWVzc2FnZSk7XG4gICAgICAgIH0pO1xuICAgIH1cblxuICAgIG1vZGVTd2l0Y2gudmFsdWUgPSBsYWJTaGVsbC5tb2RlID09PSAnc2luZ2xlLWRvY3VtZW50JztcblxuICAgIC8vIFNob3cgdGhlIGN1cnJlbnQgZmlsZSBicm93c2VyIHNob3J0Y3V0IGluIGl0cyB0aXRsZS5cbiAgICBjb25zdCB1cGRhdGVNb2RlU3dpdGNoVGl0bGUgPSAoKSA9PiB7XG4gICAgICBjb25zdCBiaW5kaW5nID0gYXBwLmNvbW1hbmRzLmtleUJpbmRpbmdzLmZpbmQoXG4gICAgICAgIGIgPT4gYi5jb21tYW5kID09PSAnYXBwbGljYXRpb246dG9nZ2xlLW1vZGUnXG4gICAgICApO1xuICAgICAgaWYgKGJpbmRpbmcpIHtcbiAgICAgICAgY29uc3Qga3MgPSBDb21tYW5kUmVnaXN0cnkuZm9ybWF0S2V5c3Ryb2tlKGJpbmRpbmcua2V5cy5qb2luKCcgJykpO1xuICAgICAgICBtb2RlU3dpdGNoLmNhcHRpb24gPSB0cmFucy5fXygnU2ltcGxlIEludGVyZmFjZSAoJTEpJywga3MpO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgbW9kZVN3aXRjaC5jYXB0aW9uID0gdHJhbnMuX18oJ1NpbXBsZSBJbnRlcmZhY2UnKTtcbiAgICAgIH1cbiAgICB9O1xuICAgIHVwZGF0ZU1vZGVTd2l0Y2hUaXRsZSgpO1xuICAgIGFwcC5jb21tYW5kcy5rZXlCaW5kaW5nQ2hhbmdlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgIHVwZGF0ZU1vZGVTd2l0Y2hUaXRsZSgpO1xuICAgIH0pO1xuXG4gICAgbW9kZVN3aXRjaC5sYWJlbCA9IHRyYW5zLl9fKCdTaW1wbGUnKTtcblxuICAgIHN0YXR1c0Jhci5yZWdpc3RlclN0YXR1c0l0ZW0obW9kZVN3aXRjaFBsdWdpbi5pZCwge1xuICAgICAgaXRlbTogbW9kZVN3aXRjaCxcbiAgICAgIGFsaWduOiAnbGVmdCcsXG4gICAgICByYW5rOiAtMVxuICAgIH0pO1xuICB9LFxuICBhdXRvU3RhcnQ6IHRydWVcbn07XG5cbi8qKlxuICogRXhwb3J0IHRoZSBwbHVnaW5zIGFzIGRlZmF1bHQuXG4gKi9cbmNvbnN0IHBsdWdpbnM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxhbnk+W10gPSBbXG4gIGNvbnRleHRNZW51UGx1Z2luLFxuICBkaXJ0eSxcbiAgbWFpbixcbiAgbWFpbkNvbW1hbmRzLFxuICBsYXlvdXQsXG4gIHJvdXRlcixcbiAgdHJlZSxcbiAgbm90Zm91bmQsXG4gIGJ1c3ksXG4gIHNoZWxsLFxuICBzdGF0dXMsXG4gIGluZm8sXG4gIHBhdGhzLFxuICBwcm9wZXJ0eUluc3BlY3RvcixcbiAgSnVweXRlckxvZ28sXG4gIHRvcGJhclxuXTtcblxuZXhwb3J0IGRlZmF1bHQgcGx1Z2lucztcblxubmFtZXNwYWNlIFByaXZhdGUge1xuICBhc3luYyBmdW5jdGlvbiBkaXNwbGF5SW5mb3JtYXRpb24odHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgY29uc3QgcmVzdWx0ID0gYXdhaXQgc2hvd0RpYWxvZyh7XG4gICAgICB0aXRsZTogdHJhbnMuX18oJ0luZm9ybWF0aW9uJyksXG4gICAgICBib2R5OiB0cmFucy5fXyhcbiAgICAgICAgJ0NvbnRleHQgbWVudSBjdXN0b21pemF0aW9uIGhhcyBjaGFuZ2VkLiBZb3Ugd2lsbCBuZWVkIHRvIHJlbG9hZCBOb3RlYm9vayB0byBzZWUgdGhlIGNoYW5nZXMuJ1xuICAgICAgKSxcbiAgICAgIGJ1dHRvbnM6IFtcbiAgICAgICAgRGlhbG9nLmNhbmNlbEJ1dHRvbigpLFxuICAgICAgICBEaWFsb2cub2tCdXR0b24oeyBsYWJlbDogdHJhbnMuX18oJ1JlbG9hZCcpIH0pXG4gICAgICBdXG4gICAgfSk7XG5cbiAgICBpZiAocmVzdWx0LmJ1dHRvbi5hY2NlcHQpIHtcbiAgICAgIGxvY2F0aW9uLnJlbG9hZCgpO1xuICAgIH1cbiAgfVxuXG4gIGV4cG9ydCBhc3luYyBmdW5jdGlvbiBsb2FkU2V0dGluZ3NDb250ZXh0TWVudShcbiAgICBjb250ZXh0TWVudTogQ29udGV4dE1lbnVTdmcsXG4gICAgcmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnksXG4gICAgbWVudUZhY3Rvcnk6IChvcHRpb25zOiBJU2V0dGluZ1JlZ2lzdHJ5LklNZW51KSA9PiBSYW5rZWRNZW51LFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yXG4gICk6IFByb21pc2U8dm9pZD4ge1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgY29uc3QgcGx1Z2luSWQgPSBjb250ZXh0TWVudVBsdWdpbi5pZDtcbiAgICBsZXQgY2Fub25pY2FsOiBJU2V0dGluZ1JlZ2lzdHJ5LklTY2hlbWEgfCBudWxsID0gbnVsbDtcbiAgICBsZXQgbG9hZGVkOiB7IFtuYW1lOiBzdHJpbmddOiBJU2V0dGluZ1JlZ2lzdHJ5LklDb250ZXh0TWVudUl0ZW1bXSB9ID0ge307XG5cbiAgICAvKipcbiAgICAgKiBQb3B1bGF0ZSB0aGUgcGx1Z2luJ3Mgc2NoZW1hIGRlZmF1bHRzLlxuICAgICAqXG4gICAgICogV2Uga2VlcCB0cmFjayBvZiBkaXNhYmxlZCBlbnRyaWVzIGluIGNhc2UgdGhlIHBsdWdpbiBpcyBsb2FkZWRcbiAgICAgKiBhZnRlciB0aGUgbWVudSBpbml0aWFsaXphdGlvbi5cbiAgICAgKi9cbiAgICBmdW5jdGlvbiBwb3B1bGF0ZShzY2hlbWE6IElTZXR0aW5nUmVnaXN0cnkuSVNjaGVtYSkge1xuICAgICAgbG9hZGVkID0ge307XG4gICAgICBjb25zdCBwbHVnaW5EZWZhdWx0cyA9IE9iamVjdC5rZXlzKHJlZ2lzdHJ5LnBsdWdpbnMpXG4gICAgICAgIC5tYXAocGx1Z2luID0+IHtcbiAgICAgICAgICBjb25zdCBpdGVtcyA9XG4gICAgICAgICAgICByZWdpc3RyeS5wbHVnaW5zW3BsdWdpbl0hLnNjaGVtYVsnanVweXRlci5sYWIubWVudXMnXT8uY29udGV4dCA/P1xuICAgICAgICAgICAgW107XG4gICAgICAgICAgbG9hZGVkW3BsdWdpbl0gPSBpdGVtcztcbiAgICAgICAgICByZXR1cm4gaXRlbXM7XG4gICAgICAgIH0pXG4gICAgICAgIC5jb25jYXQoW3NjaGVtYVsnanVweXRlci5sYWIubWVudXMnXT8uY29udGV4dCA/PyBbXV0pXG4gICAgICAgIC5yZWR1Y2VSaWdodChcbiAgICAgICAgICAoXG4gICAgICAgICAgICBhY2M6IElTZXR0aW5nUmVnaXN0cnkuSUNvbnRleHRNZW51SXRlbVtdLFxuICAgICAgICAgICAgdmFsOiBJU2V0dGluZ1JlZ2lzdHJ5LklDb250ZXh0TWVudUl0ZW1bXVxuICAgICAgICAgICkgPT4gU2V0dGluZ1JlZ2lzdHJ5LnJlY29uY2lsZUl0ZW1zKGFjYywgdmFsLCB0cnVlKSxcbiAgICAgICAgICBbXVxuICAgICAgICApITtcblxuICAgICAgLy8gQXBwbHkgZGVmYXVsdCB2YWx1ZSBhcyBsYXN0IHN0ZXAgdG8gdGFrZSBpbnRvIGFjY291bnQgb3ZlcnJpZGVzLmpzb25cbiAgICAgIC8vIFRoZSBzdGFuZGFyZCBkZWZhdWx0IGJlaW5nIFtdIGFzIHRoZSBwbHVnaW4gbXVzdCB1c2UgYGp1cHl0ZXIubGFiLm1lbnVzLmNvbnRleHRgXG4gICAgICAvLyB0byBkZWZpbmUgdGhlaXIgZGVmYXVsdCB2YWx1ZS5cbiAgICAgIHNjaGVtYS5wcm9wZXJ0aWVzIS5jb250ZXh0TWVudS5kZWZhdWx0ID0gU2V0dGluZ1JlZ2lzdHJ5LnJlY29uY2lsZUl0ZW1zKFxuICAgICAgICBwbHVnaW5EZWZhdWx0cyxcbiAgICAgICAgc2NoZW1hLnByb3BlcnRpZXMhLmNvbnRleHRNZW51LmRlZmF1bHQgYXMgYW55W10sXG4gICAgICAgIHRydWVcbiAgICAgICkhXG4gICAgICAgIC8vIGZsYXR0ZW4gb25lIGxldmVsXG4gICAgICAgIC5zb3J0KChhLCBiKSA9PiAoYS5yYW5rID8/IEluZmluaXR5KSAtIChiLnJhbmsgPz8gSW5maW5pdHkpKTtcbiAgICB9XG5cbiAgICAvLyBUcmFuc2Zvcm0gdGhlIHBsdWdpbiBvYmplY3QgdG8gcmV0dXJuIGRpZmZlcmVudCBzY2hlbWEgdGhhbiB0aGUgZGVmYXVsdC5cbiAgICByZWdpc3RyeS50cmFuc2Zvcm0ocGx1Z2luSWQsIHtcbiAgICAgIGNvbXBvc2U6IHBsdWdpbiA9PiB7XG4gICAgICAgIC8vIE9ubHkgb3ZlcnJpZGUgdGhlIGNhbm9uaWNhbCBzY2hlbWEgdGhlIGZpcnN0IHRpbWUuXG4gICAgICAgIGlmICghY2Fub25pY2FsKSB7XG4gICAgICAgICAgY2Fub25pY2FsID0gSlNPTkV4dC5kZWVwQ29weShwbHVnaW4uc2NoZW1hKTtcbiAgICAgICAgICBwb3B1bGF0ZShjYW5vbmljYWwpO1xuICAgICAgICB9XG5cbiAgICAgICAgY29uc3QgZGVmYXVsdHMgPSBjYW5vbmljYWwucHJvcGVydGllcz8uY29udGV4dE1lbnU/LmRlZmF1bHQgPz8gW107XG4gICAgICAgIGNvbnN0IHVzZXIgPSB7XG4gICAgICAgICAgLi4ucGx1Z2luLmRhdGEudXNlcixcbiAgICAgICAgICBjb250ZXh0TWVudTogcGx1Z2luLmRhdGEudXNlci5jb250ZXh0TWVudSA/PyBbXVxuICAgICAgICB9O1xuICAgICAgICBjb25zdCBjb21wb3NpdGUgPSB7XG4gICAgICAgICAgLi4ucGx1Z2luLmRhdGEuY29tcG9zaXRlLFxuICAgICAgICAgIGNvbnRleHRNZW51OiBTZXR0aW5nUmVnaXN0cnkucmVjb25jaWxlSXRlbXMoXG4gICAgICAgICAgICBkZWZhdWx0cyBhcyBJU2V0dGluZ1JlZ2lzdHJ5LklDb250ZXh0TWVudUl0ZW1bXSxcbiAgICAgICAgICAgIHVzZXIuY29udGV4dE1lbnUgYXMgSVNldHRpbmdSZWdpc3RyeS5JQ29udGV4dE1lbnVJdGVtW10sXG4gICAgICAgICAgICBmYWxzZVxuICAgICAgICAgIClcbiAgICAgICAgfTtcblxuICAgICAgICBwbHVnaW4uZGF0YSA9IHsgY29tcG9zaXRlLCB1c2VyIH07XG5cbiAgICAgICAgcmV0dXJuIHBsdWdpbjtcbiAgICAgIH0sXG4gICAgICBmZXRjaDogcGx1Z2luID0+IHtcbiAgICAgICAgLy8gT25seSBvdmVycmlkZSB0aGUgY2Fub25pY2FsIHNjaGVtYSB0aGUgZmlyc3QgdGltZS5cbiAgICAgICAgaWYgKCFjYW5vbmljYWwpIHtcbiAgICAgICAgICBjYW5vbmljYWwgPSBKU09ORXh0LmRlZXBDb3B5KHBsdWdpbi5zY2hlbWEpO1xuICAgICAgICAgIHBvcHVsYXRlKGNhbm9uaWNhbCk7XG4gICAgICAgIH1cblxuICAgICAgICByZXR1cm4ge1xuICAgICAgICAgIGRhdGE6IHBsdWdpbi5kYXRhLFxuICAgICAgICAgIGlkOiBwbHVnaW4uaWQsXG4gICAgICAgICAgcmF3OiBwbHVnaW4ucmF3LFxuICAgICAgICAgIHNjaGVtYTogY2Fub25pY2FsLFxuICAgICAgICAgIHZlcnNpb246IHBsdWdpbi52ZXJzaW9uXG4gICAgICAgIH07XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICAvLyBSZXBvcHVsYXRlIHRoZSBjYW5vbmljYWwgdmFyaWFibGUgYWZ0ZXIgdGhlIHNldHRpbmcgcmVnaXN0cnkgaGFzXG4gICAgLy8gcHJlbG9hZGVkIGFsbCBpbml0aWFsIHBsdWdpbnMuXG4gICAgY29uc3Qgc2V0dGluZ3MgPSBhd2FpdCByZWdpc3RyeS5sb2FkKHBsdWdpbklkKTtcblxuICAgIGNvbnN0IGNvbnRleHRJdGVtczogSVNldHRpbmdSZWdpc3RyeS5JQ29udGV4dE1lbnVJdGVtW10gPVxuICAgICAgKHNldHRpbmdzLmNvbXBvc2l0ZS5jb250ZXh0TWVudSBhcyBhbnkpID8/IFtdO1xuXG4gICAgLy8gQ3JlYXRlIG1lbnUgaXRlbSBmb3Igbm9uLWRpc2FibGVkIGVsZW1lbnRcbiAgICBTZXR0aW5nUmVnaXN0cnkuZmlsdGVyRGlzYWJsZWRJdGVtcyhjb250ZXh0SXRlbXMpLmZvckVhY2goaXRlbSA9PiB7XG4gICAgICBNZW51RmFjdG9yeS5hZGRDb250ZXh0SXRlbShcbiAgICAgICAge1xuICAgICAgICAgIC8vIFdlIGhhdmUgdG8gc2V0IHRoZSBkZWZhdWx0IHJhbmsgYmVjYXVzZSBMdW1pbm8gaXMgc29ydGluZyB0aGUgdmlzaWJsZSBpdGVtc1xuICAgICAgICAgIHJhbms6IERFRkFVTFRfQ09OVEVYVF9JVEVNX1JBTkssXG4gICAgICAgICAgLi4uaXRlbVxuICAgICAgICB9LFxuICAgICAgICBjb250ZXh0TWVudSxcbiAgICAgICAgbWVudUZhY3RvcnlcbiAgICAgICk7XG4gICAgfSk7XG5cbiAgICBzZXR0aW5ncy5jaGFuZ2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgLy8gQXMgZXh0ZW5zaW9uIG1heSBjaGFuZ2UgdGhlIGNvbnRleHQgbWVudSB0aHJvdWdoIEFQSSxcbiAgICAgIC8vIHByb21wdCB0aGUgdXNlciB0byByZWxvYWQgaWYgdGhlIG1lbnUgaGFzIGJlZW4gdXBkYXRlZC5cbiAgICAgIGNvbnN0IG5ld0l0ZW1zID0gKHNldHRpbmdzLmNvbXBvc2l0ZS5jb250ZXh0TWVudSBhcyBhbnkpID8/IFtdO1xuICAgICAgaWYgKCFKU09ORXh0LmRlZXBFcXVhbChjb250ZXh0SXRlbXMsIG5ld0l0ZW1zKSkge1xuICAgICAgICB2b2lkIGRpc3BsYXlJbmZvcm1hdGlvbih0cmFucyk7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICByZWdpc3RyeS5wbHVnaW5DaGFuZ2VkLmNvbm5lY3QoYXN5bmMgKHNlbmRlciwgcGx1Z2luKSA9PiB7XG4gICAgICBpZiAocGx1Z2luICE9PSBwbHVnaW5JZCkge1xuICAgICAgICAvLyBJZiB0aGUgcGx1Z2luIGNoYW5nZWQgaXRzIG1lbnUuXG4gICAgICAgIGNvbnN0IG9sZEl0ZW1zID0gbG9hZGVkW3BsdWdpbl0gPz8gW107XG4gICAgICAgIGNvbnN0IG5ld0l0ZW1zID1cbiAgICAgICAgICByZWdpc3RyeS5wbHVnaW5zW3BsdWdpbl0hLnNjaGVtYVsnanVweXRlci5sYWIubWVudXMnXT8uY29udGV4dCA/PyBbXTtcbiAgICAgICAgaWYgKCFKU09ORXh0LmRlZXBFcXVhbChvbGRJdGVtcywgbmV3SXRlbXMpKSB7XG4gICAgICAgICAgaWYgKGxvYWRlZFtwbHVnaW5dKSB7XG4gICAgICAgICAgICAvLyBUaGUgcGx1Z2luIGhhcyBjaGFuZ2VkLCByZXF1ZXN0IHRoZSB1c2VyIHRvIHJlbG9hZCB0aGUgVUlcbiAgICAgICAgICAgIGF3YWl0IGRpc3BsYXlJbmZvcm1hdGlvbih0cmFucyk7XG4gICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIC8vIFRoZSBwbHVnaW4gd2FzIG5vdCB5ZXQgbG9hZGVkIHdoZW4gdGhlIG1lbnUgd2FzIGJ1aWx0ID0+IHVwZGF0ZSB0aGUgbWVudVxuICAgICAgICAgICAgbG9hZGVkW3BsdWdpbl0gPSBKU09ORXh0LmRlZXBDb3B5KG5ld0l0ZW1zKTtcbiAgICAgICAgICAgIC8vIE1lcmdlIHBvdGVudGlhbCBkaXNhYmxlZCBzdGF0ZVxuICAgICAgICAgICAgY29uc3QgdG9BZGQgPVxuICAgICAgICAgICAgICBTZXR0aW5nUmVnaXN0cnkucmVjb25jaWxlSXRlbXMoXG4gICAgICAgICAgICAgICAgbmV3SXRlbXMsXG4gICAgICAgICAgICAgICAgY29udGV4dEl0ZW1zLFxuICAgICAgICAgICAgICAgIGZhbHNlLFxuICAgICAgICAgICAgICAgIGZhbHNlXG4gICAgICAgICAgICAgICkgPz8gW107XG4gICAgICAgICAgICBTZXR0aW5nUmVnaXN0cnkuZmlsdGVyRGlzYWJsZWRJdGVtcyh0b0FkZCkuZm9yRWFjaChpdGVtID0+IHtcbiAgICAgICAgICAgICAgTWVudUZhY3RvcnkuYWRkQ29udGV4dEl0ZW0oXG4gICAgICAgICAgICAgICAge1xuICAgICAgICAgICAgICAgICAgLy8gV2UgaGF2ZSB0byBzZXQgdGhlIGRlZmF1bHQgcmFuayBiZWNhdXNlIEx1bWlubyBpcyBzb3J0aW5nIHRoZSB2aXNpYmxlIGl0ZW1zXG4gICAgICAgICAgICAgICAgICByYW5rOiBERUZBVUxUX0NPTlRFWFRfSVRFTV9SQU5LLFxuICAgICAgICAgICAgICAgICAgLi4uaXRlbVxuICAgICAgICAgICAgICAgIH0sXG4gICAgICAgICAgICAgICAgY29udGV4dE1lbnUsXG4gICAgICAgICAgICAgICAgbWVudUZhY3RvcnlcbiAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgIH0pO1xuICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgfVxuICAgIH0pO1xuICB9XG5cbiAgZXhwb3J0IGZ1bmN0aW9uIGFjdGl2YXRlU2lkZWJhclN3aXRjaGVyKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIGxhYlNoZWxsOiBJTGFiU2hlbGwsXG4gICAgc2V0dGluZ3M6IElTZXR0aW5nUmVnaXN0cnkuSVNldHRpbmdzLFxuICAgIHRyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZVxuICApOiB2b2lkIHtcbiAgICAvLyBBZGQgYSBjb21tYW5kIHRvIHN3aXRjaCBhIHNpZGUgcGFuZWxzJ3Mgc2lkZVxuICAgIGFwcC5jb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuc3dpdGNoU2lkZWJhciwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdTd2l0Y2ggU2lkZWJhciBTaWRlJyksXG4gICAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAgIC8vIEZpcnN0LCB0cnkgdG8gZmluZCB0aGUgY29ycmVjdCBwYW5lbCBiYXNlZCBvbiB0aGUgYXBwbGljYXRpb25cbiAgICAgICAgLy8gY29udGV4dCBtZW51IGNsaWNrLiBCYWlsIGlmIHdlIGRvbid0IGZpbmQgYSBzaWRlYmFyIGZvciB0aGUgd2lkZ2V0LlxuICAgICAgICBjb25zdCBjb250ZXh0Tm9kZTogSFRNTEVsZW1lbnQgfCB1bmRlZmluZWQgPSBhcHAuY29udGV4dE1lbnVIaXRUZXN0KFxuICAgICAgICAgIG5vZGUgPT4gISFub2RlLmRhdGFzZXQuaWRcbiAgICAgICAgKTtcbiAgICAgICAgaWYgKCFjb250ZXh0Tm9kZSkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIGNvbnN0IGlkID0gY29udGV4dE5vZGUuZGF0YXNldFsnaWQnXSE7XG4gICAgICAgIGNvbnN0IGxlZnRQYW5lbCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdqcC1sZWZ0LXN0YWNrJyk7XG4gICAgICAgIGNvbnN0IG5vZGUgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChpZCk7XG5cbiAgICAgICAgbGV0IG5ld0xheW91dDoge1xuICAgICAgICAgICdzaW5nbGUtZG9jdW1lbnQnOiBJTGFiU2hlbGwuSVVzZXJMYXlvdXQ7XG4gICAgICAgICAgJ211bHRpcGxlLWRvY3VtZW50JzogSUxhYlNoZWxsLklVc2VyTGF5b3V0O1xuICAgICAgICB9IHwgbnVsbCA9IG51bGw7XG4gICAgICAgIC8vIE1vdmUgdGhlIHBhbmVsIHRvIHRoZSBvdGhlciBzaWRlLlxuICAgICAgICBpZiAobGVmdFBhbmVsICYmIG5vZGUgJiYgbGVmdFBhbmVsLmNvbnRhaW5zKG5vZGUpKSB7XG4gICAgICAgICAgY29uc3Qgd2lkZ2V0ID0gZmluZChsYWJTaGVsbC53aWRnZXRzKCdsZWZ0JyksIHcgPT4gdy5pZCA9PT0gaWQpO1xuICAgICAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgICAgIG5ld0xheW91dCA9IGxhYlNoZWxsLm1vdmUod2lkZ2V0LCAncmlnaHQnKTtcbiAgICAgICAgICAgIGxhYlNoZWxsLmFjdGl2YXRlQnlJZCh3aWRnZXQuaWQpO1xuICAgICAgICAgIH1cbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICBjb25zdCB3aWRnZXQgPSBmaW5kKGxhYlNoZWxsLndpZGdldHMoJ3JpZ2h0JyksIHcgPT4gdy5pZCA9PT0gaWQpO1xuICAgICAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgICAgIG5ld0xheW91dCA9IGxhYlNoZWxsLm1vdmUod2lkZ2V0LCAnbGVmdCcpO1xuICAgICAgICAgICAgbGFiU2hlbGwuYWN0aXZhdGVCeUlkKHdpZGdldC5pZCk7XG4gICAgICAgICAgfVxuICAgICAgICB9XG5cbiAgICAgICAgaWYgKG5ld0xheW91dCkge1xuICAgICAgICAgIHNldHRpbmdzXG4gICAgICAgICAgICAuc2V0KCdsYXlvdXQnLCB7XG4gICAgICAgICAgICAgIHNpbmdsZTogbmV3TGF5b3V0WydzaW5nbGUtZG9jdW1lbnQnXSxcbiAgICAgICAgICAgICAgbXVsdGlwbGU6IG5ld0xheW91dFsnbXVsdGlwbGUtZG9jdW1lbnQnXVxuICAgICAgICAgICAgfSBhcyBhbnkpXG4gICAgICAgICAgICAuY2F0Y2gocmVhc29uID0+IHtcbiAgICAgICAgICAgICAgY29uc29sZS5lcnJvcihcbiAgICAgICAgICAgICAgICAnRmFpbGVkIHRvIHNhdmUgdXNlciBsYXlvdXQgY3VzdG9taXphdGlvbi4nLFxuICAgICAgICAgICAgICAgIHJlYXNvblxuICAgICAgICAgICAgICApO1xuICAgICAgICAgICAgfSk7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9KTtcblxuICAgIGFwcC5jb21tYW5kcy5jb21tYW5kRXhlY3V0ZWQuY29ubmVjdCgocmVnaXN0cnksIGV4ZWN1dGVkKSA9PiB7XG4gICAgICBpZiAoZXhlY3V0ZWQuaWQgPT09IENvbW1hbmRJRHMucmVzZXRMYXlvdXQpIHtcbiAgICAgICAgc2V0dGluZ3MucmVtb3ZlKCdsYXlvdXQnKS5jYXRjaChyZWFzb24gPT4ge1xuICAgICAgICAgIGNvbnNvbGUuZXJyb3IoJ0ZhaWxlZCB0byByZW1vdmUgdXNlciBsYXlvdXQgY3VzdG9taXphdGlvbi4nLCByZWFzb24pO1xuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9KTtcbiAgfVxufVxuIiwiLypcbiAqIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuICogRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbiAqL1xuXG5pbXBvcnQge1xuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpblxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQge1xuICBjcmVhdGVUb29sYmFyRmFjdG9yeSxcbiAgSVRvb2xiYXJXaWRnZXRSZWdpc3RyeSxcbiAgc2V0VG9vbGJhclxufSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBJU2V0dGluZ1JlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2V0dGluZ3JlZ2lzdHJ5JztcbmltcG9ydCB7IElUcmFuc2xhdG9yLCBudWxsVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IFRvb2xiYXIgfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcblxuY29uc3QgVE9QQkFSX0ZBQ1RPUlkgPSAnVG9wQmFyJztcblxuLyoqXG4gKiBBIHBsdWdpbiBhZGRpbmcgYSB0b29sYmFyIHRvIHRoZSB0b3AgYXJlYS5cbiAqL1xuZXhwb3J0IGNvbnN0IHRvcGJhcjogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLWV4dGVuc2lvbjp0b3AtYmFyJyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICByZXF1aXJlczogW0lTZXR0aW5nUmVnaXN0cnksIElUb29sYmFyV2lkZ2V0UmVnaXN0cnldLFxuICBvcHRpb25hbDogW0lUcmFuc2xhdG9yXSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICBzZXR0aW5nUmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnksXG4gICAgdG9vbGJhclJlZ2lzdHJ5OiBJVG9vbGJhcldpZGdldFJlZ2lzdHJ5LFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yIHwgbnVsbFxuICApID0+IHtcbiAgICBjb25zdCB0b29sYmFyID0gbmV3IFRvb2xiYXIoKTtcbiAgICB0b29sYmFyLmlkID0gJ2pwLXRvcC1iYXInO1xuXG4gICAgLy8gU2V0IHRvb2xiYXJcbiAgICBzZXRUb29sYmFyKFxuICAgICAgdG9vbGJhcixcbiAgICAgIGNyZWF0ZVRvb2xiYXJGYWN0b3J5KFxuICAgICAgICB0b29sYmFyUmVnaXN0cnksXG4gICAgICAgIHNldHRpbmdSZWdpc3RyeSxcbiAgICAgICAgVE9QQkFSX0ZBQ1RPUlksXG4gICAgICAgIHRvcGJhci5pZCxcbiAgICAgICAgdHJhbnNsYXRvciA/PyBudWxsVHJhbnNsYXRvclxuICAgICAgKSxcbiAgICAgIHRvb2xiYXJcbiAgICApO1xuXG4gICAgYXBwLnNoZWxsLmFkZCh0b29sYmFyLCAndG9wJywgeyByYW5rOiA5MDAgfSk7XG4gIH1cbn07XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=