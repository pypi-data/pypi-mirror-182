"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_fileeditor-extension_lib_index_js"],{

/***/ "../../packages/fileeditor-extension/lib/commands.js":
/*!***********************************************************!*\
  !*** ../../packages/fileeditor-extension/lib/commands.js ***!
  \***********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CommandIDs": () => (/* binding */ CommandIDs),
/* harmony export */   "Commands": () => (/* binding */ Commands),
/* harmony export */   "FACTORY": () => (/* binding */ FACTORY)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/codeeditor */ "webpack/sharing/consume/default/@jupyterlab/codeeditor/@jupyterlab/codeeditor");
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _codemirror_commands__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @codemirror/commands */ "webpack/sharing/consume/default/@codemirror/commands/@codemirror/commands");
/* harmony import */ var _codemirror_commands__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_codemirror_commands__WEBPACK_IMPORTED_MODULE_6__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.







const autoClosingBracketsNotebook = 'notebook:toggle-autoclosing-brackets';
const autoClosingBracketsConsole = 'console:toggle-autoclosing-brackets';
/**
 * The command IDs used by the fileeditor plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.createNew = 'fileeditor:create-new';
    CommandIDs.createNewMarkdown = 'fileeditor:create-new-markdown-file';
    CommandIDs.changeFontSize = 'fileeditor:change-font-size';
    CommandIDs.lineNumbers = 'fileeditor:toggle-line-numbers';
    CommandIDs.currentLineNumbers = 'fileeditor:toggle-current-line-numbers';
    CommandIDs.lineWrap = 'fileeditor:toggle-line-wrap';
    CommandIDs.currentLineWrap = 'fileeditor:toggle-current-line-wrap';
    CommandIDs.changeTabs = 'fileeditor:change-tabs';
    CommandIDs.matchBrackets = 'fileeditor:toggle-match-brackets';
    CommandIDs.currentMatchBrackets = 'fileeditor:toggle-current-match-brackets';
    CommandIDs.autoClosingBrackets = 'fileeditor:toggle-autoclosing-brackets';
    CommandIDs.autoClosingBracketsUniversal = 'fileeditor:toggle-autoclosing-brackets-universal';
    CommandIDs.createConsole = 'fileeditor:create-console';
    CommandIDs.replaceSelection = 'fileeditor:replace-selection';
    CommandIDs.restartConsole = 'fileeditor:restart-console';
    CommandIDs.runCode = 'fileeditor:run-code';
    CommandIDs.runAllCode = 'fileeditor:run-all';
    CommandIDs.markdownPreview = 'fileeditor:markdown-preview';
    CommandIDs.undo = 'fileeditor:undo';
    CommandIDs.redo = 'fileeditor:redo';
    CommandIDs.cut = 'fileeditor:cut';
    CommandIDs.copy = 'fileeditor:copy';
    CommandIDs.paste = 'fileeditor:paste';
    CommandIDs.selectAll = 'fileeditor:select-all';
    CommandIDs.invokeCompleter = 'completer:invoke-file';
    CommandIDs.selectCompleter = 'completer:select-file';
    CommandIDs.openCodeViewer = 'code-viewer:open';
})(CommandIDs || (CommandIDs = {}));
/**
 * The name of the factory that creates editor widgets.
 */
const FACTORY = 'Editor';
const userSettings = [
    'autoClosingBrackets',
    'codeFolding',
    'cursorBlinkRate',
    'fontFamily',
    'fontSize',
    'insertSpaces',
    'lineHeight',
    'lineNumbers',
    'lineWrap',
    'matchBrackets',
    'readOnly',
    'rulers',
    'showTrailingSpace',
    'tabSize',
    'wordWrapColumn'
];
function filterUserSettings(config) {
    const filteredConfig = Object.assign({}, config);
    // Delete parts of the config that are not user settings (like handlePaste).
    for (let k of Object.keys(config)) {
        if (!userSettings.includes(k)) {
            delete config[k];
        }
    }
    return filteredConfig;
}
let config = filterUserSettings(_jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_1__.CodeEditor.defaultConfig);
/**
 * A utility class for adding commands and menu items,
 * for use by the File Editor extension or other Editor extensions.
 */
var Commands;
(function (Commands) {
    /**
     * Accessor function that returns the createConsole function for use by Create Console commands
     */
    function getCreateConsoleFunction(commands) {
        return async function createConsole(widget, args) {
            var _a;
            const options = args || {};
            const console = await commands.execute('console:create', {
                activate: options['activate'],
                name: (_a = widget.context.contentsModel) === null || _a === void 0 ? void 0 : _a.name,
                path: widget.context.path,
                preferredLanguage: widget.context.model.defaultKernelLanguage,
                ref: widget.id,
                insertMode: 'split-bottom'
            });
            widget.context.pathChanged.connect((sender, value) => {
                var _a;
                console.session.setPath(value);
                console.session.setName((_a = widget.context.contentsModel) === null || _a === void 0 ? void 0 : _a.name);
            });
        };
    }
    /**
     * Update the setting values.
     */
    function updateSettings(settings, commands) {
        config = filterUserSettings(Object.assign(Object.assign({}, _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_1__.CodeEditor.defaultConfig), settings.get('editorConfig').composite));
        // Trigger a refresh of the rendered commands
        commands.notifyCommandChanged();
    }
    Commands.updateSettings = updateSettings;
    /**
     * Update the settings of the current tracker instances.
     */
    function updateTracker(tracker) {
        tracker.forEach(widget => {
            updateWidget(widget.content);
        });
    }
    Commands.updateTracker = updateTracker;
    /**
     * Update the settings of a widget.
     * Skip global settings for transient editor specific configs.
     */
    function updateWidget(widget) {
        const editor = widget.editor;
        editor.setOptions(Object.assign({}, config));
    }
    Commands.updateWidget = updateWidget;
    /**
     * Wrapper function for adding the default File Editor commands
     */
    function addCommands(commands, settingRegistry, trans, id, isEnabled, tracker, browserFactory, consoleTracker, sessionDialogs) {
        /**
         * Add a command to change font size for File Editor
         */
        commands.addCommand(CommandIDs.changeFontSize, {
            execute: args => {
                const delta = Number(args['delta']);
                if (Number.isNaN(delta)) {
                    console.error(`${CommandIDs.changeFontSize}: delta arg must be a number`);
                    return;
                }
                const style = window.getComputedStyle(document.documentElement);
                const cssSize = parseInt(style.getPropertyValue('--jp-code-font-size'), 10);
                const currentSize = config.fontSize || cssSize;
                config.fontSize = currentSize + delta;
                return settingRegistry
                    .set(id, 'editorConfig', config)
                    .catch((reason) => {
                    console.error(`Failed to set ${id}: ${reason.message}`);
                });
            },
            label: args => {
                var _a;
                if (((_a = args.delta) !== null && _a !== void 0 ? _a : 0) > 0) {
                    return args.isMenu
                        ? trans.__('Increase Text Editor Font Size')
                        : trans.__('Increase Font Size');
                }
                else {
                    return args.isMenu
                        ? trans.__('Decrease Text Editor Font Size')
                        : trans.__('Decrease Font Size');
                }
            }
        });
        /**
         * Add the Line Numbers command
         */
        commands.addCommand(CommandIDs.lineNumbers, {
            execute: () => {
                config.lineNumbers = !config.lineNumbers;
                return settingRegistry
                    .set(id, 'editorConfig', config)
                    .catch((reason) => {
                    console.error(`Failed to set ${id}: ${reason.message}`);
                });
            },
            isEnabled,
            isToggled: () => config.lineNumbers,
            label: trans.__('Line Numbers')
        });
        commands.addCommand(CommandIDs.currentLineNumbers, {
            label: trans.__('Show Line Numbers'),
            execute: () => {
                const widget = tracker.currentWidget;
                if (!widget) {
                    return;
                }
                const lineNumbers = !widget.content.editor.getOption('lineNumbers');
                widget.content.editor.setOption('lineNumbers', lineNumbers);
            },
            isEnabled,
            isToggled: () => {
                var _a;
                const widget = tracker.currentWidget;
                return (_a = widget === null || widget === void 0 ? void 0 : widget.content.editor.getOption('lineNumbers')) !== null && _a !== void 0 ? _a : false;
            }
        });
        /**
         * Add the Word Wrap command
         */
        commands.addCommand(CommandIDs.lineWrap, {
            execute: args => {
                config.lineWrap = args['mode'] || 'off';
                return settingRegistry
                    .set(id, 'editorConfig', config)
                    .catch((reason) => {
                    console.error(`Failed to set ${id}: ${reason.message}`);
                });
            },
            isEnabled,
            isToggled: args => {
                const lineWrap = args['mode'] || 'off';
                return config.lineWrap === lineWrap;
            },
            label: trans.__('Word Wrap')
        });
        commands.addCommand(CommandIDs.currentLineWrap, {
            label: trans.__('Wrap Words'),
            execute: () => {
                const widget = tracker.currentWidget;
                if (!widget) {
                    return;
                }
                const oldValue = widget.content.editor.getOption('lineWrap');
                const newValue = oldValue === 'off' ? 'on' : 'off';
                widget.content.editor.setOption('lineWrap', newValue);
            },
            isEnabled,
            isToggled: () => {
                var _a;
                const widget = tracker.currentWidget;
                return (_a = (widget === null || widget === void 0 ? void 0 : widget.content.editor.getOption('lineWrap')) !== 'off') !== null && _a !== void 0 ? _a : false;
            }
        });
        /**
         * Add command for changing tabs size or type in File Editor
         */
        commands.addCommand(CommandIDs.changeTabs, {
            label: args => {
                var _a;
                if (args.insertSpaces) {
                    return trans._n('Spaces: %1', 'Spaces: %1', (_a = args.size) !== null && _a !== void 0 ? _a : 0);
                }
                else {
                    return trans.__('Indent with Tab');
                }
            },
            execute: args => {
                config.tabSize = args['size'] || 4;
                config.insertSpaces = !!args['insertSpaces'];
                return settingRegistry
                    .set(id, 'editorConfig', config)
                    .catch((reason) => {
                    console.error(`Failed to set ${id}: ${reason.message}`);
                });
            },
            isToggled: args => {
                const insertSpaces = !!args['insertSpaces'];
                const size = args['size'] || 4;
                return config.insertSpaces === insertSpaces && config.tabSize === size;
            }
        });
        /**
         * Add the Match Brackets command
         */
        commands.addCommand(CommandIDs.matchBrackets, {
            execute: () => {
                config.matchBrackets = !config.matchBrackets;
                return settingRegistry
                    .set(id, 'editorConfig', config)
                    .catch((reason) => {
                    console.error(`Failed to set ${id}: ${reason.message}`);
                });
            },
            label: trans.__('Match Brackets'),
            isEnabled,
            isToggled: () => config.matchBrackets
        });
        commands.addCommand(CommandIDs.currentMatchBrackets, {
            label: trans.__('Match Brackets'),
            execute: () => {
                const widget = tracker.currentWidget;
                if (!widget) {
                    return;
                }
                const matchBrackets = !widget.content.editor.getOption('matchBrackets');
                widget.content.editor.setOption('matchBrackets', matchBrackets);
            },
            isEnabled,
            isToggled: () => {
                var _a;
                const widget = tracker.currentWidget;
                return (_a = widget === null || widget === void 0 ? void 0 : widget.content.editor.getOption('matchBrackets')) !== null && _a !== void 0 ? _a : false;
            }
        });
        /**
         * Add the Auto Close Brackets for Text Editor command
         */
        commands.addCommand(CommandIDs.autoClosingBrackets, {
            execute: args => {
                var _a;
                config.autoClosingBrackets = !!((_a = args['force']) !== null && _a !== void 0 ? _a : !config.autoClosingBrackets);
                return settingRegistry
                    .set(id, 'editorConfig', config)
                    .catch((reason) => {
                    console.error(`Failed to set ${id}: ${reason.message}`);
                });
            },
            label: trans.__('Auto Close Brackets for Text Editor'),
            isToggled: () => config.autoClosingBrackets
        });
        commands.addCommand(CommandIDs.autoClosingBracketsUniversal, {
            execute: () => {
                const anyToggled = commands.isToggled(CommandIDs.autoClosingBrackets) ||
                    commands.isToggled(autoClosingBracketsNotebook) ||
                    commands.isToggled(autoClosingBracketsConsole);
                // if any auto closing brackets options is toggled, toggle both off
                if (anyToggled) {
                    void commands.execute(CommandIDs.autoClosingBrackets, {
                        force: false
                    });
                    void commands.execute(autoClosingBracketsNotebook, { force: false });
                    void commands.execute(autoClosingBracketsConsole, { force: false });
                }
                else {
                    // both are off, turn them on
                    void commands.execute(CommandIDs.autoClosingBrackets, {
                        force: true
                    });
                    void commands.execute(autoClosingBracketsNotebook, { force: true });
                    void commands.execute(autoClosingBracketsConsole, { force: true });
                }
            },
            label: trans.__('Auto Close Brackets'),
            isToggled: () => commands.isToggled(CommandIDs.autoClosingBrackets) ||
                commands.isToggled(autoClosingBracketsNotebook) ||
                commands.isToggled(autoClosingBracketsConsole)
        });
        /**
         * Add the replace selection for text editor command
         */
        commands.addCommand(CommandIDs.replaceSelection, {
            execute: args => {
                var _a, _b;
                const text = args['text'] || '';
                const widget = tracker.currentWidget;
                if (!widget) {
                    return;
                }
                (_b = (_a = widget.content.editor).replaceSelection) === null || _b === void 0 ? void 0 : _b.call(_a, text);
            },
            isEnabled,
            label: trans.__('Replace Selection in Editor')
        });
        /**
         * Add the Create Console for Editor command
         */
        commands.addCommand(CommandIDs.createConsole, {
            execute: args => {
                const widget = tracker.currentWidget;
                if (!widget) {
                    return;
                }
                return getCreateConsoleFunction(commands)(widget, args);
            },
            isEnabled,
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.consoleIcon,
            label: trans.__('Create Console for Editor')
        });
        /**
         * Restart the Console Kernel linked to the current Editor
         */
        commands.addCommand(CommandIDs.restartConsole, {
            execute: async () => {
                var _a;
                const current = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!current || consoleTracker === null) {
                    return;
                }
                const widget = consoleTracker.find(widget => { var _a; return ((_a = widget.sessionContext.session) === null || _a === void 0 ? void 0 : _a.path) === current.context.path; });
                if (widget) {
                    return (sessionDialogs || _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.sessionContextDialogs).restart(widget.sessionContext);
                }
            },
            label: trans.__('Restart Kernel'),
            isEnabled: () => consoleTracker !== null && isEnabled()
        });
        /**
         * Add the Run Code command
         */
        commands.addCommand(CommandIDs.runCode, {
            execute: () => {
                var _a;
                // Run the appropriate code, taking into account a ```fenced``` code block.
                const widget = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!widget) {
                    return;
                }
                let code = '';
                const editor = widget.editor;
                const path = widget.context.path;
                const extension = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PathExt.extname(path);
                const selection = editor.getSelection();
                const { start, end } = selection;
                let selected = start.column !== end.column || start.line !== end.line;
                if (selected) {
                    // Get the selected code from the editor.
                    const start = editor.getOffsetAt(selection.start);
                    const end = editor.getOffsetAt(selection.end);
                    code = editor.model.value.text.substring(start, end);
                }
                else if (_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.MarkdownCodeBlocks.isMarkdown(extension)) {
                    const { text } = editor.model.value;
                    const blocks = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.MarkdownCodeBlocks.findMarkdownCodeBlocks(text);
                    for (const block of blocks) {
                        if (block.startLine <= start.line && start.line <= block.endLine) {
                            code = block.code;
                            selected = true;
                            break;
                        }
                    }
                }
                if (!selected) {
                    // no selection, submit whole line and advance
                    code = editor.getLine(selection.start.line);
                    const cursor = editor.getCursorPosition();
                    if (cursor.line + 1 === editor.lineCount) {
                        const text = editor.model.value.text;
                        editor.model.value.text = text + '\n';
                    }
                    editor.setCursorPosition({
                        line: cursor.line + 1,
                        column: cursor.column
                    });
                }
                const activate = false;
                if (code) {
                    return commands.execute('console:inject', { activate, code, path });
                }
                else {
                    return Promise.resolve(void 0);
                }
            },
            isEnabled,
            label: trans.__('Run Selected Code')
        });
        /**
         * Add the Run All Code command
         */
        commands.addCommand(CommandIDs.runAllCode, {
            execute: () => {
                var _a;
                const widget = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!widget) {
                    return;
                }
                let code = '';
                const editor = widget.editor;
                const text = editor.model.value.text;
                const path = widget.context.path;
                const extension = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PathExt.extname(path);
                if (_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.MarkdownCodeBlocks.isMarkdown(extension)) {
                    // For Markdown files, run only code blocks.
                    const blocks = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.MarkdownCodeBlocks.findMarkdownCodeBlocks(text);
                    for (const block of blocks) {
                        code += block.code;
                    }
                }
                else {
                    code = text;
                }
                const activate = false;
                if (code) {
                    return commands.execute('console:inject', { activate, code, path });
                }
                else {
                    return Promise.resolve(void 0);
                }
            },
            isEnabled,
            label: trans.__('Run All Code')
        });
        /**
         * Add markdown preview command
         */
        commands.addCommand(CommandIDs.markdownPreview, {
            execute: () => {
                const widget = tracker.currentWidget;
                if (!widget) {
                    return;
                }
                const path = widget.context.path;
                return commands.execute('markdownviewer:open', {
                    path,
                    options: {
                        mode: 'split-right'
                    }
                });
            },
            isVisible: () => {
                const widget = tracker.currentWidget;
                return ((widget && _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PathExt.extname(widget.context.path) === '.md') || false);
            },
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.markdownIcon,
            label: trans.__('Show Markdown Preview')
        });
        /**
         * Add the New File command
         *
         * Defaults to Text/.txt if file type data is not specified
         */
        commands.addCommand(CommandIDs.createNew, {
            label: args => {
                var _a, _b;
                if (args.isPalette) {
                    return (_a = args.paletteLabel) !== null && _a !== void 0 ? _a : trans.__('New Text File');
                }
                return (_b = args.launcherLabel) !== null && _b !== void 0 ? _b : trans.__('Text File');
            },
            caption: args => { var _a; return (_a = args.caption) !== null && _a !== void 0 ? _a : trans.__('Create a new text file'); },
            icon: args => {
                var _a;
                return args.isPalette
                    ? undefined
                    : _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.LabIcon.resolve({
                        icon: (_a = args.iconName) !== null && _a !== void 0 ? _a : _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.textEditorIcon
                    });
            },
            execute: args => {
                var _a;
                const cwd = args.cwd || browserFactory.defaultBrowser.model.path;
                return createNew(commands, cwd, (_a = args.fileExt) !== null && _a !== void 0 ? _a : 'txt');
            }
        });
        /**
         * Add the New Markdown File command
         */
        commands.addCommand(CommandIDs.createNewMarkdown, {
            label: args => args['isPalette']
                ? trans.__('New Markdown File')
                : trans.__('Markdown File'),
            caption: trans.__('Create a new markdown file'),
            icon: args => (args['isPalette'] ? undefined : _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.markdownIcon),
            execute: args => {
                const cwd = args['cwd'] || browserFactory.defaultBrowser.model.path;
                return createNew(commands, cwd, 'md');
            }
        });
        /**
         * Add undo command
         */
        commands.addCommand(CommandIDs.undo, {
            execute: () => {
                var _a;
                const widget = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!widget) {
                    return;
                }
                widget.editor.undo();
            },
            isEnabled: () => {
                var _a;
                if (!isEnabled()) {
                    return false;
                }
                const widget = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!widget) {
                    return false;
                }
                // Ideally enable it when there are undo events stored
                // Reference issue #8590: Code mirror editor could expose the history of undo/redo events
                return true;
            },
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.undoIcon.bindprops({ stylesheet: 'menuItem' }),
            label: trans.__('Undo')
        });
        /**
         * Add redo command
         */
        commands.addCommand(CommandIDs.redo, {
            execute: () => {
                var _a;
                const widget = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!widget) {
                    return;
                }
                widget.editor.redo();
            },
            isEnabled: () => {
                var _a;
                if (!isEnabled()) {
                    return false;
                }
                const widget = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!widget) {
                    return false;
                }
                // Ideally enable it when there are redo events stored
                // Reference issue #8590: Code mirror editor could expose the history of undo/redo events
                return true;
            },
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.redoIcon.bindprops({ stylesheet: 'menuItem' }),
            label: trans.__('Redo')
        });
        /**
         * Add cut command
         */
        commands.addCommand(CommandIDs.cut, {
            execute: () => {
                var _a;
                const widget = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!widget) {
                    return;
                }
                const editor = widget.editor;
                const text = getTextSelection(editor);
                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Clipboard.copyToSystem(text);
                editor.replaceSelection && editor.replaceSelection('');
            },
            isEnabled: () => {
                var _a;
                if (!isEnabled()) {
                    return false;
                }
                const widget = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!widget) {
                    return false;
                }
                // Enable command if there is a text selection in the editor
                return isSelected(widget.editor);
            },
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.cutIcon.bindprops({ stylesheet: 'menuItem' }),
            label: trans.__('Cut')
        });
        /**
         * Add copy command
         */
        commands.addCommand(CommandIDs.copy, {
            execute: () => {
                var _a;
                const widget = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!widget) {
                    return;
                }
                const editor = widget.editor;
                const text = getTextSelection(editor);
                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Clipboard.copyToSystem(text);
            },
            isEnabled: () => {
                var _a;
                if (!isEnabled()) {
                    return false;
                }
                const widget = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!widget) {
                    return false;
                }
                // Enable command if there is a text selection in the editor
                return isSelected(widget.editor);
            },
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.copyIcon.bindprops({ stylesheet: 'menuItem' }),
            label: trans.__('Copy')
        });
        /**
         * Add paste command
         */
        commands.addCommand(CommandIDs.paste, {
            execute: async () => {
                var _a;
                const widget = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!widget) {
                    return;
                }
                const editor = widget.editor;
                // Get data from clipboard
                const clipboard = window.navigator.clipboard;
                const clipboardData = await clipboard.readText();
                if (clipboardData) {
                    // Paste data to the editor
                    editor.replaceSelection && editor.replaceSelection(clipboardData);
                }
            },
            isEnabled: () => { var _a; return Boolean(isEnabled() && ((_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content)); },
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.pasteIcon.bindprops({ stylesheet: 'menuItem' }),
            label: trans.__('Paste')
        });
        /**
         * Add select all command
         */
        commands.addCommand(CommandIDs.selectAll, {
            execute: () => {
                var _a;
                const widget = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content;
                if (!widget) {
                    return;
                }
                const editor = widget.editor;
                editor.execCommand(_codemirror_commands__WEBPACK_IMPORTED_MODULE_6__.selectAll);
            },
            isEnabled: () => { var _a; return Boolean(isEnabled() && ((_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content)); },
            label: trans.__('Select All')
        });
    }
    Commands.addCommands = addCommands;
    function addCompleterCommands(commands, editorTracker, manager, translator) {
        const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__.nullTranslator).load('jupyterlab');
        commands.addCommand(CommandIDs.invokeCompleter, {
            label: trans.__('Display the completion helper.'),
            execute: () => {
                const id = editorTracker.currentWidget && editorTracker.currentWidget.id;
                if (id) {
                    return manager.invoke(id);
                }
            }
        });
        commands.addCommand(CommandIDs.selectCompleter, {
            label: trans.__('Select the completion suggestion.'),
            execute: () => {
                const id = editorTracker.currentWidget && editorTracker.currentWidget.id;
                if (id) {
                    return manager.select(id);
                }
            }
        });
        commands.addKeyBinding({
            command: CommandIDs.selectCompleter,
            keys: ['Enter'],
            selector: '.jp-FileEditor .jp-mod-completer-active'
        });
    }
    Commands.addCompleterCommands = addCompleterCommands;
    /**
     * Helper function to check if there is a text selection in the editor
     */
    function isSelected(editor) {
        const selectionObj = editor.getSelection();
        const { start, end } = selectionObj;
        const selected = start.column !== end.column || start.line !== end.line;
        return selected;
    }
    /**
     * Helper function to get text selection from the editor
     */
    function getTextSelection(editor) {
        const selectionObj = editor.getSelection();
        const start = editor.getOffsetAt(selectionObj.start);
        const end = editor.getOffsetAt(selectionObj.end);
        const text = editor.model.value.text.substring(start, end);
        return text;
    }
    /**
     * Function to create a new untitled text file, given the current working directory.
     */
    async function createNew(commands, cwd, ext = 'txt') {
        const model = await commands.execute('docmanager:new-untitled', {
            path: cwd,
            type: 'file',
            ext
        });
        if (model != undefined) {
            const widget = (await commands.execute('docmanager:open', {
                path: model.path,
                factory: FACTORY
            }));
            widget.isUntitled = true;
            return widget;
        }
    }
    /**
     * Wrapper function for adding the default launcher items for File Editor
     */
    function addLauncherItems(launcher, trans) {
        addCreateNewToLauncher(launcher, trans);
        addCreateNewMarkdownToLauncher(launcher, trans);
    }
    Commands.addLauncherItems = addLauncherItems;
    /**
     * Add Create New Text File to the Launcher
     */
    function addCreateNewToLauncher(launcher, trans) {
        launcher.add({
            command: CommandIDs.createNew,
            category: trans.__('Other'),
            rank: 1
        });
    }
    Commands.addCreateNewToLauncher = addCreateNewToLauncher;
    /**
     * Add Create New Markdown to the Launcher
     */
    function addCreateNewMarkdownToLauncher(launcher, trans) {
        launcher.add({
            command: CommandIDs.createNewMarkdown,
            category: trans.__('Other'),
            rank: 2
        });
    }
    Commands.addCreateNewMarkdownToLauncher = addCreateNewMarkdownToLauncher;
    /**
     * Add ___ File items to the Launcher for common file types associated with available kernels
     */
    function addKernelLanguageLauncherItems(launcher, trans, availableKernelFileTypes) {
        for (let ext of availableKernelFileTypes) {
            launcher.add({
                command: CommandIDs.createNew,
                category: trans.__('Other'),
                rank: 3,
                args: ext
            });
        }
    }
    Commands.addKernelLanguageLauncherItems = addKernelLanguageLauncherItems;
    /**
     * Wrapper function for adding the default items to the File Editor palette
     */
    function addPaletteItems(palette, trans) {
        addChangeTabsCommandsToPalette(palette, trans);
        addCreateNewCommandToPalette(palette, trans);
        addCreateNewMarkdownCommandToPalette(palette, trans);
        addChangeFontSizeCommandsToPalette(palette, trans);
    }
    Commands.addPaletteItems = addPaletteItems;
    /**
     * Add commands to change the tab indentation to the File Editor palette
     */
    function addChangeTabsCommandsToPalette(palette, trans) {
        const paletteCategory = trans.__('Text Editor');
        const args = {
            insertSpaces: false,
            size: 4
        };
        const command = CommandIDs.changeTabs;
        palette.addItem({ command, args, category: paletteCategory });
        for (const size of [1, 2, 4, 8]) {
            const args = {
                insertSpaces: true,
                size
            };
            palette.addItem({ command, args, category: paletteCategory });
        }
    }
    Commands.addChangeTabsCommandsToPalette = addChangeTabsCommandsToPalette;
    /**
     * Add a Create New File command to the File Editor palette
     */
    function addCreateNewCommandToPalette(palette, trans) {
        const paletteCategory = trans.__('Text Editor');
        palette.addItem({
            command: CommandIDs.createNew,
            args: { isPalette: true },
            category: paletteCategory
        });
    }
    Commands.addCreateNewCommandToPalette = addCreateNewCommandToPalette;
    /**
     * Add a Create New Markdown command to the File Editor palette
     */
    function addCreateNewMarkdownCommandToPalette(palette, trans) {
        const paletteCategory = trans.__('Text Editor');
        palette.addItem({
            command: CommandIDs.createNewMarkdown,
            args: { isPalette: true },
            category: paletteCategory
        });
    }
    Commands.addCreateNewMarkdownCommandToPalette = addCreateNewMarkdownCommandToPalette;
    /**
     * Add commands to change the font size to the File Editor palette
     */
    function addChangeFontSizeCommandsToPalette(palette, trans) {
        const paletteCategory = trans.__('Text Editor');
        const command = CommandIDs.changeFontSize;
        let args = { delta: 1 };
        palette.addItem({ command, args, category: paletteCategory });
        args = { delta: -1 };
        palette.addItem({ command, args, category: paletteCategory });
    }
    Commands.addChangeFontSizeCommandsToPalette = addChangeFontSizeCommandsToPalette;
    /**
     * Add New ___ File commands to the File Editor palette for common file types associated with available kernels
     */
    function addKernelLanguagePaletteItems(palette, trans, availableKernelFileTypes) {
        const paletteCategory = trans.__('Text Editor');
        for (let ext of availableKernelFileTypes) {
            palette.addItem({
                command: CommandIDs.createNew,
                args: Object.assign(Object.assign({}, ext), { isPalette: true }),
                category: paletteCategory
            });
        }
    }
    Commands.addKernelLanguagePaletteItems = addKernelLanguagePaletteItems;
    /**
     * Wrapper function for adding the default menu items for File Editor
     */
    function addMenuItems(menu, tracker, consoleTracker, isEnabled) {
        // Add undo/redo hooks to the edit menu.
        menu.editMenu.undoers.redo.add({
            id: CommandIDs.redo,
            isEnabled
        });
        menu.editMenu.undoers.undo.add({
            id: CommandIDs.undo,
            isEnabled
        });
        // Add editor view options.
        menu.viewMenu.editorViewers.toggleLineNumbers.add({
            id: CommandIDs.currentLineNumbers,
            isEnabled
        });
        menu.viewMenu.editorViewers.toggleMatchBrackets.add({
            id: CommandIDs.currentMatchBrackets,
            isEnabled
        });
        menu.viewMenu.editorViewers.toggleWordWrap.add({
            id: CommandIDs.currentLineWrap,
            isEnabled
        });
        // Add a console creator the the file menu.
        menu.fileMenu.consoleCreators.add({
            id: CommandIDs.createConsole,
            isEnabled
        });
        // Add a code runner to the run menu.
        if (consoleTracker) {
            addCodeRunnersToRunMenu(menu, consoleTracker);
        }
    }
    Commands.addMenuItems = addMenuItems;
    /**
     * Add Create New ___ File commands to the File menu for common file types associated with available kernels
     */
    function addKernelLanguageMenuItems(menu, availableKernelFileTypes) {
        for (let ext of availableKernelFileTypes) {
            menu.fileMenu.newMenu.addItem({
                command: CommandIDs.createNew,
                args: ext,
                rank: 31
            });
        }
    }
    Commands.addKernelLanguageMenuItems = addKernelLanguageMenuItems;
    /**
     * Add a File Editor code runner to the Run menu
     */
    function addCodeRunnersToRunMenu(menu, consoleTracker) {
        const isEnabled = (current) => current.context &&
            !!consoleTracker.find(widget => { var _a; return ((_a = widget.sessionContext.session) === null || _a === void 0 ? void 0 : _a.path) === current.context.path; });
        menu.runMenu.codeRunners.restart.add({
            id: CommandIDs.restartConsole,
            isEnabled
        });
        menu.runMenu.codeRunners.run.add({
            id: CommandIDs.runCode,
            isEnabled
        });
        menu.runMenu.codeRunners.runAll.add({
            id: CommandIDs.runAllCode,
            isEnabled
        });
    }
    Commands.addCodeRunnersToRunMenu = addCodeRunnersToRunMenu;
    function addOpenCodeViewerCommand(app, editorServices, tracker, trans) {
        const openCodeViewer = async (args) => {
            var _a;
            const func = editorServices.factoryService.newDocumentEditor;
            const factory = options => {
                return func(options);
            };
            // Derive mimetype from extension
            let mimetype = args.mimeType;
            if (!mimetype && args.extension) {
                mimetype = editorServices.mimeTypeService.getMimeTypeByFilePath(`temp.${args.extension.replace(/\\.$/, '')}`);
            }
            const widget = _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_1__.CodeViewerWidget.createCodeViewer({
                factory,
                content: args.content,
                mimeType: mimetype
            });
            widget.title.label = args.label || trans.__('Code Viewer');
            widget.title.caption = widget.title.label;
            // Get the fileType based on the mimetype to determine the icon
            const fileType = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_5__.toArray)(app.docRegistry.fileTypes()).find(fileType => {
                return mimetype ? fileType.mimeTypes.includes(mimetype) : undefined;
            });
            widget.title.icon = (_a = fileType === null || fileType === void 0 ? void 0 : fileType.icon) !== null && _a !== void 0 ? _a : _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.textEditorIcon;
            if (args.widgetId) {
                widget.id = args.widgetId;
            }
            const main = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.MainAreaWidget({ content: widget });
            await tracker.add(main);
            app.shell.add(main, 'main');
            return widget;
        };
        app.commands.addCommand(CommandIDs.openCodeViewer, {
            label: trans.__('Open Code Viewer'),
            execute: (args) => {
                return openCodeViewer(args);
            }
        });
    }
    Commands.addOpenCodeViewerCommand = addOpenCodeViewerCommand;
})(Commands || (Commands = {}));


/***/ }),

/***/ "../../packages/fileeditor-extension/lib/index.js":
/*!********************************************************!*\
  !*** ../../packages/fileeditor-extension/lib/index.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Commands": () => (/* reexport safe */ _commands__WEBPACK_IMPORTED_MODULE_17__.Commands),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__),
/* harmony export */   "tabSpaceStatus": () => (/* binding */ tabSpaceStatus)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/codeeditor */ "webpack/sharing/consume/default/@jupyterlab/codeeditor/@jupyterlab/codeeditor");
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/completer */ "webpack/sharing/consume/default/@jupyterlab/completer/@jupyterlab/completer");
/* harmony import */ var _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_completer__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/console */ "webpack/sharing/consume/default/@jupyterlab/console/@jupyterlab/console");
/* harmony import */ var _jupyterlab_console__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/documentsearch */ "webpack/sharing/consume/default/@jupyterlab/documentsearch/@jupyterlab/documentsearch");
/* harmony import */ var _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/fileeditor */ "webpack/sharing/consume/default/@jupyterlab/fileeditor/@jupyterlab/fileeditor");
/* harmony import */ var _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @jupyterlab/lsp */ "webpack/sharing/consume/default/@jupyterlab/lsp/@jupyterlab/lsp");
/* harmony import */ var _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @jupyterlab/mainmenu */ "webpack/sharing/consume/default/@jupyterlab/mainmenu/@jupyterlab/mainmenu");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_12__);
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @jupyterlab/toc */ "webpack/sharing/consume/default/@jupyterlab/toc/@jupyterlab/toc");
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_13___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_toc__WEBPACK_IMPORTED_MODULE_13__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_14___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_14__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_15___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_15__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_16___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_16__);
/* harmony import */ var _commands__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! ./commands */ "../../packages/fileeditor-extension/lib/commands.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module fileeditor-extension
 */



















/**
 * The editor tracker extension.
 */
const plugin = {
    activate,
    id: '@jupyterlab/fileeditor-extension:plugin',
    requires: [
        _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__.IEditorServices,
        _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_6__.IFileBrowserFactory,
        _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_11__.ISettingRegistry,
        _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_14__.ITranslator
    ],
    optional: [
        _jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__.IConsoleTracker,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette,
        _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_8__.ILauncher,
        _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_10__.IMainMenu,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ISessionContextDialogs,
        _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_13__.ITableOfContentsRegistry,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IToolbarWidgetRegistry
    ],
    provides: _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.IEditorTracker,
    autoStart: true
};
/**
 * A plugin that provides a status item allowing the user to
 * switch tabs vs spaces and tab widths for text editors.
 */
const tabSpaceStatus = {
    id: '@jupyterlab/fileeditor-extension:tab-space-status',
    autoStart: true,
    requires: [_jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.IEditorTracker, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_11__.ISettingRegistry, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_14__.ITranslator],
    optional: [_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_12__.IStatusBar],
    activate: (app, editorTracker, settingRegistry, translator, statusBar) => {
        const trans = translator.load('jupyterlab');
        if (!statusBar) {
            // Automatically disable if statusbar missing
            return;
        }
        // Create a menu for switching tabs vs spaces.
        const menu = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_16__.Menu({ commands: app.commands });
        const command = 'fileeditor:change-tabs';
        const { shell } = app;
        const args = {
            insertSpaces: false,
            size: 4,
            name: trans.__('Indent with Tab')
        };
        menu.addItem({ command, args });
        for (const size of [1, 2, 4, 8]) {
            const args = {
                insertSpaces: true,
                size,
                name: trans._n('Spaces: %1', 'Spaces: %1', size)
            };
            menu.addItem({ command, args });
        }
        // Create the status item.
        const item = new _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.TabSpaceStatus({ menu, translator });
        // Keep a reference to the code editor config from the settings system.
        const updateSettings = (settings) => {
            item.model.config = Object.assign(Object.assign({}, _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__.CodeEditor.defaultConfig), settings.get('editorConfig').composite);
        };
        void Promise.all([
            settingRegistry.load('@jupyterlab/fileeditor-extension:plugin'),
            app.restored
        ]).then(([settings]) => {
            updateSettings(settings);
            settings.changed.connect(updateSettings);
        });
        // Add the status item.
        statusBar.registerStatusItem('@jupyterlab/fileeditor-extension:tab-space-status', {
            item,
            align: 'right',
            rank: 1,
            isActive: () => {
                return (!!shell.currentWidget && editorTracker.has(shell.currentWidget));
            }
        });
    }
};
/**
 * Cursor position.
 */
const lineColStatus = {
    id: '@jupyterlab/fileeditor-extension:cursor-position',
    activate: (app, tracker, positionModel) => {
        positionModel.addEditorProvider((widget) => widget && tracker.has(widget)
            ? widget.content.editor
            : null);
    },
    requires: [_jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.IEditorTracker, _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__.IPositionModel],
    autoStart: true
};
const completerPlugin = {
    id: '@jupyterlab/fileeditor-extension:completer',
    requires: [_jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.IEditorTracker],
    optional: [_jupyterlab_completer__WEBPACK_IMPORTED_MODULE_3__.ICompletionProviderManager],
    activate: activateFileEditorCompleterService,
    autoStart: true
};
/**
 * A plugin to search file editors
 */
