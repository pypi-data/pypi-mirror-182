"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_help-extension_lib_index_js"],{

/***/ "../../packages/help-extension/lib/index.js":
/*!**************************************************!*\
  !*** ../../packages/help-extension/lib/index.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
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
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _licenses__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./licenses */ "../../packages/help-extension/lib/licenses.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module help-extension
 */









/**
 * The command IDs used by the help plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.open = 'help:open';
    CommandIDs.about = 'help:about';
    CommandIDs.activate = 'help:activate';
    CommandIDs.close = 'help:close';
    CommandIDs.show = 'help:show';
    CommandIDs.hide = 'help:hide';
    CommandIDs.jupyterForum = 'help:jupyter-forum';
    CommandIDs.licenses = 'help:licenses';
    CommandIDs.licenseReport = 'help:license-report';
    CommandIDs.refreshLicenses = 'help:licenses-refresh';
})(CommandIDs || (CommandIDs = {}));
/**
 * A flag denoting whether the application is loaded over HTTPS.
 */
const LAB_IS_SECURE = window.location.protocol === 'https:';
/**
 * The class name added to the help widget.
 */
const HELP_CLASS = 'jp-Help';
/**
 * Add a command to show an About dialog.
 */
const about = {
    id: '@jupyterlab/help-extension:about',
    autoStart: true,
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.ITranslator],
    optional: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    activate: (app, translator, palette) => {
        const { commands } = app;
        const trans = translator.load('jupyterlab');
        const category = trans.__('Help');
        commands.addCommand(CommandIDs.about, {
            label: trans.__('About %1', app.name),
            execute: () => {
                // Create the header of the about dialog
                const versionNumber = trans.__('Version %1', app.version);
                const versionInfo = (react__WEBPACK_IMPORTED_MODULE_7__.createElement("span", { className: "jp-About-version-info" },
                    react__WEBPACK_IMPORTED_MODULE_7__.createElement("span", { className: "jp-About-version" }, versionNumber)));
                const title = (react__WEBPACK_IMPORTED_MODULE_7__.createElement("span", { className: "jp-About-header" },
                    react__WEBPACK_IMPORTED_MODULE_7__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.jupyterIcon.react, { margin: "7px 9.5px", height: "auto", width: "58px" }),
                    react__WEBPACK_IMPORTED_MODULE_7__.createElement("div", { className: "jp-About-header-info" },
                        react__WEBPACK_IMPORTED_MODULE_7__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.jupyterlabWordmarkIcon.react, { height: "auto", width: "196px" }),
                        versionInfo)));
                // Create the body of the about dialog
                const jupyterURL = 'https://jupyter.org/about.html';
                const contributorsURL = 'https://github.com/jupyterlab/jupyterlab/graphs/contributors';
                const externalLinks = (react__WEBPACK_IMPORTED_MODULE_7__.createElement("span", { className: "jp-About-externalLinks" },
                    react__WEBPACK_IMPORTED_MODULE_7__.createElement("a", { href: contributorsURL, target: "_blank", rel: "noopener noreferrer", className: "jp-Button-flat" }, trans.__('CONTRIBUTOR LIST')),
                    react__WEBPACK_IMPORTED_MODULE_7__.createElement("a", { href: jupyterURL, target: "_blank", rel: "noopener noreferrer", className: "jp-Button-flat" }, trans.__('ABOUT PROJECT JUPYTER'))));
                const copyright = (react__WEBPACK_IMPORTED_MODULE_7__.createElement("span", { className: "jp-About-copyright" }, trans.__('© 2015-2022 Project Jupyter Contributors')));
                const body = (react__WEBPACK_IMPORTED_MODULE_7__.createElement("div", { className: "jp-About-body" },
                    externalLinks,
                    copyright));
                return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                    title,
                    body,
                    buttons: [
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.createButton({
                            label: trans.__('Dismiss'),
                            className: 'jp-About-button jp-mod-reject jp-mod-styled'
                        })
                    ]
                });
            }
        });
        if (palette) {
            palette.addItem({ command: CommandIDs.about, category });
        }
    }
};
/**
 * A plugin to add a command to open the Jupyter Forum.
 */
const jupyterForum = {
    id: '@jupyterlab/help-extension:jupyter-forum',
    autoStart: true,
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.ITranslator],
    optional: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    activate: (app, translator, palette) => {
        const { commands } = app;
        const trans = translator.load('jupyterlab');
        const category = trans.__('Help');
        commands.addCommand(CommandIDs.jupyterForum, {
            label: trans.__('Jupyter Forum'),
            execute: () => {
                window.open('https://discourse.jupyter.org/c/jupyterlab');
            }
        });
        if (palette) {
            palette.addItem({ command: CommandIDs.jupyterForum, category });
        }
    }
};
/**
 * A plugin to add a list of resources to the help menu.
 */
const resources = {
    id: '@jupyterlab/help-extension:resources',
    autoStart: true,
    requires: [_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__.IMainMenu, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.ITranslator],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer],
    activate: (app, mainMenu, translator, labShell, palette, restorer) => {
        const trans = translator.load('jupyterlab');
        let counter = 0;
        const category = trans.__('Help');
        const namespace = 'help-doc';
        const { commands, shell, serviceManager } = app;
        const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({ namespace });
        const resources = [
            {
                text: trans.__('JupyterLab Reference'),
                url: 'https://jupyterlab.readthedocs.io/en/latest/'
            },
            {
                text: trans.__('JupyterLab FAQ'),
                url: 'https://jupyterlab.readthedocs.io/en/latest/getting_started/faq.html'
            },
            {
                text: trans.__('Jupyter Reference'),
                url: 'https://jupyter.org/documentation'
            },
            {
                text: trans.__('Markdown Reference'),
                url: 'https://commonmark.org/help/'
            }
        ];
        resources.sort((a, b) => {
            return a.text.localeCompare(b.text);
        });
        /**
         * Create a new HelpWidget widget.
         */
        function newHelpWidget(url, text) {
            // Allow scripts and forms so that things like
            // readthedocs can use their search functionality.
            // We *don't* allow same origin requests, which
            // can prevent some content from being loaded onto the
            // help pages.
            const content = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.IFrame({
                sandbox: ['allow-scripts', 'allow-forms']
            });
            content.url = url;
            content.addClass(HELP_CLASS);
            content.title.label = text;
            content.id = `${namespace}-${++counter}`;
            const widget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget({ content });
            widget.addClass('jp-Help');
            return widget;
        }
        commands.addCommand(CommandIDs.open, {
            label: args => {
                var _a;
                return (_a = args['text']) !== null && _a !== void 0 ? _a : trans.__('Open the provided `url` in a tab.');
            },
            execute: args => {
                const url = args['url'];
                const text = args['text'];
                const newBrowserTab = args['newBrowserTab'] || false;
                // If help resource will generate a mixed content error, load externally.
                if (newBrowserTab ||
                    (LAB_IS_SECURE && _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.URLExt.parse(url).protocol !== 'https:')) {
                    window.open(url);
                    return;
                }
                const widget = newHelpWidget(url, text);
                void tracker.add(widget);
                shell.add(widget, 'main');
                return widget;
            }
        });
        // Handle state restoration.
        if (restorer) {
            void restorer.restore(tracker, {
                command: CommandIDs.open,
                args: widget => ({
                    url: widget.content.url,
                    text: widget.content.title.label
                }),
                name: widget => widget.content.url
            });
        }
        // Populate the Help menu.
        const helpMenu = mainMenu.helpMenu;
        const resourcesGroup = resources.map(args => ({
            args,
            command: CommandIDs.open
        }));
        helpMenu.addGroup(resourcesGroup, 10);
        // Generate a cache of the kernel help links.
        const kernelInfoCache = new Map();
        const onSessionRunningChanged = (m, sessions) => {
            var _a;
            // If a new session has been added, it is at the back
            // of the session list. If one has changed or stopped,
            // it does not hurt to check it.
            if (!sessions.length) {
                return;
            }
            const sessionModel = sessions[sessions.length - 1];
            if (!sessionModel.kernel ||
                kernelInfoCache.has(sessionModel.kernel.name)) {
                return;
            }
            const session = serviceManager.sessions.connectTo({
                model: sessionModel,
                kernelConnectionOptions: { handleComms: false }
            });
            void ((_a = session.kernel) === null || _a === void 0 ? void 0 : _a.info.then(kernelInfo => {
                var _a, _b;
                const name = session.kernel.name;
                // Check the cache second time so that, if two callbacks get scheduled,
                // they don't try to add the same commands.
                if (kernelInfoCache.has(name)) {
                    return;
                }
                const spec = (_b = (_a = serviceManager.kernelspecs) === null || _a === void 0 ? void 0 : _a.specs) === null || _b === void 0 ? void 0 : _b.kernelspecs[name];
                if (!spec) {
                    return;
                }
                // Set the Kernel Info cache.
                kernelInfoCache.set(name, kernelInfo);
                // Utility function to check if the current widget
                // has registered itself with the help menu.
                let usesKernel = false;
                const onCurrentChanged = async () => {
                    const kernel = await commands.execute('helpmenu:get-kernel');
                    usesKernel = (kernel === null || kernel === void 0 ? void 0 : kernel.name) === name;
                };
                // Set the status for the current widget
                onCurrentChanged().catch(error => {
                    console.error('Failed to get the kernel for the current widget.', error);
                });
                if (labShell) {
                    // Update status when current widget changes
                    labShell.currentChanged.connect(onCurrentChanged);
                }
                const isEnabled = () => usesKernel;
                // Add the kernel banner to the Help Menu.
                const bannerCommand = `help-menu-${name}:banner`;
                const kernelName = spec.display_name;
                let kernelIconUrl = spec.resources['logo-64x64'];
                commands.addCommand(bannerCommand, {
                    label: trans.__('About the %1 Kernel', kernelName),
                    isVisible: isEnabled,
                    isEnabled,
                    execute: () => {
                        // Create the header of the about dialog
                        const headerLogo = react__WEBPACK_IMPORTED_MODULE_7__.createElement("img", { src: kernelIconUrl });
                        const title = (react__WEBPACK_IMPORTED_MODULE_7__.createElement("span", { className: "jp-About-header" },
                            headerLogo,
                            react__WEBPACK_IMPORTED_MODULE_7__.createElement("div", { className: "jp-About-header-info" }, kernelName)));
                        const banner = react__WEBPACK_IMPORTED_MODULE_7__.createElement("pre", null, kernelInfo.banner);
                        const body = react__WEBPACK_IMPORTED_MODULE_7__.createElement("div", { className: "jp-About-body" }, banner);
                        return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                            title,
                            body,
                            buttons: [
                                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.createButton({
                                    label: trans.__('Dismiss'),
                                    className: 'jp-About-button jp-mod-reject jp-mod-styled'
                                })
                            ]
                        });
                    }
                });
                helpMenu.addGroup([{ command: bannerCommand }], 20);
                // Add the kernel info help_links to the Help menu.
                const kernelGroup = [];
                (kernelInfo.help_links || []).forEach(link => {
                    const commandId = `help-menu-${name}:${link.text}`;
                    commands.addCommand(commandId, {
                        label: commands.label(CommandIDs.open, link),
                        isVisible: isEnabled,
                        isEnabled,
                        execute: () => {
                            return commands.execute(CommandIDs.open, link);
                        }
                    });
                    kernelGroup.push({ command: commandId });
                });
                helpMenu.addGroup(kernelGroup, 21);
            }).then(() => {
                // Dispose of the session object since we no longer need it.
                session.dispose();
            }));
        };
        // Create menu items for currently running sessions
        (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_6__.each)(serviceManager.sessions.running(), model => {
            onSessionRunningChanged(serviceManager.sessions, [model]);
        });
        serviceManager.sessions.runningChanged.connect(onSessionRunningChanged);
        if (palette) {
            resources.forEach(args => {
                palette.addItem({ args, command: CommandIDs.open, category });
            });
            palette.addItem({
                args: { reload: true },
                command: 'apputils:reset',
                category
            });
        }
    }
};
/**
 * A plugin to add a licenses reporting tools.
 */
const licenses = {
    id: '@jupyterlab/help-extension:licenses',
    autoStart: true,
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.ITranslator],
    optional: [_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_3__.IMainMenu, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer],
    activate: (app, translator, menu, palette, restorer) => {
        // bail if no license API is available from the server
        if (!_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getOption('licensesUrl')) {
            return;
        }
        const { commands, shell } = app;
        const trans = translator.load('jupyterlab');
        // translation strings
        const category = trans.__('Help');
        const downloadAsText = trans.__('Download All Licenses as');
        const licensesText = trans.__('Licenses');
        const refreshLicenses = trans.__('Refresh Licenses');
        // an incrementer for license widget ids
        let counter = 0;
        const licensesUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.URLExt.join(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getBaseUrl(), _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PageConfig.getOption('licensesUrl')) + '/';
        const licensesNamespace = 'help-licenses';
        const licensesTracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
            namespace: licensesNamespace
        });
        /**
         * Return a full license report format based on a format name
         */
        function formatOrDefault(format) {
            return (_licenses__WEBPACK_IMPORTED_MODULE_8__.Licenses.REPORT_FORMATS[format] ||
                _licenses__WEBPACK_IMPORTED_MODULE_8__.Licenses.REPORT_FORMATS[_licenses__WEBPACK_IMPORTED_MODULE_8__.Licenses.DEFAULT_FORMAT]);
        }
        /**
         * Create a MainAreaWidget for a license viewer
         */
        function createLicenseWidget(args) {
            const licensesModel = new _licenses__WEBPACK_IMPORTED_MODULE_8__.Licenses.Model(Object.assign(Object.assign({}, args), { licensesUrl,
                trans, serverSettings: app.serviceManager.serverSettings }));
            const content = new _licenses__WEBPACK_IMPORTED_MODULE_8__.Licenses({ model: licensesModel });
            content.id = `${licensesNamespace}-${++counter}`;
            content.title.label = licensesText;
            content.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.copyrightIcon;
            const main = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget({
                content,
                reveal: licensesModel.licensesReady
            });
            main.toolbar.addItem('refresh-licenses', new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.CommandToolbarButton({
                id: CommandIDs.refreshLicenses,
                args: { noLabel: 1 },
                commands
            }));
            main.toolbar.addItem('spacer', _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.Toolbar.createSpacerItem());
            for (const format of Object.keys(_licenses__WEBPACK_IMPORTED_MODULE_8__.Licenses.REPORT_FORMATS)) {
                const button = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.CommandToolbarButton({
                    id: CommandIDs.licenseReport,
                    args: { format, noLabel: 1 },
                    commands
                });
                main.toolbar.addItem(`download-${format}`, button);
            }
            return main;
        }
        // register license-related commands
        commands.addCommand(CommandIDs.licenses, {
            label: licensesText,
            execute: (args) => {
                const licenseMain = createLicenseWidget(args);
                shell.add(licenseMain, 'main', { type: 'Licenses' });
                // add to tracker so it can be restored, and update when choices change
                void licensesTracker.add(licenseMain);
                licenseMain.content.model.trackerDataChanged.connect(() => {
                    void licensesTracker.save(licenseMain);
                });
                return licenseMain;
            }
        });
        commands.addCommand(CommandIDs.refreshLicenses, {
            label: args => (args.noLabel ? '' : refreshLicenses),
            caption: refreshLicenses,
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.refreshIcon,
            execute: async () => {
                var _a;
                return (_a = licensesTracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content.model.initLicenses();
            }
        });
        commands.addCommand(CommandIDs.licenseReport, {
            label: args => {
                if (args.noLabel) {
                    return '';
                }
                const format = formatOrDefault(`${args.format}`);
                return `${downloadAsText} ${format.title}`;
            },
            caption: args => {
                const format = formatOrDefault(`${args.format}`);
                return `${downloadAsText} ${format.title}`;
            },
            icon: args => {
                const format = formatOrDefault(`${args.format}`);
                return format.icon;
            },
            execute: async (args) => {
                var _a;
                const format = formatOrDefault(`${args.format}`);
                return await ((_a = licensesTracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content.model.download({
                    format: format.id
                }));
            }
        });
        // handle optional integrations
        if (palette) {
            palette.addItem({ command: CommandIDs.licenses, category });
        }
        if (menu) {
            const helpMenu = menu.helpMenu;
            helpMenu.addGroup([{ command: CommandIDs.licenses }], 0);
        }
        if (restorer) {
            void restorer.restore(licensesTracker, {
                command: CommandIDs.licenses,
                name: widget => 'licenses',
                args: widget => {
                    const { currentBundleName, currentPackageIndex, packageFilter } = widget.content.model;
                    const args = {
                        currentBundleName,
                        currentPackageIndex,
                        packageFilter
                    };
                    return args;
                }
            });
        }
    }
};
const plugins = [
    about,
    jupyterForum,
    resources,
    licenses
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ }),

/***/ "../../packages/help-extension/lib/licenses.js":
/*!*****************************************************!*\
  !*** ../../packages/help-extension/lib/licenses.js ***!
  \*****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Licenses": () => (/* binding */ Licenses)
/* harmony export */ });
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/virtualdom */ "webpack/sharing/consume/default/@lumino/virtualdom/@lumino/virtualdom");
/* harmony import */ var _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_virtualdom__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_6__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.







/**
 * A license viewer
 */
