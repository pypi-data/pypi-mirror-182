"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_mainmenu-extension_lib_index_js"],{

/***/ "../../packages/mainmenu-extension/lib/index.js":
/*!******************************************************!*\
  !*** ../../packages/mainmenu-extension/lib/index.js ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CommandIDs": () => (/* binding */ CommandIDs),
/* harmony export */   "createEditMenu": () => (/* binding */ createEditMenu),
/* harmony export */   "createFileMenu": () => (/* binding */ createFileMenu),
/* harmony export */   "createHelpMenu": () => (/* binding */ createHelpMenu),
/* harmony export */   "createKernelMenu": () => (/* binding */ createKernelMenu),
/* harmony export */   "createRunMenu": () => (/* binding */ createRunMenu),
/* harmony export */   "createTabsMenu": () => (/* binding */ createTabsMenu),
/* harmony export */   "createViewMenu": () => (/* binding */ createViewMenu),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/mainmenu */ "webpack/sharing/consume/default/@jupyterlab/mainmenu/@jupyterlab/mainmenu");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_10__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module mainmenu-extension
 */











const PLUGIN_ID = '@jupyterlab/mainmenu-extension:plugin';
/**
 * A namespace for command IDs of semantic extension points.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.openEdit = 'editmenu:open';
    CommandIDs.undo = 'editmenu:undo';
    CommandIDs.redo = 'editmenu:redo';
    CommandIDs.clearCurrent = 'editmenu:clear-current';
    CommandIDs.clearAll = 'editmenu:clear-all';
    CommandIDs.find = 'editmenu:find';
    CommandIDs.goToLine = 'editmenu:go-to-line';
    CommandIDs.openFile = 'filemenu:open';
    CommandIDs.closeAndCleanup = 'filemenu:close-and-cleanup';
    CommandIDs.createConsole = 'filemenu:create-console';
    CommandIDs.shutdown = 'filemenu:shutdown';
    CommandIDs.logout = 'filemenu:logout';
    CommandIDs.openKernel = 'kernelmenu:open';
    CommandIDs.interruptKernel = 'kernelmenu:interrupt';
    CommandIDs.reconnectToKernel = 'kernelmenu:reconnect-to-kernel';
    CommandIDs.restartKernel = 'kernelmenu:restart';
    CommandIDs.restartKernelAndClear = 'kernelmenu:restart-and-clear';
    CommandIDs.changeKernel = 'kernelmenu:change';
    CommandIDs.shutdownKernel = 'kernelmenu:shutdown';
    CommandIDs.shutdownAllKernels = 'kernelmenu:shutdownAll';
    CommandIDs.openView = 'viewmenu:open';
    CommandIDs.wordWrap = 'viewmenu:word-wrap';
    CommandIDs.lineNumbering = 'viewmenu:line-numbering';
    CommandIDs.matchBrackets = 'viewmenu:match-brackets';
    CommandIDs.openRun = 'runmenu:open';
    CommandIDs.run = 'runmenu:run';
    CommandIDs.runAll = 'runmenu:run-all';
    CommandIDs.restartAndRunAll = 'runmenu:restart-and-run-all';
    CommandIDs.runAbove = 'runmenu:run-above';
    CommandIDs.runBelow = 'runmenu:run-below';
    CommandIDs.openTabs = 'tabsmenu:open';
    CommandIDs.activateById = 'tabsmenu:activate-by-id';
    CommandIDs.activatePreviouslyUsedTab = 'tabsmenu:activate-previously-used-tab';
    CommandIDs.openSettings = 'settingsmenu:open';
    CommandIDs.openHelp = 'helpmenu:open';
    CommandIDs.getKernel = 'helpmenu:get-kernel';
    CommandIDs.openFirst = 'mainmenu:open-first';
})(CommandIDs || (CommandIDs = {}));
/**
 * A service providing an interface to the main menu.
 */
const plugin = {
    id: PLUGIN_ID,
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.IRouter, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.ITranslator],
    optional: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.ISettingRegistry],
    provides: _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__.IMainMenu,
    activate: async (app, router, translator, palette, labShell, registry) => {
        const { commands } = app;
        const trans = translator.load('jupyterlab');
        const menu = new _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__.MainMenu(commands);
        menu.id = 'jp-MainMenu';
        menu.addClass('jp-scrollbar-tiny');
        // Built menu from settings
        if (registry) {
            await Private.loadSettingsMenu(registry, (aMenu) => {
                menu.addMenu(aMenu, { rank: aMenu.rank });
            }, options => _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__.MainMenu.generateMenu(commands, options, trans), translator);
        }
        // Only add quit button if the back-end supports it by checking page config.
        const quitButton = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getOption('quitButton').toLowerCase();
        menu.fileMenu.quitEntry = quitButton === 'true';
        // Create the application menus.
        createEditMenu(app, menu.editMenu, trans);
        createFileMenu(app, menu.fileMenu, router, trans);
        createKernelMenu(app, menu.kernelMenu, trans);
        createRunMenu(app, menu.runMenu, trans);
        createViewMenu(app, menu.viewMenu, trans);
        createHelpMenu(app, menu.helpMenu, trans);
        // The tabs menu relies on lab shell functionality.
        if (labShell) {
            createTabsMenu(app, menu.tabsMenu, labShell, trans);
        }
        // Create commands to open the main application menus.
        const activateMenu = (item) => {
            menu.activeMenu = item;
            menu.openActiveMenu();
        };
        commands.addCommand(CommandIDs.openEdit, {
            label: trans.__('Open Edit Menu'),
            execute: () => activateMenu(menu.editMenu)
        });
        commands.addCommand(CommandIDs.openFile, {
            label: trans.__('Open File Menu'),
            execute: () => activateMenu(menu.fileMenu)
        });
        commands.addCommand(CommandIDs.openKernel, {
            label: trans.__('Open Kernel Menu'),
            execute: () => activateMenu(menu.kernelMenu)
        });
        commands.addCommand(CommandIDs.openRun, {
            label: trans.__('Open Run Menu'),
            execute: () => activateMenu(menu.runMenu)
        });
        commands.addCommand(CommandIDs.openView, {
            label: trans.__('Open View Menu'),
            execute: () => activateMenu(menu.viewMenu)
        });
        commands.addCommand(CommandIDs.openSettings, {
            label: trans.__('Open Settings Menu'),
            execute: () => activateMenu(menu.settingsMenu)
        });
        commands.addCommand(CommandIDs.openTabs, {
            label: trans.__('Open Tabs Menu'),
            execute: () => activateMenu(menu.tabsMenu)
        });
        commands.addCommand(CommandIDs.openHelp, {
            label: trans.__('Open Help Menu'),
            execute: () => activateMenu(menu.helpMenu)
        });
        commands.addCommand(CommandIDs.openFirst, {
            label: trans.__('Open First Menu'),
            execute: () => {
                menu.activeIndex = 0;
                menu.openActiveMenu();
            }
        });
        if (palette) {
            // Add some of the commands defined here to the command palette.
            palette.addItem({
                command: CommandIDs.shutdown,
                category: trans.__('Main Area')
            });
            palette.addItem({
                command: CommandIDs.logout,
                category: trans.__('Main Area')
            });
            palette.addItem({
                command: CommandIDs.shutdownAllKernels,
                category: trans.__('Kernel Operations')
            });
            palette.addItem({
                command: CommandIDs.activatePreviouslyUsedTab,
                category: trans.__('Main Area')
            });
        }
        app.shell.add(menu, 'menu', { rank: 100 });
        return menu;
    }
};
/**
 * Create the basic `Edit` menu.
 */
function createEditMenu(app, menu, trans) {
    const commands = app.commands;
    // Add the undo/redo commands the the Edit menu.
    commands.addCommand(CommandIDs.undo, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.undoers.undo, {
        label: trans.__('Undo')
    }, trans));
    commands.addCommand(CommandIDs.redo, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.undoers.redo, {
        label: trans.__('Redo')
    }, trans));
    // Add the clear commands to the Edit menu.
    commands.addCommand(CommandIDs.clearCurrent, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.clearers.clearCurrent, {
        label: trans.__('Clear')
    }, trans));
    commands.addCommand(CommandIDs.clearAll, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.clearers.clearAll, {
        label: trans.__('Clear All')
    }, trans));
    commands.addCommand(CommandIDs.goToLine, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.goToLiners, {
        label: trans.__('Go to Line…')
    }, trans));
}
/**
 * Create the basic `File` menu.
 */
function createFileMenu(app, menu, router, trans) {
    const commands = app.commands;
    // Add a delegator command for closing and cleaning up an activity.
    // This one is a bit different, in that we consider it enabled
    // even if it cannot find a delegate for the activity.
    // In that case, we instead call the application `close` command.
    commands.addCommand(CommandIDs.closeAndCleanup, Object.assign(Object.assign({}, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.closeAndCleaners, {
        execute: 'application:close',
        label: trans.__('Close and Shut Down'),
        isEnabled: true
    }, trans)), { isEnabled: () => !!app.shell.currentWidget && !!app.shell.currentWidget.title.closable }));
    // Add a delegator command for creating a console for an activity.
    commands.addCommand(CommandIDs.createConsole, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.consoleCreators, {
        label: trans.__('New Console for Activity')
    }, trans));
    commands.addCommand(CommandIDs.shutdown, {
        label: trans.__('Shut Down'),
        caption: trans.__('Shut down JupyterLab'),
        isVisible: () => menu.quitEntry,
        isEnabled: () => menu.quitEntry,
        execute: () => {
            return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                title: trans.__('Shutdown confirmation'),
                body: trans.__('Please confirm you want to shut down JupyterLab.'),
                buttons: [
                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton(),
                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.warnButton({ label: trans.__('Shut Down') })
                ]
            }).then(async (result) => {
                if (result.button.accept) {
                    const setting = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_4__.ServerConnection.makeSettings();
                    const apiURL = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.URLExt.join(setting.baseUrl, 'api/shutdown');
                    // Shutdown all kernel and terminal sessions before shutting down the server
                    // If this fails, we continue execution so we can post an api/shutdown request
                    try {
                        await Promise.all([
                            app.serviceManager.sessions.shutdownAll(),
                            app.serviceManager.terminals.shutdownAll()
                        ]);
                    }
                    catch (e) {
                        // Do nothing
                        console.log(`Failed to shutdown sessions and terminals: ${e}`);
                    }
                    return _jupyterlab_services__WEBPACK_IMPORTED_MODULE_4__.ServerConnection.makeRequest(apiURL, { method: 'POST' }, setting)
                        .then(result => {
                        if (result.ok) {
                            // Close this window if the shutdown request has been successful
                            const body = document.createElement('div');
                            const p1 = document.createElement('p');
                            p1.textContent = trans.__('You have shut down the Jupyter server. You can now close this tab.');
                            const p2 = document.createElement('p');
                            p2.textContent = trans.__('To use JupyterLab again, you will need to relaunch it.');
                            body.appendChild(p1);
                            body.appendChild(p2);
                            void (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                                title: trans.__('Server stopped'),
                                body: new _lumino_widgets__WEBPACK_IMPORTED_MODULE_10__.Widget({ node: body }),
                                buttons: []
                            });
                            window.close();
                        }
                        else {
                            throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_4__.ServerConnection.ResponseError(result);
                        }
                    })
                        .catch(data => {
                        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_4__.ServerConnection.NetworkError(data);
                    });
                }
            });
        }
    });
    commands.addCommand(CommandIDs.logout, {
        label: trans.__('Log Out'),
        caption: trans.__('Log out of JupyterLab'),
        isVisible: () => menu.quitEntry,
        isEnabled: () => menu.quitEntry,
        execute: () => {
            router.navigate('/logout', { hard: true });
        }
    });
}
/**
 * Create the basic `Kernel` menu.
 */