const searchProvider = {
    id: '@jupyterlab/fileeditor-extension:search',
    requires: [_jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_5__.ISearchProviderRegistry],
    autoStart: true,
    activate: (app, registry) => {
        registry.add('jp-fileeditorSearchProvider', _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.FileEditorSearchProvider);
    }
};
const languageServerPlugin = {
    id: '@jupyterlab/fileeditor-extension:language-server',
    requires: [
        _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.IEditorTracker,
        _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_9__.ILSPDocumentConnectionManager,
        _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_9__.ILSPFeatureManager,
        _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_9__.ILSPCodeExtractorsManager
    ],
    activate: activateFileEditorLanguageServer,
    autoStart: true
};
/**
 * Export the plugins as default.
 */
const plugins = [
    plugin,
    lineColStatus,
    completerPlugin,
    languageServerPlugin,
    searchProvider,
    tabSpaceStatus
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);
/**
 * Activate the editor tracker plugin.
 */
function activate(app, editorServices, browserFactory, settingRegistry, translator, consoleTracker, palette, launcher, menu, restorer, sessionDialogs, tocRegistry, toolbarRegistry) {
    const id = plugin.id;
    const trans = translator.load('jupyterlab');
    const namespace = 'editor';
    let toolbarFactory;
    if (toolbarRegistry) {
        toolbarFactory = (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.createToolbarFactory)(toolbarRegistry, settingRegistry, _commands__WEBPACK_IMPORTED_MODULE_17__.FACTORY, id, translator);
    }
    const factory = new _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.FileEditorFactory({
        editorServices,
        factoryOptions: {
            name: _commands__WEBPACK_IMPORTED_MODULE_17__.FACTORY,
            label: trans.__('Editor'),
            fileTypes: ['markdown', '*'],
            defaultFor: ['markdown', '*'],
            toolbarFactory,
            translator
        }
    });
    const { commands, restored, shell } = app;
    const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
        namespace
    });
    const isEnabled = () => tracker.currentWidget !== null &&
        tracker.currentWidget === shell.currentWidget;
    const commonLanguageFileTypeData = new Map([
        [
            'python',
            [
                {
                    fileExt: 'py',
                    iconName: 'ui-components:python',
                    launcherLabel: trans.__('Python File'),
                    paletteLabel: trans.__('New Python File'),
                    caption: trans.__('Create a new Python file')
                }
            ]
        ],
        [
            'julia',
            [
                {
                    fileExt: 'jl',
                    iconName: 'ui-components:julia',
                    launcherLabel: trans.__('Julia File'),
                    paletteLabel: trans.__('New Julia File'),
                    caption: trans.__('Create a new Julia file')
                }
            ]
        ],
        [
            'R',
            [
                {
                    fileExt: 'r',
                    iconName: 'ui-components:r-kernel',
                    launcherLabel: trans.__('R File'),
                    paletteLabel: trans.__('New R File'),
                    caption: trans.__('Create a new R file')
                }
            ]
        ]
    ]);
    // Use available kernels to determine which common file types should have 'Create New' options in the Launcher, File Editor palette, and File menu
    const getAvailableKernelFileTypes = async () => {
        var _a, _b;
        const specsManager = app.serviceManager.kernelspecs;
        await specsManager.ready;
        let fileTypes = new Set();
        const specs = (_b = (_a = specsManager.specs) === null || _a === void 0 ? void 0 : _a.kernelspecs) !== null && _b !== void 0 ? _b : {};
        Object.keys(specs).forEach(spec => {
            const specModel = specs[spec];
            if (specModel) {
                const exts = commonLanguageFileTypeData.get(specModel.language);
                exts === null || exts === void 0 ? void 0 : exts.forEach(ext => fileTypes.add(ext));
            }
        });
        return fileTypes;
    };
    // Handle state restoration.
    if (restorer) {
        void restorer.restore(tracker, {
            command: 'docmanager:open',
            args: widget => ({ path: widget.context.path, factory: _commands__WEBPACK_IMPORTED_MODULE_17__.FACTORY }),
            name: widget => widget.context.path
        });
    }
    // Add a console creator to the File menu
    // Fetch the initial state of the settings.
    Promise.all([settingRegistry.load(id), restored])
        .then(([settings]) => {
        _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.updateSettings(settings, commands);
        _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.updateTracker(tracker);
        settings.changed.connect(() => {
            _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.updateSettings(settings, commands);
            _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.updateTracker(tracker);
        });
    })
        .catch((reason) => {
        console.error(reason.message);
        _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.updateTracker(tracker);
    });
    factory.widgetCreated.connect((sender, widget) => {
        // Notify the widget tracker if restore data needs to update.
        widget.context.pathChanged.connect(() => {
            void tracker.save(widget);
        });
        void tracker.add(widget);
        _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.updateWidget(widget.content);
    });
    app.docRegistry.addWidgetFactory(factory);
    // Handle the settings of new widgets.
    tracker.widgetAdded.connect((sender, widget) => {
        _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.updateWidget(widget.content);
    });
    _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.addCommands(commands, settingRegistry, trans, id, isEnabled, tracker, browserFactory, consoleTracker, sessionDialogs);
    const codeViewerTracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
        namespace: 'codeviewer'
    });
    // Handle state restoration for code viewers
    if (restorer) {
        void restorer.restore(codeViewerTracker, {
            command: _commands__WEBPACK_IMPORTED_MODULE_17__.CommandIDs.openCodeViewer,
            args: widget => ({
                content: widget.content.content,
                label: widget.content.title.label,
                mimeType: widget.content.mimeType,
                widgetId: widget.content.id
            }),
            name: widget => widget.content.id
        });
    }
    _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.addOpenCodeViewerCommand(app, editorServices, codeViewerTracker, trans);
    // Add a launcher item if the launcher is available.
    if (launcher) {
        _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.addLauncherItems(launcher, trans);
    }
    if (palette) {
        _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.addPaletteItems(palette, trans);
    }
    if (menu) {
        _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.addMenuItems(menu, tracker, consoleTracker, isEnabled);
    }
    getAvailableKernelFileTypes()
        .then(availableKernelFileTypes => {
        if (launcher) {
            _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.addKernelLanguageLauncherItems(launcher, trans, availableKernelFileTypes);
        }
        if (palette) {
            _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.addKernelLanguagePaletteItems(palette, trans, availableKernelFileTypes);
        }
        if (menu) {
            _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.addKernelLanguageMenuItems(menu, availableKernelFileTypes);
        }
    })
        .catch((reason) => {
        console.error(reason.message);
    });
    if (tocRegistry) {
        tocRegistry.add(new _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.LaTeXTableOfContentsFactory(tracker));
        tocRegistry.add(new _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.MarkdownTableOfContentsFactory(tracker));
        tocRegistry.add(new _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.PythonTableOfContentsFactory(tracker));
    }
    return tracker;
}
/**
 * Activate the completer service for file editor.
 */