class Licenses extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.SplitPanel {
    constructor(options) {
        super();
        this.addClass('jp-Licenses');
        this.model = options.model;
        this.initLeftPanel();
        this.initFilters();
        this.initBundles();
        this.initGrid();
        this.initLicenseText();
        this.setRelativeSizes([1, 2, 3]);
        void this.model.initLicenses().then(() => this._updateBundles());
        this.model.trackerDataChanged.connect(() => {
            this.title.label = this.model.title;
        });
    }
    /**
     * Handle disposing of the widget
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        this._bundles.currentChanged.disconnect(this.onBundleSelected, this);
        this.model.dispose();
        super.dispose();
    }
    /**
     * Initialize the left area for filters and bundles
     */
    initLeftPanel() {
        this._leftPanel = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.Panel();
        this._leftPanel.addClass('jp-Licenses-FormArea');
        this.addWidget(this._leftPanel);
        _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.SplitPanel.setStretch(this._leftPanel, 1);
    }
    /**
     * Initialize the filters
     */
    initFilters() {
        this._filters = new Licenses.Filters(this.model);
        _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.SplitPanel.setStretch(this._filters, 1);
        this._leftPanel.addWidget(this._filters);
    }
    /**
     * Initialize the listing of available bundles
     */
    initBundles() {
        this._bundles = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.TabBar({
            orientation: 'vertical',
            renderer: new Licenses.BundleTabRenderer(this.model)
        });
        this._bundles.addClass('jp-Licenses-Bundles');
        _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.SplitPanel.setStretch(this._bundles, 1);
        this._leftPanel.addWidget(this._bundles);
        this._bundles.currentChanged.connect(this.onBundleSelected, this);
        this.model.stateChanged.connect(() => this._bundles.update());
    }
    /**
     * Initialize the listing of packages within the current bundle
     */
    initGrid() {
        this._grid = new Licenses.Grid(this.model);
        _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.SplitPanel.setStretch(this._grid, 1);
        this.addWidget(this._grid);
    }
    /**
     * Initialize the full text of the current package
     */
    initLicenseText() {
        this._licenseText = new Licenses.FullText(this.model);
        _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.SplitPanel.setStretch(this._grid, 1);
        this.addWidget(this._licenseText);
    }
    /**
     * Event handler for updating the model with the current bundle
     */
    onBundleSelected() {
        var _a;
        if ((_a = this._bundles.currentTitle) === null || _a === void 0 ? void 0 : _a.label) {
            this.model.currentBundleName = this._bundles.currentTitle.label;
        }
    }
    /**
     * Update the bundle tabs.
     */
    _updateBundles() {
        this._bundles.clearTabs();
        let i = 0;
        const { currentBundleName } = this.model;
        let currentIndex = 0;
        for (const bundle of this.model.bundleNames) {
            const tab = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.Widget();
            tab.title.label = bundle;
            if (bundle === currentBundleName) {
                currentIndex = i;
            }
            this._bundles.insertTab(++i, tab.title);
        }
        this._bundles.currentIndex = currentIndex;
    }
}
/** A namespace for license components */
(function (Licenses) {
    /**
     * License report formats understood by the server (once lower-cased)
     */
    Licenses.REPORT_FORMATS = {
        markdown: {
            id: 'markdown',
            title: 'Markdown',
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.markdownIcon
        },
        csv: {
            id: 'csv',
            title: 'CSV',
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.spreadsheetIcon
        },
        json: {
            id: 'csv',
            title: 'JSON',
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.jsonIcon
        }
    };
    /**
     * The default format (most human-readable)
     */
    Licenses.DEFAULT_FORMAT = 'markdown';
    /**
     * A model for license data
     */
    class Model extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.VDomModel {
        constructor(options) {
            super();
            this._selectedPackageChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal(this);
            this._trackerDataChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal(this);
            this._currentPackageIndex = 0;
            this._licensesReady = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__.PromiseDelegate();
            this._packageFilter = {};
            this._trans = options.trans;
            this._licensesUrl = options.licensesUrl;
            this._serverSettings =
                options.serverSettings || _jupyterlab_services__WEBPACK_IMPORTED_MODULE_0__.ServerConnection.makeSettings();
            if (options.currentBundleName) {
                this._currentBundleName = options.currentBundleName;
            }
            if (options.packageFilter) {
                this._packageFilter = options.packageFilter;
            }
            if (options.currentPackageIndex) {
                this._currentPackageIndex = options.currentPackageIndex;
            }
        }
        /**
         * Handle the initial request for the licenses from the server.
         */
        async initLicenses() {
            try {
                const response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_0__.ServerConnection.makeRequest(this._licensesUrl, {}, this._serverSettings);
                this._serverResponse = await response.json();
                this._licensesReady.resolve();
                this.stateChanged.emit(void 0);
            }
            catch (err) {
                this._licensesReady.reject(err);
            }
        }
        /**
         * Create a temporary download link, and emulate clicking it to trigger a named
         * file download.
         */
        async download(options) {
            const url = `${this._licensesUrl}?format=${options.format}&download=1`;
            const element = document.createElement('a');
            element.href = url;
            element.download = '';
            document.body.appendChild(element);
            element.click();
            document.body.removeChild(element);
            return void 0;
        }
        /**
         * A promise that resolves when the licenses from the server change
         */
        get selectedPackageChanged() {
            return this._selectedPackageChanged;
        }
        /**
         * A promise that resolves when the trackable data changes
         */
        get trackerDataChanged() {
            return this._trackerDataChanged;
        }
        /**
         * The names of the license bundles available
         */
        get bundleNames() {
            var _a;
            return Object.keys(((_a = this._serverResponse) === null || _a === void 0 ? void 0 : _a.bundles) || {});
        }
        /**
         * The current license bundle
         */
        get currentBundleName() {
            if (this._currentBundleName) {
                return this._currentBundleName;
            }
            if (this.bundleNames.length) {
                return this.bundleNames[0];
            }
            return null;
        }
        /**
         * Set the current license bundle, and reset the selected index
         */
        set currentBundleName(currentBundleName) {
            if (this._currentBundleName !== currentBundleName) {
                this._currentBundleName = currentBundleName;
                this.stateChanged.emit(void 0);
                this._trackerDataChanged.emit(void 0);
            }
        }
        /**
         * A promise that resolves when the licenses are available from the server
         */
        get licensesReady() {
            return this._licensesReady.promise;
        }
        /**
         * All the license bundles, keyed by the distributing packages
         */
        get bundles() {
            var _a;
            return ((_a = this._serverResponse) === null || _a === void 0 ? void 0 : _a.bundles) || {};
        }
        /**
         * The index of the currently-selected package within its license bundle
         */
        get currentPackageIndex() {
            return this._currentPackageIndex;
        }
        /**
         * Update the currently-selected package within its license bundle
         */
        set currentPackageIndex(currentPackageIndex) {
            if (this._currentPackageIndex === currentPackageIndex) {
                return;
            }
            this._currentPackageIndex = currentPackageIndex;
            this._selectedPackageChanged.emit(void 0);
            this.stateChanged.emit(void 0);
            this._trackerDataChanged.emit(void 0);
        }
        /**
         * The license data for the currently-selected package
         */
        get currentPackage() {
            var _a;
            if (this.currentBundleName &&
                this.bundles &&
                this._currentPackageIndex != null) {
                return this.getFilteredPackages(((_a = this.bundles[this.currentBundleName]) === null || _a === void 0 ? void 0 : _a.packages) || [])[this._currentPackageIndex];
            }
            return null;
        }
        /**
         * A translation bundle
         */
        get trans() {
            return this._trans;
        }
        get title() {
            return `${this._currentBundleName || ''} ${this._trans.__('Licenses')}`.trim();
        }
        /**
         * The current package filter
         */
        get packageFilter() {
            return this._packageFilter;
        }
        set packageFilter(packageFilter) {
            this._packageFilter = packageFilter;
            this.stateChanged.emit(void 0);
            this._trackerDataChanged.emit(void 0);
        }
        /**
         * Get filtered packages from current bundle where at least one token of each
         * key is present.
         */
        getFilteredPackages(allRows) {
            let rows = [];
            let filters = Object.entries(this._packageFilter)
                .filter(([k, v]) => v && `${v}`.trim().length)
                .map(([k, v]) => [k, `${v}`.toLowerCase().trim().split(' ')]);
            for (const row of allRows) {
                let keyHits = 0;
                for (const [key, bits] of filters) {
                    let bitHits = 0;
                    let rowKeyValue = `${row[key]}`.toLowerCase();
                    for (const bit of bits) {
                        if (rowKeyValue.includes(bit)) {
                            bitHits += 1;
                        }
                    }
                    if (bitHits) {
                        keyHits += 1;
                    }
                }
                if (keyHits === filters.length) {
                    rows.push(row);
                }
            }
            return Object.values(rows);
        }
    }
    Licenses.Model = Model;
    /**
     * A filter form for limiting the packages displayed
     */
    class Filters extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.VDomRenderer {
        constructor(model) {
            super(model);
            /**
             * Render a filter input
             */
            this.renderFilter = (key) => {
                const value = this.model.packageFilter[key] || '';
                return (react__WEBPACK_IMPORTED_MODULE_6__.createElement("input", { type: "text", name: key, defaultValue: value, className: "jp-mod-styled", onInput: this.onFilterInput }));
            };
            /**
             * Handle a filter input changing
             */
            this.onFilterInput = (evt) => {
                const input = evt.currentTarget;
                const { name, value } = input;
                this.model.packageFilter = Object.assign(Object.assign({}, this.model.packageFilter), { [name]: value });
            };
            this.addClass('jp-Licenses-Filters');
            this.addClass('jp-RenderedHTMLCommon');
        }
        render() {
            const { trans } = this.model;
            return (react__WEBPACK_IMPORTED_MODULE_6__.createElement("div", null,
                react__WEBPACK_IMPORTED_MODULE_6__.createElement("label", null,
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("strong", null, trans.__('Filter Licenses By'))),
                react__WEBPACK_IMPORTED_MODULE_6__.createElement("ul", null,
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("li", null,
                        react__WEBPACK_IMPORTED_MODULE_6__.createElement("label", null, trans.__('Package')),
                        this.renderFilter('name')),
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("li", null,
                        react__WEBPACK_IMPORTED_MODULE_6__.createElement("label", null, trans.__('Version')),
                        this.renderFilter('versionInfo')),
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("li", null,
                        react__WEBPACK_IMPORTED_MODULE_6__.createElement("label", null, trans.__('License')),
                        this.renderFilter('licenseId'))),
                react__WEBPACK_IMPORTED_MODULE_6__.createElement("label", null,
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("strong", null, trans.__('Distributions')))));
        }
    }
    Licenses.Filters = Filters;
    /**
     * A fancy bundle renderer with the package count
     */
    class BundleTabRenderer extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.TabBar.Renderer {
        constructor(model) {
            super();
            this.closeIconSelector = '.lm-TabBar-tabCloseIcon';
            this.model = model;
        }
        /**
         * Render a full bundle
         */
        renderTab(data) {
            let title = data.title.caption;
            let key = this.createTabKey(data);
            let style = this.createTabStyle(data);
            let className = this.createTabClass(data);
            let dataset = this.createTabDataset(data);
            return _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_4__.h.li({ key, className, title, style, dataset }, this.renderIcon(data), this.renderLabel(data), this.renderCountBadge(data));
        }
        /**
         * Render the package count
         */
        renderCountBadge(data) {
            const bundle = data.title.label;
            const { bundles } = this.model;
            const packages = this.model.getFilteredPackages((bundles && bundle ? bundles[bundle].packages : []) || []);
            return _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_4__.h.label({}, `${packages.length}`);
        }
    }
    Licenses.BundleTabRenderer = BundleTabRenderer;
    /**
     * A grid of licenses
     */
    class Grid extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.VDomRenderer {
        constructor(model) {
            super(model);
            /**
             * Render a single package's license information
             */
            this.renderRow = (row, index) => {
                const selected = index === this.model.currentPackageIndex;
                const onCheck = () => (this.model.currentPackageIndex = index);
                return (react__WEBPACK_IMPORTED_MODULE_6__.createElement("tr", { key: row.name, className: selected ? 'jp-mod-selected' : '', onClick: onCheck },
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("td", null,
                        react__WEBPACK_IMPORTED_MODULE_6__.createElement("input", { type: "radio", name: "show-package-license", value: index, onChange: onCheck, checked: selected })),
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("th", null, row.name),
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("td", null,
                        react__WEBPACK_IMPORTED_MODULE_6__.createElement("code", null, row.versionInfo)),
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("td", null,
                        react__WEBPACK_IMPORTED_MODULE_6__.createElement("code", null, row.licenseId))));
            };
            this.addClass('jp-Licenses-Grid');
            this.addClass('jp-RenderedHTMLCommon');
        }
        /**
         * Render a grid of package license information
         */
        render() {
            var _a;
            const { bundles, currentBundleName, trans } = this.model;
            const filteredPackages = this.model.getFilteredPackages(bundles && currentBundleName
                ? ((_a = bundles[currentBundleName]) === null || _a === void 0 ? void 0 : _a.packages) || []
                : []);
            if (!filteredPackages.length) {
                return (react__WEBPACK_IMPORTED_MODULE_6__.createElement("blockquote", null,
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("em", null, trans.__('No Packages found'))));
            }
            return (react__WEBPACK_IMPORTED_MODULE_6__.createElement("form", null,
                react__WEBPACK_IMPORTED_MODULE_6__.createElement("table", null,
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("thead", null,
                        react__WEBPACK_IMPORTED_MODULE_6__.createElement("tr", null,
                            react__WEBPACK_IMPORTED_MODULE_6__.createElement("td", null),
                            react__WEBPACK_IMPORTED_MODULE_6__.createElement("th", null, trans.__('Package')),
                            react__WEBPACK_IMPORTED_MODULE_6__.createElement("th", null, trans.__('Version')),
                            react__WEBPACK_IMPORTED_MODULE_6__.createElement("th", null, trans.__('License')))),
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("tbody", null, filteredPackages.map(this.renderRow)))));
        }
    }
    Licenses.Grid = Grid;
    /**
     * A package's full license text
     */
    class FullText extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.VDomRenderer {
        constructor(model) {
            super(model);
            this.addClass('jp-Licenses-Text');
            this.addClass('jp-RenderedHTMLCommon');
            this.addClass('jp-RenderedMarkdown');
        }
        /**
         * Render the license text, or a null state if no package is selected
         */
        render() {
            const { currentPackage, trans } = this.model;
            let head = '';
            let quote = trans.__('No Package selected');
            let code = '';
            if (currentPackage) {
                const { name, versionInfo, licenseId, extractedText } = currentPackage;
                head = `${name} v${versionInfo}`;
                quote = `${trans.__('License')}: ${licenseId || trans.__('No License ID found')}`;
                code = extractedText || trans.__('No License Text found');
            }
            return [
                react__WEBPACK_IMPORTED_MODULE_6__.createElement("h1", { key: "h1" }, head),
                react__WEBPACK_IMPORTED_MODULE_6__.createElement("blockquote", { key: "quote" },
                    react__WEBPACK_IMPORTED_MODULE_6__.createElement("em", null, quote)),
                react__WEBPACK_IMPORTED_MODULE_6__.createElement("code", { key: "code" }, code)
            ];
        }
    }
    Licenses.FullText = FullText;
})(Licenses || (Licenses = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfaGVscC1leHRlbnNpb25fbGliX2luZGV4X2pzLjEwZDM1OTI2Njc3MzFjMTdkODY3LmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBTzhCO0FBT0g7QUFDNkI7QUFDVjtBQUVLO0FBU25CO0FBRU07QUFFVjtBQUNPO0FBRXRDOztHQUVHO0FBQ0gsSUFBVSxVQUFVLENBb0JuQjtBQXBCRCxXQUFVLFVBQVU7SUFDTCxlQUFJLEdBQUcsV0FBVyxDQUFDO0lBRW5CLGdCQUFLLEdBQUcsWUFBWSxDQUFDO0lBRXJCLG1CQUFRLEdBQUcsZUFBZSxDQUFDO0lBRTNCLGdCQUFLLEdBQUcsWUFBWSxDQUFDO0lBRXJCLGVBQUksR0FBRyxXQUFXLENBQUM7SUFFbkIsZUFBSSxHQUFHLFdBQVcsQ0FBQztJQUVuQix1QkFBWSxHQUFHLG9CQUFvQixDQUFDO0lBRXBDLG1CQUFRLEdBQUcsZUFBZSxDQUFDO0lBRTNCLHdCQUFhLEdBQUcscUJBQXFCLENBQUM7SUFFdEMsMEJBQWUsR0FBRyx1QkFBdUIsQ0FBQztBQUN6RCxDQUFDLEVBcEJTLFVBQVUsS0FBVixVQUFVLFFBb0JuQjtBQUVEOztHQUVHO0FBQ0gsTUFBTSxhQUFhLEdBQUcsTUFBTSxDQUFDLFFBQVEsQ0FBQyxRQUFRLEtBQUssUUFBUSxDQUFDO0FBRTVEOztHQUVHO0FBQ0gsTUFBTSxVQUFVLEdBQUcsU0FBUyxDQUFDO0FBRTdCOztHQUVHO0FBQ0gsTUFBTSxLQUFLLEdBQWdDO0lBQ3pDLEVBQUUsRUFBRSxrQ0FBa0M7SUFDdEMsU0FBUyxFQUFFLElBQUk7SUFDZixRQUFRLEVBQUUsQ0FBQyxnRUFBVyxDQUFDO0lBQ3ZCLFFBQVEsRUFBRSxDQUFDLGlFQUFlLENBQUM7SUFDM0IsUUFBUSxFQUFFLENBQ1IsR0FBb0IsRUFDcEIsVUFBdUIsRUFDdkIsT0FBK0IsRUFDekIsRUFBRTtRQUNSLE1BQU0sRUFB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LXRvcC8uLi8uLi9wYWNrYWdlcy9oZWxwLWV4dGVuc2lvbi9zcmMvaW5kZXgudHN4Iiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9oZWxwLWV4dGVuc2lvbi9zcmMvbGljZW5zZXMudHN4Il0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGhlbHAtZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSUxhYlNoZWxsLFxuICBJTGF5b3V0UmVzdG9yZXIsXG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7XG4gIERpYWxvZyxcbiAgSUNvbW1hbmRQYWxldHRlLFxuICBNYWluQXJlYVdpZGdldCxcbiAgc2hvd0RpYWxvZyxcbiAgV2lkZ2V0VHJhY2tlclxufSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBQYWdlQ29uZmlnLCBVUkxFeHQgfSBmcm9tICdAanVweXRlcmxhYi9jb3JldXRpbHMnO1xuaW1wb3J0IHsgSU1haW5NZW51IH0gZnJvbSAnQGp1cHl0ZXJsYWIvbWFpbm1lbnUnO1xuaW1wb3J0IHsgS2VybmVsLCBLZXJuZWxNZXNzYWdlLCBTZXNzaW9uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2VydmljZXMnO1xuaW1wb3J0IHsgSVRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQge1xuICBDb21tYW5kVG9vbGJhckJ1dHRvbixcbiAgY29weXJpZ2h0SWNvbixcbiAgSUZyYW1lLFxuICBqdXB5dGVySWNvbixcbiAganVweXRlcmxhYldvcmRtYXJrSWNvbixcbiAgcmVmcmVzaEljb24sXG4gIFRvb2xiYXJcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBSZWFkb25seUpTT05PYmplY3QgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBlYWNoIH0gZnJvbSAnQGx1bWluby9hbGdvcml0aG0nO1xuaW1wb3J0IHsgTWVudSB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgKiBhcyBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQgeyBMaWNlbnNlcyB9IGZyb20gJy4vbGljZW5zZXMnO1xuXG4vKipcbiAqIFRoZSBjb21tYW5kIElEcyB1c2VkIGJ5IHRoZSBoZWxwIHBsdWdpbi5cbiAqL1xubmFtZXNwYWNlIENvbW1hbmRJRHMge1xuICBleHBvcnQgY29uc3Qgb3BlbiA9ICdoZWxwOm9wZW4nO1xuXG4gIGV4cG9ydCBjb25zdCBhYm91dCA9ICdoZWxwOmFib3V0JztcblxuICBleHBvcnQgY29uc3QgYWN0aXZhdGUgPSAnaGVscDphY3RpdmF0ZSc7XG5cbiAgZXhwb3J0IGNvbnN0IGNsb3NlID0gJ2hlbHA6Y2xvc2UnO1xuXG4gIGV4cG9ydCBjb25zdCBzaG93ID0gJ2hlbHA6c2hvdyc7XG5cbiAgZXhwb3J0IGNvbnN0IGhpZGUgPSAnaGVscDpoaWRlJztcblxuICBleHBvcnQgY29uc3QganVweXRlckZvcnVtID0gJ2hlbHA6anVweXRlci1mb3J1bSc7XG5cbiAgZXhwb3J0IGNvbnN0IGxpY2Vuc2VzID0gJ2hlbHA6bGljZW5zZXMnO1xuXG4gIGV4cG9ydCBjb25zdCBsaWNlbnNlUmVwb3J0ID0gJ2hlbHA6bGljZW5zZS1yZXBvcnQnO1xuXG4gIGV4cG9ydCBjb25zdCByZWZyZXNoTGljZW5zZXMgPSAnaGVscDpsaWNlbnNlcy1yZWZyZXNoJztcbn1cblxuLyoqXG4gKiBBIGZsYWcgZGVub3Rpbmcgd2hldGhlciB0aGUgYXBwbGljYXRpb24gaXMgbG9hZGVkIG92ZXIgSFRUUFMuXG4gKi9cbmNvbnN0IExBQl9JU19TRUNVUkUgPSB3aW5kb3cubG9jYXRpb24ucHJvdG9jb2wgPT09ICdodHRwczonO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIHRoZSBoZWxwIHdpZGdldC5cbiAqL1xuY29uc3QgSEVMUF9DTEFTUyA9ICdqcC1IZWxwJztcblxuLyoqXG4gKiBBZGQgYSBjb21tYW5kIHRvIHNob3cgYW4gQWJvdXQgZGlhbG9nLlxuICovXG5jb25zdCBhYm91dDogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2hlbHAtZXh0ZW5zaW9uOmFib3V0JyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICByZXF1aXJlczogW0lUcmFuc2xhdG9yXSxcbiAgb3B0aW9uYWw6IFtJQ29tbWFuZFBhbGV0dGVdLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICAgIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSB8IG51bGxcbiAgKTogdm9pZCA9PiB7XG4gICAgY29uc3QgeyBjb21tYW5kcyB9ID0gYXBwO1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgY29uc3QgY2F0ZWdvcnkgPSB0cmFucy5fXygnSGVscCcpO1xuXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmFib3V0LCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ0Fib3V0ICUxJywgYXBwLm5hbWUpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICAvLyBDcmVhdGUgdGhlIGhlYWRlciBvZiB0aGUgYWJvdXQgZGlhbG9nXG4gICAgICAgIGNvbnN0IHZlcnNpb25OdW1iZXIgPSB0cmFucy5fXygnVmVyc2lvbiAlMScsIGFwcC52ZXJzaW9uKTtcbiAgICAgICAgY29uc3QgdmVyc2lvbkluZm8gPSAoXG4gICAgICAgICAgPHNwYW4gY2xhc3NOYW1lPVwianAtQWJvdXQtdmVyc2lvbi1pbmZvXCI+XG4gICAgICAgICAgICA8c3BhbiBjbGFzc05hbWU9XCJqcC1BYm91dC12ZXJzaW9uXCI+e3ZlcnNpb25OdW1iZXJ9PC9zcGFuPlxuICAgICAgICAgIDwvc3Bhbj5cbiAgICAgICAgKTtcbiAgICAgICAgY29uc3QgdGl0bGUgPSAoXG4gICAgICAgICAgPHNwYW4gY2xhc3NOYW1lPVwianAtQWJvdXQtaGVhZGVyXCI+XG4gICAgICAgICAgICA8anVweXRlckljb24ucmVhY3QgbWFyZ2luPVwiN3B4IDkuNXB4XCIgaGVpZ2h0PVwiYXV0b1wiIHdpZHRoPVwiNThweFwiIC8+XG4gICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImpwLUFib3V0LWhlYWRlci1pbmZvXCI+XG4gICAgICAgICAgICAgIDxqdXB5dGVybGFiV29yZG1hcmtJY29uLnJlYWN0IGhlaWdodD1cImF1dG9cIiB3aWR0aD1cIjE5NnB4XCIgLz5cbiAgICAgICAgICAgICAge3ZlcnNpb25JbmZvfVxuICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgPC9zcGFuPlxuICAgICAgICApO1xuXG4gICAgICAgIC8vIENyZWF0ZSB0aGUgYm9keSBvZiB0aGUgYWJvdXQgZGlhbG9nXG4gICAgICAgIGNvbnN0IGp1cHl0ZXJVUkwgPSAnaHR0cHM6Ly9qdXB5dGVyLm9yZy9hYm91dC5odG1sJztcbiAgICAgICAgY29uc3QgY29udHJpYnV0b3JzVVJMID1cbiAgICAgICAgICAnaHR0cHM6Ly9naXRodWIuY29tL2p1cHl0ZXJsYWIvanVweXRlcmxhYi9ncmFwaHMvY29udHJpYnV0b3JzJztcbiAgICAgICAgY29uc3QgZXh0ZXJuYWxMaW5rcyA9IChcbiAgICAgICAgICA8c3BhbiBjbGFzc05hbWU9XCJqcC1BYm91dC1leHRlcm5hbExpbmtzXCI+XG4gICAgICAgICAgICA8YVxuICAgICAgICAgICAgICBocmVmPXtjb250cmlidXRvcnNVUkx9XG4gICAgICAgICAgICAgIHRhcmdldD1cIl9ibGFua1wiXG4gICAgICAgICAgICAgIHJlbD1cIm5vb3BlbmVyIG5vcmVmZXJyZXJcIlxuICAgICAgICAgICAgICBjbGFzc05hbWU9XCJqcC1CdXR0b24tZmxhdFwiXG4gICAgICAgICAgICA+XG4gICAgICAgICAgICAgIHt0cmFucy5fXygnQ09OVFJJQlVUT1IgTElTVCcpfVxuICAgICAgICAgICAgPC9hPlxuICAgICAgICAgICAgPGFcbiAgICAgICAgICAgICAgaHJlZj17anVweXRlclVSTH1cbiAgICAgICAgICAgICAgdGFyZ2V0PVwiX2JsYW5rXCJcbiAgICAgICAgICAgICAgcmVsPVwibm9vcGVuZXIgbm9yZWZlcnJlclwiXG4gICAgICAgICAgICAgIGNsYXNzTmFtZT1cImpwLUJ1dHRvbi1mbGF0XCJcbiAgICAgICAgICAgID5cbiAgICAgICAgICAgICAge3RyYW5zLl9fKCdBQk9VVCBQUk9KRUNUIEpVUFlURVInKX1cbiAgICAgICAgICAgIDwvYT5cbiAgICAgICAgICA8L3NwYW4+XG4gICAgICAgICk7XG4gICAgICAgIGNvbnN0IGNvcHlyaWdodCA9IChcbiAgICAgICAgICA8c3BhbiBjbGFzc05hbWU9XCJqcC1BYm91dC1jb3B5cmlnaHRcIj5cbiAgICAgICAgICAgIHt0cmFucy5fXygnwqkgMjAxNS0yMDIyIFByb2plY3QgSnVweXRlciBDb250cmlidXRvcnMnKX1cbiAgICAgICAgICA8L3NwYW4+XG4gICAgICAgICk7XG4gICAgICAgIGNvbnN0IGJvZHkgPSAoXG4gICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJqcC1BYm91dC1ib2R5XCI+XG4gICAgICAgICAgICB7ZXh0ZXJuYWxMaW5rc31cbiAgICAgICAgICAgIHtjb3B5cmlnaHR9XG4gICAgICAgICAgPC9kaXY+XG4gICAgICAgICk7XG5cbiAgICAgICAgcmV0dXJuIHNob3dEaWFsb2coe1xuICAgICAgICAgIHRpdGxlLFxuICAgICAgICAgIGJvZHksXG4gICAgICAgICAgYnV0dG9uczogW1xuICAgICAgICAgICAgRGlhbG9nLmNyZWF0ZUJ1dHRvbih7XG4gICAgICAgICAgICAgIGxhYmVsOiB0cmFucy5fXygnRGlzbWlzcycpLFxuICAgICAgICAgICAgICBjbGFzc05hbWU6ICdqcC1BYm91dC1idXR0b24ganAtbW9kLXJlamVjdCBqcC1tb2Qtc3R5bGVkJ1xuICAgICAgICAgICAgfSlcbiAgICAgICAgICBdXG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgaWYgKHBhbGV0dGUpIHtcbiAgICAgIHBhbGV0dGUuYWRkSXRlbSh7IGNvbW1hbmQ6IENvbW1hbmRJRHMuYWJvdXQsIGNhdGVnb3J5IH0pO1xuICAgIH1cbiAgfVxufTtcblxuLyoqXG4gKiBBIHBsdWdpbiB0byBhZGQgYSBjb21tYW5kIHRvIG9wZW4gdGhlIEp1cHl0ZXIgRm9ydW0uXG4gKi9cbmNvbnN0IGp1cHl0ZXJGb3J1bTogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2hlbHAtZXh0ZW5zaW9uOmp1cHl0ZXItZm9ydW0nLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHJlcXVpcmVzOiBbSVRyYW5zbGF0b3JdLFxuICBvcHRpb25hbDogW0lDb21tYW5kUGFsZXR0ZV0sXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gICAgcGFsZXR0ZTogSUNvbW1hbmRQYWxldHRlIHwgbnVsbFxuICApOiB2b2lkID0+IHtcbiAgICBjb25zdCB7IGNvbW1hbmRzIH0gPSBhcHA7XG4gICAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICBjb25zdCBjYXRlZ29yeSA9IHRyYW5zLl9fKCdIZWxwJyk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuanVweXRlckZvcnVtLCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ0p1cHl0ZXIgRm9ydW0nKSxcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgd2luZG93Lm9wZW4oJ2h0dHBzOi8vZGlzY291cnNlLmp1cHl0ZXIub3JnL2MvanVweXRlcmxhYicpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgaWYgKHBhbGV0dGUpIHtcbiAgICAgIHBhbGV0dGUuYWRkSXRlbSh7IGNvbW1hbmQ6IENvbW1hbmRJRHMuanVweXRlckZvcnVtLCBjYXRlZ29yeSB9KTtcbiAgICB9XG4gIH1cbn07XG5cbi8qKlxuICogQSBwbHVnaW4gdG8gYWRkIGEgbGlzdCBvZiByZXNvdXJjZXMgdG8gdGhlIGhlbHAgbWVudS5cbiAqL1xuY29uc3QgcmVzb3VyY2VzOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvaGVscC1leHRlbnNpb246cmVzb3VyY2VzJyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICByZXF1aXJlczogW0lNYWluTWVudSwgSVRyYW5zbGF0b3JdLFxuICBvcHRpb25hbDogW0lMYWJTaGVsbCwgSUNvbW1hbmRQYWxldHRlLCBJTGF5b3V0UmVzdG9yZXJdLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIG1haW5NZW51OiBJTWFpbk1lbnUsXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gICAgbGFiU2hlbGw6IElMYWJTaGVsbCB8IG51bGwsXG4gICAgcGFsZXR0ZTogSUNvbW1hbmRQYWxldHRlIHwgbnVsbCxcbiAgICByZXN0b3JlcjogSUxheW91dFJlc3RvcmVyIHwgbnVsbFxuICApOiB2b2lkID0+IHtcbiAgICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGxldCBjb3VudGVyID0gMDtcbiAgICBjb25zdCBjYXRlZ29yeSA9IHRyYW5zLl9fKCdIZWxwJyk7XG4gICAgY29uc3QgbmFtZXNwYWNlID0gJ2hlbHAtZG9jJztcbiAgICBjb25zdCB7IGNvbW1hbmRzLCBzaGVsbCwgc2VydmljZU1hbmFnZXIgfSA9IGFwcDtcbiAgICBjb25zdCB0cmFja2VyID0gbmV3IFdpZGdldFRyYWNrZXI8TWFpbkFyZWFXaWRnZXQ8SUZyYW1lPj4oeyBuYW1lc3BhY2UgfSk7XG4gICAgY29uc3QgcmVzb3VyY2VzID0gW1xuICAgICAge1xuICAgICAgICB0ZXh0OiB0cmFucy5fXygnSnVweXRlckxhYiBSZWZlcmVuY2UnKSxcbiAgICAgICAgdXJsOiAnaHR0cHM6Ly9qdXB5dGVybGFiLnJlYWR0aGVkb2NzLmlvL2VuL2xhdGVzdC8nXG4gICAgICB9LFxuICAgICAge1xuICAgICAgICB0ZXh0OiB0cmFucy5fXygnSnVweXRlckxhYiBGQVEnKSxcbiAgICAgICAgdXJsOiAnaHR0cHM6Ly9qdXB5dGVybGFiLnJlYWR0aGVkb2NzLmlvL2VuL2xhdGVzdC9nZXR0aW5nX3N0YXJ0ZWQvZmFxLmh0bWwnXG4gICAgICB9LFxuICAgICAge1xuICAgICAgICB0ZXh0OiB0cmFucy5fXygnSnVweXRlciBSZWZlcmVuY2UnKSxcbiAgICAgICAgdXJsOiAnaHR0cHM6Ly9qdXB5dGVyLm9yZy9kb2N1bWVudGF0aW9uJ1xuICAgICAgfSxcbiAgICAgIHtcbiAgICAgICAgdGV4dDogdHJhbnMuX18oJ01hcmtkb3duIFJlZmVyZW5jZScpLFxuICAgICAgICB1cmw6ICdodHRwczovL2NvbW1vbm1hcmsub3JnL2hlbHAvJ1xuICAgICAgfVxuICAgIF07XG5cbiAgICByZXNvdXJjZXMuc29ydCgoYTogYW55LCBiOiBhbnkpID0+IHtcbiAgICAgIHJldHVybiBhLnRleHQubG9jYWxlQ29tcGFyZShiLnRleHQpO1xuICAgIH0pO1xuXG4gICAgLyoqXG4gICAgICogQ3JlYXRlIGEgbmV3IEhlbHBXaWRnZXQgd2lkZ2V0LlxuICAgICAqL1xuICAgIGZ1bmN0aW9uIG5ld0hlbHBXaWRnZXQodXJsOiBzdHJpbmcsIHRleHQ6IHN0cmluZyk6IE1haW5BcmVhV2lkZ2V0PElGcmFtZT4ge1xuICAgICAgLy8gQWxsb3cgc2NyaXB0cyBhbmQgZm9ybXMgc28gdGhhdCB0aGluZ3MgbGlrZVxuICAgICAgLy8gcmVhZHRoZWRvY3MgY2FuIHVzZSB0aGVpciBzZWFyY2ggZnVuY3Rpb25hbGl0eS5cbiAgICAgIC8vIFdlICpkb24ndCogYWxsb3cgc2FtZSBvcmlnaW4gcmVxdWVzdHMsIHdoaWNoXG4gICAgICAvLyBjYW4gcHJldmVudCBzb21lIGNvbnRlbnQgZnJvbSBiZWluZyBsb2FkZWQgb250byB0aGVcbiAgICAgIC8vIGhlbHAgcGFnZXMuXG4gICAgICBjb25zdCBjb250ZW50ID0gbmV3IElGcmFtZSh7XG4gICAgICAgIHNhbmRib3g6IFsnYWxsb3ctc2NyaXB0cycsICdhbGxvdy1mb3JtcyddXG4gICAgICB9KTtcbiAgICAgIGNvbnRlbnQudXJsID0gdXJsO1xuICAgICAgY29udGVudC5hZGRDbGFzcyhIRUxQX0NMQVNTKTtcbiAgICAgIGNvbnRlbnQudGl0bGUubGFiZWwgPSB0ZXh0O1xuICAgICAgY29udGVudC5pZCA9IGAke25hbWVzcGFjZX0tJHsrK2NvdW50ZXJ9YDtcbiAgICAgIGNvbnN0IHdpZGdldCA9IG5ldyBNYWluQXJlYVdpZGdldCh7IGNvbnRlbnQgfSk7XG4gICAgICB3aWRnZXQuYWRkQ2xhc3MoJ2pwLUhlbHAnKTtcbiAgICAgIHJldHVybiB3aWRnZXQ7XG4gICAgfVxuXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLm9wZW4sIHtcbiAgICAgIGxhYmVsOiBhcmdzID0+XG4gICAgICAgIChhcmdzWyd0ZXh0J10gYXMgc3RyaW5nKSA/P1xuICAgICAgICB0cmFucy5fXygnT3BlbiB0aGUgcHJvdmlkZWQgYHVybGAgaW4gYSB0YWIuJyksXG4gICAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgICAgY29uc3QgdXJsID0gYXJnc1sndXJsJ10gYXMgc3RyaW5nO1xuICAgICAgICBjb25zdCB0ZXh0ID0gYXJnc1sndGV4dCddIGFzIHN0cmluZztcbiAgICAgICAgY29uc3QgbmV3QnJvd3NlclRhYiA9IChhcmdzWyduZXdCcm93c2VyVGFiJ10gYXMgYm9vbGVhbikgfHwgZmFsc2U7XG5cbiAgICAgICAgLy8gSWYgaGVscCByZXNvdXJjZSB3aWxsIGdlbmVyYXRlIGEgbWl4ZWQgY29udGVudCBlcnJvciwgbG9hZCBleHRlcm5hbGx5LlxuICAgICAgICBpZiAoXG4gICAgICAgICAgbmV3QnJvd3NlclRhYiB8fFxuICAgICAgICAgIChMQUJfSVNfU0VDVVJFICYmIFVSTEV4dC5wYXJzZSh1cmwpLnByb3RvY29sICE9PSAnaHR0cHM6JylcbiAgICAgICAgKSB7XG4gICAgICAgICAgd2luZG93Lm9wZW4odXJsKTtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cblxuICAgICAgICBjb25zdCB3aWRnZXQgPSBuZXdIZWxwV2lkZ2V0KHVybCwgdGV4dCk7XG4gICAgICAgIHZvaWQgdHJhY2tlci5hZGQod2lkZ2V0KTtcbiAgICAgICAgc2hlbGwuYWRkKHdpZGdldCwgJ21haW4nKTtcbiAgICAgICAgcmV0dXJuIHdpZGdldDtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIC8vIEhhbmRsZSBzdGF0ZSByZXN0b3JhdGlvbi5cbiAgICBpZiAocmVzdG9yZXIpIHtcbiAgICAgIHZvaWQgcmVzdG9yZXIucmVzdG9yZSh0cmFja2VyLCB7XG4gICAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMub3BlbixcbiAgICAgICAgYXJnczogd2lkZ2V0ID0+ICh7XG4gICAgICAgICAgdXJsOiB3aWRnZXQuY29udGVudC51cmwsXG4gICAgICAgICAgdGV4dDogd2lkZ2V0LmNvbnRlbnQudGl0bGUubGFiZWxcbiAgICAgICAgfSksXG4gICAgICAgIG5hbWU6IHdpZGdldCA9PiB3aWRnZXQuY29udGVudC51cmxcbiAgICAgIH0pO1xuICAgIH1cblxuICAgIC8vIFBvcHVsYXRlIHRoZSBIZWxwIG1lbnUuXG4gICAgY29uc3QgaGVscE1lbnUgPSBtYWluTWVudS5oZWxwTWVudTtcblxuICAgIGNvbnN0IHJlc291cmNlc0dyb3VwID0gcmVzb3VyY2VzLm1hcChhcmdzID0+ICh7XG4gICAgICBhcmdzLFxuICAgICAgY29tbWFuZDogQ29tbWFuZElEcy5vcGVuXG4gICAgfSkpO1xuICAgIGhlbHBNZW51LmFkZEdyb3VwKHJlc291cmNlc0dyb3VwLCAxMCk7XG5cbiAgICAvLyBHZW5lcmF0ZSBhIGNhY2hlIG9mIHRoZSBrZXJuZWwgaGVscCBsaW5rcy5cbiAgICBjb25zdCBrZXJuZWxJbmZvQ2FjaGUgPSBuZXcgTWFwPFxuICAgICAgc3RyaW5nLFxuICAgICAgS2VybmVsTWVzc2FnZS5JSW5mb1JlcGx5TXNnWydjb250ZW50J11cbiAgICA+KCk7XG5cbiAgICBjb25zdCBvblNlc3Npb25SdW5uaW5nQ2hhbmdlZCA9IChcbiAgICAgIG06IFNlc3Npb24uSU1hbmFnZXIsXG4gICAgICBzZXNzaW9uczogU2Vzc2lvbi5JTW9kZWxbXVxuICAgICkgPT4ge1xuICAgICAgLy8gSWYgYSBuZXcgc2Vzc2lvbiBoYXMgYmVlbiBhZGRlZCwgaXQgaXMgYXQgdGhlIGJhY2tcbiAgICAgIC8vIG9mIHRoZSBzZXNzaW9uIGxpc3QuIElmIG9uZSBoYXMgY2hhbmdlZCBvciBzdG9wcGVkLFxuICAgICAgLy8gaXQgZG9lcyBub3QgaHVydCB0byBjaGVjayBpdC5cbiAgICAgIGlmICghc2Vzc2lvbnMubGVuZ3RoKSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGNvbnN0IHNlc3Npb25Nb2RlbCA9IHNlc3Npb25zW3Nlc3Npb25zLmxlbmd0aCAtIDFdO1xuICAgICAgaWYgKFxuICAgICAgICAhc2Vzc2lvbk1vZGVsLmtlcm5lbCB8fFxuICAgICAgICBrZXJuZWxJbmZvQ2FjaGUuaGFzKHNlc3Npb25Nb2RlbC5rZXJuZWwubmFtZSlcbiAgICAgICkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICBjb25zdCBzZXNzaW9uID0gc2VydmljZU1hbmFnZXIuc2Vzc2lvbnMuY29ubmVjdFRvKHtcbiAgICAgICAgbW9kZWw6IHNlc3Npb25Nb2RlbCxcbiAgICAgICAga2VybmVsQ29ubmVjdGlvbk9wdGlvbnM6IHsgaGFuZGxlQ29tbXM6IGZhbHNlIH1cbiAgICAgIH0pO1xuXG4gICAgICB2b2lkIHNlc3Npb24ua2VybmVsPy5pbmZvXG4gICAgICAgIC50aGVuKGtlcm5lbEluZm8gPT4ge1xuICAgICAgICAgIGNvbnN0IG5hbWUgPSBzZXNzaW9uLmtlcm5lbCEubmFtZTtcblxuICAgICAgICAgIC8vIENoZWNrIHRoZSBjYWNoZSBzZWNvbmQgdGltZSBzbyB0aGF0LCBpZiB0d28gY2FsbGJhY2tzIGdldCBzY2hlZHVsZWQsXG4gICAgICAgICAgLy8gdGhleSBkb24ndCB0cnkgdG8gYWRkIHRoZSBzYW1lIGNvbW1hbmRzLlxuICAgICAgICAgIGlmIChrZXJuZWxJbmZvQ2FjaGUuaGFzKG5hbWUpKSB7XG4gICAgICAgICAgICByZXR1cm47XG4gICAgICAgICAgfVxuXG4gICAgICAgICAgY29uc3Qgc3BlYyA9IHNlcnZpY2VNYW5hZ2VyLmtlcm5lbHNwZWNzPy5zcGVjcz8ua2VybmVsc3BlY3NbbmFtZV07XG4gICAgICAgICAgaWYgKCFzcGVjKSB7XG4gICAgICAgICAgICByZXR1cm47XG4gICAgICAgICAgfVxuXG4gICAgICAgICAgLy8gU2V0IHRoZSBLZXJuZWwgSW5mbyBjYWNoZS5cbiAgICAgICAgICBrZXJuZWxJbmZvQ2FjaGUuc2V0KG5hbWUsIGtlcm5lbEluZm8pO1xuXG4gICAgICAgICAgLy8gVXRpbGl0eSBmdW5jdGlvbiB0byBjaGVjayBpZiB0aGUgY3VycmVudCB3aWRnZXRcbiAgICAgICAgICAvLyBoYXMgcmVnaXN0ZXJlZCBpdHNlbGYgd2l0aCB0aGUgaGVscCBtZW51LlxuICAgICAgICAgIGxldCB1c2VzS2VybmVsID0gZmFsc2U7XG4gICAgICAgICAgY29uc3Qgb25DdXJyZW50Q2hhbmdlZCA9IGFzeW5jICgpID0+IHtcbiAgICAgICAgICAgIGNvbnN0IGtlcm5lbDogS2VybmVsLklLZXJuZWxDb25uZWN0aW9uIHwgbnVsbCA9XG4gICAgICAgICAgICAgIGF3YWl0IGNvbW1hbmRzLmV4ZWN1dGUoJ2hlbHBtZW51OmdldC1rZXJuZWwnKTtcbiAgICAgICAgICAgIHVzZXNLZXJuZWwgPSBrZXJuZWw/Lm5hbWUgPT09IG5hbWU7XG4gICAgICAgICAgfTtcbiAgICAgICAgICAvLyBTZXQgdGhlIHN0YXR1cyBmb3IgdGhlIGN1cnJlbnQgd2lkZ2V0XG4gICAgICAgICAgb25DdXJyZW50Q2hhbmdlZCgpLmNhdGNoKGVycm9yID0+IHtcbiAgICAgICAgICAgIGNvbnNvbGUuZXJyb3IoXG4gICAgICAgICAgICAgICdGYWlsZWQgdG8gZ2V0IHRoZSBrZXJuZWwgZm9yIHRoZSBjdXJyZW50IHdpZGdldC4nLFxuICAgICAgICAgICAgICBlcnJvclxuICAgICAgICAgICAgKTtcbiAgICAgICAgICB9KTtcbiAgICAgICAgICBpZiAobGFiU2hlbGwpIHtcbiAgICAgICAgICAgIC8vIFVwZGF0ZSBzdGF0dXMgd2hlbiBjdXJyZW50IHdpZGdldCBjaGFuZ2VzXG4gICAgICAgICAgICBsYWJTaGVsbC5jdXJyZW50Q2hhbmdlZC5jb25uZWN0KG9uQ3VycmVudENoYW5nZWQpO1xuICAgICAgICAgIH1cbiAgICAgICAgICBjb25zdCBpc0VuYWJsZWQgPSAoKSA9PiB1c2VzS2VybmVsO1xuXG4gICAgICAgICAgLy8gQWRkIHRoZSBrZXJuZWwgYmFubmVyIHRvIHRoZSBIZWxwIE1lbnUuXG4gICAgICAgICAgY29uc3QgYmFubmVyQ29tbWFuZCA9IGBoZWxwLW1lbnUtJHtuYW1lfTpiYW5uZXJgO1xuICAgICAgICAgIGNvbnN0IGtlcm5lbE5hbWUgPSBzcGVjLmRpc3BsYXlfbmFtZTtcbiAgICAgICAgICBsZXQga2VybmVsSWNvblVybCA9IHNwZWMucmVzb3VyY2VzWydsb2dvLTY0eDY0J107XG4gICAgICAgICAgY29tbWFuZHMuYWRkQ29tbWFuZChiYW5uZXJDb21tYW5kLCB7XG4gICAgICAgICAgICBsYWJlbDogdHJhbnMuX18oJ0Fib3V0IHRoZSAlMSBLZXJuZWwnLCBrZXJuZWxOYW1lKSxcbiAgICAgICAgICAgIGlzVmlzaWJsZTogaXNFbmFibGVkLFxuICAgICAgICAgICAgaXNFbmFibGVkLFxuICAgICAgICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICAgICAgICAvLyBDcmVhdGUgdGhlIGhlYWRlciBvZiB0aGUgYWJvdXQgZGlhbG9nXG4gICAgICAgICAgICAgIGNvbnN0IGhlYWRlckxvZ28gPSA8aW1nIHNyYz17a2VybmVsSWNvblVybH0gLz47XG4gICAgICAgICAgICAgIGNvbnN0IHRpdGxlID0gKFxuICAgICAgICAgICAgICAgIDxzcGFuIGNsYXNzTmFtZT1cImpwLUFib3V0LWhlYWRlclwiPlxuICAgICAgICAgICAgICAgICAge2hlYWRlckxvZ299XG4gICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImpwLUFib3V0LWhlYWRlci1pbmZvXCI+e2tlcm5lbE5hbWV9PC9kaXY+XG4gICAgICAgICAgICAgICAgPC9zcGFuPlxuICAgICAgICAgICAgICApO1xuICAgICAgICAgICAgICBjb25zdCBiYW5uZXIgPSA8cHJlPntrZXJuZWxJbmZvLmJhbm5lcn08L3ByZT47XG4gICAgICAgICAgICAgIGNvbnN0IGJvZHkgPSA8ZGl2IGNsYXNzTmFtZT1cImpwLUFib3V0LWJvZHlcIj57YmFubmVyfTwvZGl2PjtcblxuICAgICAgICAgICAgICByZXR1cm4gc2hvd0RpYWxvZyh7XG4gICAgICAgICAgICAgICAgdGl0bGUsXG4gICAgICAgICAgICAgICAgYm9keSxcbiAgICAgICAgICAgICAgICBidXR0b25zOiBbXG4gICAgICAgICAgICAgICAgICBEaWFsb2cuY3JlYXRlQnV0dG9uKHtcbiAgICAgICAgICAgICAgICAgICAgbGFiZWw6IHRyYW5zLl9fKCdEaXNtaXNzJyksXG4gICAgICAgICAgICAgICAgICAgIGNsYXNzTmFtZTogJ2pwLUFib3V0LWJ1dHRvbiBqcC1tb2QtcmVqZWN0IGpwLW1vZC1zdHlsZWQnXG4gICAgICAgICAgICAgICAgICB9KVxuICAgICAgICAgICAgICAgIF1cbiAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgfSk7XG4gICAgICAgICAgaGVscE1lbnUuYWRkR3JvdXAoW3sgY29tbWFuZDogYmFubmVyQ29tbWFuZCB9XSwgMjApO1xuXG4gICAgICAgICAgLy8gQWRkIHRoZSBrZXJuZWwgaW5mbyBoZWxwX2xpbmtzIHRvIHRoZSBIZWxwIG1lbnUuXG4gICAgICAgICAgY29uc3Qga2VybmVsR3JvdXA6IE1lbnUuSUl0ZW1PcHRpb25zW10gPSBbXTtcbiAgICAgICAgICAoa2VybmVsSW5mby5oZWxwX2xpbmtzIHx8IFtdKS5mb3JFYWNoKGxpbmsgPT4ge1xuICAgICAgICAgICAgY29uc3QgY29tbWFuZElkID0gYGhlbHAtbWVudS0ke25hbWV9OiR7bGluay50ZXh0fWA7XG4gICAgICAgICAgICBjb21tYW5kcy5hZGRDb21tYW5kKGNvbW1hbmRJZCwge1xuICAgICAgICAgICAgICBsYWJlbDogY29tbWFuZHMubGFiZWwoQ29tbWFuZElEcy5vcGVuLCBsaW5rKSxcbiAgICAgICAgICAgICAgaXNWaXNpYmxlOiBpc0VuYWJsZWQsXG4gICAgICAgICAgICAgIGlzRW5hYmxlZCxcbiAgICAgICAgICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICAgICAgICAgIHJldHVybiBjb21tYW5kcy5leGVjdXRlKENvbW1hbmRJRHMub3BlbiwgbGluayk7XG4gICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAga2VybmVsR3JvdXAucHVzaCh7IGNvbW1hbmQ6IGNvbW1hbmRJZCB9KTtcbiAgICAgICAgICB9KTtcbiAgICAgICAgICBoZWxwTWVudS5hZGRHcm91cChrZXJuZWxHcm91cCwgMjEpO1xuICAgICAgICB9KVxuICAgICAgICAudGhlbigoKSA9PiB7XG4gICAgICAgICAgLy8gRGlzcG9zZSBvZiB0aGUgc2Vzc2lvbiBvYmplY3Qgc2luY2Ugd2Ugbm8gbG9uZ2VyIG5lZWQgaXQuXG4gICAgICAgICAgc2Vzc2lvbi5kaXNwb3NlKCk7XG4gICAgICAgIH0pO1xuICAgIH07XG5cbiAgICAvLyBDcmVhdGUgbWVudSBpdGVtcyBmb3IgY3VycmVudGx5IHJ1bm5pbmcgc2Vzc2lvbnNcbiAgICBlYWNoKHNlcnZpY2VNYW5hZ2VyLnNlc3Npb25zLnJ1bm5pbmcoKSwgbW9kZWwgPT4ge1xuICAgICAgb25TZXNzaW9uUnVubmluZ0NoYW5nZWQoc2VydmljZU1hbmFnZXIuc2Vzc2lvbnMsIFttb2RlbF0pO1xuICAgIH0pO1xuICAgIHNlcnZpY2VNYW5hZ2VyLnNlc3Npb25zLnJ1bm5pbmdDaGFuZ2VkLmNvbm5lY3Qob25TZXNzaW9uUnVubmluZ0NoYW5nZWQpO1xuXG4gICAgaWYgKHBhbGV0dGUpIHtcbiAgICAgIHJlc291cmNlcy5mb3JFYWNoKGFyZ3MgPT4ge1xuICAgICAgICBwYWxldHRlLmFkZEl0ZW0oeyBhcmdzLCBjb21tYW5kOiBDb21tYW5kSURzLm9wZW4sIGNhdGVnb3J5IH0pO1xuICAgICAgfSk7XG4gICAgICBwYWxldHRlLmFkZEl0ZW0oe1xuICAgICAgICBhcmdzOiB7IHJlbG9hZDogdHJ1ZSB9LFxuICAgICAgICBjb21tYW5kOiAnYXBwdXRpbHM6cmVzZXQnLFxuICAgICAgICBjYXRlZ29yeVxuICAgICAgfSk7XG4gICAgfVxuICB9XG59O1xuXG4vKipcbiAqIEEgcGx1Z2luIHRvIGFkZCBhIGxpY2Vuc2VzIHJlcG9ydGluZyB0b29scy5cbiAqL1xuY29uc3QgbGljZW5zZXM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9oZWxwLWV4dGVuc2lvbjpsaWNlbnNlcycsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcmVxdWlyZXM6IFtJVHJhbnNsYXRvcl0sXG4gIG9wdGlvbmFsOiBbSU1haW5NZW51LCBJQ29tbWFuZFBhbGV0dGUsIElMYXlvdXRSZXN0b3Jlcl0sXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gICAgbWVudTogSU1haW5NZW51IHwgbnVsbCxcbiAgICBwYWxldHRlOiBJQ29tbWFuZFBhbGV0dGUgfCBudWxsLFxuICAgIHJlc3RvcmVyOiBJTGF5b3V0UmVzdG9yZXIgfCBudWxsXG4gICkgPT4ge1xuICAgIC8vIGJhaWwgaWYgbm8gbGljZW5zZSBBUEkgaXMgYXZhaWxhYmxlIGZyb20gdGhlIHNlcnZlclxuICAgIGlmICghUGFnZUNvbmZpZy5nZXRPcHRpb24oJ2xpY2Vuc2VzVXJsJykpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICBjb25zdCB7IGNvbW1hbmRzLCBzaGVsbCB9ID0gYXBwO1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG5cbiAgICAvLyB0cmFuc2xhdGlvbiBzdHJpbmdzXG4gICAgY29uc3QgY2F0ZWdvcnkgPSB0cmFucy5fXygnSGVscCcpO1xuICAgIGNvbnN0IGRvd25sb2FkQXNUZXh0ID0gdHJhbnMuX18oJ0Rvd25sb2FkIEFsbCBMaWNlbnNlcyBhcycpO1xuICAgIGNvbnN0IGxpY2Vuc2VzVGV4dCA9IHRyYW5zLl9fKCdMaWNlbnNlcycpO1xuICAgIGNvbnN0IHJlZnJlc2hMaWNlbnNlcyA9IHRyYW5zLl9fKCdSZWZyZXNoIExpY2Vuc2VzJyk7XG5cbiAgICAvLyBhbiBpbmNyZW1lbnRlciBmb3IgbGljZW5zZSB3aWRnZXQgaWRzXG4gICAgbGV0IGNvdW50ZXIgPSAwO1xuXG4gICAgY29uc3QgbGljZW5zZXNVcmwgPVxuICAgICAgVVJMRXh0LmpvaW4oXG4gICAgICAgIFBhZ2VDb25maWcuZ2V0QmFzZVVybCgpLFxuICAgICAgICBQYWdlQ29uZmlnLmdldE9wdGlvbignbGljZW5zZXNVcmwnKVxuICAgICAgKSArICcvJztcblxuICAgIGNvbnN0IGxpY2Vuc2VzTmFtZXNwYWNlID0gJ2hlbHAtbGljZW5zZXMnO1xuICAgIGNvbnN0IGxpY2Vuc2VzVHJhY2tlciA9IG5ldyBXaWRnZXRUcmFja2VyPE1haW5BcmVhV2lkZ2V0PExpY2Vuc2VzPj4oe1xuICAgICAgbmFtZXNwYWNlOiBsaWNlbnNlc05hbWVzcGFjZVxuICAgIH0pO1xuXG4gICAgLyoqXG4gICAgICogUmV0dXJuIGEgZnVsbCBsaWNlbnNlIHJlcG9ydCBmb3JtYXQgYmFzZWQgb24gYSBmb3JtYXQgbmFtZVxuICAgICAqL1xuICAgIGZ1bmN0aW9uIGZvcm1hdE9yRGVmYXVsdChmb3JtYXQ6IHN0cmluZyk6IExpY2Vuc2VzLklSZXBvcnRGb3JtYXQge1xuICAgICAgcmV0dXJuIChcbiAgICAgICAgTGljZW5zZXMuUkVQT1JUX0ZPUk1BVFNbZm9ybWF0XSB8fFxuICAgICAgICBMaWNlbnNlcy5SRVBPUlRfRk9STUFUU1tMaWNlbnNlcy5ERUZBVUxUX0ZPUk1BVF1cbiAgICAgICk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogQ3JlYXRlIGEgTWFpbkFyZWFXaWRnZXQgZm9yIGEgbGljZW5zZSB2aWV3ZXJcbiAgICAgKi9cbiAgICBmdW5jdGlvbiBjcmVhdGVMaWNlbnNlV2lkZ2V0KGFyZ3M6IExpY2Vuc2VzLklDcmVhdGVBcmdzKSB7XG4gICAgICBjb25zdCBsaWNlbnNlc01vZGVsID0gbmV3IExpY2Vuc2VzLk1vZGVsKHtcbiAgICAgICAgLi4uYXJncyxcbiAgICAgICAgbGljZW5zZXNVcmwsXG4gICAgICAgIHRyYW5zLFxuICAgICAgICBzZXJ2ZXJTZXR0aW5nczogYXBwLnNlcnZpY2VNYW5hZ2VyLnNlcnZlclNldHRpbmdzXG4gICAgICB9KTtcbiAgICAgIGNvbnN0IGNvbnRlbnQgPSBuZXcgTGljZW5zZXMoeyBtb2RlbDogbGljZW5zZXNNb2RlbCB9KTtcbiAgICAgIGNvbnRlbnQuaWQgPSBgJHtsaWNlbnNlc05hbWVzcGFjZX0tJHsrK2NvdW50ZXJ9YDtcbiAgICAgIGNvbnRlbnQudGl0bGUubGFiZWwgPSBsaWNlbnNlc1RleHQ7XG4gICAgICBjb250ZW50LnRpdGxlLmljb24gPSBjb3B5cmlnaHRJY29uO1xuICAgICAgY29uc3QgbWFpbiA9IG5ldyBNYWluQXJlYVdpZGdldCh7XG4gICAgICAgIGNvbnRlbnQsXG4gICAgICAgIHJldmVhbDogbGljZW5zZXNNb2RlbC5saWNlbnNlc1JlYWR5XG4gICAgICB9KTtcblxuICAgICAgbWFpbi50b29sYmFyLmFkZEl0ZW0oXG4gICAgICAgICdyZWZyZXNoLWxpY2Vuc2VzJyxcbiAgICAgICAgbmV3IENvbW1hbmRUb29sYmFyQnV0dG9uKHtcbiAgICAgICAgICBpZDogQ29tbWFuZElEcy5yZWZyZXNoTGljZW5zZXMsXG4gICAgICAgICAgYXJnczogeyBub0xhYmVsOiAxIH0sXG4gICAgICAgICAgY29tbWFuZHNcbiAgICAgICAgfSlcbiAgICAgICk7XG5cbiAgICAgIG1haW4udG9vbGJhci5hZGRJdGVtKCdzcGFjZXInLCBUb29sYmFyLmNyZWF0ZVNwYWNlckl0ZW0oKSk7XG5cbiAgICAgIGZvciAoY29uc3QgZm9ybWF0IG9mIE9iamVjdC5rZXlzKExpY2Vuc2VzLlJFUE9SVF9GT1JNQVRTKSkge1xuICAgICAgICBjb25zdCBidXR0b24gPSBuZXcgQ29tbWFuZFRvb2xiYXJCdXR0b24oe1xuICAgICAgICAgIGlkOiBDb21tYW5kSURzLmxpY2Vuc2VSZXBvcnQsXG4gICAgICAgICAgYXJnczogeyBmb3JtYXQsIG5vTGFiZWw6IDEgfSxcbiAgICAgICAgICBjb21tYW5kc1xuICAgICAgICB9KTtcbiAgICAgICAgbWFpbi50b29sYmFyLmFkZEl0ZW0oYGRvd25sb2FkLSR7Zm9ybWF0fWAsIGJ1dHRvbik7XG4gICAgICB9XG5cbiAgICAgIHJldHVybiBtYWluO1xuICAgIH1cblxuICAgIC8vIHJlZ2lzdGVyIGxpY2Vuc2UtcmVsYXRlZCBjb21tYW5kc1xuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5saWNlbnNlcywge1xuICAgICAgbGFiZWw6IGxpY2Vuc2VzVGV4dCxcbiAgICAgIGV4ZWN1dGU6IChhcmdzOiBhbnkpID0+IHtcbiAgICAgICAgY29uc3QgbGljZW5zZU1haW4gPSBjcmVhdGVMaWNlbnNlV2lkZ2V0KGFyZ3MgYXMgTGljZW5zZXMuSUNyZWF0ZUFyZ3MpO1xuICAgICAgICBzaGVsbC5hZGQobGljZW5zZU1haW4sICdtYWluJywgeyB0eXBlOiAnTGljZW5zZXMnIH0pO1xuXG4gICAgICAgIC8vIGFkZCB0byB0cmFja2VyIHNvIGl0IGNhbiBiZSByZXN0b3JlZCwgYW5kIHVwZGF0ZSB3aGVuIGNob2ljZXMgY2hhbmdlXG4gICAgICAgIHZvaWQgbGljZW5zZXNUcmFja2VyLmFkZChsaWNlbnNlTWFpbik7XG4gICAgICAgIGxpY2Vuc2VNYWluLmNvbnRlbnQubW9kZWwudHJhY2tlckRhdGFDaGFuZ2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgICAgIHZvaWQgbGljZW5zZXNUcmFja2VyLnNhdmUobGljZW5zZU1haW4pO1xuICAgICAgICB9KTtcbiAgICAgICAgcmV0dXJuIGxpY2Vuc2VNYWluO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnJlZnJlc2hMaWNlbnNlcywge1xuICAgICAgbGFiZWw6IGFyZ3MgPT4gKGFyZ3Mubm9MYWJlbCA/ICcnIDogcmVmcmVzaExpY2Vuc2VzKSxcbiAgICAgIGNhcHRpb246IHJlZnJlc2hMaWNlbnNlcyxcbiAgICAgIGljb246IHJlZnJlc2hJY29uLFxuICAgICAgZXhlY3V0ZTogYXN5bmMgKCkgPT4ge1xuICAgICAgICByZXR1cm4gbGljZW5zZXNUcmFja2VyLmN1cnJlbnRXaWRnZXQ/LmNvbnRlbnQubW9kZWwuaW5pdExpY2Vuc2VzKCk7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMubGljZW5zZVJlcG9ydCwge1xuICAgICAgbGFiZWw6IGFyZ3MgPT4ge1xuICAgICAgICBpZiAoYXJncy5ub0xhYmVsKSB7XG4gICAgICAgICAgcmV0dXJuICcnO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IGZvcm1hdCA9IGZvcm1hdE9yRGVmYXVsdChgJHthcmdzLmZvcm1hdH1gKTtcbiAgICAgICAgcmV0dXJuIGAke2Rvd25sb2FkQXNUZXh0fSAke2Zvcm1hdC50aXRsZX1gO1xuICAgICAgfSxcbiAgICAgIGNhcHRpb246IGFyZ3MgPT4ge1xuICAgICAgICBjb25zdCBmb3JtYXQgPSBmb3JtYXRPckRlZmF1bHQoYCR7YXJncy5mb3JtYXR9YCk7XG4gICAgICAgIHJldHVybiBgJHtkb3dubG9hZEFzVGV4dH0gJHtmb3JtYXQudGl0bGV9YDtcbiAgICAgIH0sXG4gICAgICBpY29uOiBhcmdzID0+IHtcbiAgICAgICAgY29uc3QgZm9ybWF0ID0gZm9ybWF0T3JEZWZhdWx0KGAke2FyZ3MuZm9ybWF0fWApO1xuICAgICAgICByZXR1cm4gZm9ybWF0Lmljb247XG4gICAgICB9LFxuICAgICAgZXhlY3V0ZTogYXN5bmMgYXJncyA9PiB7XG4gICAgICAgIGNvbnN0IGZvcm1hdCA9IGZvcm1hdE9yRGVmYXVsdChgJHthcmdzLmZvcm1hdH1gKTtcbiAgICAgICAgcmV0dXJuIGF3YWl0IGxpY2Vuc2VzVHJhY2tlci5jdXJyZW50V2lkZ2V0Py5jb250ZW50Lm1vZGVsLmRvd25sb2FkKHtcbiAgICAgICAgICBmb3JtYXQ6IGZvcm1hdC5pZFxuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIC8vIGhhbmRsZSBvcHRpb25hbCBpbnRlZ3JhdGlvbnNcbiAgICBpZiAocGFsZXR0ZSkge1xuICAgICAgcGFsZXR0ZS5hZGRJdGVtKHsgY29tbWFuZDogQ29tbWFuZElEcy5saWNlbnNlcywgY2F0ZWdvcnkgfSk7XG4gICAgfVxuXG4gICAgaWYgKG1lbnUpIHtcbiAgICAgIGNvbnN0IGhlbHBNZW51ID0gbWVudS5oZWxwTWVudTtcbiAgICAgIGhlbHBNZW51LmFkZEdyb3VwKFt7IGNvbW1hbmQ6IENvbW1hbmRJRHMubGljZW5zZXMgfV0sIDApO1xuICAgIH1cblxuICAgIGlmIChyZXN0b3Jlcikge1xuICAgICAgdm9pZCByZXN0b3Jlci5yZXN0b3JlKGxpY2Vuc2VzVHJhY2tlciwge1xuICAgICAgICBjb21tYW5kOiBDb21tYW5kSURzLmxpY2Vuc2VzLFxuICAgICAgICBuYW1lOiB3aWRnZXQgPT4gJ2xpY2Vuc2VzJyxcbiAgICAgICAgYXJnczogd2lkZ2V0ID0+IHtcbiAgICAgICAgICBjb25zdCB7IGN1cnJlbnRCdW5kbGVOYW1lLCBjdXJyZW50UGFja2FnZUluZGV4LCBwYWNrYWdlRmlsdGVyIH0gPVxuICAgICAgICAgICAgd2lkZ2V0LmNvbnRlbnQubW9kZWw7XG5cbiAgICAgICAgICBjb25zdCBhcmdzOiBMaWNlbnNlcy5JQ3JlYXRlQXJncyA9IHtcbiAgICAgICAgICAgIGN1cnJlbnRCdW5kbGVOYW1lLFxuICAgICAgICAgICAgY3VycmVudFBhY2thZ2VJbmRleCxcbiAgICAgICAgICAgIHBhY2thZ2VGaWx0ZXJcbiAgICAgICAgICB9O1xuICAgICAgICAgIHJldHVybiBhcmdzIGFzIFJlYWRvbmx5SlNPTk9iamVjdDtcbiAgICAgICAgfVxuICAgICAgfSk7XG4gICAgfVxuICB9XG59O1xuXG5jb25zdCBwbHVnaW5zOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48YW55PltdID0gW1xuICBhYm91dCxcbiAganVweXRlckZvcnVtLFxuICByZXNvdXJjZXMsXG4gIGxpY2Vuc2VzXG5dO1xuXG5leHBvcnQgZGVmYXVsdCBwbHVnaW5zO1xuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBTZXJ2ZXJDb25uZWN0aW9uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2VydmljZXMnO1xuaW1wb3J0IHsgVHJhbnNsYXRpb25CdW5kbGUgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQge1xuICBqc29uSWNvbixcbiAgTGFiSWNvbixcbiAgbWFya2Rvd25JY29uLFxuICBzcHJlYWRzaGVldEljb24sXG4gIFZEb21Nb2RlbCxcbiAgVkRvbVJlbmRlcmVyXG59IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0IHsgUHJvbWlzZURlbGVnYXRlLCBSZWFkb25seUpTT05PYmplY3QgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBJU2lnbmFsLCBTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBoLCBWaXJ0dWFsRWxlbWVudCB9IGZyb20gJ0BsdW1pbm8vdmlydHVhbGRvbSc7XG5pbXBvcnQgeyBQYW5lbCwgU3BsaXRQYW5lbCwgVGFiQmFyLCBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0ICogYXMgUmVhY3QgZnJvbSAncmVhY3QnO1xuXG4vKipcbiAqIEEgbGljZW5zZSB2aWV3ZXJcbiAqL1xuZXhwb3J0IGNsYXNzIExpY2Vuc2VzIGV4dGVuZHMgU3BsaXRQYW5lbCB7XG4gIHJlYWRvbmx5IG1vZGVsOiBMaWNlbnNlcy5Nb2RlbDtcblxuICBjb25zdHJ1Y3RvcihvcHRpb25zOiBMaWNlbnNlcy5JT3B0aW9ucykge1xuICAgIHN1cGVyKCk7XG4gICAgdGhpcy5hZGRDbGFzcygnanAtTGljZW5zZXMnKTtcbiAgICB0aGlzLm1vZGVsID0gb3B0aW9ucy5tb2RlbDtcbiAgICB0aGlzLmluaXRMZWZ0UGFuZWwoKTtcbiAgICB0aGlzLmluaXRGaWx0ZXJzKCk7XG4gICAgdGhpcy5pbml0QnVuZGxlcygpO1xuICAgIHRoaXMuaW5pdEdyaWQoKTtcbiAgICB0aGlzLmluaXRMaWNlbnNlVGV4dCgpO1xuICAgIHRoaXMuc2V0UmVsYXRpdmVTaXplcyhbMSwgMiwgM10pO1xuICAgIHZvaWQgdGhpcy5tb2RlbC5pbml0TGljZW5zZXMoKS50aGVuKCgpID0+IHRoaXMuX3VwZGF0ZUJ1bmRsZXMoKSk7XG4gICAgdGhpcy5tb2RlbC50cmFja2VyRGF0YUNoYW5nZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICB0aGlzLnRpdGxlLmxhYmVsID0gdGhpcy5tb2RlbC50aXRsZTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgZGlzcG9zaW5nIG9mIHRoZSB3aWRnZXRcbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICB0aGlzLl9idW5kbGVzLmN1cnJlbnRDaGFuZ2VkLmRpc2Nvbm5lY3QodGhpcy5vbkJ1bmRsZVNlbGVjdGVkLCB0aGlzKTtcbiAgICB0aGlzLm1vZGVsLmRpc3Bvc2UoKTtcbiAgICBzdXBlci5kaXNwb3NlKCk7XG4gIH1cblxuICAvKipcbiAgICogSW5pdGlhbGl6ZSB0aGUgbGVmdCBhcmVhIGZvciBmaWx0ZXJzIGFuZCBidW5kbGVzXG4gICAqL1xuICBwcm90ZWN0ZWQgaW5pdExlZnRQYW5lbCgpOiB2b2lkIHtcbiAgICB0aGlzLl9sZWZ0UGFuZWwgPSBuZXcgUGFuZWwoKTtcbiAgICB0aGlzLl9sZWZ0UGFuZWwuYWRkQ2xhc3MoJ2pwLUxpY2Vuc2VzLUZvcm1BcmVhJyk7XG4gICAgdGhpcy5hZGRXaWRnZXQodGhpcy5fbGVmdFBhbmVsKTtcbiAgICBTcGxpdFBhbmVsLnNldFN0cmV0Y2godGhpcy5fbGVmdFBhbmVsLCAxKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBJbml0aWFsaXplIHRoZSBmaWx0ZXJzXG4gICAqL1xuICBwcm90ZWN0ZWQgaW5pdEZpbHRlcnMoKTogdm9pZCB7XG4gICAgdGhpcy5fZmlsdGVycyA9IG5ldyBMaWNlbnNlcy5GaWx0ZXJzKHRoaXMubW9kZWwpO1xuICAgIFNwbGl0UGFuZWwuc2V0U3RyZXRjaCh0aGlzLl9maWx0ZXJzLCAxKTtcbiAgICB0aGlzLl9sZWZ0UGFuZWwuYWRkV2lkZ2V0KHRoaXMuX2ZpbHRlcnMpO1xuICB9XG5cbiAgLyoqXG4gICAqIEluaXRpYWxpemUgdGhlIGxpc3Rpbmcgb2YgYXZhaWxhYmxlIGJ1bmRsZXNcbiAgICovXG4gIHByb3RlY3RlZCBpbml0QnVuZGxlcygpOiB2b2lkIHtcbiAgICB0aGlzLl9idW5kbGVzID0gbmV3IFRhYkJhcih7XG4gICAgICBvcmllbnRhdGlvbjogJ3ZlcnRpY2FsJyxcbiAgICAgIHJlbmRlcmVyOiBuZXcgTGljZW5zZXMuQnVuZGxlVGFiUmVuZGVyZXIodGhpcy5tb2RlbClcbiAgICB9KTtcbiAgICB0aGlzLl9idW5kbGVzLmFkZENsYXNzKCdqcC1MaWNlbnNlcy1CdW5kbGVzJyk7XG4gICAgU3BsaXRQYW5lbC5zZXRTdHJldGNoKHRoaXMuX2J1bmRsZXMsIDEpO1xuICAgIHRoaXMuX2xlZnRQYW5lbC5hZGRXaWRnZXQodGhpcy5fYnVuZGxlcyk7XG4gICAgdGhpcy5fYnVuZGxlcy5jdXJyZW50Q2hhbmdlZC5jb25uZWN0KHRoaXMub25CdW5kbGVTZWxlY3RlZCwgdGhpcyk7XG4gICAgdGhpcy5tb2RlbC5zdGF0ZUNoYW5nZWQuY29ubmVjdCgoKSA9PiB0aGlzLl9idW5kbGVzLnVwZGF0ZSgpKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBJbml0aWFsaXplIHRoZSBsaXN0aW5nIG9mIHBhY2thZ2VzIHdpdGhpbiB0aGUgY3VycmVudCBidW5kbGVcbiAgICovXG4gIHByb3RlY3RlZCBpbml0R3JpZCgpOiB2b2lkIHtcbiAgICB0aGlzLl9ncmlkID0gbmV3IExpY2Vuc2VzLkdyaWQodGhpcy5tb2RlbCk7XG4gICAgU3BsaXRQYW5lbC5zZXRTdHJldGNoKHRoaXMuX2dyaWQsIDEpO1xuICAgIHRoaXMuYWRkV2lkZ2V0KHRoaXMuX2dyaWQpO1xuICB9XG5cbiAgLyoqXG4gICAqIEluaXRpYWxpemUgdGhlIGZ1bGwgdGV4dCBvZiB0aGUgY3VycmVudCBwYWNrYWdlXG4gICAqL1xuICBwcm90ZWN0ZWQgaW5pdExpY2Vuc2VUZXh0KCk6IHZvaWQge1xuICAgIHRoaXMuX2xpY2Vuc2VUZXh0ID0gbmV3IExpY2Vuc2VzLkZ1bGxUZXh0KHRoaXMubW9kZWwpO1xuICAgIFNwbGl0UGFuZWwuc2V0U3RyZXRjaCh0aGlzLl9ncmlkLCAxKTtcbiAgICB0aGlzLmFkZFdpZGdldCh0aGlzLl9saWNlbnNlVGV4dCk7XG4gIH1cblxuICAvKipcbiAgICogRXZlbnQgaGFuZGxlciBmb3IgdXBkYXRpbmcgdGhlIG1vZGVsIHdpdGggdGhlIGN1cnJlbnQgYnVuZGxlXG4gICAqL1xuICBwcm90ZWN0ZWQgb25CdW5kbGVTZWxlY3RlZCgpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5fYnVuZGxlcy5jdXJyZW50VGl0bGU/LmxhYmVsKSB7XG4gICAgICB0aGlzLm1vZGVsLmN1cnJlbnRCdW5kbGVOYW1lID0gdGhpcy5fYnVuZGxlcy5jdXJyZW50VGl0bGUubGFiZWw7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFVwZGF0ZSB0aGUgYnVuZGxlIHRhYnMuXG4gICAqL1xuICBwcm90ZWN0ZWQgX3VwZGF0ZUJ1bmRsZXMoKTogdm9pZCB7XG4gICAgdGhpcy5fYnVuZGxlcy5jbGVhclRhYnMoKTtcbiAgICBsZXQgaSA9IDA7XG4gICAgY29uc3QgeyBjdXJyZW50QnVuZGxlTmFtZSB9ID0gdGhpcy5tb2RlbDtcbiAgICBsZXQgY3VycmVudEluZGV4ID0gMDtcbiAgICBmb3IgKGNvbnN0IGJ1bmRsZSBvZiB0aGlzLm1vZGVsLmJ1bmRsZU5hbWVzKSB7XG4gICAgICBjb25zdCB0YWIgPSBuZXcgV2lkZ2V0KCk7XG4gICAgICB0YWIudGl0bGUubGFiZWwgPSBidW5kbGU7XG4gICAgICBpZiAoYnVuZGxlID09PSBjdXJyZW50QnVuZGxlTmFtZSkge1xuICAgICAgICBjdXJyZW50SW5kZXggPSBpO1xuICAgICAgfVxuICAgICAgdGhpcy5fYnVuZGxlcy5pbnNlcnRUYWIoKytpLCB0YWIudGl0bGUpO1xuICAgIH1cbiAgICB0aGlzLl9idW5kbGVzLmN1cnJlbnRJbmRleCA9IGN1cnJlbnRJbmRleDtcbiAgfVxuXG4gIC8qKlxuICAgKiBBbiBhcmVhIGZvciBzZWxlY3RpbmcgbGljZW5zZXMgYnkgYnVuZGxlIGFuZCBmaWx0ZXJzXG4gICAqL1xuICBwcm90ZWN0ZWQgX2xlZnRQYW5lbDogUGFuZWw7XG5cbiAgLyoqXG4gICAqIEZpbHRlcnMgb24gdmlzaWJsZSBsaWNlbnNlc1xuICAgKi9cbiAgcHJvdGVjdGVkIF9maWx0ZXJzOiBMaWNlbnNlcy5GaWx0ZXJzO1xuXG4gIC8qKlxuICAgKiBUYWJzIHJlZmxlY3RpbmcgYXZhaWxhYmxlIGJ1bmRsZXNcbiAgICovXG4gIHByb3RlY3RlZCBfYnVuZGxlczogVGFiQmFyPFdpZGdldD47XG5cbiAgLyoqXG4gICAqIEEgZ3JpZCBvZiB0aGUgY3VycmVudCBidW5kbGUncyBwYWNrYWdlcycgbGljZW5zZSBtZXRhZGF0YVxuICAgKi9cbiAgcHJvdGVjdGVkIF9ncmlkOiBMaWNlbnNlcy5HcmlkO1xuXG4gIC8qKlxuICAgKiBUaGUgY3VycmVudGx5LXNlbGVjdGVkIHBhY2thZ2UncyBmdWxsIGxpY2Vuc2UgdGV4dFxuICAgKi9cbiAgcHJvdGVjdGVkIF9saWNlbnNlVGV4dDogTGljZW5zZXMuRnVsbFRleHQ7XG59XG5cbi8qKiBBIG5hbWVzcGFjZSBmb3IgbGljZW5zZSBjb21wb25lbnRzICovXG5leHBvcnQgbmFtZXNwYWNlIExpY2Vuc2VzIHtcbiAgLyoqIFRoZSBpbmZvcm1hdGlvbiBhYm91dCBhIGxpY2Vuc2UgcmVwb3J0IGZvcm1hdCAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJUmVwb3J0Rm9ybWF0IHtcbiAgICB0aXRsZTogc3RyaW5nO1xuICAgIGljb246IExhYkljb247XG4gICAgaWQ6IHN0cmluZztcbiAgfVxuXG4gIC8qKlxuICAgKiBMaWNlbnNlIHJlcG9ydCBmb3JtYXRzIHVuZGVyc3Rvb2QgYnkgdGhlIHNlcnZlciAob25jZSBsb3dlci1jYXNlZClcbiAgICovXG4gIGV4cG9ydCBjb25zdCBSRVBPUlRfRk9STUFUUzogUmVjb3JkPHN0cmluZywgSVJlcG9ydEZvcm1hdD4gPSB7XG4gICAgbWFya2Rvd246IHtcbiAgICAgIGlkOiAnbWFya2Rvd24nLFxuICAgICAgdGl0bGU6ICdNYXJrZG93bicsXG4gICAgICBpY29uOiBtYXJrZG93bkljb25cbiAgICB9LFxuICAgIGNzdjoge1xuICAgICAgaWQ6ICdjc3YnLFxuICAgICAgdGl0bGU6ICdDU1YnLFxuICAgICAgaWNvbjogc3ByZWFkc2hlZXRJY29uXG4gICAgfSxcbiAgICBqc29uOiB7XG4gICAgICBpZDogJ2NzdicsXG4gICAgICB0aXRsZTogJ0pTT04nLFxuICAgICAgaWNvbjoganNvbkljb25cbiAgICB9XG4gIH07XG5cbiAgLyoqXG4gICAqIFRoZSBkZWZhdWx0IGZvcm1hdCAobW9zdCBodW1hbi1yZWFkYWJsZSlcbiAgICovXG4gIGV4cG9ydCBjb25zdCBERUZBVUxUX0ZPUk1BVCA9ICdtYXJrZG93bic7XG5cbiAgLyoqXG4gICAqIE9wdGlvbnMgZm9yIGluc3RhbnRpYXRpbmcgYSBsaWNlbnNlIHZpZXdlclxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgbW9kZWw6IE1vZGVsO1xuICB9XG4gIC8qKlxuICAgKiBPcHRpb25zIGZvciBpbnN0YW50aWF0aW5nIGEgbGljZW5zZSBtb2RlbFxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJTW9kZWxPcHRpb25zIGV4dGVuZHMgSUNyZWF0ZUFyZ3Mge1xuICAgIGxpY2Vuc2VzVXJsOiBzdHJpbmc7XG4gICAgc2VydmVyU2V0dGluZ3M/OiBTZXJ2ZXJDb25uZWN0aW9uLklTZXR0aW5ncztcbiAgICB0cmFuczogVHJhbnNsYXRpb25CdW5kbGU7XG4gIH1cblxuICAvKipcbiAgICogVGhlIEpTT04gcmVzcG9uc2UgZnJvbSB0aGUgQVBJXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElMaWNlbnNlUmVzcG9uc2Uge1xuICAgIGJ1bmRsZXM6IHtcbiAgICAgIFtrZXk6IHN0cmluZ106IElMaWNlbnNlQnVuZGxlO1xuICAgIH07XG4gIH1cblxuICAvKipcbiAgICogQSB0b3AtbGV2ZWwgcmVwb3J0IG9mIHRoZSBsaWNlbnNlcyBmb3IgYWxsIGNvZGUgaW5jbHVkZWQgaW4gYSBidW5kbGVcbiAgICpcbiAgICogIyMjIE5vdGVcbiAgICpcbiAgICogVGhpcyBpcyByb3VnaGx5IGluZm9ybWVkIGJ5IHRoZSB0ZXJtcyBkZWZpbmVkIGluIHRoZSBTUERYIHNwZWMsIHRob3VnaCBpcyBub3RcbiAgICogYW4gU1BEWCBEb2N1bWVudCwgc2luY2UgdGhlcmUgc2VlbSB0byBiZSBzZXZlcmFsIChpbmNvbXBhdGlibGUpIHNwZWNzXG4gICAqIGluIHRoYXQgcmVwby5cbiAgICpcbiAgICogQHNlZSBodHRwczovL2dpdGh1Yi5jb20vc3BkeC9zcGR4LXNwZWMvYmxvYi9kZXZlbG9wbWVudC92Mi4yLjEvc2NoZW1hcy9zcGR4LXNjaGVtYS5qc29uXG4gICAqKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJTGljZW5zZUJ1bmRsZSBleHRlbmRzIFJlYWRvbmx5SlNPTk9iamVjdCB7XG4gICAgcGFja2FnZXM6IElQYWNrYWdlTGljZW5zZUluZm9bXTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIGJlc3QtZWZmb3J0IHNpbmdsZSBidW5kbGVkIHBhY2thZ2UncyBpbmZvcm1hdGlvbi5cbiAgICpcbiAgICogIyMjIE5vdGVcbiAgICpcbiAgICogVGhpcyBpcyByb3VnaGx5IGluZm9ybWVkIGJ5IFNQRFggYHBhY2thZ2VzYCBhbmQgYGhhc0V4dHJhY3RlZExpY2Vuc2VJbmZvc2AsXG4gICAqIGFzIG1ha2luZyBpdCBjb25mb3JtYW50IHdvdWxkIHZhc3RseSBjb21wbGljYXRlIHRoZSBzdHJ1Y3R1cmUuXG4gICAqXG4gICAqIEBzZWUgaHR0cHM6Ly9naXRodWIuY29tL3NwZHgvc3BkeC1zcGVjL2Jsb2IvZGV2ZWxvcG1lbnQvdjIuMi4xL3NjaGVtYXMvc3BkeC1zY2hlbWEuanNvblxuICAgKiovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSVBhY2thZ2VMaWNlbnNlSW5mbyBleHRlbmRzIFJlYWRvbmx5SlNPTk9iamVjdCB7XG4gICAgLyoqXG4gICAgICogdGhlIG5hbWUgb2YgdGhlIHBhY2thZ2UgYXMgaXQgYXBwZWFycyBpbiBwYWNrYWdlLmpzb25cbiAgICAgKi9cbiAgICBuYW1lOiBzdHJpbmc7XG4gICAgLyoqXG4gICAgICogdGhlIHZlcnNpb24gb2YgdGhlIHBhY2thZ2UsIG9yIGFuIGVtcHR5IHN0cmluZyBpZiB1bmtub3duXG4gICAgICovXG4gICAgdmVyc2lvbkluZm86IHN0cmluZztcbiAgICAvKipcbiAgICAgKiBhbiBTUERYIGxpY2Vuc2UgaWRlbnRpZmllciBvciBMaWNlbnNlUmVmLCBvciBhbiBlbXB0eSBzdHJpbmcgaWYgdW5rbm93blxuICAgICAqL1xuICAgIGxpY2Vuc2VJZDogc3RyaW5nO1xuICAgIC8qKlxuICAgICAqIHRoZSB2ZXJiYXRpbSBleHRyYWN0ZWQgdGV4dCBvZiB0aGUgbGljZW5zZSwgb3IgYW4gZW1wdHkgc3RyaW5nIGlmIHVua25vd25cbiAgICAgKi9cbiAgICBleHRyYWN0ZWRUZXh0OiBzdHJpbmc7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGZvcm1hdCBpbmZvcm1hdGlvbiBmb3IgYSBkb3dubG9hZFxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJRG93bmxvYWRPcHRpb25zIHtcbiAgICBmb3JtYXQ6IHN0cmluZztcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgZmllbGRzIHdoaWNoIGNhbiBiZSBmaWx0ZXJlZFxuICAgKi9cbiAgZXhwb3J0IHR5cGUgVEZpbHRlcktleSA9ICduYW1lJyB8ICd2ZXJzaW9uSW5mbycgfCAnbGljZW5zZUlkJztcblxuICBleHBvcnQgaW50ZXJmYWNlIElDcmVhdGVBcmdzIHtcbiAgICBjdXJyZW50QnVuZGxlTmFtZT86IHN0cmluZyB8IG51bGw7XG4gICAgcGFja2FnZUZpbHRlcj86IFBhcnRpYWw8SVBhY2thZ2VMaWNlbnNlSW5mbz4gfCBudWxsO1xuICAgIGN1cnJlbnRQYWNrYWdlSW5kZXg/OiBudW1iZXIgfCBudWxsO1xuICB9XG5cbiAgLyoqXG4gICAqIEEgbW9kZWwgZm9yIGxpY2Vuc2UgZGF0YVxuICAgKi9cbiAgZXhwb3J0IGNsYXNzIE1vZGVsIGV4dGVuZHMgVkRvbU1vZGVsIGltcGxlbWVudHMgSUNyZWF0ZUFyZ3Mge1xuICAgIGNvbnN0cnVjdG9yKG9wdGlvbnM6IElNb2RlbE9wdGlvbnMpIHtcbiAgICAgIHN1cGVyKCk7XG4gICAgICB0aGlzLl90cmFucyA9IG9wdGlvbnMudHJhbnM7XG4gICAgICB0aGlzLl9saWNlbnNlc1VybCA9IG9wdGlvbnMubGljZW5zZXNVcmw7XG4gICAgICB0aGlzLl9zZXJ2ZXJTZXR0aW5ncyA9XG4gICAgICAgIG9wdGlvbnMuc2VydmVyU2V0dGluZ3MgfHwgU2VydmVyQ29ubmVjdGlvbi5tYWtlU2V0dGluZ3MoKTtcbiAgICAgIGlmIChvcHRpb25zLmN1cnJlbnRCdW5kbGVOYW1lKSB7XG4gICAgICAgIHRoaXMuX2N1cnJlbnRCdW5kbGVOYW1lID0gb3B0aW9ucy5jdXJyZW50QnVuZGxlTmFtZTtcbiAgICAgIH1cbiAgICAgIGlmIChvcHRpb25zLnBhY2thZ2VGaWx0ZXIpIHtcbiAgICAgICAgdGhpcy5fcGFja2FnZUZpbHRlciA9IG9wdGlvbnMucGFja2FnZUZpbHRlcjtcbiAgICAgIH1cbiAgICAgIGlmIChvcHRpb25zLmN1cnJlbnRQYWNrYWdlSW5kZXgpIHtcbiAgICAgICAgdGhpcy5fY3VycmVudFBhY2thZ2VJbmRleCA9IG9wdGlvbnMuY3VycmVudFBhY2thZ2VJbmRleDtcbiAgICAgIH1cbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBIYW5kbGUgdGhlIGluaXRpYWwgcmVxdWVzdCBmb3IgdGhlIGxpY2Vuc2VzIGZyb20gdGhlIHNlcnZlci5cbiAgICAgKi9cbiAgICBhc3luYyBpbml0TGljZW5zZXMoKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgICB0cnkge1xuICAgICAgICBjb25zdCByZXNwb25zZSA9IGF3YWl0IFNlcnZlckNvbm5lY3Rpb24ubWFrZVJlcXVlc3QoXG4gICAgICAgICAgdGhpcy5fbGljZW5zZXNVcmwsXG4gICAgICAgICAge30sXG4gICAgICAgICAgdGhpcy5fc2VydmVyU2V0dGluZ3NcbiAgICAgICAgKTtcbiAgICAgICAgdGhpcy5fc2VydmVyUmVzcG9uc2UgPSBhd2FpdCByZXNwb25zZS5qc29uKCk7XG4gICAgICAgIHRoaXMuX2xpY2Vuc2VzUmVhZHkucmVzb2x2ZSgpO1xuICAgICAgICB0aGlzLnN0YXRlQ2hhbmdlZC5lbWl0KHZvaWQgMCk7XG4gICAgICB9IGNhdGNoIChlcnIpIHtcbiAgICAgICAgdGhpcy5fbGljZW5zZXNSZWFkeS5yZWplY3QoZXJyKTtcbiAgICAgIH1cbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBDcmVhdGUgYSB0ZW1wb3JhcnkgZG93bmxvYWQgbGluaywgYW5kIGVtdWxhdGUgY2xpY2tpbmcgaXQgdG8gdHJpZ2dlciBhIG5hbWVkXG4gICAgICogZmlsZSBkb3dubG9hZC5cbiAgICAgKi9cbiAgICBhc3luYyBkb3dubG9hZChvcHRpb25zOiBJRG93bmxvYWRPcHRpb25zKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgICBjb25zdCB1cmwgPSBgJHt0aGlzLl9saWNlbnNlc1VybH0/Zm9ybWF0PSR7b3B0aW9ucy5mb3JtYXR9JmRvd25sb2FkPTFgO1xuICAgICAgY29uc3QgZWxlbWVudCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2EnKTtcbiAgICAgIGVsZW1lbnQuaHJlZiA9IHVybDtcbiAgICAgIGVsZW1lbnQuZG93bmxvYWQgPSAnJztcbiAgICAgIGRvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoZWxlbWVudCk7XG4gICAgICBlbGVtZW50LmNsaWNrKCk7XG4gICAgICBkb2N1bWVudC5ib2R5LnJlbW92ZUNoaWxkKGVsZW1lbnQpO1xuICAgICAgcmV0dXJuIHZvaWQgMDtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBBIHByb21pc2UgdGhhdCByZXNvbHZlcyB3aGVuIHRoZSBsaWNlbnNlcyBmcm9tIHRoZSBzZXJ2ZXIgY2hhbmdlXG4gICAgICovXG4gICAgZ2V0IHNlbGVjdGVkUGFja2FnZUNoYW5nZWQoKTogSVNpZ25hbDxNb2RlbCwgdm9pZD4ge1xuICAgICAgcmV0dXJuIHRoaXMuX3NlbGVjdGVkUGFja2FnZUNoYW5nZWQ7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogQSBwcm9taXNlIHRoYXQgcmVzb2x2ZXMgd2hlbiB0aGUgdHJhY2thYmxlIGRhdGEgY2hhbmdlc1xuICAgICAqL1xuICAgIGdldCB0cmFja2VyRGF0YUNoYW5nZWQoKTogSVNpZ25hbDxNb2RlbCwgdm9pZD4ge1xuICAgICAgcmV0dXJuIHRoaXMuX3RyYWNrZXJEYXRhQ2hhbmdlZDtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBUaGUgbmFtZXMgb2YgdGhlIGxpY2Vuc2UgYnVuZGxlcyBhdmFpbGFibGVcbiAgICAgKi9cbiAgICBnZXQgYnVuZGxlTmFtZXMoKTogc3RyaW5nW10ge1xuICAgICAgcmV0dXJuIE9iamVjdC5rZXlzKHRoaXMuX3NlcnZlclJlc3BvbnNlPy5idW5kbGVzIHx8IHt9KTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBUaGUgY3VycmVudCBsaWNlbnNlIGJ1bmRsZVxuICAgICAqL1xuICAgIGdldCBjdXJyZW50QnVuZGxlTmFtZSgpOiBzdHJpbmcgfCBudWxsIHtcbiAgICAgIGlmICh0aGlzLl9jdXJyZW50QnVuZGxlTmFtZSkge1xuICAgICAgICByZXR1cm4gdGhpcy5fY3VycmVudEJ1bmRsZU5hbWU7XG4gICAgICB9XG4gICAgICBpZiAodGhpcy5idW5kbGVOYW1lcy5sZW5ndGgpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMuYnVuZGxlTmFtZXNbMF07XG4gICAgICB9XG4gICAgICByZXR1cm4gbnVsbDtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBTZXQgdGhlIGN1cnJlbnQgbGljZW5zZSBidW5kbGUsIGFuZCByZXNldCB0aGUgc2VsZWN0ZWQgaW5kZXhcbiAgICAgKi9cbiAgICBzZXQgY3VycmVudEJ1bmRsZU5hbWUoY3VycmVudEJ1bmRsZU5hbWU6IHN0cmluZyB8IG51bGwpIHtcbiAgICAgIGlmICh0aGlzLl9jdXJyZW50QnVuZGxlTmFtZSAhPT0gY3VycmVudEJ1bmRsZU5hbWUpIHtcbiAgICAgICAgdGhpcy5fY3VycmVudEJ1bmRsZU5hbWUgPSBjdXJyZW50QnVuZGxlTmFtZTtcbiAgICAgICAgdGhpcy5zdGF0ZUNoYW5nZWQuZW1pdCh2b2lkIDApO1xuICAgICAgICB0aGlzLl90cmFja2VyRGF0YUNoYW5nZWQuZW1pdCh2b2lkIDApO1xuICAgICAgfVxuICAgIH1cblxuICAgIC8qKlxuICAgICAqIEEgcHJvbWlzZSB0aGF0IHJlc29sdmVzIHdoZW4gdGhlIGxpY2Vuc2VzIGFyZSBhdmFpbGFibGUgZnJvbSB0aGUgc2VydmVyXG4gICAgICovXG4gICAgZ2V0IGxpY2Vuc2VzUmVhZHkoKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgICByZXR1cm4gdGhpcy5fbGljZW5zZXNSZWFkeS5wcm9taXNlO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIEFsbCB0aGUgbGljZW5zZSBidW5kbGVzLCBrZXllZCBieSB0aGUgZGlzdHJpYnV0aW5nIHBhY2thZ2VzXG4gICAgICovXG4gICAgZ2V0IGJ1bmRsZXMoKTogbnVsbCB8IHsgW2tleTogc3RyaW5nXTogSUxpY2Vuc2VCdW5kbGUgfSB7XG4gICAgICByZXR1cm4gdGhpcy5fc2VydmVyUmVzcG9uc2U/LmJ1bmRsZXMgfHwge307XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogVGhlIGluZGV4IG9mIHRoZSBjdXJyZW50bHktc2VsZWN0ZWQgcGFja2FnZSB3aXRoaW4gaXRzIGxpY2Vuc2UgYnVuZGxlXG4gICAgICovXG4gICAgZ2V0IGN1cnJlbnRQYWNrYWdlSW5kZXgoKTogbnVtYmVyIHwgbnVsbCB7XG4gICAgICByZXR1cm4gdGhpcy5fY3VycmVudFBhY2thZ2VJbmRleDtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBVcGRhdGUgdGhlIGN1cnJlbnRseS1zZWxlY3RlZCBwYWNrYWdlIHdpdGhpbiBpdHMgbGljZW5zZSBidW5kbGVcbiAgICAgKi9cbiAgICBzZXQgY3VycmVudFBhY2thZ2VJbmRleChjdXJyZW50UGFja2FnZUluZGV4OiBudW1iZXIgfCBudWxsKSB7XG4gICAgICBpZiAodGhpcy5fY3VycmVudFBhY2thZ2VJbmRleCA9PT0gY3VycmVudFBhY2thZ2VJbmRleCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICB0aGlzLl9jdXJyZW50UGFja2FnZUluZGV4ID0gY3VycmVudFBhY2thZ2VJbmRleDtcbiAgICAgIHRoaXMuX3NlbGVjdGVkUGFja2FnZUNoYW5nZWQuZW1pdCh2b2lkIDApO1xuICAgICAgdGhpcy5zdGF0ZUNoYW5nZWQuZW1pdCh2b2lkIDApO1xuICAgICAgdGhpcy5fdHJhY2tlckRhdGFDaGFuZ2VkLmVtaXQodm9pZCAwKTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBUaGUgbGljZW5zZSBkYXRhIGZvciB0aGUgY3VycmVudGx5LXNlbGVjdGVkIHBhY2thZ2VcbiAgICAgKi9cbiAgICBnZXQgY3VycmVudFBhY2thZ2UoKTogSVBhY2thZ2VMaWNlbnNlSW5mbyB8IG51bGwge1xuICAgICAgaWYgKFxuICAgICAgICB0aGlzLmN1cnJlbnRCdW5kbGVOYW1lICYmXG4gICAgICAgIHRoaXMuYnVuZGxlcyAmJlxuICAgICAgICB0aGlzLl9jdXJyZW50UGFja2FnZUluZGV4ICE9IG51bGxcbiAgICAgICkge1xuICAgICAgICByZXR1cm4gdGhpcy5nZXRGaWx0ZXJlZFBhY2thZ2VzKFxuICAgICAgICAgIHRoaXMuYnVuZGxlc1t0aGlzLmN1cnJlbnRCdW5kbGVOYW1lXT8ucGFja2FnZXMgfHwgW11cbiAgICAgICAgKVt0aGlzLl9jdXJyZW50UGFja2FnZUluZGV4XTtcbiAgICAgIH1cblxuICAgICAgcmV0dXJuIG51bGw7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogQSB0cmFuc2xhdGlvbiBidW5kbGVcbiAgICAgKi9cbiAgICBnZXQgdHJhbnMoKTogVHJhbnNsYXRpb25CdW5kbGUge1xuICAgICAgcmV0dXJuIHRoaXMuX3RyYW5zO1xuICAgIH1cblxuICAgIGdldCB0aXRsZSgpOiBzdHJpbmcge1xuICAgICAgcmV0dXJuIGAke3RoaXMuX2N1cnJlbnRCdW5kbGVOYW1lIHx8ICcnfSAke3RoaXMuX3RyYW5zLl9fKFxuICAgICAgICAnTGljZW5zZXMnXG4gICAgICApfWAudHJpbSgpO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIFRoZSBjdXJyZW50IHBhY2thZ2UgZmlsdGVyXG4gICAgICovXG4gICAgZ2V0IHBhY2thZ2VGaWx0ZXIoKTogUGFydGlhbDxJUGFja2FnZUxpY2Vuc2VJbmZvPiB7XG4gICAgICByZXR1cm4gdGhpcy5fcGFja2FnZUZpbHRlcjtcbiAgICB9XG5cbiAgICBzZXQgcGFja2FnZUZpbHRlcihwYWNrYWdlRmlsdGVyOiBQYXJ0aWFsPElQYWNrYWdlTGljZW5zZUluZm8+KSB7XG4gICAgICB0aGlzLl9wYWNrYWdlRmlsdGVyID0gcGFja2FnZUZpbHRlcjtcbiAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQodm9pZCAwKTtcbiAgICAgIHRoaXMuX3RyYWNrZXJEYXRhQ2hhbmdlZC5lbWl0KHZvaWQgMCk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogR2V0IGZpbHRlcmVkIHBhY2thZ2VzIGZyb20gY3VycmVudCBidW5kbGUgd2hlcmUgYXQgbGVhc3Qgb25lIHRva2VuIG9mIGVhY2hcbiAgICAgKiBrZXkgaXMgcHJlc2VudC5cbiAgICAgKi9cbiAgICBnZXRGaWx0ZXJlZFBhY2thZ2VzKGFsbFJvd3M6IElQYWNrYWdlTGljZW5zZUluZm9bXSk6IElQYWNrYWdlTGljZW5zZUluZm9bXSB7XG4gICAgICBsZXQgcm93czogSVBhY2thZ2VMaWNlbnNlSW5mb1tdID0gW107XG4gICAgICBsZXQgZmlsdGVyczogW3N0cmluZywgc3RyaW5nW11dW10gPSBPYmplY3QuZW50cmllcyh0aGlzLl9wYWNrYWdlRmlsdGVyKVxuICAgICAgICAuZmlsdGVyKChbaywgdl0pID0+IHYgJiYgYCR7dn1gLnRyaW0oKS5sZW5ndGgpXG4gICAgICAgIC5tYXAoKFtrLCB2XSkgPT4gW2ssIGAke3Z9YC50b0xvd2VyQ2FzZSgpLnRyaW0oKS5zcGxpdCgnICcpXSk7XG4gICAgICBmb3IgKGNvbnN0IHJvdyBvZiBhbGxSb3dzKSB7XG4gICAgICAgIGxldCBrZXlIaXRzID0gMDtcbiAgICAgICAgZm9yIChjb25zdCBba2V5LCBiaXRzXSBvZiBmaWx0ZXJzKSB7XG4gICAgICAgICAgbGV0IGJpdEhpdHMgPSAwO1xuICAgICAgICAgIGxldCByb3dLZXlWYWx1ZSA9IGAke3Jvd1trZXldfWAudG9Mb3dlckNhc2UoKTtcbiAgICAgICAgICBmb3IgKGNvbnN0IGJpdCBvZiBiaXRzKSB7XG4gICAgICAgICAgICBpZiAocm93S2V5VmFsdWUuaW5jbHVkZXMoYml0KSkge1xuICAgICAgICAgICAgICBiaXRIaXRzICs9IDE7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgfVxuICAgICAgICAgIGlmIChiaXRIaXRzKSB7XG4gICAgICAgICAgICBrZXlIaXRzICs9IDE7XG4gICAgICAgICAgfVxuICAgICAgICB9XG4gICAgICAgIGlmIChrZXlIaXRzID09PSBmaWx0ZXJzLmxlbmd0aCkge1xuICAgICAgICAgIHJvd3MucHVzaChyb3cpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgICByZXR1cm4gT2JqZWN0LnZhbHVlcyhyb3dzKTtcbiAgICB9XG5cbiAgICBwcml2YXRlIF9zZWxlY3RlZFBhY2thZ2VDaGFuZ2VkOiBTaWduYWw8TW9kZWwsIHZvaWQ+ID0gbmV3IFNpZ25hbCh0aGlzKTtcbiAgICBwcml2YXRlIF90cmFja2VyRGF0YUNoYW5nZWQ6IFNpZ25hbDxNb2RlbCwgdm9pZD4gPSBuZXcgU2lnbmFsKHRoaXMpO1xuICAgIHByaXZhdGUgX3NlcnZlclJlc3BvbnNlOiBJTGljZW5zZVJlc3BvbnNlIHwgbnVsbDtcbiAgICBwcml2YXRlIF9saWNlbnNlc1VybDogc3RyaW5nO1xuICAgIHByaXZhdGUgX3NlcnZlclNldHRpbmdzOiBTZXJ2ZXJDb25uZWN0aW9uLklTZXR0aW5ncztcbiAgICBwcml2YXRlIF9jdXJyZW50QnVuZGxlTmFtZTogc3RyaW5nIHwgbnVsbDtcbiAgICBwcml2YXRlIF90cmFuczogVHJhbnNsYXRpb25CdW5kbGU7XG4gICAgcHJpdmF0ZSBfY3VycmVudFBhY2thZ2VJbmRleDogbnVtYmVyIHwgbnVsbCA9IDA7XG4gICAgcHJpdmF0ZSBfbGljZW5zZXNSZWFkeSA9IG5ldyBQcm9taXNlRGVsZWdhdGU8dm9pZD4oKTtcbiAgICBwcml2YXRlIF9wYWNrYWdlRmlsdGVyOiBQYXJ0aWFsPElQYWNrYWdlTGljZW5zZUluZm8+ID0ge307XG4gIH1cblxuICAvKipcbiAgICogQSBmaWx0ZXIgZm9ybSBmb3IgbGltaXRpbmcgdGhlIHBhY2thZ2VzIGRpc3BsYXllZFxuICAgKi9cbiAgZXhwb3J0IGNsYXNzIEZpbHRlcnMgZXh0ZW5kcyBWRG9tUmVuZGVyZXI8TW9kZWw+IHtcbiAgICBjb25zdHJ1Y3Rvcihtb2RlbDogTW9kZWwpIHtcbiAgICAgIHN1cGVyKG1vZGVsKTtcbiAgICAgIHRoaXMuYWRkQ2xhc3MoJ2pwLUxpY2Vuc2VzLUZpbHRlcnMnKTtcbiAgICAgIHRoaXMuYWRkQ2xhc3MoJ2pwLVJlbmRlcmVkSFRNTENvbW1vbicpO1xuICAgIH1cblxuICAgIHByb3RlY3RlZCByZW5kZXIoKTogSlNYLkVsZW1lbnQge1xuICAgICAgY29uc3QgeyB0cmFucyB9ID0gdGhpcy5tb2RlbDtcbiAgICAgIHJldHVybiAoXG4gICAgICAgIDxkaXY+XG4gICAgICAgICAgPGxhYmVsPlxuICAgICAgICAgICAgPHN0cm9uZz57dHJhbnMuX18oJ0ZpbHRlciBMaWNlbnNlcyBCeScpfTwvc3Ryb25nPlxuICAgICAgICAgIDwvbGFiZWw+XG4gICAgICAgICAgPHVsPlxuICAgICAgICAgICAgPGxpPlxuICAgICAgICAgICAgICA8bGFiZWw+e3RyYW5zLl9fKCdQYWNrYWdlJyl9PC9sYWJlbD5cbiAgICAgICAgICAgICAge3RoaXMucmVuZGVyRmlsdGVyKCduYW1lJyl9XG4gICAgICAgICAgICA8L2xpPlxuICAgICAgICAgICAgPGxpPlxuICAgICAgICAgICAgICA8bGFiZWw+e3RyYW5zLl9fKCdWZXJzaW9uJyl9PC9sYWJlbD5cbiAgICAgICAgICAgICAge3RoaXMucmVuZGVyRmlsdGVyKCd2ZXJzaW9uSW5mbycpfVxuICAgICAgICAgICAgPC9saT5cbiAgICAgICAgICAgIDxsaT5cbiAgICAgICAgICAgICAgPGxhYmVsPnt0cmFucy5fXygnTGljZW5zZScpfTwvbGFiZWw+XG4gICAgICAgICAgICAgIHt0aGlzLnJlbmRlckZpbHRlcignbGljZW5zZUlkJyl9XG4gICAgICAgICAgICA8L2xpPlxuICAgICAgICAgIDwvdWw+XG4gICAgICAgICAgPGxhYmVsPlxuICAgICAgICAgICAgPHN0cm9uZz57dHJhbnMuX18oJ0Rpc3RyaWJ1dGlvbnMnKX08L3N0cm9uZz5cbiAgICAgICAgICA8L2xhYmVsPlxuICAgICAgICA8L2Rpdj5cbiAgICAgICk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogUmVuZGVyIGEgZmlsdGVyIGlucHV0XG4gICAgICovXG4gICAgcHJvdGVjdGVkIHJlbmRlckZpbHRlciA9IChrZXk6IFRGaWx0ZXJLZXkpOiBKU1guRWxlbWVudCA9PiB7XG4gICAgICBjb25zdCB2YWx1ZSA9IHRoaXMubW9kZWwucGFja2FnZUZpbHRlcltrZXldIHx8ICcnO1xuICAgICAgcmV0dXJuIChcbiAgICAgICAgPGlucHV0XG4gICAgICAgICAgdHlwZT1cInRleHRcIlxuICAgICAgICAgIG5hbWU9e2tleX1cbiAgICAgICAgICBkZWZhdWx0VmFsdWU9e3ZhbHVlfVxuICAgICAgICAgIGNsYXNzTmFtZT1cImpwLW1vZC1zdHlsZWRcIlxuICAgICAgICAgIG9uSW5wdXQ9e3RoaXMub25GaWx0ZXJJbnB1dH1cbiAgICAgICAgLz5cbiAgICAgICk7XG4gICAgfTtcblxuICAgIC8qKlxuICAgICAqIEhhbmRsZSBhIGZpbHRlciBpbnB1dCBjaGFuZ2luZ1xuICAgICAqL1xuICAgIHByb3RlY3RlZCBvbkZpbHRlcklucHV0ID0gKFxuICAgICAgZXZ0OiBSZWFjdC5DaGFuZ2VFdmVudDxIVE1MSW5wdXRFbGVtZW50PlxuICAgICk6IHZvaWQgPT4ge1xuICAgICAgY29uc3QgaW5wdXQgPSBldnQuY3VycmVudFRhcmdldDtcbiAgICAgIGNvbnN0IHsgbmFtZSwgdmFsdWUgfSA9IGlucHV0O1xuICAgICAgdGhpcy5tb2RlbC5wYWNrYWdlRmlsdGVyID0geyAuLi50aGlzLm1vZGVsLnBhY2thZ2VGaWx0ZXIsIFtuYW1lXTogdmFsdWUgfTtcbiAgICB9O1xuICB9XG5cbiAgLyoqXG4gICAqIEEgZmFuY3kgYnVuZGxlIHJlbmRlcmVyIHdpdGggdGhlIHBhY2thZ2UgY291bnRcbiAgICovXG4gIGV4cG9ydCBjbGFzcyBCdW5kbGVUYWJSZW5kZXJlciBleHRlbmRzIFRhYkJhci5SZW5kZXJlciB7XG4gICAgLyoqXG4gICAgICogQSBtb2RlbCBvZiB0aGUgc3RhdGUgb2YgbGljZW5zZSB2aWV3aW5nIGFzIHdlbGwgYXMgdGhlIHVuZGVybHlpbmcgZGF0YVxuICAgICAqL1xuICAgIG1vZGVsOiBNb2RlbDtcblxuICAgIHJlYWRvbmx5IGNsb3NlSWNvblNlbGVjdG9yID0gJy5sbS1UYWJCYXItdGFiQ2xvc2VJY29uJztcblxuICAgIGNvbnN0cnVjdG9yKG1vZGVsOiBNb2RlbCkge1xuICAgICAgc3VwZXIoKTtcbiAgICAgIHRoaXMubW9kZWwgPSBtb2RlbDtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBSZW5kZXIgYSBmdWxsIGJ1bmRsZVxuICAgICAqL1xuICAgIHJlbmRlclRhYihkYXRhOiBUYWJCYXIuSVJlbmRlckRhdGE8V2lkZ2V0Pik6IFZpcnR1YWxFbGVtZW50IHtcbiAgICAgIGxldCB0aXRsZSA9IGRhdGEudGl0bGUuY2FwdGlvbjtcbiAgICAgIGxldCBrZXkgPSB0aGlzLmNyZWF0ZVRhYktleShkYXRhKTtcbiAgICAgIGxldCBzdHlsZSA9IHRoaXMuY3JlYXRlVGFiU3R5bGUoZGF0YSk7XG4gICAgICBsZXQgY2xhc3NOYW1lID0gdGhpcy5jcmVhdGVUYWJDbGFzcyhkYXRhKTtcbiAgICAgIGxldCBkYXRhc2V0ID0gdGhpcy5jcmVhdGVUYWJEYXRhc2V0KGRhdGEpO1xuICAgICAgcmV0dXJuIGgubGkoXG4gICAgICAgIHsga2V5LCBjbGFzc05hbWUsIHRpdGxlLCBzdHlsZSwgZGF0YXNldCB9LFxuICAgICAgICB0aGlzLnJlbmRlckljb24oZGF0YSksXG4gICAgICAgIHRoaXMucmVuZGVyTGFiZWwoZGF0YSksXG4gICAgICAgIHRoaXMucmVuZGVyQ291bnRCYWRnZShkYXRhKVxuICAgICAgKTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBSZW5kZXIgdGhlIHBhY2thZ2UgY291bnRcbiAgICAgKi9cbiAgICByZW5kZXJDb3VudEJhZGdlKGRhdGE6IFRhYkJhci5JUmVuZGVyRGF0YTxXaWRnZXQ+KTogVmlydHVhbEVsZW1lbnQge1xuICAgICAgY29uc3QgYnVuZGxlID0gZGF0YS50aXRsZS5sYWJlbDtcbiAgICAgIGNvbnN0IHsgYnVuZGxlcyB9ID0gdGhpcy5tb2RlbDtcbiAgICAgIGNvbnN0IHBhY2thZ2VzID0gdGhpcy5tb2RlbC5nZXRGaWx0ZXJlZFBhY2thZ2VzKFxuICAgICAgICAoYnVuZGxlcyAmJiBidW5kbGUgPyBidW5kbGVzW2J1bmRsZV0ucGFja2FnZXMgOiBbXSkgfHwgW11cbiAgICAgICk7XG4gICAgICByZXR1cm4gaC5sYWJlbCh7fSwgYCR7cGFja2FnZXMubGVuZ3RofWApO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBBIGdyaWQgb2YgbGljZW5zZXNcbiAgICovXG4gIGV4cG9ydCBjbGFzcyBHcmlkIGV4dGVuZHMgVkRvbVJlbmRlcmVyPExpY2Vuc2VzLk1vZGVsPiB7XG4gICAgY29uc3RydWN0b3IobW9kZWw6IExpY2Vuc2VzLk1vZGVsKSB7XG4gICAgICBzdXBlcihtb2RlbCk7XG4gICAgICB0aGlzLmFkZENsYXNzKCdqcC1MaWNlbnNlcy1HcmlkJyk7XG4gICAgICB0aGlzLmFkZENsYXNzKCdqcC1SZW5kZXJlZEhUTUxDb21tb24nKTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBSZW5kZXIgYSBncmlkIG9mIHBhY2thZ2UgbGljZW5zZSBpbmZvcm1hdGlvblxuICAgICAqL1xuICAgIHByb3RlY3RlZCByZW5kZXIoKTogSlNYLkVsZW1lbnQge1xuICAgICAgY29uc3QgeyBidW5kbGVzLCBjdXJyZW50QnVuZGxlTmFtZSwgdHJhbnMgfSA9IHRoaXMubW9kZWw7XG4gICAgICBjb25zdCBmaWx0ZXJlZFBhY2thZ2VzID0gdGhpcy5tb2RlbC5nZXRGaWx0ZXJlZFBhY2thZ2VzKFxuICAgICAgICBidW5kbGVzICYmIGN1cnJlbnRCdW5kbGVOYW1lXG4gICAgICAgICAgPyBidW5kbGVzW2N1cnJlbnRCdW5kbGVOYW1lXT8ucGFja2FnZXMgfHwgW11cbiAgICAgICAgICA6IFtdXG4gICAgICApO1xuICAgICAgaWYgKCFmaWx0ZXJlZFBhY2thZ2VzLmxlbmd0aCkge1xuICAgICAgICByZXR1cm4gKFxuICAgICAgICAgIDxibG9ja3F1b3RlPlxuICAgICAgICAgICAgPGVtPnt0cmFucy5fXygnTm8gUGFja2FnZXMgZm91bmQnKX08L2VtPlxuICAgICAgICAgIDwvYmxvY2txdW90ZT5cbiAgICAgICAgKTtcbiAgICAgIH1cbiAgICAgIHJldHVybiAoXG4gICAgICAgIDxmb3JtPlxuICAgICAgICAgIDx0YWJsZT5cbiAgICAgICAgICAgIDx0aGVhZD5cbiAgICAgICAgICAgICAgPHRyPlxuICAgICAgICAgICAgICAgIDx0ZD48L3RkPlxuICAgICAgICAgICAgICAgIDx0aD57dHJhbnMuX18oJ1BhY2thZ2UnKX08L3RoPlxuICAgICAgICAgICAgICAgIDx0aD57dHJhbnMuX18oJ1ZlcnNpb24nKX08L3RoPlxuICAgICAgICAgICAgICAgIDx0aD57dHJhbnMuX18oJ0xpY2Vuc2UnKX08L3RoPlxuICAgICAgICAgICAgICA8L3RyPlxuICAgICAgICAgICAgPC90aGVhZD5cbiAgICAgICAgICAgIDx0Ym9keT57ZmlsdGVyZWRQYWNrYWdlcy5tYXAodGhpcy5yZW5kZXJSb3cpfTwvdGJvZHk+XG4gICAgICAgICAgPC90YWJsZT5cbiAgICAgICAgPC9mb3JtPlxuICAgICAgKTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBSZW5kZXIgYSBzaW5nbGUgcGFja2FnZSdzIGxpY2Vuc2UgaW5mb3JtYXRpb25cbiAgICAgKi9cbiAgICBwcm90ZWN0ZWQgcmVuZGVyUm93ID0gKFxuICAgICAgcm93OiBMaWNlbnNlcy5JUGFja2FnZUxpY2Vuc2VJbmZvLFxuICAgICAgaW5kZXg6IG51bWJlclxuICAgICk6IEpTWC5FbGVtZW50ID0+IHtcbiAgICAgIGNvbnN0IHNlbGVjdGVkID0gaW5kZXggPT09IHRoaXMubW9kZWwuY3VycmVudFBhY2thZ2VJbmRleDtcbiAgICAgIGNvbnN0IG9uQ2hlY2sgPSAoKSA9PiAodGhpcy5tb2RlbC5jdXJyZW50UGFja2FnZUluZGV4ID0gaW5kZXgpO1xuICAgICAgcmV0dXJuIChcbiAgICAgICAgPHRyXG4gICAgICAgICAga2V5PXtyb3cubmFtZX1cbiAgICAgICAgICBjbGFzc05hbWU9e3NlbGVjdGVkID8gJ2pwLW1vZC1zZWxlY3RlZCcgOiAnJ31cbiAgICAgICAgICBvbkNsaWNrPXtvbkNoZWNrfVxuICAgICAgICA+XG4gICAgICAgICAgPHRkPlxuICAgICAgICAgICAgPGlucHV0XG4gICAgICAgICAgICAgIHR5cGU9XCJyYWRpb1wiXG4gICAgICAgICAgICAgIG5hbWU9XCJzaG93LXBhY2thZ2UtbGljZW5zZVwiXG4gICAgICAgICAgICAgIHZhbHVlPXtpbmRleH1cbiAgICAgICAgICAgICAgb25DaGFuZ2U9e29uQ2hlY2t9XG4gICAgICAgICAgICAgIGNoZWNrZWQ9e3NlbGVjdGVkfVxuICAgICAgICAgICAgLz5cbiAgICAgICAgICA8L3RkPlxuICAgICAgICAgIDx0aD57cm93Lm5hbWV9PC90aD5cbiAgICAgICAgICA8dGQ+XG4gICAgICAgICAgICA8Y29kZT57cm93LnZlcnNpb25JbmZvfTwvY29kZT5cbiAgICAgICAgICA8L3RkPlxuICAgICAgICAgIDx0ZD5cbiAgICAgICAgICAgIDxjb2RlPntyb3cubGljZW5zZUlkfTwvY29kZT5cbiAgICAgICAgICA8L3RkPlxuICAgICAgICA8L3RyPlxuICAgICAgKTtcbiAgICB9O1xuICB9XG5cbiAgLyoqXG4gICAqIEEgcGFja2FnZSdzIGZ1bGwgbGljZW5zZSB0ZXh0XG4gICAqL1xuICBleHBvcnQgY2xhc3MgRnVsbFRleHQgZXh0ZW5kcyBWRG9tUmVuZGVyZXI8TW9kZWw+IHtcbiAgICBjb25zdHJ1Y3Rvcihtb2RlbDogTW9kZWwpIHtcbiAgICAgIHN1cGVyKG1vZGVsKTtcbiAgICAgIHRoaXMuYWRkQ2xhc3MoJ2pwLUxpY2Vuc2VzLVRleHQnKTtcbiAgICAgIHRoaXMuYWRkQ2xhc3MoJ2pwLVJlbmRlcmVkSFRNTENvbW1vbicpO1xuICAgICAgdGhpcy5hZGRDbGFzcygnanAtUmVuZGVyZWRNYXJrZG93bicpO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIFJlbmRlciB0aGUgbGljZW5zZSB0ZXh0LCBvciBhIG51bGwgc3RhdGUgaWYgbm8gcGFja2FnZSBpcyBzZWxlY3RlZFxuICAgICAqL1xuICAgIHByb3RlY3RlZCByZW5kZXIoKTogSlNYLkVsZW1lbnRbXSB7XG4gICAgICBjb25zdCB7IGN1cnJlbnRQYWNrYWdlLCB0cmFucyB9ID0gdGhpcy5tb2RlbDtcbiAgICAgIGxldCBoZWFkID0gJyc7XG4gICAgICBsZXQgcXVvdGUgPSB0cmFucy5fXygnTm8gUGFja2FnZSBzZWxlY3RlZCcpO1xuICAgICAgbGV0IGNvZGUgPSAnJztcbiAgICAgIGlmIChjdXJyZW50UGFja2FnZSkge1xuICAgICAgICBjb25zdCB7IG5hbWUsIHZlcnNpb25JbmZvLCBsaWNlbnNlSWQsIGV4dHJhY3RlZFRleHQgfSA9IGN1cnJlbnRQYWNrYWdlO1xuICAgICAgICBoZWFkID0gYCR7bmFtZX0gdiR7dmVyc2lvbkluZm99YDtcbiAgICAgICAgcXVvdGUgPSBgJHt0cmFucy5fXygnTGljZW5zZScpfTogJHtcbiAgICAgICAgICBsaWNlbnNlSWQgfHwgdHJhbnMuX18oJ05vIExpY2Vuc2UgSUQgZm91bmQnKVxuICAgICAgICB9YDtcbiAgICAgICAgY29kZSA9IGV4dHJhY3RlZFRleHQgfHwgdHJhbnMuX18oJ05vIExpY2Vuc2UgVGV4dCBmb3VuZCcpO1xuICAgICAgfVxuICAgICAgcmV0dXJuIFtcbiAgICAgICAgPGgxIGtleT1cImgxXCI+e2hlYWR9PC9oMT4sXG4gICAgICAgIDxibG9ja3F1b3RlIGtleT1cInF1b3RlXCI+XG4gICAgICAgICAgPGVtPntxdW90ZX08L2VtPlxuICAgICAgICA8L2Jsb2NrcXVvdGU+LFxuICAgICAgICA8Y29kZSBrZXk9XCJjb2RlXCI+e2NvZGV9PC9jb2RlPlxuICAgICAgXTtcbiAgICB9XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==