function createKernelMenu(app, menu, trans) {
    const commands = app.commands;
    commands.addCommand(CommandIDs.interruptKernel, Object.assign(Object.assign({}, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.kernelUsers.interruptKernel, {
        label: trans.__('Interrupt Kernel'),
        caption: trans.__('Interrupt the kernel')
    }, trans)), { icon: args => (args.toolbar ? _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7__.stopIcon : undefined) }));
    commands.addCommand(CommandIDs.reconnectToKernel, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.kernelUsers.reconnectToKernel, {
        label: trans.__('Reconnect to Kernel')
    }, trans));
    commands.addCommand(CommandIDs.restartKernel, Object.assign(Object.assign({}, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.kernelUsers.restartKernel, {
        label: trans.__('Restart Kernel…'),
        caption: trans.__('Restart the kernel')
    }, trans)), { icon: args => (args.toolbar ? _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7__.refreshIcon : undefined) }));
    commands.addCommand(CommandIDs.restartKernelAndClear, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, [menu.kernelUsers.restartKernel, menu.kernelUsers.clearWidget], {
        label: trans.__('Restart Kernel and Clear…')
    }, trans));
    commands.addCommand(CommandIDs.changeKernel, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.kernelUsers.changeKernel, {
        label: trans.__('Change Kernel…')
    }, trans));
    commands.addCommand(CommandIDs.shutdownKernel, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.kernelUsers.shutdownKernel, {
        label: trans.__('Shut Down Kernel'),
        caption: trans.__('Shut down kernel')
    }, trans));
    commands.addCommand(CommandIDs.shutdownAllKernels, {
        label: trans.__('Shut Down All Kernels…'),
        isEnabled: () => {
            return app.serviceManager.sessions.running().next() !== undefined;
        },
        execute: () => {
            return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                title: trans.__('Shut Down All?'),
                body: trans.__('Shut down all kernels?'),
                buttons: [
                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton({ label: trans.__('Dismiss') }),
                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.warnButton({ label: trans.__('Shut Down All') })
                ]
            }).then(result => {
                if (result.button.accept) {
                    return app.serviceManager.sessions.shutdownAll();
                }
            });
        }
    });
}
/**
 * Create the basic `View` menu.
 */
function createViewMenu(app, menu, trans) {
    const commands = app.commands;
    commands.addCommand(CommandIDs.lineNumbering, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.editorViewers.toggleLineNumbers, {
        label: trans.__('Show Line Numbers')
    }, trans));
    commands.addCommand(CommandIDs.matchBrackets, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.editorViewers.toggleMatchBrackets, {
        label: trans.__('Match Brackets')
    }, trans));
    commands.addCommand(CommandIDs.wordWrap, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.editorViewers.toggleWordWrap, {
        label: trans.__('Wrap Words')
    }, trans));
}
/**
 * Create the basic `Run` menu.
 */
function createRunMenu(app, menu, trans) {
    const commands = app.commands;
    commands.addCommand(CommandIDs.run, Object.assign(Object.assign({}, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.codeRunners.run, {
        label: trans.__('Run Selected'),
        caption: trans.__('Run Selected')
    }, trans)), { icon: args => (args.toolbar ? _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7__.runIcon : undefined) }));
    commands.addCommand(CommandIDs.runAll, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.codeRunners.runAll, {
        label: trans.__('Run All'),
        caption: trans.__('Run All')
    }, trans));
    commands.addCommand(CommandIDs.restartAndRunAll, Object.assign(Object.assign({}, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, [menu.codeRunners.restart, menu.codeRunners.runAll], {
        label: trans.__('Restart Kernel and Run All'),
        caption: trans.__('Restart Kernel and Run All')
    }, trans)), { icon: args => (args.toolbar ? _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_7__.fastForwardIcon : undefined) }));
}
/**
 * Create the basic `Tabs` menu.
 */
function createTabsMenu(app, menu, labShell, trans) {
    const commands = app.commands;
    // A list of the active tabs in the main area.
    const tabGroup = [];
    // A disposable for getting rid of the out-of-date tabs list.
    let disposable;
    // Command to activate a widget by id.
    commands.addCommand(CommandIDs.activateById, {
        label: args => {
            if (args.id === undefined) {
                return trans.__('Activate a widget by its `id`.');
            }
            const id = args['id'] || '';
            const widget = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_8__.find)(app.shell.widgets('main'), w => w.id === id);
            return (widget && widget.title.label) || '';
        },
        isToggled: args => {
            const id = args['id'] || '';
            return !!app.shell.currentWidget && app.shell.currentWidget.id === id;
        },
        execute: args => app.shell.activateById(args['id'] || '')
    });
    let previousId = '';
    // Command to toggle between the current
    // tab and the last modified tab.
    commands.addCommand(CommandIDs.activatePreviouslyUsedTab, {
        label: trans.__('Activate Previously Used Tab'),
        isEnabled: () => !!previousId,
        execute: () => commands.execute(CommandIDs.activateById, { id: previousId })
    });
    if (labShell) {
        void app.restored.then(() => {
            // Iterate over the current widgets in the
            // main area, and add them to the tab group
            // of the menu.
            const populateTabs = () => {
                // remove the previous tab list
                if (disposable && !disposable.isDisposed) {
                    disposable.dispose();
                }
                tabGroup.length = 0;
                let isPreviouslyUsedTabAttached = false;
                (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_8__.each)(app.shell.widgets('main'), widget => {
                    if (widget.id === previousId) {
                        isPreviouslyUsedTabAttached = true;
                    }
                    tabGroup.push({
                        command: CommandIDs.activateById,
                        args: { id: widget.id }
                    });
                });
                disposable = menu.addGroup(tabGroup, 1);
                previousId = isPreviouslyUsedTabAttached ? previousId : '';
            };
            populateTabs();
            labShell.layoutModified.connect(() => {
                populateTabs();
            });
            // Update the ID of the previous active tab if a new tab is selected.
            labShell.currentChanged.connect((_, args) => {
                const widget = args.oldValue;
                if (!widget) {
                    return;
                }
                previousId = widget.id;
            });
        });
    }
}
/**
 * Create the basic `Help` menu.
 */
function createHelpMenu(app, menu, trans) {
    app.commands.addCommand(CommandIDs.getKernel, (0,_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.createSemanticCommand)(app, menu.getKernel, {
        label: trans.__('Get Kernel'),
        isVisible: false
    }, trans));
}
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);
/**
 * A namespace for Private data.
 */