function activateFileEditorCompleterService(app, editorTracker, manager, translator) {
    if (!manager) {
        return;
    }
    _commands__WEBPACK_IMPORTED_MODULE_17__.Commands.addCompleterCommands(app.commands, editorTracker, manager, translator);
    const sessionManager = app.serviceManager.sessions;
    const _activeSessions = new Map();
    const updateCompleter = async (_, widget) => {
        const completerContext = {
            editor: widget.content.editor,
            widget
        };
        await manager.updateCompleter(completerContext);
        const onRunningChanged = (_, models) => {
            const oldSession = _activeSessions.get(widget.id);
            // Search for a matching path.
            const model = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_15__.find)(models, m => m.path === widget.context.path);
            if (model) {
                // If there is a matching path, but it is the same
                // session as we previously had, do nothing.
                if (oldSession && oldSession.id === model.id) {
                    return;
                }
                // Otherwise, dispose of the old session and reset to
                // a new CompletionConnector.
                if (oldSession) {
                    _activeSessions.delete(widget.id);
                    oldSession.dispose();
                }
                const session = sessionManager.connectTo({ model });
                const newCompleterContext = {
                    editor: widget.content.editor,
                    widget,
                    session
                };
                manager.updateCompleter(newCompleterContext).catch(console.error);
                _activeSessions.set(widget.id, session);
            }
            else {
                // If we didn't find a match, make sure
                // the connector is the contextConnector and
                // dispose of any previous connection.
                if (oldSession) {
                    _activeSessions.delete(widget.id);
                    oldSession.dispose();
                }
            }
        };
        onRunningChanged(sessionManager, (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_15__.toArray)(sessionManager.running()));
        sessionManager.runningChanged.connect(onRunningChanged);
        widget.disposed.connect(() => {
            sessionManager.runningChanged.disconnect(onRunningChanged);
            const session = _activeSessions.get(widget.id);
            if (session) {
                _activeSessions.delete(widget.id);
                session.dispose();
            }
        });
    };
    editorTracker.widgetAdded.connect(updateCompleter);
    manager.activeProvidersChanged.connect(() => {
        editorTracker.forEach(editorWidget => {
            updateCompleter(editorTracker, editorWidget).catch(console.error);
        });
    });
}
function activateFileEditorLanguageServer(app, editors, connectionManager, featureManager, extractorManager) {
    editors.widgetAdded.connect(async (_, editor) => {
        const adapter = new _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.FileEditorAdapter(editor, {
            connectionManager,
            featureManager,
            foreignCodeExtractorsManager: extractorManager,
            docRegistry: app.docRegistry
        });
        connectionManager.registerAdapter(editor.context.path, adapter);
    });
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfZmlsZWVkaXRvci1leHRlbnNpb25fbGliX2luZGV4X2pzLjAxNzUzMDQzMGExM2I3YTRmMzA3LmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQVU3QjtBQUtFO0FBSW9DO0FBV25DO0FBV0U7QUFDUztBQU9LO0FBRWpELE1BQU0sMkJBQTJCLEdBQUcsc0NBQXNDLENBQUM7QUFDM0UsTUFBTSwwQkFBMEIsR0FBRyxxQ0FBcUMsQ0FBQztBQUd6RTs7R0FFRztBQUNJLElBQVUsVUFBVSxDQXdEMUI7QUF4REQsV0FBaUIsVUFBVTtJQUNaLG9CQUFTLEdBQUcsdUJBQXVCLENBQUM7SUFFcEMsNEJBQWlCLEdBQUcscUNBQXFDLENBQUM7SUFFMUQseUJBQWMsR0FBRyw2QkFBNkIsQ0FBQztJQUUvQyxzQkFBVyxHQUFHLGdDQUFnQyxDQUFDO0lBRS9DLDZCQUFrQixHQUFHLHdDQUF3QyxDQUFDO0lBRTlELG1CQUFRLEdBQUcsNkJBQTZCLENBQUM7SUFFekMsMEJBQWUsR0FBRyxxQ0FBcUMsQ0FBQztJQUV4RCxxQkFBVSxHQUFHLHdCQUF3QixDQUFDO0lBRXRDLHdCQUFhLEdBQUcsa0NBQWtDLENBQUM7SUFFbkQsK0JBQW9CLEdBQy9CLDBDQUEwQyxDQUFDO0lBRWhDLDhCQUFtQixHQUFHLHdDQUF3QyxDQUFDO0lBRS9ELHVDQUE0QixHQUN2QyxrREFBa0QsQ0FBQztJQUV4Qyx3QkFBYSxHQUFHLDJCQUEyQixDQUFDO0lBRTVDLDJCQUFnQixHQUFHLDhCQUE4QixDQUFDO0lBRWxELHlCQUFjLEdBQUcsNEJBQTRCLENBQUM7SUFFOUMsa0JBQU8sR0FBRyxxQkFBcUIsQ0FBQztJQUVoQyxxQkFBVSxHQUFHLG9CQUFvQixDQUFDO0lBRWxDLDBCQUFlLEdBQUcsNkJBQTZCLENBQUM7SUFFaEQsZUFBSSxHQUFHLGlCQUFpQixDQUFDO0lBRXpCLGVBQUksR0FBRyxpQkFBaUIsQ0FBQztJQUV6QixjQUFHLEdBQUcsZ0JBQWdCLENBQUM7SUFFdkIsZUFBSSxHQUFHLGlCQUFpQixDQUFDO0lBRXpCLGdCQUFLLEdBQUcsa0JBQWtCLENBQUM7SUFFM0Isb0JBQVMsR0FBRyx1QkFBdUIsQ0FBQztJQUVwQywwQkFBZSxHQUFHLHVCQUF1QixDQUFDO0lBRTFDLDBCQUFlLEdBQUcsdUJBQXVCLENBQUM7SUFFMUMseUJBQWMsR0FBRyxrQkFBa0IsQ0FBQztBQUNuRCxDQUFDLEVBeERnQixVQUFVLEtBQVYsVUFBVSxRQXdEMUI7QUFVRDs7R0FFRztBQUNJLE1BQU0sT0FBTyxHQUFHLFFBQVEsQ0FBQztBQUVoQyxNQUFNLFlBQVksR0FBRztJQUNuQixxQkFBcUI7SUFDckIsYUFBYTtJQUNiLGlCQUFpQjtJQUNqQixZQUFZO0lBQ1osVUFBVTtJQUNWLGNBQWM7SUFDZCxZQUFZO0lBQ1osYUFBYTtJQUNiLFVBQVU7SUFDVixlQUFlO0lBQ2YsVUFBVTtJQUNWLFFBQVE7SUFDUixtQkFBbUI7SUFDbkIsU0FBUztJQUNULGdCQUFnQjtDQUNqQixDQUFDO0FBRUYsU0FBUyxrQkFBa0IsQ0FBQyxNQUEwQjtJQUNwRCxNQUFNLGNBQWMscUJBQVEsTUFBTSxDQUFFLENBQUM7SUFDckMsNEVBQTRFO0lBQzVFLEtBQUssSUFBSSxDQUFDLElBQUksTUFBTSxDQUFDLElBQUksQ0FBQyxNQUFNLENBQUMsRUFBRTtRQUNqQyxJQUFJLENBQUMsWUFBWSxDQUFDLFFBQVEsQ0FBQyxDQUFDLENBQUMsRUFBRTtZQUM3QixPQUFRLE1BQWMsQ0FBQyxDQUFDLENBQUMsQ0FBQztTQUMzQjtLQUNGO0lBQ0QsT0FBTyxjQUFjLENBQUM7QUFDeEIsQ0FBQztBQUVELElBQUksTUFBTSxHQUF1QixrQkFBa0IsQ0FBQyw0RUFBd0IsQ0FBQyxDQUFDO0FBRTlFOzs7R0FHRztBQUNJLElBQVUsUUFBUSxDQWdsQ3hCO0FBaGxDRCxXQUFpQixRQUFRO0lBQ3ZCOztPQUVHO0lBQ0gsU0FBUyx3QkFBd0IsQ0FDL0IsUUFBeUI7UUFLekIsT0FBTyxLQUFLLFVBQVUsYUFBYSxDQUNqQyxNQUFtQyxFQUNuQyxJQUFnQzs7WUFFaEMsTUFBTSxPQUFPLEdBQUcsSUFBSSxJQUFJLEVBQUUsQ0FBQztZQUMzQixNQUFNLE9BQU8sR0FBRyxNQUFNLFFBQVEsQ0FBQyxPQUFPLENBQUMsZ0JBQWdCLEVBQUU7Z0JBQ3ZELFFBQVEsRUFBRSxPQUFPLENBQUMsVUFBVSxDQUFDO2dCQUM3QixJQUFJLEVBQUUsWUFBTSxDQUFDLE9BQU8sQ0FBQyxhQUFhLDBDQUFFLElBQUk7Z0JBQ3hDLElBQUksRUFBRSxNQUFNLENBQUMsT0FBTyxDQUFDLElBQUk7Z0JBQ3pCLGlCQUFpQixFQUFFLE1BQU0sQ0FBQyxPQUFPLENBQUMsS0FBSyxDQUFDLHFCQUFxQjtnQkFDN0QsR0FBRyxFQUFFLE1BQU0sQ0FBQyxFQUFFO2dCQUNkLFVBQVUsRUFBRSxjQUFjO2FBQzNCLENBQUMsQ0FBQztZQUVILE1BQU0sQ0FBQyxPQUFPLENBQUMsV0FBVyxDQUFDLE9BQU8sQ0FBQyxDQUFDLE1BQU0sRUFBRSxLQUFLLEVBQUUsRUFBRTs7Z0JBQ25ELE9BQU8sQ0FBQyxPQUFPLENBQUMsT0FBTyxDQUFDLEtBQUssQ0FBQyxDQUFDO2dCQUMvQixPQUFPLENBQUMsT0FBTyxDQUFDLE9BQU8sQ0FBQyxZQUFNLENBQUMsT0FBTyxDQUFDLGFBQWEsMENBQUUsSUFBSSxDQUFDLENBQUM7WUFDOUQsQ0FBQyxDQUFDLENBQUM7UUFDTCxDQUFDLENBQUM7SUFDSixDQUFDO0lBRUQ7O09BRUc7SUFDSCxTQUFnQixjQUFjLENBQzVCLFFBQW9DLEVBQ3BDLFFBQXlCO1FBRXpCLE1BQU0sR0FBRyxrQkFBa0IsaUNBQ3RCLDRFQUF3QixHQUN2QixRQUFRLENBQUMsR0FBRyxDQUFDLGNBQWMsQ0FBQyxDQUFDLFNBQXdCLEVBQ3pELENBQUM7UUFFSCw2Q0FBNkM7UUFDN0MsUUFBUSxDQUFDLG9CQUFvQixFQUFFLENBQUM7SUFDbEMsQ0FBQztJQVhlLHVCQUFjLGlCQVc3QjtJQUVEOztPQUVHO0lBQ0gsU0FBZ0IsYUFBYSxDQUMzQixPQUFtRDtRQUVuRCxPQUFPLENBQUMsT0FBTyxDQUFDLE1BQU0sQ0FBQyxFQUFFO1lBQ3ZCLFlBQVksQ0FBQyxNQUFNLENBQUMsT0FBTyxDQUFDLENBQUM7UUFDL0IsQ0FBQyxDQUFDLENBQUM7SUFDTCxDQUFDO0lBTmUsc0JBQWEsZ0JBTTVCO0lBRUQ7OztPQUdHO0lBQ0gsU0FBZ0IsWUFBWSxDQUFDLE1BQWtCO1FBQzdDLE1BQU0sTUFBTSxHQUFHLE1BQU0sQ0FBQyxNQUFNLENBQUM7UUFDN0IsTUFBTSxDQUFDLFVBQVUsbUJBQU0sTUFBTSxFQUFHLENBQUM7SUFDbkMsQ0FBQztJQUhlLHFCQUFZLGVBRzNCO0lBRUQ7O09BRUc7SUFDSCxTQUFnQixXQUFXLENBQ3pCLFFBQXlCLEVBQ3pCLGVBQWlDLEVBQ2pDLEtBQXdCLEVBQ3hCLEVBQVUsRUFDVixTQUF3QixFQUN4QixPQUFtRCxFQUNuRCxjQUFtQyxFQUNuQyxjQUFzQyxFQUN0QyxjQUE2QztRQUU3Qzs7V0FFRztRQUNILFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLGNBQWMsRUFBRTtZQUM3QyxPQUFPLEVBQUUsSUFBSSxDQUFDLEVBQUU7Z0JBQ2QsTUFBTSxLQUFLLEdBQUcsTUFBTSxDQUFDLElBQUksQ0FBQyxPQUFPLENBQUMsQ0FBQyxDQUFDO2dCQUNwQyxJQUFJLE1BQU0sQ0FBQyxLQUFLLENBQUMsS0FBSyxDQUFDLEVBQUU7b0JBQ3ZCLE9BQU8sQ0FBQyxLQUFLLENBQ1gsR0FBRyxVQUFVLENBQUMsY0FBYyw4QkFBOEIsQ0FDM0QsQ0FBQztvQkFDRixPQUFPO2lCQUNSO2dCQUNELE1BQU0sS0FBSyxHQUFHLE1BQU0sQ0FBQyxnQkFBZ0IsQ0FBQyxRQUFRLENBQUMsZUFBZSxDQUFDLENBQUM7Z0JBQ2hFLE1BQU0sT0FBTyxHQUFHLFFBQVEsQ0FDdEIsS0FBSyxDQUFDLGdCQUFnQixDQUFDLHFCQUFxQixDQUFDLEVBQzdDLEVBQUUsQ0FDSCxDQUFDO2dCQUNGLE1BQU0sV0FBVyxHQUFHLE1BQU0sQ0FBQyxRQUFRLElBQUksT0FBTyxDQUFDO2dCQUMvQyxNQUFNLENBQUMsUUFBUSxHQUFHLFdBQVcsR0FBRyxLQUFLLENBQUM7Z0JBQ3RDLE9BQU8sZUFBZTtxQkFDbkIsR0FBRyxDQUFDLEVBQUUsRUFBRSxjQUFjLEVBQUUsTUFBK0IsQ0FBQztxQkFDeEQsS0FBSyxDQUFDLENBQUMsTUFBYSxFQUFFLEVBQUU7b0JBQ3ZCLE9BQU8sQ0FBQyxLQUFLLENBQUMsaUJBQWlCLEVBQUUsS0FBSyxNQUFNLENBQUMsT0FBTyxFQUFFLENBQUMsQ0FBQztnQkFDMUQsQ0FBQyxDQUFDLENBQUM7WUFDUCxDQUFDO1lBQ0QsS0FBSyxFQUFFLElBQUksQ0FBQyxFQUFFOztnQkFDWixJQUFJLENBQUMsVUFBSSxDQUFDLEtBQUssbUNBQUksQ0FBQyxDQUFDLEdBQUcsQ0FBQyxFQUFFO29CQUN6QixPQUFPLElBQUksQ0FBQyxNQUFNO3dCQUNoQixDQUFDLENBQUMsS0FBSyxDQUFDLEVBQUUsQ0FBQyxnQ0FBZ0MsQ0FBQzt3QkFDNUMsQ0FBQyxDQUFDLEtBQUssQ0FBQyxFQUFFLENBQUMsb0JBQW9CLENBQUMsQ0FBQztpQkFDcEM7cUJBQU07b0JBQ0wsT0FBTyxJQUFJLENBQUMsTUFBTTt3QkFDaEIsQ0FBQyxDQUFDLEtBQUssQ0FBQyxFQUFFLENBQUMsZ0NBQWdDLENBQUM7d0JBQzVDLENBQUMsQ0FBQyxLQUFLLENBQUMsRUFBRSxDQUFDLG9CQUFvQixDQUFDLENBQUM7aUJBQ3BDO1lBQ0gsQ0FBQztTQUNGLENBQUMsQ0FBQztRQUVIOztXQUVHO1FBQ0gsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsV0FBVyxFQUFFO1lBQzFDLE9BQU8sRUFBRSxHQUFHLEVBQUU7Z0JBQ1osTUFBTSxDQUFDLFdBQVcsR0FBRyxDQUFDLE1BQU0sQ0FBQyxXQUFXLENBQUM7Z0JBQ3pDLE9BQU8sZUFBZTtxQkFDbkIsR0FBRyxDQUFDLEVBQUUsRUFBRSxjQUFjLEVBQUUsTUFBK0IsQ0FBQztxQkFDeEQsS0FBSyxDQUFDLENBQUMsTUFBYSxFQUFFLEVBQUU7b0JBQ3ZCLE9BQU8sQ0FBQyxLQUFLLENBQUMsaUJBQWlCLEVBQUUsS0FBSyxNQUFNLENBQUMsT0FBTyxFQUFFLENBQUMsQ0FBQztnQkFDMUQsQ0FBQyxDQUFDLENBQUM7WUFDUCxDQUFDO1lBQ0QsU0FBUztZQUNULFNBQVMsRUFBRSxHQUFHLEVBQUUsQ0FBQyxNQUFNLENBQUMsV0FBVztZQUNuQyxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxjQUFjLENBQUM7U0FDaEMsQ0FBQyxDQUFDO1FBRUgsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsa0JBQWtCLEVBQUU7WUFDakQsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsbUJBQW1CLENBQUM7WUFDcEMsT0FBTyxFQUFFLEdBQUcsRUFBRTtnQkFDWixNQUFNLE1BQU0sR0FBRyxPQUFPLENBQUMsYUFBYSxDQUFDO2dCQUNyQyxJQUFJLENBQUMsTUFBTSxFQUFFO29CQUNYLE9BQU87aUJBQ1I7Z0JBQ0QsTUFBTSxXQUFXLEdBQUcsQ0FBQyxNQUFNLENBQUMsT0FBTyxDQUFDLE1BQU0sQ0FBQyxTQUFTLENBQUMsYUFBYSxDQUFDLENBQUM7Z0JBQ3BFLE1BQU0sQ0FBQyxPQUFPLENBQUMsTUFBTSxDQUFDLFNBQVMsQ0FBQyxhQUFhLEVBQUUsV0FBVyxDQUFDLENBQUM7WUFDOUQsQ0FBQztZQUNELFNBQVM7WUFDVCxTQUFTLEVBQUUsR0FBRyxFQUFFOztnQkFDZCxNQUFNLE1BQU0sR0FBRyxPQUFPLENBQUMsYUFBYSxDQUFDO2dCQUNyQyxPQUFPLFlBQU0sYUFBTixNQUFNLHVCQUFOLE1BQU0sQ0FBRSxPQUFPLENBQUMsTUFBTSxDQUFDLFNBQVMsQ0FBQyxhQUFhLENBQUMsbUNBQUksS0FBSyxDQUFDO1lBQ2xFLENBQUM7U0FDRixDQUFDLENBQUM7UUFFSDs7V0FFRztRQUNILFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLFFBQVEsRUFBRTtZQUN2QyxPQUFPLEVBQUUsSUFBSSxDQUFDLEVBQUU7Z0JBQ2QsTUFBTSxDQUFDLFFBQVEsR0FBSSxJQUFJLENBQUMsTUFBTSxDQUFrQixJQUFJLEtBQUssQ0FBQztnQkFDMUQsT0FBTyxlQUFlO3FCQUNuQixHQUFHLENBQUMsRUFBRSxFQUFFLGNBQWMsRUFBRSxNQUErQixDQUFDO3FCQUN4RCxLQUFLLENBQUMsQ0FBQyxNQUFhLEVBQUUsRUFBRTtvQkFDdkIsT0FBTyxDQUFDLEtBQUssQ0FBQyxpQkFBaUIsRUFBRSxLQUFLLE1BQU0sQ0FBQyxPQUFPLEVBQUUsQ0FBQyxDQUFDO2dCQUMxRCxDQUFDLENBQUMsQ0FBQztZQUNQLENBQUM7WUFDRCxTQUFTO1lBQ1QsU0FBUyxFQUFFLElBQUksQ0FBQyxFQUFFO2dCQUNoQixNQUFNLFFBQVEsR0FBSSxJQUFJLENBQUMsTUFBTSxDQUFrQixJQUFJLEtBQUssQ0FBQztnQkFDekQsT0FBTyxNQUFNLENBQUMsUUFBUSxLQUFLLFFBQVEsQ0FBQztZQUN0QyxDQUFDO1lBQ0QsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsV0FBVyxDQUFDO1NBQzdCLENBQUMsQ0FBQztRQUVILFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLGVBQWUsRUFBRTtZQUM5QyxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxZQUFZLENBQUM7WUFDN0IsT0FBTyxFQUFFLEdBQUcsRUFBRTtnQkFDWixNQUFNLE1BQU0sR0FBRyxPQUFPLENBQUMsYUFBYSxDQUFDO2dCQUNyQyxJQUFJLENBQUMsTUFBTSxFQUFFO29CQUNYLE9BQU87aUJBQ1I7Z0JBQ0QsTUFBTSxRQUFRLEdBQUcsTUFBTSxDQUFDLE9BQU8sQ0FBQyxNQUFNLENBQUMsU0FBUyxDQUFDLFVBQVUsQ0FBQyxDQUFDO2dCQUM3RCxNQUFNLFFBQVEsR0FBRyxRQUFRLEtBQUssS0FBSyxDQUFDLENBQUMsQ0FBQyxJQUFJLENBQUMsQ0FBQyxDQUFDLEtBQUssQ0FBQztnQkFDbkQsTUFBTSxDQUFDLE9BQU8sQ0FBQyxNQUFNLENBQUMsU0FBUyxDQUFDLFVBQVUsRUFBRSxRQUFRLENBQUMsQ0FBQztZQUN4RCxDQUFDO1lBQ0QsU0FBUztZQUNULFNBQVMsRUFBRSxHQUFHLEVBQUU7O2dCQUNkLE1BQU0sTUFBTSxHQUFHLE9BQU8sQ0FBQyxhQUFhLENBQUM7Z0JBQ3JDLE9BQU8sYUFBTSxhQUFOLE1BQU0sdUJBQU4sTUFBTSxDQUFFLE9BQU8sQ0FBQyxNQUFNLENBQUMsU0FBUyxDQUFDLFVBQVUsQ0FBQyxNQUFLLEtBQUssbUNBQUksS0FBSyxDQUFDO1lBQ3pFLENBQUM7U0FDRixDQUFDLENBQUM7UUFFSDs7V0FFRztRQUVILFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLFVBQVUsRUFBRTtZQUN6QyxLQUFLLEVBQUUsSUFBSSxDQUFDLEVBQUU7O2dCQUNaLElBQUksSUFBSSxDQUFDLFlBQVksRUFBRTtvQkFDckIsT0FBTyxLQUFLLENBQUMsRUFBRSxDQUNiLFlBQVksRUFDWixZQUFZLEVBQ1osTUFBQyxJQUFJLENBQUMsSUFBZSxtQ0FBSSxDQUFDLENBQzNCLENBQUM7aUJBQ0g7cUJBQU07b0JBQ0wsT0FBTyxLQUFLLENBQUMsRUFBRSxDQUFDLGlCQUFpQixDQUFDLENBQUM7aUJBQ3BDO1lBQ0gsQ0FBQztZQUNELE9BQU8sRUFBRSxJQUFJLENBQUMsRUFBRTtnQkFDZCxNQUFNLENBQUMsT0FBTyxHQUFJLElBQUksQ0FBQyxNQUFNLENBQVksSUFBSSxDQUFDLENBQUM7Z0JBQy9DLE1BQU0sQ0FBQyxZQUFZLEdBQUcsQ0FBQyxDQUFDLElBQUksQ0FBQyxjQUFjLENBQUMsQ0FBQztnQkFDN0MsT0FBTyxlQUFlO3FCQUNuQixHQUFHLENBQUMsRUFBRSxFQUFFLGNBQWMsRUFBRSxNQUErQixDQUFDO3FCQUN4RCxLQUFLLENBQUMsQ0FBQyxNQUFhLEVBQUUsRUFBRTtvQkFDdkIsT0FBTyxDQUFDLEtBQUssQ0FBQyxpQkFBaUIsRUFBRSxLQUFLLE1BQU0sQ0FBQyxPQUFPLEVBQUUsQ0FBQyxDQUFDO2dCQUMxRCxDQUFDLENBQUMsQ0FBQztZQUNQLENBQUM7WUFDRCxTQUFTLEVBQUUsSUFBSSxDQUFDLEVBQUU7Z0JBQ2hCLE1BQU0sWUFBWSxHQUFHLENBQUMsQ0FBQyxJQUFJLENBQUMsY0FBYyxDQUFDLENBQUM7Z0JBQzVDLE1BQU0sSUFBSSxHQUFJLElBQUksQ0FBQyxNQUFNLENBQVksSUFBSSxDQUFDLENBQUM7Z0JBQzNDLE9BQU8sTUFBTSxDQUFDLFlBQVksS0FBSyxZQUFZLElBQUksTUFBTSxDQUFDLE9BQU8sS0FBSyxJQUFJLENBQUM7WUFDekUsQ0FBQztTQUNGLENBQUMsQ0FBQztRQUVIOztXQUVHO1FBQ0gsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsYUFBYSxFQUFFO1lBQzVDLE9BQU8sRUFBRSxHQUFHLEVBQUU7Z0JBQ1osTUFBTSxDQUFDLGFBQWEsR0FBRyxDQUFDLE1BQU0sQ0FBQyxhQUFhLENBQUM7Z0JBQzdDLE9BQU8sZUFBZTtxQkFDbkIsR0FBRyxDQUFDLEVBQUUsRUFBRSxjQUFjLEVBQUUsTUFBK0IsQ0FBQztxQkFDeEQsS0FBSyxDQUFDLENBQUMsTUFBYSxFQUFFLEVBQUU7b0JBQ3ZCLE9BQU8sQ0FBQyxLQUFLLENBQUMsaUJBQWlCLEVBQUUsS0FBSyxNQUFNLENBQUMsT0FBTyxFQUFFLENBQUMsQ0FBQztnQkFDMUQsQ0FBQyxDQUFDLENBQUM7WUFDUCxDQUFDO1lBQ0QsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsZ0JBQWdCLENBQUM7WUFDakMsU0FBUztZQUNULFNBQVMsRUFBRSxHQUFHLEVBQUUsQ0FBQyxNQUFNLENBQUMsYUFBYTtTQUN0QyxDQUFDLENBQUM7UUFFSCxRQUFRLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyxvQkFBb0IsRUFBRTtZQUNuRCxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxnQkFBZ0IsQ0FBQztZQUNqQyxPQUFPLEVBQUUsR0FBRyxFQUFFO2dCQUNaLE1BQU0sTUFBTSxHQUFHLE9BQU8sQ0FBQyxhQUFhLENBQUM7Z0JBQ3JDLElBQUksQ0FBQyxNQUFNLEVBQUU7b0JBQ1gsT0FBTztpQkFDUjtnQkFDRCxNQUFNLGFBQWEsR0FBRyxDQUFDLE1BQU0sQ0FBQyxPQUFPLENBQUMsTUFBTSxDQUFDLFNBQVMsQ0FBQyxlQUFlLENBQUMsQ0FBQztnQkFDeEUsTUFBTSxDQUFDLE9BQU8sQ0FBQyxNQUFNLENBQUMsU0FBUyxDQUFDLGVBQWUsRUFBRSxhQUFhLENBQUMsQ0FBQztZQUNsRSxDQUFDO1lBQ0QsU0FBUztZQUNULFNBQVMsRUFBRSxHQUFHLEVBQUU7O2dCQUNkLE1BQU0sTUFBTSxHQUFHLE9BQU8sQ0FBQyxhQUFhLENBQUM7Z0JBQ3JDLE9BQU8sWUFBTSxhQUFOLE1BQU0sdUJBQU4sTUFBTSxDQUFFLE9BQU8sQ0FBQyxNQUFNLENBQUMsU0FBUyxDQUFDLGVBQWUsQ0FBQyxtQ0FBSSxLQUFLLENBQUM7WUFDcEUsQ0FBQztTQUNGLENBQUMsQ0FBQztRQUVIOztXQUVHO1FBQ0gsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsbUJBQW1CLEVBQUU7WUFDbEQsT0FBTyxFQUFFLElBQUksQ0FBQyxFQUFFOztnQkFDZCxNQUFNLENBQUMsbUJBQW1CLEdBQUcsQ0FBQyxDQUFDLENBQzdCLFVBQUksQ0FBQyxPQUFPLENBQUMsbUNBQUksQ0FBQyxNQUFNLENBQUMsbUJBQW1CLENBQzdDLENBQUM7Z0JBQ0YsT0FBTyxlQUFlO3FCQUNuQixHQUFHLENBQUMsRUFBRSxFQUFFLGNBQWMsRUFBRSxNQUErQixDQUFDO3FCQUN4RCxLQUFLLENBQUMsQ0FBQyxNQUFhLEVBQUUsRUFBRTtvQkFDdkIsT0FBTyxDQUFDLEtBQUssQ0FBQyxpQkFBaUIsRUFBRSxLQUFLLE1BQU0sQ0FBQyxPQUFPLEVBQUUsQ0FBQyxDQUFDO2dCQUMxRCxDQUFDLENBQUMsQ0FBQztZQUNQLENBQUM7WUFDRCxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxxQ0FBcUMsQ0FBQztZQUN0RCxTQUFTLEVBQUUsR0FBRyxFQUFFLENBQUMsTUFBTSxDQUFDLG1CQUFtQjtTQUM1QyxDQUFDLENBQUM7UUFFSCxRQUFRLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyw0QkFBNEIsRUFBRTtZQUMzRCxPQUFPLEVBQUUsR0FBRyxFQUFFO2dCQUNaLE1BQU0sVUFBVSxHQUNkLFFBQVEsQ0FBQyxTQUFTLENBQUMsVUFBVSxDQUFDLG1CQUFtQixDQUFDO29CQUNsRCxRQUFRLENBQUMsU0FBUyxDQUFDLDJCQUEyQixDQUFDO29CQUMvQyxRQUFRLENBQUMsU0FBUyxDQUFDLDBCQUEwQixDQUFDLENBQUM7Z0JBQ2pELG1FQUFtRTtnQkFDbkUsSUFBSSxVQUFVLEVBQUU7b0JBQ2QsS0FBSyxRQUFRLENBQUMsT0FBTyxDQUFDLFVBQVUsQ0FBQyxtQkFBbUIsRUFBRTt3QkFDcEQsS0FBSyxFQUFFLEtBQUs7cUJBQ2IsQ0FBQyxDQUFDO29CQUNILEtBQUssUUFBUSxDQUFDLE9BQU8sQ0FBQywyQkFBMkIsRUFBRSxFQUFFLEtBQUssRUFBRSxLQUFLLEVBQUUsQ0FBQyxDQUFDO29CQUNyRSxLQUFLLFFBQVEsQ0FBQyxPQUFPLENBQUMsMEJBQTBCLEVBQUUsRUFBRSxLQUFLLEVBQUUsS0FBSyxFQUFFLENBQUMsQ0FBQztpQkFDckU7cUJBQU07b0JBQ0wsNkJBQTZCO29CQUM3QixLQUFLLFFBQVEsQ0FBQyxPQUFPLENBQUMsVUFBVSxDQUFDLG1CQUFtQixFQUFFO3dCQUNwRCxLQUFLLEVBQUUsSUFBSTtxQkFDWixDQUFDLENBQUM7b0JBQ0gsS0FBSyxRQUFRLENBQUMsT0FBTyxDQUFDLDJCQUEyQixFQUFFLEVBQUUsS0FBSyxFQUFFLElBQUksRUFBRSxDQUFDLENBQUM7b0JBQ3BFLEtBQUssUUFBUSxDQUFDLE9BQU8sQ0FBQywwQkFBMEIsRUFBRSxFQUFFLEtBQUssRUFBRSxJQUFJLEVBQUUsQ0FBQyxDQUFDO2lCQUNwRTtZQUNILENBQUM7WUFDRCxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxxQkFBcUIsQ0FBQztZQUN0QyxTQUFTLEVBQUUsR0FBRyxFQUFFLENBQ2QsUUFBUSxDQUFDLFNBQVMsQ0FBQyxVQUFVLENBQUMsbUJBQW1CLENBQUM7Z0JBQ2xELFFBQVEsQ0FBQyxTQUFTLENBQUMsMkJBQTJCLENBQUM7Z0JBQy9DLFFBQVEsQ0FBQyxTQUFTLENBQUMsMEJBQTBCLENBQUM7U0FDakQsQ0FBQyxDQUFDO1FBRUg7O1dBRUc7UUFFSCxRQUFRLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyxnQkFBZ0IsRUFBRTtZQUMvQyxPQUFPLEVBQUUsSUFBSSxDQUFDLEVBQUU7O2dCQUNkLE1BQU0sSUFBSSxHQUFZLElBQUksQ0FBQyxNQUFNLENBQVksSUFBSSxFQUFFLENBQUM7Z0JBQ3BELE1BQU0sTUFBTSxHQUFHLE9BQU8sQ0FBQyxhQUFhLENBQUM7Z0JBQ3JDLElBQUksQ0FBQyxNQUFNLEVBQUU7b0JBQ1gsT0FBTztpQkFDUjtnQkFDRCxrQkFBTSxDQUFDLE9BQU8sQ0FBQyxNQUFNLEVBQUMsZ0JBQWdCLG1EQUFHLElBQUksQ0FBQyxDQUFDO1lBQ2pELENBQUM7WUFDRCxTQUFTO1lBQ1QsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsNkJBQTZCLENBQUM7U0FDL0MsQ0FBQyxDQUFDO1FBRUg7O1dBRUc7UUFDSCxRQUFRLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyxhQUFhLEVBQUU7WUFDNUMsT0FBTyxFQUFFLElBQUksQ0FBQyxFQUFFO2dCQUNkLE1BQU0sTUFBTSxHQUFHLE9BQU8sQ0FBQyxhQUFhLENBQUM7Z0JBRXJDLElBQUksQ0FBQyxNQUFNLEVBQUU7b0JBQ1gsT0FBTztpQkFDUjtnQkFFRCxPQUFPLHdCQUF3QixDQUFDLFFBQVEsQ0FBQyxDQUFDLE1BQU0sRUFBRSxJQUFJLENBQUMsQ0FBQztZQUMxRCxDQUFDO1lBQ0QsU0FBUztZQUNULElBQUksRUFBRSxrRUFBVztZQUNqQixLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQywyQkFBMkIsQ0FBQztTQUM3QyxDQUFDLENBQUM7UUFFSDs7V0FFRztRQUNILFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLGNBQWMsRUFBRTtZQUM3QyxPQUFPLEVBQUUsS0FBSyxJQUFJLEVBQUU7O2dCQUNsQixNQUFNLE9BQU8sR0FBRyxhQUFPLENBQUMsYUFBYSwwQ0FBRSxPQUFPLENBQUM7Z0JBRS9DLElBQUksQ0FBQyxPQUFPLElBQUksY0FBYyxLQUFLLElBQUksRUFBRTtvQkFDdkMsT0FBTztpQkFDUjtnQkFFRCxNQUFNLE1BQU0sR0FBRyxjQUFjLENBQUMsSUFBSSxDQUNoQyxNQUFNLENBQUMsRUFBRSxXQUFDLG9CQUFNLENBQUMsY0FBYyxDQUFDLE9BQU8sMENBQUUsSUFBSSxNQUFLLE9BQU8sQ0FBQyxPQUFPLENBQUMsSUFBSSxJQUN2RSxDQUFDO2dCQUNGLElBQUksTUFBTSxFQUFFO29CQUNWLE9BQU8sQ0FBQyxjQUFjLElBQUksdUVBQXFCLENBQUMsQ0FBQyxPQUFPLENBQ3RELE1BQU0sQ0FBQyxjQUFjLENBQ3RCLENBQUM7aUJBQ0g7WUFDSCxDQUFDO1lBQ0QsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsZ0JBQWdCLENBQUM7WUFDakMsU0FBUyxFQUFFLEdBQUcsRUFBRSxDQUFDLGNBQWMsS0FBSyxJQUFJLElBQUksU0FBUyxFQUFFO1NBQ3hELENBQUMsQ0FBQztRQUVIOztXQUVHO1FBQ0gsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsT0FBTyxFQUFFO1lBQ3RDLE9BQU8sRUFBRSxHQUFHLEVBQUU7O2dCQUNaLDJFQUEyRTtnQkFDM0UsTUFBTSxNQUFNLEdBQUcsYUFBTyxDQUFDLGFBQWEsMENBQUUsT0FBTyxDQUFDO2dCQUU5QyxJQUFJLENBQUMsTUFBTSxFQUFFO29CQUNYLE9BQU87aUJBQ1I7Z0JBRUQsSUFBSSxJQUFJLEdBQXVCLEVBQUUsQ0FBQztnQkFDbEMsTUFBTSxNQUFNLEdBQUcsTUFBTSxDQUFDLE1BQU0sQ0FBQztnQkFDN0IsTUFBTSxJQUFJLEdBQUcsTUFBTSxDQUFDLE9BQU8sQ0FBQyxJQUFJLENBQUM7Z0JBQ2pDLE1BQU0sU0FBUyxHQUFHLGtFQUFlLENBQUMsSUFBSSxDQUFDLENBQUM7Z0JBQ3hDLE1BQU0sU0FBUyxHQUFHLE1BQU0sQ0FBQyxZQUFZLEVBQUUsQ0FBQztnQkFDeEMsTUFBTSxFQUFFLEtBQUssRUFBRSxHQUFHLEVBQUUsR0FBRyxTQUFTLENBQUM7Z0JBQ2pDLElBQUksUUFBUSxHQUFHLEtBQUssQ0FBQyxNQUFNLEtBQUssR0FBRyxDQUFDLE1BQU0sSUFBSSxLQUFLLENBQUMsSUFBSSxLQUFLLEdBQUcsQ0FBQyxJQUFJLENBQUM7Z0JBRXRFLElBQUksUUFBUSxFQUFFO29CQUNaLHlDQUF5QztvQkFDekMsTUFBTSxLQUFLLEdBQUcsTUFBTSxDQUFDLFdBQVcsQ0FBQyxTQUFTLENBQUMsS0FBSyxDQUFDLENBQUM7b0JBQ2xELE1BQU0sR0FBRyxHQUFHLE1BQU0sQ0FBQyxXQUFXLENBQUMsU0FBUyxDQUFDLEdBQUcsQ0FBQyxDQUFDO29CQUU5QyxJQUFJLEdBQUcsTUFBTSxDQUFDLEtBQUssQ0FBQyxLQUFLLENBQUMsSUFBSSxDQUFDLFNBQVMsQ0FBQyxLQUFLLEVBQUUsR0FBRyxDQUFDLENBQUM7aUJBQ3REO3FCQUFNLElBQUksZ0ZBQTZCLENBQUMsU0FBUyxDQUFDLEVBQUU7b0JBQ25ELE1BQU0sRUFBRSxJQUFJLEVBQUUsR0FBRyxNQUFNLENBQUMsS0FBSyxDQUFDLEtBQUssQ0FBQztvQkFDcEMsTUFBTSxNQUFNLEdBQUcsNEZBQXlDLENBQUMsSUFBSSxDQUFDLENBQUM7b0JBRS9ELEtBQUssTUFBTSxLQUFLLElBQUksTUFBTSxFQUFFO3dCQUMxQixJQUFJLEtBQUssQ0FBQyxTQUFTLElBQUksS0FBSyxDQUFDLElBQUksSUFBSSxLQUFLLENBQUMsSUFBSSxJQUFJLEtBQUssQ0FBQyxPQUFPLEVBQUU7NEJBQ2hFLElBQUksR0FBRyxLQUFLLENBQUMsSUFBSSxDQUFDOzRCQUNsQixRQUFRLEdBQUcsSUFBSSxDQUFDOzRCQUNoQixNQUFNO3lCQUNQO3FCQUNGO2lCQUNGO2dCQUVELElBQUksQ0FBQyxRQUFRLEVBQUU7b0JBQ2IsOENBQThDO29CQUM5QyxJQUFJLEdBQUcsTUFBTSxDQUFDLE9BQU8sQ0FBQyxTQUFTLENBQUMsS0FBSyxDQUFDLElBQUksQ0FBQyxDQUFDO29CQUM1QyxNQUFNLE1BQU0sR0FBRyxNQUFNLENBQUMsaUJBQWlCLEVBQUUsQ0FBQztvQkFDMUMsSUFBSSxNQUFNLENBQUMsSUFBSSxHQUFHLENBQUMsS0FBSyxNQUFNLENBQUMsU0FBUyxFQUFFO3dCQUN4QyxNQUFNLElBQUksR0FBRyxNQUFNLENBQUMsS0FBSyxDQUFDLEtBQUssQ0FBQyxJQUFJLENBQUM7d0JBQ3JDLE1BQU0sQ0FBQyxLQUFLLENBQUMsS0FBSyxDQUFDLElBQUksR0FBRyxJQUFJLEdBQUcsSUFBSSxDQUFDO3FCQUN2QztvQkFDRCxNQUFNLENBQUMsaUJBQWlCLENBQUM7d0JBQ3ZCLElBQUksRUFBRSxNQUFNLENBQUMsSUFBSSxHQUFHLENBQUM7d0JBQ3JCLE1BQU0sRUFBRSxNQUFNLENBQUMsTUFBTTtxQkFDdEIsQ0FBQyxDQUFDO2lCQUNKO2dCQUVELE1BQU0sUUFBUSxHQUFHLEtBQUssQ0FBQztnQkFDdkIsSUFBSSxJQUFJLEVBQUU7b0JBQ1IsT0FBTyxRQUFRLENBQUMsT0FBTyxDQUFDLGdCQUFnQixFQUFFLEVBQUUsUUFBUSxFQUFFLElBQUksRUFBRSxJQUFJLEVBQUUsQ0FBQyxDQUFDO2lCQUNyRTtxQkFBTTtvQkFDTCxPQUFPLE9BQU8sQ0FBQyxPQUFPLENBQUMsS0FBSyxDQUFDLENBQUMsQ0FBQztpQkFDaEM7WUFDSCxDQUFDO1lBQ0QsU0FBUztZQUNULEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLG1CQUFtQixDQUFDO1NBQ3JDLENBQUMsQ0FBQztRQUVIOztXQUVHO1FBQ0gsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsVUFBVSxFQUFFO1lBQ3pDLE9BQU8sRUFBRSxHQUFHLEVBQUU7O2dCQUNaLE1BQU0sTUFBTSxHQUFHLGFBQU8sQ0FBQyxhQUFhLDBDQUFFLE9BQU8sQ0FBQztnQkFFOUMsSUFBSSxDQUFDLE1BQU0sRUFBRTtvQkFDWCxPQUFPO2lCQUNSO2dCQUVELElBQUksSUFBSSxHQUFHLEVBQUUsQ0FBQztnQkFDZCxNQUFNLE1BQU0sR0FBRyxNQUFNLENBQUMsTUFBTSxDQUFDO2dCQUM3QixNQUFNLElBQUksR0FBRyxNQUFNLENBQUMsS0FBSyxDQUFDLEtBQUssQ0FBQyxJQUFJLENBQUM7Z0JBQ3JDLE1BQU0sSUFBSSxHQUFHLE1BQU0sQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDO2dCQUNqQyxNQUFNLFNBQVMsR0FBRyxrRUFBZSxDQUFDLElBQUksQ0FBQyxDQUFDO2dCQUV4QyxJQUFJLGdGQUE2QixDQUFDLFNBQVMsQ0FBQyxFQUFFO29CQUM1Qyw0Q0FBNEM7b0JBQzVDLE1BQU0sTUFBTSxHQUFHLDRGQUF5QyxDQUFDLElBQUksQ0FBQyxDQUFDO29CQUMvRCxLQUFLLE1BQU0sS0FBSyxJQUFJLE1BQU0sRUFBRTt3QkFDMUIsSUFBSSxJQUFJLEtBQUssQ0FBQyxJQUFJLENBQUM7cUJBQ3BCO2lCQUNGO3FCQUFNO29CQUNMLElBQUksR0FBRyxJQUFJLENBQUM7aUJBQ2I7Z0JBRUQsTUFBTSxRQUFRLEdBQUcsS0FBSyxDQUFDO2dCQUN2QixJQUFJLElBQUksRUFBRTtvQkFDUixPQUFPLFFBQVEsQ0FBQyxPQUFPLENBQUMsZ0JBQWdCLEVBQUUsRUFBRSxRQUFRLEVBQUUsSUFBSSxFQUFFLElBQUksRUFBRSxDQUFDLENBQUM7aUJBQ3JFO3FCQUFNO29CQUNMLE9BQU8sT0FBTyxDQUFDLE9BQU8sQ0FBQyxLQUFLLENBQUMsQ0FBQyxDQUFDO2lCQUNoQztZQUNILENBQUM7WUFDRCxTQUFTO1lBQ1QsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsY0FBYyxDQUFDO1NBQ2hDLENBQUMsQ0FBQztRQUVIOztXQUVHO1FBQ0gsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsZUFBZSxFQUFFO1lBQzlDLE9BQU8sRUFBRSxHQUFHLEVBQUU7Z0JBQ1osTUFBTSxNQUFNLEdBQUcsT0FBTyxDQUFDLGFBQWEsQ0FBQztnQkFDckMsSUFBSSxDQUFDLE1BQU0sRUFBRTtvQkFDWCxPQUFPO2lCQUNSO2dCQUNELE1BQU0sSUFBSSxHQUFHLE1BQU0sQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDO2dCQUNqQyxPQUFPLFFBQVEsQ0FBQyxPQUFPLENBQUMscUJBQXFCLEVBQUU7b0JBQzdDLElBQUk7b0JBQ0osT0FBTyxFQUFFO3dCQUNQLElBQUksRUFBRSxhQUFhO3FCQUNwQjtpQkFDRixDQUFDLENBQUM7WUFDTCxDQUFDO1lBQ0QsU0FBUyxFQUFFLEdBQUcsRUFBRTtnQkFDZCxNQUFNLE1BQU0sR0FBRyxPQUFPLENBQUMsYUFBYSxDQUFDO2dCQUNyQyxPQUFPLENBQ0wsQ0FBQyxNQUFNLElBQUksa0VBQWUsQ0FBQyxNQUFNLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxLQUFLLEtBQUssQ0FBQyxJQUFJLEtBQUssQ0FDcEUsQ0FBQztZQUNKLENBQUM7WUFDRCxJQUFJLEVBQUUsbUVBQVk7WUFDbEIsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsdUJBQXVCLENBQUM7U0FDekMsQ0FBQyxDQUFDO1FBRUg7Ozs7V0FJRztRQUNILFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLFNBQVMsRUFBRTtZQUN4QyxLQUFLLEVBQUUsSUFBSSxDQUFDLEVBQUU7O2dCQUNaLElBQUksSUFBSSxDQUFDLFNBQVMsRUFBRTtvQkFDbEIsT0FBTyxNQUFDLElBQUksQ0FBQyxZQUF1QixtQ0FBSSxLQUFLLENBQUMsRUFBRSxDQUFDLGVBQWUsQ0FBQyxDQUFDO2lCQUNuRTtnQkFDRCxPQUFPLE1BQUMsSUFBSSxDQUFDLGFBQXdCLG1DQUFJLEtBQUssQ0FBQyxFQUFFLENBQUMsV0FBVyxDQUFDLENBQUM7WUFDakUsQ0FBQztZQUNELE9BQU8sRUFBRSxJQUFJLENBQUMsRUFBRSxXQUNkLGFBQUMsSUFBSSxDQUFDLE9BQWtCLG1DQUFJLEtBQUssQ0FBQyxFQUFFLENBQUMsd0JBQXdCLENBQUM7WUFDaEUsSUFBSSxFQUFFLElBQUksQ0FBQyxFQUFFOztnQkFDWCxXQUFJLENBQUMsU0FBUztvQkFDWixDQUFDLENBQUMsU0FBUztvQkFDWCxDQUFDLENBQUMsc0VBQWUsQ0FBQzt3QkFDZCxJQUFJLEVBQUUsTUFBQyxJQUFJLENBQUMsUUFBbUIsbUNBQUkscUVBQWM7cUJBQ2xELENBQUM7YUFBQTtZQUNSLE9BQU8sRUFBRSxJQUFJLENBQUMsRUFBRTs7Z0JBQ2QsTUFBTSxHQUFHLEdBQUcsSUFBSSxDQUFDLEdBQUcsSUFBSSxjQUFjLENBQUMsY0FBYyxDQUFDLEtBQUssQ0FBQyxJQUFJLENBQUM7Z0JBQ2pFLE9BQU8sU0FBUyxDQUNkLFFBQVEsRUFDUixHQUFhLEVBQ2IsTUFBQyxJQUFJLENBQUMsT0FBa0IsbUNBQUksS0FBSyxDQUNsQyxDQUFDO1lBQ0osQ0FBQztTQUNGLENBQUMsQ0FBQztRQUVIOztXQUVHO1FBQ0gsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsaUJBQWlCLEVBQUU7WUFDaEQsS0FBSyxFQUFFLElBQUksQ0FBQyxFQUFFLENBQ1osSUFBSSxDQUFDLFdBQVcsQ0FBQztnQkFDZixDQUFDLENBQUMsS0FBSyxDQUFDLEVBQUUsQ0FBQyxtQkFBbUIsQ0FBQztnQkFDL0IsQ0FBQyxDQUFDLEtBQUssQ0FBQyxFQUFFLENBQUMsZUFBZSxDQUFDO1lBQy9CLE9BQU8sRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLDRCQUE0QixDQUFDO1lBQy9DLElBQUksRUFBRSxJQUFJLENBQUMsRUFBRSxDQUFDLENBQUMsSUFBSSxDQUFDLFdBQVcsQ0FBQyxDQUFDLENBQUMsQ0FBQyxTQUFTLENBQUMsQ0FBQyxDQUFDLG1FQUFZLENBQUM7WUFDNUQsT0FBTyxFQUFFLElBQUksQ0FBQyxFQUFFO2dCQUNkLE1BQU0sR0FBRyxHQUFHLElBQUksQ0FBQyxLQUFLLENBQUMsSUFBSSxjQUFjLENBQUMsY0FBYyxDQUFDLEtBQUssQ0FBQyxJQUFJLENBQUM7Z0JBQ3BFLE9BQU8sU0FBUyxDQUFDLFFBQVEsRUFBRSxHQUFhLEVBQUUsSUFBSSxDQUFDLENBQUM7WUFDbEQsQ0FBQztTQUNGLENBQUMsQ0FBQztRQUVIOztXQUVHO1FBQ0gsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsSUFBSSxFQUFFO1lBQ25DLE9BQU8sRUFBRSxHQUFHLEVBQUU7O2dCQUNaLE1BQU0sTUFBTSxHQUFHLGFBQU8sQ0FBQyxhQUFhLDBDQUFFLE9BQU8sQ0FBQztnQkFFOUMsSUFBSSxDQUFDLE1BQU0sRUFBRTtvQkFDWCxPQUFPO2lCQUNSO2dCQUVELE1BQU0sQ0FBQyxNQUFNLENBQUMsSUFBSSxFQUFFLENBQUM7WUFDdkIsQ0FBQztZQUNELFNBQVMsRUFBRSxHQUFHLEVBQUU7O2dCQUNkLElBQUksQ0FBQyxTQUFTLEVBQUUsRUFBRTtvQkFDaEIsT0FBTyxLQUFLLENBQUM7aUJBQ2Q7Z0JBRUQsTUFBTSxNQUFNLEdBQUcsYUFBTyxDQUFDLGFBQWEsMENBQUUsT0FBTyxDQUFDO2dCQUU5QyxJQUFJLENBQUMsTUFBTSxFQUFFO29CQUNYLE9BQU8sS0FBSyxDQUFDO2lCQUNkO2dCQUNELHNEQUFzRDtnQkFDdEQseUZBQXlGO2dCQUN6RixPQUFPLElBQUksQ0FBQztZQUNkLENBQUM7WUFDRCxJQUFJLEVBQUUseUVBQWtCLENBQUMsRUFBRSxVQUFVLEVBQUUsVUFBVSxFQUFFLENBQUM7WUFDcEQsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsTUFBTSxDQUFDO1NBQ3hCLENBQUMsQ0FBQztRQUVIOztXQUVHO1FBQ0gsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsSUFBSSxFQUFFO1lBQ25DLE9BQU8sRUFBRSxHQUFHLEVBQUU7O2dCQUNaLE1BQU0sTUFBTSxHQUFHLGFBQU8sQ0FBQyxhQUFhLDBDQUFFLE9BQU8sQ0FBQztnQkFFOUMsSUFBSSxDQUFDLE1BQU0sRUFBRTtvQkFDWCxPQUFPO2lCQUNSO2dCQUVELE1BQU0sQ0FBQyxNQUFNLENBQUMsSUFBSSxFQUFFLENBQUM7WUFDdkIsQ0FBQztZQUNELFNBQVMsRUFBRSxHQUFHLEVBQUU7O2dCQUNkLElBQUksQ0FBQyxTQUFTLEVBQUUsRUFBRTtvQkFDaEIsT0FBTyxLQUFLLENBQUM7aUJBQ2Q7Z0JBRUQsTUFBTSxNQUFNLEdBQUcsYUFBTyxDQUFDLGFBQWEsMENBQUUsT0FBTyxDQUFDO2dCQUU5QyxJQUFJLENBQUMsTUFBTSxFQUFFO29CQUNYLE9BQU8sS0FBSyxDQUFDO2lCQUNkO2dCQUNELHNEQUFzRDtnQkFDdEQseUZBQXlGO2dCQUN6RixPQUFPLElBQUksQ0FBQztZQUNkLENBQUM7WUFDRCxJQUFJLEVBQUUseUVBQWtCLENBQUMsRUFBRSxVQUFVLEVBQUUsVUFBVSxFQUFFLENBQUM7WUFDcEQsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsTUFBTSxDQUFDO1NBQ3hCLENBQUMsQ0FBQztRQUVIOztXQUVHO1FBQ0gsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsR0FBRyxFQUFFO1lBQ2xDLE9BQU8sRUFBRSxHQUFHLEVBQUU7O2dCQUNaLE1BQU0sTUFBTSxHQUFHLGFBQU8sQ0FBQyxhQUFhLDBDQUFFLE9BQU8sQ0FBQztnQkFFOUMsSUFBSSxDQUFDLE1BQU0sRUFBRTtvQkFDWCxPQUFPO2lCQUNSO2dCQUVELE1BQU0sTUFBTSxHQUFHLE1BQU0sQ0FBQyxNQUEwQixDQUFDO2dCQUNqRCxNQUFNLElBQUksR0FBRyxnQkFBZ0IsQ0FBQyxNQUFNLENBQUMsQ0FBQztnQkFFdEMsd0VBQXNCLENBQUMsSUFBSSxDQUFDLENBQUM7Z0JBQzdCLE1BQU0sQ0FBQyxnQkFBZ0IsSUFBSSxNQUFNLENBQUMsZ0JBQWdCLENBQUMsRUFBRSxDQUFDLENBQUM7WUFDekQsQ0FBQztZQUNELFNBQVMsRUFBRSxHQUFHLEVBQUU7O2dCQUNkLElBQUksQ0FBQyxTQUFTLEVBQUUsRUFBRTtvQkFDaEIsT0FBTyxLQUFLLENBQUM7aUJBQ2Q7Z0JBRUQsTUFBTSxNQUFNLEdBQUcsYUFBTyxDQUFDLGFBQWEsMENBQUUsT0FBTyxDQUFDO2dCQUU5QyxJQUFJLENBQUMsTUFBTSxFQUFFO29CQUNYLE9BQU8sS0FBSyxDQUFDO2lCQUNkO2dCQUVELDREQUE0RDtnQkFDNUQsT0FBTyxVQUFVLENBQUMsTUFBTSxDQUFDLE1BQTBCLENBQUMsQ0FBQztZQUN2RCxDQUFDO1lBQ0QsSUFBSSxFQUFFLHdFQUFpQixDQUFDLEVBQUUsVUFBVSxFQUFFLFVBQVUsRUFBRSxDQUFDO1lBQ25ELEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLEtBQUssQ0FBQztTQUN2QixDQUFDLENBQUM7UUFFSDs7V0FFRztRQUNILFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLElBQUksRUFBRTtZQUNuQyxPQUFPLEVBQUUsR0FBRyxFQUFFOztnQkFDWixNQUFNLE1BQU0sR0FBRyxhQUFPLENBQUMsYUFBYSwwQ0FBRSxPQUFPLENBQUM7Z0JBRTlDLElBQUksQ0FBQyxNQUFNLEVBQUU7b0JBQ1gsT0FBTztpQkFDUjtnQkFFRCxNQUFNLE1BQU0sR0FBRyxNQUFNLENBQUMsTUFBMEIsQ0FBQztnQkFDakQsTUFBTSxJQUFJLEdBQUcsZ0JBQWdCLENBQUMsTUFBTSxDQUFDLENBQUM7Z0JBRXRDLHdFQUFzQixDQUFDLElBQUksQ0FBQyxDQUFDO1lBQy9CLENBQUM7WUFDRCxTQUFTLEVBQUUsR0FBRyxFQUFFOztnQkFDZCxJQUFJLENBQUMsU0FBUyxFQUFFLEVBQUU7b0JBQ2hCLE9BQU8sS0FBSyxDQUFDO2lCQUNkO2dCQUVELE1BQU0sTUFBTSxHQUFHLGFBQU8sQ0FBQyxhQUFhLDBDQUFFLE9BQU8sQ0FBQztnQkFFOUMsSUFBSSxDQUFDLE1BQU0sRUFBRTtvQkFDWCxPQUFPLEtBQUssQ0FBQztpQkFDZDtnQkFFRCw0REFBNEQ7Z0JBQzVELE9BQU8sVUFBVSxDQUFDLE1BQU0sQ0FBQyxNQUEwQixDQUFDLENBQUM7WUFDdkQsQ0FBQztZQUNELElBQUksRUFBRSx5RUFBa0IsQ0FBQyxFQUFFLFVBQVUsRUFBRSxVQUFVLEVBQUUsQ0FBQztZQUNwRCxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxNQUFNLENBQUM7U0FDeEIsQ0FBQyxDQUFDO1FBRUg7O1dBRUc7UUFDSCxRQUFRLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyxLQUFLLEVBQUU7WUFDcEMsT0FBTyxFQUFFLEtBQUssSUFBSSxFQUFFOztnQkFDbEIsTUFBTSxNQUFNLEdBQUcsYUFBTyxDQUFDLGFBQWEsMENBQUUsT0FBTyxDQUFDO2dCQUU5QyxJQUFJLENBQUMsTUFBTSxFQUFFO29CQUNYLE9BQU87aUJBQ1I7Z0JBRUQsTUFBTSxNQUFNLEdBQXVCLE1BQU0sQ0FBQyxNQUFNLENBQUM7Z0JBRWpELDBCQUEwQjtnQkFDMUIsTUFBTSxTQUFTLEdBQUcsTUFBTSxDQUFDLFNBQVMsQ0FBQyxTQUFTLENBQUM7Z0JBQzdDLE1BQU0sYUFBYSxHQUFXLE1BQU0sU0FBUyxDQUFDLFFBQVEsRUFBRSxDQUFDO2dCQUV6RCxJQUFJLGFBQWEsRUFBRTtvQkFDakIsMkJBQTJCO29CQUMzQixNQUFNLENBQUMsZ0JBQWdCLElBQUksTUFBTSxDQUFDLGdCQUFnQixDQUFDLGFBQWEsQ0FBQyxDQUFDO2lCQUNuRTtZQUNILENBQUM7WUFDRCxTQUFTLEVBQUUsR0FBRyxFQUFFLFdBQUMsY0FBTyxDQUFDLFNBQVMsRUFBRSxLQUFJLGFBQU8sQ0FBQyxhQUFhLDBDQUFFLE9BQU8sRUFBQztZQUN2RSxJQUFJLEVBQUUsMEVBQW1CLENBQUMsRUFBRSxVQUFVLEVBQUUsVUFBVSxFQUFFLENBQUM7WUFDckQsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsT0FBTyxDQUFDO1NBQ3pCLENBQUMsQ0FBQztRQUVIOztXQUVHO1FBQ0gsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsU0FBUyxFQUFFO1lBQ3hDLE9BQU8sRUFBRSxHQUFHLEVBQUU7O2dCQUNaLE1BQU0sTUFBTSxHQUFHLGFBQU8sQ0FBQyxhQUFhLDBDQUFFLE9BQU8sQ0FBQztnQkFFOUMsSUFBSSxDQUFDLE1BQU0sRUFBRTtvQkFDWCxPQUFPO2lCQUNSO2dCQUVELE1BQU0sTUFBTSxHQUFHLE1BQU0sQ0FBQyxNQUEwQixDQUFDO2dCQUNqRCxNQUFNLENBQUMsV0FBVyxDQUFDLDJEQUFTLENBQUMsQ0FBQztZQUNoQyxDQUFDO1lBQ0QsU0FBUyxFQUFFLEdBQUcsRUFBRSxXQUFDLGNBQU8sQ0FBQyxTQUFTLEVBQUUsS0FBSSxhQUFPLENBQUMsYUFBYSwwQ0FBRSxPQUFPLEVBQUM7WUFDdkUsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsWUFBWSxDQUFDO1NBQzlCLENBQUMsQ0FBQztJQUNMLENBQUM7SUFub0JlLG9CQUFXLGNBbW9CMUI7SUFFRCxTQUFnQixvQkFBb0IsQ0FDbEMsUUFBeUIsRUFDekIsYUFBNkIsRUFDN0IsT0FBbUMsRUFDbkMsVUFBOEI7UUFFOUIsTUFBTSxLQUFLLEdBQUcsQ0FBQyxVQUFVLGFBQVYsVUFBVSxjQUFWLFVBQVUsR0FBSSxtRUFBYyxDQUFDLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FBQyxDQUFDO1FBRWhFLFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLGVBQWUsRUFBRTtZQUM5QyxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxnQ0FBZ0MsQ0FBQztZQUNqRCxPQUFPLEVBQUUsR0FBRyxFQUFFO2dCQUNaLE1BQU0sRUFBRSxHQUNOLGFBQWEsQ0FBQyxhQUFhLElBQUksYUFBYSxDQUFDLGFBQWEsQ0FBQyxFQUFFLENBQUM7Z0JBQ2hFLElBQUksRUFBRSxFQUFFO29CQUNOLE9BQU8sT0FBTyxDQUFDLE1BQU0sQ0FBQyxFQUFFLENBQUMsQ0FBQztpQkFDM0I7WUFDSCxDQUFDO1NBQ0YsQ0FBQyxDQUFDO1FBRUgsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsZUFBZSxFQUFFO1lBQzlDLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLG1DQUFtQyxDQUFDO1lBQ3BELE9BQU8sRUFBRSxHQUFHLEVBQUU7Z0JBQ1osTUFBTSxFQUFFLEdBQ04sYUFBYSxDQUFDLGFBQWEsSUFBSSxhQUFhLENBQUMsYUFBYSxDQUFDLEVBQUUsQ0FBQztnQkFDaEUsSUFBSSxFQUFFLEVBQUU7b0JBQ04sT0FBTyxPQUFPLENBQUMsTUFBTSxDQUFDLEVBQUUsQ0FBQyxDQUFDO2lCQUMzQjtZQUNILENBQUM7U0FDRixDQUFDLENBQUM7UUFFSCxRQUFRLENBQUMsYUFBYSxDQUFDO1lBQ3JCLE9BQU8sRUFBRSxVQUFVLENBQUMsZUFBZTtZQUNuQyxJQUFJLEVBQUUsQ0FBQyxPQUFPLENBQUM7WUFDZixRQUFRLEVBQUUseUNBQXlDO1NBQ3BELENBQUMsQ0FBQztJQUNMLENBQUM7SUFuQ2UsNkJBQW9CLHVCQW1DbkM7SUFFRDs7T0FFRztJQUNILFNBQVMsVUFBVSxDQUFDLE1BQXdCO1FBQzFDLE1BQU0sWUFBWSxHQUFHLE1BQU0sQ0FBQyxZQUFZLEVBQUUsQ0FBQztRQUMzQyxNQUFNLEVBQUUsS0FBSyxFQUFFLEdBQUcsRUFBRSxHQUFHLFlBQVksQ0FBQztRQUNwQyxNQUFNLFFBQVEsR0FBRyxLQUFLLENBQUMsTUFBTSxLQUFLLEdBQUcsQ0FBQyxNQUFNLElBQUksS0FBSyxDQUFDLElBQUksS0FBSyxHQUFHLENBQUMsSUFBSSxDQUFDO1FBRXhFLE9BQU8sUUFBUSxDQUFDO0lBQ2xCLENBQUM7SUFFRDs7T0FFRztJQUNILFNBQVMsZ0JBQWdCLENBQUMsTUFBd0I7UUFDaEQsTUFBTSxZQUFZLEdBQUcsTUFBTSxDQUFDLFlBQVksRUFBRSxDQUFDO1FBQzNDLE1BQU0sS0FBSyxHQUFHLE1BQU0sQ0FBQyxXQUFXLENBQUMsWUFBWSxDQUFDLEtBQUssQ0FBQyxDQUFDO1FBQ3JELE1BQU0sR0FBRyxHQUFHLE1BQU0sQ0FBQyxXQUFXLENBQUMsWUFBWSxDQUFDLEdBQUcsQ0FBQyxDQUFDO1FBQ2pELE1BQU0sSUFBSSxHQUFHLE1BQU0sQ0FBQyxLQUFLLENBQUMsS0FBSyxDQUFDLElBQUksQ0FBQyxTQUFTLENBQUMsS0FBSyxFQUFFLEdBQUcsQ0FBQyxDQUFDO1FBRTNELE9BQU8sSUFBSSxDQUFDO0lBQ2QsQ0FBQztJQUVEOztPQUVHO0lBQ0gsS0FBSyxVQUFVLFNBQVMsQ0FDdEIsUUFBeUIsRUFDekIsR0FBVyxFQUNYLE1BQWMsS0FBSztRQUVuQixNQUFNLEtBQUssR0FBRyxNQUFNLFFBQVEsQ0FBQyxPQUFPLENBQUMseUJBQXlCLEVBQUU7WUFDOUQsSUFBSSxFQUFFLEdBQUc7WUFDVCxJQUFJLEVBQUUsTUFBTTtZQUNaLEdBQUc7U0FDSixDQUFDLENBQUM7UUFDSCxJQUFJLEtBQUssSUFBSSxTQUFTLEVBQUU7WUFDdEIsTUFBTSxNQUFNLEdBQUcsQ0FBQyxNQUFNLFFBQVEsQ0FBQyxPQUFPLENBQUMsaUJBQWlCLEVBQUU7Z0JBQ3hELElBQUksRUFBRSxLQUFLLENBQUMsSUFBSTtnQkFDaEIsT0FBTyxFQUFFLE9BQU87YUFDakIsQ0FBQyxDQUErQixDQUFDO1lBQ2xDLE1BQU0sQ0FBQyxVQUFVLEdBQUcsSUFBSSxDQUFDO1lBQ3pCLE9BQU8sTUFBTSxDQUFDO1NBQ2Y7SUFDSCxDQUFDO0lBRUQ7O09BRUc7SUFDSCxTQUFnQixnQkFBZ0IsQ0FDOUIsUUFBbUIsRUFDbkIsS0FBd0I7UUFFeEIsc0JBQXNCLENBQUMsUUFBUSxFQUFFLEtBQUssQ0FBQyxDQUFDO1FBRXhDLDhCQUE4QixDQUFDLFFBQVEsRUFBRSxLQUFLLENBQUMsQ0FBQztJQUNsRCxDQUFDO0lBUGUseUJBQWdCLG1CQU8vQjtJQUVEOztPQUVHO0lBQ0gsU0FBZ0Isc0JBQXNCLENBQ3BDLFFBQW1CLEVBQ25CLEtBQXdCO1FBRXhCLFFBQVEsQ0FBQyxHQUFHLENBQUM7WUFDWCxPQUFPLEVBQUUsVUFBVSxDQUFDLFNBQVM7WUFDN0IsUUFBUSxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsT0FBTyxDQUFDO1lBQzNCLElBQUksRUFBRSxDQUFDO1NBQ1IsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztJQVRlLCtCQUFzQix5QkFTckM7SUFFRDs7T0FFRztJQUNILFNBQWdCLDhCQUE4QixDQUM1QyxRQUFtQixFQUNuQixLQUF3QjtRQUV4QixRQUFRLENBQUMsR0FBRyxDQUFDO1lBQ1gsT0FBTyxFQUFFLFVBQVUsQ0FBQyxpQkFBaUI7WUFDckMsUUFBUSxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsT0FBTyxDQUFDO1lBQzNCLElBQUksRUFBRSxDQUFDO1NBQ1IsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztJQVRlLHVDQUE4QixpQ0FTN0M7SUFFRDs7T0FFRztJQUNILFNBQWdCLDhCQUE4QixDQUM1QyxRQUFtQixFQUNuQixLQUF3QixFQUN4Qix3QkFBaUQ7UUFFakQsS0FBSyxJQUFJLEdBQUcsSUFBSSx3QkFBd0IsRUFBRTtZQUN4QyxRQUFRLENBQUMsR0FBRyxDQUFDO2dCQUNYLE9BQU8sRUFBRSxVQUFVLENBQUMsU0FBUztnQkFDN0IsUUFBUSxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsT0FBTyxDQUFDO2dCQUMzQixJQUFJLEVBQUUsQ0FBQztnQkFDUCxJQUFJLEVBQUUsR0FBRzthQUNWLENBQUMsQ0FBQztTQUNKO0lBQ0gsQ0FBQztJQWJlLHVDQUE4QixpQ0FhN0M7SUFFRDs7T0FFRztJQUNILFNBQWdCLGVBQWUsQ0FDN0IsT0FBd0IsRUFDeEIsS0FBd0I7UUFFeEIsOEJBQThCLENBQUMsT0FBTyxFQUFFLEtBQUssQ0FBQyxDQUFDO1FBRS9DLDRCQUE0QixDQUFDLE9BQU8sRUFBRSxLQUFLLENBQUMsQ0FBQztRQUU3QyxvQ0FBb0MsQ0FBQyxPQUFPLEVBQUUsS0FBSyxDQUFDLENBQUM7UUFFckQsa0NBQWtDLENBQUMsT0FBTyxFQUFFLEtBQUssQ0FBQyxDQUFDO0lBQ3JELENBQUM7SUFYZSx3QkFBZSxrQkFXOUI7SUFFRDs7T0FFRztJQUNILFNBQWdCLDhCQUE4QixDQUM1QyxPQUF3QixFQUN4QixLQUF3QjtRQUV4QixNQUFNLGVBQWUsR0FBRyxLQUFLLENBQUMsRUFBRSxDQUFDLGFBQWEsQ0FBQyxDQUFDO1FBQ2hELE1BQU0sSUFBSSxHQUFlO1lBQ3ZCLFlBQVksRUFBRSxLQUFLO1lBQ25CLElBQUksRUFBRSxDQUFDO1NBQ1IsQ0FBQztRQUNGLE1BQU0sT0FBTyxHQUFHLFVBQVUsQ0FBQyxVQUFVLENBQUM7UUFDdEMsT0FBTyxDQUFDLE9BQU8sQ0FBQyxFQUFFLE9BQU8sRUFBRSxJQUFJLEVBQUUsUUFBUSxFQUFFLGVBQWUsRUFBRSxDQUFDLENBQUM7UUFFOUQsS0FBSyxNQUFNLElBQUksSUFBSSxDQUFDLENBQUMsRUFBRSxDQUFDLEVBQUUsQ0FBQyxFQUFFLENBQUMsQ0FBQyxFQUFFO1lBQy9CLE1BQU0sSUFBSSxHQUFlO2dCQUN2QixZQUFZLEVBQUUsSUFBSTtnQkFDbEIsSUFBSTthQUNMLENBQUM7WUFDRixPQUFPLENBQUMsT0FBTyxDQUFDLEVBQUUsT0FBTyxFQUFFLElBQUksRUFBRSxRQUFRLEVBQUUsZUFBZSxFQUFFLENBQUMsQ0FBQztTQUMvRDtJQUNILENBQUM7SUFuQmUsdUNBQThCLGlDQW1CN0M7SUFFRDs7T0FFRztJQUNILFNBQWdCLDRCQUE0QixDQUMxQyxPQUF3QixFQUN4QixLQUF3QjtRQUV4QixNQUFNLGVBQWUsR0FBRyxLQUFLLENBQUMsRUFBRSxDQUFDLGFBQWEsQ0FBQyxDQUFDO1FBQ2hELE9BQU8sQ0FBQyxPQUFPLENBQUM7WUFDZCxPQUFPLEVBQUUsVUFBVSxDQUFDLFNBQVM7WUFDN0IsSUFBSSxFQUFFLEVBQUUsU0FBUyxFQUFFLElBQUksRUFBRTtZQUN6QixRQUFRLEVBQUUsZUFBZTtTQUMxQixDQUFDLENBQUM7SUFDTCxDQUFDO0lBVmUscUNBQTRCLCtCQVUzQztJQUVEOztPQUVHO0lBQ0gsU0FBZ0Isb0NBQW9DLENBQ2xELE9BQXdCLEVBQ3hCLEtBQXdCO1FBRXhCLE1BQU0sZUFBZSxHQUFHLEtBQUssQ0FBQyxFQUFFLENBQUMsYUFBYSxDQUFDLENBQUM7UUFDaEQsT0FBTyxDQUFDLE9BQU8sQ0FBQztZQUNkLE9BQU8sRUFBRSxVQUFVLENBQUMsaUJBQWlCO1lBQ3JDLElBQUksRUFBRSxFQUFFLFNBQVMsRUFBRSxJQUFJLEVBQUU7WUFDekIsUUFBUSxFQUFFLGVBQWU7U0FDMUIsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztJQVZlLDZDQUFvQyx1Q0FVbkQ7SUFFRDs7T0FFRztJQUNILFNBQWdCLGtDQUFrQyxDQUNoRCxPQUF3QixFQUN4QixLQUF3QjtRQUV4QixNQUFNLGVBQWUsR0FBRyxLQUFLLENBQUMsRUFBRSxDQUFDLGFBQWEsQ0FBQyxDQUFDO1FBQ2hELE1BQU0sT0FBTyxHQUFHLFVBQVUsQ0FBQyxjQUFjLENBQUM7UUFFMUMsSUFBSSxJQUFJLEdBQUcsRUFBRSxLQUFLLEVBQUUsQ0FBQyxFQUFFLENBQUM7UUFDeEIsT0FBTyxDQUFDLE9BQU8sQ0FBQyxFQUFFLE9BQU8sRUFBRSxJQUFJLEVBQUUsUUFBUSxFQUFFLGVBQWUsRUFBRSxDQUFDLENBQUM7UUFFOUQsSUFBSSxHQUFHLEVBQUUsS0FBSyxFQUFFLENBQUMsQ0FBQyxFQUFFLENBQUM7UUFDckIsT0FBTyxDQUFDLE9BQU8sQ0FBQyxFQUFFLE9BQU8sRUFBRSxJQUFJLEVBQUUsUUFBUSxFQUFFLGVBQWUsRUFBRSxDQUFDLENBQUM7SUFDaEUsQ0FBQztJQVplLDJDQUFrQyxxQ0FZakQ7SUFFRDs7T0FFRztJQUNILFNBQWdCLDZCQUE2QixDQUMzQyxPQUF3QixFQUN4QixLQUF3QixFQUN4Qix3QkFBaUQ7UUFFakQsTUFBTSxlQUFlLEdBQUcsS0FBSyxDQUFDLEVBQUUsQ0FBQyxhQUFhLENBQUMsQ0FBQztRQUNoRCxLQUFLLElBQUksR0FBRyxJQUFJLHdCQUF3QixFQUFFO1lBQ3hDLE9BQU8sQ0FBQyxPQUFPLENBQUM7Z0JBQ2QsT0FBTyxFQUFFLFVBQVUsQ0FBQyxTQUFTO2dCQUM3QixJQUFJLGtDQUFPLEdBQUcsS0FBRSxTQUFTLEVBQUUsSUFBSSxHQUFFO2dCQUNqQyxRQUFRLEVBQUUsZUFBZTthQUMxQixDQUFDLENBQUM7U0FDSjtJQUNILENBQUM7SUFiZSxzQ0FBNkIsZ0NBYTVDO0lBRUQ7O09BRUc7SUFDSCxTQUFnQixZQUFZLENBQzFCLElBQWUsRUFDZixPQUFtRCxFQUNuRCxjQUFzQyxFQUN0QyxTQUF3QjtRQUV4Qix3Q0FBd0M7UUFDeEMsSUFBSSxDQUFDLFFBQVEsQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLEdBQUcsQ0FBQztZQUM3QixFQUFFLEVBQUUsVUFBVSxDQUFDLElBQUk7WUFDbkIsU0FBUztTQUNWLENBQUMsQ0FBQztRQUNILElBQUksQ0FBQyxRQUFRLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxHQUFHLENBQUM7WUFDN0IsRUFBRSxFQUFFLFVBQVUsQ0FBQyxJQUFJO1lBQ25CLFNBQVM7U0FDVixDQUFDLENBQUM7UUFFSCwyQkFBMkI7UUFDM0IsSUFBSSxDQUFDLFFBQVEsQ0FBQyxhQUFhLENBQUMsaUJBQWlCLENBQUMsR0FBRyxDQUFDO1lBQ2hELEVBQUUsRUFBRSxVQUFVLENBQUMsa0JBQWtCO1lBQ2pDLFNBQVM7U0FDVixDQUFDLENBQUM7UUFDSCxJQUFJLENBQUMsUUFBUSxDQUFDLGFBQWEsQ0FBQyxtQkFBbUIsQ0FBQyxHQUFHLENBQUM7WUFDbEQsRUFBRSxFQUFFLFVBQVUsQ0FBQyxvQkFBb0I7WUFDbkMsU0FBUztTQUNWLENBQUMsQ0FBQztRQUNILElBQUksQ0FBQyxRQUFRLENBQUMsYUFBYSxDQUFDLGNBQWMsQ0FBQyxHQUFHLENBQUM7WUFDN0MsRUFBRSxFQUFFLFVBQVUsQ0FBQyxlQUFlO1lBQzlCLFNBQVM7U0FDVixDQUFDLENBQUM7UUFFSCwyQ0FBMkM7UUFDM0MsSUFBSSxDQUFDLFFBQVEsQ0FBQyxlQUFlLENBQUMsR0FBRyxDQUFDO1lBQ2hDLEVBQUUsRUFBRSxVQUFVLENBQUMsYUFBYTtZQUM1QixTQUFTO1NBQ1YsQ0FBQyxDQUFDO1FBRUgscUNBQXFDO1FBQ3JDLElBQUksY0FBYyxFQUFFO1lBQ2xCLHVCQUF1QixDQUFDLElBQUksRUFBRSxjQUFjLENBQUMsQ0FBQztTQUMvQztJQUNILENBQUM7SUF4Q2UscUJBQVksZUF3QzNCO0lBRUQ7O09BRUc7SUFDSCxTQUFnQiwwQkFBMEIsQ0FDeEMsSUFBZSxFQUNmLHdCQUFpRDtRQUVqRCxLQUFLLElBQUksR0FBRyxJQUFJLHdCQUF3QixFQUFFO1lBQ3hDLElBQUksQ0FBQyxRQUFRLENBQUMsT0FBTyxDQUFDLE9BQU8sQ0FBQztnQkFDNUIsT0FBTyxFQUFFLFVBQVUsQ0FBQyxTQUFTO2dCQUM3QixJQUFJLEVBQUUsR0FBRztnQkFDVCxJQUFJLEVBQUUsRUFBRTthQUNULENBQUMsQ0FBQztTQUNKO0lBQ0gsQ0FBQztJQVhlLG1DQUEwQiw2QkFXekM7SUFFRDs7T0FFRztJQUNILFNBQWdCLHVCQUF1QixDQUNyQyxJQUFlLEVBQ2YsY0FBK0I7UUFFL0IsTUFBTSxTQUFTLEdBQUcsQ0FBQyxPQUFvQyxFQUFFLEVBQUUsQ0FDekQsT0FBTyxDQUFDLE9BQU87WUFDZixDQUFDLENBQUMsY0FBYyxDQUFDLElBQUksQ0FDbkIsTUFBTSxDQUFDLEVBQUUsV0FBQyxvQkFBTSxDQUFDLGNBQWMsQ0FBQyxPQUFPLDBDQUFFLElBQUksTUFBSyxPQUFPLENBQUMsT0FBTyxDQUFDLElBQUksSUFDdkUsQ0FBQztRQUNKLElBQUksQ0FBQyxPQUFPLENBQUMsV0FBVyxDQUFDLE9BQU8sQ0FBQyxHQUFHLENBQUM7WUFDbkMsRUFBRSxFQUFFLFVBQVUsQ0FBQyxjQUFjO1lBQzdCLFNBQVM7U0FDVixDQUFDLENBQUM7UUFDSCxJQUFJLENBQUMsT0FBTyxDQUFDLFdBQVcsQ0FBQyxHQUFHLENBQUMsR0FBRyxDQUFDO1lBQy9CLEVBQUUsRUFBRSxVQUFVLENBQUMsT0FBTztZQUN0QixTQUFTO1NBQ1YsQ0FBQyxDQUFDO1FBQ0gsSUFBSSxDQUFDLE9BQU8sQ0FBQyxXQUFXLENBQUMsTUFBTSxDQUFDLEdBQUcsQ0FBQztZQUNsQyxFQUFFLEVBQUUsVUFBVSxDQUFDLFVBQVU7WUFDekIsU0FBUztTQUNWLENBQUMsQ0FBQztJQUNMLENBQUM7SUFyQmUsZ0NBQXVCLDBCQXFCdEM7SUFFRCxTQUFnQix3QkFBd0IsQ0FDdEMsR0FBb0IsRUFDcEIsY0FBK0IsRUFDL0IsT0FBd0QsRUFDeEQsS0FBd0I7UUFFeEIsTUFBTSxjQUFjLEdBQUcsS0FBSyxFQUFFLElBTTdCLEVBQTZCLEVBQUU7O1lBQzlCLE1BQU0sSUFBSSxHQUFHLGNBQWMsQ0FBQyxjQUFjLENBQUMsaUJBQWlCLENBQUM7WUFDN0QsTUFBTSxPQUFPLEdBQXVCLE9BQU8sQ0FBQyxFQUFFO2dCQUM1QyxPQUFPLElBQUksQ0FBQyxPQUFPLENBQUMsQ0FBQztZQUN2QixDQUFDLENBQUM7WUFFRixpQ0FBaUM7WUFDakMsSUFBSSxRQUFRLEdBQUcsSUFBSSxDQUFDLFFBQVEsQ0FBQztZQUM3QixJQUFJLENBQUMsUUFBUSxJQUFJLElBQUksQ0FBQyxTQUFTLEVBQUU7Z0JBQy9CLFFBQVEsR0FBRyxjQUFjLENBQUMsZUFBZSxDQUFDLHFCQUFxQixDQUM3RCxRQUFRLElBQUksQ0FBQyxTQUFTLENBQUMsT0FBTyxDQUFDLE1BQU0sRUFBRSxFQUFFLENBQUMsRUFBRSxDQUM3QyxDQUFDO2FBQ0g7WUFFRCxNQUFNLE1BQU0sR0FBRyxxRkFBaUMsQ0FBQztnQkFDL0MsT0FBTztnQkFDUCxPQUFPLEVBQUUsSUFBSSxDQUFDLE9BQU87Z0JBQ3JCLFFBQVEsRUFBRSxRQUFRO2FBQ25CLENBQUMsQ0FBQztZQUNILE1BQU0sQ0FBQyxLQUFLLENBQUMsS0FBSyxHQUFHLElBQUksQ0FBQyxLQUFLLElBQUksS0FBSyxDQUFDLEVBQUUsQ0FBQyxhQUFhLENBQUMsQ0FBQztZQUMzRCxNQUFNLENBQUMsS0FBSyxDQUFDLE9BQU8sR0FBRyxNQUFNLENBQUMsS0FBSyxDQUFDLEtBQUssQ0FBQztZQUUxQywrREFBK0Q7WUFDL0QsTUFBTSxRQUFRLEdBQUcsMERBQU8sQ0FBQyxHQUFHLENBQUMsV0FBVyxDQUFDLFNBQVMsRUFBRSxDQUFDLENBQUMsSUFBSSxDQUFDLFFBQVEsQ0FBQyxFQUFFO2dCQUNwRSxPQUFPLFFBQVEsQ0FBQyxDQUFDLENBQUMsUUFBUSxDQUFDLFNBQVMsQ0FBQyxRQUFRLENBQUMsUUFBUSxDQUFDLENBQUMsQ0FBQyxDQUFDLFNBQVMsQ0FBQztZQUN0RSxDQUFDLENBQUMsQ0FBQztZQUNILE1BQU0sQ0FBQyxLQUFLLENBQUMsSUFBSSxHQUFHLGNBQVEsYUFBUixRQUFRLHVCQUFSLFFBQVEsQ0FBRSxJQUFJLG1DQUFJLHFFQUFjLENBQUM7WUFFckQsSUFBSSxJQUFJLENBQUMsUUFBUSxFQUFFO2dCQUNqQixNQUFNLENBQUMsRUFBRSxHQUFHLElBQUksQ0FBQyxRQUFRLENBQUM7YUFDM0I7WUFDRCxNQUFNLElBQUksR0FBRyxJQUFJLGdFQUFjLENBQUMsRUFBRSxPQUFPLEVBQUUsTUFBTSxFQUFFLENBQUMsQ0FBQztZQUNyRCxNQUFNLE9BQU8sQ0FBQyxHQUFHLENBQUMsSUFBSSxDQUFDLENBQUM7WUFDeEIsR0FBRyxDQUFDLEtBQUssQ0FBQyxHQUFHLENBQUMsSUFBSSxFQUFFLE1BQU0sQ0FBQyxDQUFDO1lBQzVCLE9BQU8sTUFBTSxDQUFDO1FBQ2hCLENBQUMsQ0FBQztRQUVGLEdBQUcsQ0FBQyxRQUFRLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyxjQUFjLEVBQUU7WUFDakQsS0FBSyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsa0JBQWtCLENBQUM7WUFDbkMsT0FBTyxFQUFFLENBQUMsSUFBUyxFQUFFLEVBQUU7Z0JBQ3JCLE9BQU8sY0FBYyxDQUFDLElBQUksQ0FBQyxDQUFDO1lBQzlCLENBQUM7U0FDRixDQUFDLENBQUM7SUFDTCxDQUFDO0lBdkRlLGlDQUF3QiwyQkF1RHZDO0FBQ0gsQ0FBQyxFQWhsQ2dCLFFBQVEsS0FBUixRQUFRLFFBZ2xDeEI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUNydkNELDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBTThCO0FBUUg7QUFNRTtBQUNtQztBQUNiO0FBRWU7QUFDUDtBQVc5QjtBQUNpQjtBQUt4QjtBQUN3QjtBQUdjO0FBQ1o7QUFDUTtBQUNMO0FBQ0o7QUFFSDtBQUUyQjtBQUVwQztBQUV0Qzs7R0FFRztBQUNILE1BQU0sTUFBTSxHQUEwQztJQUNwRCxRQUFRO0lBQ1IsRUFBRSxFQUFFLHlDQUF5QztJQUM3QyxRQUFRLEVBQUU7UUFDUixtRUFBZTtRQUNmLHdFQUFtQjtRQUNuQiwwRUFBZ0I7UUFDaEIsaUVBQVc7S0FDWjtJQUNELFFBQVEsRUFBRTtRQUNSLGdFQUFlO1FBQ2YsaUVBQWU7UUFDZiwyREFBUztRQUNULDREQUFTO1FBQ1Qsb0VBQWU7UUFDZix3RUFBc0I7UUFDdEIsc0VBQXdCO1FBQ3hCLHdFQUFzQjtLQUN2QjtJQUNELFFBQVEsRUFBRSxrRUFBYztJQUN4QixTQUFTLEVBQUUsSUFBSTtDQUNoQixDQUFDO0FBRUY7OztHQUdHO0FBQ0ksTUFBTSxjQUFjLEdBQWdDO0lBQ3pELEVBQUUsRUFBRSxtREFBbUQ7SUFDdkQsU0FBUyxFQUFFLElBQUk7SUFDZixRQUFRLEVBQUUsQ0FBQyxrRUFBYyxFQUFFLDBFQUFnQixFQUFFLGlFQUFXLENBQUM7SUFDekQsUUFBUSxFQUFFLENBQUMsOERBQVUsQ0FBQztJQUN0QixRQUFRLEVBQUUsQ0FDUixHQUFvQixFQUNwQixhQUE2QixFQUM3QixlQUFpQyxFQUNqQyxVQUF1QixFQUN2QixTQUE0QixFQUM1QixFQUFFO1FBQ0YsTUFBTSxLQUFLLEdBQUcsVUFBVSxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUMsQ0FBQztRQUM1QyxJQUFJLENBQUMsU0FBUyxFQUFFO1lBQ2QsNkNBQTZDO1lBQzdDLE9BQU87U0FDUjtRQUNELDhDQUE4QztRQUM5QyxNQUFNLElBQUksR0FBRyxJQUFJLGtEQUFJLENBQUMsRUFBRSxRQUFRLEVBQUUsR0FBRyxDQUFDLFFBQVEsRUFBRSxDQUFDLENBQUM7UUFDbEQsTUFBTSxPQUFPLEdBQUcsd0JBQXdCLENBQUM7UUFDekMsTUFBTSxFQUFFLEtBQUssRUFBRSxHQUFHLEdBQUcsQ0FBQztRQUN0QixNQUFNLElBQUksR0FBZTtZQUN2QixZQUFZLEVBQUUsS0FBSztZQUNuQixJQUFJLEVBQUUsQ0FBQztZQUNQLElBQUksRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLGlCQUFpQixDQUFDO1NBQ2xDLENBQUM7UUFDRixJQUFJLENBQUMsT0FBTyxDQUFDLEVBQUUsT0FBTyxFQUFFLElBQUksRUFBRSxDQUFDLENBQUM7UUFDaEMsS0FBSyxNQUFNLElBQUksSUFBSSxDQUFDLENBQUMsRUFBRSxDQUFDLEVBQUUsQ0FBQyxFQUFFLENBQUMsQ0FBQyxFQUFFO1lBQy9CLE1BQU0sSUFBSSxHQUFlO2dCQUN2QixZQUFZLEVBQUUsSUFBSTtnQkFDbEIsSUFBSTtnQkFDSixJQUFJLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxZQUFZLEVBQUUsWUFBWSxFQUFFLElBQUksQ0FBQzthQUNqRCxDQUFDO1lBQ0YsSUFBSSxDQUFDLE9BQU8sQ0FBQyxFQUFFLE9BQU8sRUFBRSxJQUFJLEVBQUUsQ0FBQyxDQUFDO1NBQ2pDO1FBRUQsMEJBQTBCO1FBQzFCLE1BQU0sSUFBSSxHQUFHLElBQUksa0VBQWMsQ0FBQyxFQUFFLElBQUksRUFBRSxVQUFVLEVBQUUsQ0FBQyxDQUFDO1FBRXRELHVFQUF1RTtRQUN2RSxNQUFNLGNBQWMsR0FBRyxDQUFDLFFBQW9DLEVBQVEsRUFBRTtZQUNwRSxJQUFJLENBQUMsS0FBTSxDQUFDLE1BQU0sbUNBQ2IsNEVBQXdCLEdBQ3ZCLFFBQVEsQ0FBQyxHQUFHLENBQUMsY0FBYyxDQUFDLENBQUMsU0FBd0IsQ0FDMUQsQ0FBQztRQUNKLENBQUMsQ0FBQztRQUNGLEtBQUssT0FBTyxDQUFDLEdBQUcsQ0FBQztZQUNmLGVBQWUsQ0FBQyxJQUFJLENBQUMseUNBQXlDLENBQUM7WUFDL0QsR0FBRyxDQUFDLFFBQVE7U0FDYixDQUFDLENBQUMsSUFBSSxDQUFDLENBQUMsQ0FBQyxRQUFRLENBQUMsRUFBRSxFQUFFO1lBQ3JCLGNBQWMsQ0FBQyxRQUFRLENBQUMsQ0FBQztZQUN6QixRQUFRLENBQUMsT0FBTyxDQUFDLE9BQU8sQ0FBQyxjQUFjLENBQUMsQ0FBQztRQUMzQyxDQUFDLENBQUMsQ0FBQztRQUVILHVCQUF1QjtRQUN2QixTQUFTLENBQUMsa0JBQWtCLENBQzFCLG1EQUFtRCxFQUNuRDtZQUNFLElBQUk7WUFDSixLQUFLLEVBQUUsT0FBTztZQUNkLElBQUksRUFBRSxDQUFDO1lBQ1AsUUFBUSxFQUFFLEdBQUcsRUFBRTtnQkFDYixPQUFPLENBQ0wsQ0FBQyxDQUFDLEtBQUssQ0FBQyxhQUFhLElBQUksYUFBYSxDQUFDLEdBQUcsQ0FBQyxLQUFLLENBQUMsYUFBYSxDQUFDLENBQ2hFLENBQUM7WUFDSixDQUFDO1NBQ0YsQ0FDRixDQUFDO0lBQ0osQ0FBQztDQUNGLENBQUM7QUFFRjs7R0FFRztBQUNILE1BQU0sYUFBYSxHQUFnQztJQUNqRCxFQUFFLEVBQUUsa0RBQWtEO0lBQ3RELFFBQVEsRUFBRSxDQUNSLEdBQW9CLEVBQ3BCLE9BQXVCLEVBQ3ZCLGFBQTZCLEVBQzdCLEVBQUU7UUFDRixhQUFhLENBQUMsaUJBQWlCLENBQUMsQ0FBQyxNQUFxQixFQUFFLEVBQUUsQ0FDeEQsTUFBTSxJQUFJLE9BQU8sQ0FBQyxHQUFHLENBQUMsTUFBTSxDQUFDO1lBQzNCLENBQUMsQ0FBRSxNQUFzQyxDQUFDLE9BQU8sQ0FBQyxNQUFNO1lBQ3hELENBQUMsQ0FBQyxJQUFJLENBQ1QsQ0FBQztJQUNKLENBQUM7SUFDRCxRQUFRLEVBQUUsQ0FBQyxrRUFBYyxFQUFFLGtFQUFjLENBQUM7SUFDMUMsU0FBUyxFQUFFLElBQUk7Q0FDaEIsQ0FBQztBQUVGLE1BQU0sZUFBZSxHQUFnQztJQUNuRCxFQUFFLEVBQUUsNENBQTRDO0lBQ2hELFFBQVEsRUFBRSxDQUFDLGtFQUFjLENBQUM7SUFDMUIsUUFBUSxFQUFFLENBQUMsNkVBQTBCLENBQUM7SUFDdEMsUUFBUSxFQUFFLGtDQUFrQztJQUM1QyxTQUFTLEVBQUUsSUFBSTtDQUNoQixDQUFDO0FBRUY7O0dBRUc7QUFDSCxNQUFNLGNBQWMsR0FBZ0M7SUFDbEQsRUFBRSxFQUFFLHlDQUF5QztJQUM3QyxRQUFRLEVBQUUsQ0FBQywrRUFBdUIsQ0FBQztJQUNuQyxTQUFTLEVBQUUsSUFBSTtJQUNmLFFBQVEsRUFBRSxDQUFDLEdBQW9CLEVBQUUsUUFBaUMsRUFBRSxFQUFFO1FBQ3BFLFFBQVEsQ0FBQyxHQUFHLENBQUMsNkJBQTZCLEVBQUUsNEVBQXdCLENBQUMsQ0FBQztJQUN4RSxDQUFDO0NBQ0YsQ0FBQztBQUVGLE1BQU0sb0JBQW9CLEdBQWdDO0lBQ3hELEVBQUUsRUFBRSxrREFBa0Q7SUFDdEQsUUFBUSxFQUFFO1FBQ1Isa0VBQWM7UUFDZCwwRUFBNkI7UUFDN0IsK0RBQWtCO1FBQ2xCLHNFQUF5QjtLQUMxQjtJQUVELFFBQVEsRUFBRSxnQ0FBZ0M7SUFDMUMsU0FBUyxFQUFFLElBQUk7Q0FDaEIsQ0FBQztBQUVGOztHQUVHO0FBQ0gsTUFBTSxPQUFPLEdBQWlDO0lBQzVDLE1BQU07SUFDTixhQUFhO0lBQ2IsZUFBZTtJQUNmLG9CQUFvQjtJQUNwQixjQUFjO0lBQ2QsY0FBYztDQUNmLENBQUM7QUFDRixpRUFBZSxPQUFPLEVBQUM7QUFFdkI7O0dBRUc7QUFDSCxTQUFTLFFBQVEsQ0FDZixHQUFvQixFQUNwQixjQUErQixFQUMvQixjQUFtQyxFQUNuQyxlQUFpQyxFQUNqQyxVQUF1QixFQUN2QixjQUFzQyxFQUN0QyxPQUErQixFQUMvQixRQUEwQixFQUMxQixJQUFzQixFQUN0QixRQUFnQyxFQUNoQyxjQUE2QyxFQUM3QyxXQUE0QyxFQUM1QyxlQUE4QztJQUU5QyxNQUFNLEVBQUUsR0FBRyxNQUFNLENBQUMsRUFBRSxDQUFDO0lBQ3JCLE1BQU0sS0FBSyxHQUFHLFVBQVUsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUM7SUFDNUMsTUFBTSxTQUFTLEdBQUcsUUFBUSxDQUFDO0lBQzNCLElBQUksY0FJUyxDQUFDO0lBRWQsSUFBSSxlQUFlLEVBQUU7UUFDbkIsY0FBYyxHQUFHLDBFQUFvQixDQUNuQyxlQUFlLEVBQ2YsZUFBZSxFQUNmLCtDQUFPLEVBQ1AsRUFBRSxFQUNGLFVBQVUsQ0FDWCxDQUFDO0tBQ0g7SUFFRCxNQUFNLE9BQU8sR0FBRyxJQUFJLHFFQUFpQixDQUFDO1FBQ3BDLGNBQWM7UUFDZCxjQUFjLEVBQUU7WUFDZCxJQUFJLEVBQUUsK0NBQU87WUFDYixLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxRQUFRLENBQUM7WUFDekIsU0FBUyxFQUFFLENBQUMsVUFBVSxFQUFFLEdBQUcsQ0FBQztZQUM1QixVQUFVLEVBQUUsQ0FBQyxVQUFVLEVBQUUsR0FBRyxDQUFDO1lBQzdCLGNBQWM7WUFDZCxVQUFVO1NBQ1g7S0FDRixDQUFDLENBQUM7SUFDSCxNQUFNLEVBQUUsUUFBUSxFQUFFLFFBQVEsRUFBRSxLQUFLLEVBQUUsR0FBRyxHQUFHLENBQUM7SUFDMUMsTUFBTSxPQUFPLEdBQUcsSUFBSSwrREFBYSxDQUE4QjtRQUM3RCxTQUFTO0tBQ1YsQ0FBQyxDQUFDO0lBQ0gsTUFBTSxTQUFTLEdBQUcsR0FBRyxFQUFFLENBQ3JCLE9BQU8sQ0FBQyxhQUFhLEtBQUssSUFBSTtRQUM5QixPQUFPLENBQUMsYUFBYSxLQUFLLEtBQUssQ0FBQyxhQUFhLENBQUM7SUFFaEQsTUFBTSwwQkFBMEIsR0FBRyxJQUFJLEdBQUcsQ0FBMEI7UUFDbEU7WUFDRSxRQUFRO1lBQ1I7Z0JBQ0U7b0JBQ0UsT0FBTyxFQUFFLElBQUk7b0JBQ2IsUUFBUSxFQUFFLHNCQUFzQjtvQkFDaEMsYUFBYSxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsYUFBYSxDQUFDO29CQUN0QyxZQUFZLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxpQkFBaUIsQ0FBQztvQkFDekMsT0FBTyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsMEJBQTBCLENBQUM7aUJBQzlDO2FBQ0Y7U0FDRjtRQUNEO1lBQ0UsT0FBTztZQUNQO2dCQUNFO29CQUNFLE9BQU8sRUFBRSxJQUFJO29CQUNiLFFBQVEsRUFBRSxxQkFBcUI7b0JBQy9CLGFBQWEsRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLFlBQVksQ0FBQztvQkFDckMsWUFBWSxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsZ0JBQWdCLENBQUM7b0JBQ3hDLE9BQU8sRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLHlCQUF5QixDQUFDO2lCQUM3QzthQUNGO1NBQ0Y7UUFDRDtZQUNFLEdBQUc7WUFDSDtnQkFDRTtvQkFDRSxPQUFPLEVBQUUsR0FBRztvQkFDWixRQUFRLEVBQUUsd0JBQXdCO29CQUNsQyxhQUFhLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxRQUFRLENBQUM7b0JBQ2pDLFlBQVksRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLFlBQVksQ0FBQztvQkFDcEMsT0FBTyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMscUJBQXFCLENBQUM7aUJBQ3pDO2FBQ0Y7U0FDRjtLQUNGLENBQUMsQ0FBQztJQUVILGtKQUFrSjtJQUNsSixNQUFNLDJCQUEyQixHQUFHLEtBQUssSUFBaUMsRUFBRTs7UUFDMUUsTUFBTSxZQUFZLEdBQUcsR0FBRyxDQUFDLGNBQWMsQ0FBQyxXQUFXLENBQUM7UUFDcEQsTUFBTSxZQUFZLENBQUMsS0FBSyxDQUFDO1FBQ3pCLElBQUksU0FBUyxHQUFHLElBQUksR0FBRyxFQUFpQixDQUFDO1FBQ3pDLE1BQU0sS0FBSyxHQUFHLHdCQUFZLENBQUMsS0FBSywwQ0FBRSxXQUFXLG1DQUFJLEVBQUUsQ0FBQztRQUNwRCxNQUFNLENBQUMsSUFBSSxDQUFDLEtBQUssQ0FBQyxDQUFDLE9BQU8sQ0FBQyxJQUFJLENBQUMsRUFBRTtZQUNoQyxNQUFNLFNBQVMsR0FBRyxLQUFLLENBQUMsSUFBSSxDQUFDLENBQUM7WUFDOUIsSUFBSSxTQUFTLEVBQUU7Z0JBQ2IsTUFBTSxJQUFJLEdBQUcsMEJBQTBCLENBQUMsR0FBRyxDQUFDLFNBQVMsQ0FBQyxRQUFRLENBQUMsQ0FBQztnQkFDaEUsSUFBSSxhQUFKLElBQUksdUJBQUosSUFBSSxDQUFFLE9BQU8sQ0FBQyxHQUFHLENBQUMsRUFBRSxDQUFDLFNBQVMsQ0FBQyxHQUFHLENBQUMsR0FBRyxDQUFDLENBQUMsQ0FBQzthQUMxQztRQUNILENBQUMsQ0FBQyxDQUFDO1FBQ0gsT0FBTyxTQUFTLENBQUM7SUFDbkIsQ0FBQyxDQUFDO0lBRUYsNEJBQTRCO0lBQzVCLElBQUksUUFBUSxFQUFFO1FBQ1osS0FBSyxRQUFRLENBQUMsT0FBTyxDQUFDLE9BQU8sRUFBRTtZQUM3QixPQUFPLEVBQUUsaUJBQWlCO1lBQzFCLElBQUksRUFBRSxNQUFNLENBQUMsRUFBRSxDQUFDLENBQUMsRUFBRSxJQUFJLEVBQUUsTUFBTSxDQUFDLE9BQU8sQ0FBQyxJQUFJLEVBQUUsT0FBTyxFQUFFLCtDQUFPLEVBQUUsQ0FBQztZQUNqRSxJQUFJLEVBQUUsTUFBTSxDQUFDLEVBQUUsQ0FBQyxNQUFNLENBQUMsT0FBTyxDQUFDLElBQUk7U0FDcEMsQ0FBQyxDQUFDO0tBQ0o7SUFFRCx5Q0FBeUM7SUFDekMsMkNBQTJDO0lBQzNDLE9BQU8sQ0FBQyxHQUFHLENBQUMsQ0FBQyxlQUFlLENBQUMsSUFBSSxDQUFDLEVBQUUsQ0FBQyxFQUFFLFFBQVEsQ0FBQyxDQUFDO1NBQzlDLElBQUksQ0FBQyxDQUFDLENBQUMsUUFBUSxDQUFDLEVBQUUsRUFBRTtRQUNuQiwrREFBdUIsQ0FBQyxRQUFRLEVBQUUsUUFBUSxDQUFDLENBQUM7UUFDNUMsOERBQXNCLENBQUMsT0FBTyxDQUFDLENBQUM7UUFDaEMsUUFBUSxDQUFDLE9BQU8sQ0FBQyxPQUFPLENBQUMsR0FBRyxFQUFFO1lBQzVCLCtEQUF1QixDQUFDLFFBQVEsRUFBRSxRQUFRLENBQUMsQ0FBQztZQUM1Qyw4REFBc0IsQ0FBQyxPQUFPLENBQUMsQ0FBQztRQUNsQyxDQUFDLENBQUMsQ0FBQztJQUNMLENBQUMsQ0FBQztTQUNELEtBQUssQ0FBQyxDQUFDLE1BQWEsRUFBRSxFQUFFO1FBQ3ZCLE9BQU8sQ0FBQyxLQUFLLENBQUMsTUFBTSxDQUFDLE9BQU8sQ0FBQyxDQUFDO1FBQzlCLDhEQUFzQixDQUFDLE9BQU8sQ0FBQyxDQUFDO0lBQ2xDLENBQUMsQ0FBQyxDQUFDO0lBRUwsT0FBTyxDQUFDLGFBQWEsQ0FBQyxPQUFPLENBQUMsQ0FBQyxNQUFNLEVBQUUsTUFBTSxFQUFFLEVBQUU7UUFDL0MsNkRBQTZEO1FBQzdELE1BQU0sQ0FBQyxPQUFPLENBQUMsV0FBVyxDQUFDLE9BQU8sQ0FBQyxHQUFHLEVBQUU7WUFDdEMsS0FBSyxPQUFPLENBQUMsSUFBSSxDQUFDLE1BQU0sQ0FBQyxDQUFDO1FBQzVCLENBQUMsQ0FBQyxDQUFDO1FBQ0gsS0FBSyxPQUFPLENBQUMsR0FBRyxDQUFDLE1BQU0sQ0FBQyxDQUFDO1FBQ3pCLDZEQUFxQixDQUFDLE1BQU0sQ0FBQyxPQUFPLENBQUMsQ0FBQztJQUN4QyxDQUFDLENBQUMsQ0FBQztJQUNILEdBQUcsQ0FBQyxXQUFXLENBQUMsZ0JBQWdCLENBQUMsT0FBTyxDQUFDLENBQUM7SUFFMUMsc0NBQXNDO0lBQ3RDLE9BQU8sQ0FBQyxXQUFXLENBQUMsT0FBTyxDQUFDLENBQUMsTUFBTSxFQUFFLE1BQU0sRUFBRSxFQUFFO1FBQzdDLDZEQUFxQixDQUFDLE1BQU0sQ0FBQyxPQUFPLENBQUMsQ0FBQztJQUN4QyxDQUFDLENBQUMsQ0FBQztJQUVILDREQUFvQixDQUNsQixRQUFRLEVBQ1IsZUFBZSxFQUNmLEtBQUssRUFDTCxFQUFFLEVBQ0YsU0FBUyxFQUNULE9BQU8sRUFDUCxjQUFjLEVBQ2QsY0FBYyxFQUNkLGNBQWMsQ0FDZixDQUFDO0lBRUYsTUFBTSxpQkFBaUIsR0FBRyxJQUFJLCtEQUFhLENBQ3pDO1FBQ0UsU0FBUyxFQUFFLFlBQVk7S0FDeEIsQ0FDRixDQUFDO0lBRUYsNENBQTRDO0lBQzVDLElBQUksUUFBUSxFQUFFO1FBQ1osS0FBSyxRQUFRLENBQUMsT0FBTyxDQUFDLGlCQUFpQixFQUFFO1lBQ3ZDLE9BQU8sRUFBRSxpRUFBeUI7WUFDbEMsSUFBSSxFQUFFLE1BQU0sQ0FBQyxFQUFFLENBQUMsQ0FBQztnQkFDZixPQUFPLEVBQUUsTUFBTSxDQUFDLE9BQU8sQ0FBQyxPQUFPO2dCQUMvQixLQUFLLEVBQUUsTUFBTSxDQUFDLE9BQU8sQ0FBQyxLQUFLLENBQUMsS0FBSztnQkFDakMsUUFBUSxFQUFFLE1BQU0sQ0FBQyxPQUFPLENBQUMsUUFBUTtnQkFDakMsUUFBUSxFQUFFLE1BQU0sQ0FBQyxPQUFPLENBQUMsRUFBRTthQUM1QixDQUFDO1lBQ0YsSUFBSSxFQUFFLE1BQU0sQ0FBQyxFQUFFLENBQUMsTUFBTSxDQUFDLE9BQU8sQ0FBQyxFQUFFO1NBQ2xDLENBQUMsQ0FBQztLQUNKO0lBRUQseUVBQWlDLENBQy9CLEdBQUcsRUFDSCxjQUFjLEVBQ2QsaUJBQWlCLEVBQ2pCLEtBQUssQ0FDTixDQUFDO0lBRUYsb0RBQW9EO0lBQ3BELElBQUksUUFBUSxFQUFFO1FBQ1osaUVBQXlCLENBQUMsUUFBUSxFQUFFLEtBQUssQ0FBQyxDQUFDO0tBQzVDO0lBRUQsSUFBSSxPQUFPLEVBQUU7UUFDWCxnRUFBd0IsQ0FBQyxPQUFPLEVBQUUsS0FBSyxDQUFDLENBQUM7S0FDMUM7SUFFRCxJQUFJLElBQUksRUFBRTtRQUNSLDZEQUFxQixDQUFDLElBQUksRUFBRSxPQUFPLEVBQUUsY0FBYyxFQUFFLFNBQVMsQ0FBQyxDQUFDO0tBQ2pFO0lBRUQsMkJBQTJCLEVBQUU7U0FDMUIsSUFBSSxDQUFDLHdCQUF3QixDQUFDLEVBQUU7UUFDL0IsSUFBSSxRQUFRLEVBQUU7WUFDWiwrRUFBdUMsQ0FDckMsUUFBUSxFQUNSLEtBQUssRUFDTCx3QkFBd0IsQ0FDekIsQ0FBQztTQUNIO1FBRUQsSUFBSSxPQUFPLEVBQUU7WUFDWCw4RUFBc0MsQ0FDcEMsT0FBTyxFQUNQLEtBQUssRUFDTCx3QkFBd0IsQ0FDekIsQ0FBQztTQUNIO1FBRUQsSUFBSSxJQUFJLEVBQUU7WUFDUiwyRUFBbUMsQ0FBQyxJQUFJLEVBQUUsd0JBQXdCLENBQUMsQ0FBQztTQUNyRTtJQUNILENBQUMsQ0FBQztTQUNELEtBQUssQ0FBQyxDQUFDLE1BQWEsRUFBRSxFQUFFO1FBQ3ZCLE9BQU8sQ0FBQyxLQUFLLENBQUMsTUFBTSxDQUFDLE9BQU8sQ0FBQyxDQUFDO0lBQ2hDLENBQUMsQ0FBQyxDQUFDO0lBRUwsSUFBSSxXQUFXLEVBQUU7UUFDZixXQUFXLENBQUMsR0FBRyxDQUFDLElBQUksK0VBQTJCLENBQUMsT0FBTyxDQUFDLENBQUMsQ0FBQztRQUMxRCxXQUFXLENBQUMsR0FBRyxDQUFDLElBQUksa0ZBQThCLENBQUMsT0FBTyxDQUFDLENBQUMsQ0FBQztRQUM3RCxXQUFXLENBQUMsR0FBRyxDQUFDLElBQUksZ0ZBQTRCLENBQUMsT0FBTyxDQUFDLENBQUMsQ0FBQztLQUM1RDtJQUVELE9BQU8sT0FBTyxDQUFDO0FBQ2pCLENBQUM7QUFFRDs7R0FFRztBQUNILFNBQVMsa0NBQWtDLENBQ3pDLEdBQW9CLEVBQ3BCLGFBQTZCLEVBQzdCLE9BQTBDLEVBQzFDLFVBQThCO0lBRTlCLElBQUksQ0FBQyxPQUFPLEVBQUU7UUFDWixPQUFPO0tBQ1I7SUFFRCxxRUFBNkIsQ0FDM0IsR0FBRyxDQUFDLFFBQVEsRUFDWixhQUFhLEVBQ2IsT0FBTyxFQUNQLFVBQVUsQ0FDWCxDQUFDO0lBQ0YsTUFBTSxjQUFjLEdBQUcsR0FBRyxDQUFDLGNBQWMsQ0FBQyxRQUFRLENBQUM7SUFFbkQsTUFBTSxlQUFlLEdBQUcsSUFBSSxHQUFHLEVBQXNDLENBQUM7SUFDdEUsTUFBTSxlQUFlLEdBQUcsS0FBSyxFQUMzQixDQUFpQixFQUNqQixNQUFtQyxFQUNuQyxFQUFFO1FBQ0YsTUFBTSxnQkFBZ0IsR0FBRztZQUN2QixNQUFNLEVBQUUsTUFBTSxDQUFDLE9BQU8sQ0FBQyxNQUFNO1lBQzdCLE1BQU07U0FDUCxDQUFDO1FBRUYsTUFBTSxPQUFPLENBQUMsZUFBZSxDQUFDLGdCQUFnQixDQUFDLENBQUM7UUFDaEQsTUFBTSxnQkFBZ0IsR0FBRyxDQUN2QixDQUFtQixFQUNuQixNQUF3QixFQUN4QixFQUFFO1lBQ0YsTUFBTSxVQUFVLEdBQUcsZUFBZSxDQUFDLEdBQUcsQ0FBQyxNQUFNLENBQUMsRUFBRSxDQUFDLENBQUM7WUFDbEQsOEJBQThCO1lBQzlCLE1BQU0sS0FBSyxHQUFHLHdEQUFJLENBQUMsTUFBTSxFQUFFLENBQUMsQ0FBQyxFQUFFLENBQUMsQ0FBQyxDQUFDLElBQUksS0FBSyxNQUFNLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxDQUFDO1lBQ2hFLElBQUksS0FBSyxFQUFFO2dCQUNULGtEQUFrRDtnQkFDbEQsNENBQTRDO2dCQUM1QyxJQUFJLFVBQVUsSUFBSSxVQUFVLENBQUMsRUFBRSxLQUFLLEtBQUssQ0FBQyxFQUFFLEVBQUU7b0JBQzVDLE9BQU87aUJBQ1I7Z0JBQ0QscURBQXFEO2dCQUNyRCw2QkFBNkI7Z0JBQzdCLElBQUksVUFBVSxFQUFFO29CQUNkLGVBQWUsQ0FBQyxNQUFNLENBQUMsTUFBTSxDQUFDLEVBQUUsQ0FBQyxDQUFDO29CQUNsQyxVQUFVLENBQUMsT0FBTyxFQUFFLENBQUM7aUJBQ3RCO2dCQUNELE1BQU0sT0FBTyxHQUFHLGNBQWMsQ0FBQyxTQUFTLENBQUMsRUFBRSxLQUFLLEVBQUUsQ0FBQyxDQUFDO2dCQUNwRCxNQUFNLG1CQUFtQixHQUFHO29CQUMxQixNQUFNLEVBQUUsTUFBTSxDQUFDLE9BQU8sQ0FBQyxNQUFNO29CQUM3QixNQUFNO29CQUNOLE9BQU87aUJBQ1IsQ0FBQztnQkFDRixPQUFPLENBQUMsZUFBZSxDQUFDLG1CQUFtQixDQUFDLENBQUMsS0FBSyxDQUFDLE9BQU8sQ0FBQyxLQUFLLENBQUMsQ0FBQztnQkFDbEUsZUFBZSxDQUFDLEdBQUcsQ0FBQyxNQUFNLENBQUMsRUFBRSxFQUFFLE9BQU8sQ0FBQyxDQUFDO2FBQ3pDO2lCQUFNO2dCQUNMLHVDQUF1QztnQkFDdkMsNENBQTRDO2dCQUM1QyxzQ0FBc0M7Z0JBQ3RDLElBQUksVUFBVSxFQUFFO29CQUNkLGVBQWUsQ0FBQyxNQUFNLENBQUMsTUFBTSxDQUFDLEVBQUUsQ0FBQyxDQUFDO29CQUNsQyxVQUFVLENBQUMsT0FBTyxFQUFFLENBQUM7aUJBQ3RCO2FBQ0Y7UUFDSCxDQUFDLENBQUM7UUFFRixnQkFBZ0IsQ0FBQyxjQUFjLEVBQUUsMkRBQU8sQ0FBQyxjQUFjLENBQUMsT0FBTyxFQUFFLENBQUMsQ0FBQyxDQUFDO1FBQ3BFLGNBQWMsQ0FBQyxjQUFjLENBQUMsT0FBTyxDQUFDLGdCQUFnQixDQUFDLENBQUM7UUFFeEQsTUFBTSxDQUFDLFFBQVEsQ0FBQyxPQUFPLENBQUMsR0FBRyxFQUFFO1lBQzNCLGNBQWMsQ0FBQyxjQUFjLENBQUMsVUFBVSxDQUFDLGdCQUFnQixDQUFDLENBQUM7WUFDM0QsTUFBTSxPQUFPLEdBQUcsZUFBZSxDQUFDLEdBQUcsQ0FBQyxNQUFNLENBQUMsRUFBRSxDQUFDLENBQUM7WUFDL0MsSUFBSSxPQUFPLEVBQUU7Z0JBQ1gsZUFBZSxDQUFDLE1BQU0sQ0FBQyxNQUFNLENBQUMsRUFBRSxDQUFDLENBQUM7Z0JBQ2xDLE9BQU8sQ0FBQyxPQUFPLEVBQUUsQ0FBQzthQUNuQjtRQUNILENBQUMsQ0FBQyxDQUFDO0lBQ0wsQ0FBQyxDQUFDO0lBQ0YsYUFBYSxDQUFDLFdBQVcsQ0FBQyxPQUFPLENBQUMsZUFBZSxDQUFDLENBQUM7SUFDbkQsT0FBTyxDQUFDLHNCQUFzQixDQUFDLE9BQU8sQ0FBQyxHQUFHLEVBQUU7UUFDMUMsYUFBYSxDQUFDLE9BQU8sQ0FBQyxZQUFZLENBQUMsRUFBRTtZQUNuQyxlQUFlLENBQUMsYUFBYSxFQUFFLFlBQVksQ0FBQyxDQUFDLEtBQUssQ0FBQyxPQUFPLENBQUMsS0FBSyxDQUFDLENBQUM7UUFDcEUsQ0FBQyxDQUFDLENBQUM7SUFDTCxDQUFDLENBQUMsQ0FBQztBQUNMLENBQUM7QUFFRCxTQUFTLGdDQUFnQyxDQUN2QyxHQUFvQixFQUNwQixPQUF1QixFQUN2QixpQkFBZ0QsRUFDaEQsY0FBa0MsRUFDbEMsZ0JBQTJDO0lBRTNDLE9BQU8sQ0FBQyxXQUFXLENBQUMsT0FBTyxDQUFDLEtBQUssRUFBRSxDQUFDLEVBQUUsTUFBTSxFQUFFLEVBQUU7UUFDOUMsTUFBTSxPQUFPLEdBQUcsSUFBSSxxRUFBaUIsQ0FBQyxNQUFNLEVBQUU7WUFDNUMsaUJBQWlCO1lBQ2pCLGNBQWM7WUFDZCw0QkFBNEIsRUFBRSxnQkFBZ0I7WUFDOUMsV0FBVyxFQUFFLEdBQUcsQ0FBQyxXQUFXO1NBQzdCLENBQUMsQ0FBQztRQUNILGlCQUFpQixDQUFDLGVBQWUsQ0FBQyxNQUFNLENBQUMsT0FBTyxDQUFDLElBQUksRUFBRSxPQUFPLENBQUMsQ0FBQztJQUNsRSxDQUFDLENBQUMsQ0FBQztBQUNMLENBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZmlsZWVkaXRvci1leHRlbnNpb24vc3JjL2NvbW1hbmRzLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9maWxlZWRpdG9yLWV4dGVuc2lvbi9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBKdXB5dGVyRnJvbnRFbmQgfSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQge1xuICBDbGlwYm9hcmQsXG4gIElDb21tYW5kUGFsZXR0ZSxcbiAgSVNlc3Npb25Db250ZXh0RGlhbG9ncyxcbiAgTWFpbkFyZWFXaWRnZXQsXG4gIHNlc3Npb25Db250ZXh0RGlhbG9ncyxcbiAgV2lkZ2V0VHJhY2tlclxufSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQge1xuICBDb2RlRWRpdG9yLFxuICBDb2RlVmlld2VyV2lkZ2V0LFxuICBJRWRpdG9yU2VydmljZXNcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvY29kZWVkaXRvcic7XG5pbXBvcnQgeyBDb2RlTWlycm9yRWRpdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29kZW1pcnJvcic7XG5pbXBvcnQgeyBJQ29tcGxldGlvblByb3ZpZGVyTWFuYWdlciB9IGZyb20gJ0BqdXB5dGVybGFiL2NvbXBsZXRlcic7XG5pbXBvcnQgeyBJQ29uc29sZVRyYWNrZXIgfSBmcm9tICdAanVweXRlcmxhYi9jb25zb2xlJztcbmltcG9ydCB7IE1hcmtkb3duQ29kZUJsb2NrcywgUGF0aEV4dCB9IGZyb20gJ0BqdXB5dGVybGFiL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBJRG9jdW1lbnRXaWRnZXQgfSBmcm9tICdAanVweXRlcmxhYi9kb2NyZWdpc3RyeSc7XG5pbXBvcnQgeyBJRmlsZUJyb3dzZXJGYWN0b3J5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvZmlsZWJyb3dzZXInO1xuaW1wb3J0IHsgRmlsZUVkaXRvciwgSUVkaXRvclRyYWNrZXIgfSBmcm9tICdAanVweXRlcmxhYi9maWxlZWRpdG9yJztcbmltcG9ydCB7IElMYXVuY2hlciB9IGZyb20gJ0BqdXB5dGVybGFiL2xhdW5jaGVyJztcbmltcG9ydCB7IElNYWluTWVudSB9IGZyb20gJ0BqdXB5dGVybGFiL21haW5tZW51JztcbmltcG9ydCB7IElTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHtcbiAgSVRyYW5zbGF0b3IsXG4gIG51bGxUcmFuc2xhdG9yLFxuICBUcmFuc2xhdGlvbkJ1bmRsZVxufSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQge1xuICBjb25zb2xlSWNvbixcbiAgY29weUljb24sXG4gIGN1dEljb24sXG4gIExhYkljb24sXG4gIG1hcmtkb3duSWNvbixcbiAgcGFzdGVJY29uLFxuICByZWRvSWNvbixcbiAgdGV4dEVkaXRvckljb24sXG4gIHVuZG9JY29uXG59IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0IHsgdG9BcnJheSB9IGZyb20gJ0BsdW1pbm8vYWxnb3JpdGhtJztcbmltcG9ydCB7IENvbW1hbmRSZWdpc3RyeSB9IGZyb20gJ0BsdW1pbm8vY29tbWFuZHMnO1xuaW1wb3J0IHtcbiAgSlNPTk9iamVjdCxcbiAgUmVhZG9ubHlKU09OT2JqZWN0LFxuICBSZWFkb25seVBhcnRpYWxKU09OT2JqZWN0XG59IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IHNlbGVjdEFsbCB9IGZyb20gJ0Bjb2RlbWlycm9yL2NvbW1hbmRzJztcblxuY29uc3QgYXV0b0Nsb3NpbmdCcmFja2V0c05vdGVib29rID0gJ25vdGVib29rOnRvZ2dsZS1hdXRvY2xvc2luZy1icmFja2V0cyc7XG5jb25zdCBhdXRvQ2xvc2luZ0JyYWNrZXRzQ29uc29sZSA9ICdjb25zb2xlOnRvZ2dsZS1hdXRvY2xvc2luZy1icmFja2V0cyc7XG50eXBlIHdyYXBwaW5nTW9kZSA9ICdvbicgfCAnb2ZmJyB8ICd3b3JkV3JhcENvbHVtbicgfCAnYm91bmRlZCc7XG5cbi8qKlxuICogVGhlIGNvbW1hbmQgSURzIHVzZWQgYnkgdGhlIGZpbGVlZGl0b3IgcGx1Z2luLlxuICovXG5leHBvcnQgbmFtZXNwYWNlIENvbW1hbmRJRHMge1xuICBleHBvcnQgY29uc3QgY3JlYXRlTmV3ID0gJ2ZpbGVlZGl0b3I6Y3JlYXRlLW5ldyc7XG5cbiAgZXhwb3J0IGNvbnN0IGNyZWF0ZU5ld01hcmtkb3duID0gJ2ZpbGVlZGl0b3I6Y3JlYXRlLW5ldy1tYXJrZG93bi1maWxlJztcblxuICBleHBvcnQgY29uc3QgY2hhbmdlRm9udFNpemUgPSAnZmlsZWVkaXRvcjpjaGFuZ2UtZm9udC1zaXplJztcblxuICBleHBvcnQgY29uc3QgbGluZU51bWJlcnMgPSAnZmlsZWVkaXRvcjp0b2dnbGUtbGluZS1udW1iZXJzJztcblxuICBleHBvcnQgY29uc3QgY3VycmVudExpbmVOdW1iZXJzID0gJ2ZpbGVlZGl0b3I6dG9nZ2xlLWN1cnJlbnQtbGluZS1udW1iZXJzJztcblxuICBleHBvcnQgY29uc3QgbGluZVdyYXAgPSAnZmlsZWVkaXRvcjp0b2dnbGUtbGluZS13cmFwJztcblxuICBleHBvcnQgY29uc3QgY3VycmVudExpbmVXcmFwID0gJ2ZpbGVlZGl0b3I6dG9nZ2xlLWN1cnJlbnQtbGluZS13cmFwJztcblxuICBleHBvcnQgY29uc3QgY2hhbmdlVGFicyA9ICdmaWxlZWRpdG9yOmNoYW5nZS10YWJzJztcblxuICBleHBvcnQgY29uc3QgbWF0Y2hCcmFja2V0cyA9ICdmaWxlZWRpdG9yOnRvZ2dsZS1tYXRjaC1icmFja2V0cyc7XG5cbiAgZXhwb3J0IGNvbnN0IGN1cnJlbnRNYXRjaEJyYWNrZXRzID1cbiAgICAnZmlsZWVkaXRvcjp0b2dnbGUtY3VycmVudC1tYXRjaC1icmFja2V0cyc7XG5cbiAgZXhwb3J0IGNvbnN0IGF1dG9DbG9zaW5nQnJhY2tldHMgPSAnZmlsZWVkaXRvcjp0b2dnbGUtYXV0b2Nsb3NpbmctYnJhY2tldHMnO1xuXG4gIGV4cG9ydCBjb25zdCBhdXRvQ2xvc2luZ0JyYWNrZXRzVW5pdmVyc2FsID1cbiAgICAnZmlsZWVkaXRvcjp0b2dnbGUtYXV0b2Nsb3NpbmctYnJhY2tldHMtdW5pdmVyc2FsJztcblxuICBleHBvcnQgY29uc3QgY3JlYXRlQ29uc29sZSA9ICdmaWxlZWRpdG9yOmNyZWF0ZS1jb25zb2xlJztcblxuICBleHBvcnQgY29uc3QgcmVwbGFjZVNlbGVjdGlvbiA9ICdmaWxlZWRpdG9yOnJlcGxhY2Utc2VsZWN0aW9uJztcblxuICBleHBvcnQgY29uc3QgcmVzdGFydENvbnNvbGUgPSAnZmlsZWVkaXRvcjpyZXN0YXJ0LWNvbnNvbGUnO1xuXG4gIGV4cG9ydCBjb25zdCBydW5Db2RlID0gJ2ZpbGVlZGl0b3I6cnVuLWNvZGUnO1xuXG4gIGV4cG9ydCBjb25zdCBydW5BbGxDb2RlID0gJ2ZpbGVlZGl0b3I6cnVuLWFsbCc7XG5cbiAgZXhwb3J0IGNvbnN0IG1hcmtkb3duUHJldmlldyA9ICdmaWxlZWRpdG9yOm1hcmtkb3duLXByZXZpZXcnO1xuXG4gIGV4cG9ydCBjb25zdCB1bmRvID0gJ2ZpbGVlZGl0b3I6dW5kbyc7XG5cbiAgZXhwb3J0IGNvbnN0IHJlZG8gPSAnZmlsZWVkaXRvcjpyZWRvJztcblxuICBleHBvcnQgY29uc3QgY3V0ID0gJ2ZpbGVlZGl0b3I6Y3V0JztcblxuICBleHBvcnQgY29uc3QgY29weSA9ICdmaWxlZWRpdG9yOmNvcHknO1xuXG4gIGV4cG9ydCBjb25zdCBwYXN0ZSA9ICdmaWxlZWRpdG9yOnBhc3RlJztcblxuICBleHBvcnQgY29uc3Qgc2VsZWN0QWxsID0gJ2ZpbGVlZGl0b3I6c2VsZWN0LWFsbCc7XG5cbiAgZXhwb3J0IGNvbnN0IGludm9rZUNvbXBsZXRlciA9ICdjb21wbGV0ZXI6aW52b2tlLWZpbGUnO1xuXG4gIGV4cG9ydCBjb25zdCBzZWxlY3RDb21wbGV0ZXIgPSAnY29tcGxldGVyOnNlbGVjdC1maWxlJztcblxuICBleHBvcnQgY29uc3Qgb3BlbkNvZGVWaWV3ZXIgPSAnY29kZS12aWV3ZXI6b3Blbic7XG59XG5cbmV4cG9ydCBpbnRlcmZhY2UgSUZpbGVUeXBlRGF0YSBleHRlbmRzIFJlYWRvbmx5SlNPTk9iamVjdCB7XG4gIGZpbGVFeHQ6IHN0cmluZztcbiAgaWNvbk5hbWU6IHN0cmluZztcbiAgbGF1bmNoZXJMYWJlbDogc3RyaW5nO1xuICBwYWxldHRlTGFiZWw6IHN0cmluZztcbiAgY2FwdGlvbjogc3RyaW5nO1xufVxuXG4vKipcbiAqIFRoZSBuYW1lIG9mIHRoZSBmYWN0b3J5IHRoYXQgY3JlYXRlcyBlZGl0b3Igd2lkZ2V0cy5cbiAqL1xuZXhwb3J0IGNvbnN0IEZBQ1RPUlkgPSAnRWRpdG9yJztcblxuY29uc3QgdXNlclNldHRpbmdzID0gW1xuICAnYXV0b0Nsb3NpbmdCcmFja2V0cycsXG4gICdjb2RlRm9sZGluZycsXG4gICdjdXJzb3JCbGlua1JhdGUnLFxuICAnZm9udEZhbWlseScsXG4gICdmb250U2l6ZScsXG4gICdpbnNlcnRTcGFjZXMnLFxuICAnbGluZUhlaWdodCcsXG4gICdsaW5lTnVtYmVycycsXG4gICdsaW5lV3JhcCcsXG4gICdtYXRjaEJyYWNrZXRzJyxcbiAgJ3JlYWRPbmx5JyxcbiAgJ3J1bGVycycsXG4gICdzaG93VHJhaWxpbmdTcGFjZScsXG4gICd0YWJTaXplJyxcbiAgJ3dvcmRXcmFwQ29sdW1uJ1xuXTtcblxuZnVuY3Rpb24gZmlsdGVyVXNlclNldHRpbmdzKGNvbmZpZzogQ29kZUVkaXRvci5JQ29uZmlnKTogQ29kZUVkaXRvci5JQ29uZmlnIHtcbiAgY29uc3QgZmlsdGVyZWRDb25maWcgPSB7IC4uLmNvbmZpZyB9O1xuICAvLyBEZWxldGUgcGFydHMgb2YgdGhlIGNvbmZpZyB0aGF0IGFyZSBub3QgdXNlciBzZXR0aW5ncyAobGlrZSBoYW5kbGVQYXN0ZSkuXG4gIGZvciAobGV0IGsgb2YgT2JqZWN0LmtleXMoY29uZmlnKSkge1xuICAgIGlmICghdXNlclNldHRpbmdzLmluY2x1ZGVzKGspKSB7XG4gICAgICBkZWxldGUgKGNvbmZpZyBhcyBhbnkpW2tdO1xuICAgIH1cbiAgfVxuICByZXR1cm4gZmlsdGVyZWRDb25maWc7XG59XG5cbmxldCBjb25maWc6IENvZGVFZGl0b3IuSUNvbmZpZyA9IGZpbHRlclVzZXJTZXR0aW5ncyhDb2RlRWRpdG9yLmRlZmF1bHRDb25maWcpO1xuXG4vKipcbiAqIEEgdXRpbGl0eSBjbGFzcyBmb3IgYWRkaW5nIGNvbW1hbmRzIGFuZCBtZW51IGl0ZW1zLFxuICogZm9yIHVzZSBieSB0aGUgRmlsZSBFZGl0b3IgZXh0ZW5zaW9uIG9yIG90aGVyIEVkaXRvciBleHRlbnNpb25zLlxuICovXG5leHBvcnQgbmFtZXNwYWNlIENvbW1hbmRzIHtcbiAgLyoqXG4gICAqIEFjY2Vzc29yIGZ1bmN0aW9uIHRoYXQgcmV0dXJucyB0aGUgY3JlYXRlQ29uc29sZSBmdW5jdGlvbiBmb3IgdXNlIGJ5IENyZWF0ZSBDb25zb2xlIGNvbW1hbmRzXG4gICAqL1xuICBmdW5jdGlvbiBnZXRDcmVhdGVDb25zb2xlRnVuY3Rpb24oXG4gICAgY29tbWFuZHM6IENvbW1hbmRSZWdpc3RyeVxuICApOiAoXG4gICAgd2lkZ2V0OiBJRG9jdW1lbnRXaWRnZXQ8RmlsZUVkaXRvcj4sXG4gICAgYXJncz86IFJlYWRvbmx5UGFydGlhbEpTT05PYmplY3RcbiAgKSA9PiBQcm9taXNlPHZvaWQ+IHtcbiAgICByZXR1cm4gYXN5bmMgZnVuY3Rpb24gY3JlYXRlQ29uc29sZShcbiAgICAgIHdpZGdldDogSURvY3VtZW50V2lkZ2V0PEZpbGVFZGl0b3I+LFxuICAgICAgYXJncz86IFJlYWRvbmx5UGFydGlhbEpTT05PYmplY3RcbiAgICApOiBQcm9taXNlPHZvaWQ+IHtcbiAgICAgIGNvbnN0IG9wdGlvbnMgPSBhcmdzIHx8IHt9O1xuICAgICAgY29uc3QgY29uc29sZSA9IGF3YWl0IGNvbW1hbmRzLmV4ZWN1dGUoJ2NvbnNvbGU6Y3JlYXRlJywge1xuICAgICAgICBhY3RpdmF0ZTogb3B0aW9uc1snYWN0aXZhdGUnXSxcbiAgICAgICAgbmFtZTogd2lkZ2V0LmNvbnRleHQuY29udGVudHNNb2RlbD8ubmFtZSxcbiAgICAgICAgcGF0aDogd2lkZ2V0LmNvbnRleHQucGF0aCxcbiAgICAgICAgcHJlZmVycmVkTGFuZ3VhZ2U6IHdpZGdldC5jb250ZXh0Lm1vZGVsLmRlZmF1bHRLZXJuZWxMYW5ndWFnZSxcbiAgICAgICAgcmVmOiB3aWRnZXQuaWQsXG4gICAgICAgIGluc2VydE1vZGU6ICdzcGxpdC1ib3R0b20nXG4gICAgICB9KTtcblxuICAgICAgd2lkZ2V0LmNvbnRleHQucGF0aENoYW5nZWQuY29ubmVjdCgoc2VuZGVyLCB2YWx1ZSkgPT4ge1xuICAgICAgICBjb25zb2xlLnNlc3Npb24uc2V0UGF0aCh2YWx1ZSk7XG4gICAgICAgIGNvbnNvbGUuc2Vzc2lvbi5zZXROYW1lKHdpZGdldC5jb250ZXh0LmNvbnRlbnRzTW9kZWw/Lm5hbWUpO1xuICAgICAgfSk7XG4gICAgfTtcbiAgfVxuXG4gIC8qKlxuICAgKiBVcGRhdGUgdGhlIHNldHRpbmcgdmFsdWVzLlxuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIHVwZGF0ZVNldHRpbmdzKFxuICAgIHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LklTZXR0aW5ncyxcbiAgICBjb21tYW5kczogQ29tbWFuZFJlZ2lzdHJ5XG4gICk6IHZvaWQge1xuICAgIGNvbmZpZyA9IGZpbHRlclVzZXJTZXR0aW5ncyh7XG4gICAgICAuLi5Db2RlRWRpdG9yLmRlZmF1bHRDb25maWcsXG4gICAgICAuLi4oc2V0dGluZ3MuZ2V0KCdlZGl0b3JDb25maWcnKS5jb21wb3NpdGUgYXMgSlNPTk9iamVjdClcbiAgICB9KTtcblxuICAgIC8vIFRyaWdnZXIgYSByZWZyZXNoIG9mIHRoZSByZW5kZXJlZCBjb21tYW5kc1xuICAgIGNvbW1hbmRzLm5vdGlmeUNvbW1hbmRDaGFuZ2VkKCk7XG4gIH1cblxuICAvKipcbiAgICogVXBkYXRlIHRoZSBzZXR0aW5ncyBvZiB0aGUgY3VycmVudCB0cmFja2VyIGluc3RhbmNlcy5cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiB1cGRhdGVUcmFja2VyKFxuICAgIHRyYWNrZXI6IFdpZGdldFRyYWNrZXI8SURvY3VtZW50V2lkZ2V0PEZpbGVFZGl0b3I+PlxuICApOiB2b2lkIHtcbiAgICB0cmFja2VyLmZvckVhY2god2lkZ2V0ID0+IHtcbiAgICAgIHVwZGF0ZVdpZGdldCh3aWRnZXQuY29udGVudCk7XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogVXBkYXRlIHRoZSBzZXR0aW5ncyBvZiBhIHdpZGdldC5cbiAgICogU2tpcCBnbG9iYWwgc2V0dGluZ3MgZm9yIHRyYW5zaWVudCBlZGl0b3Igc3BlY2lmaWMgY29uZmlncy5cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiB1cGRhdGVXaWRnZXQod2lkZ2V0OiBGaWxlRWRpdG9yKTogdm9pZCB7XG4gICAgY29uc3QgZWRpdG9yID0gd2lkZ2V0LmVkaXRvcjtcbiAgICBlZGl0b3Iuc2V0T3B0aW9ucyh7IC4uLmNvbmZpZyB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBXcmFwcGVyIGZ1bmN0aW9uIGZvciBhZGRpbmcgdGhlIGRlZmF1bHQgRmlsZSBFZGl0b3IgY29tbWFuZHNcbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBhZGRDb21tYW5kcyhcbiAgICBjb21tYW5kczogQ29tbWFuZFJlZ2lzdHJ5LFxuICAgIHNldHRpbmdSZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSxcbiAgICB0cmFuczogVHJhbnNsYXRpb25CdW5kbGUsXG4gICAgaWQ6IHN0cmluZyxcbiAgICBpc0VuYWJsZWQ6ICgpID0+IGJvb2xlYW4sXG4gICAgdHJhY2tlcjogV2lkZ2V0VHJhY2tlcjxJRG9jdW1lbnRXaWRnZXQ8RmlsZUVkaXRvcj4+LFxuICAgIGJyb3dzZXJGYWN0b3J5OiBJRmlsZUJyb3dzZXJGYWN0b3J5LFxuICAgIGNvbnNvbGVUcmFja2VyOiBJQ29uc29sZVRyYWNrZXIgfCBudWxsLFxuICAgIHNlc3Npb25EaWFsb2dzOiBJU2Vzc2lvbkNvbnRleHREaWFsb2dzIHwgbnVsbFxuICApOiB2b2lkIHtcbiAgICAvKipcbiAgICAgKiBBZGQgYSBjb21tYW5kIHRvIGNoYW5nZSBmb250IHNpemUgZm9yIEZpbGUgRWRpdG9yXG4gICAgICovXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmNoYW5nZUZvbnRTaXplLCB7XG4gICAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgICAgY29uc3QgZGVsdGEgPSBOdW1iZXIoYXJnc1snZGVsdGEnXSk7XG4gICAgICAgIGlmIChOdW1iZXIuaXNOYU4oZGVsdGEpKSB7XG4gICAgICAgICAgY29uc29sZS5lcnJvcihcbiAgICAgICAgICAgIGAke0NvbW1hbmRJRHMuY2hhbmdlRm9udFNpemV9OiBkZWx0YSBhcmcgbXVzdCBiZSBhIG51bWJlcmBcbiAgICAgICAgICApO1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuICAgICAgICBjb25zdCBzdHlsZSA9IHdpbmRvdy5nZXRDb21wdXRlZFN0eWxlKGRvY3VtZW50LmRvY3VtZW50RWxlbWVudCk7XG4gICAgICAgIGNvbnN0IGNzc1NpemUgPSBwYXJzZUludChcbiAgICAgICAgICBzdHlsZS5nZXRQcm9wZXJ0eVZhbHVlKCctLWpwLWNvZGUtZm9udC1zaXplJyksXG4gICAgICAgICAgMTBcbiAgICAgICAgKTtcbiAgICAgICAgY29uc3QgY3VycmVudFNpemUgPSBjb25maWcuZm9udFNpemUgfHwgY3NzU2l6ZTtcbiAgICAgICAgY29uZmlnLmZvbnRTaXplID0gY3VycmVudFNpemUgKyBkZWx0YTtcbiAgICAgICAgcmV0dXJuIHNldHRpbmdSZWdpc3RyeVxuICAgICAgICAgIC5zZXQoaWQsICdlZGl0b3JDb25maWcnLCBjb25maWcgYXMgdW5rbm93biBhcyBKU09OT2JqZWN0KVxuICAgICAgICAgIC5jYXRjaCgocmVhc29uOiBFcnJvcikgPT4ge1xuICAgICAgICAgICAgY29uc29sZS5lcnJvcihgRmFpbGVkIHRvIHNldCAke2lkfTogJHtyZWFzb24ubWVzc2FnZX1gKTtcbiAgICAgICAgICB9KTtcbiAgICAgIH0sXG4gICAgICBsYWJlbDogYXJncyA9PiB7XG4gICAgICAgIGlmICgoYXJncy5kZWx0YSA/PyAwKSA+IDApIHtcbiAgICAgICAgICByZXR1cm4gYXJncy5pc01lbnVcbiAgICAgICAgICAgID8gdHJhbnMuX18oJ0luY3JlYXNlIFRleHQgRWRpdG9yIEZvbnQgU2l6ZScpXG4gICAgICAgICAgICA6IHRyYW5zLl9fKCdJbmNyZWFzZSBGb250IFNpemUnKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICByZXR1cm4gYXJncy5pc01lbnVcbiAgICAgICAgICAgID8gdHJhbnMuX18oJ0RlY3JlYXNlIFRleHQgRWRpdG9yIEZvbnQgU2l6ZScpXG4gICAgICAgICAgICA6IHRyYW5zLl9fKCdEZWNyZWFzZSBGb250IFNpemUnKTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH0pO1xuXG4gICAgLyoqXG4gICAgICogQWRkIHRoZSBMaW5lIE51bWJlcnMgY29tbWFuZFxuICAgICAqL1xuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5saW5lTnVtYmVycywge1xuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICBjb25maWcubGluZU51bWJlcnMgPSAhY29uZmlnLmxpbmVOdW1iZXJzO1xuICAgICAgICByZXR1cm4gc2V0dGluZ1JlZ2lzdHJ5XG4gICAgICAgICAgLnNldChpZCwgJ2VkaXRvckNvbmZpZycsIGNvbmZpZyBhcyB1bmtub3duIGFzIEpTT05PYmplY3QpXG4gICAgICAgICAgLmNhdGNoKChyZWFzb246IEVycm9yKSA9PiB7XG4gICAgICAgICAgICBjb25zb2xlLmVycm9yKGBGYWlsZWQgdG8gc2V0ICR7aWR9OiAke3JlYXNvbi5tZXNzYWdlfWApO1xuICAgICAgICAgIH0pO1xuICAgICAgfSxcbiAgICAgIGlzRW5hYmxlZCxcbiAgICAgIGlzVG9nZ2xlZDogKCkgPT4gY29uZmlnLmxpbmVOdW1iZXJzLFxuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdMaW5lIE51bWJlcnMnKVxuICAgIH0pO1xuXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmN1cnJlbnRMaW5lTnVtYmVycywge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdTaG93IExpbmUgTnVtYmVycycpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IGxpbmVOdW1iZXJzID0gIXdpZGdldC5jb250ZW50LmVkaXRvci5nZXRPcHRpb24oJ2xpbmVOdW1iZXJzJyk7XG4gICAgICAgIHdpZGdldC5jb250ZW50LmVkaXRvci5zZXRPcHRpb24oJ2xpbmVOdW1iZXJzJywgbGluZU51bWJlcnMpO1xuICAgICAgfSxcbiAgICAgIGlzRW5hYmxlZCxcbiAgICAgIGlzVG9nZ2xlZDogKCkgPT4ge1xuICAgICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgICAgIHJldHVybiB3aWRnZXQ/LmNvbnRlbnQuZWRpdG9yLmdldE9wdGlvbignbGluZU51bWJlcnMnKSA/PyBmYWxzZTtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIC8qKlxuICAgICAqIEFkZCB0aGUgV29yZCBXcmFwIGNvbW1hbmRcbiAgICAgKi9cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMubGluZVdyYXAsIHtcbiAgICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgICBjb25maWcubGluZVdyYXAgPSAoYXJnc1snbW9kZSddIGFzIHdyYXBwaW5nTW9kZSkgfHwgJ29mZic7XG4gICAgICAgIHJldHVybiBzZXR0aW5nUmVnaXN0cnlcbiAgICAgICAgICAuc2V0KGlkLCAnZWRpdG9yQ29uZmlnJywgY29uZmlnIGFzIHVua25vd24gYXMgSlNPTk9iamVjdClcbiAgICAgICAgICAuY2F0Y2goKHJlYXNvbjogRXJyb3IpID0+IHtcbiAgICAgICAgICAgIGNvbnNvbGUuZXJyb3IoYEZhaWxlZCB0byBzZXQgJHtpZH06ICR7cmVhc29uLm1lc3NhZ2V9YCk7XG4gICAgICAgICAgfSk7XG4gICAgICB9LFxuICAgICAgaXNFbmFibGVkLFxuICAgICAgaXNUb2dnbGVkOiBhcmdzID0+IHtcbiAgICAgICAgY29uc3QgbGluZVdyYXAgPSAoYXJnc1snbW9kZSddIGFzIHdyYXBwaW5nTW9kZSkgfHwgJ29mZic7XG4gICAgICAgIHJldHVybiBjb25maWcubGluZVdyYXAgPT09IGxpbmVXcmFwO1xuICAgICAgfSxcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnV29yZCBXcmFwJylcbiAgICB9KTtcblxuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5jdXJyZW50TGluZVdyYXAsIHtcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnV3JhcCBXb3JkcycpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IG9sZFZhbHVlID0gd2lkZ2V0LmNvbnRlbnQuZWRpdG9yLmdldE9wdGlvbignbGluZVdyYXAnKTtcbiAgICAgICAgY29uc3QgbmV3VmFsdWUgPSBvbGRWYWx1ZSA9PT0gJ29mZicgPyAnb24nIDogJ29mZic7XG4gICAgICAgIHdpZGdldC5jb250ZW50LmVkaXRvci5zZXRPcHRpb24oJ2xpbmVXcmFwJywgbmV3VmFsdWUpO1xuICAgICAgfSxcbiAgICAgIGlzRW5hYmxlZCxcbiAgICAgIGlzVG9nZ2xlZDogKCkgPT4ge1xuICAgICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgICAgIHJldHVybiB3aWRnZXQ/LmNvbnRlbnQuZWRpdG9yLmdldE9wdGlvbignbGluZVdyYXAnKSAhPT0gJ29mZicgPz8gZmFsc2U7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICAvKipcbiAgICAgKiBBZGQgY29tbWFuZCBmb3IgY2hhbmdpbmcgdGFicyBzaXplIG9yIHR5cGUgaW4gRmlsZSBFZGl0b3JcbiAgICAgKi9cblxuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5jaGFuZ2VUYWJzLCB7XG4gICAgICBsYWJlbDogYXJncyA9PiB7XG4gICAgICAgIGlmIChhcmdzLmluc2VydFNwYWNlcykge1xuICAgICAgICAgIHJldHVybiB0cmFucy5fbihcbiAgICAgICAgICAgICdTcGFjZXM6ICUxJyxcbiAgICAgICAgICAgICdTcGFjZXM6ICUxJyxcbiAgICAgICAgICAgIChhcmdzLnNpemUgYXMgbnVtYmVyKSA/PyAwXG4gICAgICAgICAgKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICByZXR1cm4gdHJhbnMuX18oJ0luZGVudCB3aXRoIFRhYicpO1xuICAgICAgICB9XG4gICAgICB9LFxuICAgICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICAgIGNvbmZpZy50YWJTaXplID0gKGFyZ3NbJ3NpemUnXSBhcyBudW1iZXIpIHx8IDQ7XG4gICAgICAgIGNvbmZpZy5pbnNlcnRTcGFjZXMgPSAhIWFyZ3NbJ2luc2VydFNwYWNlcyddO1xuICAgICAgICByZXR1cm4gc2V0dGluZ1JlZ2lzdHJ5XG4gICAgICAgICAgLnNldChpZCwgJ2VkaXRvckNvbmZpZycsIGNvbmZpZyBhcyB1bmtub3duIGFzIEpTT05PYmplY3QpXG4gICAgICAgICAgLmNhdGNoKChyZWFzb246IEVycm9yKSA9PiB7XG4gICAgICAgICAgICBjb25zb2xlLmVycm9yKGBGYWlsZWQgdG8gc2V0ICR7aWR9OiAke3JlYXNvbi5tZXNzYWdlfWApO1xuICAgICAgICAgIH0pO1xuICAgICAgfSxcbiAgICAgIGlzVG9nZ2xlZDogYXJncyA9PiB7XG4gICAgICAgIGNvbnN0IGluc2VydFNwYWNlcyA9ICEhYXJnc1snaW5zZXJ0U3BhY2VzJ107XG4gICAgICAgIGNvbnN0IHNpemUgPSAoYXJnc1snc2l6ZSddIGFzIG51bWJlcikgfHwgNDtcbiAgICAgICAgcmV0dXJuIGNvbmZpZy5pbnNlcnRTcGFjZXMgPT09IGluc2VydFNwYWNlcyAmJiBjb25maWcudGFiU2l6ZSA9PT0gc2l6ZTtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIC8qKlxuICAgICAqIEFkZCB0aGUgTWF0Y2ggQnJhY2tldHMgY29tbWFuZFxuICAgICAqL1xuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5tYXRjaEJyYWNrZXRzLCB7XG4gICAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAgIGNvbmZpZy5tYXRjaEJyYWNrZXRzID0gIWNvbmZpZy5tYXRjaEJyYWNrZXRzO1xuICAgICAgICByZXR1cm4gc2V0dGluZ1JlZ2lzdHJ5XG4gICAgICAgICAgLnNldChpZCwgJ2VkaXRvckNvbmZpZycsIGNvbmZpZyBhcyB1bmtub3duIGFzIEpTT05PYmplY3QpXG4gICAgICAgICAgLmNhdGNoKChyZWFzb246IEVycm9yKSA9PiB7XG4gICAgICAgICAgICBjb25zb2xlLmVycm9yKGBGYWlsZWQgdG8gc2V0ICR7aWR9OiAke3JlYXNvbi5tZXNzYWdlfWApO1xuICAgICAgICAgIH0pO1xuICAgICAgfSxcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnTWF0Y2ggQnJhY2tldHMnKSxcbiAgICAgIGlzRW5hYmxlZCxcbiAgICAgIGlzVG9nZ2xlZDogKCkgPT4gY29uZmlnLm1hdGNoQnJhY2tldHNcbiAgICB9KTtcblxuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5jdXJyZW50TWF0Y2hCcmFja2V0cywge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdNYXRjaCBCcmFja2V0cycpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IG1hdGNoQnJhY2tldHMgPSAhd2lkZ2V0LmNvbnRlbnQuZWRpdG9yLmdldE9wdGlvbignbWF0Y2hCcmFja2V0cycpO1xuICAgICAgICB3aWRnZXQuY29udGVudC5lZGl0b3Iuc2V0T3B0aW9uKCdtYXRjaEJyYWNrZXRzJywgbWF0Y2hCcmFja2V0cyk7XG4gICAgICB9LFxuICAgICAgaXNFbmFibGVkLFxuICAgICAgaXNUb2dnbGVkOiAoKSA9PiB7XG4gICAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldDtcbiAgICAgICAgcmV0dXJuIHdpZGdldD8uY29udGVudC5lZGl0b3IuZ2V0T3B0aW9uKCdtYXRjaEJyYWNrZXRzJykgPz8gZmFsc2U7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICAvKipcbiAgICAgKiBBZGQgdGhlIEF1dG8gQ2xvc2UgQnJhY2tldHMgZm9yIFRleHQgRWRpdG9yIGNvbW1hbmRcbiAgICAgKi9cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuYXV0b0Nsb3NpbmdCcmFja2V0cywge1xuICAgICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICAgIGNvbmZpZy5hdXRvQ2xvc2luZ0JyYWNrZXRzID0gISEoXG4gICAgICAgICAgYXJnc1snZm9yY2UnXSA/PyAhY29uZmlnLmF1dG9DbG9zaW5nQnJhY2tldHNcbiAgICAgICAgKTtcbiAgICAgICAgcmV0dXJuIHNldHRpbmdSZWdpc3RyeVxuICAgICAgICAgIC5zZXQoaWQsICdlZGl0b3JDb25maWcnLCBjb25maWcgYXMgdW5rbm93biBhcyBKU09OT2JqZWN0KVxuICAgICAgICAgIC5jYXRjaCgocmVhc29uOiBFcnJvcikgPT4ge1xuICAgICAgICAgICAgY29uc29sZS5lcnJvcihgRmFpbGVkIHRvIHNldCAke2lkfTogJHtyZWFzb24ubWVzc2FnZX1gKTtcbiAgICAgICAgICB9KTtcbiAgICAgIH0sXG4gICAgICBsYWJlbDogdHJhbnMuX18oJ0F1dG8gQ2xvc2UgQnJhY2tldHMgZm9yIFRleHQgRWRpdG9yJyksXG4gICAgICBpc1RvZ2dsZWQ6ICgpID0+IGNvbmZpZy5hdXRvQ2xvc2luZ0JyYWNrZXRzXG4gICAgfSk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuYXV0b0Nsb3NpbmdCcmFja2V0c1VuaXZlcnNhbCwge1xuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICBjb25zdCBhbnlUb2dnbGVkID1cbiAgICAgICAgICBjb21tYW5kcy5pc1RvZ2dsZWQoQ29tbWFuZElEcy5hdXRvQ2xvc2luZ0JyYWNrZXRzKSB8fFxuICAgICAgICAgIGNvbW1hbmRzLmlzVG9nZ2xlZChhdXRvQ2xvc2luZ0JyYWNrZXRzTm90ZWJvb2spIHx8XG4gICAgICAgICAgY29tbWFuZHMuaXNUb2dnbGVkKGF1dG9DbG9zaW5nQnJhY2tldHNDb25zb2xlKTtcbiAgICAgICAgLy8gaWYgYW55IGF1dG8gY2xvc2luZyBicmFja2V0cyBvcHRpb25zIGlzIHRvZ2dsZWQsIHRvZ2dsZSBib3RoIG9mZlxuICAgICAgICBpZiAoYW55VG9nZ2xlZCkge1xuICAgICAgICAgIHZvaWQgY29tbWFuZHMuZXhlY3V0ZShDb21tYW5kSURzLmF1dG9DbG9zaW5nQnJhY2tldHMsIHtcbiAgICAgICAgICAgIGZvcmNlOiBmYWxzZVxuICAgICAgICAgIH0pO1xuICAgICAgICAgIHZvaWQgY29tbWFuZHMuZXhlY3V0ZShhdXRvQ2xvc2luZ0JyYWNrZXRzTm90ZWJvb2ssIHsgZm9yY2U6IGZhbHNlIH0pO1xuICAgICAgICAgIHZvaWQgY29tbWFuZHMuZXhlY3V0ZShhdXRvQ2xvc2luZ0JyYWNrZXRzQ29uc29sZSwgeyBmb3JjZTogZmFsc2UgfSk7XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgLy8gYm90aCBhcmUgb2ZmLCB0dXJuIHRoZW0gb25cbiAgICAgICAgICB2b2lkIGNvbW1hbmRzLmV4ZWN1dGUoQ29tbWFuZElEcy5hdXRvQ2xvc2luZ0JyYWNrZXRzLCB7XG4gICAgICAgICAgICBmb3JjZTogdHJ1ZVxuICAgICAgICAgIH0pO1xuICAgICAgICAgIHZvaWQgY29tbWFuZHMuZXhlY3V0ZShhdXRvQ2xvc2luZ0JyYWNrZXRzTm90ZWJvb2ssIHsgZm9yY2U6IHRydWUgfSk7XG4gICAgICAgICAgdm9pZCBjb21tYW5kcy5leGVjdXRlKGF1dG9DbG9zaW5nQnJhY2tldHNDb25zb2xlLCB7IGZvcmNlOiB0cnVlIH0pO1xuICAgICAgICB9XG4gICAgICB9LFxuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdBdXRvIENsb3NlIEJyYWNrZXRzJyksXG4gICAgICBpc1RvZ2dsZWQ6ICgpID0+XG4gICAgICAgIGNvbW1hbmRzLmlzVG9nZ2xlZChDb21tYW5kSURzLmF1dG9DbG9zaW5nQnJhY2tldHMpIHx8XG4gICAgICAgIGNvbW1hbmRzLmlzVG9nZ2xlZChhdXRvQ2xvc2luZ0JyYWNrZXRzTm90ZWJvb2spIHx8XG4gICAgICAgIGNvbW1hbmRzLmlzVG9nZ2xlZChhdXRvQ2xvc2luZ0JyYWNrZXRzQ29uc29sZSlcbiAgICB9KTtcblxuICAgIC8qKlxuICAgICAqIEFkZCB0aGUgcmVwbGFjZSBzZWxlY3Rpb24gZm9yIHRleHQgZWRpdG9yIGNvbW1hbmRcbiAgICAgKi9cblxuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5yZXBsYWNlU2VsZWN0aW9uLCB7XG4gICAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgICAgY29uc3QgdGV4dDogc3RyaW5nID0gKGFyZ3NbJ3RleHQnXSBhcyBzdHJpbmcpIHx8ICcnO1xuICAgICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIHdpZGdldC5jb250ZW50LmVkaXRvci5yZXBsYWNlU2VsZWN0aW9uPy4odGV4dCk7XG4gICAgICB9LFxuICAgICAgaXNFbmFibGVkLFxuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdSZXBsYWNlIFNlbGVjdGlvbiBpbiBFZGl0b3InKVxuICAgIH0pO1xuXG4gICAgLyoqXG4gICAgICogQWRkIHRoZSBDcmVhdGUgQ29uc29sZSBmb3IgRWRpdG9yIGNvbW1hbmRcbiAgICAgKi9cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY3JlYXRlQ29uc29sZSwge1xuICAgICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldDtcblxuICAgICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIHJldHVybiBnZXRDcmVhdGVDb25zb2xlRnVuY3Rpb24oY29tbWFuZHMpKHdpZGdldCwgYXJncyk7XG4gICAgICB9LFxuICAgICAgaXNFbmFibGVkLFxuICAgICAgaWNvbjogY29uc29sZUljb24sXG4gICAgICBsYWJlbDogdHJhbnMuX18oJ0NyZWF0ZSBDb25zb2xlIGZvciBFZGl0b3InKVxuICAgIH0pO1xuXG4gICAgLyoqXG4gICAgICogUmVzdGFydCB0aGUgQ29uc29sZSBLZXJuZWwgbGlua2VkIHRvIHRoZSBjdXJyZW50IEVkaXRvclxuICAgICAqL1xuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5yZXN0YXJ0Q29uc29sZSwge1xuICAgICAgZXhlY3V0ZTogYXN5bmMgKCkgPT4ge1xuICAgICAgICBjb25zdCBjdXJyZW50ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0Py5jb250ZW50O1xuXG4gICAgICAgIGlmICghY3VycmVudCB8fCBjb25zb2xlVHJhY2tlciA9PT0gbnVsbCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIGNvbnN0IHdpZGdldCA9IGNvbnNvbGVUcmFja2VyLmZpbmQoXG4gICAgICAgICAgd2lkZ2V0ID0+IHdpZGdldC5zZXNzaW9uQ29udGV4dC5zZXNzaW9uPy5wYXRoID09PSBjdXJyZW50LmNvbnRleHQucGF0aFxuICAgICAgICApO1xuICAgICAgICBpZiAod2lkZ2V0KSB7XG4gICAgICAgICAgcmV0dXJuIChzZXNzaW9uRGlhbG9ncyB8fCBzZXNzaW9uQ29udGV4dERpYWxvZ3MpLnJlc3RhcnQoXG4gICAgICAgICAgICB3aWRnZXQuc2Vzc2lvbkNvbnRleHRcbiAgICAgICAgICApO1xuICAgICAgICB9XG4gICAgICB9LFxuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdSZXN0YXJ0IEtlcm5lbCcpLFxuICAgICAgaXNFbmFibGVkOiAoKSA9PiBjb25zb2xlVHJhY2tlciAhPT0gbnVsbCAmJiBpc0VuYWJsZWQoKVxuICAgIH0pO1xuXG4gICAgLyoqXG4gICAgICogQWRkIHRoZSBSdW4gQ29kZSBjb21tYW5kXG4gICAgICovXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnJ1bkNvZGUsIHtcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgLy8gUnVuIHRoZSBhcHByb3ByaWF0ZSBjb2RlLCB0YWtpbmcgaW50byBhY2NvdW50IGEgYGBgZmVuY2VkYGBgIGNvZGUgYmxvY2suXG4gICAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldD8uY29udGVudDtcblxuICAgICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIGxldCBjb2RlOiBzdHJpbmcgfCB1bmRlZmluZWQgPSAnJztcbiAgICAgICAgY29uc3QgZWRpdG9yID0gd2lkZ2V0LmVkaXRvcjtcbiAgICAgICAgY29uc3QgcGF0aCA9IHdpZGdldC5jb250ZXh0LnBhdGg7XG4gICAgICAgIGNvbnN0IGV4dGVuc2lvbiA9IFBhdGhFeHQuZXh0bmFtZShwYXRoKTtcbiAgICAgICAgY29uc3Qgc2VsZWN0aW9uID0gZWRpdG9yLmdldFNlbGVjdGlvbigpO1xuICAgICAgICBjb25zdCB7IHN0YXJ0LCBlbmQgfSA9IHNlbGVjdGlvbjtcbiAgICAgICAgbGV0IHNlbGVjdGVkID0gc3RhcnQuY29sdW1uICE9PSBlbmQuY29sdW1uIHx8IHN0YXJ0LmxpbmUgIT09IGVuZC5saW5lO1xuXG4gICAgICAgIGlmIChzZWxlY3RlZCkge1xuICAgICAgICAgIC8vIEdldCB0aGUgc2VsZWN0ZWQgY29kZSBmcm9tIHRoZSBlZGl0b3IuXG4gICAgICAgICAgY29uc3Qgc3RhcnQgPSBlZGl0b3IuZ2V0T2Zmc2V0QXQoc2VsZWN0aW9uLnN0YXJ0KTtcbiAgICAgICAgICBjb25zdCBlbmQgPSBlZGl0b3IuZ2V0T2Zmc2V0QXQoc2VsZWN0aW9uLmVuZCk7XG5cbiAgICAgICAgICBjb2RlID0gZWRpdG9yLm1vZGVsLnZhbHVlLnRleHQuc3Vic3RyaW5nKHN0YXJ0LCBlbmQpO1xuICAgICAgICB9IGVsc2UgaWYgKE1hcmtkb3duQ29kZUJsb2Nrcy5pc01hcmtkb3duKGV4dGVuc2lvbikpIHtcbiAgICAgICAgICBjb25zdCB7IHRleHQgfSA9IGVkaXRvci5tb2RlbC52YWx1ZTtcbiAgICAgICAgICBjb25zdCBibG9ja3MgPSBNYXJrZG93bkNvZGVCbG9ja3MuZmluZE1hcmtkb3duQ29kZUJsb2Nrcyh0ZXh0KTtcblxuICAgICAgICAgIGZvciAoY29uc3QgYmxvY2sgb2YgYmxvY2tzKSB7XG4gICAgICAgICAgICBpZiAoYmxvY2suc3RhcnRMaW5lIDw9IHN0YXJ0LmxpbmUgJiYgc3RhcnQubGluZSA8PSBibG9jay5lbmRMaW5lKSB7XG4gICAgICAgICAgICAgIGNvZGUgPSBibG9jay5jb2RlO1xuICAgICAgICAgICAgICBzZWxlY3RlZCA9IHRydWU7XG4gICAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICAgICAgfVxuICAgICAgICAgIH1cbiAgICAgICAgfVxuXG4gICAgICAgIGlmICghc2VsZWN0ZWQpIHtcbiAgICAgICAgICAvLyBubyBzZWxlY3Rpb24sIHN1Ym1pdCB3aG9sZSBsaW5lIGFuZCBhZHZhbmNlXG4gICAgICAgICAgY29kZSA9IGVkaXRvci5nZXRMaW5lKHNlbGVjdGlvbi5zdGFydC5saW5lKTtcbiAgICAgICAgICBjb25zdCBjdXJzb3IgPSBlZGl0b3IuZ2V0Q3Vyc29yUG9zaXRpb24oKTtcbiAgICAgICAgICBpZiAoY3Vyc29yLmxpbmUgKyAxID09PSBlZGl0b3IubGluZUNvdW50KSB7XG4gICAgICAgICAgICBjb25zdCB0ZXh0ID0gZWRpdG9yLm1vZGVsLnZhbHVlLnRleHQ7XG4gICAgICAgICAgICBlZGl0b3IubW9kZWwudmFsdWUudGV4dCA9IHRleHQgKyAnXFxuJztcbiAgICAgICAgICB9XG4gICAgICAgICAgZWRpdG9yLnNldEN1cnNvclBvc2l0aW9uKHtcbiAgICAgICAgICAgIGxpbmU6IGN1cnNvci5saW5lICsgMSxcbiAgICAgICAgICAgIGNvbHVtbjogY3Vyc29yLmNvbHVtblxuICAgICAgICAgIH0pO1xuICAgICAgICB9XG5cbiAgICAgICAgY29uc3QgYWN0aXZhdGUgPSBmYWxzZTtcbiAgICAgICAgaWYgKGNvZGUpIHtcbiAgICAgICAgICByZXR1cm4gY29tbWFuZHMuZXhlY3V0ZSgnY29uc29sZTppbmplY3QnLCB7IGFjdGl2YXRlLCBjb2RlLCBwYXRoIH0pO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUodm9pZCAwKTtcbiAgICAgICAgfVxuICAgICAgfSxcbiAgICAgIGlzRW5hYmxlZCxcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnUnVuIFNlbGVjdGVkIENvZGUnKVxuICAgIH0pO1xuXG4gICAgLyoqXG4gICAgICogQWRkIHRoZSBSdW4gQWxsIENvZGUgY29tbWFuZFxuICAgICAqL1xuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5ydW5BbGxDb2RlLCB7XG4gICAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldD8uY29udGVudDtcblxuICAgICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIGxldCBjb2RlID0gJyc7XG4gICAgICAgIGNvbnN0IGVkaXRvciA9IHdpZGdldC5lZGl0b3I7XG4gICAgICAgIGNvbnN0IHRleHQgPSBlZGl0b3IubW9kZWwudmFsdWUudGV4dDtcbiAgICAgICAgY29uc3QgcGF0aCA9IHdpZGdldC5jb250ZXh0LnBhdGg7XG4gICAgICAgIGNvbnN0IGV4dGVuc2lvbiA9IFBhdGhFeHQuZXh0bmFtZShwYXRoKTtcblxuICAgICAgICBpZiAoTWFya2Rvd25Db2RlQmxvY2tzLmlzTWFya2Rvd24oZXh0ZW5zaW9uKSkge1xuICAgICAgICAgIC8vIEZvciBNYXJrZG93biBmaWxlcywgcnVuIG9ubHkgY29kZSBibG9ja3MuXG4gICAgICAgICAgY29uc3QgYmxvY2tzID0gTWFya2Rvd25Db2RlQmxvY2tzLmZpbmRNYXJrZG93bkNvZGVCbG9ja3ModGV4dCk7XG4gICAgICAgICAgZm9yIChjb25zdCBibG9jayBvZiBibG9ja3MpIHtcbiAgICAgICAgICAgIGNvZGUgKz0gYmxvY2suY29kZTtcbiAgICAgICAgICB9XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgY29kZSA9IHRleHQ7XG4gICAgICAgIH1cblxuICAgICAgICBjb25zdCBhY3RpdmF0ZSA9IGZhbHNlO1xuICAgICAgICBpZiAoY29kZSkge1xuICAgICAgICAgIHJldHVybiBjb21tYW5kcy5leGVjdXRlKCdjb25zb2xlOmluamVjdCcsIHsgYWN0aXZhdGUsIGNvZGUsIHBhdGggfSk7XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZSh2b2lkIDApO1xuICAgICAgICB9XG4gICAgICB9LFxuICAgICAgaXNFbmFibGVkLFxuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdSdW4gQWxsIENvZGUnKVxuICAgIH0pO1xuXG4gICAgLyoqXG4gICAgICogQWRkIG1hcmtkb3duIHByZXZpZXcgY29tbWFuZFxuICAgICAqL1xuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5tYXJrZG93blByZXZpZXcsIHtcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuICAgICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuICAgICAgICBjb25zdCBwYXRoID0gd2lkZ2V0LmNvbnRleHQucGF0aDtcbiAgICAgICAgcmV0dXJuIGNvbW1hbmRzLmV4ZWN1dGUoJ21hcmtkb3dudmlld2VyOm9wZW4nLCB7XG4gICAgICAgICAgcGF0aCxcbiAgICAgICAgICBvcHRpb25zOiB7XG4gICAgICAgICAgICBtb2RlOiAnc3BsaXQtcmlnaHQnXG4gICAgICAgICAgfVxuICAgICAgICB9KTtcbiAgICAgIH0sXG4gICAgICBpc1Zpc2libGU6ICgpID0+IHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuICAgICAgICByZXR1cm4gKFxuICAgICAgICAgICh3aWRnZXQgJiYgUGF0aEV4dC5leHRuYW1lKHdpZGdldC5jb250ZXh0LnBhdGgpID09PSAnLm1kJykgfHwgZmFsc2VcbiAgICAgICAgKTtcbiAgICAgIH0sXG4gICAgICBpY29uOiBtYXJrZG93bkljb24sXG4gICAgICBsYWJlbDogdHJhbnMuX18oJ1Nob3cgTWFya2Rvd24gUHJldmlldycpXG4gICAgfSk7XG5cbiAgICAvKipcbiAgICAgKiBBZGQgdGhlIE5ldyBGaWxlIGNvbW1hbmRcbiAgICAgKlxuICAgICAqIERlZmF1bHRzIHRvIFRleHQvLnR4dCBpZiBmaWxlIHR5cGUgZGF0YSBpcyBub3Qgc3BlY2lmaWVkXG4gICAgICovXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmNyZWF0ZU5ldywge1xuICAgICAgbGFiZWw6IGFyZ3MgPT4ge1xuICAgICAgICBpZiAoYXJncy5pc1BhbGV0dGUpIHtcbiAgICAgICAgICByZXR1cm4gKGFyZ3MucGFsZXR0ZUxhYmVsIGFzIHN0cmluZykgPz8gdHJhbnMuX18oJ05ldyBUZXh0IEZpbGUnKTtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gKGFyZ3MubGF1bmNoZXJMYWJlbCBhcyBzdHJpbmcpID8/IHRyYW5zLl9fKCdUZXh0IEZpbGUnKTtcbiAgICAgIH0sXG4gICAgICBjYXB0aW9uOiBhcmdzID0+XG4gICAgICAgIChhcmdzLmNhcHRpb24gYXMgc3RyaW5nKSA/PyB0cmFucy5fXygnQ3JlYXRlIGEgbmV3IHRleHQgZmlsZScpLFxuICAgICAgaWNvbjogYXJncyA9PlxuICAgICAgICBhcmdzLmlzUGFsZXR0ZVxuICAgICAgICAgID8gdW5kZWZpbmVkXG4gICAgICAgICAgOiBMYWJJY29uLnJlc29sdmUoe1xuICAgICAgICAgICAgICBpY29uOiAoYXJncy5pY29uTmFtZSBhcyBzdHJpbmcpID8/IHRleHRFZGl0b3JJY29uXG4gICAgICAgICAgICB9KSxcbiAgICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgICBjb25zdCBjd2QgPSBhcmdzLmN3ZCB8fCBicm93c2VyRmFjdG9yeS5kZWZhdWx0QnJvd3Nlci5tb2RlbC5wYXRoO1xuICAgICAgICByZXR1cm4gY3JlYXRlTmV3KFxuICAgICAgICAgIGNvbW1hbmRzLFxuICAgICAgICAgIGN3ZCBhcyBzdHJpbmcsXG4gICAgICAgICAgKGFyZ3MuZmlsZUV4dCBhcyBzdHJpbmcpID8/ICd0eHQnXG4gICAgICAgICk7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICAvKipcbiAgICAgKiBBZGQgdGhlIE5ldyBNYXJrZG93biBGaWxlIGNvbW1hbmRcbiAgICAgKi9cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY3JlYXRlTmV3TWFya2Rvd24sIHtcbiAgICAgIGxhYmVsOiBhcmdzID0+XG4gICAgICAgIGFyZ3NbJ2lzUGFsZXR0ZSddXG4gICAgICAgICAgPyB0cmFucy5fXygnTmV3IE1hcmtkb3duIEZpbGUnKVxuICAgICAgICAgIDogdHJhbnMuX18oJ01hcmtkb3duIEZpbGUnKSxcbiAgICAgIGNhcHRpb246IHRyYW5zLl9fKCdDcmVhdGUgYSBuZXcgbWFya2Rvd24gZmlsZScpLFxuICAgICAgaWNvbjogYXJncyA9PiAoYXJnc1snaXNQYWxldHRlJ10gPyB1bmRlZmluZWQgOiBtYXJrZG93bkljb24pLFxuICAgICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICAgIGNvbnN0IGN3ZCA9IGFyZ3NbJ2N3ZCddIHx8IGJyb3dzZXJGYWN0b3J5LmRlZmF1bHRCcm93c2VyLm1vZGVsLnBhdGg7XG4gICAgICAgIHJldHVybiBjcmVhdGVOZXcoY29tbWFuZHMsIGN3ZCBhcyBzdHJpbmcsICdtZCcpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgLyoqXG4gICAgICogQWRkIHVuZG8gY29tbWFuZFxuICAgICAqL1xuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy51bmRvLCB7XG4gICAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldD8uY29udGVudDtcblxuICAgICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIHdpZGdldC5lZGl0b3IudW5kbygpO1xuICAgICAgfSxcbiAgICAgIGlzRW5hYmxlZDogKCkgPT4ge1xuICAgICAgICBpZiAoIWlzRW5hYmxlZCgpKSB7XG4gICAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgICB9XG5cbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0Py5jb250ZW50O1xuXG4gICAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgICB9XG4gICAgICAgIC8vIElkZWFsbHkgZW5hYmxlIGl0IHdoZW4gdGhlcmUgYXJlIHVuZG8gZXZlbnRzIHN0b3JlZFxuICAgICAgICAvLyBSZWZlcmVuY2UgaXNzdWUgIzg1OTA6IENvZGUgbWlycm9yIGVkaXRvciBjb3VsZCBleHBvc2UgdGhlIGhpc3Rvcnkgb2YgdW5kby9yZWRvIGV2ZW50c1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH0sXG4gICAgICBpY29uOiB1bmRvSWNvbi5iaW5kcHJvcHMoeyBzdHlsZXNoZWV0OiAnbWVudUl0ZW0nIH0pLFxuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdVbmRvJylcbiAgICB9KTtcblxuICAgIC8qKlxuICAgICAqIEFkZCByZWRvIGNvbW1hbmRcbiAgICAgKi9cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMucmVkbywge1xuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ/LmNvbnRlbnQ7XG5cbiAgICAgICAgaWYgKCF3aWRnZXQpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cblxuICAgICAgICB3aWRnZXQuZWRpdG9yLnJlZG8oKTtcbiAgICAgIH0sXG4gICAgICBpc0VuYWJsZWQ6ICgpID0+IHtcbiAgICAgICAgaWYgKCFpc0VuYWJsZWQoKSkge1xuICAgICAgICAgIHJldHVybiBmYWxzZTtcbiAgICAgICAgfVxuXG4gICAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldD8uY29udGVudDtcblxuICAgICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICAgIHJldHVybiBmYWxzZTtcbiAgICAgICAgfVxuICAgICAgICAvLyBJZGVhbGx5IGVuYWJsZSBpdCB3aGVuIHRoZXJlIGFyZSByZWRvIGV2ZW50cyBzdG9yZWRcbiAgICAgICAgLy8gUmVmZXJlbmNlIGlzc3VlICM4NTkwOiBDb2RlIG1pcnJvciBlZGl0b3IgY291bGQgZXhwb3NlIHRoZSBoaXN0b3J5IG9mIHVuZG8vcmVkbyBldmVudHNcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9LFxuICAgICAgaWNvbjogcmVkb0ljb24uYmluZHByb3BzKHsgc3R5bGVzaGVldDogJ21lbnVJdGVtJyB9KSxcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnUmVkbycpXG4gICAgfSk7XG5cbiAgICAvKipcbiAgICAgKiBBZGQgY3V0IGNvbW1hbmRcbiAgICAgKi9cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY3V0LCB7XG4gICAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldD8uY29udGVudDtcblxuICAgICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIGNvbnN0IGVkaXRvciA9IHdpZGdldC5lZGl0b3IgYXMgQ29kZU1pcnJvckVkaXRvcjtcbiAgICAgICAgY29uc3QgdGV4dCA9IGdldFRleHRTZWxlY3Rpb24oZWRpdG9yKTtcblxuICAgICAgICBDbGlwYm9hcmQuY29weVRvU3lzdGVtKHRleHQpO1xuICAgICAgICBlZGl0b3IucmVwbGFjZVNlbGVjdGlvbiAmJiBlZGl0b3IucmVwbGFjZVNlbGVjdGlvbignJyk7XG4gICAgICB9LFxuICAgICAgaXNFbmFibGVkOiAoKSA9PiB7XG4gICAgICAgIGlmICghaXNFbmFibGVkKCkpIHtcbiAgICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICAgIH1cblxuICAgICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ/LmNvbnRlbnQ7XG5cbiAgICAgICAgaWYgKCF3aWRnZXQpIHtcbiAgICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICAgIH1cblxuICAgICAgICAvLyBFbmFibGUgY29tbWFuZCBpZiB0aGVyZSBpcyBhIHRleHQgc2VsZWN0aW9uIGluIHRoZSBlZGl0b3JcbiAgICAgICAgcmV0dXJuIGlzU2VsZWN0ZWQod2lkZ2V0LmVkaXRvciBhcyBDb2RlTWlycm9yRWRpdG9yKTtcbiAgICAgIH0sXG4gICAgICBpY29uOiBjdXRJY29uLmJpbmRwcm9wcyh7IHN0eWxlc2hlZXQ6ICdtZW51SXRlbScgfSksXG4gICAgICBsYWJlbDogdHJhbnMuX18oJ0N1dCcpXG4gICAgfSk7XG5cbiAgICAvKipcbiAgICAgKiBBZGQgY29weSBjb21tYW5kXG4gICAgICovXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmNvcHksIHtcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0Py5jb250ZW50O1xuXG4gICAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG5cbiAgICAgICAgY29uc3QgZWRpdG9yID0gd2lkZ2V0LmVkaXRvciBhcyBDb2RlTWlycm9yRWRpdG9yO1xuICAgICAgICBjb25zdCB0ZXh0ID0gZ2V0VGV4dFNlbGVjdGlvbihlZGl0b3IpO1xuXG4gICAgICAgIENsaXBib2FyZC5jb3B5VG9TeXN0ZW0odGV4dCk7XG4gICAgICB9LFxuICAgICAgaXNFbmFibGVkOiAoKSA9PiB7XG4gICAgICAgIGlmICghaXNFbmFibGVkKCkpIHtcbiAgICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICAgIH1cblxuICAgICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ/LmNvbnRlbnQ7XG5cbiAgICAgICAgaWYgKCF3aWRnZXQpIHtcbiAgICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICAgIH1cblxuICAgICAgICAvLyBFbmFibGUgY29tbWFuZCBpZiB0aGVyZSBpcyBhIHRleHQgc2VsZWN0aW9uIGluIHRoZSBlZGl0b3JcbiAgICAgICAgcmV0dXJuIGlzU2VsZWN0ZWQod2lkZ2V0LmVkaXRvciBhcyBDb2RlTWlycm9yRWRpdG9yKTtcbiAgICAgIH0sXG4gICAgICBpY29uOiBjb3B5SWNvbi5iaW5kcHJvcHMoeyBzdHlsZXNoZWV0OiAnbWVudUl0ZW0nIH0pLFxuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdDb3B5JylcbiAgICB9KTtcblxuICAgIC8qKlxuICAgICAqIEFkZCBwYXN0ZSBjb21tYW5kXG4gICAgICovXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnBhc3RlLCB7XG4gICAgICBleGVjdXRlOiBhc3luYyAoKSA9PiB7XG4gICAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldD8uY29udGVudDtcblxuICAgICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIGNvbnN0IGVkaXRvcjogQ29kZUVkaXRvci5JRWRpdG9yID0gd2lkZ2V0LmVkaXRvcjtcblxuICAgICAgICAvLyBHZXQgZGF0YSBmcm9tIGNsaXBib2FyZFxuICAgICAgICBjb25zdCBjbGlwYm9hcmQgPSB3aW5kb3cubmF2aWdhdG9yLmNsaXBib2FyZDtcbiAgICAgICAgY29uc3QgY2xpcGJvYXJkRGF0YTogc3RyaW5nID0gYXdhaXQgY2xpcGJvYXJkLnJlYWRUZXh0KCk7XG5cbiAgICAgICAgaWYgKGNsaXBib2FyZERhdGEpIHtcbiAgICAgICAgICAvLyBQYXN0ZSBkYXRhIHRvIHRoZSBlZGl0b3JcbiAgICAgICAgICBlZGl0b3IucmVwbGFjZVNlbGVjdGlvbiAmJiBlZGl0b3IucmVwbGFjZVNlbGVjdGlvbihjbGlwYm9hcmREYXRhKTtcbiAgICAgICAgfVxuICAgICAgfSxcbiAgICAgIGlzRW5hYmxlZDogKCkgPT4gQm9vbGVhbihpc0VuYWJsZWQoKSAmJiB0cmFja2VyLmN1cnJlbnRXaWRnZXQ/LmNvbnRlbnQpLFxuICAgICAgaWNvbjogcGFzdGVJY29uLmJpbmRwcm9wcyh7IHN0eWxlc2hlZXQ6ICdtZW51SXRlbScgfSksXG4gICAgICBsYWJlbDogdHJhbnMuX18oJ1Bhc3RlJylcbiAgICB9KTtcblxuICAgIC8qKlxuICAgICAqIEFkZCBzZWxlY3QgYWxsIGNvbW1hbmRcbiAgICAgKi9cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuc2VsZWN0QWxsLCB7XG4gICAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldD8uY29udGVudDtcblxuICAgICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIGNvbnN0IGVkaXRvciA9IHdpZGdldC5lZGl0b3IgYXMgQ29kZU1pcnJvckVkaXRvcjtcbiAgICAgICAgZWRpdG9yLmV4ZWNDb21tYW5kKHNlbGVjdEFsbCk7XG4gICAgICB9LFxuICAgICAgaXNFbmFibGVkOiAoKSA9PiBCb29sZWFuKGlzRW5hYmxlZCgpICYmIHRyYWNrZXIuY3VycmVudFdpZGdldD8uY29udGVudCksXG4gICAgICBsYWJlbDogdHJhbnMuX18oJ1NlbGVjdCBBbGwnKVxuICAgIH0pO1xuICB9XG5cbiAgZXhwb3J0IGZ1bmN0aW9uIGFkZENvbXBsZXRlckNvbW1hbmRzKFxuICAgIGNvbW1hbmRzOiBDb21tYW5kUmVnaXN0cnksXG4gICAgZWRpdG9yVHJhY2tlcjogSUVkaXRvclRyYWNrZXIsXG4gICAgbWFuYWdlcjogSUNvbXBsZXRpb25Qcm92aWRlck1hbmFnZXIsXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IgfCBudWxsXG4gICk6IHZvaWQge1xuICAgIGNvbnN0IHRyYW5zID0gKHRyYW5zbGF0b3IgPz8gbnVsbFRyYW5zbGF0b3IpLmxvYWQoJ2p1cHl0ZXJsYWInKTtcblxuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5pbnZva2VDb21wbGV0ZXIsIHtcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnRGlzcGxheSB0aGUgY29tcGxldGlvbiBoZWxwZXIuJyksXG4gICAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAgIGNvbnN0IGlkID1cbiAgICAgICAgICBlZGl0b3JUcmFja2VyLmN1cnJlbnRXaWRnZXQgJiYgZWRpdG9yVHJhY2tlci5jdXJyZW50V2lkZ2V0LmlkO1xuICAgICAgICBpZiAoaWQpIHtcbiAgICAgICAgICByZXR1cm4gbWFuYWdlci5pbnZva2UoaWQpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuc2VsZWN0Q29tcGxldGVyLCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ1NlbGVjdCB0aGUgY29tcGxldGlvbiBzdWdnZXN0aW9uLicpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICBjb25zdCBpZCA9XG4gICAgICAgICAgZWRpdG9yVHJhY2tlci5jdXJyZW50V2lkZ2V0ICYmIGVkaXRvclRyYWNrZXIuY3VycmVudFdpZGdldC5pZDtcbiAgICAgICAgaWYgKGlkKSB7XG4gICAgICAgICAgcmV0dXJuIG1hbmFnZXIuc2VsZWN0KGlkKTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH0pO1xuXG4gICAgY29tbWFuZHMuYWRkS2V5QmluZGluZyh7XG4gICAgICBjb21tYW5kOiBDb21tYW5kSURzLnNlbGVjdENvbXBsZXRlcixcbiAgICAgIGtleXM6IFsnRW50ZXInXSxcbiAgICAgIHNlbGVjdG9yOiAnLmpwLUZpbGVFZGl0b3IgLmpwLW1vZC1jb21wbGV0ZXItYWN0aXZlJ1xuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIEhlbHBlciBmdW5jdGlvbiB0byBjaGVjayBpZiB0aGVyZSBpcyBhIHRleHQgc2VsZWN0aW9uIGluIHRoZSBlZGl0b3JcbiAgICovXG4gIGZ1bmN0aW9uIGlzU2VsZWN0ZWQoZWRpdG9yOiBDb2RlTWlycm9yRWRpdG9yKSB7XG4gICAgY29uc3Qgc2VsZWN0aW9uT2JqID0gZWRpdG9yLmdldFNlbGVjdGlvbigpO1xuICAgIGNvbnN0IHsgc3RhcnQsIGVuZCB9ID0gc2VsZWN0aW9uT2JqO1xuICAgIGNvbnN0IHNlbGVjdGVkID0gc3RhcnQuY29sdW1uICE9PSBlbmQuY29sdW1uIHx8IHN0YXJ0LmxpbmUgIT09IGVuZC5saW5lO1xuXG4gICAgcmV0dXJuIHNlbGVjdGVkO1xuICB9XG5cbiAgLyoqXG4gICAqIEhlbHBlciBmdW5jdGlvbiB0byBnZXQgdGV4dCBzZWxlY3Rpb24gZnJvbSB0aGUgZWRpdG9yXG4gICAqL1xuICBmdW5jdGlvbiBnZXRUZXh0U2VsZWN0aW9uKGVkaXRvcjogQ29kZU1pcnJvckVkaXRvcikge1xuICAgIGNvbnN0IHNlbGVjdGlvbk9iaiA9IGVkaXRvci5nZXRTZWxlY3Rpb24oKTtcbiAgICBjb25zdCBzdGFydCA9IGVkaXRvci5nZXRPZmZzZXRBdChzZWxlY3Rpb25PYmouc3RhcnQpO1xuICAgIGNvbnN0IGVuZCA9IGVkaXRvci5nZXRPZmZzZXRBdChzZWxlY3Rpb25PYmouZW5kKTtcbiAgICBjb25zdCB0ZXh0ID0gZWRpdG9yLm1vZGVsLnZhbHVlLnRleHQuc3Vic3RyaW5nKHN0YXJ0LCBlbmQpO1xuXG4gICAgcmV0dXJuIHRleHQ7XG4gIH1cblxuICAvKipcbiAgICogRnVuY3Rpb24gdG8gY3JlYXRlIGEgbmV3IHVudGl0bGVkIHRleHQgZmlsZSwgZ2l2ZW4gdGhlIGN1cnJlbnQgd29ya2luZyBkaXJlY3RvcnkuXG4gICAqL1xuICBhc3luYyBmdW5jdGlvbiBjcmVhdGVOZXcoXG4gICAgY29tbWFuZHM6IENvbW1hbmRSZWdpc3RyeSxcbiAgICBjd2Q6IHN0cmluZyxcbiAgICBleHQ6IHN0cmluZyA9ICd0eHQnXG4gICkge1xuICAgIGNvbnN0IG1vZGVsID0gYXdhaXQgY29tbWFuZHMuZXhlY3V0ZSgnZG9jbWFuYWdlcjpuZXctdW50aXRsZWQnLCB7XG4gICAgICBwYXRoOiBjd2QsXG4gICAgICB0eXBlOiAnZmlsZScsXG4gICAgICBleHRcbiAgICB9KTtcbiAgICBpZiAobW9kZWwgIT0gdW5kZWZpbmVkKSB7XG4gICAgICBjb25zdCB3aWRnZXQgPSAoYXdhaXQgY29tbWFuZHMuZXhlY3V0ZSgnZG9jbWFuYWdlcjpvcGVuJywge1xuICAgICAgICBwYXRoOiBtb2RlbC5wYXRoLFxuICAgICAgICBmYWN0b3J5OiBGQUNUT1JZXG4gICAgICB9KSkgYXMgdW5rbm93biBhcyBJRG9jdW1lbnRXaWRnZXQ7XG4gICAgICB3aWRnZXQuaXNVbnRpdGxlZCA9IHRydWU7XG4gICAgICByZXR1cm4gd2lkZ2V0O1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBXcmFwcGVyIGZ1bmN0aW9uIGZvciBhZGRpbmcgdGhlIGRlZmF1bHQgbGF1bmNoZXIgaXRlbXMgZm9yIEZpbGUgRWRpdG9yXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gYWRkTGF1bmNoZXJJdGVtcyhcbiAgICBsYXVuY2hlcjogSUxhdW5jaGVyLFxuICAgIHRyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZVxuICApOiB2b2lkIHtcbiAgICBhZGRDcmVhdGVOZXdUb0xhdW5jaGVyKGxhdW5jaGVyLCB0cmFucyk7XG5cbiAgICBhZGRDcmVhdGVOZXdNYXJrZG93blRvTGF1bmNoZXIobGF1bmNoZXIsIHRyYW5zKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBZGQgQ3JlYXRlIE5ldyBUZXh0IEZpbGUgdG8gdGhlIExhdW5jaGVyXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gYWRkQ3JlYXRlTmV3VG9MYXVuY2hlcihcbiAgICBsYXVuY2hlcjogSUxhdW5jaGVyLFxuICAgIHRyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZVxuICApOiB2b2lkIHtcbiAgICBsYXVuY2hlci5hZGQoe1xuICAgICAgY29tbWFuZDogQ29tbWFuZElEcy5jcmVhdGVOZXcsXG4gICAgICBjYXRlZ29yeTogdHJhbnMuX18oJ090aGVyJyksXG4gICAgICByYW5rOiAxXG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogQWRkIENyZWF0ZSBOZXcgTWFya2Rvd24gdG8gdGhlIExhdW5jaGVyXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gYWRkQ3JlYXRlTmV3TWFya2Rvd25Ub0xhdW5jaGVyKFxuICAgIGxhdW5jaGVyOiBJTGF1bmNoZXIsXG4gICAgdHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlXG4gICk6IHZvaWQge1xuICAgIGxhdW5jaGVyLmFkZCh7XG4gICAgICBjb21tYW5kOiBDb21tYW5kSURzLmNyZWF0ZU5ld01hcmtkb3duLFxuICAgICAgY2F0ZWdvcnk6IHRyYW5zLl9fKCdPdGhlcicpLFxuICAgICAgcmFuazogMlxuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIEFkZCBfX18gRmlsZSBpdGVtcyB0byB0aGUgTGF1bmNoZXIgZm9yIGNvbW1vbiBmaWxlIHR5cGVzIGFzc29jaWF0ZWQgd2l0aCBhdmFpbGFibGUga2VybmVsc1xuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIGFkZEtlcm5lbExhbmd1YWdlTGF1bmNoZXJJdGVtcyhcbiAgICBsYXVuY2hlcjogSUxhdW5jaGVyLFxuICAgIHRyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZSxcbiAgICBhdmFpbGFibGVLZXJuZWxGaWxlVHlwZXM6IEl0ZXJhYmxlPElGaWxlVHlwZURhdGE+XG4gICk6IHZvaWQge1xuICAgIGZvciAobGV0IGV4dCBvZiBhdmFpbGFibGVLZXJuZWxGaWxlVHlwZXMpIHtcbiAgICAgIGxhdW5jaGVyLmFkZCh7XG4gICAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMuY3JlYXRlTmV3LFxuICAgICAgICBjYXRlZ29yeTogdHJhbnMuX18oJ090aGVyJyksXG4gICAgICAgIHJhbms6IDMsXG4gICAgICAgIGFyZ3M6IGV4dFxuICAgICAgfSk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFdyYXBwZXIgZnVuY3Rpb24gZm9yIGFkZGluZyB0aGUgZGVmYXVsdCBpdGVtcyB0byB0aGUgRmlsZSBFZGl0b3IgcGFsZXR0ZVxuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIGFkZFBhbGV0dGVJdGVtcyhcbiAgICBwYWxldHRlOiBJQ29tbWFuZFBhbGV0dGUsXG4gICAgdHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlXG4gICk6IHZvaWQge1xuICAgIGFkZENoYW5nZVRhYnNDb21tYW5kc1RvUGFsZXR0ZShwYWxldHRlLCB0cmFucyk7XG5cbiAgICBhZGRDcmVhdGVOZXdDb21tYW5kVG9QYWxldHRlKHBhbGV0dGUsIHRyYW5zKTtcblxuICAgIGFkZENyZWF0ZU5ld01hcmtkb3duQ29tbWFuZFRvUGFsZXR0ZShwYWxldHRlLCB0cmFucyk7XG5cbiAgICBhZGRDaGFuZ2VGb250U2l6ZUNvbW1hbmRzVG9QYWxldHRlKHBhbGV0dGUsIHRyYW5zKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBZGQgY29tbWFuZHMgdG8gY2hhbmdlIHRoZSB0YWIgaW5kZW50YXRpb24gdG8gdGhlIEZpbGUgRWRpdG9yIHBhbGV0dGVcbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBhZGRDaGFuZ2VUYWJzQ29tbWFuZHNUb1BhbGV0dGUoXG4gICAgcGFsZXR0ZTogSUNvbW1hbmRQYWxldHRlLFxuICAgIHRyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZVxuICApOiB2b2lkIHtcbiAgICBjb25zdCBwYWxldHRlQ2F0ZWdvcnkgPSB0cmFucy5fXygnVGV4dCBFZGl0b3InKTtcbiAgICBjb25zdCBhcmdzOiBKU09OT2JqZWN0ID0ge1xuICAgICAgaW5zZXJ0U3BhY2VzOiBmYWxzZSxcbiAgICAgIHNpemU6IDRcbiAgICB9O1xuICAgIGNvbnN0IGNvbW1hbmQgPSBDb21tYW5kSURzLmNoYW5nZVRhYnM7XG4gICAgcGFsZXR0ZS5hZGRJdGVtKHsgY29tbWFuZCwgYXJncywgY2F0ZWdvcnk6IHBhbGV0dGVDYXRlZ29yeSB9KTtcblxuICAgIGZvciAoY29uc3Qgc2l6ZSBvZiBbMSwgMiwgNCwgOF0pIHtcbiAgICAgIGNvbnN0IGFyZ3M6IEpTT05PYmplY3QgPSB7XG4gICAgICAgIGluc2VydFNwYWNlczogdHJ1ZSxcbiAgICAgICAgc2l6ZVxuICAgICAgfTtcbiAgICAgIHBhbGV0dGUuYWRkSXRlbSh7IGNvbW1hbmQsIGFyZ3MsIGNhdGVnb3J5OiBwYWxldHRlQ2F0ZWdvcnkgfSk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEFkZCBhIENyZWF0ZSBOZXcgRmlsZSBjb21tYW5kIHRvIHRoZSBGaWxlIEVkaXRvciBwYWxldHRlXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gYWRkQ3JlYXRlTmV3Q29tbWFuZFRvUGFsZXR0ZShcbiAgICBwYWxldHRlOiBJQ29tbWFuZFBhbGV0dGUsXG4gICAgdHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlXG4gICk6IHZvaWQge1xuICAgIGNvbnN0IHBhbGV0dGVDYXRlZ29yeSA9IHRyYW5zLl9fKCdUZXh0IEVkaXRvcicpO1xuICAgIHBhbGV0dGUuYWRkSXRlbSh7XG4gICAgICBjb21tYW5kOiBDb21tYW5kSURzLmNyZWF0ZU5ldyxcbiAgICAgIGFyZ3M6IHsgaXNQYWxldHRlOiB0cnVlIH0sXG4gICAgICBjYXRlZ29yeTogcGFsZXR0ZUNhdGVnb3J5XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogQWRkIGEgQ3JlYXRlIE5ldyBNYXJrZG93biBjb21tYW5kIHRvIHRoZSBGaWxlIEVkaXRvciBwYWxldHRlXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gYWRkQ3JlYXRlTmV3TWFya2Rvd25Db21tYW5kVG9QYWxldHRlKFxuICAgIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSxcbiAgICB0cmFuczogVHJhbnNsYXRpb25CdW5kbGVcbiAgKTogdm9pZCB7XG4gICAgY29uc3QgcGFsZXR0ZUNhdGVnb3J5ID0gdHJhbnMuX18oJ1RleHQgRWRpdG9yJyk7XG4gICAgcGFsZXR0ZS5hZGRJdGVtKHtcbiAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMuY3JlYXRlTmV3TWFya2Rvd24sXG4gICAgICBhcmdzOiB7IGlzUGFsZXR0ZTogdHJ1ZSB9LFxuICAgICAgY2F0ZWdvcnk6IHBhbGV0dGVDYXRlZ29yeVxuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIEFkZCBjb21tYW5kcyB0byBjaGFuZ2UgdGhlIGZvbnQgc2l6ZSB0byB0aGUgRmlsZSBFZGl0b3IgcGFsZXR0ZVxuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIGFkZENoYW5nZUZvbnRTaXplQ29tbWFuZHNUb1BhbGV0dGUoXG4gICAgcGFsZXR0ZTogSUNvbW1hbmRQYWxldHRlLFxuICAgIHRyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZVxuICApOiB2b2lkIHtcbiAgICBjb25zdCBwYWxldHRlQ2F0ZWdvcnkgPSB0cmFucy5fXygnVGV4dCBFZGl0b3InKTtcbiAgICBjb25zdCBjb21tYW5kID0gQ29tbWFuZElEcy5jaGFuZ2VGb250U2l6ZTtcblxuICAgIGxldCBhcmdzID0geyBkZWx0YTogMSB9O1xuICAgIHBhbGV0dGUuYWRkSXRlbSh7IGNvbW1hbmQsIGFyZ3MsIGNhdGVnb3J5OiBwYWxldHRlQ2F0ZWdvcnkgfSk7XG5cbiAgICBhcmdzID0geyBkZWx0YTogLTEgfTtcbiAgICBwYWxldHRlLmFkZEl0ZW0oeyBjb21tYW5kLCBhcmdzLCBjYXRlZ29yeTogcGFsZXR0ZUNhdGVnb3J5IH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIEFkZCBOZXcgX19fIEZpbGUgY29tbWFuZHMgdG8gdGhlIEZpbGUgRWRpdG9yIHBhbGV0dGUgZm9yIGNvbW1vbiBmaWxlIHR5cGVzIGFzc29jaWF0ZWQgd2l0aCBhdmFpbGFibGUga2VybmVsc1xuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIGFkZEtlcm5lbExhbmd1YWdlUGFsZXR0ZUl0ZW1zKFxuICAgIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSxcbiAgICB0cmFuczogVHJhbnNsYXRpb25CdW5kbGUsXG4gICAgYXZhaWxhYmxlS2VybmVsRmlsZVR5cGVzOiBJdGVyYWJsZTxJRmlsZVR5cGVEYXRhPlxuICApOiB2b2lkIHtcbiAgICBjb25zdCBwYWxldHRlQ2F0ZWdvcnkgPSB0cmFucy5fXygnVGV4dCBFZGl0b3InKTtcbiAgICBmb3IgKGxldCBleHQgb2YgYXZhaWxhYmxlS2VybmVsRmlsZVR5cGVzKSB7XG4gICAgICBwYWxldHRlLmFkZEl0ZW0oe1xuICAgICAgICBjb21tYW5kOiBDb21tYW5kSURzLmNyZWF0ZU5ldyxcbiAgICAgICAgYXJnczogeyAuLi5leHQsIGlzUGFsZXR0ZTogdHJ1ZSB9LFxuICAgICAgICBjYXRlZ29yeTogcGFsZXR0ZUNhdGVnb3J5XG4gICAgICB9KTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogV3JhcHBlciBmdW5jdGlvbiBmb3IgYWRkaW5nIHRoZSBkZWZhdWx0IG1lbnUgaXRlbXMgZm9yIEZpbGUgRWRpdG9yXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gYWRkTWVudUl0ZW1zKFxuICAgIG1lbnU6IElNYWluTWVudSxcbiAgICB0cmFja2VyOiBXaWRnZXRUcmFja2VyPElEb2N1bWVudFdpZGdldDxGaWxlRWRpdG9yPj4sXG4gICAgY29uc29sZVRyYWNrZXI6IElDb25zb2xlVHJhY2tlciB8IG51bGwsXG4gICAgaXNFbmFibGVkOiAoKSA9PiBib29sZWFuXG4gICk6IHZvaWQge1xuICAgIC8vIEFkZCB1bmRvL3JlZG8gaG9va3MgdG8gdGhlIGVkaXQgbWVudS5cbiAgICBtZW51LmVkaXRNZW51LnVuZG9lcnMucmVkby5hZGQoe1xuICAgICAgaWQ6IENvbW1hbmRJRHMucmVkbyxcbiAgICAgIGlzRW5hYmxlZFxuICAgIH0pO1xuICAgIG1lbnUuZWRpdE1lbnUudW5kb2Vycy51bmRvLmFkZCh7XG4gICAgICBpZDogQ29tbWFuZElEcy51bmRvLFxuICAgICAgaXNFbmFibGVkXG4gICAgfSk7XG5cbiAgICAvLyBBZGQgZWRpdG9yIHZpZXcgb3B0aW9ucy5cbiAgICBtZW51LnZpZXdNZW51LmVkaXRvclZpZXdlcnMudG9nZ2xlTGluZU51bWJlcnMuYWRkKHtcbiAgICAgIGlkOiBDb21tYW5kSURzLmN1cnJlbnRMaW5lTnVtYmVycyxcbiAgICAgIGlzRW5hYmxlZFxuICAgIH0pO1xuICAgIG1lbnUudmlld01lbnUuZWRpdG9yVmlld2Vycy50b2dnbGVNYXRjaEJyYWNrZXRzLmFkZCh7XG4gICAgICBpZDogQ29tbWFuZElEcy5jdXJyZW50TWF0Y2hCcmFja2V0cyxcbiAgICAgIGlzRW5hYmxlZFxuICAgIH0pO1xuICAgIG1lbnUudmlld01lbnUuZWRpdG9yVmlld2Vycy50b2dnbGVXb3JkV3JhcC5hZGQoe1xuICAgICAgaWQ6IENvbW1hbmRJRHMuY3VycmVudExpbmVXcmFwLFxuICAgICAgaXNFbmFibGVkXG4gICAgfSk7XG5cbiAgICAvLyBBZGQgYSBjb25zb2xlIGNyZWF0b3IgdGhlIHRoZSBmaWxlIG1lbnUuXG4gICAgbWVudS5maWxlTWVudS5jb25zb2xlQ3JlYXRvcnMuYWRkKHtcbiAgICAgIGlkOiBDb21tYW5kSURzLmNyZWF0ZUNvbnNvbGUsXG4gICAgICBpc0VuYWJsZWRcbiAgICB9KTtcblxuICAgIC8vIEFkZCBhIGNvZGUgcnVubmVyIHRvIHRoZSBydW4gbWVudS5cbiAgICBpZiAoY29uc29sZVRyYWNrZXIpIHtcbiAgICAgIGFkZENvZGVSdW5uZXJzVG9SdW5NZW51KG1lbnUsIGNvbnNvbGVUcmFja2VyKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogQWRkIENyZWF0ZSBOZXcgX19fIEZpbGUgY29tbWFuZHMgdG8gdGhlIEZpbGUgbWVudSBmb3IgY29tbW9uIGZpbGUgdHlwZXMgYXNzb2NpYXRlZCB3aXRoIGF2YWlsYWJsZSBrZXJuZWxzXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gYWRkS2VybmVsTGFuZ3VhZ2VNZW51SXRlbXMoXG4gICAgbWVudTogSU1haW5NZW51LFxuICAgIGF2YWlsYWJsZUtlcm5lbEZpbGVUeXBlczogSXRlcmFibGU8SUZpbGVUeXBlRGF0YT5cbiAgKTogdm9pZCB7XG4gICAgZm9yIChsZXQgZXh0IG9mIGF2YWlsYWJsZUtlcm5lbEZpbGVUeXBlcykge1xuICAgICAgbWVudS5maWxlTWVudS5uZXdNZW51LmFkZEl0ZW0oe1xuICAgICAgICBjb21tYW5kOiBDb21tYW5kSURzLmNyZWF0ZU5ldyxcbiAgICAgICAgYXJnczogZXh0LFxuICAgICAgICByYW5rOiAzMVxuICAgICAgfSk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEFkZCBhIEZpbGUgRWRpdG9yIGNvZGUgcnVubmVyIHRvIHRoZSBSdW4gbWVudVxuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIGFkZENvZGVSdW5uZXJzVG9SdW5NZW51KFxuICAgIG1lbnU6IElNYWluTWVudSxcbiAgICBjb25zb2xlVHJhY2tlcjogSUNvbnNvbGVUcmFja2VyXG4gICk6IHZvaWQge1xuICAgIGNvbnN0IGlzRW5hYmxlZCA9IChjdXJyZW50OiBJRG9jdW1lbnRXaWRnZXQ8RmlsZUVkaXRvcj4pID0+XG4gICAgICBjdXJyZW50LmNvbnRleHQgJiZcbiAgICAgICEhY29uc29sZVRyYWNrZXIuZmluZChcbiAgICAgICAgd2lkZ2V0ID0+IHdpZGdldC5zZXNzaW9uQ29udGV4dC5zZXNzaW9uPy5wYXRoID09PSBjdXJyZW50LmNvbnRleHQucGF0aFxuICAgICAgKTtcbiAgICBtZW51LnJ1bk1lbnUuY29kZVJ1bm5lcnMucmVzdGFydC5hZGQoe1xuICAgICAgaWQ6IENvbW1hbmRJRHMucmVzdGFydENvbnNvbGUsXG4gICAgICBpc0VuYWJsZWRcbiAgICB9KTtcbiAgICBtZW51LnJ1bk1lbnUuY29kZVJ1bm5lcnMucnVuLmFkZCh7XG4gICAgICBpZDogQ29tbWFuZElEcy5ydW5Db2RlLFxuICAgICAgaXNFbmFibGVkXG4gICAgfSk7XG4gICAgbWVudS5ydW5NZW51LmNvZGVSdW5uZXJzLnJ1bkFsbC5hZGQoe1xuICAgICAgaWQ6IENvbW1hbmRJRHMucnVuQWxsQ29kZSxcbiAgICAgIGlzRW5hYmxlZFxuICAgIH0pO1xuICB9XG5cbiAgZXhwb3J0IGZ1bmN0aW9uIGFkZE9wZW5Db2RlVmlld2VyQ29tbWFuZChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICBlZGl0b3JTZXJ2aWNlczogSUVkaXRvclNlcnZpY2VzLFxuICAgIHRyYWNrZXI6IFdpZGdldFRyYWNrZXI8TWFpbkFyZWFXaWRnZXQ8Q29kZVZpZXdlcldpZGdldD4+LFxuICAgIHRyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZVxuICApIHtcbiAgICBjb25zdCBvcGVuQ29kZVZpZXdlciA9IGFzeW5jIChhcmdzOiB7XG4gICAgICBjb250ZW50OiBzdHJpbmc7XG4gICAgICBsYWJlbD86IHN0cmluZztcbiAgICAgIG1pbWVUeXBlPzogc3RyaW5nO1xuICAgICAgZXh0ZW5zaW9uPzogc3RyaW5nO1xuICAgICAgd2lkZ2V0SWQ/OiBzdHJpbmc7XG4gICAgfSk6IFByb21pc2U8Q29kZVZpZXdlcldpZGdldD4gPT4ge1xuICAgICAgY29uc3QgZnVuYyA9IGVkaXRvclNlcnZpY2VzLmZhY3RvcnlTZXJ2aWNlLm5ld0RvY3VtZW50RWRpdG9yO1xuICAgICAgY29uc3QgZmFjdG9yeTogQ29kZUVkaXRvci5GYWN0b3J5ID0gb3B0aW9ucyA9PiB7XG4gICAgICAgIHJldHVybiBmdW5jKG9wdGlvbnMpO1xuICAgICAgfTtcblxuICAgICAgLy8gRGVyaXZlIG1pbWV0eXBlIGZyb20gZXh0ZW5zaW9uXG4gICAgICBsZXQgbWltZXR5cGUgPSBhcmdzLm1pbWVUeXBlO1xuICAgICAgaWYgKCFtaW1ldHlwZSAmJiBhcmdzLmV4dGVuc2lvbikge1xuICAgICAgICBtaW1ldHlwZSA9IGVkaXRvclNlcnZpY2VzLm1pbWVUeXBlU2VydmljZS5nZXRNaW1lVHlwZUJ5RmlsZVBhdGgoXG4gICAgICAgICAgYHRlbXAuJHthcmdzLmV4dGVuc2lvbi5yZXBsYWNlKC9cXFxcLiQvLCAnJyl9YFxuICAgICAgICApO1xuICAgICAgfVxuXG4gICAgICBjb25zdCB3aWRnZXQgPSBDb2RlVmlld2VyV2lkZ2V0LmNyZWF0ZUNvZGVWaWV3ZXIoe1xuICAgICAgICBmYWN0b3J5LFxuICAgICAgICBjb250ZW50OiBhcmdzLmNvbnRlbnQsXG4gICAgICAgIG1pbWVUeXBlOiBtaW1ldHlwZVxuICAgICAgfSk7XG4gICAgICB3aWRnZXQudGl0bGUubGFiZWwgPSBhcmdzLmxhYmVsIHx8IHRyYW5zLl9fKCdDb2RlIFZpZXdlcicpO1xuICAgICAgd2lkZ2V0LnRpdGxlLmNhcHRpb24gPSB3aWRnZXQudGl0bGUubGFiZWw7XG5cbiAgICAgIC8vIEdldCB0aGUgZmlsZVR5cGUgYmFzZWQgb24gdGhlIG1pbWV0eXBlIHRvIGRldGVybWluZSB0aGUgaWNvblxuICAgICAgY29uc3QgZmlsZVR5cGUgPSB0b0FycmF5KGFwcC5kb2NSZWdpc3RyeS5maWxlVHlwZXMoKSkuZmluZChmaWxlVHlwZSA9PiB7XG4gICAgICAgIHJldHVybiBtaW1ldHlwZSA/IGZpbGVUeXBlLm1pbWVUeXBlcy5pbmNsdWRlcyhtaW1ldHlwZSkgOiB1bmRlZmluZWQ7XG4gICAgICB9KTtcbiAgICAgIHdpZGdldC50aXRsZS5pY29uID0gZmlsZVR5cGU/Lmljb24gPz8gdGV4dEVkaXRvckljb247XG5cbiAgICAgIGlmIChhcmdzLndpZGdldElkKSB7XG4gICAgICAgIHdpZGdldC5pZCA9IGFyZ3Mud2lkZ2V0SWQ7XG4gICAgICB9XG4gICAgICBjb25zdCBtYWluID0gbmV3IE1haW5BcmVhV2lkZ2V0KHsgY29udGVudDogd2lkZ2V0IH0pO1xuICAgICAgYXdhaXQgdHJhY2tlci5hZGQobWFpbik7XG4gICAgICBhcHAuc2hlbGwuYWRkKG1haW4sICdtYWluJyk7XG4gICAgICByZXR1cm4gd2lkZ2V0O1xuICAgIH07XG5cbiAgICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLm9wZW5Db2RlVmlld2VyLCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ09wZW4gQ29kZSBWaWV3ZXInKSxcbiAgICAgIGV4ZWN1dGU6IChhcmdzOiBhbnkpID0+IHtcbiAgICAgICAgcmV0dXJuIG9wZW5Db2RlVmlld2VyKGFyZ3MpO1xuICAgICAgfVxuICAgIH0pO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBmaWxlZWRpdG9yLWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7XG4gIElMYXlvdXRSZXN0b3JlcixcbiAgSnVweXRlckZyb250RW5kLFxuICBKdXB5dGVyRnJvbnRFbmRQbHVnaW5cbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24nO1xuaW1wb3J0IHtcbiAgY3JlYXRlVG9vbGJhckZhY3RvcnksXG4gIElDb21tYW5kUGFsZXR0ZSxcbiAgSVNlc3Npb25Db250ZXh0RGlhbG9ncyxcbiAgSVRvb2xiYXJXaWRnZXRSZWdpc3RyeSxcbiAgTWFpbkFyZWFXaWRnZXQsXG4gIFdpZGdldFRyYWNrZXJcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHtcbiAgQ29kZUVkaXRvcixcbiAgQ29kZVZpZXdlcldpZGdldCxcbiAgSUVkaXRvclNlcnZpY2VzLFxuICBJUG9zaXRpb25Nb2RlbFxufSBmcm9tICdAanVweXRlcmxhYi9jb2RlZWRpdG9yJztcbmltcG9ydCB7IElDb21wbGV0aW9uUHJvdmlkZXJNYW5hZ2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29tcGxldGVyJztcbmltcG9ydCB7IElDb25zb2xlVHJhY2tlciB9IGZyb20gJ0BqdXB5dGVybGFiL2NvbnNvbGUnO1xuaW1wb3J0IHsgRG9jdW1lbnRSZWdpc3RyeSwgSURvY3VtZW50V2lkZ2V0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jcmVnaXN0cnknO1xuaW1wb3J0IHsgSVNlYXJjaFByb3ZpZGVyUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9kb2N1bWVudHNlYXJjaCc7XG5pbXBvcnQgeyBJRmlsZUJyb3dzZXJGYWN0b3J5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvZmlsZWJyb3dzZXInO1xuaW1wb3J0IHtcbiAgRmlsZUVkaXRvcixcbiAgRmlsZUVkaXRvckFkYXB0ZXIsXG4gIEZpbGVFZGl0b3JGYWN0b3J5LFxuICBGaWxlRWRpdG9yU2VhcmNoUHJvdmlkZXIsXG4gIElFZGl0b3JUcmFja2VyLFxuICBMYVRlWFRhYmxlT2ZDb250ZW50c0ZhY3RvcnksXG4gIE1hcmtkb3duVGFibGVPZkNvbnRlbnRzRmFjdG9yeSxcbiAgUHl0aG9uVGFibGVPZkNvbnRlbnRzRmFjdG9yeSxcbiAgVGFiU3BhY2VTdGF0dXNcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvZmlsZWVkaXRvcic7XG5pbXBvcnQgeyBJTGF1bmNoZXIgfSBmcm9tICdAanVweXRlcmxhYi9sYXVuY2hlcic7XG5pbXBvcnQge1xuICBJTFNQQ29kZUV4dHJhY3RvcnNNYW5hZ2VyLFxuICBJTFNQRG9jdW1lbnRDb25uZWN0aW9uTWFuYWdlcixcbiAgSUxTUEZlYXR1cmVNYW5hZ2VyXG59IGZyb20gJ0BqdXB5dGVybGFiL2xzcCc7XG5pbXBvcnQgeyBJTWFpbk1lbnUgfSBmcm9tICdAanVweXRlcmxhYi9tYWlubWVudSc7XG5pbXBvcnQgeyBJT2JzZXJ2YWJsZUxpc3QgfSBmcm9tICdAanVweXRlcmxhYi9vYnNlcnZhYmxlcyc7XG5pbXBvcnQgeyBTZXNzaW9uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2VydmljZXMnO1xuaW1wb3J0IHsgSVNldHRpbmdSZWdpc3RyeSB9IGZyb20gJ0BqdXB5dGVybGFiL3NldHRpbmdyZWdpc3RyeSc7XG5pbXBvcnQgeyBJU3RhdHVzQmFyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc3RhdHVzYmFyJztcbmltcG9ydCB7IElUYWJsZU9mQ29udGVudHNSZWdpc3RyeSB9IGZyb20gJ0BqdXB5dGVybGFiL3RvYyc7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IGZpbmQsIHRvQXJyYXkgfSBmcm9tICdAbHVtaW5vL2FsZ29yaXRobSc7XG5pbXBvcnQgeyBKU09OT2JqZWN0IH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgTWVudSwgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcblxuaW1wb3J0IHsgQ29tbWFuZElEcywgQ29tbWFuZHMsIEZBQ1RPUlksIElGaWxlVHlwZURhdGEgfSBmcm9tICcuL2NvbW1hbmRzJztcblxuZXhwb3J0IHsgQ29tbWFuZHMgfSBmcm9tICcuL2NvbW1hbmRzJztcblxuLyoqXG4gKiBUaGUgZWRpdG9yIHRyYWNrZXIgZXh0ZW5zaW9uLlxuICovXG5jb25zdCBwbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJRWRpdG9yVHJhY2tlcj4gPSB7XG4gIGFjdGl2YXRlLFxuICBpZDogJ0BqdXB5dGVybGFiL2ZpbGVlZGl0b3ItZXh0ZW5zaW9uOnBsdWdpbicsXG4gIHJlcXVpcmVzOiBbXG4gICAgSUVkaXRvclNlcnZpY2VzLFxuICAgIElGaWxlQnJvd3NlckZhY3RvcnksXG4gICAgSVNldHRpbmdSZWdpc3RyeSxcbiAgICBJVHJhbnNsYXRvclxuICBdLFxuICBvcHRpb25hbDogW1xuICAgIElDb25zb2xlVHJhY2tlcixcbiAgICBJQ29tbWFuZFBhbGV0dGUsXG4gICAgSUxhdW5jaGVyLFxuICAgIElNYWluTWVudSxcbiAgICBJTGF5b3V0UmVzdG9yZXIsXG4gICAgSVNlc3Npb25Db250ZXh0RGlhbG9ncyxcbiAgICBJVGFibGVPZkNvbnRlbnRzUmVnaXN0cnksXG4gICAgSVRvb2xiYXJXaWRnZXRSZWdpc3RyeVxuICBdLFxuICBwcm92aWRlczogSUVkaXRvclRyYWNrZXIsXG4gIGF1dG9TdGFydDogdHJ1ZVxufTtcblxuLyoqXG4gKiBBIHBsdWdpbiB0aGF0IHByb3ZpZGVzIGEgc3RhdHVzIGl0ZW0gYWxsb3dpbmcgdGhlIHVzZXIgdG9cbiAqIHN3aXRjaCB0YWJzIHZzIHNwYWNlcyBhbmQgdGFiIHdpZHRocyBmb3IgdGV4dCBlZGl0b3JzLlxuICovXG5leHBvcnQgY29uc3QgdGFiU3BhY2VTdGF0dXM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9maWxlZWRpdG9yLWV4dGVuc2lvbjp0YWItc3BhY2Utc3RhdHVzJyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICByZXF1aXJlczogW0lFZGl0b3JUcmFja2VyLCBJU2V0dGluZ1JlZ2lzdHJ5LCBJVHJhbnNsYXRvcl0sXG4gIG9wdGlvbmFsOiBbSVN0YXR1c0Jhcl0sXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgZWRpdG9yVHJhY2tlcjogSUVkaXRvclRyYWNrZXIsXG4gICAgc2V0dGluZ1JlZ2lzdHJ5OiBJU2V0dGluZ1JlZ2lzdHJ5LFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICAgIHN0YXR1c0JhcjogSVN0YXR1c0JhciB8IG51bGxcbiAgKSA9PiB7XG4gICAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICBpZiAoIXN0YXR1c0Jhcikge1xuICAgICAgLy8gQXV0b21hdGljYWxseSBkaXNhYmxlIGlmIHN0YXR1c2JhciBtaXNzaW5nXG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIC8vIENyZWF0ZSBhIG1lbnUgZm9yIHN3aXRjaGluZyB0YWJzIHZzIHNwYWNlcy5cbiAgICBjb25zdCBtZW51ID0gbmV3IE1lbnUoeyBjb21tYW5kczogYXBwLmNvbW1hbmRzIH0pO1xuICAgIGNvbnN0IGNvbW1hbmQgPSAnZmlsZWVkaXRvcjpjaGFuZ2UtdGFicyc7XG4gICAgY29uc3QgeyBzaGVsbCB9ID0gYXBwO1xuICAgIGNvbnN0IGFyZ3M6IEpTT05PYmplY3QgPSB7XG4gICAgICBpbnNlcnRTcGFjZXM6IGZhbHNlLFxuICAgICAgc2l6ZTogNCxcbiAgICAgIG5hbWU6IHRyYW5zLl9fKCdJbmRlbnQgd2l0aCBUYWInKVxuICAgIH07XG4gICAgbWVudS5hZGRJdGVtKHsgY29tbWFuZCwgYXJncyB9KTtcbiAgICBmb3IgKGNvbnN0IHNpemUgb2YgWzEsIDIsIDQsIDhdKSB7XG4gICAgICBjb25zdCBhcmdzOiBKU09OT2JqZWN0ID0ge1xuICAgICAgICBpbnNlcnRTcGFjZXM6IHRydWUsXG4gICAgICAgIHNpemUsXG4gICAgICAgIG5hbWU6IHRyYW5zLl9uKCdTcGFjZXM6ICUxJywgJ1NwYWNlczogJTEnLCBzaXplKVxuICAgICAgfTtcbiAgICAgIG1lbnUuYWRkSXRlbSh7IGNvbW1hbmQsIGFyZ3MgfSk7XG4gICAgfVxuXG4gICAgLy8gQ3JlYXRlIHRoZSBzdGF0dXMgaXRlbS5cbiAgICBjb25zdCBpdGVtID0gbmV3IFRhYlNwYWNlU3RhdHVzKHsgbWVudSwgdHJhbnNsYXRvciB9KTtcblxuICAgIC8vIEtlZXAgYSByZWZlcmVuY2UgdG8gdGhlIGNvZGUgZWRpdG9yIGNvbmZpZyBmcm9tIHRoZSBzZXR0aW5ncyBzeXN0ZW0uXG4gICAgY29uc3QgdXBkYXRlU2V0dGluZ3MgPSAoc2V0dGluZ3M6IElTZXR0aW5nUmVnaXN0cnkuSVNldHRpbmdzKTogdm9pZCA9PiB7XG4gICAgICBpdGVtLm1vZGVsIS5jb25maWcgPSB7XG4gICAgICAgIC4uLkNvZGVFZGl0b3IuZGVmYXVsdENvbmZpZyxcbiAgICAgICAgLi4uKHNldHRpbmdzLmdldCgnZWRpdG9yQ29uZmlnJykuY29tcG9zaXRlIGFzIEpTT05PYmplY3QpXG4gICAgICB9O1xuICAgIH07XG4gICAgdm9pZCBQcm9taXNlLmFsbChbXG4gICAgICBzZXR0aW5nUmVnaXN0cnkubG9hZCgnQGp1cHl0ZXJsYWIvZmlsZWVkaXRvci1leHRlbnNpb246cGx1Z2luJyksXG4gICAgICBhcHAucmVzdG9yZWRcbiAgICBdKS50aGVuKChbc2V0dGluZ3NdKSA9PiB7XG4gICAgICB1cGRhdGVTZXR0aW5ncyhzZXR0aW5ncyk7XG4gICAgICBzZXR0aW5ncy5jaGFuZ2VkLmNvbm5lY3QodXBkYXRlU2V0dGluZ3MpO1xuICAgIH0pO1xuXG4gICAgLy8gQWRkIHRoZSBzdGF0dXMgaXRlbS5cbiAgICBzdGF0dXNCYXIucmVnaXN0ZXJTdGF0dXNJdGVtKFxuICAgICAgJ0BqdXB5dGVybGFiL2ZpbGVlZGl0b3ItZXh0ZW5zaW9uOnRhYi1zcGFjZS1zdGF0dXMnLFxuICAgICAge1xuICAgICAgICBpdGVtLFxuICAgICAgICBhbGlnbjogJ3JpZ2h0JyxcbiAgICAgICAgcmFuazogMSxcbiAgICAgICAgaXNBY3RpdmU6ICgpID0+IHtcbiAgICAgICAgICByZXR1cm4gKFxuICAgICAgICAgICAgISFzaGVsbC5jdXJyZW50V2lkZ2V0ICYmIGVkaXRvclRyYWNrZXIuaGFzKHNoZWxsLmN1cnJlbnRXaWRnZXQpXG4gICAgICAgICAgKTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgICk7XG4gIH1cbn07XG5cbi8qKlxuICogQ3Vyc29yIHBvc2l0aW9uLlxuICovXG5jb25zdCBsaW5lQ29sU3RhdHVzOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvZmlsZWVkaXRvci1leHRlbnNpb246Y3Vyc29yLXBvc2l0aW9uJyxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICB0cmFja2VyOiBJRWRpdG9yVHJhY2tlcixcbiAgICBwb3NpdGlvbk1vZGVsOiBJUG9zaXRpb25Nb2RlbFxuICApID0+IHtcbiAgICBwb3NpdGlvbk1vZGVsLmFkZEVkaXRvclByb3ZpZGVyKCh3aWRnZXQ6IFdpZGdldCB8IG51bGwpID0+XG4gICAgICB3aWRnZXQgJiYgdHJhY2tlci5oYXMod2lkZ2V0KVxuICAgICAgICA/ICh3aWRnZXQgYXMgSURvY3VtZW50V2lkZ2V0PEZpbGVFZGl0b3I+KS5jb250ZW50LmVkaXRvclxuICAgICAgICA6IG51bGxcbiAgICApO1xuICB9LFxuICByZXF1aXJlczogW0lFZGl0b3JUcmFja2VyLCBJUG9zaXRpb25Nb2RlbF0sXG4gIGF1dG9TdGFydDogdHJ1ZVxufTtcblxuY29uc3QgY29tcGxldGVyUGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvZmlsZWVkaXRvci1leHRlbnNpb246Y29tcGxldGVyJyxcbiAgcmVxdWlyZXM6IFtJRWRpdG9yVHJhY2tlcl0sXG4gIG9wdGlvbmFsOiBbSUNvbXBsZXRpb25Qcm92aWRlck1hbmFnZXJdLFxuICBhY3RpdmF0ZTogYWN0aXZhdGVGaWxlRWRpdG9yQ29tcGxldGVyU2VydmljZSxcbiAgYXV0b1N0YXJ0OiB0cnVlXG59O1xuXG4vKipcbiAqIEEgcGx1Z2luIHRvIHNlYXJjaCBmaWxlIGVkaXRvcnNcbiAqL1xuY29uc3Qgc2VhcmNoUHJvdmlkZXI6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9maWxlZWRpdG9yLWV4dGVuc2lvbjpzZWFyY2gnLFxuICByZXF1aXJlczogW0lTZWFyY2hQcm92aWRlclJlZ2lzdHJ5XSxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBhY3RpdmF0ZTogKGFwcDogSnVweXRlckZyb250RW5kLCByZWdpc3RyeTogSVNlYXJjaFByb3ZpZGVyUmVnaXN0cnkpID0+IHtcbiAgICByZWdpc3RyeS5hZGQoJ2pwLWZpbGVlZGl0b3JTZWFyY2hQcm92aWRlcicsIEZpbGVFZGl0b3JTZWFyY2hQcm92aWRlcik7XG4gIH1cbn07XG5cbmNvbnN0IGxhbmd1YWdlU2VydmVyUGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvZmlsZWVkaXRvci1leHRlbnNpb246bGFuZ3VhZ2Utc2VydmVyJyxcbiAgcmVxdWlyZXM6IFtcbiAgICBJRWRpdG9yVHJhY2tlcixcbiAgICBJTFNQRG9jdW1lbnRDb25uZWN0aW9uTWFuYWdlcixcbiAgICBJTFNQRmVhdHVyZU1hbmFnZXIsXG4gICAgSUxTUENvZGVFeHRyYWN0b3JzTWFuYWdlclxuICBdLFxuXG4gIGFjdGl2YXRlOiBhY3RpdmF0ZUZpbGVFZGl0b3JMYW5ndWFnZVNlcnZlcixcbiAgYXV0b1N0YXJ0OiB0cnVlXG59O1xuXG4vKipcbiAqIEV4cG9ydCB0aGUgcGx1Z2lucyBhcyBkZWZhdWx0LlxuICovXG5jb25zdCBwbHVnaW5zOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48YW55PltdID0gW1xuICBwbHVnaW4sXG4gIGxpbmVDb2xTdGF0dXMsXG4gIGNvbXBsZXRlclBsdWdpbixcbiAgbGFuZ3VhZ2VTZXJ2ZXJQbHVnaW4sXG4gIHNlYXJjaFByb3ZpZGVyLFxuICB0YWJTcGFjZVN0YXR1c1xuXTtcbmV4cG9ydCBkZWZhdWx0IHBsdWdpbnM7XG5cbi8qKlxuICogQWN0aXZhdGUgdGhlIGVkaXRvciB0cmFja2VyIHBsdWdpbi5cbiAqL1xuZnVuY3Rpb24gYWN0aXZhdGUoXG4gIGFwcDogSnVweXRlckZyb250RW5kLFxuICBlZGl0b3JTZXJ2aWNlczogSUVkaXRvclNlcnZpY2VzLFxuICBicm93c2VyRmFjdG9yeTogSUZpbGVCcm93c2VyRmFjdG9yeSxcbiAgc2V0dGluZ1JlZ2lzdHJ5OiBJU2V0dGluZ1JlZ2lzdHJ5LFxuICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcixcbiAgY29uc29sZVRyYWNrZXI6IElDb25zb2xlVHJhY2tlciB8IG51bGwsXG4gIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSB8IG51bGwsXG4gIGxhdW5jaGVyOiBJTGF1bmNoZXIgfCBudWxsLFxuICBtZW51OiBJTWFpbk1lbnUgfCBudWxsLFxuICByZXN0b3JlcjogSUxheW91dFJlc3RvcmVyIHwgbnVsbCxcbiAgc2Vzc2lvbkRpYWxvZ3M6IElTZXNzaW9uQ29udGV4dERpYWxvZ3MgfCBudWxsLFxuICB0b2NSZWdpc3RyeTogSVRhYmxlT2ZDb250ZW50c1JlZ2lzdHJ5IHwgbnVsbCxcbiAgdG9vbGJhclJlZ2lzdHJ5OiBJVG9vbGJhcldpZGdldFJlZ2lzdHJ5IHwgbnVsbFxuKTogSUVkaXRvclRyYWNrZXIge1xuICBjb25zdCBpZCA9IHBsdWdpbi5pZDtcbiAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgY29uc3QgbmFtZXNwYWNlID0gJ2VkaXRvcic7XG4gIGxldCB0b29sYmFyRmFjdG9yeTpcbiAgICB8ICgoXG4gICAgICAgIHdpZGdldDogSURvY3VtZW50V2lkZ2V0PEZpbGVFZGl0b3I+XG4gICAgICApID0+IElPYnNlcnZhYmxlTGlzdDxEb2N1bWVudFJlZ2lzdHJ5LklUb29sYmFySXRlbT4pXG4gICAgfCB1bmRlZmluZWQ7XG5cbiAgaWYgKHRvb2xiYXJSZWdpc3RyeSkge1xuICAgIHRvb2xiYXJGYWN0b3J5ID0gY3JlYXRlVG9vbGJhckZhY3RvcnkoXG4gICAgICB0b29sYmFyUmVnaXN0cnksXG4gICAgICBzZXR0aW5nUmVnaXN0cnksXG4gICAgICBGQUNUT1JZLFxuICAgICAgaWQsXG4gICAgICB0cmFuc2xhdG9yXG4gICAgKTtcbiAgfVxuXG4gIGNvbnN0IGZhY3RvcnkgPSBuZXcgRmlsZUVkaXRvckZhY3Rvcnkoe1xuICAgIGVkaXRvclNlcnZpY2VzLFxuICAgIGZhY3RvcnlPcHRpb25zOiB7XG4gICAgICBuYW1lOiBGQUNUT1JZLFxuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdFZGl0b3InKSxcbiAgICAgIGZpbGVUeXBlczogWydtYXJrZG93bicsICcqJ10sIC8vIEV4cGxpY2l0bHkgYWRkIHRoZSBtYXJrZG93biBmaWxlVHlwZSBzb1xuICAgICAgZGVmYXVsdEZvcjogWydtYXJrZG93bicsICcqJ10sIC8vIGl0IG91dHJhbmtzIHRoZSBkZWZhdWx0UmVuZGVyZWQgdmlld2VyLlxuICAgICAgdG9vbGJhckZhY3RvcnksXG4gICAgICB0cmFuc2xhdG9yXG4gICAgfVxuICB9KTtcbiAgY29uc3QgeyBjb21tYW5kcywgcmVzdG9yZWQsIHNoZWxsIH0gPSBhcHA7XG4gIGNvbnN0IHRyYWNrZXIgPSBuZXcgV2lkZ2V0VHJhY2tlcjxJRG9jdW1lbnRXaWRnZXQ8RmlsZUVkaXRvcj4+KHtcbiAgICBuYW1lc3BhY2VcbiAgfSk7XG4gIGNvbnN0IGlzRW5hYmxlZCA9ICgpID0+XG4gICAgdHJhY2tlci5jdXJyZW50V2lkZ2V0ICE9PSBudWxsICYmXG4gICAgdHJhY2tlci5jdXJyZW50V2lkZ2V0ID09PSBzaGVsbC5jdXJyZW50V2lkZ2V0O1xuXG4gIGNvbnN0IGNvbW1vbkxhbmd1YWdlRmlsZVR5cGVEYXRhID0gbmV3IE1hcDxzdHJpbmcsIElGaWxlVHlwZURhdGFbXT4oW1xuICAgIFtcbiAgICAgICdweXRob24nLFxuICAgICAgW1xuICAgICAgICB7XG4gICAgICAgICAgZmlsZUV4dDogJ3B5JyxcbiAgICAgICAgICBpY29uTmFtZTogJ3VpLWNvbXBvbmVudHM6cHl0aG9uJyxcbiAgICAgICAgICBsYXVuY2hlckxhYmVsOiB0cmFucy5fXygnUHl0aG9uIEZpbGUnKSxcbiAgICAgICAgICBwYWxldHRlTGFiZWw6IHRyYW5zLl9fKCdOZXcgUHl0aG9uIEZpbGUnKSxcbiAgICAgICAgICBjYXB0aW9uOiB0cmFucy5fXygnQ3JlYXRlIGEgbmV3IFB5dGhvbiBmaWxlJylcbiAgICAgICAgfVxuICAgICAgXVxuICAgIF0sXG4gICAgW1xuICAgICAgJ2p1bGlhJyxcbiAgICAgIFtcbiAgICAgICAge1xuICAgICAgICAgIGZpbGVFeHQ6ICdqbCcsXG4gICAgICAgICAgaWNvbk5hbWU6ICd1aS1jb21wb25lbnRzOmp1bGlhJyxcbiAgICAgICAgICBsYXVuY2hlckxhYmVsOiB0cmFucy5fXygnSnVsaWEgRmlsZScpLFxuICAgICAgICAgIHBhbGV0dGVMYWJlbDogdHJhbnMuX18oJ05ldyBKdWxpYSBGaWxlJyksXG4gICAgICAgICAgY2FwdGlvbjogdHJhbnMuX18oJ0NyZWF0ZSBhIG5ldyBKdWxpYSBmaWxlJylcbiAgICAgICAgfVxuICAgICAgXVxuICAgIF0sXG4gICAgW1xuICAgICAgJ1InLFxuICAgICAgW1xuICAgICAgICB7XG4gICAgICAgICAgZmlsZUV4dDogJ3InLFxuICAgICAgICAgIGljb25OYW1lOiAndWktY29tcG9uZW50czpyLWtlcm5lbCcsXG4gICAgICAgICAgbGF1bmNoZXJMYWJlbDogdHJhbnMuX18oJ1IgRmlsZScpLFxuICAgICAgICAgIHBhbGV0dGVMYWJlbDogdHJhbnMuX18oJ05ldyBSIEZpbGUnKSxcbiAgICAgICAgICBjYXB0aW9uOiB0cmFucy5fXygnQ3JlYXRlIGEgbmV3IFIgZmlsZScpXG4gICAgICAgIH1cbiAgICAgIF1cbiAgICBdXG4gIF0pO1xuXG4gIC8vIFVzZSBhdmFpbGFibGUga2VybmVscyB0byBkZXRlcm1pbmUgd2hpY2ggY29tbW9uIGZpbGUgdHlwZXMgc2hvdWxkIGhhdmUgJ0NyZWF0ZSBOZXcnIG9wdGlvbnMgaW4gdGhlIExhdW5jaGVyLCBGaWxlIEVkaXRvciBwYWxldHRlLCBhbmQgRmlsZSBtZW51XG4gIGNvbnN0IGdldEF2YWlsYWJsZUtlcm5lbEZpbGVUeXBlcyA9IGFzeW5jICgpOiBQcm9taXNlPFNldDxJRmlsZVR5cGVEYXRhPj4gPT4ge1xuICAgIGNvbnN0IHNwZWNzTWFuYWdlciA9IGFwcC5zZXJ2aWNlTWFuYWdlci5rZXJuZWxzcGVjcztcbiAgICBhd2FpdCBzcGVjc01hbmFnZXIucmVhZHk7XG4gICAgbGV0IGZpbGVUeXBlcyA9IG5ldyBTZXQ8SUZpbGVUeXBlRGF0YT4oKTtcbiAgICBjb25zdCBzcGVjcyA9IHNwZWNzTWFuYWdlci5zcGVjcz8ua2VybmVsc3BlY3MgPz8ge307XG4gICAgT2JqZWN0LmtleXMoc3BlY3MpLmZvckVhY2goc3BlYyA9PiB7XG4gICAgICBjb25zdCBzcGVjTW9kZWwgPSBzcGVjc1tzcGVjXTtcbiAgICAgIGlmIChzcGVjTW9kZWwpIHtcbiAgICAgICAgY29uc3QgZXh0cyA9IGNvbW1vbkxhbmd1YWdlRmlsZVR5cGVEYXRhLmdldChzcGVjTW9kZWwubGFuZ3VhZ2UpO1xuICAgICAgICBleHRzPy5mb3JFYWNoKGV4dCA9PiBmaWxlVHlwZXMuYWRkKGV4dCkpO1xuICAgICAgfVxuICAgIH0pO1xuICAgIHJldHVybiBmaWxlVHlwZXM7XG4gIH07XG5cbiAgLy8gSGFuZGxlIHN0YXRlIHJlc3RvcmF0aW9uLlxuICBpZiAocmVzdG9yZXIpIHtcbiAgICB2b2lkIHJlc3RvcmVyLnJlc3RvcmUodHJhY2tlciwge1xuICAgICAgY29tbWFuZDogJ2RvY21hbmFnZXI6b3BlbicsXG4gICAgICBhcmdzOiB3aWRnZXQgPT4gKHsgcGF0aDogd2lkZ2V0LmNvbnRleHQucGF0aCwgZmFjdG9yeTogRkFDVE9SWSB9KSxcbiAgICAgIG5hbWU6IHdpZGdldCA9PiB3aWRnZXQuY29udGV4dC5wYXRoXG4gICAgfSk7XG4gIH1cblxuICAvLyBBZGQgYSBjb25zb2xlIGNyZWF0b3IgdG8gdGhlIEZpbGUgbWVudVxuICAvLyBGZXRjaCB0aGUgaW5pdGlhbCBzdGF0ZSBvZiB0aGUgc2V0dGluZ3MuXG4gIFByb21pc2UuYWxsKFtzZXR0aW5nUmVnaXN0cnkubG9hZChpZCksIHJlc3RvcmVkXSlcbiAgICAudGhlbigoW3NldHRpbmdzXSkgPT4ge1xuICAgICAgQ29tbWFuZHMudXBkYXRlU2V0dGluZ3Moc2V0dGluZ3MsIGNvbW1hbmRzKTtcbiAgICAgIENvbW1hbmRzLnVwZGF0ZVRyYWNrZXIodHJhY2tlcik7XG4gICAgICBzZXR0aW5ncy5jaGFuZ2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgICBDb21tYW5kcy51cGRhdGVTZXR0aW5ncyhzZXR0aW5ncywgY29tbWFuZHMpO1xuICAgICAgICBDb21tYW5kcy51cGRhdGVUcmFja2VyKHRyYWNrZXIpO1xuICAgICAgfSk7XG4gICAgfSlcbiAgICAuY2F0Y2goKHJlYXNvbjogRXJyb3IpID0+IHtcbiAgICAgIGNvbnNvbGUuZXJyb3IocmVhc29uLm1lc3NhZ2UpO1xuICAgICAgQ29tbWFuZHMudXBkYXRlVHJhY2tlcih0cmFja2VyKTtcbiAgICB9KTtcblxuICBmYWN0b3J5LndpZGdldENyZWF0ZWQuY29ubmVjdCgoc2VuZGVyLCB3aWRnZXQpID0+IHtcbiAgICAvLyBOb3RpZnkgdGhlIHdpZGdldCB0cmFja2VyIGlmIHJlc3RvcmUgZGF0YSBuZWVkcyB0byB1cGRhdGUuXG4gICAgd2lkZ2V0LmNvbnRleHQucGF0aENoYW5nZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICB2b2lkIHRyYWNrZXIuc2F2ZSh3aWRnZXQpO1xuICAgIH0pO1xuICAgIHZvaWQgdHJhY2tlci5hZGQod2lkZ2V0KTtcbiAgICBDb21tYW5kcy51cGRhdGVXaWRnZXQod2lkZ2V0LmNvbnRlbnQpO1xuICB9KTtcbiAgYXBwLmRvY1JlZ2lzdHJ5LmFkZFdpZGdldEZhY3RvcnkoZmFjdG9yeSk7XG5cbiAgLy8gSGFuZGxlIHRoZSBzZXR0aW5ncyBvZiBuZXcgd2lkZ2V0cy5cbiAgdHJhY2tlci53aWRnZXRBZGRlZC5jb25uZWN0KChzZW5kZXIsIHdpZGdldCkgPT4ge1xuICAgIENvbW1hbmRzLnVwZGF0ZVdpZGdldCh3aWRnZXQuY29udGVudCk7XG4gIH0pO1xuXG4gIENvbW1hbmRzLmFkZENvbW1hbmRzKFxuICAgIGNvbW1hbmRzLFxuICAgIHNldHRpbmdSZWdpc3RyeSxcbiAgICB0cmFucyxcbiAgICBpZCxcbiAgICBpc0VuYWJsZWQsXG4gICAgdHJhY2tlcixcbiAgICBicm93c2VyRmFjdG9yeSxcbiAgICBjb25zb2xlVHJhY2tlcixcbiAgICBzZXNzaW9uRGlhbG9nc1xuICApO1xuXG4gIGNvbnN0IGNvZGVWaWV3ZXJUcmFja2VyID0gbmV3IFdpZGdldFRyYWNrZXI8TWFpbkFyZWFXaWRnZXQ8Q29kZVZpZXdlcldpZGdldD4+KFxuICAgIHtcbiAgICAgIG5hbWVzcGFjZTogJ2NvZGV2aWV3ZXInXG4gICAgfVxuICApO1xuXG4gIC8vIEhhbmRsZSBzdGF0ZSByZXN0b3JhdGlvbiBmb3IgY29kZSB2aWV3ZXJzXG4gIGlmIChyZXN0b3Jlcikge1xuICAgIHZvaWQgcmVzdG9yZXIucmVzdG9yZShjb2RlVmlld2VyVHJhY2tlciwge1xuICAgICAgY29tbWFuZDogQ29tbWFuZElEcy5vcGVuQ29kZVZpZXdlcixcbiAgICAgIGFyZ3M6IHdpZGdldCA9PiAoe1xuICAgICAgICBjb250ZW50OiB3aWRnZXQuY29udGVudC5jb250ZW50LFxuICAgICAgICBsYWJlbDogd2lkZ2V0LmNvbnRlbnQudGl0bGUubGFiZWwsXG4gICAgICAgIG1pbWVUeXBlOiB3aWRnZXQuY29udGVudC5taW1lVHlwZSxcbiAgICAgICAgd2lkZ2V0SWQ6IHdpZGdldC5jb250ZW50LmlkXG4gICAgICB9KSxcbiAgICAgIG5hbWU6IHdpZGdldCA9PiB3aWRnZXQuY29udGVudC5pZFxuICAgIH0pO1xuICB9XG5cbiAgQ29tbWFuZHMuYWRkT3BlbkNvZGVWaWV3ZXJDb21tYW5kKFxuICAgIGFwcCxcbiAgICBlZGl0b3JTZXJ2aWNlcyxcbiAgICBjb2RlVmlld2VyVHJhY2tlcixcbiAgICB0cmFuc1xuICApO1xuXG4gIC8vIEFkZCBhIGxhdW5jaGVyIGl0ZW0gaWYgdGhlIGxhdW5jaGVyIGlzIGF2YWlsYWJsZS5cbiAgaWYgKGxhdW5jaGVyKSB7XG4gICAgQ29tbWFuZHMuYWRkTGF1bmNoZXJJdGVtcyhsYXVuY2hlciwgdHJhbnMpO1xuICB9XG5cbiAgaWYgKHBhbGV0dGUpIHtcbiAgICBDb21tYW5kcy5hZGRQYWxldHRlSXRlbXMocGFsZXR0ZSwgdHJhbnMpO1xuICB9XG5cbiAgaWYgKG1lbnUpIHtcbiAgICBDb21tYW5kcy5hZGRNZW51SXRlbXMobWVudSwgdHJhY2tlciwgY29uc29sZVRyYWNrZXIsIGlzRW5hYmxlZCk7XG4gIH1cblxuICBnZXRBdmFpbGFibGVLZXJuZWxGaWxlVHlwZXMoKVxuICAgIC50aGVuKGF2YWlsYWJsZUtlcm5lbEZpbGVUeXBlcyA9PiB7XG4gICAgICBpZiAobGF1bmNoZXIpIHtcbiAgICAgICAgQ29tbWFuZHMuYWRkS2VybmVsTGFuZ3VhZ2VMYXVuY2hlckl0ZW1zKFxuICAgICAgICAgIGxhdW5jaGVyLFxuICAgICAgICAgIHRyYW5zLFxuICAgICAgICAgIGF2YWlsYWJsZUtlcm5lbEZpbGVUeXBlc1xuICAgICAgICApO1xuICAgICAgfVxuXG4gICAgICBpZiAocGFsZXR0ZSkge1xuICAgICAgICBDb21tYW5kcy5hZGRLZXJuZWxMYW5ndWFnZVBhbGV0dGVJdGVtcyhcbiAgICAgICAgICBwYWxldHRlLFxuICAgICAgICAgIHRyYW5zLFxuICAgICAgICAgIGF2YWlsYWJsZUtlcm5lbEZpbGVUeXBlc1xuICAgICAgICApO1xuICAgICAgfVxuXG4gICAgICBpZiAobWVudSkge1xuICAgICAgICBDb21tYW5kcy5hZGRLZXJuZWxMYW5ndWFnZU1lbnVJdGVtcyhtZW51LCBhdmFpbGFibGVLZXJuZWxGaWxlVHlwZXMpO1xuICAgICAgfVxuICAgIH0pXG4gICAgLmNhdGNoKChyZWFzb246IEVycm9yKSA9PiB7XG4gICAgICBjb25zb2xlLmVycm9yKHJlYXNvbi5tZXNzYWdlKTtcbiAgICB9KTtcblxuICBpZiAodG9jUmVnaXN0cnkpIHtcbiAgICB0b2NSZWdpc3RyeS5hZGQobmV3IExhVGVYVGFibGVPZkNvbnRlbnRzRmFjdG9yeSh0cmFja2VyKSk7XG4gICAgdG9jUmVnaXN0cnkuYWRkKG5ldyBNYXJrZG93blRhYmxlT2ZDb250ZW50c0ZhY3RvcnkodHJhY2tlcikpO1xuICAgIHRvY1JlZ2lzdHJ5LmFkZChuZXcgUHl0aG9uVGFibGVPZkNvbnRlbnRzRmFjdG9yeSh0cmFja2VyKSk7XG4gIH1cblxuICByZXR1cm4gdHJhY2tlcjtcbn1cblxuLyoqXG4gKiBBY3RpdmF0ZSB0aGUgY29tcGxldGVyIHNlcnZpY2UgZm9yIGZpbGUgZWRpdG9yLlxuICovXG5mdW5jdGlvbiBhY3RpdmF0ZUZpbGVFZGl0b3JDb21wbGV0ZXJTZXJ2aWNlKFxuICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgZWRpdG9yVHJhY2tlcjogSUVkaXRvclRyYWNrZXIsXG4gIG1hbmFnZXI6IElDb21wbGV0aW9uUHJvdmlkZXJNYW5hZ2VyIHwgbnVsbCxcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IgfCBudWxsXG4pOiB2b2lkIHtcbiAgaWYgKCFtYW5hZ2VyKSB7XG4gICAgcmV0dXJuO1xuICB9XG5cbiAgQ29tbWFuZHMuYWRkQ29tcGxldGVyQ29tbWFuZHMoXG4gICAgYXBwLmNvbW1hbmRzLFxuICAgIGVkaXRvclRyYWNrZXIsXG4gICAgbWFuYWdlcixcbiAgICB0cmFuc2xhdG9yXG4gICk7XG4gIGNvbnN0IHNlc3Npb25NYW5hZ2VyID0gYXBwLnNlcnZpY2VNYW5hZ2VyLnNlc3Npb25zO1xuXG4gIGNvbnN0IF9hY3RpdmVTZXNzaW9ucyA9IG5ldyBNYXA8c3RyaW5nLCBTZXNzaW9uLklTZXNzaW9uQ29ubmVjdGlvbj4oKTtcbiAgY29uc3QgdXBkYXRlQ29tcGxldGVyID0gYXN5bmMgKFxuICAgIF86IElFZGl0b3JUcmFja2VyLFxuICAgIHdpZGdldDogSURvY3VtZW50V2lkZ2V0PEZpbGVFZGl0b3I+XG4gICkgPT4ge1xuICAgIGNvbnN0IGNvbXBsZXRlckNvbnRleHQgPSB7XG4gICAgICBlZGl0b3I6IHdpZGdldC5jb250ZW50LmVkaXRvcixcbiAgICAgIHdpZGdldFxuICAgIH07XG5cbiAgICBhd2FpdCBtYW5hZ2VyLnVwZGF0ZUNvbXBsZXRlcihjb21wbGV0ZXJDb250ZXh0KTtcbiAgICBjb25zdCBvblJ1bm5pbmdDaGFuZ2VkID0gKFxuICAgICAgXzogU2Vzc2lvbi5JTWFuYWdlcixcbiAgICAgIG1vZGVsczogU2Vzc2lvbi5JTW9kZWxbXVxuICAgICkgPT4ge1xuICAgICAgY29uc3Qgb2xkU2Vzc2lvbiA9IF9hY3RpdmVTZXNzaW9ucy5nZXQod2lkZ2V0LmlkKTtcbiAgICAgIC8vIFNlYXJjaCBmb3IgYSBtYXRjaGluZyBwYXRoLlxuICAgICAgY29uc3QgbW9kZWwgPSBmaW5kKG1vZGVscywgbSA9PiBtLnBhdGggPT09IHdpZGdldC5jb250ZXh0LnBhdGgpO1xuICAgICAgaWYgKG1vZGVsKSB7XG4gICAgICAgIC8vIElmIHRoZXJlIGlzIGEgbWF0Y2hpbmcgcGF0aCwgYnV0IGl0IGlzIHRoZSBzYW1lXG4gICAgICAgIC8vIHNlc3Npb24gYXMgd2UgcHJldmlvdXNseSBoYWQsIGRvIG5vdGhpbmcuXG4gICAgICAgIGlmIChvbGRTZXNzaW9uICYmIG9sZFNlc3Npb24uaWQgPT09IG1vZGVsLmlkKSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIC8vIE90aGVyd2lzZSwgZGlzcG9zZSBvZiB0aGUgb2xkIHNlc3Npb24gYW5kIHJlc2V0IHRvXG4gICAgICAgIC8vIGEgbmV3IENvbXBsZXRpb25Db25uZWN0b3IuXG4gICAgICAgIGlmIChvbGRTZXNzaW9uKSB7XG4gICAgICAgICAgX2FjdGl2ZVNlc3Npb25zLmRlbGV0ZSh3aWRnZXQuaWQpO1xuICAgICAgICAgIG9sZFNlc3Npb24uZGlzcG9zZSgpO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IHNlc3Npb24gPSBzZXNzaW9uTWFuYWdlci5jb25uZWN0VG8oeyBtb2RlbCB9KTtcbiAgICAgICAgY29uc3QgbmV3Q29tcGxldGVyQ29udGV4dCA9IHtcbiAgICAgICAgICBlZGl0b3I6IHdpZGdldC5jb250ZW50LmVkaXRvcixcbiAgICAgICAgICB3aWRnZXQsXG4gICAgICAgICAgc2Vzc2lvblxuICAgICAgICB9O1xuICAgICAgICBtYW5hZ2VyLnVwZGF0ZUNvbXBsZXRlcihuZXdDb21wbGV0ZXJDb250ZXh0KS5jYXRjaChjb25zb2xlLmVycm9yKTtcbiAgICAgICAgX2FjdGl2ZVNlc3Npb25zLnNldCh3aWRnZXQuaWQsIHNlc3Npb24pO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgLy8gSWYgd2UgZGlkbid0IGZpbmQgYSBtYXRjaCwgbWFrZSBzdXJlXG4gICAgICAgIC8vIHRoZSBjb25uZWN0b3IgaXMgdGhlIGNvbnRleHRDb25uZWN0b3IgYW5kXG4gICAgICAgIC8vIGRpc3Bvc2Ugb2YgYW55IHByZXZpb3VzIGNvbm5lY3Rpb24uXG4gICAgICAgIGlmIChvbGRTZXNzaW9uKSB7XG4gICAgICAgICAgX2FjdGl2ZVNlc3Npb25zLmRlbGV0ZSh3aWRnZXQuaWQpO1xuICAgICAgICAgIG9sZFNlc3Npb24uZGlzcG9zZSgpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfTtcblxuICAgIG9uUnVubmluZ0NoYW5nZWQoc2Vzc2lvbk1hbmFnZXIsIHRvQXJyYXkoc2Vzc2lvbk1hbmFnZXIucnVubmluZygpKSk7XG4gICAgc2Vzc2lvbk1hbmFnZXIucnVubmluZ0NoYW5nZWQuY29ubmVjdChvblJ1bm5pbmdDaGFuZ2VkKTtcblxuICAgIHdpZGdldC5kaXNwb3NlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgIHNlc3Npb25NYW5hZ2VyLnJ1bm5pbmdDaGFuZ2VkLmRpc2Nvbm5lY3Qob25SdW5uaW5nQ2hhbmdlZCk7XG4gICAgICBjb25zdCBzZXNzaW9uID0gX2FjdGl2ZVNlc3Npb25zLmdldCh3aWRnZXQuaWQpO1xuICAgICAgaWYgKHNlc3Npb24pIHtcbiAgICAgICAgX2FjdGl2ZVNlc3Npb25zLmRlbGV0ZSh3aWRnZXQuaWQpO1xuICAgICAgICBzZXNzaW9uLmRpc3Bvc2UoKTtcbiAgICAgIH1cbiAgICB9KTtcbiAgfTtcbiAgZWRpdG9yVHJhY2tlci53aWRnZXRBZGRlZC5jb25uZWN0KHVwZGF0ZUNvbXBsZXRlcik7XG4gIG1hbmFnZXIuYWN0aXZlUHJvdmlkZXJzQ2hhbmdlZC5jb25uZWN0KCgpID0+IHtcbiAgICBlZGl0b3JUcmFja2VyLmZvckVhY2goZWRpdG9yV2lkZ2V0ID0+IHtcbiAgICAgIHVwZGF0ZUNvbXBsZXRlcihlZGl0b3JUcmFja2VyLCBlZGl0b3JXaWRnZXQpLmNhdGNoKGNvbnNvbGUuZXJyb3IpO1xuICAgIH0pO1xuICB9KTtcbn1cblxuZnVuY3Rpb24gYWN0aXZhdGVGaWxlRWRpdG9yTGFuZ3VhZ2VTZXJ2ZXIoXG4gIGFwcDogSnVweXRlckZyb250RW5kLFxuICBlZGl0b3JzOiBJRWRpdG9yVHJhY2tlcixcbiAgY29ubmVjdGlvbk1hbmFnZXI6IElMU1BEb2N1bWVudENvbm5lY3Rpb25NYW5hZ2VyLFxuICBmZWF0dXJlTWFuYWdlcjogSUxTUEZlYXR1cmVNYW5hZ2VyLFxuICBleHRyYWN0b3JNYW5hZ2VyOiBJTFNQQ29kZUV4dHJhY3RvcnNNYW5hZ2VyXG4pOiB2b2lkIHtcbiAgZWRpdG9ycy53aWRnZXRBZGRlZC5jb25uZWN0KGFzeW5jIChfLCBlZGl0b3IpID0+IHtcbiAgICBjb25zdCBhZGFwdGVyID0gbmV3IEZpbGVFZGl0b3JBZGFwdGVyKGVkaXRvciwge1xuICAgICAgY29ubmVjdGlvbk1hbmFnZXIsXG4gICAgICBmZWF0dXJlTWFuYWdlcixcbiAgICAgIGZvcmVpZ25Db2RlRXh0cmFjdG9yc01hbmFnZXI6IGV4dHJhY3Rvck1hbmFnZXIsXG4gICAgICBkb2NSZWdpc3RyeTogYXBwLmRvY1JlZ2lzdHJ5XG4gICAgfSk7XG4gICAgY29ubmVjdGlvbk1hbmFnZXIucmVnaXN0ZXJBZGFwdGVyKGVkaXRvci5jb250ZXh0LnBhdGgsIGFkYXB0ZXIpO1xuICB9KTtcbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==