var Private;
(function (Private) {
    async function displayInformation(trans) {
        const result = await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
            title: trans.__('Information'),
            body: trans.__('Menu customization has changed. You will need to reload JupyterLab to see the changes.'),
            buttons: [
                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton(),
                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton({ label: trans.__('Reload') })
            ]
        });
        if (result.button.accept) {
            location.reload();
        }
    }
    async function loadSettingsMenu(registry, addMenu, menuFactory, translator) {
        var _a;
        const trans = translator.load('jupyterlab');
        let canonical = null;
        let loaded = {};
        /**
         * Populate the plugin's schema defaults.
         */
        function populate(schema) {
            var _a, _b;
            loaded = {};
            const pluginDefaults = Object.keys(registry.plugins)
                .map(plugin => {
                var _a, _b;
                const menus = (_b = (_a = registry.plugins[plugin].schema['jupyter.lab.menus']) === null || _a === void 0 ? void 0 : _a.main) !== null && _b !== void 0 ? _b : [];
                loaded[plugin] = menus;
                return menus;
            })
                .concat([(_b = (_a = schema['jupyter.lab.menus']) === null || _a === void 0 ? void 0 : _a.main) !== null && _b !== void 0 ? _b : []])
                .reduceRight((acc, val) => _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.SettingRegistry.reconcileMenus(acc, val, true), schema.properties.menus.default);
            // Apply default value as last step to take into account overrides.json
            // The standard default being [] as the plugin must use `jupyter.lab.menus.main`
            // to define their default value.
            schema.properties.menus.default = _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.SettingRegistry.reconcileMenus(pluginDefaults, schema.properties.menus.default, true)
                // flatten one level
                .sort((a, b) => { var _a, _b; return ((_a = a.rank) !== null && _a !== void 0 ? _a : Infinity) - ((_b = b.rank) !== null && _b !== void 0 ? _b : Infinity); });
        }
        // Transform the plugin object to return different schema than the default.
        registry.transform(PLUGIN_ID, {
            compose: plugin => {
                var _a, _b, _c, _d;
                // Only override the canonical schema the first time.
                if (!canonical) {
                    canonical = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_9__.JSONExt.deepCopy(plugin.schema);
                    populate(canonical);
                }
                const defaults = (_c = (_b = (_a = canonical.properties) === null || _a === void 0 ? void 0 : _a.menus) === null || _b === void 0 ? void 0 : _b.default) !== null && _c !== void 0 ? _c : [];
                const user = Object.assign(Object.assign({}, plugin.data.user), { menus: (_d = plugin.data.user.menus) !== null && _d !== void 0 ? _d : [] });
                const composite = Object.assign(Object.assign({}, plugin.data.composite), { menus: _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.SettingRegistry.reconcileMenus(defaults, user.menus) });
                plugin.data = { composite, user };
                return plugin;
            },
            fetch: plugin => {
                // Only override the canonical schema the first time.
                if (!canonical) {
                    canonical = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_9__.JSONExt.deepCopy(plugin.schema);
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
        const settings = await registry.load(PLUGIN_ID);
        const currentMenus = (_a = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_9__.JSONExt.deepCopy(settings.composite.menus)) !== null && _a !== void 0 ? _a : [];
        const menus = new Array();
        // Create menu for non-disabled element
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MenuFactory.createMenus(currentMenus
            .filter(menu => !menu.disabled)
            .map(menu => {
            var _a;
            return Object.assign(Object.assign({}, menu), { items: _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.SettingRegistry.filterDisabledItems((_a = menu.items) !== null && _a !== void 0 ? _a : []) });
        }), menuFactory).forEach(menu => {
            menus.push(menu);
            addMenu(menu);
        });
        settings.changed.connect(() => {
            var _a;
            // As extension may change menu through API, prompt the user to reload if the
            // menu has been updated.
            const newMenus = (_a = settings.composite.menus) !== null && _a !== void 0 ? _a : [];
            if (!_lumino_coreutils__WEBPACK_IMPORTED_MODULE_9__.JSONExt.deepEqual(currentMenus, newMenus)) {
                void displayInformation(trans);
            }
        });
        registry.pluginChanged.connect(async (sender, plugin) => {
            var _a, _b, _c;
            if (plugin !== PLUGIN_ID) {
                // If the plugin changed its menu.
                const oldMenus = (_a = loaded[plugin]) !== null && _a !== void 0 ? _a : [];
                const newMenus = (_c = (_b = registry.plugins[plugin].schema['jupyter.lab.menus']) === null || _b === void 0 ? void 0 : _b.main) !== null && _c !== void 0 ? _c : [];
                if (!_lumino_coreutils__WEBPACK_IMPORTED_MODULE_9__.JSONExt.deepEqual(oldMenus, newMenus)) {
                    if (loaded[plugin]) {
                        // The plugin has changed, request the user to reload the UI - this should not happen
                        await displayInformation(trans);
                    }
                    else {
                        // The plugin was not yet loaded when the menu was built => update the menu
                        loaded[plugin] = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_9__.JSONExt.deepCopy(newMenus);
                        // Merge potential disabled state
                        const toAdd = _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.SettingRegistry.reconcileMenus(newMenus, currentMenus, false, false)
                            .filter(menu => !menu.disabled)
                            .map(menu => {
                            var _a;
                            return Object.assign(Object.assign({}, menu), { items: _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.SettingRegistry.filterDisabledItems((_a = menu.items) !== null && _a !== void 0 ? _a : []) });
                        });
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MenuFactory.updateMenus(menus, toAdd, menuFactory).forEach(menu => {
                            addMenu(menu);
                        });
                    }
                }
            }
        });
    }
    Private.loadSettingsMenu = loadSettingsMenu;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfbWFpbm1lbnUtZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy5kYWNiODlhYzkwZjg4MzBjZDYzYS5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFROEI7QUFNSDtBQUM2QjtBQVk3QjtBQUMwQjtBQUN3QjtBQUNQO0FBTXRDO0FBQ1k7QUFDSDtBQUVHO0FBRS9DLE1BQU0sU0FBUyxHQUFHLHVDQUF1QyxDQUFDO0FBRTFEOztHQUVHO0FBQ0ksSUFBVSxVQUFVLENBMkUxQjtBQTNFRCxXQUFpQixVQUFVO0lBQ1osbUJBQVEsR0FBRyxlQUFlLENBQUM7SUFFM0IsZUFBSSxHQUFHLGVBQWUsQ0FBQztJQUV2QixlQUFJLEdBQUcsZUFBZSxDQUFDO0lBRXZCLHVCQUFZLEdBQUcsd0JBQXdCLENBQUM7SUFFeEMsbUJBQVEsR0FBRyxvQkFBb0IsQ0FBQztJQUVoQyxlQUFJLEdBQUcsZUFBZSxDQUFDO0lBRXZCLG1CQUFRLEdBQUcscUJBQXFCLENBQUM7SUFFakMsbUJBQVEsR0FBRyxlQUFlLENBQUM7SUFFM0IsMEJBQWUsR0FBRyw0QkFBNEIsQ0FBQztJQUUvQyx3QkFBYSxHQUFHLHlCQUF5QixDQUFDO0lBRTFDLG1CQUFRLEdBQUcsbUJBQW1CLENBQUM7SUFFL0IsaUJBQU0sR0FBRyxpQkFBaUIsQ0FBQztJQUUzQixxQkFBVSxHQUFHLGlCQUFpQixDQUFDO0lBRS9CLDBCQUFlLEdBQUcsc0JBQXNCLENBQUM7SUFFekMsNEJBQWlCLEdBQUcsZ0NBQWdDLENBQUM7SUFFckQsd0JBQWEsR0FBRyxvQkFBb0IsQ0FBQztJQUVyQyxnQ0FBcUIsR0FBRyw4QkFBOEIsQ0FBQztJQUV2RCx1QkFBWSxHQUFHLG1CQUFtQixDQUFDO0lBRW5DLHlCQUFjLEdBQUcscUJBQXFCLENBQUM7SUFFdkMsNkJBQWtCLEdBQUcsd0JBQXdCLENBQUM7SUFFOUMs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QUFDLElBQUksQ0FBQyxRQUFRLENBQUM7NkJBQzlCLEdBQUcsQ0FBQyxJQUFJLENBQUMsRUFBRTs7NEJBQ1YsdUNBQ0ssSUFBSSxLQUNQLEtBQUssRUFBRSw0RkFBbUMsQ0FBQyxVQUFJLENBQUMsS0FBSyxtQ0FBSSxFQUFFLENBQUMsSUFDNUQ7d0JBQ0osQ0FBQyxDQUFDLENBQUM7d0JBRUwseUVBQXVCLENBQUMsS0FBSyxFQUFFLEtBQUssRUFBRSxXQUFXLENBQUMsQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLEVBQUU7NEJBQ2hFLE9BQU8sQ0FBQyxJQUFJLENBQUMsQ0FBQzt3QkFDaEIsQ0FBQyxDQUFDLENBQUM7cUJBQ0o7aUJBQ0Y7YUFDRjtRQUNILENBQUMsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztJQXRKcUIsd0JBQWdCLG1CQXNKckM7QUFDSCxDQUFDLEVBektTLE9BQU8sS0FBUCxPQUFPLFFBeUtoQiIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9tYWlubWVudS1leHRlbnNpb24vc3JjL2luZGV4LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIG1haW5tZW51LWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7XG4gIGNyZWF0ZVNlbWFudGljQ29tbWFuZCxcbiAgSUxhYlNoZWxsLFxuICBJUm91dGVyLFxuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpblxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQge1xuICBEaWFsb2csXG4gIElDb21tYW5kUGFsZXR0ZSxcbiAgTWVudUZhY3RvcnksXG4gIHNob3dEaWFsb2dcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgUGFnZUNvbmZpZywgVVJMRXh0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29yZXV0aWxzJztcbmltcG9ydCB7XG4gIElFZGl0TWVudSxcbiAgSUZpbGVNZW51LFxuICBJSGVscE1lbnUsXG4gIElLZXJuZWxNZW51LFxuICBJTWFpbk1lbnUsXG4gIElSdW5NZW51LFxuICBJVGFic01lbnUsXG4gIElWaWV3TWVudSxcbiAgSnVweXRlckxhYk1lbnUsXG4gIE1haW5NZW51XG59IGZyb20gJ0BqdXB5dGVybGFiL21haW5tZW51JztcbmltcG9ydCB7IFNlcnZlckNvbm5lY3Rpb24gfSBmcm9tICdAanVweXRlcmxhYi9zZXJ2aWNlcyc7XG5pbXBvcnQgeyBJU2V0dGluZ1JlZ2lzdHJ5LCBTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHsgSVRyYW5zbGF0b3IsIFRyYW5zbGF0aW9uQnVuZGxlIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHtcbiAgZmFzdEZvcndhcmRJY29uLFxuICByZWZyZXNoSWNvbixcbiAgcnVuSWNvbixcbiAgc3RvcEljb25cbn0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBlYWNoLCBmaW5kIH0gZnJvbSAnQGx1bWluby9hbGdvcml0aG0nO1xuaW1wb3J0IHsgSlNPTkV4dCB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IElEaXNwb3NhYmxlIH0gZnJvbSAnQGx1bWluby9kaXNwb3NhYmxlJztcbmltcG9ydCB7IE1lbnUsIFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5cbmNvbnN0IFBMVUdJTl9JRCA9ICdAanVweXRlcmxhYi9tYWlubWVudS1leHRlbnNpb246cGx1Z2luJztcblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgY29tbWFuZCBJRHMgb2Ygc2VtYW50aWMgZXh0ZW5zaW9uIHBvaW50cy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBDb21tYW5kSURzIHtcbiAgZXhwb3J0IGNvbnN0IG9wZW5FZGl0ID0gJ2VkaXRtZW51Om9wZW4nO1xuXG4gIGV4cG9ydCBjb25zdCB1bmRvID0gJ2VkaXRtZW51OnVuZG8nO1xuXG4gIGV4cG9ydCBjb25zdCByZWRvID0gJ2VkaXRtZW51OnJlZG8nO1xuXG4gIGV4cG9ydCBjb25zdCBjbGVhckN1cnJlbnQgPSAnZWRpdG1lbnU6Y2xlYXItY3VycmVudCc7XG5cbiAgZXhwb3J0IGNvbnN0IGNsZWFyQWxsID0gJ2VkaXRtZW51OmNsZWFyLWFsbCc7XG5cbiAgZXhwb3J0IGNvbnN0IGZpbmQgPSAnZWRpdG1lbnU6ZmluZCc7XG5cbiAgZXhwb3J0IGNvbnN0IGdvVG9MaW5lID0gJ2VkaXRtZW51OmdvLXRvLWxpbmUnO1xuXG4gIGV4cG9ydCBjb25zdCBvcGVuRmlsZSA9ICdmaWxlbWVudTpvcGVuJztcblxuICBleHBvcnQgY29uc3QgY2xvc2VBbmRDbGVhbnVwID0gJ2ZpbGVtZW51OmNsb3NlLWFuZC1jbGVhbnVwJztcblxuICBleHBvcnQgY29uc3QgY3JlYXRlQ29uc29sZSA9ICdmaWxlbWVudTpjcmVhdGUtY29uc29sZSc7XG5cbiAgZXhwb3J0IGNvbnN0IHNodXRkb3duID0gJ2ZpbGVtZW51OnNodXRkb3duJztcblxuICBleHBvcnQgY29uc3QgbG9nb3V0ID0gJ2ZpbGVtZW51OmxvZ291dCc7XG5cbiAgZXhwb3J0IGNvbnN0IG9wZW5LZXJuZWwgPSAna2VybmVsbWVudTpvcGVuJztcblxuICBleHBvcnQgY29uc3QgaW50ZXJydXB0S2VybmVsID0gJ2tlcm5lbG1lbnU6aW50ZXJydXB0JztcblxuICBleHBvcnQgY29uc3QgcmVjb25uZWN0VG9LZXJuZWwgPSAna2VybmVsbWVudTpyZWNvbm5lY3QtdG8ta2VybmVsJztcblxuICBleHBvcnQgY29uc3QgcmVzdGFydEtlcm5lbCA9ICdrZXJuZWxtZW51OnJlc3RhcnQnO1xuXG4gIGV4cG9ydCBjb25zdCByZXN0YXJ0S2VybmVsQW5kQ2xlYXIgPSAna2VybmVsbWVudTpyZXN0YXJ0LWFuZC1jbGVhcic7XG5cbiAgZXhwb3J0IGNvbnN0IGNoYW5nZUtlcm5lbCA9ICdrZXJuZWxtZW51OmNoYW5nZSc7XG5cbiAgZXhwb3J0IGNvbnN0IHNodXRkb3duS2VybmVsID0gJ2tlcm5lbG1lbnU6c2h1dGRvd24nO1xuXG4gIGV4cG9ydCBjb25zdCBzaHV0ZG93bkFsbEtlcm5lbHMgPSAna2VybmVsbWVudTpzaHV0ZG93bkFsbCc7XG5cbiAgZXhwb3J0IGNvbnN0IG9wZW5WaWV3ID0gJ3ZpZXdtZW51Om9wZW4nO1xuXG4gIGV4cG9ydCBjb25zdCB3b3JkV3JhcCA9ICd2aWV3bWVudTp3b3JkLXdyYXAnO1xuXG4gIGV4cG9ydCBjb25zdCBsaW5lTnVtYmVyaW5nID0gJ3ZpZXdtZW51OmxpbmUtbnVtYmVyaW5nJztcblxuICBleHBvcnQgY29uc3QgbWF0Y2hCcmFja2V0cyA9ICd2aWV3bWVudTptYXRjaC1icmFja2V0cyc7XG5cbiAgZXhwb3J0IGNvbnN0IG9wZW5SdW4gPSAncnVubWVudTpvcGVuJztcblxuICBleHBvcnQgY29uc3QgcnVuID0gJ3J1bm1lbnU6cnVuJztcblxuICBleHBvcnQgY29uc3QgcnVuQWxsID0gJ3J1bm1lbnU6cnVuLWFsbCc7XG5cbiAgZXhwb3J0IGNvbnN0IHJlc3RhcnRBbmRSdW5BbGwgPSAncnVubWVudTpyZXN0YXJ0LWFuZC1ydW4tYWxsJztcblxuICBleHBvcnQgY29uc3QgcnVuQWJvdmUgPSAncnVubWVudTpydW4tYWJvdmUnO1xuXG4gIGV4cG9ydCBjb25zdCBydW5CZWxvdyA9ICdydW5tZW51OnJ1bi1iZWxvdyc7XG5cbiAgZXhwb3J0IGNvbnN0IG9wZW5UYWJzID0gJ3RhYnNtZW51Om9wZW4nO1xuXG4gIGV4cG9ydCBjb25zdCBhY3RpdmF0ZUJ5SWQgPSAndGFic21lbnU6YWN0aXZhdGUtYnktaWQnO1xuXG4gIGV4cG9ydCBjb25zdCBhY3RpdmF0ZVByZXZpb3VzbHlVc2VkVGFiID1cbiAgICAndGFic21lbnU6YWN0aXZhdGUtcHJldmlvdXNseS11c2VkLXRhYic7XG5cbiAgZXhwb3J0IGNvbnN0IG9wZW5TZXR0aW5ncyA9ICdzZXR0aW5nc21lbnU6b3Blbic7XG5cbiAgZXhwb3J0IGNvbnN0IG9wZW5IZWxwID0gJ2hlbHBtZW51Om9wZW4nO1xuXG4gIGV4cG9ydCBjb25zdCBnZXRLZXJuZWwgPSAnaGVscG1lbnU6Z2V0LWtlcm5lbCc7XG5cbiAgZXhwb3J0IGNvbnN0IG9wZW5GaXJzdCA9ICdtYWlubWVudTpvcGVuLWZpcnN0Jztcbn1cblxuLyoqXG4gKiBBIHNlcnZpY2UgcHJvdmlkaW5nIGFuIGludGVyZmFjZSB0byB0aGUgbWFpbiBtZW51LlxuICovXG5jb25zdCBwbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJTWFpbk1lbnU+ID0ge1xuICBpZDogUExVR0lOX0lELFxuICByZXF1aXJlczogW0lSb3V0ZXIsIElUcmFuc2xhdG9yXSxcbiAgb3B0aW9uYWw6IFtJQ29tbWFuZFBhbGV0dGUsIElMYWJTaGVsbCwgSVNldHRpbmdSZWdpc3RyeV0sXG4gIHByb3ZpZGVzOiBJTWFpbk1lbnUsXG4gIGFjdGl2YXRlOiBhc3luYyAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgcm91dGVyOiBJUm91dGVyLFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICAgIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSB8IG51bGwsXG4gICAgbGFiU2hlbGw6IElMYWJTaGVsbCB8IG51bGwsXG4gICAgcmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnkgfCBudWxsXG4gICk6IFByb21pc2U8SU1haW5NZW51PiA9PiB7XG4gICAgY29uc3QgeyBjb21tYW5kcyB9ID0gYXBwO1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG5cbiAgICBjb25zdCBtZW51ID0gbmV3IE1haW5NZW51KGNvbW1hbmRzKTtcbiAgICBtZW51LmlkID0gJ2pwLU1haW5NZW51JztcbiAgICBtZW51LmFkZENsYXNzKCdqcC1zY3JvbGxiYXItdGlueScpO1xuXG4gICAgLy8gQnVpbHQgbWVudSBmcm9tIHNldHRpbmdzXG4gICAgaWYgKHJlZ2lzdHJ5KSB7XG4gICAgICBhd2FpdCBQcml2YXRlLmxvYWRTZXR0aW5nc01lbnUoXG4gICAgICAgIHJlZ2lzdHJ5LFxuICAgICAgICAoYU1lbnU6IEp1cHl0ZXJMYWJNZW51KSA9PiB7XG4gICAgICAgICAgbWVudS5hZGRNZW51KGFNZW51LCB7IHJhbms6IGFNZW51LnJhbmsgfSk7XG4gICAgICAgIH0sXG4gICAgICAgIG9wdGlvbnMgPT4gTWFpbk1lbnUuZ2VuZXJhdGVNZW51KGNvbW1hbmRzLCBvcHRpb25zLCB0cmFucyksXG4gICAgICAgIHRyYW5zbGF0b3JcbiAgICAgICk7XG4gICAgfVxuXG4gICAgLy8gT25seSBhZGQgcXVpdCBidXR0b24gaWYgdGhlIGJhY2stZW5kIHN1cHBvcnRzIGl0IGJ5IGNoZWNraW5nIHBhZ2UgY29uZmlnLlxuICAgIGNvbnN0IHF1aXRCdXR0b24gPSBQYWdlQ29uZmlnLmdldE9wdGlvbigncXVpdEJ1dHRvbicpLnRvTG93ZXJDYXNlKCk7XG4gICAgbWVudS5maWxlTWVudS5xdWl0RW50cnkgPSBxdWl0QnV0dG9uID09PSAndHJ1ZSc7XG5cbiAgICAvLyBDcmVhdGUgdGhlIGFwcGxpY2F0aW9uIG1lbnVzLlxuICAgIGNyZWF0ZUVkaXRNZW51KGFwcCwgbWVudS5lZGl0TWVudSwgdHJhbnMpO1xuICAgIGNyZWF0ZUZpbGVNZW51KGFwcCwgbWVudS5maWxlTWVudSwgcm91dGVyLCB0cmFucyk7XG4gICAgY3JlYXRlS2VybmVsTWVudShhcHAsIG1lbnUua2VybmVsTWVudSwgdHJhbnMpO1xuICAgIGNyZWF0ZVJ1bk1lbnUoYXBwLCBtZW51LnJ1bk1lbnUsIHRyYW5zKTtcbiAgICBjcmVhdGVWaWV3TWVudShhcHAsIG1lbnUudmlld01lbnUsIHRyYW5zKTtcbiAgICBjcmVhdGVIZWxwTWVudShhcHAsIG1lbnUuaGVscE1lbnUsIHRyYW5zKTtcblxuICAgIC8vIFRoZSB0YWJzIG1lbnUgcmVsaWVzIG9uIGxhYiBzaGVsbCBmdW5jdGlvbmFsaXR5LlxuICAgIGlmIChsYWJTaGVsbCkge1xuICAgICAgY3JlYXRlVGFic01lbnUoYXBwLCBtZW51LnRhYnNNZW51LCBsYWJTaGVsbCwgdHJhbnMpO1xuICAgIH1cblxuICAgIC8vIENyZWF0ZSBjb21tYW5kcyB0byBvcGVuIHRoZSBtYWluIGFwcGxpY2F0aW9uIG1lbnVzLlxuICAgIGNvbnN0IGFjdGl2YXRlTWVudSA9IChpdGVtOiBNZW51KSA9PiB7XG4gICAgICBtZW51LmFjdGl2ZU1lbnUgPSBpdGVtO1xuICAgICAgbWVudS5vcGVuQWN0aXZlTWVudSgpO1xuICAgIH07XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMub3BlbkVkaXQsIHtcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnT3BlbiBFZGl0IE1lbnUnKSxcbiAgICAgIGV4ZWN1dGU6ICgpID0+IGFjdGl2YXRlTWVudShtZW51LmVkaXRNZW51KVxuICAgIH0pO1xuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5vcGVuRmlsZSwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdPcGVuIEZpbGUgTWVudScpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4gYWN0aXZhdGVNZW51KG1lbnUuZmlsZU1lbnUpXG4gICAgfSk7XG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLm9wZW5LZXJuZWwsIHtcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnT3BlbiBLZXJuZWwgTWVudScpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4gYWN0aXZhdGVNZW51KG1lbnUua2VybmVsTWVudSlcbiAgICB9KTtcbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMub3BlblJ1biwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdPcGVuIFJ1biBNZW51JyksXG4gICAgICBleGVjdXRlOiAoKSA9PiBhY3RpdmF0ZU1lbnUobWVudS5ydW5NZW51KVxuICAgIH0pO1xuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5vcGVuVmlldywge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdPcGVuIFZpZXcgTWVudScpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4gYWN0aXZhdGVNZW51KG1lbnUudmlld01lbnUpXG4gICAgfSk7XG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLm9wZW5TZXR0aW5ncywge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdPcGVuIFNldHRpbmdzIE1lbnUnKSxcbiAgICAgIGV4ZWN1dGU6ICgpID0+IGFjdGl2YXRlTWVudShtZW51LnNldHRpbmdzTWVudSlcbiAgICB9KTtcbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMub3BlblRhYnMsIHtcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnT3BlbiBUYWJzIE1lbnUnKSxcbiAgICAgIGV4ZWN1dGU6ICgpID0+IGFjdGl2YXRlTWVudShtZW51LnRhYnNNZW51KVxuICAgIH0pO1xuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5vcGVuSGVscCwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdPcGVuIEhlbHAgTWVudScpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4gYWN0aXZhdGVNZW51KG1lbnUuaGVscE1lbnUpXG4gICAgfSk7XG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLm9wZW5GaXJzdCwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdPcGVuIEZpcnN0IE1lbnUnKSxcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgbWVudS5hY3RpdmVJbmRleCA9IDA7XG4gICAgICAgIG1lbnUub3BlbkFjdGl2ZU1lbnUoKTtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIGlmIChwYWxldHRlKSB7XG4gICAgICAvLyBBZGQgc29tZSBvZiB0aGUgY29tbWFuZHMgZGVmaW5lZCBoZXJlIHRvIHRoZSBjb21tYW5kIHBhbGV0dGUuXG4gICAgICBwYWxldHRlLmFkZEl0ZW0oe1xuICAgICAgICBjb21tYW5kOiBDb21tYW5kSURzLnNodXRkb3duLFxuICAgICAgICBjYXRlZ29yeTogdHJhbnMuX18oJ01haW4gQXJlYScpXG4gICAgICB9KTtcbiAgICAgIHBhbGV0dGUuYWRkSXRlbSh7XG4gICAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMubG9nb3V0LFxuICAgICAgICBjYXRlZ29yeTogdHJhbnMuX18oJ01haW4gQXJlYScpXG4gICAgICB9KTtcblxuICAgICAgcGFsZXR0ZS5hZGRJdGVtKHtcbiAgICAgICAgY29tbWFuZDogQ29tbWFuZElEcy5zaHV0ZG93bkFsbEtlcm5lbHMsXG4gICAgICAgIGNhdGVnb3J5OiB0cmFucy5fXygnS2VybmVsIE9wZXJhdGlvbnMnKVxuICAgICAgfSk7XG5cbiAgICAgIHBhbGV0dGUuYWRkSXRlbSh7XG4gICAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMuYWN0aXZhdGVQcmV2aW91c2x5VXNlZFRhYixcbiAgICAgICAgY2F0ZWdvcnk6IHRyYW5zLl9fKCdNYWluIEFyZWEnKVxuICAgICAgfSk7XG4gICAgfVxuXG4gICAgYXBwLnNoZWxsLmFkZChtZW51LCAnbWVudScsIHsgcmFuazogMTAwIH0pO1xuXG4gICAgcmV0dXJuIG1lbnU7XG4gIH1cbn07XG5cbi8qKlxuICogQ3JlYXRlIHRoZSBiYXNpYyBgRWRpdGAgbWVudS5cbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIGNyZWF0ZUVkaXRNZW51KFxuICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgbWVudTogSUVkaXRNZW51LFxuICB0cmFuczogVHJhbnNsYXRpb25CdW5kbGVcbik6IHZvaWQge1xuICBjb25zdCBjb21tYW5kcyA9IGFwcC5jb21tYW5kcztcblxuICAvLyBBZGQgdGhlIHVuZG8vcmVkbyBjb21tYW5kcyB0aGUgdGhlIEVkaXQgbWVudS5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChcbiAgICBDb21tYW5kSURzLnVuZG8sXG4gICAgY3JlYXRlU2VtYW50aWNDb21tYW5kKFxuICAgICAgYXBwLFxuICAgICAgbWVudS51bmRvZXJzLnVuZG8sXG4gICAgICB7XG4gICAgICAgIGxhYmVsOiB0cmFucy5fXygnVW5kbycpXG4gICAgICB9LFxuICAgICAgdHJhbnNcbiAgICApXG4gICk7XG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoXG4gICAgQ29tbWFuZElEcy5yZWRvLFxuICAgIGNyZWF0ZVNlbWFudGljQ29tbWFuZChcbiAgICAgIGFwcCxcbiAgICAgIG1lbnUudW5kb2Vycy5yZWRvLFxuICAgICAge1xuICAgICAgICBsYWJlbDogdHJhbnMuX18oJ1JlZG8nKVxuICAgICAgfSxcbiAgICAgIHRyYW5zXG4gICAgKVxuICApO1xuXG4gIC8vIEFkZCB0aGUgY2xlYXIgY29tbWFuZHMgdG8gdGhlIEVkaXQgbWVudS5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChcbiAgICBDb21tYW5kSURzLmNsZWFyQ3VycmVudCxcbiAgICBjcmVhdGVTZW1hbnRpY0NvbW1hbmQoXG4gICAgICBhcHAsXG4gICAgICBtZW51LmNsZWFyZXJzLmNsZWFyQ3VycmVudCxcbiAgICAgIHtcbiAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdDbGVhcicpXG4gICAgICB9LFxuICAgICAgdHJhbnNcbiAgICApXG4gICk7XG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoXG4gICAgQ29tbWFuZElEcy5jbGVhckFsbCxcbiAgICBjcmVhdGVTZW1hbnRpY0NvbW1hbmQoXG4gICAgICBhcHAsXG4gICAgICBtZW51LmNsZWFyZXJzLmNsZWFyQWxsLFxuICAgICAge1xuICAgICAgICBsYWJlbDogdHJhbnMuX18oJ0NsZWFyIEFsbCcpXG4gICAgICB9LFxuICAgICAgdHJhbnNcbiAgICApXG4gICk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChcbiAgICBDb21tYW5kSURzLmdvVG9MaW5lLFxuICAgIGNyZWF0ZVNlbWFudGljQ29tbWFuZChcbiAgICAgIGFwcCxcbiAgICAgIG1lbnUuZ29Ub0xpbmVycyxcbiAgICAgIHtcbiAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdHbyB0byBMaW5l4oCmJylcbiAgICAgIH0sXG4gICAgICB0cmFuc1xuICAgIClcbiAgKTtcbn1cblxuLyoqXG4gKiBDcmVhdGUgdGhlIGJhc2ljIGBGaWxlYCBtZW51LlxuICovXG5leHBvcnQgZnVuY3Rpb24gY3JlYXRlRmlsZU1lbnUoXG4gIGFwcDogSnVweXRlckZyb250RW5kLFxuICBtZW51OiBJRmlsZU1lbnUsXG4gIHJvdXRlcjogSVJvdXRlcixcbiAgdHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlXG4pOiB2b2lkIHtcbiAgY29uc3QgY29tbWFuZHMgPSBhcHAuY29tbWFuZHM7XG5cbiAgLy8gQWRkIGEgZGVsZWdhdG9yIGNvbW1hbmQgZm9yIGNsb3NpbmcgYW5kIGNsZWFuaW5nIHVwIGFuIGFjdGl2aXR5LlxuICAvLyBUaGlzIG9uZSBpcyBhIGJpdCBkaWZmZXJlbnQsIGluIHRoYXQgd2UgY29uc2lkZXIgaXQgZW5hYmxlZFxuICAvLyBldmVuIGlmIGl0IGNhbm5vdCBmaW5kIGEgZGVsZWdhdGUgZm9yIHRoZSBhY3Rpdml0eS5cbiAgLy8gSW4gdGhhdCBjYXNlLCB3ZSBpbnN0ZWFkIGNhbGwgdGhlIGFwcGxpY2F0aW9uIGBjbG9zZWAgY29tbWFuZC5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmNsb3NlQW5kQ2xlYW51cCwge1xuICAgIC4uLmNyZWF0ZVNlbWFudGljQ29tbWFuZChcbiAgICAgIGFwcCxcbiAgICAgIG1lbnUuY2xvc2VBbmRDbGVhbmVycyxcbiAgICAgIHtcbiAgICAgICAgZXhlY3V0ZTogJ2FwcGxpY2F0aW9uOmNsb3NlJyxcbiAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdDbG9zZSBhbmQgU2h1dCBEb3duJyksXG4gICAgICAgIGlzRW5hYmxlZDogdHJ1ZVxuICAgICAgfSxcbiAgICAgIHRyYW5zXG4gICAgKSxcbiAgICBpc0VuYWJsZWQ6ICgpID0+XG4gICAgICAhIWFwcC5zaGVsbC5jdXJyZW50V2lkZ2V0ICYmICEhYXBwLnNoZWxsLmN1cnJlbnRXaWRnZXQudGl0bGUuY2xvc2FibGVcbiAgfSk7XG5cbiAgLy8gQWRkIGEgZGVsZWdhdG9yIGNvbW1hbmQgZm9yIGNyZWF0aW5nIGEgY29uc29sZSBmb3IgYW4gYWN0aXZpdHkuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoXG4gICAgQ29tbWFuZElEcy5jcmVhdGVDb25zb2xlLFxuICAgIGNyZWF0ZVNlbWFudGljQ29tbWFuZChcbiAgICAgIGFwcCxcbiAgICAgIG1lbnUuY29uc29sZUNyZWF0b3JzLFxuICAgICAge1xuICAgICAgICBsYWJlbDogdHJhbnMuX18oJ05ldyBDb25zb2xlIGZvciBBY3Rpdml0eScpXG4gICAgICB9LFxuICAgICAgdHJhbnNcbiAgICApXG4gICk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnNodXRkb3duLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdTaHV0IERvd24nKSxcbiAgICBjYXB0aW9uOiB0cmFucy5fXygnU2h1dCBkb3duIEp1cHl0ZXJMYWInKSxcbiAgICBpc1Zpc2libGU6ICgpID0+IG1lbnUucXVpdEVudHJ5LFxuICAgIGlzRW5hYmxlZDogKCkgPT4gbWVudS5xdWl0RW50cnksXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgcmV0dXJuIHNob3dEaWFsb2coe1xuICAgICAgICB0aXRsZTogdHJhbnMuX18oJ1NodXRkb3duIGNvbmZpcm1hdGlvbicpLFxuICAgICAgICBib2R5OiB0cmFucy5fXygnUGxlYXNlIGNvbmZpcm0geW91IHdhbnQgdG8gc2h1dCBkb3duIEp1cHl0ZXJMYWIuJyksXG4gICAgICAgIGJ1dHRvbnM6IFtcbiAgICAgICAgICBEaWFsb2cuY2FuY2VsQnV0dG9uKCksXG4gICAgICAgICAgRGlhbG9nLndhcm5CdXR0b24oeyBsYWJlbDogdHJhbnMuX18oJ1NodXQgRG93bicpIH0pXG4gICAgICAgIF1cbiAgICAgIH0pLnRoZW4oYXN5bmMgcmVzdWx0ID0+IHtcbiAgICAgICAgaWYgKHJlc3VsdC5idXR0b24uYWNjZXB0KSB7XG4gICAgICAgICAgY29uc3Qgc2V0dGluZyA9IFNlcnZlckNvbm5lY3Rpb24ubWFrZVNldHRpbmdzKCk7XG4gICAgICAgICAgY29uc3QgYXBpVVJMID0gVVJMRXh0LmpvaW4oc2V0dGluZy5iYXNlVXJsLCAnYXBpL3NodXRkb3duJyk7XG5cbiAgICAgICAgICAvLyBTaHV0ZG93biBhbGwga2VybmVsIGFuZCB0ZXJtaW5hbCBzZXNzaW9ucyBiZWZvcmUgc2h1dHRpbmcgZG93biB0aGUgc2VydmVyXG4gICAgICAgICAgLy8gSWYgdGhpcyBmYWlscywgd2UgY29udGludWUgZXhlY3V0aW9uIHNvIHdlIGNhbiBwb3N0IGFuIGFwaS9zaHV0ZG93biByZXF1ZXN0XG4gICAgICAgICAgdHJ5IHtcbiAgICAgICAgICAgIGF3YWl0IFByb21pc2UuYWxsKFtcbiAgICAgICAgICAgICAgYXBwLnNlcnZpY2VNYW5hZ2VyLnNlc3Npb25zLnNodXRkb3duQWxsKCksXG4gICAgICAgICAgICAgIGFwcC5zZXJ2aWNlTWFuYWdlci50ZXJtaW5hbHMuc2h1dGRvd25BbGwoKVxuICAgICAgICAgICAgXSk7XG4gICAgICAgICAgfSBjYXRjaCAoZSkge1xuICAgICAgICAgICAgLy8gRG8gbm90aGluZ1xuICAgICAgICAgICAgY29uc29sZS5sb2coYEZhaWxlZCB0byBzaHV0ZG93biBzZXNzaW9ucyBhbmQgdGVybWluYWxzOiAke2V9YCk7XG4gICAgICAgICAgfVxuXG4gICAgICAgICAgcmV0dXJuIFNlcnZlckNvbm5lY3Rpb24ubWFrZVJlcXVlc3QoXG4gICAgICAgICAgICBhcGlVUkwsXG4gICAgICAgICAgICB7IG1ldGhvZDogJ1BPU1QnIH0sXG4gICAgICAgICAgICBzZXR0aW5nXG4gICAgICAgICAgKVxuICAgICAgICAgICAgLnRoZW4ocmVzdWx0ID0+IHtcbiAgICAgICAgICAgICAgaWYgKHJlc3VsdC5vaykge1xuICAgICAgICAgICAgICAgIC8vIENsb3NlIHRoaXMgd2luZG93IGlmIHRoZSBzaHV0ZG93biByZXF1ZXN0IGhhcyBiZWVuIHN1Y2Nlc3NmdWxcbiAgICAgICAgICAgICAgICBjb25zdCBib2R5ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2Jyk7XG4gICAgICAgICAgICAgICAgY29uc3QgcDEgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdwJyk7XG4gICAgICAgICAgICAgICAgcDEudGV4dENvbnRlbnQgPSB0cmFucy5fXyhcbiAgICAgICAgICAgICAgICAgICdZb3UgaGF2ZSBzaHV0IGRvd24gdGhlIEp1cHl0ZXIgc2VydmVyLiBZb3UgY2FuIG5vdyBjbG9zZSB0aGlzIHRhYi4nXG4gICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgICBjb25zdCBwMiA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3AnKTtcbiAgICAgICAgICAgICAgICBwMi50ZXh0Q29udGVudCA9IHRyYW5zLl9fKFxuICAgICAgICAgICAgICAgICAgJ1RvIHVzZSBKdXB5dGVyTGFiIGFnYWluLCB5b3Ugd2lsbCBuZWVkIHRvIHJlbGF1bmNoIGl0LidcbiAgICAgICAgICAgICAgICApO1xuXG4gICAgICAgICAgICAgICAgYm9keS5hcHBlbmRDaGlsZChwMSk7XG4gICAgICAgICAgICAgICAgYm9keS5hcHBlbmRDaGlsZChwMik7XG4gICAgICAgICAgICAgICAgdm9pZCBzaG93RGlhbG9nKHtcbiAgICAgICAgICAgICAgICAgIHRpdGxlOiB0cmFucy5fXygnU2VydmVyIHN0b3BwZWQnKSxcbiAgICAgICAgICAgICAgICAgIGJvZHk6IG5ldyBXaWRnZXQoeyBub2RlOiBib2R5IH0pLFxuICAgICAgICAgICAgICAgICAgYnV0dG9uczogW11cbiAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICB3aW5kb3cuY2xvc2UoKTtcbiAgICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICB0aHJvdyBuZXcgU2VydmVyQ29ubmVjdGlvbi5SZXNwb25zZUVycm9yKHJlc3VsdCk7XG4gICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH0pXG4gICAgICAgICAgICAuY2F0Y2goZGF0YSA9PiB7XG4gICAgICAgICAgICAgIHRocm93IG5ldyBTZXJ2ZXJDb25uZWN0aW9uLk5ldHdvcmtFcnJvcihkYXRhKTtcbiAgICAgICAgICAgIH0pO1xuICAgICAgICB9XG4gICAgICB9KTtcbiAgICB9XG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5sb2dvdXQsIHtcbiAgICBsYWJlbDogdHJhbnMuX18oJ0xvZyBPdXQnKSxcbiAgICBjYXB0aW9uOiB0cmFucy5fXygnTG9nIG91dCBvZiBKdXB5dGVyTGFiJyksXG4gICAgaXNWaXNpYmxlOiAoKSA9PiBtZW51LnF1aXRFbnRyeSxcbiAgICBpc0VuYWJsZWQ6ICgpID0+IG1lbnUucXVpdEVudHJ5LFxuICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgIHJvdXRlci5uYXZpZ2F0ZSgnL2xvZ291dCcsIHsgaGFyZDogdHJ1ZSB9KTtcbiAgICB9XG4gIH0pO1xufVxuXG4vKipcbiAqIENyZWF0ZSB0aGUgYmFzaWMgYEtlcm5lbGAgbWVudS5cbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIGNyZWF0ZUtlcm5lbE1lbnUoXG4gIGFwcDogSnVweXRlckZyb250RW5kLFxuICBtZW51OiBJS2VybmVsTWVudSxcbiAgdHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlXG4pOiB2b2lkIHtcbiAgY29uc3QgY29tbWFuZHMgPSBhcHAuY29tbWFuZHM7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmludGVycnVwdEtlcm5lbCwge1xuICAgIC4uLmNyZWF0ZVNlbWFudGljQ29tbWFuZChcbiAgICAgIGFwcCxcbiAgICAgIG1lbnUua2VybmVsVXNlcnMuaW50ZXJydXB0S2VybmVsLFxuICAgICAge1xuICAgICAgICBsYWJlbDogdHJhbnMuX18oJ0ludGVycnVwdCBLZXJuZWwnKSxcbiAgICAgICAgY2FwdGlvbjogdHJhbnMuX18oJ0ludGVycnVwdCB0aGUga2VybmVsJylcbiAgICAgIH0sXG4gICAgICB0cmFuc1xuICAgICksXG4gICAgaWNvbjogYXJncyA9PiAoYXJncy50b29sYmFyID8gc3RvcEljb24gOiB1bmRlZmluZWQpXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoXG4gICAgQ29tbWFuZElEcy5yZWNvbm5lY3RUb0tlcm5lbCxcbiAgICBjcmVhdGVTZW1hbnRpY0NvbW1hbmQoXG4gICAgICBhcHAsXG4gICAgICBtZW51Lmtlcm5lbFVzZXJzLnJlY29ubmVjdFRvS2VybmVsLFxuICAgICAge1xuICAgICAgICBsYWJlbDogdHJhbnMuX18oJ1JlY29ubmVjdCB0byBLZXJuZWwnKVxuICAgICAgfSxcbiAgICAgIHRyYW5zXG4gICAgKVxuICApO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5yZXN0YXJ0S2VybmVsLCB7XG4gICAgLi4uY3JlYXRlU2VtYW50aWNDb21tYW5kKFxuICAgICAgYXBwLFxuICAgICAgbWVudS5rZXJuZWxVc2Vycy5yZXN0YXJ0S2VybmVsLFxuICAgICAge1xuICAgICAgICBsYWJlbDogdHJhbnMuX18oJ1Jlc3RhcnQgS2VybmVs4oCmJyksXG4gICAgICAgIGNhcHRpb246IHRyYW5zLl9fKCdSZXN0YXJ0IHRoZSBrZXJuZWwnKVxuICAgICAgfSxcbiAgICAgIHRyYW5zXG4gICAgKSxcbiAgICBpY29uOiBhcmdzID0+IChhcmdzLnRvb2xiYXIgPyByZWZyZXNoSWNvbiA6IHVuZGVmaW5lZClcbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChcbiAgICBDb21tYW5kSURzLnJlc3RhcnRLZXJuZWxBbmRDbGVhcixcbiAgICBjcmVhdGVTZW1hbnRpY0NvbW1hbmQoXG4gICAgICBhcHAsXG4gICAgICBbbWVudS5rZXJuZWxVc2Vycy5yZXN0YXJ0S2VybmVsLCBtZW51Lmtlcm5lbFVzZXJzLmNsZWFyV2lkZ2V0XSxcbiAgICAgIHtcbiAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdSZXN0YXJ0IEtlcm5lbCBhbmQgQ2xlYXLigKYnKVxuICAgICAgfSxcbiAgICAgIHRyYW5zXG4gICAgKVxuICApO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoXG4gICAgQ29tbWFuZElEcy5jaGFuZ2VLZXJuZWwsXG4gICAgY3JlYXRlU2VtYW50aWNDb21tYW5kKFxuICAgICAgYXBwLFxuICAgICAgbWVudS5rZXJuZWxVc2Vycy5jaGFuZ2VLZXJuZWwsXG4gICAgICB7XG4gICAgICAgIGxhYmVsOiB0cmFucy5fXygnQ2hhbmdlIEtlcm5lbOKApicpXG4gICAgICB9LFxuICAgICAgdHJhbnNcbiAgICApXG4gICk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChcbiAgICBDb21tYW5kSURzLnNodXRkb3duS2VybmVsLFxuICAgIGNyZWF0ZVNlbWFudGljQ29tbWFuZChcbiAgICAgIGFwcCxcbiAgICAgIG1lbnUua2VybmVsVXNlcnMuc2h1dGRvd25LZXJuZWwsXG4gICAgICB7XG4gICAgICAgIGxhYmVsOiB0cmFucy5fXygnU2h1dCBEb3duIEtlcm5lbCcpLFxuICAgICAgICBjYXB0aW9uOiB0cmFucy5fXygnU2h1dCBkb3duIGtlcm5lbCcpXG4gICAgICB9LFxuICAgICAgdHJhbnNcbiAgICApXG4gICk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnNodXRkb3duQWxsS2VybmVscywge1xuICAgIGxhYmVsOiB0cmFucy5fXygnU2h1dCBEb3duIEFsbCBLZXJuZWxz4oCmJyksXG4gICAgaXNFbmFibGVkOiAoKSA9PiB7XG4gICAgICByZXR1cm4gYXBwLnNlcnZpY2VNYW5hZ2VyLnNlc3Npb25zLnJ1bm5pbmcoKS5uZXh0KCkgIT09IHVuZGVmaW5lZDtcbiAgICB9LFxuICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgIHJldHVybiBzaG93RGlhbG9nKHtcbiAgICAgICAgdGl0bGU6IHRyYW5zLl9fKCdTaHV0IERvd24gQWxsPycpLFxuICAgICAgICBib2R5OiB0cmFucy5fXygnU2h1dCBkb3duIGFsbCBrZXJuZWxzPycpLFxuICAgICAgICBidXR0b25zOiBbXG4gICAgICAgICAgRGlhbG9nLmNhbmNlbEJ1dHRvbih7IGxhYmVsOiB0cmFucy5fXygnRGlzbWlzcycpIH0pLFxuICAgICAgICAgIERpYWxvZy53YXJuQnV0dG9uKHsgbGFiZWw6IHRyYW5zLl9fKCdTaHV0IERvd24gQWxsJykgfSlcbiAgICAgICAgXVxuICAgICAgfSkudGhlbihyZXN1bHQgPT4ge1xuICAgICAgICBpZiAocmVzdWx0LmJ1dHRvbi5hY2NlcHQpIHtcbiAgICAgICAgICByZXR1cm4gYXBwLnNlcnZpY2VNYW5hZ2VyLnNlc3Npb25zLnNodXRkb3duQWxsKCk7XG4gICAgICAgIH1cbiAgICAgIH0pO1xuICAgIH1cbiAgfSk7XG59XG5cbi8qKlxuICogQ3JlYXRlIHRoZSBiYXNpYyBgVmlld2AgbWVudS5cbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIGNyZWF0ZVZpZXdNZW51KFxuICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgbWVudTogSVZpZXdNZW51LFxuICB0cmFuczogVHJhbnNsYXRpb25CdW5kbGVcbik6IHZvaWQge1xuICBjb25zdCBjb21tYW5kcyA9IGFwcC5jb21tYW5kcztcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKFxuICAgIENvbW1hbmRJRHMubGluZU51bWJlcmluZyxcbiAgICBjcmVhdGVTZW1hbnRpY0NvbW1hbmQoXG4gICAgICBhcHAsXG4gICAgICBtZW51LmVkaXRvclZpZXdlcnMudG9nZ2xlTGluZU51bWJlcnMsXG4gICAgICB7XG4gICAgICAgIGxhYmVsOiB0cmFucy5fXygnU2hvdyBMaW5lIE51bWJlcnMnKVxuICAgICAgfSxcbiAgICAgIHRyYW5zXG4gICAgKVxuICApO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoXG4gICAgQ29tbWFuZElEcy5tYXRjaEJyYWNrZXRzLFxuICAgIGNyZWF0ZVNlbWFudGljQ29tbWFuZChcbiAgICAgIGFwcCxcbiAgICAgIG1lbnUuZWRpdG9yVmlld2Vycy50b2dnbGVNYXRjaEJyYWNrZXRzLFxuICAgICAge1xuICAgICAgICBsYWJlbDogdHJhbnMuX18oJ01hdGNoIEJyYWNrZXRzJylcbiAgICAgIH0sXG4gICAgICB0cmFuc1xuICAgIClcbiAgKTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKFxuICAgIENvbW1hbmRJRHMud29yZFdyYXAsXG4gICAgY3JlYXRlU2VtYW50aWNDb21tYW5kKFxuICAgICAgYXBwLFxuICAgICAgbWVudS5lZGl0b3JWaWV3ZXJzLnRvZ2dsZVdvcmRXcmFwLFxuICAgICAge1xuICAgICAgICBsYWJlbDogdHJhbnMuX18oJ1dyYXAgV29yZHMnKVxuICAgICAgfSxcbiAgICAgIHRyYW5zXG4gICAgKVxuICApO1xufVxuXG4vKipcbiAqIENyZWF0ZSB0aGUgYmFzaWMgYFJ1bmAgbWVudS5cbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIGNyZWF0ZVJ1bk1lbnUoXG4gIGFwcDogSnVweXRlckZyb250RW5kLFxuICBtZW51OiBJUnVuTWVudSxcbiAgdHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlXG4pOiB2b2lkIHtcbiAgY29uc3QgY29tbWFuZHMgPSBhcHAuY29tbWFuZHM7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnJ1biwge1xuICAgIC4uLmNyZWF0ZVNlbWFudGljQ29tbWFuZChcbiAgICAgIGFwcCxcbiAgICAgIG1lbnUuY29kZVJ1bm5lcnMucnVuLFxuICAgICAge1xuICAgICAgICBsYWJlbDogdHJhbnMuX18oJ1J1biBTZWxlY3RlZCcpLFxuICAgICAgICBjYXB0aW9uOiB0cmFucy5fXygnUnVuIFNlbGVjdGVkJylcbiAgICAgIH0sXG4gICAgICB0cmFuc1xuICAgICksXG4gICAgaWNvbjogYXJncyA9PiAoYXJncy50b29sYmFyID8gcnVuSWNvbiA6IHVuZGVmaW5lZClcbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChcbiAgICBDb21tYW5kSURzLnJ1bkFsbCxcbiAgICBjcmVhdGVTZW1hbnRpY0NvbW1hbmQoXG4gICAgICBhcHAsXG4gICAgICBtZW51LmNvZGVSdW5uZXJzLnJ1bkFsbCxcbiAgICAgIHtcbiAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdSdW4gQWxsJyksXG4gICAgICAgIGNhcHRpb246IHRyYW5zLl9fKCdSdW4gQWxsJylcbiAgICAgIH0sXG4gICAgICB0cmFuc1xuICAgIClcbiAgKTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMucmVzdGFydEFuZFJ1bkFsbCwge1xuICAgIC4uLmNyZWF0ZVNlbWFudGljQ29tbWFuZChcbiAgICAgIGFwcCxcbiAgICAgIFttZW51LmNvZGVSdW5uZXJzLnJlc3RhcnQsIG1lbnUuY29kZVJ1bm5lcnMucnVuQWxsXSxcbiAgICAgIHtcbiAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdSZXN0YXJ0IEtlcm5lbCBhbmQgUnVuIEFsbCcpLFxuICAgICAgICBjYXB0aW9uOiB0cmFucy5fXygnUmVzdGFydCBLZXJuZWwgYW5kIFJ1biBBbGwnKVxuICAgICAgfSxcbiAgICAgIHRyYW5zXG4gICAgKSxcbiAgICBpY29uOiBhcmdzID0+IChhcmdzLnRvb2xiYXIgPyBmYXN0Rm9yd2FyZEljb24gOiB1bmRlZmluZWQpXG4gIH0pO1xufVxuXG4vKipcbiAqIENyZWF0ZSB0aGUgYmFzaWMgYFRhYnNgIG1lbnUuXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiBjcmVhdGVUYWJzTWVudShcbiAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gIG1lbnU6IElUYWJzTWVudSxcbiAgbGFiU2hlbGw6IElMYWJTaGVsbCB8IG51bGwsXG4gIHRyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZVxuKTogdm9pZCB7XG4gIGNvbnN0IGNvbW1hbmRzID0gYXBwLmNvbW1hbmRzO1xuXG4gIC8vIEEgbGlzdCBvZiB0aGUgYWN0aXZlIHRhYnMgaW4gdGhlIG1haW4gYXJlYS5cbiAgY29uc3QgdGFiR3JvdXA6IE1lbnUuSUl0ZW1PcHRpb25zW10gPSBbXTtcbiAgLy8gQSBkaXNwb3NhYmxlIGZvciBnZXR0aW5nIHJpZCBvZiB0aGUgb3V0LW9mLWRhdGUgdGFicyBsaXN0LlxuICBsZXQgZGlzcG9zYWJsZTogSURpc3Bvc2FibGU7XG5cbiAgLy8gQ29tbWFuZCB0byBhY3RpdmF0ZSBhIHdpZGdldCBieSBpZC5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmFjdGl2YXRlQnlJZCwge1xuICAgIGxhYmVsOiBhcmdzID0+IHtcbiAgICAgIGlmIChhcmdzLmlkID09PSB1bmRlZmluZWQpIHtcbiAgICAgICAgcmV0dXJuIHRyYW5zLl9fKCdBY3RpdmF0ZSBhIHdpZGdldCBieSBpdHMgYGlkYC4nKTtcbiAgICAgIH1cbiAgICAgIGNvbnN0IGlkID0gYXJnc1snaWQnXSB8fCAnJztcbiAgICAgIGNvbnN0IHdpZGdldCA9IGZpbmQoYXBwLnNoZWxsLndpZGdldHMoJ21haW4nKSwgdyA9PiB3LmlkID09PSBpZCk7XG4gICAgICByZXR1cm4gKHdpZGdldCAmJiB3aWRnZXQudGl0bGUubGFiZWwpIHx8ICcnO1xuICAgIH0sXG4gICAgaXNUb2dnbGVkOiBhcmdzID0+IHtcbiAgICAgIGNvbnN0IGlkID0gYXJnc1snaWQnXSB8fCAnJztcbiAgICAgIHJldHVybiAhIWFwcC5zaGVsbC5jdXJyZW50V2lkZ2V0ICYmIGFwcC5zaGVsbC5jdXJyZW50V2lkZ2V0LmlkID09PSBpZDtcbiAgICB9LFxuICAgIGV4ZWN1dGU6IGFyZ3MgPT4gYXBwLnNoZWxsLmFjdGl2YXRlQnlJZCgoYXJnc1snaWQnXSBhcyBzdHJpbmcpIHx8ICcnKVxuICB9KTtcblxuICBsZXQgcHJldmlvdXNJZCA9ICcnO1xuICAvLyBDb21tYW5kIHRvIHRvZ2dsZSBiZXR3ZWVuIHRoZSBjdXJyZW50XG4gIC8vIHRhYiBhbmQgdGhlIGxhc3QgbW9kaWZpZWQgdGFiLlxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuYWN0aXZhdGVQcmV2aW91c2x5VXNlZFRhYiwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnQWN0aXZhdGUgUHJldmlvdXNseSBVc2VkIFRhYicpLFxuICAgIGlzRW5hYmxlZDogKCkgPT4gISFwcmV2aW91c0lkLFxuICAgIGV4ZWN1dGU6ICgpID0+IGNvbW1hbmRzLmV4ZWN1dGUoQ29tbWFuZElEcy5hY3RpdmF0ZUJ5SWQsIHsgaWQ6IHByZXZpb3VzSWQgfSlcbiAgfSk7XG5cbiAgaWYgKGxhYlNoZWxsKSB7XG4gICAgdm9pZCBhcHAucmVzdG9yZWQudGhlbigoKSA9PiB7XG4gICAgICAvLyBJdGVyYXRlIG92ZXIgdGhlIGN1cnJlbnQgd2lkZ2V0cyBpbiB0aGVcbiAgICAgIC8vIG1haW4gYXJlYSwgYW5kIGFkZCB0aGVtIHRvIHRoZSB0YWIgZ3JvdXBcbiAgICAgIC8vIG9mIHRoZSBtZW51LlxuICAgICAgY29uc3QgcG9wdWxhdGVUYWJzID0gKCkgPT4ge1xuICAgICAgICAvLyByZW1vdmUgdGhlIHByZXZpb3VzIHRhYiBsaXN0XG4gICAgICAgIGlmIChkaXNwb3NhYmxlICYmICFkaXNwb3NhYmxlLmlzRGlzcG9zZWQpIHtcbiAgICAgICAgICBkaXNwb3NhYmxlLmRpc3Bvc2UoKTtcbiAgICAgICAgfVxuICAgICAgICB0YWJHcm91cC5sZW5ndGggPSAwO1xuXG4gICAgICAgIGxldCBpc1ByZXZpb3VzbHlVc2VkVGFiQXR0YWNoZWQgPSBmYWxzZTtcbiAgICAgICAgZWFjaChhcHAuc2hlbGwud2lkZ2V0cygnbWFpbicpLCB3aWRnZXQgPT4ge1xuICAgICAgICAgIGlmICh3aWRnZXQuaWQgPT09IHByZXZpb3VzSWQpIHtcbiAgICAgICAgICAgIGlzUHJldmlvdXNseVVzZWRUYWJBdHRhY2hlZCA9IHRydWU7XG4gICAgICAgICAgfVxuICAgICAgICAgIHRhYkdyb3VwLnB1c2goe1xuICAgICAgICAgICAgY29tbWFuZDogQ29tbWFuZElEcy5hY3RpdmF0ZUJ5SWQsXG4gICAgICAgICAgICBhcmdzOiB7IGlkOiB3aWRnZXQuaWQgfVxuICAgICAgICAgIH0pO1xuICAgICAgICB9KTtcbiAgICAgICAgZGlzcG9zYWJsZSA9IG1lbnUuYWRkR3JvdXAodGFiR3JvdXAsIDEpO1xuICAgICAgICBwcmV2aW91c0lkID0gaXNQcmV2aW91c2x5VXNlZFRhYkF0dGFjaGVkID8gcHJldmlvdXNJZCA6ICcnO1xuICAgICAgfTtcbiAgICAgIHBvcHVsYXRlVGFicygpO1xuICAgICAgbGFiU2hlbGwubGF5b3V0TW9kaWZpZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICAgIHBvcHVsYXRlVGFicygpO1xuICAgICAgfSk7XG4gICAgICAvLyBVcGRhdGUgdGhlIElEIG9mIHRoZSBwcmV2aW91cyBhY3RpdmUgdGFiIGlmIGEgbmV3IHRhYiBpcyBzZWxlY3RlZC5cbiAgICAgIGxhYlNoZWxsLmN1cnJlbnRDaGFuZ2VkLmNvbm5lY3QoKF8sIGFyZ3MpID0+IHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gYXJncy5vbGRWYWx1ZTtcbiAgICAgICAgaWYgKCF3aWRnZXQpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cbiAgICAgICAgcHJldmlvdXNJZCA9IHdpZGdldC5pZDtcbiAgICAgIH0pO1xuICAgIH0pO1xuICB9XG59XG5cbi8qKlxuICogQ3JlYXRlIHRoZSBiYXNpYyBgSGVscGAgbWVudS5cbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIGNyZWF0ZUhlbHBNZW51KFxuICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgbWVudTogSUhlbHBNZW51LFxuICB0cmFuczogVHJhbnNsYXRpb25CdW5kbGVcbik6IHZvaWQge1xuICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChcbiAgICBDb21tYW5kSURzLmdldEtlcm5lbCxcbiAgICBjcmVhdGVTZW1hbnRpY0NvbW1hbmQoXG4gICAgICBhcHAsXG4gICAgICBtZW51LmdldEtlcm5lbCxcbiAgICAgIHtcbiAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdHZXQgS2VybmVsJyksXG4gICAgICAgIGlzVmlzaWJsZTogZmFsc2VcbiAgICAgIH0sXG4gICAgICB0cmFuc1xuICAgIClcbiAgKTtcbn1cblxuZXhwb3J0IGRlZmF1bHQgcGx1Z2luO1xuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBQcml2YXRlIGRhdGEuXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgYXN5bmMgZnVuY3Rpb24gZGlzcGxheUluZm9ybWF0aW9uKHRyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZSk6IFByb21pc2U8dm9pZD4ge1xuICAgIGNvbnN0IHJlc3VsdCA9IGF3YWl0IHNob3dEaWFsb2coe1xuICAgICAgdGl0bGU6IHRyYW5zLl9fKCdJbmZvcm1hdGlvbicpLFxuICAgICAgYm9keTogdHJhbnMuX18oXG4gICAgICAgICdNZW51IGN1c3RvbWl6YXRpb24gaGFzIGNoYW5nZWQuIFlvdSB3aWxsIG5lZWQgdG8gcmVsb2FkIEp1cHl0ZXJMYWIgdG8gc2VlIHRoZSBjaGFuZ2VzLidcbiAgICAgICksXG4gICAgICBidXR0b25zOiBbXG4gICAgICAgIERpYWxvZy5jYW5jZWxCdXR0b24oKSxcbiAgICAgICAgRGlhbG9nLm9rQnV0dG9uKHsgbGFiZWw6IHRyYW5zLl9fKCdSZWxvYWQnKSB9KVxuICAgICAgXVxuICAgIH0pO1xuXG4gICAgaWYgKHJlc3VsdC5idXR0b24uYWNjZXB0KSB7XG4gICAgICBsb2NhdGlvbi5yZWxvYWQoKTtcbiAgICB9XG4gIH1cblxuICBleHBvcnQgYXN5bmMgZnVuY3Rpb24gbG9hZFNldHRpbmdzTWVudShcbiAgICByZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSxcbiAgICBhZGRNZW51OiAobWVudTogTWVudSkgPT4gdm9pZCxcbiAgICBtZW51RmFjdG9yeTogKG9wdGlvbnM6IElNYWluTWVudS5JTWVudU9wdGlvbnMpID0+IEp1cHl0ZXJMYWJNZW51LFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yXG4gICk6IFByb21pc2U8dm9pZD4ge1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgbGV0IGNhbm9uaWNhbDogSVNldHRpbmdSZWdpc3RyeS5JU2NoZW1hIHwgbnVsbCA9IG51bGw7XG4gICAgbGV0IGxvYWRlZDogeyBbbmFtZTogc3RyaW5nXTogSVNldHRpbmdSZWdpc3RyeS5JTWVudVtdIH0gPSB7fTtcblxuICAgIC8qKlxuICAgICAqIFBvcHVsYXRlIHRoZSBwbHVnaW4ncyBzY2hlbWEgZGVmYXVsdHMuXG4gICAgICovXG4gICAgZnVuY3Rpb24gcG9wdWxhdGUoc2NoZW1hOiBJU2V0dGluZ1JlZ2lzdHJ5LklTY2hlbWEpIHtcbiAgICAgIGxvYWRlZCA9IHt9O1xuICAgICAgY29uc3QgcGx1Z2luRGVmYXVsdHMgPSBPYmplY3Qua2V5cyhyZWdpc3RyeS5wbHVnaW5zKVxuICAgICAgICAubWFwKHBsdWdpbiA9PiB7XG4gICAgICAgICAgY29uc3QgbWVudXMgPVxuICAgICAgICAgICAgcmVnaXN0cnkucGx1Z2luc1twbHVnaW5dIS5zY2hlbWFbJ2p1cHl0ZXIubGFiLm1lbnVzJ10/Lm1haW4gPz8gW107XG4gICAgICAgICAgbG9hZGVkW3BsdWdpbl0gPSBtZW51cztcbiAgICAgICAgICByZXR1cm4gbWVudXM7XG4gICAgICAgIH0pXG4gICAgICAgIC5jb25jYXQoW3NjaGVtYVsnanVweXRlci5sYWIubWVudXMnXT8ubWFpbiA/PyBbXV0pXG4gICAgICAgIC5yZWR1Y2VSaWdodChcbiAgICAgICAgICAoYWNjLCB2YWwpID0+IFNldHRpbmdSZWdpc3RyeS5yZWNvbmNpbGVNZW51cyhhY2MsIHZhbCwgdHJ1ZSksXG4gICAgICAgICAgc2NoZW1hLnByb3BlcnRpZXMhLm1lbnVzLmRlZmF1bHQgYXMgYW55W11cbiAgICAgICAgKTtcblxuICAgICAgLy8gQXBwbHkgZGVmYXVsdCB2YWx1ZSBhcyBsYXN0IHN0ZXAgdG8gdGFrZSBpbnRvIGFjY291bnQgb3ZlcnJpZGVzLmpzb25cbiAgICAgIC8vIFRoZSBzdGFuZGFyZCBkZWZhdWx0IGJlaW5nIFtdIGFzIHRoZSBwbHVnaW4gbXVzdCB1c2UgYGp1cHl0ZXIubGFiLm1lbnVzLm1haW5gXG4gICAgICAvLyB0byBkZWZpbmUgdGhlaXIgZGVmYXVsdCB2YWx1ZS5cbiAgICAgIHNjaGVtYS5wcm9wZXJ0aWVzIS5tZW51cy5kZWZhdWx0ID0gU2V0dGluZ1JlZ2lzdHJ5LnJlY29uY2lsZU1lbnVzKFxuICAgICAgICBwbHVnaW5EZWZhdWx0cyxcbiAgICAgICAgc2NoZW1hLnByb3BlcnRpZXMhLm1lbnVzLmRlZmF1bHQgYXMgYW55W10sXG4gICAgICAgIHRydWVcbiAgICAgIClcbiAgICAgICAgLy8gZmxhdHRlbiBvbmUgbGV2ZWxcbiAgICAgICAgLnNvcnQoKGEsIGIpID0+IChhLnJhbmsgPz8gSW5maW5pdHkpIC0gKGIucmFuayA/PyBJbmZpbml0eSkpO1xuICAgIH1cblxuICAgIC8vIFRyYW5zZm9ybSB0aGUgcGx1Z2luIG9iamVjdCB0byByZXR1cm4gZGlmZmVyZW50IHNjaGVtYSB0aGFuIHRoZSBkZWZhdWx0LlxuICAgIHJlZ2lzdHJ5LnRyYW5zZm9ybShQTFVHSU5fSUQsIHtcbiAgICAgIGNvbXBvc2U6IHBsdWdpbiA9PiB7XG4gICAgICAgIC8vIE9ubHkgb3ZlcnJpZGUgdGhlIGNhbm9uaWNhbCBzY2hlbWEgdGhlIGZpcnN0IHRpbWUuXG4gICAgICAgIGlmICghY2Fub25pY2FsKSB7XG4gICAgICAgICAgY2Fub25pY2FsID0gSlNPTkV4dC5kZWVwQ29weShwbHVnaW4uc2NoZW1hKTtcbiAgICAgICAgICBwb3B1bGF0ZShjYW5vbmljYWwpO1xuICAgICAgICB9XG5cbiAgICAgICAgY29uc3QgZGVmYXVsdHMgPSBjYW5vbmljYWwucHJvcGVydGllcz8ubWVudXM/LmRlZmF1bHQgPz8gW107XG4gICAgICAgIGNvbnN0IHVzZXIgPSB7XG4gICAgICAgICAgLi4ucGx1Z2luLmRhdGEudXNlcixcbiAgICAgICAgICBtZW51czogcGx1Z2luLmRhdGEudXNlci5tZW51cyA/PyBbXVxuICAgICAgICB9O1xuICAgICAgICBjb25zdCBjb21wb3NpdGUgPSB7XG4gICAgICAgICAgLi4ucGx1Z2luLmRhdGEuY29tcG9zaXRlLFxuICAgICAgICAgIG1lbnVzOiBTZXR0aW5nUmVnaXN0cnkucmVjb25jaWxlTWVudXMoXG4gICAgICAgICAgICBkZWZhdWx0cyBhcyBJU2V0dGluZ1JlZ2lzdHJ5LklNZW51W10sXG4gICAgICAgICAgICB1c2VyLm1lbnVzIGFzIElTZXR0aW5nUmVnaXN0cnkuSU1lbnVbXVxuICAgICAgICAgIClcbiAgICAgICAgfTtcblxuICAgICAgICBwbHVnaW4uZGF0YSA9IHsgY29tcG9zaXRlLCB1c2VyIH07XG5cbiAgICAgICAgcmV0dXJuIHBsdWdpbjtcbiAgICAgIH0sXG4gICAgICBmZXRjaDogcGx1Z2luID0+IHtcbiAgICAgICAgLy8gT25seSBvdmVycmlkZSB0aGUgY2Fub25pY2FsIHNjaGVtYSB0aGUgZmlyc3QgdGltZS5cbiAgICAgICAgaWYgKCFjYW5vbmljYWwpIHtcbiAgICAgICAgICBjYW5vbmljYWwgPSBKU09ORXh0LmRlZXBDb3B5KHBsdWdpbi5zY2hlbWEpO1xuICAgICAgICAgIHBvcHVsYXRlKGNhbm9uaWNhbCk7XG4gICAgICAgIH1cblxuICAgICAgICByZXR1cm4ge1xuICAgICAgICAgIGRhdGE6IHBsdWdpbi5kYXRhLFxuICAgICAgICAgIGlkOiBwbHVnaW4uaWQsXG4gICAgICAgICAgcmF3OiBwbHVnaW4ucmF3LFxuICAgICAgICAgIHNjaGVtYTogY2Fub25pY2FsLFxuICAgICAgICAgIHZlcnNpb246IHBsdWdpbi52ZXJzaW9uXG4gICAgICAgIH07XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICAvLyBSZXBvcHVsYXRlIHRoZSBjYW5vbmljYWwgdmFyaWFibGUgYWZ0ZXIgdGhlIHNldHRpbmcgcmVnaXN0cnkgaGFzXG4gICAgLy8gcHJlbG9hZGVkIGFsbCBpbml0aWFsIHBsdWdpbnMuXG4gICAgY29uc3Qgc2V0dGluZ3MgPSBhd2FpdCByZWdpc3RyeS5sb2FkKFBMVUdJTl9JRCk7XG5cbiAgICBjb25zdCBjdXJyZW50TWVudXM6IElTZXR0aW5nUmVnaXN0cnkuSU1lbnVbXSA9XG4gICAgICBKU09ORXh0LmRlZXBDb3B5KHNldHRpbmdzLmNvbXBvc2l0ZS5tZW51cyBhcyBhbnkpID8/IFtdO1xuICAgIGNvbnN0IG1lbnVzID0gbmV3IEFycmF5PE1lbnU+KCk7XG4gICAgLy8gQ3JlYXRlIG1lbnUgZm9yIG5vbi1kaXNhYmxlZCBlbGVtZW50XG4gICAgTWVudUZhY3RvcnkuY3JlYXRlTWVudXMoXG4gICAgICBjdXJyZW50TWVudXNcbiAgICAgICAgLmZpbHRlcihtZW51ID0+ICFtZW51LmRpc2FibGVkKVxuICAgICAgICAubWFwKG1lbnUgPT4ge1xuICAgICAgICAgIHJldHVybiB7XG4gICAgICAgICAgICAuLi5tZW51LFxuICAgICAgICAgICAgaXRlbXM6IFNldHRpbmdSZWdpc3RyeS5maWx0ZXJEaXNhYmxlZEl0ZW1zKG1lbnUuaXRlbXMgPz8gW10pXG4gICAgICAgICAgfTtcbiAgICAgICAgfSksXG4gICAgICBtZW51RmFjdG9yeVxuICAgICkuZm9yRWFjaChtZW51ID0+IHtcbiAgICAgIG1lbnVzLnB1c2gobWVudSk7XG4gICAgICBhZGRNZW51KG1lbnUpO1xuICAgIH0pO1xuXG4gICAgc2V0dGluZ3MuY2hhbmdlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgIC8vIEFzIGV4dGVuc2lvbiBtYXkgY2hhbmdlIG1lbnUgdGhyb3VnaCBBUEksIHByb21wdCB0aGUgdXNlciB0byByZWxvYWQgaWYgdGhlXG4gICAgICAvLyBtZW51IGhhcyBiZWVuIHVwZGF0ZWQuXG4gICAgICBjb25zdCBuZXdNZW51cyA9IChzZXR0aW5ncy5jb21wb3NpdGUubWVudXMgYXMgYW55KSA/PyBbXTtcbiAgICAgIGlmICghSlNPTkV4dC5kZWVwRXF1YWwoY3VycmVudE1lbnVzLCBuZXdNZW51cykpIHtcbiAgICAgICAgdm9pZCBkaXNwbGF5SW5mb3JtYXRpb24odHJhbnMpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgcmVnaXN0cnkucGx1Z2luQ2hhbmdlZC5jb25uZWN0KGFzeW5jIChzZW5kZXIsIHBsdWdpbikgPT4ge1xuICAgICAgaWYgKHBsdWdpbiAhPT0gUExVR0lOX0lEKSB7XG4gICAgICAgIC8vIElmIHRoZSBwbHVnaW4gY2hhbmdlZCBpdHMgbWVudS5cbiAgICAgICAgY29uc3Qgb2xkTWVudXMgPSBsb2FkZWRbcGx1Z2luXSA/PyBbXTtcbiAgICAgICAgY29uc3QgbmV3TWVudXMgPVxuICAgICAgICAgIHJlZ2lzdHJ5LnBsdWdpbnNbcGx1Z2luXSEuc2NoZW1hWydqdXB5dGVyLmxhYi5tZW51cyddPy5tYWluID8/IFtdO1xuICAgICAgICBpZiAoIUpTT05FeHQuZGVlcEVxdWFsKG9sZE1lbnVzLCBuZXdNZW51cykpIHtcbiAgICAgICAgICBpZiAobG9hZGVkW3BsdWdpbl0pIHtcbiAgICAgICAgICAgIC8vIFRoZSBwbHVnaW4gaGFzIGNoYW5nZWQsIHJlcXVlc3QgdGhlIHVzZXIgdG8gcmVsb2FkIHRoZSBVSSAtIHRoaXMgc2hvdWxkIG5vdCBoYXBwZW5cbiAgICAgICAgICAgIGF3YWl0IGRpc3BsYXlJbmZvcm1hdGlvbih0cmFucyk7XG4gICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIC8vIFRoZSBwbHVnaW4gd2FzIG5vdCB5ZXQgbG9hZGVkIHdoZW4gdGhlIG1lbnUgd2FzIGJ1aWx0ID0+IHVwZGF0ZSB0aGUgbWVudVxuICAgICAgICAgICAgbG9hZGVkW3BsdWdpbl0gPSBKU09ORXh0LmRlZXBDb3B5KG5ld01lbnVzKTtcbiAgICAgICAgICAgIC8vIE1lcmdlIHBvdGVudGlhbCBkaXNhYmxlZCBzdGF0ZVxuICAgICAgICAgICAgY29uc3QgdG9BZGQgPSBTZXR0aW5nUmVnaXN0cnkucmVjb25jaWxlTWVudXMoXG4gICAgICAgICAgICAgIG5ld01lbnVzLFxuICAgICAgICAgICAgICBjdXJyZW50TWVudXMsXG4gICAgICAgICAgICAgIGZhbHNlLFxuICAgICAgICAgICAgICBmYWxzZVxuICAgICAgICAgICAgKVxuICAgICAgICAgICAgICAuZmlsdGVyKG1lbnUgPT4gIW1lbnUuZGlzYWJsZWQpXG4gICAgICAgICAgICAgIC5tYXAobWVudSA9PiB7XG4gICAgICAgICAgICAgICAgcmV0dXJuIHtcbiAgICAgICAgICAgICAgICAgIC4uLm1lbnUsXG4gICAgICAgICAgICAgICAgICBpdGVtczogU2V0dGluZ1JlZ2lzdHJ5LmZpbHRlckRpc2FibGVkSXRlbXMobWVudS5pdGVtcyA/PyBbXSlcbiAgICAgICAgICAgICAgICB9O1xuICAgICAgICAgICAgICB9KTtcblxuICAgICAgICAgICAgTWVudUZhY3RvcnkudXBkYXRlTWVudXMobWVudXMsIHRvQWRkLCBtZW51RmFjdG9yeSkuZm9yRWFjaChtZW51ID0+IHtcbiAgICAgICAgICAgICAgYWRkTWVudShtZW51KTtcbiAgICAgICAgICAgIH0pO1xuICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgfVxuICAgIH0pO1xuICB9XG59XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=