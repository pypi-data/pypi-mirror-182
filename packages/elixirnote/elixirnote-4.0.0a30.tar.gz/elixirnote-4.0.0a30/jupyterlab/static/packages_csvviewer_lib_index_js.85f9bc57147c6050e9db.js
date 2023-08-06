"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_csvviewer_lib_index_js"],{

/***/ "../../packages/csvviewer/lib/index.js":
/*!*********************************************!*\
  !*** ../../packages/csvviewer/lib/index.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CSVDelimiter": () => (/* reexport safe */ _toolbar__WEBPACK_IMPORTED_MODULE_2__.CSVDelimiter),
/* harmony export */   "CSVDocumentWidget": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_3__.CSVDocumentWidget),
/* harmony export */   "CSVViewer": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_3__.CSVViewer),
/* harmony export */   "CSVViewerFactory": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_3__.CSVViewerFactory),
/* harmony export */   "DSVModel": () => (/* reexport safe */ _model__WEBPACK_IMPORTED_MODULE_0__.DSVModel),
/* harmony export */   "GridSearchService": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_3__.GridSearchService),
/* harmony export */   "TSVViewerFactory": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_3__.TSVViewerFactory),
/* harmony export */   "TextRenderConfig": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_3__.TextRenderConfig),
/* harmony export */   "parseDSV": () => (/* reexport safe */ _parse__WEBPACK_IMPORTED_MODULE_1__.parseDSV),
/* harmony export */   "parseDSVNoQuotes": () => (/* reexport safe */ _parse__WEBPACK_IMPORTED_MODULE_1__.parseDSVNoQuotes)
/* harmony export */ });
/* harmony import */ var _model__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./model */ "../../packages/csvviewer/lib/model.js");
/* harmony import */ var _parse__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./parse */ "../../packages/csvviewer/lib/parse.js");
/* harmony import */ var _toolbar__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./toolbar */ "../../packages/csvviewer/lib/toolbar.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./widget */ "../../packages/csvviewer/lib/widget.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module csvviewer
 */






/***/ }),

/***/ "../../packages/csvviewer/lib/model.js":
/*!*********************************************!*\
  !*** ../../packages/csvviewer/lib/model.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "DSVModel": () => (/* binding */ DSVModel)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_datagrid__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/datagrid */ "webpack/sharing/consume/default/@lumino/datagrid/@lumino/datagrid");
/* harmony import */ var _lumino_datagrid__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_datagrid__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _parse__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./parse */ "../../packages/csvviewer/lib/parse.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/*
Possible ideas for further implementation:

- Show a spinner or something visible when we are doing delayed parsing.
- The cache right now handles scrolling down great - it gets the next several hundred rows. However, scrolling up causes lots of cache misses - each new row causes a flush of the cache. When invalidating an entire cache, we should put the requested row in middle of the cache (adjusting for rows at the beginning or end). When populating a cache, we should retrieve rows both above and below the requested row.
- When we have a header, and we are guessing the parser to use, try checking just the part of the file *after* the header row for quotes. I think often a first header row is quoted, but the rest of the file is not and can be parsed much faster.
- autdetect the delimiter (look for comma, tab, semicolon in first line. If more than one found, parse first row with comma, tab, semicolon delimiters. One with most fields wins).
- Toolbar buttons to control the row delimiter, the parsing engine (quoted/not quoted), the quote character, etc.
- Investigate incremental loading strategies in the parseAsync function. In initial investigations, setting the chunk size to 100k in parseAsync seems cause instability with large files in Chrome (such as 8-million row files). Perhaps this is because we are recycling the row offset and column offset arrays quickly? It doesn't seem that there is a memory leak. On this theory, perhaps we just need to keep the offsets list an actual list, and pass it into the parsing function to extend without copying, and finalize it into an array buffer only when we are done parsing. Or perhaps we double the size of the array buffer each time, which may be wasteful, but at the end we trim it down if it's too wasteful (perhaps we have our own object that is backed by an array buffer, but has a push method that will automatically double the array buffer size as needed, and a trim function to finalize the array to exactly the size needed)? Or perhaps we don't use array buffers at all - compare the memory cost and speed of keeping the offsets as lists instead of memory buffers.
- Investigate a time-based incremental parsing strategy, rather than a row-based one. The parser could take a maximum time to parse (say 300ms), and will parse up to that duration, in which case the parser probably also needs a way to notify when it has reached the end of a file.
- For very large files, where we are only storing a small cache, scrolling is very laggy in Safari. It would be good to profile it.
*/
/**
 * Possible delimiter-separated data parsers.
 */
const PARSERS = {
    quotes: _parse__WEBPACK_IMPORTED_MODULE_2__.parseDSV,
    noquotes: _parse__WEBPACK_IMPORTED_MODULE_2__.parseDSVNoQuotes
};
/**
 * A data model implementation for in-memory delimiter-separated data.
 *
 * #### Notes
 * This model handles data with up to 2**32 characters.
 */
class DSVModel extends _lumino_datagrid__WEBPACK_IMPORTED_MODULE_1__.DataModel {
    /**
     * Create a data model with static CSV data.
     *
     * @param options - The options for initializing the data model.
     */
    constructor(options) {
        super();
        this._rowCount = 0;
        // Cache information
        /**
         * The header strings.
         */
        this._header = [];
        /**
         * The column offset cache, starting with row _columnOffsetsStartingRow
         *
         * #### Notes
         * The index of the first character in the data string for row r, column c is
         * _columnOffsets[(r-this._columnOffsetsStartingRow)*numColumns+c]
         */
        this._columnOffsets = new Uint32Array(0);
        /**
         * The row that _columnOffsets[0] represents.
         */
        this._columnOffsetsStartingRow = 0;
        /**
         * The maximum number of rows to parse when there is a cache miss.
         */
        this._maxCacheGet = 1000;
        /**
         * The index for the start of each row.
         */
        this._rowOffsets = new Uint32Array(0);
        // Bookkeeping variables.
        this._delayedParse = null;
        this._startedParsing = false;
        this._doneParsing = false;
        this._isDisposed = false;
        this._ready = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.PromiseDelegate();
        let { data, delimiter = ',', rowDelimiter = undefined, quote = '"', quoteParser = undefined, header = true, initialRows = 500 } = options;
        this._rawData = data;
        this._delimiter = delimiter;
        this._quote = quote;
        this._quoteEscaped = new RegExp(quote + quote, 'g');
        this._initialRows = initialRows;
        // Guess the row delimiter if it was not supplied. This will be fooled if a
        // different line delimiter possibility appears in the first row.
        if (rowDelimiter === undefined) {
            const i = data.slice(0, 5000).indexOf('\r');
            if (i === -1) {
                rowDelimiter = '\n';
            }
            else if (data[i + 1] === '\n') {
                rowDelimiter = '\r\n';
            }
            else {
                rowDelimiter = '\r';
            }
        }
        this._rowDelimiter = rowDelimiter;
        if (quoteParser === undefined) {
            // Check for the existence of quotes if the quoteParser is not set.
            quoteParser = data.indexOf(quote) >= 0;
        }
        this._parser = quoteParser ? 'quotes' : 'noquotes';
        // Parse the data.
        this.parseAsync();
        // Cache the header row.
        if (header === true && this._columnCount > 0) {
            const h = [];
            for (let c = 0; c < this._columnCount; c++) {
                h.push(this._getField(0, c));
            }
            this._header = h;
        }
    }
    /**
     * Whether this model has been disposed.
     */
    get isDisposed() {
        return this._isDisposed;
    }
    /**
     * A promise that resolves when the model has parsed all of its data.
     */
    get ready() {
        return this._ready.promise;
    }
    /**
     * The string representation of the data.
     */
    get rawData() {
        return this._rawData;
    }
    set rawData(value) {
        this._rawData = value;
    }
    /**
     * The initial chunk of rows to parse.
     */
    get initialRows() {
        return this._initialRows;
    }
    set initialRows(value) {
        this._initialRows = value;
    }
    /**
     * The header strings.
     */
    get header() {
        return this._header;
    }
    set header(value) {
        this._header = value;
    }
    /**
     * The delimiter between entries on the same row.
     */
    get delimiter() {
        return this._delimiter;
    }
    /**
     * The delimiter between rows.
     */
    get rowDelimiter() {
        return this._rowDelimiter;
    }
    /**
     * A boolean determined by whether parsing has completed.
     */
    get doneParsing() {
        return this._doneParsing;
    }
    /**
     * Get the row count for a region in the data model.
     *
     * @param region - The row region of interest.
     *
     * @returns - The row count for the region.
     */
    rowCount(region) {
        if (region === 'body') {
            if (this._header.length === 0) {
                return this._rowCount;
            }
            else {
                return this._rowCount - 1;
            }
        }
        return 1;
    }
    /**
     * Get the column count for a region in the data model.
     *
     * @param region - The column region of interest.
     *
     * @returns - The column count for the region.
     */
    columnCount(region) {
        if (region === 'body') {
            return this._columnCount;
        }
        return 1;
    }
    /**
     * Get the data value for a cell in the data model.
     *
     * @param region - The cell region of interest.
     *
     * @param row - The row index of the cell of interest.
     *
     * @param column - The column index of the cell of interest.
     *
     * @param returns - The data value for the specified cell.
     */
    data(region, row, column) {
        let value;
        // Look up the field and value for the region.
        switch (region) {
            case 'body':
                if (this._header.length === 0) {
                    value = this._getField(row, column);
                }
                else {
                    value = this._getField(row + 1, column);
                }
                break;
            case 'column-header':
                if (this._header.length === 0) {
                    value = (column + 1).toString();
                }
                else {
                    value = this._header[column];
                }
                break;
            case 'row-header':
                value = (row + 1).toString();
                break;
            case 'corner-header':
                value = '';
                break;
            default:
                throw 'unreachable';
        }
        // Return the final value.
        return value;
    }
    /**
     * Dispose the resources held by this model.
     */
    dispose() {
        if (this._isDisposed) {
            return;
        }
        this._isDisposed = true;
        this._columnCount = undefined;
        this._rowCount = undefined;
        this._rowOffsets = null;
        this._columnOffsets = null;
        this._rawData = null;
        // Clear out state associated with the asynchronous parsing.
        if (this._doneParsing === false) {
            // Explicitly catch this rejection at least once so an error is not thrown
            // to the console.
            this.ready.catch(() => {
                return;
            });
            this._ready.reject(undefined);
        }
        if (this._delayedParse !== null) {
            window.clearTimeout(this._delayedParse);
        }
    }
    /**
     * Get the index in the data string for the first character of a row and
     * column.
     *
     * @param row - The row of the data item.
     * @param column - The column of the data item.
     * @returns - The index into the data string where the data item starts.
     */
    getOffsetIndex(row, column) {
        // Declare local variables.
        const ncols = this._columnCount;
        // Check to see if row *should* be in the cache, based on the cache size.
        let rowIndex = (row - this._columnOffsetsStartingRow) * ncols;
        if (rowIndex < 0 || rowIndex > this._columnOffsets.length) {
            // Row isn't in the cache, so we invalidate the entire cache and set up
            // the cache to hold the requested row.
            this._columnOffsets.fill(0xffffffff);
            this._columnOffsetsStartingRow = row;
            rowIndex = 0;
        }
        // Check to see if we need to fetch the row data into the cache.
        if (this._columnOffsets[rowIndex] === 0xffffffff) {
            // Figure out how many rows below us also need to be fetched.
            let maxRows = 1;
            while (maxRows <= this._maxCacheGet &&
                this._columnOffsets[rowIndex + maxRows * ncols] === 0xffffff) {
                maxRows++;
            }
            // Parse the data to get the column offsets.
            const { offsets } = PARSERS[this._parser]({
                data: this._rawData,
                delimiter: this._delimiter,
                rowDelimiter: this._rowDelimiter,
                quote: this._quote,
                columnOffsets: true,
                maxRows: maxRows,
                ncols: ncols,
                startIndex: this._rowOffsets[row]
            });
            // Copy results to the cache.
            for (let i = 0; i < offsets.length; i++) {
                this._columnOffsets[rowIndex + i] = offsets[i];
            }
        }
        // Return the offset index from cache.
        return this._columnOffsets[rowIndex + column];
    }
    /**
     * Parse the data string asynchronously.
     *
     * #### Notes
     * It can take several seconds to parse a several hundred megabyte string, so
     * we parse the first 500 rows to get something up on the screen, then we
     * parse the full data string asynchronously.
     */
    parseAsync() {
        // Number of rows to get initially.
        let currentRows = this._initialRows;
        // Number of rows to get in each chunk thereafter. We set this high to just
        // get the rest of the rows for now.
        let chunkRows = Math.pow(2, 32) - 1;
        // We give the UI a chance to draw by delaying the chunk parsing.
        const delay = 30; // milliseconds
        // Define a function to parse a chunk up to and including endRow.
        const parseChunk = (endRow) => {
            try {
                this._computeRowOffsets(endRow);
            }
            catch (e) {
                // Sometimes the data string cannot be parsed with the full parser (for
                // example, we may have the wrong delimiter). In these cases, fall back to
                // the simpler parser so we can show something.
                if (this._parser === 'quotes') {
                    console.warn(e);
                    this._parser = 'noquotes';
                    this._resetParser();
                    this._computeRowOffsets(endRow);
                }
                else {
                    throw e;
                }
            }
            return this._doneParsing;
        };
        // Reset the parser to its initial state.
        this._resetParser();
        // Parse the first rows to give us the start of the data right away.
        const done = parseChunk(currentRows);
        // If we are done, return early.
        if (done) {
            return;
        }
        // Define a function to recursively parse the next chunk after a delay.
        const delayedParse = () => {
            // Parse up to the new end row.
            const done = parseChunk(currentRows + chunkRows);
            currentRows += chunkRows;
            // Gradually double the chunk size until we reach a million rows, if we
            // start below a million-row chunk size.
            if (chunkRows < 1000000) {
                chunkRows *= 2;
            }
            // If we aren't done, the schedule another parse.
            if (done) {
                this._delayedParse = null;
            }
            else {
                this._delayedParse = window.setTimeout(delayedParse, delay);
            }
        };
        // Parse full data string in chunks, delayed by a few milliseconds to give the UI a chance to draw.
        this._delayedParse = window.setTimeout(delayedParse, delay);
    }
    /**
     * Compute the row offsets and initialize the column offset cache.
     *
     * @param endRow - The last row to parse, from the start of the data (first
     * row is row 1).
     *
     * #### Notes
     * This method supports parsing the data incrementally by calling it with
     * incrementally higher endRow. Rows that have already been parsed will not be
     * parsed again.
     */
    _computeRowOffsets(endRow = 4294967295) {
        var _a;
        // If we've already parsed up to endRow, or if we've already parsed the
        // entire data set, return early.
        if (this._rowCount >= endRow || this._doneParsing === true) {
            return;
        }
        // Compute the column count if we don't already have it.
        if (this._columnCount === undefined) {
            // Get number of columns in first row
            this._columnCount = PARSERS[this._parser]({
                data: this._rawData,
                delimiter: this._delimiter,
                rowDelimiter: this._rowDelimiter,
                quote: this._quote,
                columnOffsets: true,
                maxRows: 1
            }).ncols;
        }
        // `reparse` is the number of rows we are requesting to parse over again.
        // We generally start at the beginning of the last row offset, so that the
        // first row offset returned is the same as the last row offset we already
        // have. We parse the data up to and including the requested row.
        const reparse = this._rowCount > 0 ? 1 : 0;
        const { nrows, offsets } = PARSERS[this._parser]({
            data: this._rawData,
            startIndex: (_a = this._rowOffsets[this._rowCount - reparse]) !== null && _a !== void 0 ? _a : 0,
            delimiter: this._delimiter,
            rowDelimiter: this._rowDelimiter,
            quote: this._quote,
            columnOffsets: false,
            maxRows: endRow - this._rowCount + reparse
        });
        // If we have already set up our initial bookkeeping, return early if we
        // did not get any new rows beyond the last row that we've parsed, i.e.,
        // nrows===1.
        if (this._startedParsing && nrows <= reparse) {
            this._doneParsing = true;
            this._ready.resolve(undefined);
            return;
        }
        this._startedParsing = true;
        // Update the row count, accounting for how many rows were reparsed.
        const oldRowCount = this._rowCount;
        const duplicateRows = Math.min(nrows, reparse);
        this._rowCount = oldRowCount + nrows - duplicateRows;
        // If we didn't reach the requested row, we must be done.
        if (this._rowCount < endRow) {
            this._doneParsing = true;
            this._ready.resolve(undefined);
        }
        // Copy the new offsets into a new row offset array if needed.
        if (this._rowCount > oldRowCount) {
            const oldRowOffsets = this._rowOffsets;
            this._rowOffsets = new Uint32Array(this._rowCount);
            this._rowOffsets.set(oldRowOffsets);
            this._rowOffsets.set(offsets, oldRowCount - duplicateRows);
        }
        // Expand the column offsets array if needed
        // If the full column offsets array is small enough, build a cache big
        // enough for all column offsets. We allocate up to 128 megabytes:
        // 128*(2**20 bytes/M)/(4 bytes/entry) = 33554432 entries.
        const maxColumnOffsetsRows = Math.floor(33554432 / this._columnCount);
        // We need to expand the column offset array if we were storing all column
        // offsets before. Check to see if the previous size was small enough that
        // we stored all column offsets.
        if (oldRowCount <= maxColumnOffsetsRows) {
            // Check to see if the new column offsets array is small enough to still
            // store, or if we should cut over to a small cache.
            if (this._rowCount <= maxColumnOffsetsRows) {
                // Expand the existing column offset array for new column offsets.
                const oldColumnOffsets = this._columnOffsets;
                this._columnOffsets = new Uint32Array(this._rowCount * this._columnCount);
                this._columnOffsets.set(oldColumnOffsets);
                this._columnOffsets.fill(0xffffffff, oldColumnOffsets.length);
            }
            else {
                // If not, then our cache size is at most the maximum number of rows we
                // fill in the cache at a time.
                const oldColumnOffsets = this._columnOffsets;
                this._columnOffsets = new Uint32Array(Math.min(this._maxCacheGet, maxColumnOffsetsRows) * this._columnCount);
                // Fill in the entries we already have.
                this._columnOffsets.set(oldColumnOffsets.subarray(0, this._columnOffsets.length));
                // Invalidate the rest of the entries.
                this._columnOffsets.fill(0xffffffff, oldColumnOffsets.length);
                this._columnOffsetsStartingRow = 0;
            }
        }
        // We have more rows than before, so emit the rows-inserted change signal.
        let firstIndex = oldRowCount;
        if (this._header.length > 0) {
            firstIndex -= 1;
        }
        this.emitChanged({
            type: 'rows-inserted',
            region: 'body',
            index: firstIndex,
            span: this._rowCount - oldRowCount
        });
    }
    /**
     * Get the parsed string field for a row and column.
     *
     * @param row - The row number of the data item.
     * @param column - The column number of the data item.
     * @returns The parsed string for the data item.
     */
    _getField(row, column) {
        // Declare local variables.
        let value;
        let nextIndex;
        // Find the index for the first character in the field.
        const index = this.getOffsetIndex(row, column);
        // Initialize the trim adjustments.
        let trimRight = 0;
        let trimLeft = 0;
        // Find the end of the slice (the start of the next field), and how much we
        // should adjust to trim off a trailing field or row delimiter. First check
        // if we are getting the last column.
        if (column === this._columnCount - 1) {
            // Check if we are getting any row but the last.
            if (row < this._rowCount - 1) {
                // Set the next offset to the next row, column 0.
                nextIndex = this.getOffsetIndex(row + 1, 0);
                // Since we are not at the last row, we need to trim off the row
                // delimiter.
                trimRight += this._rowDelimiter.length;
            }
            else {
                // We are getting the last data item, so the slice end is the end of the
                // data string.
                nextIndex = this._rawData.length;
                // The string may or may not end in a row delimiter (RFC 4180 2.2), so
                // we explicitly check if we should trim off a row delimiter.
                if (this._rawData[nextIndex - 1] ===
                    this._rowDelimiter[this._rowDelimiter.length - 1]) {
                    trimRight += this._rowDelimiter.length;
                }
            }
        }
        else {
            // The next field starts at the next column offset.
            nextIndex = this.getOffsetIndex(row, column + 1);
            // Trim off the delimiter if it exists at the end of the field
            if (index < nextIndex &&
                this._rawData[nextIndex - 1] === this._delimiter) {
                trimRight += 1;
            }
        }
        // Check to see if the field begins with a quote. If it does, trim a quote on either side.
        if (this._rawData[index] === this._quote) {
            trimLeft += 1;
            trimRight += 1;
        }
        // Slice the actual value out of the data string.
        value = this._rawData.slice(index + trimLeft, nextIndex - trimRight);
        // If we have a quoted field and we have an escaped quote inside it, unescape it.
        if (trimLeft === 1 && value.indexOf(this._quote) !== -1) {
            value = value.replace(this._quoteEscaped, this._quote);
        }
        // Return the value.
        return value;
    }
    /**
     * Reset the parser state.
     */
    _resetParser() {
        this._columnCount = undefined;
        this._rowOffsets = new Uint32Array(0);
        this._rowCount = 0;
        this._startedParsing = false;
        this._columnOffsets = new Uint32Array(0);
        // Clear out state associated with the asynchronous parsing.
        if (this._doneParsing === false) {
            // Explicitly catch this rejection at least once so an error is not thrown
            // to the console.
            this.ready.catch(() => {
                return;
            });
            this._ready.reject(undefined);
        }
        this._doneParsing = false;
        this._ready = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.PromiseDelegate();
        if (this._delayedParse !== null) {
            window.clearTimeout(this._delayedParse);
            this._delayedParse = null;
        }
        this.emitChanged({ type: 'model-reset' });
    }
}


/***/ }),

/***/ "../../packages/csvviewer/lib/parse.js":
/*!*********************************************!*\
  !*** ../../packages/csvviewer/lib/parse.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "parseDSV": () => (/* binding */ parseDSV),
/* harmony export */   "parseDSVNoQuotes": () => (/* binding */ parseDSVNoQuotes)
/* harmony export */ });
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * Possible parser states.
 */
var STATE;
(function (STATE) {
    STATE[STATE["QUOTED_FIELD"] = 0] = "QUOTED_FIELD";
    STATE[STATE["QUOTED_FIELD_QUOTE"] = 1] = "QUOTED_FIELD_QUOTE";
    STATE[STATE["UNQUOTED_FIELD"] = 2] = "UNQUOTED_FIELD";
    STATE[STATE["NEW_FIELD"] = 3] = "NEW_FIELD";
    STATE[STATE["NEW_ROW"] = 4] = "NEW_ROW";
})(STATE || (STATE = {}));
/**
 * Possible row delimiters for the parser.
 */
var ROW_DELIMITER;
(function (ROW_DELIMITER) {
    ROW_DELIMITER[ROW_DELIMITER["CR"] = 0] = "CR";
    ROW_DELIMITER[ROW_DELIMITER["CRLF"] = 1] = "CRLF";
    ROW_DELIMITER[ROW_DELIMITER["LF"] = 2] = "LF";
})(ROW_DELIMITER || (ROW_DELIMITER = {}));
/**
 * Parse delimiter-separated data.
 *
 * @param options: The parser options
 * @returns An object giving the offsets for the rows or columns parsed.
 *
 * #### Notes
 * This implementation is based on [RFC 4180](https://tools.ietf.org/html/rfc4180).
 */
function parseDSV(options) {
    const { data, columnOffsets, delimiter = ',', startIndex = 0, maxRows = 0xffffffff, rowDelimiter = '\r\n', quote = '"' } = options;
    // ncols will be set automatically if it is undefined.
    let ncols = options.ncols;
    // The number of rows we've already parsed.
    let nrows = 0;
    // The row or column offsets we return.
    const offsets = [];
    // Set up some useful local variables.
    const CH_DELIMITER = delimiter.charCodeAt(0);
    const CH_QUOTE = quote.charCodeAt(0);
    const CH_LF = 10; // \n
    const CH_CR = 13; // \r
    const endIndex = data.length;
    const { QUOTED_FIELD, QUOTED_FIELD_QUOTE, UNQUOTED_FIELD, NEW_FIELD, NEW_ROW } = STATE;
    const { CR, LF, CRLF } = ROW_DELIMITER;
    const [rowDelimiterCode, rowDelimiterLength] = rowDelimiter === '\r\n'
        ? [CRLF, 2]
        : rowDelimiter === '\r'
            ? [CR, 1]
            : [LF, 1];
    // Always start off at the beginning of a row.
    let state = NEW_ROW;
    // Set up the starting index.
    let i = startIndex;
    // We initialize to 0 just in case we are asked to parse past the end of the
    // string. In that case, we want the number of columns to be 0.
    let col = 0;
    // Declare some useful temporaries
    let char;
    // Loop through the data string
    while (i < endIndex) {
        // i is the index of a character in the state.
        // If we just hit a new row, and there are still characters left, push a new
        // offset on and reset the column counter. We want this logic at the top of
        // the while loop rather than the bottom because we don't want a trailing
        // row delimiter at the end of the data to trigger a new row offset.
        if (state === NEW_ROW) {
            // Start a new row and reset the column counter.
            offsets.push(i);
            col = 1;
        }
        // Below, we handle this character, modify the parser state and increment the index to be consistent.
        // Get the integer code for the current character, so the comparisons below
        // are faster.
        char = data.charCodeAt(i);
        // Update the parser state. This switch statement is responsible for
        // updating the state to be consistent with the index i+1 (we increment i
        // after the switch statement). In some situations, we may increment i
        // inside this loop to skip over indices as a shortcut.
        switch (state) {
            // At the beginning of a row or field, we can have a quote, row delimiter, or field delimiter.
            case NEW_ROW:
            case NEW_FIELD:
                switch (char) {
                    // If we have a quote, we are starting an escaped field.
                    case CH_QUOTE:
                        state = QUOTED_FIELD;
                        break;
                    // A field delimiter means we are starting a new field.
                    case CH_DELIMITER:
                        state = NEW_FIELD;
                        break;
                    // A row delimiter means we are starting a new row.
                    case CH_CR:
                        if (rowDelimiterCode === CR) {
                            state = NEW_ROW;
                        }
                        else if (rowDelimiterCode === CRLF &&
                            data.charCodeAt(i + 1) === CH_LF) {
                            // If we see an expected \r\n, then increment to the end of the delimiter.
                            i++;
                            state = NEW_ROW;
                        }
                        else {
                            throw `string index ${i} (in row ${nrows}, column ${col}): carriage return found, but not as part of a row delimiter C ${data.charCodeAt(i + 1)}`;
                        }
                        break;
                    case CH_LF:
                        if (rowDelimiterCode === LF) {
                            state = NEW_ROW;
                        }
                        else {
                            throw `string index ${i} (in row ${nrows}, column ${col}): line feed found, but row delimiter starts with a carriage return`;
                        }
                        break;
                    // Otherwise, we are starting an unquoted field.
                    default:
                        state = UNQUOTED_FIELD;
                        break;
                }
                break;
            // We are in a quoted field.
            case QUOTED_FIELD:
                // Skip ahead until we see another quote, which either ends the quoted
                // field or starts an escaped quote.
                i = data.indexOf(quote, i);
                if (i < 0) {
                    throw `string index ${i} (in row ${nrows}, column ${col}): mismatched quote`;
                }
                state = QUOTED_FIELD_QUOTE;
                break;
            // We just saw a quote in a quoted field. This could be the end of the
            // field, or it could be a repeated quote (i.e., an escaped quote according
            // to RFC 4180).
            case QUOTED_FIELD_QUOTE:
                switch (char) {
                    // Another quote means we just saw an escaped quote, so we are still in
                    // the quoted field.
                    case CH_QUOTE:
                        state = QUOTED_FIELD;
                        break;
                    // A field or row delimiter means the quoted field just ended and we are
                    // going into a new field or new row.
                    case CH_DELIMITER:
                        state = NEW_FIELD;
                        break;
                    // A row delimiter means we are starting a new row in the next index.
                    case CH_CR:
                        if (rowDelimiterCode === CR) {
                            state = NEW_ROW;
                        }
                        else if (rowDelimiterCode === CRLF &&
                            data.charCodeAt(i + 1) === CH_LF) {
                            // If we see an expected \r\n, then increment to the end of the delimiter.
                            i++;
                            state = NEW_ROW;
                        }
                        else {
                            throw `string index ${i} (in row ${nrows}, column ${col}): carriage return found, but not as part of a row delimiter C ${data.charCodeAt(i + 1)}`;
                        }
                        break;
                    case CH_LF:
                        if (rowDelimiterCode === LF) {
                            state = NEW_ROW;
                        }
                        else {
                            throw `string index ${i} (in row ${nrows}, column ${col}): line feed found, but row delimiter starts with a carriage return`;
                        }
                        break;
                    default:
                        throw `string index ${i} (in row ${nrows}, column ${col}): quote in escaped field not followed by quote, delimiter, or row delimiter`;
                }
                break;
            // We are in an unquoted field, so the only thing we look for is the next
            // row or field delimiter.
            case UNQUOTED_FIELD:
                // Skip ahead to either the next field delimiter or possible start of a
                // row delimiter (CR or LF).
                while (i < endIndex) {
                    char = data.charCodeAt(i);
                    if (char === CH_DELIMITER || char === CH_LF || char === CH_CR) {
                        break;
                    }
                    i++;
                }
                // Process the character we're seeing in an unquoted field.
                switch (char) {
                    // A field delimiter means we are starting a new field.
                    case CH_DELIMITER:
                        state = NEW_FIELD;
                        break;
                    // A row delimiter means we are starting a new row in the next index.
                    case CH_CR:
                        if (rowDelimiterCode === CR) {
                            state = NEW_ROW;
                        }
                        else if (rowDelimiterCode === CRLF &&
                            data.charCodeAt(i + 1) === CH_LF) {
                            // If we see an expected \r\n, then increment to the end of the delimiter.
                            i++;
                            state = NEW_ROW;
                        }
                        else {
                            throw `string index ${i} (in row ${nrows}, column ${col}): carriage return found, but not as part of a row delimiter C ${data.charCodeAt(i + 1)}`;
                        }
                        break;
                    case CH_LF:
                        if (rowDelimiterCode === LF) {
                            state = NEW_ROW;
                        }
                        else {
                            throw `string index ${i} (in row ${nrows}, column ${col}): line feed found, but row delimiter starts with a carriage return`;
                        }
                        break;
                    // Otherwise, we continue on in the unquoted field.
                    default:
                        continue;
                }
                break;
            // We should never reach this point since the parser state is handled above,
            // so throw an error if we do.
            default:
                throw `string index ${i} (in row ${nrows}, column ${col}): state not recognized`;
        }
        // Increment i to the next character index
        i++;
        // Update return values based on state.
        switch (state) {
            case NEW_ROW:
                nrows++;
                // If ncols is undefined, set it to the number of columns in this row (first row implied).
                if (ncols === undefined) {
                    if (nrows !== 1) {
                        throw new Error('Error parsing default number of columns');
                    }
                    ncols = col;
                }
                // Pad or truncate the column offsets in the previous row if we are
                // returning them.
                if (columnOffsets === true) {
                    if (col < ncols) {
                        // We didn't have enough columns, so add some more column offsets that
                        // point to just before the row delimiter we just saw.
                        for (; col < ncols; col++) {
                            offsets.push(i - rowDelimiterLength);
                        }
                    }
                    else if (col > ncols) {
                        // We had too many columns, so truncate them.
                        offsets.length = offsets.length - (col - ncols);
                    }
                }
                // Shortcut return if nrows reaches the maximum rows we are to parse.
                if (nrows === maxRows) {
                    return { nrows, ncols: columnOffsets ? ncols : 0, offsets };
                }
                break;
            case NEW_FIELD:
                // If we are returning column offsets, log the current index.
                if (columnOffsets === true) {
                    offsets.push(i);
                }
                // Update the column counter.
                col++;
                break;
            default:
                break;
        }
    }
    // If we finished parsing and we are *not* in the NEW_ROW state, then do the
    // column padding/truncation for the last row. Also make sure ncols is
    // defined.
    if (state !== NEW_ROW) {
        nrows++;
        if (columnOffsets === true) {
            // If ncols is *still* undefined, then we only parsed one row and didn't
            // have a newline, so set it to the number of columns we found.
            if (ncols === undefined) {
                ncols = col;
            }
            if (col < ncols) {
                // We didn't have enough columns, so add some more column offsets that
                // point to just before the row delimiter we just saw.
                for (; col < ncols; col++) {
                    offsets.push(i - (rowDelimiterLength - 1));
                }
            }
            else if (col > ncols) {
                // We had too many columns, so truncate them.
                offsets.length = offsets.length - (col - ncols);
            }
        }
    }
    return { nrows, ncols: columnOffsets ? ncols !== null && ncols !== void 0 ? ncols : 0 : 0, offsets };
}
/**
 * Parse delimiter-separated data where no delimiter is quoted.
 *
 * @param options: The parser options
 * @returns An object giving the offsets for the rows or columns parsed.
 *
 * #### Notes
 * This function is an optimized parser for cases where there are no field or
 * row delimiters in quotes. Note that the data can have quotes, but they are
 * not interpreted in any special way. This implementation is based on [RFC
 * 4180](https://tools.ietf.org/html/rfc4180), but disregards quotes.
 */
function parseDSVNoQuotes(options) {
    // Set option defaults.
    const { data, columnOffsets, delimiter = ',', rowDelimiter = '\r\n', startIndex = 0, maxRows = 0xffffffff } = options;
    // ncols will be set automatically if it is undefined.
    let ncols = options.ncols;
    // Set up our return variables.
    const offsets = [];
    let nrows = 0;
    // Set up various state variables.
    const rowDelimiterLength = rowDelimiter.length;
    let currRow = startIndex;
    const len = data.length;
    let nextRow;
    let col;
    let rowString;
    let colIndex;
    // The end of the current row.
    let rowEnd;
    // Start parsing at the start index.
    nextRow = startIndex;
    // Loop through rows until we run out of data or we've reached maxRows.
    while (nextRow !== -1 && nrows < maxRows && currRow < len) {
        // Store the offset for the beginning of the row and increment the rows.
        offsets.push(currRow);
        nrows++;
        // Find the next row delimiter.
        nextRow = data.indexOf(rowDelimiter, currRow);
        // If the next row delimiter is not found, set the end of the row to the
        // end of the data string.
        rowEnd = nextRow === -1 ? len : nextRow;
        // If we are returning column offsets, push them onto the array.
        if (columnOffsets === true) {
            // Find the next field delimiter. We slice the current row out so that
            // the indexOf will stop at the end of the row. It may possibly be faster
            // to just use a loop to check each character.
            col = 1;
            rowString = data.slice(currRow, rowEnd);
            colIndex = rowString.indexOf(delimiter);
            if (ncols === undefined) {
                // If we don't know how many columns we need, loop through and find all
                // of the field delimiters in this row.
                while (colIndex !== -1) {
                    offsets.push(currRow + colIndex + 1);
                    col++;
                    colIndex = rowString.indexOf(delimiter, colIndex + 1);
                }
                // Set ncols to the number of fields we found.
                ncols = col;
            }
            else {
                // If we know the number of columns we expect, find the field delimiters
                // up to that many columns.
                while (colIndex !== -1 && col < ncols) {
                    offsets.push(currRow + colIndex + 1);
                    col++;
                    colIndex = rowString.indexOf(delimiter, colIndex + 1);
                }
                // If we didn't reach the number of columns we expected, pad the offsets
                // with the offset just before the row delimiter.
                while (col < ncols) {
                    offsets.push(rowEnd);
                    col++;
                }
            }
        }
        // Skip past the row delimiter at the end of the row.
        currRow = rowEnd + rowDelimiterLength;
    }
    return { nrows, ncols: columnOffsets ? ncols !== null && ncols !== void 0 ? ncols : 0 : 0, offsets };
}


/***/ }),

/***/ "../../packages/csvviewer/lib/toolbar.js":
/*!***********************************************!*\
  !*** ../../packages/csvviewer/lib/toolbar.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CSVDelimiter": () => (/* binding */ CSVDelimiter)
/* harmony export */ });
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_4__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.





/**
 * The class name added to a csv toolbar widget.
 */
const CSV_DELIMITER_CLASS = 'jp-CSVDelimiter';
const CSV_DELIMITER_LABEL_CLASS = 'jp-CSVDelimiter-label';
/**
 * The class name added to a csv toolbar's dropdown element.
 */
const CSV_DELIMITER_DROPDOWN_CLASS = 'jp-CSVDelimiter-dropdown';
/**
 * A widget for selecting a delimiter.
 */
class CSVDelimiter extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_4__.Widget {
    /**
     * Construct a new csv table widget.
     */
    constructor(options) {
        super({
            node: Private.createNode(options.widget.delimiter, options.translator)
        });
        this._delimiterChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal(this);
        this._widget = options.widget;
        this.addClass(CSV_DELIMITER_CLASS);
    }
    /**
     * A signal emitted when the delimiter selection has changed.
     *
     * @deprecated since v3.2
     * This is dead code now.
     */
    get delimiterChanged() {
        return this._delimiterChanged;
    }
    /**
     * The delimiter dropdown menu.
     */
    get selectNode() {
        return this.node.getElementsByTagName('select')[0];
    }
    /**
     * Handle the DOM events for the widget.
     *
     * @param event - The DOM event sent to the widget.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the dock panel's node. It should
     * not be called directly by user code.
     */
    handleEvent(event) {
        switch (event.type) {
            case 'change':
                this._delimiterChanged.emit(this.selectNode.value);
                this._widget.delimiter = this.selectNode.value;
                break;
            default:
                break;
        }
    }
    /**
     * Handle `after-attach` messages for the widget.
     */
    onAfterAttach(msg) {
        this.selectNode.addEventListener('change', this);
    }
    /**
     * Handle `before-detach` messages for the widget.
     */
    onBeforeDetach(msg) {
        this.selectNode.removeEventListener('change', this);
    }
}
/**
 * A namespace for private toolbar methods.
 */
var Private;
(function (Private) {
    /**
     * Create the node for the delimiter switcher.
     */
    function createNode(selected, translator) {
        translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator;
        const trans = translator === null || translator === void 0 ? void 0 : translator.load('jupyterlab');
        // The supported parsing delimiters and labels.
        const delimiters = [
            [',', ','],
            [';', ';'],
            ['\t', trans.__('tab')],
            ['|', trans.__('pipe')],
            ['#', trans.__('hash')]
        ];
        const div = document.createElement('div');
        const label = document.createElement('span');
        const select = document.createElement('select');
        label.textContent = trans.__('Delimiter: ');
        label.className = CSV_DELIMITER_LABEL_CLASS;
        (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__.each)(delimiters, ([delimiter, label]) => {
            const option = document.createElement('option');
            option.value = delimiter;
            option.textContent = label;
            if (delimiter === selected) {
                option.selected = true;
            }
            select.appendChild(option);
        });
        div.appendChild(label);
        const node = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.Styling.wrapSelect(select);
        node.classList.add(CSV_DELIMITER_DROPDOWN_CLASS);
        div.appendChild(node);
        return div;
    }
    Private.createNode = createNode;
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/csvviewer/lib/widget.js":
/*!**********************************************!*\
  !*** ../../packages/csvviewer/lib/widget.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CSVDocumentWidget": () => (/* binding */ CSVDocumentWidget),
/* harmony export */   "CSVViewer": () => (/* binding */ CSVViewer),
/* harmony export */   "CSVViewerFactory": () => (/* binding */ CSVViewerFactory),
/* harmony export */   "GridSearchService": () => (/* binding */ GridSearchService),
/* harmony export */   "TSVViewerFactory": () => (/* binding */ TSVViewerFactory),
/* harmony export */   "TextRenderConfig": () => (/* binding */ TextRenderConfig)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/docregistry */ "webpack/sharing/consume/default/@jupyterlab/docregistry/@jupyterlab/docregistry");
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_datagrid__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/datagrid */ "webpack/sharing/consume/default/@lumino/datagrid/@lumino/datagrid");
/* harmony import */ var _lumino_datagrid__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_datagrid__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _model__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./model */ "../../packages/csvviewer/lib/model.js");
/* harmony import */ var _toolbar__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./toolbar */ "../../packages/csvviewer/lib/toolbar.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
var __rest = (undefined && undefined.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};








/**
 * The class name added to a CSV viewer.
 */
const CSV_CLASS = 'jp-CSVViewer';
/**
 * The class name added to a CSV viewer datagrid.
 */
const CSV_GRID_CLASS = 'jp-CSVViewer-grid';
/**
 * The timeout to wait for change activity to have ceased before rendering.
 */
const RENDER_TIMEOUT = 1000;
/**
 * Configuration for cells textrenderer.
 */
class TextRenderConfig {
}
/**
 * Search service remembers the search state and the location of the last
 * match, for incremental searching.
 * Search service is also responsible of providing a cell renderer function
 * to set the background color of cells matching the search text.
 */
class GridSearchService {
    constructor(grid) {
        this._looping = true;
        this._changed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__.Signal(this);
        this._grid = grid;
        this._query = null;
        this._row = 0;
        this._column = -1;
    }
    /**
     * A signal fired when the grid changes.
     */
    get changed() {
        return this._changed;
    }
    /**
     * Returns a cellrenderer config function to render each cell background.
     * If cell match, background is matchBackgroundColor, if it's the current
     * match, background is currentMatchBackgroundColor.
     */
    cellBackgroundColorRendererFunc(config) {
        return ({ value, row, column }) => {
            if (this._query) {
                if (value.match(this._query)) {
                    if (this._row === row && this._column === column) {
                        return config.currentMatchBackgroundColor;
                    }
                    return config.matchBackgroundColor;
                }
            }
            return '';
        };
    }
    /**
     * Clear the search.
     */
    clear() {
        this._query = null;
        this._row = 0;
        this._column = -1;
        this._changed.emit(undefined);
    }
    /**
     * incrementally look for searchText.
     */
    find(query, reverse = false) {
        const model = this._grid.dataModel;
        const rowCount = model.rowCount('body');
        const columnCount = model.columnCount('body');
        if (this._query !== query) {
            // reset search
            this._row = 0;
            this._column = -1;
        }
        this._query = query;
        // check if the match is in current viewport
        const minRow = this._grid.scrollY / this._grid.defaultSizes.rowHeight;
        const maxRow = (this._grid.scrollY + this._grid.pageHeight) /
            this._grid.defaultSizes.rowHeight;
        const minColumn = this._grid.scrollX / this._grid.defaultSizes.columnHeaderHeight;
        const maxColumn = (this._grid.scrollX + this._grid.pageWidth) /
            this._grid.defaultSizes.columnHeaderHeight;
        const isInViewport = (row, column) => {
            return (row >= minRow &&
                row <= maxRow &&
                column >= minColumn &&
                column <= maxColumn);
        };
        const increment = reverse ? -1 : 1;
        this._column += increment;
        for (let row = this._row; reverse ? row >= 0 : row < rowCount; row += increment) {
            for (let col = this._column; reverse ? col >= 0 : col < columnCount; col += increment) {
                const cellData = model.data('body', row, col);
                if (cellData.match(query)) {
                    // to update the background of matching cells.
                    // TODO: we only really need to invalidate the previous and current
                    // cell rects, not the entire grid.
                    this._changed.emit(undefined);
                    if (!isInViewport(row, col)) {
                        this._grid.scrollToRow(row);
                    }
                    this._row = row;
                    this._column = col;
                    return true;
                }
            }
            this._column = reverse ? columnCount - 1 : 0;
        }
        // We've finished searching all the way to the limits of the grid. If this
        // is the first time through (looping is true), wrap the indices and search
        // again. Otherwise, give up.
        if (this._looping) {
            this._looping = false;
            this._row = reverse ? 0 : rowCount - 1;
            this._wrapRows(reverse);
            try {
                return this.find(query, reverse);
            }
            finally {
                this._looping = true;
            }
        }
        return false;
    }
    /**
     * Wrap indices if needed to just before the start or just after the end.
     */
    _wrapRows(reverse = false) {
        const model = this._grid.dataModel;
        const rowCount = model.rowCount('body');
        const columnCount = model.columnCount('body');
        if (reverse && this._row <= 0) {
            // if we are at the front, wrap to just past the end.
            this._row = rowCount - 1;
            this._column = columnCount;
        }
        else if (!reverse && this._row >= rowCount - 1) {
            // if we are at the end, wrap to just before the front.
            this._row = 0;
            this._column = -1;
        }
    }
    get query() {
        return this._query;
    }
}
/**
 * A viewer for CSV tables.
 */
class CSVViewer extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.Widget {
    /**
     * Construct a new CSV viewer.
     */
    constructor(options) {
        super();
        this._monitor = null;
        this._delimiter = ',';
        this._revealed = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__.PromiseDelegate();
        this._baseRenderer = null;
        const context = (this._context = options.context);
        const layout = (this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.PanelLayout());
        this.addClass(CSV_CLASS);
        this._grid = new _lumino_datagrid__WEBPACK_IMPORTED_MODULE_3__.DataGrid({
            defaultSizes: {
                rowHeight: 24,
                columnWidth: 144,
                rowHeaderWidth: 64,
                columnHeaderHeight: 36
            }
        });
        this._grid.addClass(CSV_GRID_CLASS);
        this._grid.headerVisibility = 'all';
        this._grid.keyHandler = new _lumino_datagrid__WEBPACK_IMPORTED_MODULE_3__.BasicKeyHandler();
        this._grid.mouseHandler = new _lumino_datagrid__WEBPACK_IMPORTED_MODULE_3__.BasicMouseHandler();
        this._grid.copyConfig = {
            separator: '\t',
            format: _lumino_datagrid__WEBPACK_IMPORTED_MODULE_3__.DataGrid.copyFormatGeneric,
            headers: 'all',
            warningThreshold: 1e6
        };
        layout.addWidget(this._grid);
        this._searchService = new GridSearchService(this._grid);
        this._searchService.changed.connect(this._updateRenderer, this);
        void this._context.ready.then(() => {
            this._updateGrid();
            this._revealed.resolve(undefined);
            // Throttle the rendering rate of the widget.
            this._monitor = new _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.ActivityMonitor({
                signal: context.model.contentChanged,
                timeout: RENDER_TIMEOUT
            });
            this._monitor.activityStopped.connect(this._updateGrid, this);
        });
    }
    /**
     * The CSV widget's context.
     */
    get context() {
        return this._context;
    }
    /**
     * A promise that resolves when the csv viewer is ready to be revealed.
     */
    get revealed() {
        return this._revealed.promise;
    }
    /**
     * The delimiter for the file.
     */
    get delimiter() {
        return this._delimiter;
    }
    set delimiter(value) {
        if (value === this._delimiter) {
            return;
        }
        this._delimiter = value;
        this._updateGrid();
    }
    /**
     * The style used by the data grid.
     */
    get style() {
        return this._grid.style;
    }
    set style(value) {
        this._grid.style = value;
    }
    /**
     * The config used to create text renderer.
     */
    set rendererConfig(rendererConfig) {
        this._baseRenderer = rendererConfig;
        this._updateRenderer();
    }
    /**
     * The search service
     */
    get searchService() {
        return this._searchService;
    }
    /**
     * Dispose of the resources used by the widget.
     */
    dispose() {
        if (this._monitor) {
            this._monitor.dispose();
        }
        super.dispose();
    }
    /**
     * Go to line
     */
    goToLine(lineNumber) {
        this._grid.scrollToRow(lineNumber);
    }
    /**
     * Handle `'activate-request'` messages.
     */
    onActivateRequest(msg) {
        this.node.tabIndex = -1;
        this.node.focus();
    }
    /**
     * Create the model for the grid.
     */
    _updateGrid() {
        const data = this._context.model.toString();
        const delimiter = this._delimiter;
        const oldModel = this._grid.dataModel;
        const dataModel = (this._grid.dataModel = new _model__WEBPACK_IMPORTED_MODULE_6__.DSVModel({
            data,
            delimiter
        }));
        this._grid.selectionModel = new _lumino_datagrid__WEBPACK_IMPORTED_MODULE_3__.BasicSelectionModel({ dataModel });
        if (oldModel) {
            oldModel.dispose();
        }
    }
    /**
     * Update the renderer for the grid.
     */
    _updateRenderer() {
        if (this._baseRenderer === null) {
            return;
        }
        const rendererConfig = this._baseRenderer;
        const renderer = new _lumino_datagrid__WEBPACK_IMPORTED_MODULE_3__.TextRenderer({
            textColor: rendererConfig.textColor,
            horizontalAlignment: rendererConfig.horizontalAlignment,
            backgroundColor: this._searchService.cellBackgroundColorRendererFunc(rendererConfig)
        });
        this._grid.cellRenderers.update({
            body: renderer,
            'column-header': renderer,
            'corner-header': renderer,
            'row-header': renderer
        });
    }
}
/**
 * A document widget for CSV content widgets.
 */
class CSVDocumentWidget extends _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__.DocumentWidget {
    constructor(options) {
        let { content, context, delimiter, reveal } = options, other = __rest(options, ["content", "context", "delimiter", "reveal"]);
        content = content || Private.createContent(context);
        reveal = Promise.all([reveal, content.revealed]);
        super(Object.assign({ content, context, reveal }, other));
        if (delimiter) {
            content.delimiter = delimiter;
        }
    }
    /**
     * Set URI fragment identifier for rows
     */
    setFragment(fragment) {
        const parseFragments = fragment.split('=');
        // TODO: expand to allow columns and cells to be selected
        // reference: https://tools.ietf.org/html/rfc7111#section-3
        if (parseFragments[0] !== '#row') {
            return;
        }
        // multiple rows, separated by semi-colons can be provided, we will just
        // go to the top one
        let topRow = parseFragments[1].split(';')[0];
        // a range of rows can be provided, we will take the first value
        topRow = topRow.split('-')[0];
        // go to that row
        void this.context.ready.then(() => {
            this.content.goToLine(Number(topRow));
        });
    }
}
var Private;
(function (Private) {
    function createContent(context) {
        return new CSVViewer({ context });
    }
    Private.createContent = createContent;
})(Private || (Private = {}));
/**
 * A widget factory for CSV widgets.
 */
class CSVViewerFactory extends _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__.ABCWidgetFactory {
    /**
     * Create a new widget given a context.
     */
    createNewWidget(context) {
        const translator = this.translator;
        return new CSVDocumentWidget({ context, translator });
    }
    /**
     * Default factory for toolbar items to be added after the widget is created.
     */
    defaultToolbarFactory(widget) {
        return [
            {
                name: 'delimiter',
                widget: new _toolbar__WEBPACK_IMPORTED_MODULE_7__.CSVDelimiter({
                    widget: widget.content,
                    translator: this.translator
                })
            }
        ];
    }
}
/**
 * A widget factory for TSV widgets.
 */
class TSVViewerFactory extends CSVViewerFactory {
    /**
     * Create a new widget given a context.
     */
    createNewWidget(context) {
        const delimiter = '\t';
        return new CSVDocumentWidget({
            context,
            delimiter,
            translator: this.translator
        });
    }
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY3N2dmlld2VyX2xpYl9pbmRleF9qcy44NWY5YmM1NzE0N2M2MDUwZTlkYi5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBRXFCO0FBQ0E7QUFDRTtBQUNEOzs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQ1Z6QiwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBRVA7QUFDUDtBQUVpQjtBQUU5RDs7Ozs7Ozs7Ozs7RUFXRTtBQUVGOztHQUVHO0FBQ0gsTUFBTSxPQUFPLEdBQStCO0lBQzFDLE1BQU0sRUFBRSw0Q0FBUTtJQUNoQixRQUFRLEVBQUUsb0RBQWdCO0NBQzNCLENBQUM7QUFFRjs7Ozs7R0FLRztBQUNJLE1BQU0sUUFBUyxTQUFRLHVEQUFTO0lBQ3JDOzs7O09BSUc7SUFDSCxZQUFZLE9BQTBCO1FBQ3BDLEtBQUssRUFBRSxDQUFDO1FBa2xCRixjQUFTLEdBQXVCLENBQUMsQ0FBQztRQUcxQyxvQkFBb0I7UUFDcEI7O1dBRUc7UUFDSyxZQUFPLEdBQWEsRUFBRSxDQUFDO1FBQy9COzs7Ozs7V0FNRztRQUNLLG1CQUFjLEdBQWdCLElBQUksV0FBVyxDQUFDLENBQUMsQ0FBQyxDQUFDO1FBQ3pEOztXQUVHO1FBQ0ssOEJBQXlCLEdBQVcsQ0FBQyxDQUFDO1FBQzlDOztXQUVHO1FBQ0ssaUJBQVksR0FBVyxJQUFJLENBQUM7UUFDcEM7O1dBRUc7UUFDSyxnQkFBVyxHQUFnQixJQUFJLFdBQVcsQ0FBQyxDQUFDLENBQUMsQ0FBQztRQU90RCx5QkFBeUI7UUFDakIsa0JBQWEsR0FBa0IsSUFBSSxDQUFDO1FBQ3BDLG9CQUFlLEdBQVksS0FBSyxDQUFDO1FBQ2pDLGlCQUFZLEdBQVksS0FBSyxDQUFDO1FBQzlCLGdCQUFXLEdBQVksS0FBSyxDQUFDO1FBQzdCLFdBQU0sR0FBRyxJQUFJLDhEQUFlLEVBQVEsQ0FBQztRQXhuQjNDLElBQUksRUFDRixJQUFJLEVBQ0os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QixhQUFhLENBQzNCLE9BQTJEO1FBRTNELE9BQU8sSUFBSSxTQUFTLENBQUMsRUFBRSxPQUFPLEVBQUUsQ0FBQyxDQUFDO0lBQ3BDLENBQUM7SUFKZSxxQkFBYSxnQkFJNUI7QUFDSCxDQUFDLEVBTlMsT0FBTyxLQUFQLE9BQU8sUUFNaEI7QUFFRDs7R0FFRztBQUNJLE1BQU0sZ0JBQWlCLFNBQVEscUVBRXJDO0lBQ0M7O09BRUc7SUFDTyxlQUFlLENBQ3ZCLE9BQWlDO1FBRWpDLE1BQU0sVUFBVSxHQUFHLElBQUksQ0FBQyxVQUFVLENBQUM7UUFDbkMsT0FBTyxJQUFJLGlCQUFpQixDQUFDLEVBQUUsT0FBTyxFQUFFLFVBQVUsRUFBRSxDQUFDLENBQUM7SUFDeEQsQ0FBQztJQUVEOztPQUVHO0lBQ08scUJBQXFCLENBQzdCLE1BQWtDO1FBRWxDLE9BQU87WUFDTDtnQkFDRSxJQUFJLEVBQUUsV0FBVztnQkFDakIsTUFBTSxFQUFFLElBQUksa0RBQVksQ0FBQztvQkFDdkIsTUFBTSxFQUFFLE1BQU0sQ0FBQyxPQUFPO29CQUN0QixVQUFVLEVBQUUsSUFBSSxDQUFDLFVBQVU7aUJBQzVCLENBQUM7YUFDSDtTQUNGLENBQUM7SUFDSixDQUFDO0NBQ0Y7QUFFRDs7R0FFRztBQUNJLE1BQU0sZ0JBQWlCLFNBQVEsZ0JBQWdCO0lBQ3BEOztPQUVHO0lBQ08sZUFBZSxDQUN2QixPQUFpQztRQUVqQyxNQUFNLFNBQVMsR0FBRyxJQUFJLENBQUM7UUFDdkIsT0FBTyxJQUFJLGlCQUFpQixDQUFDO1lBQzNCLE9BQU87WUFDUCxTQUFTO1lBQ1QsVUFBVSxFQUFFLElBQUksQ0FBQyxVQUFVO1NBQzVCLENBQUMsQ0FBQztJQUNMLENBQUM7Q0FDRiIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jc3Z2aWV3ZXIvc3JjL2luZGV4LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jc3Z2aWV3ZXIvc3JjL21vZGVsLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jc3Z2aWV3ZXIvc3JjL3BhcnNlLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jc3Z2aWV3ZXIvc3JjL3Rvb2xiYXIudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NzdnZpZXdlci9zcmMvd2lkZ2V0LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGNzdnZpZXdlclxuICovXG5cbmV4cG9ydCAqIGZyb20gJy4vbW9kZWwnO1xuZXhwb3J0ICogZnJvbSAnLi9wYXJzZSc7XG5leHBvcnQgKiBmcm9tICcuL3Rvb2xiYXInO1xuZXhwb3J0ICogZnJvbSAnLi93aWRnZXQnO1xuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBQcm9taXNlRGVsZWdhdGUgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBEYXRhTW9kZWwgfSBmcm9tICdAbHVtaW5vL2RhdGFncmlkJztcbmltcG9ydCB7IElEaXNwb3NhYmxlIH0gZnJvbSAnQGx1bWluby9kaXNwb3NhYmxlJztcbmltcG9ydCB7IElQYXJzZXIsIHBhcnNlRFNWLCBwYXJzZURTVk5vUXVvdGVzIH0gZnJvbSAnLi9wYXJzZSc7XG5cbi8qXG5Qb3NzaWJsZSBpZGVhcyBmb3IgZnVydGhlciBpbXBsZW1lbnRhdGlvbjpcblxuLSBTaG93IGEgc3Bpbm5lciBvciBzb21ldGhpbmcgdmlzaWJsZSB3aGVuIHdlIGFyZSBkb2luZyBkZWxheWVkIHBhcnNpbmcuXG4tIFRoZSBjYWNoZSByaWdodCBub3cgaGFuZGxlcyBzY3JvbGxpbmcgZG93biBncmVhdCAtIGl0IGdldHMgdGhlIG5leHQgc2V2ZXJhbCBodW5kcmVkIHJvd3MuIEhvd2V2ZXIsIHNjcm9sbGluZyB1cCBjYXVzZXMgbG90cyBvZiBjYWNoZSBtaXNzZXMgLSBlYWNoIG5ldyByb3cgY2F1c2VzIGEgZmx1c2ggb2YgdGhlIGNhY2hlLiBXaGVuIGludmFsaWRhdGluZyBhbiBlbnRpcmUgY2FjaGUsIHdlIHNob3VsZCBwdXQgdGhlIHJlcXVlc3RlZCByb3cgaW4gbWlkZGxlIG9mIHRoZSBjYWNoZSAoYWRqdXN0aW5nIGZvciByb3dzIGF0IHRoZSBiZWdpbm5pbmcgb3IgZW5kKS4gV2hlbiBwb3B1bGF0aW5nIGEgY2FjaGUsIHdlIHNob3VsZCByZXRyaWV2ZSByb3dzIGJvdGggYWJvdmUgYW5kIGJlbG93IHRoZSByZXF1ZXN0ZWQgcm93LlxuLSBXaGVuIHdlIGhhdmUgYSBoZWFkZXIsIGFuZCB3ZSBhcmUgZ3Vlc3NpbmcgdGhlIHBhcnNlciB0byB1c2UsIHRyeSBjaGVja2luZyBqdXN0IHRoZSBwYXJ0IG9mIHRoZSBmaWxlICphZnRlciogdGhlIGhlYWRlciByb3cgZm9yIHF1b3Rlcy4gSSB0aGluayBvZnRlbiBhIGZpcnN0IGhlYWRlciByb3cgaXMgcXVvdGVkLCBidXQgdGhlIHJlc3Qgb2YgdGhlIGZpbGUgaXMgbm90IGFuZCBjYW4gYmUgcGFyc2VkIG11Y2ggZmFzdGVyLlxuLSBhdXRkZXRlY3QgdGhlIGRlbGltaXRlciAobG9vayBmb3IgY29tbWEsIHRhYiwgc2VtaWNvbG9uIGluIGZpcnN0IGxpbmUuIElmIG1vcmUgdGhhbiBvbmUgZm91bmQsIHBhcnNlIGZpcnN0IHJvdyB3aXRoIGNvbW1hLCB0YWIsIHNlbWljb2xvbiBkZWxpbWl0ZXJzLiBPbmUgd2l0aCBtb3N0IGZpZWxkcyB3aW5zKS5cbi0gVG9vbGJhciBidXR0b25zIHRvIGNvbnRyb2wgdGhlIHJvdyBkZWxpbWl0ZXIsIHRoZSBwYXJzaW5nIGVuZ2luZSAocXVvdGVkL25vdCBxdW90ZWQpLCB0aGUgcXVvdGUgY2hhcmFjdGVyLCBldGMuXG4tIEludmVzdGlnYXRlIGluY3JlbWVudGFsIGxvYWRpbmcgc3RyYXRlZ2llcyBpbiB0aGUgcGFyc2VBc3luYyBmdW5jdGlvbi4gSW4gaW5pdGlhbCBpbnZlc3RpZ2F0aW9ucywgc2V0dGluZyB0aGUgY2h1bmsgc2l6ZSB0byAxMDBrIGluIHBhcnNlQXN5bmMgc2VlbXMgY2F1c2UgaW5zdGFiaWxpdHkgd2l0aCBsYXJnZSBmaWxlcyBpbiBDaHJvbWUgKHN1Y2ggYXMgOC1taWxsaW9uIHJvdyBmaWxlcykuIFBlcmhhcHMgdGhpcyBpcyBiZWNhdXNlIHdlIGFyZSByZWN5Y2xpbmcgdGhlIHJvdyBvZmZzZXQgYW5kIGNvbHVtbiBvZmZzZXQgYXJyYXlzIHF1aWNrbHk/IEl0IGRvZXNuJ3Qgc2VlbSB0aGF0IHRoZXJlIGlzIGEgbWVtb3J5IGxlYWsuIE9uIHRoaXMgdGhlb3J5LCBwZXJoYXBzIHdlIGp1c3QgbmVlZCB0byBrZWVwIHRoZSBvZmZzZXRzIGxpc3QgYW4gYWN0dWFsIGxpc3QsIGFuZCBwYXNzIGl0IGludG8gdGhlIHBhcnNpbmcgZnVuY3Rpb24gdG8gZXh0ZW5kIHdpdGhvdXQgY29weWluZywgYW5kIGZpbmFsaXplIGl0IGludG8gYW4gYXJyYXkgYnVmZmVyIG9ubHkgd2hlbiB3ZSBhcmUgZG9uZSBwYXJzaW5nLiBPciBwZXJoYXBzIHdlIGRvdWJsZSB0aGUgc2l6ZSBvZiB0aGUgYXJyYXkgYnVmZmVyIGVhY2ggdGltZSwgd2hpY2ggbWF5IGJlIHdhc3RlZnVsLCBidXQgYXQgdGhlIGVuZCB3ZSB0cmltIGl0IGRvd24gaWYgaXQncyB0b28gd2FzdGVmdWwgKHBlcmhhcHMgd2UgaGF2ZSBvdXIgb3duIG9iamVjdCB0aGF0IGlzIGJhY2tlZCBieSBhbiBhcnJheSBidWZmZXIsIGJ1dCBoYXMgYSBwdXNoIG1ldGhvZCB0aGF0IHdpbGwgYXV0b21hdGljYWxseSBkb3VibGUgdGhlIGFycmF5IGJ1ZmZlciBzaXplIGFzIG5lZWRlZCwgYW5kIGEgdHJpbSBmdW5jdGlvbiB0byBmaW5hbGl6ZSB0aGUgYXJyYXkgdG8gZXhhY3RseSB0aGUgc2l6ZSBuZWVkZWQpPyBPciBwZXJoYXBzIHdlIGRvbid0IHVzZSBhcnJheSBidWZmZXJzIGF0IGFsbCAtIGNvbXBhcmUgdGhlIG1lbW9yeSBjb3N0IGFuZCBzcGVlZCBvZiBrZWVwaW5nIHRoZSBvZmZzZXRzIGFzIGxpc3RzIGluc3RlYWQgb2YgbWVtb3J5IGJ1ZmZlcnMuXG4tIEludmVzdGlnYXRlIGEgdGltZS1iYXNlZCBpbmNyZW1lbnRhbCBwYXJzaW5nIHN0cmF0ZWd5LCByYXRoZXIgdGhhbiBhIHJvdy1iYXNlZCBvbmUuIFRoZSBwYXJzZXIgY291bGQgdGFrZSBhIG1heGltdW0gdGltZSB0byBwYXJzZSAoc2F5IDMwMG1zKSwgYW5kIHdpbGwgcGFyc2UgdXAgdG8gdGhhdCBkdXJhdGlvbiwgaW4gd2hpY2ggY2FzZSB0aGUgcGFyc2VyIHByb2JhYmx5IGFsc28gbmVlZHMgYSB3YXkgdG8gbm90aWZ5IHdoZW4gaXQgaGFzIHJlYWNoZWQgdGhlIGVuZCBvZiBhIGZpbGUuXG4tIEZvciB2ZXJ5IGxhcmdlIGZpbGVzLCB3aGVyZSB3ZSBhcmUgb25seSBzdG9yaW5nIGEgc21hbGwgY2FjaGUsIHNjcm9sbGluZyBpcyB2ZXJ5IGxhZ2d5IGluIFNhZmFyaS4gSXQgd291bGQgYmUgZ29vZCB0byBwcm9maWxlIGl0LlxuKi9cblxuLyoqXG4gKiBQb3NzaWJsZSBkZWxpbWl0ZXItc2VwYXJhdGVkIGRhdGEgcGFyc2Vycy5cbiAqL1xuY29uc3QgUEFSU0VSUzogeyBba2V5OiBzdHJpbmddOiBJUGFyc2VyIH0gPSB7XG4gIHF1b3RlczogcGFyc2VEU1YsXG4gIG5vcXVvdGVzOiBwYXJzZURTVk5vUXVvdGVzXG59O1xuXG4vKipcbiAqIEEgZGF0YSBtb2RlbCBpbXBsZW1lbnRhdGlvbiBmb3IgaW4tbWVtb3J5IGRlbGltaXRlci1zZXBhcmF0ZWQgZGF0YS5cbiAqXG4gKiAjIyMjIE5vdGVzXG4gKiBUaGlzIG1vZGVsIGhhbmRsZXMgZGF0YSB3aXRoIHVwIHRvIDIqKjMyIGNoYXJhY3RlcnMuXG4gKi9cbmV4cG9ydCBjbGFzcyBEU1ZNb2RlbCBleHRlbmRzIERhdGFNb2RlbCBpbXBsZW1lbnRzIElEaXNwb3NhYmxlIHtcbiAgLyoqXG4gICAqIENyZWF0ZSBhIGRhdGEgbW9kZWwgd2l0aCBzdGF0aWMgQ1NWIGRhdGEuXG4gICAqXG4gICAqIEBwYXJhbSBvcHRpb25zIC0gVGhlIG9wdGlvbnMgZm9yIGluaXRpYWxpemluZyB0aGUgZGF0YSBtb2RlbC5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IERTVk1vZGVsLklPcHRpb25zKSB7XG4gICAgc3VwZXIoKTtcbiAgICBsZXQge1xuICAgICAgZGF0YSxcbiAgICAgIGRlbGltaXRlciA9ICcsJyxcbiAgICAgIHJvd0RlbGltaXRlciA9IHVuZGVmaW5lZCxcbiAgICAgIHF1b3RlID0gJ1wiJyxcbiAgICAgIHF1b3RlUGFyc2VyID0gdW5kZWZpbmVkLFxuICAgICAgaGVhZGVyID0gdHJ1ZSxcbiAgICAgIGluaXRpYWxSb3dzID0gNTAwXG4gICAgfSA9IG9wdGlvbnM7XG4gICAgdGhpcy5fcmF3RGF0YSA9IGRhdGE7XG4gICAgdGhpcy5fZGVsaW1pdGVyID0gZGVsaW1pdGVyO1xuICAgIHRoaXMuX3F1b3RlID0gcXVvdGU7XG4gICAgdGhpcy5fcXVvdGVFc2NhcGVkID0gbmV3IFJlZ0V4cChxdW90ZSArIHF1b3RlLCAnZycpO1xuICAgIHRoaXMuX2luaXRpYWxSb3dzID0gaW5pdGlhbFJvd3M7XG5cbiAgICAvLyBHdWVzcyB0aGUgcm93IGRlbGltaXRlciBpZiBpdCB3YXMgbm90IHN1cHBsaWVkLiBUaGlzIHdpbGwgYmUgZm9vbGVkIGlmIGFcbiAgICAvLyBkaWZmZXJlbnQgbGluZSBkZWxpbWl0ZXIgcG9zc2liaWxpdHkgYXBwZWFycyBpbiB0aGUgZmlyc3Qgcm93LlxuICAgIGlmIChyb3dEZWxpbWl0ZXIgPT09IHVuZGVmaW5lZCkge1xuICAgICAgY29uc3QgaSA9IGRhdGEuc2xpY2UoMCwgNTAwMCkuaW5kZXhPZignXFxyJyk7XG4gICAgICBpZiAoaSA9PT0gLTEpIHtcbiAgICAgICAgcm93RGVsaW1pdGVyID0gJ1xcbic7XG4gICAgICB9IGVsc2UgaWYgKGRhdGFbaSArIDFdID09PSAnXFxuJykge1xuICAgICAgICByb3dEZWxpbWl0ZXIgPSAnXFxyXFxuJztcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIHJvd0RlbGltaXRlciA9ICdcXHInO1xuICAgICAgfVxuICAgIH1cbiAgICB0aGlzLl9yb3dEZWxpbWl0ZXIgPSByb3dEZWxpbWl0ZXI7XG5cbiAgICBpZiAocXVvdGVQYXJzZXIgPT09IHVuZGVmaW5lZCkge1xuICAgICAgLy8gQ2hlY2sgZm9yIHRoZSBleGlzdGVuY2Ugb2YgcXVvdGVzIGlmIHRoZSBxdW90ZVBhcnNlciBpcyBub3Qgc2V0LlxuICAgICAgcXVvdGVQYXJzZXIgPSBkYXRhLmluZGV4T2YocXVvdGUpID49IDA7XG4gICAgfVxuICAgIHRoaXMuX3BhcnNlciA9IHF1b3RlUGFyc2VyID8gJ3F1b3RlcycgOiAnbm9xdW90ZXMnO1xuXG4gICAgLy8gUGFyc2UgdGhlIGRhdGEuXG4gICAgdGhpcy5wYXJzZUFzeW5jKCk7XG5cbiAgICAvLyBDYWNoZSB0aGUgaGVhZGVyIHJvdy5cbiAgICBpZiAoaGVhZGVyID09PSB0cnVlICYmIHRoaXMuX2NvbHVtbkNvdW50ISA+IDApIHtcbiAgICAgIGNvbnN0IGggPSBbXTtcbiAgICAgIGZvciAobGV0IGMgPSAwOyBjIDwgdGhpcy5fY29sdW1uQ291bnQhOyBjKyspIHtcbiAgICAgICAgaC5wdXNoKHRoaXMuX2dldEZpZWxkKDAsIGMpKTtcbiAgICAgIH1cbiAgICAgIHRoaXMuX2hlYWRlciA9IGg7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFdoZXRoZXIgdGhpcyBtb2RlbCBoYXMgYmVlbiBkaXNwb3NlZC5cbiAgICovXG4gIGdldCBpc0Rpc3Bvc2VkKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiB0aGlzLl9pc0Rpc3Bvc2VkO1xuICB9XG5cbiAgLyoqXG4gICAqIEEgcHJvbWlzZSB0aGF0IHJlc29sdmVzIHdoZW4gdGhlIG1vZGVsIGhhcyBwYXJzZWQgYWxsIG9mIGl0cyBkYXRhLlxuICAgKi9cbiAgZ2V0IHJlYWR5KCk6IFByb21pc2U8dm9pZD4ge1xuICAgIHJldHVybiB0aGlzLl9yZWFkeS5wcm9taXNlO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBzdHJpbmcgcmVwcmVzZW50YXRpb24gb2YgdGhlIGRhdGEuXG4gICAqL1xuICBnZXQgcmF3RGF0YSgpOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLl9yYXdEYXRhO1xuICB9XG4gIHNldCByYXdEYXRhKHZhbHVlOiBzdHJpbmcpIHtcbiAgICB0aGlzLl9yYXdEYXRhID0gdmFsdWU7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGluaXRpYWwgY2h1bmsgb2Ygcm93cyB0byBwYXJzZS5cbiAgICovXG4gIGdldCBpbml0aWFsUm93cygpOiBudW1iZXIge1xuICAgIHJldHVybiB0aGlzLl9pbml0aWFsUm93cztcbiAgfVxuICBzZXQgaW5pdGlhbFJvd3ModmFsdWU6IG51bWJlcikge1xuICAgIHRoaXMuX2luaXRpYWxSb3dzID0gdmFsdWU7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGhlYWRlciBzdHJpbmdzLlxuICAgKi9cbiAgZ2V0IGhlYWRlcigpOiBzdHJpbmdbXSB7XG4gICAgcmV0dXJuIHRoaXMuX2hlYWRlcjtcbiAgfVxuICBzZXQgaGVhZGVyKHZhbHVlOiBzdHJpbmdbXSkge1xuICAgIHRoaXMuX2hlYWRlciA9IHZhbHVlO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBkZWxpbWl0ZXIgYmV0d2VlbiBlbnRyaWVzIG9uIHRoZSBzYW1lIHJvdy5cbiAgICovXG4gIGdldCBkZWxpbWl0ZXIoKTogc3RyaW5nIHtcbiAgICByZXR1cm4gdGhpcy5fZGVsaW1pdGVyO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBkZWxpbWl0ZXIgYmV0d2VlbiByb3dzLlxuICAgKi9cbiAgZ2V0IHJvd0RlbGltaXRlcigpOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLl9yb3dEZWxpbWl0ZXI7XG4gIH1cblxuICAvKipcbiAgICogQSBib29sZWFuIGRldGVybWluZWQgYnkgd2hldGhlciBwYXJzaW5nIGhhcyBjb21wbGV0ZWQuXG4gICAqL1xuICBnZXQgZG9uZVBhcnNpbmcoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuX2RvbmVQYXJzaW5nO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgcm93IGNvdW50IGZvciBhIHJlZ2lvbiBpbiB0aGUgZGF0YSBtb2RlbC5cbiAgICpcbiAgICogQHBhcmFtIHJlZ2lvbiAtIFRoZSByb3cgcmVnaW9uIG9mIGludGVyZXN0LlxuICAgKlxuICAgKiBAcmV0dXJucyAtIFRoZSByb3cgY291bnQgZm9yIHRoZSByZWdpb24uXG4gICAqL1xuICByb3dDb3VudChyZWdpb246IERhdGFNb2RlbC5Sb3dSZWdpb24pOiBudW1iZXIge1xuICAgIGlmIChyZWdpb24gPT09ICdib2R5Jykge1xuICAgICAgaWYgKHRoaXMuX2hlYWRlci5sZW5ndGggPT09IDApIHtcbiAgICAgICAgcmV0dXJuIHRoaXMuX3Jvd0NvdW50ITtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIHJldHVybiB0aGlzLl9yb3dDb3VudCEgLSAxO1xuICAgICAgfVxuICAgIH1cbiAgICByZXR1cm4gMTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgdGhlIGNvbHVtbiBjb3VudCBmb3IgYSByZWdpb24gaW4gdGhlIGRhdGEgbW9kZWwuXG4gICAqXG4gICAqIEBwYXJhbSByZWdpb24gLSBUaGUgY29sdW1uIHJlZ2lvbiBvZiBpbnRlcmVzdC5cbiAgICpcbiAgICogQHJldHVybnMgLSBUaGUgY29sdW1uIGNvdW50IGZvciB0aGUgcmVnaW9uLlxuICAgKi9cbiAgY29sdW1uQ291bnQocmVnaW9uOiBEYXRhTW9kZWwuQ29sdW1uUmVnaW9uKTogbnVtYmVyIHtcbiAgICBpZiAocmVnaW9uID09PSAnYm9keScpIHtcbiAgICAgIHJldHVybiB0aGlzLl9jb2x1bW5Db3VudCE7XG4gICAgfVxuICAgIHJldHVybiAxO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgZGF0YSB2YWx1ZSBmb3IgYSBjZWxsIGluIHRoZSBkYXRhIG1vZGVsLlxuICAgKlxuICAgKiBAcGFyYW0gcmVnaW9uIC0gVGhlIGNlbGwgcmVnaW9uIG9mIGludGVyZXN0LlxuICAgKlxuICAgKiBAcGFyYW0gcm93IC0gVGhlIHJvdyBpbmRleCBvZiB0aGUgY2VsbCBvZiBpbnRlcmVzdC5cbiAgICpcbiAgICogQHBhcmFtIGNvbHVtbiAtIFRoZSBjb2x1bW4gaW5kZXggb2YgdGhlIGNlbGwgb2YgaW50ZXJlc3QuXG4gICAqXG4gICAqIEBwYXJhbSByZXR1cm5zIC0gVGhlIGRhdGEgdmFsdWUgZm9yIHRoZSBzcGVjaWZpZWQgY2VsbC5cbiAgICovXG4gIGRhdGEocmVnaW9uOiBEYXRhTW9kZWwuQ2VsbFJlZ2lvbiwgcm93OiBudW1iZXIsIGNvbHVtbjogbnVtYmVyKTogc3RyaW5nIHtcbiAgICBsZXQgdmFsdWU6IHN0cmluZztcblxuICAgIC8vIExvb2sgdXAgdGhlIGZpZWxkIGFuZCB2YWx1ZSBmb3IgdGhlIHJlZ2lvbi5cbiAgICBzd2l0Y2ggKHJlZ2lvbikge1xuICAgICAgY2FzZSAnYm9keSc6XG4gICAgICAgIGlmICh0aGlzLl9oZWFkZXIubGVuZ3RoID09PSAwKSB7XG4gICAgICAgICAgdmFsdWUgPSB0aGlzLl9nZXRGaWVsZChyb3csIGNvbHVtbik7XG4gICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgdmFsdWUgPSB0aGlzLl9nZXRGaWVsZChyb3cgKyAxLCBjb2x1bW4pO1xuICAgICAgICB9XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnY29sdW1uLWhlYWRlcic6XG4gICAgICAgIGlmICh0aGlzLl9oZWFkZXIubGVuZ3RoID09PSAwKSB7XG4gICAgICAgICAgdmFsdWUgPSAoY29sdW1uICsgMSkudG9TdHJpbmcoKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICB2YWx1ZSA9IHRoaXMuX2hlYWRlcltjb2x1bW5dO1xuICAgICAgICB9XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAncm93LWhlYWRlcic6XG4gICAgICAgIHZhbHVlID0gKHJvdyArIDEpLnRvU3RyaW5nKCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnY29ybmVyLWhlYWRlcic6XG4gICAgICAgIHZhbHVlID0gJyc7XG4gICAgICAgIGJyZWFrO1xuICAgICAgZGVmYXVsdDpcbiAgICAgICAgdGhyb3cgJ3VucmVhY2hhYmxlJztcbiAgICB9XG5cbiAgICAvLyBSZXR1cm4gdGhlIGZpbmFsIHZhbHVlLlxuICAgIHJldHVybiB2YWx1ZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIHRoZSByZXNvdXJjZXMgaGVsZCBieSB0aGlzIG1vZGVsLlxuICAgKi9cbiAgZGlzcG9zZSgpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5faXNEaXNwb3NlZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIHRoaXMuX2lzRGlzcG9zZWQgPSB0cnVlO1xuXG4gICAgdGhpcy5fY29sdW1uQ291bnQgPSB1bmRlZmluZWQ7XG4gICAgdGhpcy5fcm93Q291bnQgPSB1bmRlZmluZWQ7XG4gICAgdGhpcy5fcm93T2Zmc2V0cyA9IG51bGwhO1xuICAgIHRoaXMuX2NvbHVtbk9mZnNldHMgPSBudWxsITtcbiAgICB0aGlzLl9yYXdEYXRhID0gbnVsbCE7XG5cbiAgICAvLyBDbGVhciBvdXQgc3RhdGUgYXNzb2NpYXRlZCB3aXRoIHRoZSBhc3luY2hyb25vdXMgcGFyc2luZy5cbiAgICBpZiAodGhpcy5fZG9uZVBhcnNpbmcgPT09IGZhbHNlKSB7XG4gICAgICAvLyBFeHBsaWNpdGx5IGNhdGNoIHRoaXMgcmVqZWN0aW9uIGF0IGxlYXN0IG9uY2Ugc28gYW4gZXJyb3IgaXMgbm90IHRocm93blxuICAgICAgLy8gdG8gdGhlIGNvbnNvbGUuXG4gICAgICB0aGlzLnJlYWR5LmNhdGNoKCgpID0+IHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfSk7XG4gICAgICB0aGlzLl9yZWFkeS5yZWplY3QodW5kZWZpbmVkKTtcbiAgICB9XG4gICAgaWYgKHRoaXMuX2RlbGF5ZWRQYXJzZSAhPT0gbnVsbCkge1xuICAgICAgd2luZG93LmNsZWFyVGltZW91dCh0aGlzLl9kZWxheWVkUGFyc2UpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgdGhlIGluZGV4IGluIHRoZSBkYXRhIHN0cmluZyBmb3IgdGhlIGZpcnN0IGNoYXJhY3RlciBvZiBhIHJvdyBhbmRcbiAgICogY29sdW1uLlxuICAgKlxuICAgKiBAcGFyYW0gcm93IC0gVGhlIHJvdyBvZiB0aGUgZGF0YSBpdGVtLlxuICAgKiBAcGFyYW0gY29sdW1uIC0gVGhlIGNvbHVtbiBvZiB0aGUgZGF0YSBpdGVtLlxuICAgKiBAcmV0dXJucyAtIFRoZSBpbmRleCBpbnRvIHRoZSBkYXRhIHN0cmluZyB3aGVyZSB0aGUgZGF0YSBpdGVtIHN0YXJ0cy5cbiAgICovXG4gIGdldE9mZnNldEluZGV4KHJvdzogbnVtYmVyLCBjb2x1bW46IG51bWJlcik6IG51bWJlciB7XG4gICAgLy8gRGVjbGFyZSBsb2NhbCB2YXJpYWJsZXMuXG4gICAgY29uc3QgbmNvbHMgPSB0aGlzLl9jb2x1bW5Db3VudCE7XG5cbiAgICAvLyBDaGVjayB0byBzZWUgaWYgcm93ICpzaG91bGQqIGJlIGluIHRoZSBjYWNoZSwgYmFzZWQgb24gdGhlIGNhY2hlIHNpemUuXG4gICAgbGV0IHJvd0luZGV4ID0gKHJvdyAtIHRoaXMuX2NvbHVtbk9mZnNldHNTdGFydGluZ1JvdykgKiBuY29scztcbiAgICBpZiAocm93SW5kZXggPCAwIHx8IHJvd0luZGV4ID4gdGhpcy5fY29sdW1uT2Zmc2V0cy5sZW5ndGgpIHtcbiAgICAgIC8vIFJvdyBpc24ndCBpbiB0aGUgY2FjaGUsIHNvIHdlIGludmFsaWRhdGUgdGhlIGVudGlyZSBjYWNoZSBhbmQgc2V0IHVwXG4gICAgICAvLyB0aGUgY2FjaGUgdG8gaG9sZCB0aGUgcmVxdWVzdGVkIHJvdy5cbiAgICAgIHRoaXMuX2NvbHVtbk9mZnNldHMuZmlsbCgweGZmZmZmZmZmKTtcbiAgICAgIHRoaXMuX2NvbHVtbk9mZnNldHNTdGFydGluZ1JvdyA9IHJvdztcbiAgICAgIHJvd0luZGV4ID0gMDtcbiAgICB9XG5cbiAgICAvLyBDaGVjayB0byBzZWUgaWYgd2UgbmVlZCB0byBmZXRjaCB0aGUgcm93IGRhdGEgaW50byB0aGUgY2FjaGUuXG4gICAgaWYgKHRoaXMuX2NvbHVtbk9mZnNldHNbcm93SW5kZXhdID09PSAweGZmZmZmZmZmKSB7XG4gICAgICAvLyBGaWd1cmUgb3V0IGhvdyBtYW55IHJvd3MgYmVsb3cgdXMgYWxzbyBuZWVkIHRvIGJlIGZldGNoZWQuXG4gICAgICBsZXQgbWF4Um93cyA9IDE7XG4gICAgICB3aGlsZSAoXG4gICAgICAgIG1heFJvd3MgPD0gdGhpcy5fbWF4Q2FjaGVHZXQgJiZcbiAgICAgICAgdGhpcy5fY29sdW1uT2Zmc2V0c1tyb3dJbmRleCArIG1heFJvd3MgKiBuY29sc10gPT09IDB4ZmZmZmZmXG4gICAgICApIHtcbiAgICAgICAgbWF4Um93cysrO1xuICAgICAgfVxuXG4gICAgICAvLyBQYXJzZSB0aGUgZGF0YSB0byBnZXQgdGhlIGNvbHVtbiBvZmZzZXRzLlxuICAgICAgY29uc3QgeyBvZmZzZXRzIH0gPSBQQVJTRVJTW3RoaXMuX3BhcnNlcl0oe1xuICAgICAgICBkYXRhOiB0aGlzLl9yYXdEYXRhLFxuICAgICAgICBkZWxpbWl0ZXI6IHRoaXMuX2RlbGltaXRlcixcbiAgICAgICAgcm93RGVsaW1pdGVyOiB0aGlzLl9yb3dEZWxpbWl0ZXIsXG4gICAgICAgIHF1b3RlOiB0aGlzLl9xdW90ZSxcbiAgICAgICAgY29sdW1uT2Zmc2V0czogdHJ1ZSxcbiAgICAgICAgbWF4Um93czogbWF4Um93cyxcbiAgICAgICAgbmNvbHM6IG5jb2xzLFxuICAgICAgICBzdGFydEluZGV4OiB0aGlzLl9yb3dPZmZzZXRzW3Jvd11cbiAgICAgIH0pO1xuXG4gICAgICAvLyBDb3B5IHJlc3VsdHMgdG8gdGhlIGNhY2hlLlxuICAgICAgZm9yIChsZXQgaSA9IDA7IGkgPCBvZmZzZXRzLmxlbmd0aDsgaSsrKSB7XG4gICAgICAgIHRoaXMuX2NvbHVtbk9mZnNldHNbcm93SW5kZXggKyBpXSA9IG9mZnNldHNbaV07XG4gICAgICB9XG4gICAgfVxuXG4gICAgLy8gUmV0dXJuIHRoZSBvZmZzZXQgaW5kZXggZnJvbSBjYWNoZS5cbiAgICByZXR1cm4gdGhpcy5fY29sdW1uT2Zmc2V0c1tyb3dJbmRleCArIGNvbHVtbl07XG4gIH1cblxuICAvKipcbiAgICogUGFyc2UgdGhlIGRhdGEgc3RyaW5nIGFzeW5jaHJvbm91c2x5LlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIEl0IGNhbiB0YWtlIHNldmVyYWwgc2Vjb25kcyB0byBwYXJzZSBhIHNldmVyYWwgaHVuZHJlZCBtZWdhYnl0ZSBzdHJpbmcsIHNvXG4gICAqIHdlIHBhcnNlIHRoZSBmaXJzdCA1MDAgcm93cyB0byBnZXQgc29tZXRoaW5nIHVwIG9uIHRoZSBzY3JlZW4sIHRoZW4gd2VcbiAgICogcGFyc2UgdGhlIGZ1bGwgZGF0YSBzdHJpbmcgYXN5bmNocm9ub3VzbHkuXG4gICAqL1xuICBwYXJzZUFzeW5jKCk6IHZvaWQge1xuICAgIC8vIE51bWJlciBvZiByb3dzIHRvIGdldCBpbml0aWFsbHkuXG4gICAgbGV0IGN1cnJlbnRSb3dzID0gdGhpcy5faW5pdGlhbFJvd3M7XG5cbiAgICAvLyBOdW1iZXIgb2Ygcm93cyB0byBnZXQgaW4gZWFjaCBjaHVuayB0aGVyZWFmdGVyLiBXZSBzZXQgdGhpcyBoaWdoIHRvIGp1c3RcbiAgICAvLyBnZXQgdGhlIHJlc3Qgb2YgdGhlIHJvd3MgZm9yIG5vdy5cbiAgICBsZXQgY2h1bmtSb3dzID0gTWF0aC5wb3coMiwgMzIpIC0gMTtcblxuICAgIC8vIFdlIGdpdmUgdGhlIFVJIGEgY2hhbmNlIHRvIGRyYXcgYnkgZGVsYXlpbmcgdGhlIGNodW5rIHBhcnNpbmcuXG4gICAgY29uc3QgZGVsYXkgPSAzMDsgLy8gbWlsbGlzZWNvbmRzXG5cbiAgICAvLyBEZWZpbmUgYSBmdW5jdGlvbiB0byBwYXJzZSBhIGNodW5rIHVwIHRvIGFuZCBpbmNsdWRpbmcgZW5kUm93LlxuICAgIGNvbnN0IHBhcnNlQ2h1bmsgPSAoZW5kUm93OiBudW1iZXIpID0+IHtcbiAgICAgIHRyeSB7XG4gICAgICAgIHRoaXMuX2NvbXB1dGVSb3dPZmZzZXRzKGVuZFJvdyk7XG4gICAgICB9IGNhdGNoIChlKSB7XG4gICAgICAgIC8vIFNvbWV0aW1lcyB0aGUgZGF0YSBzdHJpbmcgY2Fubm90IGJlIHBhcnNlZCB3aXRoIHRoZSBmdWxsIHBhcnNlciAoZm9yXG4gICAgICAgIC8vIGV4YW1wbGUsIHdlIG1heSBoYXZlIHRoZSB3cm9uZyBkZWxpbWl0ZXIpLiBJbiB0aGVzZSBjYXNlcywgZmFsbCBiYWNrIHRvXG4gICAgICAgIC8vIHRoZSBzaW1wbGVyIHBhcnNlciBzbyB3ZSBjYW4gc2hvdyBzb21ldGhpbmcuXG4gICAgICAgIGlmICh0aGlzLl9wYXJzZXIgPT09ICdxdW90ZXMnKSB7XG4gICAgICAgICAgY29uc29sZS53YXJuKGUpO1xuICAgICAgICAgIHRoaXMuX3BhcnNlciA9ICdub3F1b3Rlcyc7XG4gICAgICAgICAgdGhpcy5fcmVzZXRQYXJzZXIoKTtcbiAgICAgICAgICB0aGlzLl9jb21wdXRlUm93T2Zmc2V0cyhlbmRSb3cpO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIHRocm93IGU7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICAgIHJldHVybiB0aGlzLl9kb25lUGFyc2luZztcbiAgICB9O1xuXG4gICAgLy8gUmVzZXQgdGhlIHBhcnNlciB0byBpdHMgaW5pdGlhbCBzdGF0ZS5cbiAgICB0aGlzLl9yZXNldFBhcnNlcigpO1xuXG4gICAgLy8gUGFyc2UgdGhlIGZpcnN0IHJvd3MgdG8gZ2l2ZSB1cyB0aGUgc3RhcnQgb2YgdGhlIGRhdGEgcmlnaHQgYXdheS5cbiAgICBjb25zdCBkb25lID0gcGFyc2VDaHVuayhjdXJyZW50Um93cyk7XG5cbiAgICAvLyBJZiB3ZSBhcmUgZG9uZSwgcmV0dXJuIGVhcmx5LlxuICAgIGlmIChkb25lKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgLy8gRGVmaW5lIGEgZnVuY3Rpb24gdG8gcmVjdXJzaXZlbHkgcGFyc2UgdGhlIG5leHQgY2h1bmsgYWZ0ZXIgYSBkZWxheS5cbiAgICBjb25zdCBkZWxheWVkUGFyc2UgPSAoKSA9PiB7XG4gICAgICAvLyBQYXJzZSB1cCB0byB0aGUgbmV3IGVuZCByb3cuXG4gICAgICBjb25zdCBkb25lID0gcGFyc2VDaHVuayhjdXJyZW50Um93cyArIGNodW5rUm93cyk7XG4gICAgICBjdXJyZW50Um93cyArPSBjaHVua1Jvd3M7XG5cbiAgICAgIC8vIEdyYWR1YWxseSBkb3VibGUgdGhlIGNodW5rIHNpemUgdW50aWwgd2UgcmVhY2ggYSBtaWxsaW9uIHJvd3MsIGlmIHdlXG4gICAgICAvLyBzdGFydCBiZWxvdyBhIG1pbGxpb24tcm93IGNodW5rIHNpemUuXG4gICAgICBpZiAoY2h1bmtSb3dzIDwgMTAwMDAwMCkge1xuICAgICAgICBjaHVua1Jvd3MgKj0gMjtcbiAgICAgIH1cblxuICAgICAgLy8gSWYgd2UgYXJlbid0IGRvbmUsIHRoZSBzY2hlZHVsZSBhbm90aGVyIHBhcnNlLlxuICAgICAgaWYgKGRvbmUpIHtcbiAgICAgICAgdGhpcy5fZGVsYXllZFBhcnNlID0gbnVsbDtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIHRoaXMuX2RlbGF5ZWRQYXJzZSA9IHdpbmRvdy5zZXRUaW1lb3V0KGRlbGF5ZWRQYXJzZSwgZGVsYXkpO1xuICAgICAgfVxuICAgIH07XG5cbiAgICAvLyBQYXJzZSBmdWxsIGRhdGEgc3RyaW5nIGluIGNodW5rcywgZGVsYXllZCBieSBhIGZldyBtaWxsaXNlY29uZHMgdG8gZ2l2ZSB0aGUgVUkgYSBjaGFuY2UgdG8gZHJhdy5cbiAgICB0aGlzLl9kZWxheWVkUGFyc2UgPSB3aW5kb3cuc2V0VGltZW91dChkZWxheWVkUGFyc2UsIGRlbGF5KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBDb21wdXRlIHRoZSByb3cgb2Zmc2V0cyBhbmQgaW5pdGlhbGl6ZSB0aGUgY29sdW1uIG9mZnNldCBjYWNoZS5cbiAgICpcbiAgICogQHBhcmFtIGVuZFJvdyAtIFRoZSBsYXN0IHJvdyB0byBwYXJzZSwgZnJvbSB0aGUgc3RhcnQgb2YgdGhlIGRhdGEgKGZpcnN0XG4gICAqIHJvdyBpcyByb3cgMSkuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBtZXRob2Qgc3VwcG9ydHMgcGFyc2luZyB0aGUgZGF0YSBpbmNyZW1lbnRhbGx5IGJ5IGNhbGxpbmcgaXQgd2l0aFxuICAgKiBpbmNyZW1lbnRhbGx5IGhpZ2hlciBlbmRSb3cuIFJvd3MgdGhhdCBoYXZlIGFscmVhZHkgYmVlbiBwYXJzZWQgd2lsbCBub3QgYmVcbiAgICogcGFyc2VkIGFnYWluLlxuICAgKi9cbiAgcHJpdmF0ZSBfY29tcHV0ZVJvd09mZnNldHMoZW5kUm93ID0gNDI5NDk2NzI5NSk6IHZvaWQge1xuICAgIC8vIElmIHdlJ3ZlIGFscmVhZHkgcGFyc2VkIHVwIHRvIGVuZFJvdywgb3IgaWYgd2UndmUgYWxyZWFkeSBwYXJzZWQgdGhlXG4gICAgLy8gZW50aXJlIGRhdGEgc2V0LCByZXR1cm4gZWFybHkuXG4gICAgaWYgKHRoaXMuX3Jvd0NvdW50ISA+PSBlbmRSb3cgfHwgdGhpcy5fZG9uZVBhcnNpbmcgPT09IHRydWUpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICAvLyBDb21wdXRlIHRoZSBjb2x1bW4gY291bnQgaWYgd2UgZG9uJ3QgYWxyZWFkeSBoYXZlIGl0LlxuICAgIGlmICh0aGlzLl9jb2x1bW5Db3VudCA9PT0gdW5kZWZpbmVkKSB7XG4gICAgICAvLyBHZXQgbnVtYmVyIG9mIGNvbHVtbnMgaW4gZmlyc3Qgcm93XG4gICAgICB0aGlzLl9jb2x1bW5Db3VudCA9IFBBUlNFUlNbdGhpcy5fcGFyc2VyXSh7XG4gICAgICAgIGRhdGE6IHRoaXMuX3Jhd0RhdGEsXG4gICAgICAgIGRlbGltaXRlcjogdGhpcy5fZGVsaW1pdGVyLFxuICAgICAgICByb3dEZWxpbWl0ZXI6IHRoaXMuX3Jvd0RlbGltaXRlcixcbiAgICAgICAgcXVvdGU6IHRoaXMuX3F1b3RlLFxuICAgICAgICBjb2x1bW5PZmZzZXRzOiB0cnVlLFxuICAgICAgICBtYXhSb3dzOiAxXG4gICAgICB9KS5uY29scztcbiAgICB9XG5cbiAgICAvLyBgcmVwYXJzZWAgaXMgdGhlIG51bWJlciBvZiByb3dzIHdlIGFyZSByZXF1ZXN0aW5nIHRvIHBhcnNlIG92ZXIgYWdhaW4uXG4gICAgLy8gV2UgZ2VuZXJhbGx5IHN0YXJ0IGF0IHRoZSBiZWdpbm5pbmcgb2YgdGhlIGxhc3Qgcm93IG9mZnNldCwgc28gdGhhdCB0aGVcbiAgICAvLyBmaXJzdCByb3cgb2Zmc2V0IHJldHVybmVkIGlzIHRoZSBzYW1lIGFzIHRoZSBsYXN0IHJvdyBvZmZzZXQgd2UgYWxyZWFkeVxuICAgIC8vIGhhdmUuIFdlIHBhcnNlIHRoZSBkYXRhIHVwIHRvIGFuZCBpbmNsdWRpbmcgdGhlIHJlcXVlc3RlZCByb3cuXG4gICAgY29uc3QgcmVwYXJzZSA9IHRoaXMuX3Jvd0NvdW50ISA+IDAgPyAxIDogMDtcbiAgICBjb25zdCB7IG5yb3dzLCBvZmZzZXRzIH0gPSBQQVJTRVJTW3RoaXMuX3BhcnNlcl0oe1xuICAgICAgZGF0YTogdGhpcy5fcmF3RGF0YSxcbiAgICAgIHN0YXJ0SW5kZXg6IHRoaXMuX3Jvd09mZnNldHNbdGhpcy5fcm93Q291bnQhIC0gcmVwYXJzZV0gPz8gMCxcbiAgICAgIGRlbGltaXRlcjogdGhpcy5fZGVsaW1pdGVyLFxuICAgICAgcm93RGVsaW1pdGVyOiB0aGlzLl9yb3dEZWxpbWl0ZXIsXG4gICAgICBxdW90ZTogdGhpcy5fcXVvdGUsXG4gICAgICBjb2x1bW5PZmZzZXRzOiBmYWxzZSxcbiAgICAgIG1heFJvd3M6IGVuZFJvdyAtIHRoaXMuX3Jvd0NvdW50ISArIHJlcGFyc2VcbiAgICB9KTtcblxuICAgIC8vIElmIHdlIGhhdmUgYWxyZWFkeSBzZXQgdXAgb3VyIGluaXRpYWwgYm9va2tlZXBpbmcsIHJldHVybiBlYXJseSBpZiB3ZVxuICAgIC8vIGRpZCBub3QgZ2V0IGFueSBuZXcgcm93cyBiZXlvbmQgdGhlIGxhc3Qgcm93IHRoYXQgd2UndmUgcGFyc2VkLCBpLmUuLFxuICAgIC8vIG5yb3dzPT09MS5cbiAgICBpZiAodGhpcy5fc3RhcnRlZFBhcnNpbmcgJiYgbnJvd3MgPD0gcmVwYXJzZSkge1xuICAgICAgdGhpcy5fZG9uZVBhcnNpbmcgPSB0cnVlO1xuICAgICAgdGhpcy5fcmVhZHkucmVzb2x2ZSh1bmRlZmluZWQpO1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIHRoaXMuX3N0YXJ0ZWRQYXJzaW5nID0gdHJ1ZTtcblxuICAgIC8vIFVwZGF0ZSB0aGUgcm93IGNvdW50LCBhY2NvdW50aW5nIGZvciBob3cgbWFueSByb3dzIHdlcmUgcmVwYXJzZWQuXG4gICAgY29uc3Qgb2xkUm93Q291bnQgPSB0aGlzLl9yb3dDb3VudCE7XG4gICAgY29uc3QgZHVwbGljYXRlUm93cyA9IE1hdGgubWluKG5yb3dzLCByZXBhcnNlKTtcbiAgICB0aGlzLl9yb3dDb3VudCA9IG9sZFJvd0NvdW50ICsgbnJvd3MgLSBkdXBsaWNhdGVSb3dzO1xuXG4gICAgLy8gSWYgd2UgZGlkbid0IHJlYWNoIHRoZSByZXF1ZXN0ZWQgcm93LCB3ZSBtdXN0IGJlIGRvbmUuXG4gICAgaWYgKHRoaXMuX3Jvd0NvdW50IDwgZW5kUm93KSB7XG4gICAgICB0aGlzLl9kb25lUGFyc2luZyA9IHRydWU7XG4gICAgICB0aGlzLl9yZWFkeS5yZXNvbHZlKHVuZGVmaW5lZCk7XG4gICAgfVxuXG4gICAgLy8gQ29weSB0aGUgbmV3IG9mZnNldHMgaW50byBhIG5ldyByb3cgb2Zmc2V0IGFycmF5IGlmIG5lZWRlZC5cbiAgICBpZiAodGhpcy5fcm93Q291bnQgPiBvbGRSb3dDb3VudCkge1xuICAgICAgY29uc3Qgb2xkUm93T2Zmc2V0cyA9IHRoaXMuX3Jvd09mZnNldHM7XG4gICAgICB0aGlzLl9yb3dPZmZzZXRzID0gbmV3IFVpbnQzMkFycmF5KHRoaXMuX3Jvd0NvdW50KTtcbiAgICAgIHRoaXMuX3Jvd09mZnNldHMuc2V0KG9sZFJvd09mZnNldHMpO1xuICAgICAgdGhpcy5fcm93T2Zmc2V0cy5zZXQob2Zmc2V0cywgb2xkUm93Q291bnQgLSBkdXBsaWNhdGVSb3dzKTtcbiAgICB9XG5cbiAgICAvLyBFeHBhbmQgdGhlIGNvbHVtbiBvZmZzZXRzIGFycmF5IGlmIG5lZWRlZFxuXG4gICAgLy8gSWYgdGhlIGZ1bGwgY29sdW1uIG9mZnNldHMgYXJyYXkgaXMgc21hbGwgZW5vdWdoLCBidWlsZCBhIGNhY2hlIGJpZ1xuICAgIC8vIGVub3VnaCBmb3IgYWxsIGNvbHVtbiBvZmZzZXRzLiBXZSBhbGxvY2F0ZSB1cCB0byAxMjggbWVnYWJ5dGVzOlxuICAgIC8vIDEyOCooMioqMjAgYnl0ZXMvTSkvKDQgYnl0ZXMvZW50cnkpID0gMzM1NTQ0MzIgZW50cmllcy5cbiAgICBjb25zdCBtYXhDb2x1bW5PZmZzZXRzUm93cyA9IE1hdGguZmxvb3IoMzM1NTQ0MzIgLyB0aGlzLl9jb2x1bW5Db3VudCk7XG5cbiAgICAvLyBXZSBuZWVkIHRvIGV4cGFuZCB0aGUgY29sdW1uIG9mZnNldCBhcnJheSBpZiB3ZSB3ZXJlIHN0b3JpbmcgYWxsIGNvbHVtblxuICAgIC8vIG9mZnNldHMgYmVmb3JlLiBDaGVjayB0byBzZWUgaWYgdGhlIHByZXZpb3VzIHNpemUgd2FzIHNtYWxsIGVub3VnaCB0aGF0XG4gICAgLy8gd2Ugc3RvcmVkIGFsbCBjb2x1bW4gb2Zmc2V0cy5cbiAgICBpZiAob2xkUm93Q291bnQgPD0gbWF4Q29sdW1uT2Zmc2V0c1Jvd3MpIHtcbiAgICAgIC8vIENoZWNrIHRvIHNlZSBpZiB0aGUgbmV3IGNvbHVtbiBvZmZzZXRzIGFycmF5IGlzIHNtYWxsIGVub3VnaCB0byBzdGlsbFxuICAgICAgLy8gc3RvcmUsIG9yIGlmIHdlIHNob3VsZCBjdXQgb3ZlciB0byBhIHNtYWxsIGNhY2hlLlxuICAgICAgaWYgKHRoaXMuX3Jvd0NvdW50IDw9IG1heENvbHVtbk9mZnNldHNSb3dzKSB7XG4gICAgICAgIC8vIEV4cGFuZCB0aGUgZXhpc3RpbmcgY29sdW1uIG9mZnNldCBhcnJheSBmb3IgbmV3IGNvbHVtbiBvZmZzZXRzLlxuICAgICAgICBjb25zdCBvbGRDb2x1bW5PZmZzZXRzID0gdGhpcy5fY29sdW1uT2Zmc2V0cztcbiAgICAgICAgdGhpcy5fY29sdW1uT2Zmc2V0cyA9IG5ldyBVaW50MzJBcnJheShcbiAgICAgICAgICB0aGlzLl9yb3dDb3VudCAqIHRoaXMuX2NvbHVtbkNvdW50XG4gICAgICAgICk7XG4gICAgICAgIHRoaXMuX2NvbHVtbk9mZnNldHMuc2V0KG9sZENvbHVtbk9mZnNldHMpO1xuICAgICAgICB0aGlzLl9jb2x1bW5PZmZzZXRzLmZpbGwoMHhmZmZmZmZmZiwgb2xkQ29sdW1uT2Zmc2V0cy5sZW5ndGgpO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgLy8gSWYgbm90LCB0aGVuIG91ciBjYWNoZSBzaXplIGlzIGF0IG1vc3QgdGhlIG1heGltdW0gbnVtYmVyIG9mIHJvd3Mgd2VcbiAgICAgICAgLy8gZmlsbCBpbiB0aGUgY2FjaGUgYXQgYSB0aW1lLlxuICAgICAgICBjb25zdCBvbGRDb2x1bW5PZmZzZXRzID0gdGhpcy5fY29sdW1uT2Zmc2V0cztcbiAgICAgICAgdGhpcy5fY29sdW1uT2Zmc2V0cyA9IG5ldyBVaW50MzJBcnJheShcbiAgICAgICAgICBNYXRoLm1pbih0aGlzLl9tYXhDYWNoZUdldCwgbWF4Q29sdW1uT2Zmc2V0c1Jvd3MpICogdGhpcy5fY29sdW1uQ291bnRcbiAgICAgICAgKTtcblxuICAgICAgICAvLyBGaWxsIGluIHRoZSBlbnRyaWVzIHdlIGFscmVhZHkgaGF2ZS5cbiAgICAgICAgdGhpcy5fY29sdW1uT2Zmc2V0cy5zZXQoXG4gICAgICAgICAgb2xkQ29sdW1uT2Zmc2V0cy5zdWJhcnJheSgwLCB0aGlzLl9jb2x1bW5PZmZzZXRzLmxlbmd0aClcbiAgICAgICAgKTtcblxuICAgICAgICAvLyBJbnZhbGlkYXRlIHRoZSByZXN0IG9mIHRoZSBlbnRyaWVzLlxuICAgICAgICB0aGlzLl9jb2x1bW5PZmZzZXRzLmZpbGwoMHhmZmZmZmZmZiwgb2xkQ29sdW1uT2Zmc2V0cy5sZW5ndGgpO1xuICAgICAgICB0aGlzLl9jb2x1bW5PZmZzZXRzU3RhcnRpbmdSb3cgPSAwO1xuICAgICAgfVxuICAgIH1cblxuICAgIC8vIFdlIGhhdmUgbW9yZSByb3dzIHRoYW4gYmVmb3JlLCBzbyBlbWl0IHRoZSByb3dzLWluc2VydGVkIGNoYW5nZSBzaWduYWwuXG4gICAgbGV0IGZpcnN0SW5kZXggPSBvbGRSb3dDb3VudDtcbiAgICBpZiAodGhpcy5faGVhZGVyLmxlbmd0aCA+IDApIHtcbiAgICAgIGZpcnN0SW5kZXggLT0gMTtcbiAgICB9XG4gICAgdGhpcy5lbWl0Q2hhbmdlZCh7XG4gICAgICB0eXBlOiAncm93cy1pbnNlcnRlZCcsXG4gICAgICByZWdpb246ICdib2R5JyxcbiAgICAgIGluZGV4OiBmaXJzdEluZGV4LFxuICAgICAgc3BhbjogdGhpcy5fcm93Q291bnQgLSBvbGRSb3dDb3VudFxuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgcGFyc2VkIHN0cmluZyBmaWVsZCBmb3IgYSByb3cgYW5kIGNvbHVtbi5cbiAgICpcbiAgICogQHBhcmFtIHJvdyAtIFRoZSByb3cgbnVtYmVyIG9mIHRoZSBkYXRhIGl0ZW0uXG4gICAqIEBwYXJhbSBjb2x1bW4gLSBUaGUgY29sdW1uIG51bWJlciBvZiB0aGUgZGF0YSBpdGVtLlxuICAgKiBAcmV0dXJucyBUaGUgcGFyc2VkIHN0cmluZyBmb3IgdGhlIGRhdGEgaXRlbS5cbiAgICovXG4gIHByaXZhdGUgX2dldEZpZWxkKHJvdzogbnVtYmVyLCBjb2x1bW46IG51bWJlcik6IHN0cmluZyB7XG4gICAgLy8gRGVjbGFyZSBsb2NhbCB2YXJpYWJsZXMuXG4gICAgbGV0IHZhbHVlOiBzdHJpbmc7XG4gICAgbGV0IG5leHRJbmRleDtcblxuICAgIC8vIEZpbmQgdGhlIGluZGV4IGZvciB0aGUgZmlyc3QgY2hhcmFjdGVyIGluIHRoZSBmaWVsZC5cbiAgICBjb25zdCBpbmRleCA9IHRoaXMuZ2V0T2Zmc2V0SW5kZXgocm93LCBjb2x1bW4pO1xuXG4gICAgLy8gSW5pdGlhbGl6ZSB0aGUgdHJpbSBhZGp1c3RtZW50cy5cbiAgICBsZXQgdHJpbVJpZ2h0ID0gMDtcbiAgICBsZXQgdHJpbUxlZnQgPSAwO1xuXG4gICAgLy8gRmluZCB0aGUgZW5kIG9mIHRoZSBzbGljZSAodGhlIHN0YXJ0IG9mIHRoZSBuZXh0IGZpZWxkKSwgYW5kIGhvdyBtdWNoIHdlXG4gICAgLy8gc2hvdWxkIGFkanVzdCB0byB0cmltIG9mZiBhIHRyYWlsaW5nIGZpZWxkIG9yIHJvdyBkZWxpbWl0ZXIuIEZpcnN0IGNoZWNrXG4gICAgLy8gaWYgd2UgYXJlIGdldHRpbmcgdGhlIGxhc3QgY29sdW1uLlxuICAgIGlmIChjb2x1bW4gPT09IHRoaXMuX2NvbHVtbkNvdW50ISAtIDEpIHtcbiAgICAgIC8vIENoZWNrIGlmIHdlIGFyZSBnZXR0aW5nIGFueSByb3cgYnV0IHRoZSBsYXN0LlxuICAgICAgaWYgKHJvdyA8IHRoaXMuX3Jvd0NvdW50ISAtIDEpIHtcbiAgICAgICAgLy8gU2V0IHRoZSBuZXh0IG9mZnNldCB0byB0aGUgbmV4dCByb3csIGNvbHVtbiAwLlxuICAgICAgICBuZXh0SW5kZXggPSB0aGlzLmdldE9mZnNldEluZGV4KHJvdyArIDEsIDApO1xuXG4gICAgICAgIC8vIFNpbmNlIHdlIGFyZSBub3QgYXQgdGhlIGxhc3Qgcm93LCB3ZSBuZWVkIHRvIHRyaW0gb2ZmIHRoZSByb3dcbiAgICAgICAgLy8gZGVsaW1pdGVyLlxuICAgICAgICB0cmltUmlnaHQgKz0gdGhpcy5fcm93RGVsaW1pdGVyLmxlbmd0aDtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIC8vIFdlIGFyZSBnZXR0aW5nIHRoZSBsYXN0IGRhdGEgaXRlbSwgc28gdGhlIHNsaWNlIGVuZCBpcyB0aGUgZW5kIG9mIHRoZVxuICAgICAgICAvLyBkYXRhIHN0cmluZy5cbiAgICAgICAgbmV4dEluZGV4ID0gdGhpcy5fcmF3RGF0YS5sZW5ndGg7XG5cbiAgICAgICAgLy8gVGhlIHN0cmluZyBtYXkgb3IgbWF5IG5vdCBlbmQgaW4gYSByb3cgZGVsaW1pdGVyIChSRkMgNDE4MCAyLjIpLCBzb1xuICAgICAgICAvLyB3ZSBleHBsaWNpdGx5IGNoZWNrIGlmIHdlIHNob3VsZCB0cmltIG9mZiBhIHJvdyBkZWxpbWl0ZXIuXG4gICAgICAgIGlmIChcbiAgICAgICAgICB0aGlzLl9yYXdEYXRhW25leHRJbmRleCAtIDFdID09PVxuICAgICAgICAgIHRoaXMuX3Jvd0RlbGltaXRlclt0aGlzLl9yb3dEZWxpbWl0ZXIubGVuZ3RoIC0gMV1cbiAgICAgICAgKSB7XG4gICAgICAgICAgdHJpbVJpZ2h0ICs9IHRoaXMuX3Jvd0RlbGltaXRlci5sZW5ndGg7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9IGVsc2Uge1xuICAgICAgLy8gVGhlIG5leHQgZmllbGQgc3RhcnRzIGF0IHRoZSBuZXh0IGNvbHVtbiBvZmZzZXQuXG4gICAgICBuZXh0SW5kZXggPSB0aGlzLmdldE9mZnNldEluZGV4KHJvdywgY29sdW1uICsgMSk7XG5cbiAgICAgIC8vIFRyaW0gb2ZmIHRoZSBkZWxpbWl0ZXIgaWYgaXQgZXhpc3RzIGF0IHRoZSBlbmQgb2YgdGhlIGZpZWxkXG4gICAgICBpZiAoXG4gICAgICAgIGluZGV4IDwgbmV4dEluZGV4ICYmXG4gICAgICAgIHRoaXMuX3Jhd0RhdGFbbmV4dEluZGV4IC0gMV0gPT09IHRoaXMuX2RlbGltaXRlclxuICAgICAgKSB7XG4gICAgICAgIHRyaW1SaWdodCArPSAxO1xuICAgICAgfVxuICAgIH1cblxuICAgIC8vIENoZWNrIHRvIHNlZSBpZiB0aGUgZmllbGQgYmVnaW5zIHdpdGggYSBxdW90ZS4gSWYgaXQgZG9lcywgdHJpbSBhIHF1b3RlIG9uIGVpdGhlciBzaWRlLlxuICAgIGlmICh0aGlzLl9yYXdEYXRhW2luZGV4XSA9PT0gdGhpcy5fcXVvdGUpIHtcbiAgICAgIHRyaW1MZWZ0ICs9IDE7XG4gICAgICB0cmltUmlnaHQgKz0gMTtcbiAgICB9XG5cbiAgICAvLyBTbGljZSB0aGUgYWN0dWFsIHZhbHVlIG91dCBvZiB0aGUgZGF0YSBzdHJpbmcuXG4gICAgdmFsdWUgPSB0aGlzLl9yYXdEYXRhLnNsaWNlKGluZGV4ICsgdHJpbUxlZnQsIG5leHRJbmRleCAtIHRyaW1SaWdodCk7XG5cbiAgICAvLyBJZiB3ZSBoYXZlIGEgcXVvdGVkIGZpZWxkIGFuZCB3ZSBoYXZlIGFuIGVzY2FwZWQgcXVvdGUgaW5zaWRlIGl0LCB1bmVzY2FwZSBpdC5cbiAgICBpZiAodHJpbUxlZnQgPT09IDEgJiYgdmFsdWUuaW5kZXhPZih0aGlzLl9xdW90ZSkgIT09IC0xKSB7XG4gICAgICB2YWx1ZSA9IHZhbHVlLnJlcGxhY2UodGhpcy5fcXVvdGVFc2NhcGVkLCB0aGlzLl9xdW90ZSk7XG4gICAgfVxuXG4gICAgLy8gUmV0dXJuIHRoZSB2YWx1ZS5cbiAgICByZXR1cm4gdmFsdWU7XG4gIH1cblxuICAvKipcbiAgICogUmVzZXQgdGhlIHBhcnNlciBzdGF0ZS5cbiAgICovXG4gIHByaXZhdGUgX3Jlc2V0UGFyc2VyKCk6IHZvaWQge1xuICAgIHRoaXMuX2NvbHVtbkNvdW50ID0gdW5kZWZpbmVkO1xuXG4gICAgdGhpcy5fcm93T2Zmc2V0cyA9IG5ldyBVaW50MzJBcnJheSgwKTtcbiAgICB0aGlzLl9yb3dDb3VudCA9IDA7XG4gICAgdGhpcy5fc3RhcnRlZFBhcnNpbmcgPSBmYWxzZTtcblxuICAgIHRoaXMuX2NvbHVtbk9mZnNldHMgPSBuZXcgVWludDMyQXJyYXkoMCk7XG5cbiAgICAvLyBDbGVhciBvdXQgc3RhdGUgYXNzb2NpYXRlZCB3aXRoIHRoZSBhc3luY2hyb25vdXMgcGFyc2luZy5cbiAgICBpZiAodGhpcy5fZG9uZVBhcnNpbmcgPT09IGZhbHNlKSB7XG4gICAgICAvLyBFeHBsaWNpdGx5IGNhdGNoIHRoaXMgcmVqZWN0aW9uIGF0IGxlYXN0IG9uY2Ugc28gYW4gZXJyb3IgaXMgbm90IHRocm93blxuICAgICAgLy8gdG8gdGhlIGNvbnNvbGUuXG4gICAgICB0aGlzLnJlYWR5LmNhdGNoKCgpID0+IHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfSk7XG4gICAgICB0aGlzLl9yZWFkeS5yZWplY3QodW5kZWZpbmVkKTtcbiAgICB9XG4gICAgdGhpcy5fZG9uZVBhcnNpbmcgPSBmYWxzZTtcbiAgICB0aGlzLl9yZWFkeSA9IG5ldyBQcm9taXNlRGVsZWdhdGU8dm9pZD4oKTtcbiAgICBpZiAodGhpcy5fZGVsYXllZFBhcnNlICE9PSBudWxsKSB7XG4gICAgICB3aW5kb3cuY2xlYXJUaW1lb3V0KHRoaXMuX2RlbGF5ZWRQYXJzZSk7XG4gICAgICB0aGlzLl9kZWxheWVkUGFyc2UgPSBudWxsO1xuICAgIH1cblxuICAgIHRoaXMuZW1pdENoYW5nZWQoeyB0eXBlOiAnbW9kZWwtcmVzZXQnIH0pO1xuICB9XG5cbiAgLy8gUGFyc2VyIHNldHRpbmdzXG4gIHByaXZhdGUgX2RlbGltaXRlcjogc3RyaW5nO1xuICBwcml2YXRlIF9xdW90ZTogc3RyaW5nO1xuICBwcml2YXRlIF9xdW90ZUVzY2FwZWQ6IFJlZ0V4cDtcbiAgcHJpdmF0ZSBfcGFyc2VyOiAncXVvdGVzJyB8ICdub3F1b3Rlcyc7XG4gIHByaXZhdGUgX3Jvd0RlbGltaXRlcjogc3RyaW5nO1xuXG4gIC8vIERhdGEgdmFsdWVzXG4gIHByaXZhdGUgX3Jhd0RhdGE6IHN0cmluZztcbiAgcHJpdmF0ZSBfcm93Q291bnQ6IG51bWJlciB8IHVuZGVmaW5lZCA9IDA7XG4gIHByaXZhdGUgX2NvbHVtbkNvdW50OiBudW1iZXIgfCB1bmRlZmluZWQ7XG5cbiAgLy8gQ2FjaGUgaW5mb3JtYXRpb25cbiAgLyoqXG4gICAqIFRoZSBoZWFkZXIgc3RyaW5ncy5cbiAgICovXG4gIHByaXZhdGUgX2hlYWRlcjogc3RyaW5nW10gPSBbXTtcbiAgLyoqXG4gICAqIFRoZSBjb2x1bW4gb2Zmc2V0IGNhY2hlLCBzdGFydGluZyB3aXRoIHJvdyBfY29sdW1uT2Zmc2V0c1N0YXJ0aW5nUm93XG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhlIGluZGV4IG9mIHRoZSBmaXJzdCBjaGFyYWN0ZXIgaW4gdGhlIGRhdGEgc3RyaW5nIGZvciByb3cgciwgY29sdW1uIGMgaXNcbiAgICogX2NvbHVtbk9mZnNldHNbKHItdGhpcy5fY29sdW1uT2Zmc2V0c1N0YXJ0aW5nUm93KSpudW1Db2x1bW5zK2NdXG4gICAqL1xuICBwcml2YXRlIF9jb2x1bW5PZmZzZXRzOiBVaW50MzJBcnJheSA9IG5ldyBVaW50MzJBcnJheSgwKTtcbiAgLyoqXG4gICAqIFRoZSByb3cgdGhhdCBfY29sdW1uT2Zmc2V0c1swXSByZXByZXNlbnRzLlxuICAgKi9cbiAgcHJpdmF0ZSBfY29sdW1uT2Zmc2V0c1N0YXJ0aW5nUm93OiBudW1iZXIgPSAwO1xuICAvKipcbiAgICogVGhlIG1heGltdW0gbnVtYmVyIG9mIHJvd3MgdG8gcGFyc2Ugd2hlbiB0aGVyZSBpcyBhIGNhY2hlIG1pc3MuXG4gICAqL1xuICBwcml2YXRlIF9tYXhDYWNoZUdldDogbnVtYmVyID0gMTAwMDtcbiAgLyoqXG4gICAqIFRoZSBpbmRleCBmb3IgdGhlIHN0YXJ0IG9mIGVhY2ggcm93LlxuICAgKi9cbiAgcHJpdmF0ZSBfcm93T2Zmc2V0czogVWludDMyQXJyYXkgPSBuZXcgVWludDMyQXJyYXkoMCk7XG4gIC8qKlxuICAgKiBUaGUgbnVtYmVyIG9mIHJvd3MgdG8gcGFyc2UgaW5pdGlhbGx5IGJlZm9yZSBkb2luZyBhIGRlbGF5ZWQgcGFyc2Ugb2YgdGhlXG4gICAqIGVudGlyZSBkYXRhLlxuICAgKi9cbiAgcHJpdmF0ZSBfaW5pdGlhbFJvd3M6IG51bWJlcjtcblxuICAvLyBCb29ra2VlcGluZyB2YXJpYWJsZXMuXG4gIHByaXZhdGUgX2RlbGF5ZWRQYXJzZTogbnVtYmVyIHwgbnVsbCA9IG51bGw7XG4gIHByaXZhdGUgX3N0YXJ0ZWRQYXJzaW5nOiBib29sZWFuID0gZmFsc2U7XG4gIHByaXZhdGUgX2RvbmVQYXJzaW5nOiBib29sZWFuID0gZmFsc2U7XG4gIHByaXZhdGUgX2lzRGlzcG9zZWQ6IGJvb2xlYW4gPSBmYWxzZTtcbiAgcHJpdmF0ZSBfcmVhZHkgPSBuZXcgUHJvbWlzZURlbGVnYXRlPHZvaWQ+KCk7XG59XG5cbi8qKlxuICogVGhlIG5hbWVzcGFjZSBmb3IgdGhlIGBEU1ZNb2RlbGAgY2xhc3Mgc3RhdGljcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBEU1ZNb2RlbCB7XG4gIC8qKlxuICAgKiBBbiBvcHRpb25zIG9iamVjdCBmb3IgaW5pdGlhbGl6aW5nIGEgZGVsaW1pdGVyLXNlcGFyYXRlZCBkYXRhIG1vZGVsLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIGZpZWxkIGRlbGltaXRlciwgc3VjaCBhcyAnLCcgb3IgJ1xcdCcuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogVGhlIGZpZWxkIGRlbGltaXRlciBtdXN0IGJlIGEgc2luZ2xlIGNoYXJhY3Rlci5cbiAgICAgKi9cbiAgICBkZWxpbWl0ZXI6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFRoZSBkYXRhIHNvdXJjZSBmb3IgdGhlIGRhdGEgbW9kZWwuXG4gICAgICovXG4gICAgZGF0YTogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0aGUgZGF0YSBoYXMgYSBvbmUtcm93IGhlYWRlci5cbiAgICAgKi9cbiAgICBoZWFkZXI/OiBib29sZWFuO1xuXG4gICAgLyoqXG4gICAgICogUm93IGRlbGltaXRlci5cbiAgICAgKlxuICAgICAqICMjIyMgTm90ZXNcbiAgICAgKiBBbnkgY2FycmlhZ2UgcmV0dXJuIG9yIG5ld2xpbmUgY2hhcmFjdGVyIHRoYXQgaXMgbm90IGEgZGVsaW1pdGVyIHNob3VsZFxuICAgICAqIGJlIGluIGEgcXVvdGVkIGZpZWxkLCByZWdhcmRsZXNzIG9mIHRoZSByb3cgZGVsaW1pdGVyIHNldHRpbmcuXG4gICAgICovXG4gICAgcm93RGVsaW1pdGVyPzogJ1xcclxcbicgfCAnXFxyJyB8ICdcXG4nO1xuXG4gICAgLyoqXG4gICAgICogUXVvdGUgY2hhcmFjdGVyLlxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIFF1b3RlcyBhcmUgZXNjYXBlZCBieSByZXBlYXRpbmcgdGhlbSwgYXMgaW4gUkZDIDQxODAuIFRoZSBxdW90ZSBtdXN0IGJlIGFcbiAgICAgKiBzaW5nbGUgY2hhcmFjdGVyLlxuICAgICAqL1xuICAgIHF1b3RlPzogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0byB1c2UgdGhlIHBhcnNlciB0aGF0IGNhbiBoYW5kbGUgcXVvdGVkIGRlbGltaXRlcnMuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogU2V0dGluZyB0aGlzIHRvIGZhbHNlIHVzZXMgYSBtdWNoIGZhc3RlciBwYXJzZXIsIGJ1dCBhc3N1bWVzIHRoZXJlIGFyZVxuICAgICAqIG5vdCBhbnkgZmllbGQgb3Igcm93IGRlbGltaXRlcnMgdGhhdCBhcmUgcXVvdGVkIGluIGZpZWxkcy4gSWYgdGhpcyBpcyBub3RcbiAgICAgKiBzZXQsIGl0IGRlZmF1bHRzIHRvIHRydWUgaWYgYW55IHF1b3RlcyBhcmUgZm91bmQgaW4gdGhlIGRhdGEsIGFuZCBmYWxzZVxuICAgICAqIG90aGVyd2lzZS5cbiAgICAgKi9cbiAgICBxdW90ZVBhcnNlcj86IGJvb2xlYW47XG5cbiAgICAvKipcbiAgICAgKiBUaGUgbWF4aW11bSBudW1iZXIgb2YgaW5pdGlhbCByb3dzIHRvIHBhcnNlIGJlZm9yZSBkb2luZyBhIGFzeW5jaHJvbm91c1xuICAgICAqIGZ1bGwgcGFyc2Ugb2YgdGhlIGRhdGEuIFRoaXMgc2hvdWxkIGJlIGdyZWF0ZXIgdGhhbiAwLlxuICAgICAqL1xuICAgIGluaXRpYWxSb3dzPzogbnVtYmVyO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbi8qXG5Qb3NzaWJsZSBvcHRpb25zIHRvIGFkZCB0byB0aGUgcGFyc2VyOlxuXG4tIE9wdGlvbmFsIG9mZnNldHMgYXJyYXkgdG8gbW9kaWZ5LCBzbyB3ZSBkb24ndCBuZWVkIHRvIGNyZWF0ZSBhIG5ldyBvZmZzZXRzIGxpc3QgKHdlIHdvdWxkIG5lZWQgdG8gYmUgY2FyZWZ1bCBub3QgdG8gb3ZlcndyaXRlIHRoaW5ncyBpZiBhIHJvdyBuZWVkcyB0byBiZSB0cnVuY2F0ZWQuKVxuLSBDb21tZW50IGNoYXJhY3RlciBhdCB0aGUgc3RhcnQgb2YgdGhlIGxpbmVcbi0gU2tpcCBlbXB0eSB3aGl0ZXNwYWNlIGxpbmVzXG4tIFNraXAgcm93cyB3aXRoIGVtcHR5IGNvbHVtbnNcbi0gTG9nZ2luZyBhbiBlcnJvciBmb3IgdG9vIG1hbnkgb3IgdG9vIGZldyBmaWVsZHMgb24gYSBsaW5lXG4tIElnbm9yZSB3aGl0ZXNwYWNlIGFyb3VuZCBkZWxpbWl0ZXJzXG4tIEFkZCBhbiBleHBvcnRlZCBmdW5jdGlvbiBpbiB0aGlzIGZpbGUgZm9yIGdldHRpbmcgYSBmaWVsZCBmcm9tIHRoZSByZXR1cm5lZCBvZmZzZXRzIGFycmF5IChpbmNsdWRpbmcgc3RyaXBwaW5nIGZpZWxkIG9yIHJvdyBkZWxpbWl0ZXJzIGFuZCBwYXJzaW5nIHF1b3RlZCBkYXRhKS4gUmlnaHQgbm93IHRoaXMgbG9naWMgaXMgaW4gdGhlIERTVk1vZGVsLiBMaWtlbHkgd2Ugd2FudCB0byBrZWVwIHRoZSBsb2dpYyB0aGVyZSBmb3Igc3BlZWQsIGJ1dCBoYXZpbmcgaXQgaGVyZSBhcyB3ZWxsIHdpbGwgbWFrZSB0aGUgcGFyc2VyIG1vcmUgc2VsZi1jb250YWluZWQgYW5kIHVzYWJsZSBieSBvdGhlcnMuXG4tIFNhbml0eSBjaGVjayBvbiBmaWVsZCBzaXplLCB3aXRoIGFuIGVycm9yIGlmIHRoZSBmaWVsZCBleGNlZWRzIHRoZSBzaXplXG4tIFRlc3RzIGFnYWluc3QgaHR0cHM6Ly9naXRodWIuY29tL21heG9nZGVuL2Nzdi1zcGVjdHJ1bVxuLSBCZW5jaG1hcmsgYWdhaW5zdCBodHRwczovL3d3dy5ucG1qcy5jb20vcGFja2FnZS9jc3YtcGFyc2VyIGFuZCBodHRwczovL3d3dy5ucG1qcy5jb20vcGFja2FnZS9jc3Ytc3RyaW5nIGFuZCBmYXN0LWNzdi5cblxuKi9cblxuLyoqXG4gKiBJbnRlcmZhY2UgZm9yIGEgZGVsaW1pdGVyLXNlcGFyYXRlZCBkYXRhIHBhcnNlci5cbiAqXG4gKiBAcGFyYW0gb3B0aW9uczogVGhlIHBhcnNlciBvcHRpb25zXG4gKiBAcmV0dXJucyBBbiBvYmplY3QgZ2l2aW5nIHRoZSBvZmZzZXRzIGZvciB0aGUgcm93cyBvciBjb2x1bW5zIHBhcnNlZC5cbiAqXG4gKiAjIyMjIE5vdGVzXG4gKiBUaGUgcGFyc2VycyBhcmUgYmFzZWQgb24gW1JGQyA0MTgwXShodHRwczovL3Rvb2xzLmlldGYub3JnL2h0bWwvcmZjNDE4MCkuXG4gKi9cbmV4cG9ydCB0eXBlIElQYXJzZXIgPSAob3B0aW9uczogSVBhcnNlci5JT3B0aW9ucykgPT4gSVBhcnNlci5JUmVzdWx0cztcblxuZXhwb3J0IG5hbWVzcGFjZSBJUGFyc2VyIHtcbiAgLyoqXG4gICAqIFRoZSBvcHRpb25zIGZvciBhIHBhcnNlci5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMge1xuICAgIC8qKlxuICAgICAqIFRoZSBkYXRhIHRvIHBhcnNlLlxuICAgICAqL1xuICAgIGRhdGE6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFdoZXRoZXIgdG8gcmV0dXJuIGNvbHVtbiBvZmZzZXRzIGluIHRoZSBvZmZzZXRzIGFycmF5LlxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIElmIGZhbHNlLCB0aGUgcmV0dXJuZWQgb2Zmc2V0cyBhcnJheSBjb250YWlucyBqdXN0IHRoZSByb3cgb2Zmc2V0cy4gSWZcbiAgICAgKiB0cnVlLCB0aGUgcmV0dXJuZWQgb2Zmc2V0cyBhcnJheSBjb250YWlucyBhbGwgY29sdW1uIG9mZnNldHMgZm9yIGVhY2hcbiAgICAgKiBjb2x1bW4gaW4gdGhlIHJvd3MgKGkuZS4sIGl0IGhhcyBucm93cypuY29scyBlbnRyaWVzKS4gSW5kaXZpZHVhbCByb3dzXG4gICAgICogd2lsbCBoYXZlIGVtcHR5IGNvbHVtbnMgYWRkZWQgb3IgZXh0cmEgY29sdW1ucyBtZXJnZWQgaW50byB0aGUgbGFzdFxuICAgICAqIGNvbHVtbiBpZiB0aGV5IGRvIG5vdCBoYXZlIGV4YWN0bHkgbmNvbHMgY29sdW1ucy5cbiAgICAgKi9cbiAgICBjb2x1bW5PZmZzZXRzOiBib29sZWFuO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGRlbGltaXRlciB0byB1c2UuIERlZmF1bHRzIHRvICcsJy5cbiAgICAgKi9cbiAgICBkZWxpbWl0ZXI/OiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgcm93IGRlbGltaXRlciB0byB1c2UuIERlZmF1bHRzIHRvICdcXHJcXG4nLlxuICAgICAqL1xuICAgIHJvd0RlbGltaXRlcj86IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFRoZSBxdW90ZSBjaGFyYWN0ZXIgZm9yIHF1b3RpbmcgZmllbGRzLiBEZWZhdWx0cyB0byB0aGUgZG91YmxlIHF1b3RlIChcIikuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogQXMgc3BlY2lmaWVkIGluIFtSRkMgNDE4MF0oaHR0cHM6Ly90b29scy5pZXRmLm9yZy9odG1sL3JmYzQxODApLCBxdW90ZXNcbiAgICAgKiBhcmUgZXNjYXBlZCBpbiBhIHF1b3RlZCBmaWVsZCBieSBkb3VibGluZyB0aGVtIChmb3IgZXhhbXBsZSwgXCJhXCJcImJcIiBpcyB0aGUgZmllbGRcbiAgICAgKiBhXCJiKS5cbiAgICAgKi9cbiAgICBxdW90ZT86IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFRoZSBzdGFydGluZyBpbmRleCBpbiB0aGUgc3RyaW5nIGZvciBwcm9jZXNzaW5nLiBEZWZhdWx0cyB0byAwLiBUaGlzXG4gICAgICogaW5kZXggc2hvdWxkIGJlIHRoZSBmaXJzdCBjaGFyYWN0ZXIgb2YgYSBuZXcgcm93LiBUaGlzIG11c3QgYmUgbGVzcyB0aGFuXG4gICAgICogZGF0YS5sZW5ndGguXG4gICAgICovXG4gICAgc3RhcnRJbmRleD86IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIE1heGltdW0gbnVtYmVyIG9mIHJvd3MgdG8gcGFyc2UuXG4gICAgICpcbiAgICAgKiBJZiB0aGlzIGlzIG5vdCBnaXZlbiwgcGFyc2luZyBwcm9jZWVkcyB0byB0aGUgZW5kIG9mIHRoZSBkYXRhLlxuICAgICAqL1xuICAgIG1heFJvd3M/OiBudW1iZXI7XG5cbiAgICAvKipcbiAgICAgKiBOdW1iZXIgb2YgY29sdW1ucyBpbiBlYWNoIHJvdyB0byBwYXJzZS5cbiAgICAgKlxuICAgICAqICMjIyMgTm90ZXNcbiAgICAgKiBJZiB0aGlzIGlzIG5vdCBnaXZlbiwgdGhlIG5jb2xzIGRlZmF1bHRzIHRvIHRoZSBudW1iZXIgb2YgY29sdW1ucyBpbiB0aGVcbiAgICAgKiBmaXJzdCByb3cuXG4gICAgICovXG4gICAgbmNvbHM/OiBudW1iZXI7XG4gIH1cblxuICAvKipcbiAgICogVGhlIHJlc3VsdHMgZnJvbSBhIHBhcnNlci5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSVJlc3VsdHMge1xuICAgIC8qKlxuICAgICAqIFRoZSBudW1iZXIgb2Ygcm93cyBwYXJzZWQuXG4gICAgICovXG4gICAgbnJvd3M6IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBudW1iZXIgb2YgY29sdW1ucyBwYXJzZWQsIG9yIDAgaWYgb25seSByb3cgb2Zmc2V0cyBhcmUgcmV0dXJuZWQuXG4gICAgICovXG4gICAgbmNvbHM6IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBpbmRleCBvZmZzZXRzIGludG8gdGhlIGRhdGEgc3RyaW5nIGZvciB0aGUgcm93cyBvciBkYXRhIGl0ZW1zLlxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIElmIHRoZSBjb2x1bW5PZmZzZXRzIGFyZ3VtZW50IHRvIHRoZSBwYXJzZXIgaXMgZmFsc2UsIHRoZSBvZmZzZXRzIGFycmF5XG4gICAgICogd2lsbCBiZSBhbiBhcnJheSBvZiBsZW5ndGggbnJvd3MsIHdoZXJlIGBvZmZzZXRzW3JdYCBpcyB0aGUgaW5kZXggb2YgdGhlXG4gICAgICogZmlyc3QgY2hhcmFjdGVyIG9mIHJvdyByLlxuICAgICAqXG4gICAgICogSWYgdGhlIGNvbHVtbk9mZnNldHMgYXJndW1lbnQgdG8gdGhlIHBhcnNlciBpcyB0cnVlLCB0aGUgb2Zmc2V0cyBhcnJheVxuICAgICAqIHdpbGwgYmUgYW4gYXJyYXkgb2YgbGVuZ3RoIGBucm93cypuY29sc2AsIHdoZXJlIGBvZmZzZXRzW3IqbmNvbHMgKyBjXWAgaXNcbiAgICAgKiB0aGUgaW5kZXggb2YgdGhlIGZpcnN0IGNoYXJhY3RlciBvZiB0aGUgaXRlbSBpbiByb3cgciwgY29sdW1uIGMuXG4gICAgICovXG4gICAgb2Zmc2V0czogbnVtYmVyW107XG4gIH1cbn1cblxuLyoqXG4gKiBQb3NzaWJsZSBwYXJzZXIgc3RhdGVzLlxuICovXG5lbnVtIFNUQVRFIHtcbiAgUVVPVEVEX0ZJRUxELFxuICBRVU9URURfRklFTERfUVVPVEUsXG4gIFVOUVVPVEVEX0ZJRUxELFxuICBORVdfRklFTEQsXG4gIE5FV19ST1dcbn1cblxuLyoqXG4gKiBQb3NzaWJsZSByb3cgZGVsaW1pdGVycyBmb3IgdGhlIHBhcnNlci5cbiAqL1xuZW51bSBST1dfREVMSU1JVEVSIHtcbiAgQ1IsXG4gIENSTEYsXG4gIExGXG59XG5cbi8qKlxuICogUGFyc2UgZGVsaW1pdGVyLXNlcGFyYXRlZCBkYXRhLlxuICpcbiAqIEBwYXJhbSBvcHRpb25zOiBUaGUgcGFyc2VyIG9wdGlvbnNcbiAqIEByZXR1cm5zIEFuIG9iamVjdCBnaXZpbmcgdGhlIG9mZnNldHMgZm9yIHRoZSByb3dzIG9yIGNvbHVtbnMgcGFyc2VkLlxuICpcbiAqICMjIyMgTm90ZXNcbiAqIFRoaXMgaW1wbGVtZW50YXRpb24gaXMgYmFzZWQgb24gW1JGQyA0MTgwXShodHRwczovL3Rvb2xzLmlldGYub3JnL2h0bWwvcmZjNDE4MCkuXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiBwYXJzZURTVihvcHRpb25zOiBJUGFyc2VyLklPcHRpb25zKTogSVBhcnNlci5JUmVzdWx0cyB7XG4gIGNvbnN0IHtcbiAgICBkYXRhLFxuICAgIGNvbHVtbk9mZnNldHMsXG4gICAgZGVsaW1pdGVyID0gJywnLFxuICAgIHN0YXJ0SW5kZXggPSAwLFxuICAgIG1heFJvd3MgPSAweGZmZmZmZmZmLFxuICAgIHJvd0RlbGltaXRlciA9ICdcXHJcXG4nLFxuICAgIHF1b3RlID0gJ1wiJ1xuICB9ID0gb3B0aW9ucztcblxuICAvLyBuY29scyB3aWxsIGJlIHNldCBhdXRvbWF0aWNhbGx5IGlmIGl0IGlzIHVuZGVmaW5lZC5cbiAgbGV0IG5jb2xzID0gb3B0aW9ucy5uY29scztcblxuICAvLyBUaGUgbnVtYmVyIG9mIHJvd3Mgd2UndmUgYWxyZWFkeSBwYXJzZWQuXG4gIGxldCBucm93cyA9IDA7XG5cbiAgLy8gVGhlIHJvdyBvciBjb2x1bW4gb2Zmc2V0cyB3ZSByZXR1cm4uXG4gIGNvbnN0IG9mZnNldHMgPSBbXTtcblxuICAvLyBTZXQgdXAgc29tZSB1c2VmdWwgbG9jYWwgdmFyaWFibGVzLlxuICBjb25zdCBDSF9ERUxJTUlURVIgPSBkZWxpbWl0ZXIuY2hhckNvZGVBdCgwKTtcbiAgY29uc3QgQ0hfUVVPVEUgPSBxdW90ZS5jaGFyQ29kZUF0KDApO1xuICBjb25zdCBDSF9MRiA9IDEwOyAvLyBcXG5cbiAgY29uc3QgQ0hfQ1IgPSAxMzsgLy8gXFxyXG4gIGNvbnN0IGVuZEluZGV4ID0gZGF0YS5sZW5ndGg7XG4gIGNvbnN0IHtcbiAgICBRVU9URURfRklFTEQsXG4gICAgUVVPVEVEX0ZJRUxEX1FVT1RFLFxuICAgIFVOUVVPVEVEX0ZJRUxELFxuICAgIE5FV19GSUVMRCxcbiAgICBORVdfUk9XXG4gIH0gPSBTVEFURTtcbiAgY29uc3QgeyBDUiwgTEYsIENSTEYgfSA9IFJPV19ERUxJTUlURVI7XG4gIGNvbnN0IFtyb3dEZWxpbWl0ZXJDb2RlLCByb3dEZWxpbWl0ZXJMZW5ndGhdID1cbiAgICByb3dEZWxpbWl0ZXIgPT09ICdcXHJcXG4nXG4gICAgICA/IFtDUkxGLCAyXVxuICAgICAgOiByb3dEZWxpbWl0ZXIgPT09ICdcXHInXG4gICAgICA/IFtDUiwgMV1cbiAgICAgIDogW0xGLCAxXTtcblxuICAvLyBBbHdheXMgc3RhcnQgb2ZmIGF0IHRoZSBiZWdpbm5pbmcgb2YgYSByb3cuXG4gIGxldCBzdGF0ZSA9IE5FV19ST1c7XG5cbiAgLy8gU2V0IHVwIHRoZSBzdGFydGluZyBpbmRleC5cbiAgbGV0IGkgPSBzdGFydEluZGV4O1xuXG4gIC8vIFdlIGluaXRpYWxpemUgdG8gMCBqdXN0IGluIGNhc2Ugd2UgYXJlIGFza2VkIHRvIHBhcnNlIHBhc3QgdGhlIGVuZCBvZiB0aGVcbiAgLy8gc3RyaW5nLiBJbiB0aGF0IGNhc2UsIHdlIHdhbnQgdGhlIG51bWJlciBvZiBjb2x1bW5zIHRvIGJlIDAuXG4gIGxldCBjb2wgPSAwO1xuXG4gIC8vIERlY2xhcmUgc29tZSB1c2VmdWwgdGVtcG9yYXJpZXNcbiAgbGV0IGNoYXI7XG5cbiAgLy8gTG9vcCB0aHJvdWdoIHRoZSBkYXRhIHN0cmluZ1xuICB3aGlsZSAoaSA8IGVuZEluZGV4KSB7XG4gICAgLy8gaSBpcyB0aGUgaW5kZXggb2YgYSBjaGFyYWN0ZXIgaW4gdGhlIHN0YXRlLlxuXG4gICAgLy8gSWYgd2UganVzdCBoaXQgYSBuZXcgcm93LCBhbmQgdGhlcmUgYXJlIHN0aWxsIGNoYXJhY3RlcnMgbGVmdCwgcHVzaCBhIG5ld1xuICAgIC8vIG9mZnNldCBvbiBhbmQgcmVzZXQgdGhlIGNvbHVtbiBjb3VudGVyLiBXZSB3YW50IHRoaXMgbG9naWMgYXQgdGhlIHRvcCBvZlxuICAgIC8vIHRoZSB3aGlsZSBsb29wIHJhdGhlciB0aGFuIHRoZSBib3R0b20gYmVjYXVzZSB3ZSBkb24ndCB3YW50IGEgdHJhaWxpbmdcbiAgICAvLyByb3cgZGVsaW1pdGVyIGF0IHRoZSBlbmQgb2YgdGhlIGRhdGEgdG8gdHJpZ2dlciBhIG5ldyByb3cgb2Zmc2V0LlxuICAgIGlmIChzdGF0ZSA9PT0gTkVXX1JPVykge1xuICAgICAgLy8gU3RhcnQgYSBuZXcgcm93IGFuZCByZXNldCB0aGUgY29sdW1uIGNvdW50ZXIuXG4gICAgICBvZmZzZXRzLnB1c2goaSk7XG4gICAgICBjb2wgPSAxO1xuICAgIH1cblxuICAgIC8vIEJlbG93LCB3ZSBoYW5kbGUgdGhpcyBjaGFyYWN0ZXIsIG1vZGlmeSB0aGUgcGFyc2VyIHN0YXRlIGFuZCBpbmNyZW1lbnQgdGhlIGluZGV4IHRvIGJlIGNvbnNpc3RlbnQuXG5cbiAgICAvLyBHZXQgdGhlIGludGVnZXIgY29kZSBmb3IgdGhlIGN1cnJlbnQgY2hhcmFjdGVyLCBzbyB0aGUgY29tcGFyaXNvbnMgYmVsb3dcbiAgICAvLyBhcmUgZmFzdGVyLlxuICAgIGNoYXIgPSBkYXRhLmNoYXJDb2RlQXQoaSk7XG5cbiAgICAvLyBVcGRhdGUgdGhlIHBhcnNlciBzdGF0ZS4gVGhpcyBzd2l0Y2ggc3RhdGVtZW50IGlzIHJlc3BvbnNpYmxlIGZvclxuICAgIC8vIHVwZGF0aW5nIHRoZSBzdGF0ZSB0byBiZSBjb25zaXN0ZW50IHdpdGggdGhlIGluZGV4IGkrMSAod2UgaW5jcmVtZW50IGlcbiAgICAvLyBhZnRlciB0aGUgc3dpdGNoIHN0YXRlbWVudCkuIEluIHNvbWUgc2l0dWF0aW9ucywgd2UgbWF5IGluY3JlbWVudCBpXG4gICAgLy8gaW5zaWRlIHRoaXMgbG9vcCB0byBza2lwIG92ZXIgaW5kaWNlcyBhcyBhIHNob3J0Y3V0LlxuICAgIHN3aXRjaCAoc3RhdGUpIHtcbiAgICAgIC8vIEF0IHRoZSBiZWdpbm5pbmcgb2YgYSByb3cgb3IgZmllbGQsIHdlIGNhbiBoYXZlIGEgcXVvdGUsIHJvdyBkZWxpbWl0ZXIsIG9yIGZpZWxkIGRlbGltaXRlci5cbiAgICAgIGNhc2UgTkVXX1JPVzpcbiAgICAgIGNhc2UgTkVXX0ZJRUxEOlxuICAgICAgICBzd2l0Y2ggKGNoYXIpIHtcbiAgICAgICAgICAvLyBJZiB3ZSBoYXZlIGEgcXVvdGUsIHdlIGFyZSBzdGFydGluZyBhbiBlc2NhcGVkIGZpZWxkLlxuICAgICAgICAgIGNhc2UgQ0hfUVVPVEU6XG4gICAgICAgICAgICBzdGF0ZSA9IFFVT1RFRF9GSUVMRDtcbiAgICAgICAgICAgIGJyZWFrO1xuXG4gICAgICAgICAgLy8gQSBmaWVsZCBkZWxpbWl0ZXIgbWVhbnMgd2UgYXJlIHN0YXJ0aW5nIGEgbmV3IGZpZWxkLlxuICAgICAgICAgIGNhc2UgQ0hfREVMSU1JVEVSOlxuICAgICAgICAgICAgc3RhdGUgPSBORVdfRklFTEQ7XG4gICAgICAgICAgICBicmVhaztcblxuICAgICAgICAgIC8vIEEgcm93IGRlbGltaXRlciBtZWFucyB3ZSBhcmUgc3RhcnRpbmcgYSBuZXcgcm93LlxuICAgICAgICAgIGNhc2UgQ0hfQ1I6XG4gICAgICAgICAgICBpZiAocm93RGVsaW1pdGVyQ29kZSA9PT0gQ1IpIHtcbiAgICAgICAgICAgICAgc3RhdGUgPSBORVdfUk9XO1xuICAgICAgICAgICAgfSBlbHNlIGlmIChcbiAgICAgICAgICAgICAgcm93RGVsaW1pdGVyQ29kZSA9PT0gQ1JMRiAmJlxuICAgICAgICAgICAgICBkYXRhLmNoYXJDb2RlQXQoaSArIDEpID09PSBDSF9MRlxuICAgICAgICAgICAgKSB7XG4gICAgICAgICAgICAgIC8vIElmIHdlIHNlZSBhbiBleHBlY3RlZCBcXHJcXG4sIHRoZW4gaW5jcmVtZW50IHRvIHRoZSBlbmQgb2YgdGhlIGRlbGltaXRlci5cbiAgICAgICAgICAgICAgaSsrO1xuICAgICAgICAgICAgICBzdGF0ZSA9IE5FV19ST1c7XG4gICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICB0aHJvdyBgc3RyaW5nIGluZGV4ICR7aX0gKGluIHJvdyAke25yb3dzfSwgY29sdW1uICR7Y29sfSk6IGNhcnJpYWdlIHJldHVybiBmb3VuZCwgYnV0IG5vdCBhcyBwYXJ0IG9mIGEgcm93IGRlbGltaXRlciBDICR7ZGF0YS5jaGFyQ29kZUF0KFxuICAgICAgICAgICAgICAgIGkgKyAxXG4gICAgICAgICAgICAgICl9YDtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICAgIGNhc2UgQ0hfTEY6XG4gICAgICAgICAgICBpZiAocm93RGVsaW1pdGVyQ29kZSA9PT0gTEYpIHtcbiAgICAgICAgICAgICAgc3RhdGUgPSBORVdfUk9XO1xuICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgdGhyb3cgYHN0cmluZyBpbmRleCAke2l9IChpbiByb3cgJHtucm93c30sIGNvbHVtbiAke2NvbH0pOiBsaW5lIGZlZWQgZm91bmQsIGJ1dCByb3cgZGVsaW1pdGVyIHN0YXJ0cyB3aXRoIGEgY2FycmlhZ2UgcmV0dXJuYDtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIGJyZWFrO1xuXG4gICAgICAgICAgLy8gT3RoZXJ3aXNlLCB3ZSBhcmUgc3RhcnRpbmcgYW4gdW5xdW90ZWQgZmllbGQuXG4gICAgICAgICAgZGVmYXVsdDpcbiAgICAgICAgICAgIHN0YXRlID0gVU5RVU9URURfRklFTEQ7XG4gICAgICAgICAgICBicmVhaztcbiAgICAgICAgfVxuICAgICAgICBicmVhaztcblxuICAgICAgLy8gV2UgYXJlIGluIGEgcXVvdGVkIGZpZWxkLlxuICAgICAgY2FzZSBRVU9URURfRklFTEQ6XG4gICAgICAgIC8vIFNraXAgYWhlYWQgdW50aWwgd2Ugc2VlIGFub3RoZXIgcXVvdGUsIHdoaWNoIGVpdGhlciBlbmRzIHRoZSBxdW90ZWRcbiAgICAgICAgLy8gZmllbGQgb3Igc3RhcnRzIGFuIGVzY2FwZWQgcXVvdGUuXG4gICAgICAgIGkgPSBkYXRhLmluZGV4T2YocXVvdGUsIGkpO1xuICAgICAgICBpZiAoaSA8IDApIHtcbiAgICAgICAgICB0aHJvdyBgc3RyaW5nIGluZGV4ICR7aX0gKGluIHJvdyAke25yb3dzfSwgY29sdW1uICR7Y29sfSk6IG1pc21hdGNoZWQgcXVvdGVgO1xuICAgICAgICB9XG4gICAgICAgIHN0YXRlID0gUVVPVEVEX0ZJRUxEX1FVT1RFO1xuICAgICAgICBicmVhaztcblxuICAgICAgLy8gV2UganVzdCBzYXcgYSBxdW90ZSBpbiBhIHF1b3RlZCBmaWVsZC4gVGhpcyBjb3VsZCBiZSB0aGUgZW5kIG9mIHRoZVxuICAgICAgLy8gZmllbGQsIG9yIGl0IGNvdWxkIGJlIGEgcmVwZWF0ZWQgcXVvdGUgKGkuZS4sIGFuIGVzY2FwZWQgcXVvdGUgYWNjb3JkaW5nXG4gICAgICAvLyB0byBSRkMgNDE4MCkuXG4gICAgICBjYXNlIFFVT1RFRF9GSUVMRF9RVU9URTpcbiAgICAgICAgc3dpdGNoIChjaGFyKSB7XG4gICAgICAgICAgLy8gQW5vdGhlciBxdW90ZSBtZWFucyB3ZSBqdXN0IHNhdyBhbiBlc2NhcGVkIHF1b3RlLCBzbyB3ZSBhcmUgc3RpbGwgaW5cbiAgICAgICAgICAvLyB0aGUgcXVvdGVkIGZpZWxkLlxuICAgICAgICAgIGNhc2UgQ0hfUVVPVEU6XG4gICAgICAgICAgICBzdGF0ZSA9IFFVT1RFRF9GSUVMRDtcbiAgICAgICAgICAgIGJyZWFrO1xuXG4gICAgICAgICAgLy8gQSBmaWVsZCBvciByb3cgZGVsaW1pdGVyIG1lYW5zIHRoZSBxdW90ZWQgZmllbGQganVzdCBlbmRlZCBhbmQgd2UgYXJlXG4gICAgICAgICAgLy8gZ29pbmcgaW50byBhIG5ldyBmaWVsZCBvciBuZXcgcm93LlxuICAgICAgICAgIGNhc2UgQ0hfREVMSU1JVEVSOlxuICAgICAgICAgICAgc3RhdGUgPSBORVdfRklFTEQ7XG4gICAgICAgICAgICBicmVhaztcblxuICAgICAgICAgIC8vIEEgcm93IGRlbGltaXRlciBtZWFucyB3ZSBhcmUgc3RhcnRpbmcgYSBuZXcgcm93IGluIHRoZSBuZXh0IGluZGV4LlxuICAgICAgICAgIGNhc2UgQ0hfQ1I6XG4gICAgICAgICAgICBpZiAocm93RGVsaW1pdGVyQ29kZSA9PT0gQ1IpIHtcbiAgICAgICAgICAgICAgc3RhdGUgPSBORVdfUk9XO1xuICAgICAgICAgICAgfSBlbHNlIGlmIChcbiAgICAgICAgICAgICAgcm93RGVsaW1pdGVyQ29kZSA9PT0gQ1JMRiAmJlxuICAgICAgICAgICAgICBkYXRhLmNoYXJDb2RlQXQoaSArIDEpID09PSBDSF9MRlxuICAgICAgICAgICAgKSB7XG4gICAgICAgICAgICAgIC8vIElmIHdlIHNlZSBhbiBleHBlY3RlZCBcXHJcXG4sIHRoZW4gaW5jcmVtZW50IHRvIHRoZSBlbmQgb2YgdGhlIGRlbGltaXRlci5cbiAgICAgICAgICAgICAgaSsrO1xuICAgICAgICAgICAgICBzdGF0ZSA9IE5FV19ST1c7XG4gICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICB0aHJvdyBgc3RyaW5nIGluZGV4ICR7aX0gKGluIHJvdyAke25yb3dzfSwgY29sdW1uICR7Y29sfSk6IGNhcnJpYWdlIHJldHVybiBmb3VuZCwgYnV0IG5vdCBhcyBwYXJ0IG9mIGEgcm93IGRlbGltaXRlciBDICR7ZGF0YS5jaGFyQ29kZUF0KFxuICAgICAgICAgICAgICAgIGkgKyAxXG4gICAgICAgICAgICAgICl9YDtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICAgIGNhc2UgQ0hfTEY6XG4gICAgICAgICAgICBpZiAocm93RGVsaW1pdGVyQ29kZSA9PT0gTEYpIHtcbiAgICAgICAgICAgICAgc3RhdGUgPSBORVdfUk9XO1xuICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgdGhyb3cgYHN0cmluZyBpbmRleCAke2l9IChpbiByb3cgJHtucm93c30sIGNvbHVtbiAke2NvbH0pOiBsaW5lIGZlZWQgZm91bmQsIGJ1dCByb3cgZGVsaW1pdGVyIHN0YXJ0cyB3aXRoIGEgY2FycmlhZ2UgcmV0dXJuYDtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIGJyZWFrO1xuXG4gICAgICAgICAgZGVmYXVsdDpcbiAgICAgICAgICAgIHRocm93IGBzdHJpbmcgaW5kZXggJHtpfSAoaW4gcm93ICR7bnJvd3N9LCBjb2x1bW4gJHtjb2x9KTogcXVvdGUgaW4gZXNjYXBlZCBmaWVsZCBub3QgZm9sbG93ZWQgYnkgcXVvdGUsIGRlbGltaXRlciwgb3Igcm93IGRlbGltaXRlcmA7XG4gICAgICAgIH1cbiAgICAgICAgYnJlYWs7XG5cbiAgICAgIC8vIFdlIGFyZSBpbiBhbiB1bnF1b3RlZCBmaWVsZCwgc28gdGhlIG9ubHkgdGhpbmcgd2UgbG9vayBmb3IgaXMgdGhlIG5leHRcbiAgICAgIC8vIHJvdyBvciBmaWVsZCBkZWxpbWl0ZXIuXG4gICAgICBjYXNlIFVOUVVPVEVEX0ZJRUxEOlxuICAgICAgICAvLyBTa2lwIGFoZWFkIHRvIGVpdGhlciB0aGUgbmV4dCBmaWVsZCBkZWxpbWl0ZXIgb3IgcG9zc2libGUgc3RhcnQgb2YgYVxuICAgICAgICAvLyByb3cgZGVsaW1pdGVyIChDUiBvciBMRikuXG4gICAgICAgIHdoaWxlIChpIDwgZW5kSW5kZXgpIHtcbiAgICAgICAgICBjaGFyID0gZGF0YS5jaGFyQ29kZUF0KGkpO1xuICAgICAgICAgIGlmIChjaGFyID09PSBDSF9ERUxJTUlURVIgfHwgY2hhciA9PT0gQ0hfTEYgfHwgY2hhciA9PT0gQ0hfQ1IpIHtcbiAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICAgIH1cbiAgICAgICAgICBpKys7XG4gICAgICAgIH1cblxuICAgICAgICAvLyBQcm9jZXNzIHRoZSBjaGFyYWN0ZXIgd2UncmUgc2VlaW5nIGluIGFuIHVucXVvdGVkIGZpZWxkLlxuICAgICAgICBzd2l0Y2ggKGNoYXIpIHtcbiAgICAgICAgICAvLyBBIGZpZWxkIGRlbGltaXRlciBtZWFucyB3ZSBhcmUgc3RhcnRpbmcgYSBuZXcgZmllbGQuXG4gICAgICAgICAgY2FzZSBDSF9ERUxJTUlURVI6XG4gICAgICAgICAgICBzdGF0ZSA9IE5FV19GSUVMRDtcbiAgICAgICAgICAgIGJyZWFrO1xuXG4gICAgICAgICAgLy8gQSByb3cgZGVsaW1pdGVyIG1lYW5zIHdlIGFyZSBzdGFydGluZyBhIG5ldyByb3cgaW4gdGhlIG5leHQgaW5kZXguXG4gICAgICAgICAgY2FzZSBDSF9DUjpcbiAgICAgICAgICAgIGlmIChyb3dEZWxpbWl0ZXJDb2RlID09PSBDUikge1xuICAgICAgICAgICAgICBzdGF0ZSA9IE5FV19ST1c7XG4gICAgICAgICAgICB9IGVsc2UgaWYgKFxuICAgICAgICAgICAgICByb3dEZWxpbWl0ZXJDb2RlID09PSBDUkxGICYmXG4gICAgICAgICAgICAgIGRhdGEuY2hhckNvZGVBdChpICsgMSkgPT09IENIX0xGXG4gICAgICAgICAgICApIHtcbiAgICAgICAgICAgICAgLy8gSWYgd2Ugc2VlIGFuIGV4cGVjdGVkIFxcclxcbiwgdGhlbiBpbmNyZW1lbnQgdG8gdGhlIGVuZCBvZiB0aGUgZGVsaW1pdGVyLlxuICAgICAgICAgICAgICBpKys7XG4gICAgICAgICAgICAgIHN0YXRlID0gTkVXX1JPVztcbiAgICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICAgIHRocm93IGBzdHJpbmcgaW5kZXggJHtpfSAoaW4gcm93ICR7bnJvd3N9LCBjb2x1bW4gJHtjb2x9KTogY2FycmlhZ2UgcmV0dXJuIGZvdW5kLCBidXQgbm90IGFzIHBhcnQgb2YgYSByb3cgZGVsaW1pdGVyIEMgJHtkYXRhLmNoYXJDb2RlQXQoXG4gICAgICAgICAgICAgICAgaSArIDFcbiAgICAgICAgICAgICAgKX1gO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgYnJlYWs7XG4gICAgICAgICAgY2FzZSBDSF9MRjpcbiAgICAgICAgICAgIGlmIChyb3dEZWxpbWl0ZXJDb2RlID09PSBMRikge1xuICAgICAgICAgICAgICBzdGF0ZSA9IE5FV19ST1c7XG4gICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICB0aHJvdyBgc3RyaW5nIGluZGV4ICR7aX0gKGluIHJvdyAke25yb3dzfSwgY29sdW1uICR7Y29sfSk6IGxpbmUgZmVlZCBmb3VuZCwgYnV0IHJvdyBkZWxpbWl0ZXIgc3RhcnRzIHdpdGggYSBjYXJyaWFnZSByZXR1cm5gO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgYnJlYWs7XG5cbiAgICAgICAgICAvLyBPdGhlcndpc2UsIHdlIGNvbnRpbnVlIG9uIGluIHRoZSB1bnF1b3RlZCBmaWVsZC5cbiAgICAgICAgICBkZWZhdWx0OlxuICAgICAgICAgICAgY29udGludWU7XG4gICAgICAgIH1cbiAgICAgICAgYnJlYWs7XG5cbiAgICAgIC8vIFdlIHNob3VsZCBuZXZlciByZWFjaCB0aGlzIHBvaW50IHNpbmNlIHRoZSBwYXJzZXIgc3RhdGUgaXMgaGFuZGxlZCBhYm92ZSxcbiAgICAgIC8vIHNvIHRocm93IGFuIGVycm9yIGlmIHdlIGRvLlxuICAgICAgZGVmYXVsdDpcbiAgICAgICAgdGhyb3cgYHN0cmluZyBpbmRleCAke2l9IChpbiByb3cgJHtucm93c30sIGNvbHVtbiAke2NvbH0pOiBzdGF0ZSBub3QgcmVjb2duaXplZGA7XG4gICAgfVxuXG4gICAgLy8gSW5jcmVtZW50IGkgdG8gdGhlIG5leHQgY2hhcmFjdGVyIGluZGV4XG4gICAgaSsrO1xuXG4gICAgLy8gVXBkYXRlIHJldHVybiB2YWx1ZXMgYmFzZWQgb24gc3RhdGUuXG4gICAgc3dpdGNoIChzdGF0ZSkge1xuICAgICAgY2FzZSBORVdfUk9XOlxuICAgICAgICBucm93cysrO1xuXG4gICAgICAgIC8vIElmIG5jb2xzIGlzIHVuZGVmaW5lZCwgc2V0IGl0IHRvIHRoZSBudW1iZXIgb2YgY29sdW1ucyBpbiB0aGlzIHJvdyAoZmlyc3Qgcm93IGltcGxpZWQpLlxuICAgICAgICBpZiAobmNvbHMgPT09IHVuZGVmaW5lZCkge1xuICAgICAgICAgIGlmIChucm93cyAhPT0gMSkge1xuICAgICAgICAgICAgdGhyb3cgbmV3IEVycm9yKCdFcnJvciBwYXJzaW5nIGRlZmF1bHQgbnVtYmVyIG9mIGNvbHVtbnMnKTtcbiAgICAgICAgICB9XG4gICAgICAgICAgbmNvbHMgPSBjb2w7XG4gICAgICAgIH1cblxuICAgICAgICAvLyBQYWQgb3IgdHJ1bmNhdGUgdGhlIGNvbHVtbiBvZmZzZXRzIGluIHRoZSBwcmV2aW91cyByb3cgaWYgd2UgYXJlXG4gICAgICAgIC8vIHJldHVybmluZyB0aGVtLlxuICAgICAgICBpZiAoY29sdW1uT2Zmc2V0cyA9PT0gdHJ1ZSkge1xuICAgICAgICAgIGlmIChjb2wgPCBuY29scykge1xuICAgICAgICAgICAgLy8gV2UgZGlkbid0IGhhdmUgZW5vdWdoIGNvbHVtbnMsIHNvIGFkZCBzb21lIG1vcmUgY29sdW1uIG9mZnNldHMgdGhhdFxuICAgICAgICAgICAgLy8gcG9pbnQgdG8ganVzdCBiZWZvcmUgdGhlIHJvdyBkZWxpbWl0ZXIgd2UganVzdCBzYXcuXG4gICAgICAgICAgICBmb3IgKDsgY29sIDwgbmNvbHM7IGNvbCsrKSB7XG4gICAgICAgICAgICAgIG9mZnNldHMucHVzaChpIC0gcm93RGVsaW1pdGVyTGVuZ3RoKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICB9IGVsc2UgaWYgKGNvbCA+IG5jb2xzKSB7XG4gICAgICAgICAgICAvLyBXZSBoYWQgdG9vIG1hbnkgY29sdW1ucywgc28gdHJ1bmNhdGUgdGhlbS5cbiAgICAgICAgICAgIG9mZnNldHMubGVuZ3RoID0gb2Zmc2V0cy5sZW5ndGggLSAoY29sIC0gbmNvbHMpO1xuICAgICAgICAgIH1cbiAgICAgICAgfVxuXG4gICAgICAgIC8vIFNob3J0Y3V0IHJldHVybiBpZiBucm93cyByZWFjaGVzIHRoZSBtYXhpbXVtIHJvd3Mgd2UgYXJlIHRvIHBhcnNlLlxuICAgICAgICBpZiAobnJvd3MgPT09IG1heFJvd3MpIHtcbiAgICAgICAgICByZXR1cm4geyBucm93cywgbmNvbHM6IGNvbHVtbk9mZnNldHMgPyBuY29scyA6IDAsIG9mZnNldHMgfTtcbiAgICAgICAgfVxuICAgICAgICBicmVhaztcblxuICAgICAgY2FzZSBORVdfRklFTEQ6XG4gICAgICAgIC8vIElmIHdlIGFyZSByZXR1cm5pbmcgY29sdW1uIG9mZnNldHMsIGxvZyB0aGUgY3VycmVudCBpbmRleC5cbiAgICAgICAgaWYgKGNvbHVtbk9mZnNldHMgPT09IHRydWUpIHtcbiAgICAgICAgICBvZmZzZXRzLnB1c2goaSk7XG4gICAgICAgIH1cblxuICAgICAgICAvLyBVcGRhdGUgdGhlIGNvbHVtbiBjb3VudGVyLlxuICAgICAgICBjb2wrKztcbiAgICAgICAgYnJlYWs7XG5cbiAgICAgIGRlZmF1bHQ6XG4gICAgICAgIGJyZWFrO1xuICAgIH1cbiAgfVxuXG4gIC8vIElmIHdlIGZpbmlzaGVkIHBhcnNpbmcgYW5kIHdlIGFyZSAqbm90KiBpbiB0aGUgTkVXX1JPVyBzdGF0ZSwgdGhlbiBkbyB0aGVcbiAgLy8gY29sdW1uIHBhZGRpbmcvdHJ1bmNhdGlvbiBmb3IgdGhlIGxhc3Qgcm93LiBBbHNvIG1ha2Ugc3VyZSBuY29scyBpc1xuICAvLyBkZWZpbmVkLlxuICBpZiAoc3RhdGUgIT09IE5FV19ST1cpIHtcbiAgICBucm93cysrO1xuICAgIGlmIChjb2x1bW5PZmZzZXRzID09PSB0cnVlKSB7XG4gICAgICAvLyBJZiBuY29scyBpcyAqc3RpbGwqIHVuZGVmaW5lZCwgdGhlbiB3ZSBvbmx5IHBhcnNlZCBvbmUgcm93IGFuZCBkaWRuJ3RcbiAgICAgIC8vIGhhdmUgYSBuZXdsaW5lLCBzbyBzZXQgaXQgdG8gdGhlIG51bWJlciBvZiBjb2x1bW5zIHdlIGZvdW5kLlxuICAgICAgaWYgKG5jb2xzID09PSB1bmRlZmluZWQpIHtcbiAgICAgICAgbmNvbHMgPSBjb2w7XG4gICAgICB9XG5cbiAgICAgIGlmIChjb2wgPCBuY29scykge1xuICAgICAgICAvLyBXZSBkaWRuJ3QgaGF2ZSBlbm91Z2ggY29sdW1ucywgc28gYWRkIHNvbWUgbW9yZSBjb2x1bW4gb2Zmc2V0cyB0aGF0XG4gICAgICAgIC8vIHBvaW50IHRvIGp1c3QgYmVmb3JlIHRoZSByb3cgZGVsaW1pdGVyIHdlIGp1c3Qgc2F3LlxuICAgICAgICBmb3IgKDsgY29sIDwgbmNvbHM7IGNvbCsrKSB7XG4gICAgICAgICAgb2Zmc2V0cy5wdXNoKGkgLSAocm93RGVsaW1pdGVyTGVuZ3RoIC0gMSkpO1xuICAgICAgICB9XG4gICAgICB9IGVsc2UgaWYgKGNvbCA+IG5jb2xzKSB7XG4gICAgICAgIC8vIFdlIGhhZCB0b28gbWFueSBjb2x1bW5zLCBzbyB0cnVuY2F0ZSB0aGVtLlxuICAgICAgICBvZmZzZXRzLmxlbmd0aCA9IG9mZnNldHMubGVuZ3RoIC0gKGNvbCAtIG5jb2xzKTtcbiAgICAgIH1cbiAgICB9XG4gIH1cblxuICByZXR1cm4geyBucm93cywgbmNvbHM6IGNvbHVtbk9mZnNldHMgPyBuY29scyA/PyAwIDogMCwgb2Zmc2V0cyB9O1xufVxuXG4vKipcbiAqIFBhcnNlIGRlbGltaXRlci1zZXBhcmF0ZWQgZGF0YSB3aGVyZSBubyBkZWxpbWl0ZXIgaXMgcXVvdGVkLlxuICpcbiAqIEBwYXJhbSBvcHRpb25zOiBUaGUgcGFyc2VyIG9wdGlvbnNcbiAqIEByZXR1cm5zIEFuIG9iamVjdCBnaXZpbmcgdGhlIG9mZnNldHMgZm9yIHRoZSByb3dzIG9yIGNvbHVtbnMgcGFyc2VkLlxuICpcbiAqICMjIyMgTm90ZXNcbiAqIFRoaXMgZnVuY3Rpb24gaXMgYW4gb3B0aW1pemVkIHBhcnNlciBmb3IgY2FzZXMgd2hlcmUgdGhlcmUgYXJlIG5vIGZpZWxkIG9yXG4gKiByb3cgZGVsaW1pdGVycyBpbiBxdW90ZXMuIE5vdGUgdGhhdCB0aGUgZGF0YSBjYW4gaGF2ZSBxdW90ZXMsIGJ1dCB0aGV5IGFyZVxuICogbm90IGludGVycHJldGVkIGluIGFueSBzcGVjaWFsIHdheS4gVGhpcyBpbXBsZW1lbnRhdGlvbiBpcyBiYXNlZCBvbiBbUkZDXG4gKiA0MTgwXShodHRwczovL3Rvb2xzLmlldGYub3JnL2h0bWwvcmZjNDE4MCksIGJ1dCBkaXNyZWdhcmRzIHF1b3Rlcy5cbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIHBhcnNlRFNWTm9RdW90ZXMob3B0aW9uczogSVBhcnNlci5JT3B0aW9ucyk6IElQYXJzZXIuSVJlc3VsdHMge1xuICAvLyBTZXQgb3B0aW9uIGRlZmF1bHRzLlxuICBjb25zdCB7XG4gICAgZGF0YSxcbiAgICBjb2x1bW5PZmZzZXRzLFxuICAgIGRlbGltaXRlciA9ICcsJyxcbiAgICByb3dEZWxpbWl0ZXIgPSAnXFxyXFxuJyxcbiAgICBzdGFydEluZGV4ID0gMCxcbiAgICBtYXhSb3dzID0gMHhmZmZmZmZmZlxuICB9ID0gb3B0aW9ucztcblxuICAvLyBuY29scyB3aWxsIGJlIHNldCBhdXRvbWF0aWNhbGx5IGlmIGl0IGlzIHVuZGVmaW5lZC5cbiAgbGV0IG5jb2xzID0gb3B0aW9ucy5uY29scztcblxuICAvLyBTZXQgdXAgb3VyIHJldHVybiB2YXJpYWJsZXMuXG4gIGNvbnN0IG9mZnNldHM6IG51bWJlcltdID0gW107XG4gIGxldCBucm93cyA9IDA7XG5cbiAgLy8gU2V0IHVwIHZhcmlvdXMgc3RhdGUgdmFyaWFibGVzLlxuICBjb25zdCByb3dEZWxpbWl0ZXJMZW5ndGggPSByb3dEZWxpbWl0ZXIubGVuZ3RoO1xuICBsZXQgY3VyclJvdyA9IHN0YXJ0SW5kZXg7XG4gIGNvbnN0IGxlbiA9IGRhdGEubGVuZ3RoO1xuICBsZXQgbmV4dFJvdzogbnVtYmVyO1xuICBsZXQgY29sOiBudW1iZXI7XG4gIGxldCByb3dTdHJpbmc6IHN0cmluZztcbiAgbGV0IGNvbEluZGV4OiBudW1iZXI7XG5cbiAgLy8gVGhlIGVuZCBvZiB0aGUgY3VycmVudCByb3cuXG4gIGxldCByb3dFbmQ6IG51bWJlcjtcblxuICAvLyBTdGFydCBwYXJzaW5nIGF0IHRoZSBzdGFydCBpbmRleC5cbiAgbmV4dFJvdyA9IHN0YXJ0SW5kZXg7XG5cbiAgLy8gTG9vcCB0aHJvdWdoIHJvd3MgdW50aWwgd2UgcnVuIG91dCBvZiBkYXRhIG9yIHdlJ3ZlIHJlYWNoZWQgbWF4Um93cy5cbiAgd2hpbGUgKG5leHRSb3cgIT09IC0xICYmIG5yb3dzIDwgbWF4Um93cyAmJiBjdXJyUm93IDwgbGVuKSB7XG4gICAgLy8gU3RvcmUgdGhlIG9mZnNldCBmb3IgdGhlIGJlZ2lubmluZyBvZiB0aGUgcm93IGFuZCBpbmNyZW1lbnQgdGhlIHJvd3MuXG4gICAgb2Zmc2V0cy5wdXNoKGN1cnJSb3cpO1xuICAgIG5yb3dzKys7XG5cbiAgICAvLyBGaW5kIHRoZSBuZXh0IHJvdyBkZWxpbWl0ZXIuXG4gICAgbmV4dFJvdyA9IGRhdGEuaW5kZXhPZihyb3dEZWxpbWl0ZXIsIGN1cnJSb3cpO1xuXG4gICAgLy8gSWYgdGhlIG5leHQgcm93IGRlbGltaXRlciBpcyBub3QgZm91bmQsIHNldCB0aGUgZW5kIG9mIHRoZSByb3cgdG8gdGhlXG4gICAgLy8gZW5kIG9mIHRoZSBkYXRhIHN0cmluZy5cbiAgICByb3dFbmQgPSBuZXh0Um93ID09PSAtMSA/IGxlbiA6IG5leHRSb3c7XG5cbiAgICAvLyBJZiB3ZSBhcmUgcmV0dXJuaW5nIGNvbHVtbiBvZmZzZXRzLCBwdXNoIHRoZW0gb250byB0aGUgYXJyYXkuXG4gICAgaWYgKGNvbHVtbk9mZnNldHMgPT09IHRydWUpIHtcbiAgICAgIC8vIEZpbmQgdGhlIG5leHQgZmllbGQgZGVsaW1pdGVyLiBXZSBzbGljZSB0aGUgY3VycmVudCByb3cgb3V0IHNvIHRoYXRcbiAgICAgIC8vIHRoZSBpbmRleE9mIHdpbGwgc3RvcCBhdCB0aGUgZW5kIG9mIHRoZSByb3cuIEl0IG1heSBwb3NzaWJseSBiZSBmYXN0ZXJcbiAgICAgIC8vIHRvIGp1c3QgdXNlIGEgbG9vcCB0byBjaGVjayBlYWNoIGNoYXJhY3Rlci5cbiAgICAgIGNvbCA9IDE7XG4gICAgICByb3dTdHJpbmcgPSBkYXRhLnNsaWNlKGN1cnJSb3csIHJvd0VuZCk7XG4gICAgICBjb2xJbmRleCA9IHJvd1N0cmluZy5pbmRleE9mKGRlbGltaXRlcik7XG5cbiAgICAgIGlmIChuY29scyA9PT0gdW5kZWZpbmVkKSB7XG4gICAgICAgIC8vIElmIHdlIGRvbid0IGtub3cgaG93IG1hbnkgY29sdW1ucyB3ZSBuZWVkLCBsb29wIHRocm91Z2ggYW5kIGZpbmQgYWxsXG4gICAgICAgIC8vIG9mIHRoZSBmaWVsZCBkZWxpbWl0ZXJzIGluIHRoaXMgcm93LlxuICAgICAgICB3aGlsZSAoY29sSW5kZXggIT09IC0xKSB7XG4gICAgICAgICAgb2Zmc2V0cy5wdXNoKGN1cnJSb3cgKyBjb2xJbmRleCArIDEpO1xuICAgICAgICAgIGNvbCsrO1xuICAgICAgICAgIGNvbEluZGV4ID0gcm93U3RyaW5nLmluZGV4T2YoZGVsaW1pdGVyLCBjb2xJbmRleCArIDEpO1xuICAgICAgICB9XG5cbiAgICAgICAgLy8gU2V0IG5jb2xzIHRvIHRoZSBudW1iZXIgb2YgZmllbGRzIHdlIGZvdW5kLlxuICAgICAgICBuY29scyA9IGNvbDtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIC8vIElmIHdlIGtub3cgdGhlIG51bWJlciBvZiBjb2x1bW5zIHdlIGV4cGVjdCwgZmluZCB0aGUgZmllbGQgZGVsaW1pdGVyc1xuICAgICAgICAvLyB1cCB0byB0aGF0IG1hbnkgY29sdW1ucy5cbiAgICAgICAgd2hpbGUgKGNvbEluZGV4ICE9PSAtMSAmJiBjb2wgPCBuY29scykge1xuICAgICAgICAgIG9mZnNldHMucHVzaChjdXJyUm93ICsgY29sSW5kZXggKyAxKTtcbiAgICAgICAgICBjb2wrKztcbiAgICAgICAgICBjb2xJbmRleCA9IHJvd1N0cmluZy5pbmRleE9mKGRlbGltaXRlciwgY29sSW5kZXggKyAxKTtcbiAgICAgICAgfVxuXG4gICAgICAgIC8vIElmIHdlIGRpZG4ndCByZWFjaCB0aGUgbnVtYmVyIG9mIGNvbHVtbnMgd2UgZXhwZWN0ZWQsIHBhZCB0aGUgb2Zmc2V0c1xuICAgICAgICAvLyB3aXRoIHRoZSBvZmZzZXQganVzdCBiZWZvcmUgdGhlIHJvdyBkZWxpbWl0ZXIuXG4gICAgICAgIHdoaWxlIChjb2wgPCBuY29scykge1xuICAgICAgICAgIG9mZnNldHMucHVzaChyb3dFbmQpO1xuICAgICAgICAgIGNvbCsrO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfVxuXG4gICAgLy8gU2tpcCBwYXN0IHRoZSByb3cgZGVsaW1pdGVyIGF0IHRoZSBlbmQgb2YgdGhlIHJvdy5cbiAgICBjdXJyUm93ID0gcm93RW5kICsgcm93RGVsaW1pdGVyTGVuZ3RoO1xuICB9XG5cbiAgcmV0dXJuIHsgbnJvd3MsIG5jb2xzOiBjb2x1bW5PZmZzZXRzID8gbmNvbHMgPz8gMCA6IDAsIG9mZnNldHMgfTtcbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgSVRyYW5zbGF0b3IsIG51bGxUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgU3R5bGluZyB9IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0IHsgZWFjaCB9IGZyb20gJ0BsdW1pbm8vYWxnb3JpdGhtJztcbmltcG9ydCB7IE1lc3NhZ2UgfSBmcm9tICdAbHVtaW5vL21lc3NhZ2luZyc7XG5pbXBvcnQgeyBJU2lnbmFsLCBTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0IHsgQ1NWVmlld2VyIH0gZnJvbSAnLi93aWRnZXQnO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIGEgY3N2IHRvb2xiYXIgd2lkZ2V0LlxuICovXG5jb25zdCBDU1ZfREVMSU1JVEVSX0NMQVNTID0gJ2pwLUNTVkRlbGltaXRlcic7XG5cbmNvbnN0IENTVl9ERUxJTUlURVJfTEFCRUxfQ0xBU1MgPSAnanAtQ1NWRGVsaW1pdGVyLWxhYmVsJztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCB0byBhIGNzdiB0b29sYmFyJ3MgZHJvcGRvd24gZWxlbWVudC5cbiAqL1xuY29uc3QgQ1NWX0RFTElNSVRFUl9EUk9QRE9XTl9DTEFTUyA9ICdqcC1DU1ZEZWxpbWl0ZXItZHJvcGRvd24nO1xuXG4vKipcbiAqIEEgd2lkZ2V0IGZvciBzZWxlY3RpbmcgYSBkZWxpbWl0ZXIuXG4gKi9cbmV4cG9ydCBjbGFzcyBDU1ZEZWxpbWl0ZXIgZXh0ZW5kcyBXaWRnZXQge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IGNzdiB0YWJsZSB3aWRnZXQuXG4gICAqL1xuICBjb25zdHJ1Y3RvcihvcHRpb25zOiBDU1ZUb29sYmFyLklPcHRpb25zKSB7XG4gICAgc3VwZXIoe1xuICAgICAgbm9kZTogUHJpdmF0ZS5jcmVhdGVOb2RlKG9wdGlvbnMud2lkZ2V0LmRlbGltaXRlciwgb3B0aW9ucy50cmFuc2xhdG9yKVxuICAgIH0pO1xuICAgIHRoaXMuX3dpZGdldCA9IG9wdGlvbnMud2lkZ2V0O1xuICAgIHRoaXMuYWRkQ2xhc3MoQ1NWX0RFTElNSVRFUl9DTEFTUyk7XG4gIH1cblxuICAvKipcbiAgICogQSBzaWduYWwgZW1pdHRlZCB3aGVuIHRoZSBkZWxpbWl0ZXIgc2VsZWN0aW9uIGhhcyBjaGFuZ2VkLlxuICAgKlxuICAgKiBAZGVwcmVjYXRlZCBzaW5jZSB2My4yXG4gICAqIFRoaXMgaXMgZGVhZCBjb2RlIG5vdy5cbiAgICovXG4gIGdldCBkZWxpbWl0ZXJDaGFuZ2VkKCk6IElTaWduYWw8dGhpcywgc3RyaW5nPiB7XG4gICAgcmV0dXJuIHRoaXMuX2RlbGltaXRlckNoYW5nZWQ7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGRlbGltaXRlciBkcm9wZG93biBtZW51LlxuICAgKi9cbiAgZ2V0IHNlbGVjdE5vZGUoKTogSFRNTFNlbGVjdEVsZW1lbnQge1xuICAgIHJldHVybiB0aGlzLm5vZGUuZ2V0RWxlbWVudHNCeVRhZ05hbWUoJ3NlbGVjdCcpIVswXTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIERPTSBldmVudHMgZm9yIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSBldmVudCAtIFRoZSBET00gZXZlbnQgc2VudCB0byB0aGUgd2lkZ2V0LlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoaXMgbWV0aG9kIGltcGxlbWVudHMgdGhlIERPTSBgRXZlbnRMaXN0ZW5lcmAgaW50ZXJmYWNlIGFuZCBpc1xuICAgKiBjYWxsZWQgaW4gcmVzcG9uc2UgdG8gZXZlbnRzIG9uIHRoZSBkb2NrIHBhbmVsJ3Mgbm9kZS4gSXQgc2hvdWxkXG4gICAqIG5vdCBiZSBjYWxsZWQgZGlyZWN0bHkgYnkgdXNlciBjb2RlLlxuICAgKi9cbiAgaGFuZGxlRXZlbnQoZXZlbnQ6IEV2ZW50KTogdm9pZCB7XG4gICAgc3dpdGNoIChldmVudC50eXBlKSB7XG4gICAgICBjYXNlICdjaGFuZ2UnOlxuICAgICAgICB0aGlzLl9kZWxpbWl0ZXJDaGFuZ2VkLmVtaXQodGhpcy5zZWxlY3ROb2RlLnZhbHVlKTtcbiAgICAgICAgdGhpcy5fd2lkZ2V0LmRlbGltaXRlciA9IHRoaXMuc2VsZWN0Tm9kZS52YWx1ZTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBkZWZhdWx0OlxuICAgICAgICBicmVhaztcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGBhZnRlci1hdHRhY2hgIG1lc3NhZ2VzIGZvciB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQWZ0ZXJBdHRhY2gobXNnOiBNZXNzYWdlKTogdm9pZCB7XG4gICAgdGhpcy5zZWxlY3ROb2RlLmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIHRoaXMpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBgYmVmb3JlLWRldGFjaGAgbWVzc2FnZXMgZm9yIHRoZSB3aWRnZXQuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25CZWZvcmVEZXRhY2gobXNnOiBNZXNzYWdlKTogdm9pZCB7XG4gICAgdGhpcy5zZWxlY3ROb2RlLnJlbW92ZUV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIHRoaXMpO1xuICB9XG5cbiAgcHJpdmF0ZSBfZGVsaW1pdGVyQ2hhbmdlZCA9IG5ldyBTaWduYWw8dGhpcywgc3RyaW5nPih0aGlzKTtcbiAgcHJvdGVjdGVkIF93aWRnZXQ6IENTVlZpZXdlcjtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgYENTVlRvb2xiYXJgIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgQ1NWVG9vbGJhciB7XG4gIC8qKlxuICAgKiBUaGUgaW5zdGFudGlhdGlvbiBvcHRpb25zIGZvciBhIENTViB0b29sYmFyLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogRG9jdW1lbnQgd2lkZ2V0IGZvciB0aGlzIHRvb2xiYXJcbiAgICAgKi9cbiAgICB3aWRnZXQ6IENTVlZpZXdlcjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBhcHBsaWNhdGlvbiBsYW5ndWFnZSB0cmFuc2xhdG9yLlxuICAgICAqL1xuICAgIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvcjtcbiAgfVxufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBwcml2YXRlIHRvb2xiYXIgbWV0aG9kcy5cbiAqL1xubmFtZXNwYWNlIFByaXZhdGUge1xuICAvKipcbiAgICogQ3JlYXRlIHRoZSBub2RlIGZvciB0aGUgZGVsaW1pdGVyIHN3aXRjaGVyLlxuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIGNyZWF0ZU5vZGUoXG4gICAgc2VsZWN0ZWQ6IHN0cmluZyxcbiAgICB0cmFuc2xhdG9yPzogSVRyYW5zbGF0b3JcbiAgKTogSFRNTEVsZW1lbnQge1xuICAgIHRyYW5zbGF0b3IgPSB0cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvcj8ubG9hZCgnanVweXRlcmxhYicpO1xuXG4gICAgLy8gVGhlIHN1cHBvcnRlZCBwYXJzaW5nIGRlbGltaXRlcnMgYW5kIGxhYmVscy5cbiAgICBjb25zdCBkZWxpbWl0ZXJzID0gW1xuICAgICAgWycsJywgJywnXSxcbiAgICAgIFsnOycsICc7J10sXG4gICAgICBbJ1xcdCcsIHRyYW5zLl9fKCd0YWInKV0sXG4gICAgICBbJ3wnLCB0cmFucy5fXygncGlwZScpXSxcbiAgICAgIFsnIycsIHRyYW5zLl9fKCdoYXNoJyldXG4gICAgXTtcblxuICAgIGNvbnN0IGRpdiA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2RpdicpO1xuICAgIGNvbnN0IGxhYmVsID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpO1xuICAgIGNvbnN0IHNlbGVjdCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3NlbGVjdCcpO1xuICAgIGxhYmVsLnRleHRDb250ZW50ID0gdHJhbnMuX18oJ0RlbGltaXRlcjogJyk7XG4gICAgbGFiZWwuY2xhc3NOYW1lID0gQ1NWX0RFTElNSVRFUl9MQUJFTF9DTEFTUztcbiAgICBlYWNoKGRlbGltaXRlcnMsIChbZGVsaW1pdGVyLCBsYWJlbF0pID0+IHtcbiAgICAgIGNvbnN0IG9wdGlvbiA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ29wdGlvbicpO1xuICAgICAgb3B0aW9uLnZhbHVlID0gZGVsaW1pdGVyO1xuICAgICAgb3B0aW9uLnRleHRDb250ZW50ID0gbGFiZWw7XG4gICAgICBpZiAoZGVsaW1pdGVyID09PSBzZWxlY3RlZCkge1xuICAgICAgICBvcHRpb24uc2VsZWN0ZWQgPSB0cnVlO1xuICAgICAgfVxuICAgICAgc2VsZWN0LmFwcGVuZENoaWxkKG9wdGlvbik7XG4gICAgfSk7XG4gICAgZGl2LmFwcGVuZENoaWxkKGxhYmVsKTtcbiAgICBjb25zdCBub2RlID0gU3R5bGluZy53cmFwU2VsZWN0KHNlbGVjdCk7XG4gICAgbm9kZS5jbGFzc0xpc3QuYWRkKENTVl9ERUxJTUlURVJfRFJPUERPV05fQ0xBU1MpO1xuICAgIGRpdi5hcHBlbmRDaGlsZChub2RlKTtcbiAgICByZXR1cm4gZGl2O1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IEFjdGl2aXR5TW9uaXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL2NvcmV1dGlscyc7XG5pbXBvcnQge1xuICBBQkNXaWRnZXRGYWN0b3J5LFxuICBEb2N1bWVudFJlZ2lzdHJ5LFxuICBEb2N1bWVudFdpZGdldCxcbiAgSURvY3VtZW50V2lkZ2V0XG59IGZyb20gJ0BqdXB5dGVybGFiL2RvY3JlZ2lzdHJ5JztcbmltcG9ydCB7IFByb21pc2VEZWxlZ2F0ZSB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7XG4gIEJhc2ljS2V5SGFuZGxlcixcbiAgQmFzaWNNb3VzZUhhbmRsZXIsXG4gIEJhc2ljU2VsZWN0aW9uTW9kZWwsXG4gIENlbGxSZW5kZXJlcixcbiAgRGF0YUdyaWQsXG4gIFRleHRSZW5kZXJlclxufSBmcm9tICdAbHVtaW5vL2RhdGFncmlkJztcbmltcG9ydCB7IE1lc3NhZ2UgfSBmcm9tICdAbHVtaW5vL21lc3NhZ2luZyc7XG5pbXBvcnQgeyBJU2lnbmFsLCBTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBQYW5lbExheW91dCwgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IERTVk1vZGVsIH0gZnJvbSAnLi9tb2RlbCc7XG5pbXBvcnQgeyBDU1ZEZWxpbWl0ZXIgfSBmcm9tICcuL3Rvb2xiYXInO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIGEgQ1NWIHZpZXdlci5cbiAqL1xuY29uc3QgQ1NWX0NMQVNTID0gJ2pwLUNTVlZpZXdlcic7XG5cbi8qKlxuICogVGhlIGNsYXNzIG5hbWUgYWRkZWQgdG8gYSBDU1Ygdmlld2VyIGRhdGFncmlkLlxuICovXG5jb25zdCBDU1ZfR1JJRF9DTEFTUyA9ICdqcC1DU1ZWaWV3ZXItZ3JpZCc7XG5cbi8qKlxuICogVGhlIHRpbWVvdXQgdG8gd2FpdCBmb3IgY2hhbmdlIGFjdGl2aXR5IHRvIGhhdmUgY2Vhc2VkIGJlZm9yZSByZW5kZXJpbmcuXG4gKi9cbmNvbnN0IFJFTkRFUl9USU1FT1VUID0gMTAwMDtcblxuLyoqXG4gKiBDb25maWd1cmF0aW9uIGZvciBjZWxscyB0ZXh0cmVuZGVyZXIuXG4gKi9cbmV4cG9ydCBjbGFzcyBUZXh0UmVuZGVyQ29uZmlnIHtcbiAgLyoqXG4gICAqIGRlZmF1bHQgdGV4dCBjb2xvclxuICAgKi9cbiAgdGV4dENvbG9yOiBzdHJpbmc7XG4gIC8qKlxuICAgKiBiYWNrZ3JvdW5kIGNvbG9yIGZvciBhIHNlYXJjaCBtYXRjaFxuICAgKi9cbiAgbWF0Y2hCYWNrZ3JvdW5kQ29sb3I6IHN0cmluZztcbiAgLyoqXG4gICAqIGJhY2tncm91bmQgY29sb3IgZm9yIHRoZSBjdXJyZW50IHNlYXJjaCBtYXRjaC5cbiAgICovXG4gIGN1cnJlbnRNYXRjaEJhY2tncm91bmRDb2xvcjogc3RyaW5nO1xuICAvKipcbiAgICogaG9yaXpvbnRhbEFsaWdubWVudCBvZiB0aGUgdGV4dFxuICAgKi9cbiAgaG9yaXpvbnRhbEFsaWdubWVudDogVGV4dFJlbmRlcmVyLkhvcml6b250YWxBbGlnbm1lbnQ7XG59XG5cbi8qKlxuICogU2VhcmNoIHNlcnZpY2UgcmVtZW1iZXJzIHRoZSBzZWFyY2ggc3RhdGUgYW5kIHRoZSBsb2NhdGlvbiBvZiB0aGUgbGFzdFxuICogbWF0Y2gsIGZvciBpbmNyZW1lbnRhbCBzZWFyY2hpbmcuXG4gKiBTZWFyY2ggc2VydmljZSBpcyBhbHNvIHJlc3BvbnNpYmxlIG9mIHByb3ZpZGluZyBhIGNlbGwgcmVuZGVyZXIgZnVuY3Rpb25cbiAqIHRvIHNldCB0aGUgYmFja2dyb3VuZCBjb2xvciBvZiBjZWxscyBtYXRjaGluZyB0aGUgc2VhcmNoIHRleHQuXG4gKi9cbmV4cG9ydCBjbGFzcyBHcmlkU2VhcmNoU2VydmljZSB7XG4gIGNvbnN0cnVjdG9yKGdyaWQ6IERhdGFHcmlkKSB7XG4gICAgdGhpcy5fZ3JpZCA9IGdyaWQ7XG4gICAgdGhpcy5fcXVlcnkgPSBudWxsO1xuICAgIHRoaXMuX3JvdyA9IDA7XG4gICAgdGhpcy5fY29sdW1uID0gLTE7XG4gIH1cblxuICAvKipcbiAgICogQSBzaWduYWwgZmlyZWQgd2hlbiB0aGUgZ3JpZCBjaGFuZ2VzLlxuICAgKi9cbiAgZ2V0IGNoYW5nZWQoKTogSVNpZ25hbDxHcmlkU2VhcmNoU2VydmljZSwgdm9pZD4ge1xuICAgIHJldHVybiB0aGlzLl9jaGFuZ2VkO1xuICB9XG5cbiAgLyoqXG4gICAqIFJldHVybnMgYSBjZWxscmVuZGVyZXIgY29uZmlnIGZ1bmN0aW9uIHRvIHJlbmRlciBlYWNoIGNlbGwgYmFja2dyb3VuZC5cbiAgICogSWYgY2VsbCBtYXRjaCwgYmFja2dyb3VuZCBpcyBtYXRjaEJhY2tncm91bmRDb2xvciwgaWYgaXQncyB0aGUgY3VycmVudFxuICAgKiBtYXRjaCwgYmFja2dyb3VuZCBpcyBjdXJyZW50TWF0Y2hCYWNrZ3JvdW5kQ29sb3IuXG4gICAqL1xuICBjZWxsQmFja2dyb3VuZENvbG9yUmVuZGVyZXJGdW5jKFxuICAgIGNvbmZpZzogVGV4dFJlbmRlckNvbmZpZ1xuICApOiBDZWxsUmVuZGVyZXIuQ29uZmlnRnVuYzxzdHJpbmc+IHtcbiAgICByZXR1cm4gKHsgdmFsdWUsIHJvdywgY29sdW1uIH0pID0+IHtcbiAgICAgIGlmICh0aGlzLl9xdWVyeSkge1xuICAgICAgICBpZiAoKHZhbHVlIGFzIHN0cmluZykubWF0Y2godGhpcy5fcXVlcnkpKSB7XG4gICAgICAgICAgaWYgKHRoaXMuX3JvdyA9PT0gcm93ICYmIHRoaXMuX2NvbHVtbiA9PT0gY29sdW1uKSB7XG4gICAgICAgICAgICByZXR1cm4gY29uZmlnLmN1cnJlbnRNYXRjaEJhY2tncm91bmRDb2xvcjtcbiAgICAgICAgICB9XG4gICAgICAgICAgcmV0dXJuIGNvbmZpZy5tYXRjaEJhY2tncm91bmRDb2xvcjtcbiAgICAgICAgfVxuICAgICAgfVxuICAgICAgcmV0dXJuICcnO1xuICAgIH07XG4gIH1cblxuICAvKipcbiAgICogQ2xlYXIgdGhlIHNlYXJjaC5cbiAgICovXG4gIGNsZWFyKCk6IHZvaWQge1xuICAgIHRoaXMuX3F1ZXJ5ID0gbnVsbDtcbiAgICB0aGlzLl9yb3cgPSAwO1xuICAgIHRoaXMuX2NvbHVtbiA9IC0xO1xuICAgIHRoaXMuX2NoYW5nZWQuZW1pdCh1bmRlZmluZWQpO1xuICB9XG5cbiAgLyoqXG4gICAqIGluY3JlbWVudGFsbHkgbG9vayBmb3Igc2VhcmNoVGV4dC5cbiAgICovXG4gIGZpbmQocXVlcnk6IFJlZ0V4cCwgcmV2ZXJzZSA9IGZhbHNlKTogYm9vbGVhbiB7XG4gICAgY29uc3QgbW9kZWwgPSB0aGlzLl9ncmlkLmRhdGFNb2RlbCE7XG4gICAgY29uc3Qgcm93Q291bnQgPSBtb2RlbC5yb3dDb3VudCgnYm9keScpO1xuICAgIGNvbnN0IGNvbHVtbkNvdW50ID0gbW9kZWwuY29sdW1uQ291bnQoJ2JvZHknKTtcblxuICAgIGlmICh0aGlzLl9xdWVyeSAhPT0gcXVlcnkpIHtcbiAgICAgIC8vIHJlc2V0IHNlYXJjaFxuICAgICAgdGhpcy5fcm93ID0gMDtcbiAgICAgIHRoaXMuX2NvbHVtbiA9IC0xO1xuICAgIH1cbiAgICB0aGlzLl9xdWVyeSA9IHF1ZXJ5O1xuXG4gICAgLy8gY2hlY2sgaWYgdGhlIG1hdGNoIGlzIGluIGN1cnJlbnQgdmlld3BvcnRcblxuICAgIGNvbnN0IG1pblJvdyA9IHRoaXMuX2dyaWQuc2Nyb2xsWSAvIHRoaXMuX2dyaWQuZGVmYXVsdFNpemVzLnJvd0hlaWdodDtcbiAgICBjb25zdCBtYXhSb3cgPVxuICAgICAgKHRoaXMuX2dyaWQuc2Nyb2xsWSArIHRoaXMuX2dyaWQucGFnZUhlaWdodCkgL1xuICAgICAgdGhpcy5fZ3JpZC5kZWZhdWx0U2l6ZXMucm93SGVpZ2h0O1xuICAgIGNvbnN0IG1pbkNvbHVtbiA9XG4gICAgICB0aGlzLl9ncmlkLnNjcm9sbFggLyB0aGlzLl9ncmlkLmRlZmF1bHRTaXplcy5jb2x1bW5IZWFkZXJIZWlnaHQ7XG4gICAgY29uc3QgbWF4Q29sdW1uID1cbiAgICAgICh0aGlzLl9ncmlkLnNjcm9sbFggKyB0aGlzLl9ncmlkLnBhZ2VXaWR0aCkgL1xuICAgICAgdGhpcy5fZ3JpZC5kZWZhdWx0U2l6ZXMuY29sdW1uSGVhZGVySGVpZ2h0O1xuICAgIGNvbnN0IGlzSW5WaWV3cG9ydCA9IChyb3c6IG51bWJlciwgY29sdW1uOiBudW1iZXIpID0+IHtcbiAgICAgIHJldHVybiAoXG4gICAgICAgIHJvdyA+PSBtaW5Sb3cgJiZcbiAgICAgICAgcm93IDw9IG1heFJvdyAmJlxuICAgICAgICBjb2x1bW4gPj0gbWluQ29sdW1uICYmXG4gICAgICAgIGNvbHVtbiA8PSBtYXhDb2x1bW5cbiAgICAgICk7XG4gICAgfTtcblxuICAgIGNvbnN0IGluY3JlbWVudCA9IHJldmVyc2UgPyAtMSA6IDE7XG4gICAgdGhpcy5fY29sdW1uICs9IGluY3JlbWVudDtcbiAgICBmb3IgKFxuICAgICAgbGV0IHJvdyA9IHRoaXMuX3JvdztcbiAgICAgIHJldmVyc2UgPyByb3cgPj0gMCA6IHJvdyA8IHJvd0NvdW50O1xuICAgICAgcm93ICs9IGluY3JlbWVudFxuICAgICkge1xuICAgICAgZm9yIChcbiAgICAgICAgbGV0IGNvbCA9IHRoaXMuX2NvbHVtbjtcbiAgICAgICAgcmV2ZXJzZSA/IGNvbCA+PSAwIDogY29sIDwgY29sdW1uQ291bnQ7XG4gICAgICAgIGNvbCArPSBpbmNyZW1lbnRcbiAgICAgICkge1xuICAgICAgICBjb25zdCBjZWxsRGF0YSA9IG1vZGVsLmRhdGEoJ2JvZHknLCByb3csIGNvbCkgYXMgc3RyaW5nO1xuICAgICAgICBpZiAoY2VsbERhdGEubWF0Y2gocXVlcnkpKSB7XG4gICAgICAgICAgLy8gdG8gdXBkYXRlIHRoZSBiYWNrZ3JvdW5kIG9mIG1hdGNoaW5nIGNlbGxzLlxuXG4gICAgICAgICAgLy8gVE9ETzogd2Ugb25seSByZWFsbHkgbmVlZCB0byBpbnZhbGlkYXRlIHRoZSBwcmV2aW91cyBhbmQgY3VycmVudFxuICAgICAgICAgIC8vIGNlbGwgcmVjdHMsIG5vdCB0aGUgZW50aXJlIGdyaWQuXG4gICAgICAgICAgdGhpcy5fY2hhbmdlZC5lbWl0KHVuZGVmaW5lZCk7XG5cbiAgICAgICAgICBpZiAoIWlzSW5WaWV3cG9ydChyb3csIGNvbCkpIHtcbiAgICAgICAgICAgIHRoaXMuX2dyaWQuc2Nyb2xsVG9Sb3cocm93KTtcbiAgICAgICAgICB9XG4gICAgICAgICAgdGhpcy5fcm93ID0gcm93O1xuICAgICAgICAgIHRoaXMuX2NvbHVtbiA9IGNvbDtcbiAgICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgICAgdGhpcy5fY29sdW1uID0gcmV2ZXJzZSA/IGNvbHVtbkNvdW50IC0gMSA6IDA7XG4gICAgfVxuICAgIC8vIFdlJ3ZlIGZpbmlzaGVkIHNlYXJjaGluZyBhbGwgdGhlIHdheSB0byB0aGUgbGltaXRzIG9mIHRoZSBncmlkLiBJZiB0aGlzXG4gICAgLy8gaXMgdGhlIGZpcnN0IHRpbWUgdGhyb3VnaCAobG9vcGluZyBpcyB0cnVlKSwgd3JhcCB0aGUgaW5kaWNlcyBhbmQgc2VhcmNoXG4gICAgLy8gYWdhaW4uIE90aGVyd2lzZSwgZ2l2ZSB1cC5cbiAgICBpZiAodGhpcy5fbG9vcGluZykge1xuICAgICAgdGhpcy5fbG9vcGluZyA9IGZhbHNlO1xuICAgICAgdGhpcy5fcm93ID0gcmV2ZXJzZSA/IDAgOiByb3dDb3VudCAtIDE7XG4gICAgICB0aGlzLl93cmFwUm93cyhyZXZlcnNlKTtcbiAgICAgIHRyeSB7XG4gICAgICAgIHJldHVybiB0aGlzLmZpbmQocXVlcnksIHJldmVyc2UpO1xuICAgICAgfSBmaW5hbGx5IHtcbiAgICAgICAgdGhpcy5fbG9vcGluZyA9IHRydWU7XG4gICAgICB9XG4gICAgfVxuICAgIHJldHVybiBmYWxzZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBXcmFwIGluZGljZXMgaWYgbmVlZGVkIHRvIGp1c3QgYmVmb3JlIHRoZSBzdGFydCBvciBqdXN0IGFmdGVyIHRoZSBlbmQuXG4gICAqL1xuICBwcml2YXRlIF93cmFwUm93cyhyZXZlcnNlID0gZmFsc2UpIHtcbiAgICBjb25zdCBtb2RlbCA9IHRoaXMuX2dyaWQuZGF0YU1vZGVsITtcbiAgICBjb25zdCByb3dDb3VudCA9IG1vZGVsLnJvd0NvdW50KCdib2R5Jyk7XG4gICAgY29uc3QgY29sdW1uQ291bnQgPSBtb2RlbC5jb2x1bW5Db3VudCgnYm9keScpO1xuXG4gICAgaWYgKHJldmVyc2UgJiYgdGhpcy5fcm93IDw9IDApIHtcbiAgICAgIC8vIGlmIHdlIGFyZSBhdCB0aGUgZnJvbnQsIHdyYXAgdG8ganVzdCBwYXN0IHRoZSBlbmQuXG4gICAgICB0aGlzLl9yb3cgPSByb3dDb3VudCAtIDE7XG4gICAgICB0aGlzLl9jb2x1bW4gPSBjb2x1bW5Db3VudDtcbiAgICB9IGVsc2UgaWYgKCFyZXZlcnNlICYmIHRoaXMuX3JvdyA+PSByb3dDb3VudCAtIDEpIHtcbiAgICAgIC8vIGlmIHdlIGFyZSBhdCB0aGUgZW5kLCB3cmFwIHRvIGp1c3QgYmVmb3JlIHRoZSBmcm9udC5cbiAgICAgIHRoaXMuX3JvdyA9IDA7XG4gICAgICB0aGlzLl9jb2x1bW4gPSAtMTtcbiAgICB9XG4gIH1cblxuICBnZXQgcXVlcnkoKTogUmVnRXhwIHwgbnVsbCB7XG4gICAgcmV0dXJuIHRoaXMuX3F1ZXJ5O1xuICB9XG5cbiAgcHJpdmF0ZSBfZ3JpZDogRGF0YUdyaWQ7XG4gIHByaXZhdGUgX3F1ZXJ5OiBSZWdFeHAgfCBudWxsO1xuICBwcml2YXRlIF9yb3c6IG51bWJlcjtcbiAgcHJpdmF0ZSBfY29sdW1uOiBudW1iZXI7XG4gIHByaXZhdGUgX2xvb3BpbmcgPSB0cnVlO1xuICBwcml2YXRlIF9jaGFuZ2VkID0gbmV3IFNpZ25hbDxHcmlkU2VhcmNoU2VydmljZSwgdm9pZD4odGhpcyk7XG59XG5cbi8qKlxuICogQSB2aWV3ZXIgZm9yIENTViB0YWJsZXMuXG4gKi9cbmV4cG9ydCBjbGFzcyBDU1ZWaWV3ZXIgZXh0ZW5kcyBXaWRnZXQge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IENTViB2aWV3ZXIuXG4gICAqL1xuICBjb25zdHJ1Y3RvcihvcHRpb25zOiBDU1ZWaWV3ZXIuSU9wdGlvbnMpIHtcbiAgICBzdXBlcigpO1xuXG4gICAgY29uc3QgY29udGV4dCA9ICh0aGlzLl9jb250ZXh0ID0gb3B0aW9ucy5jb250ZXh0KTtcbiAgICBjb25zdCBsYXlvdXQgPSAodGhpcy5sYXlvdXQgPSBuZXcgUGFuZWxMYXlvdXQoKSk7XG5cbiAgICB0aGlzLmFkZENsYXNzKENTVl9DTEFTUyk7XG5cbiAgICB0aGlzLl9ncmlkID0gbmV3IERhdGFHcmlkKHtcbiAgICAgIGRlZmF1bHRTaXplczoge1xuICAgICAgICByb3dIZWlnaHQ6IDI0LFxuICAgICAgICBjb2x1bW5XaWR0aDogMTQ0LFxuICAgICAgICByb3dIZWFkZXJXaWR0aDogNjQsXG4gICAgICAgIGNvbHVtbkhlYWRlckhlaWdodDogMzZcbiAgICAgIH1cbiAgICB9KTtcbiAgICB0aGlzLl9ncmlkLmFkZENsYXNzKENTVl9HUklEX0NMQVNTKTtcbiAgICB0aGlzLl9ncmlkLmhlYWRlclZpc2liaWxpdHkgPSAnYWxsJztcbiAgICB0aGlzLl9ncmlkLmtleUhhbmRsZXIgPSBuZXcgQmFzaWNLZXlIYW5kbGVyKCk7XG4gICAgdGhpcy5fZ3JpZC5tb3VzZUhhbmRsZXIgPSBuZXcgQmFzaWNNb3VzZUhhbmRsZXIoKTtcbiAgICB0aGlzLl9ncmlkLmNvcHlDb25maWcgPSB7XG4gICAgICBzZXBhcmF0b3I6ICdcXHQnLFxuICAgICAgZm9ybWF0OiBEYXRhR3JpZC5jb3B5Rm9ybWF0R2VuZXJpYyxcbiAgICAgIGhlYWRlcnM6ICdhbGwnLFxuICAgICAgd2FybmluZ1RocmVzaG9sZDogMWU2XG4gICAgfTtcblxuICAgIGxheW91dC5hZGRXaWRnZXQodGhpcy5fZ3JpZCk7XG5cbiAgICB0aGlzLl9zZWFyY2hTZXJ2aWNlID0gbmV3IEdyaWRTZWFyY2hTZXJ2aWNlKHRoaXMuX2dyaWQpO1xuICAgIHRoaXMuX3NlYXJjaFNlcnZpY2UuY2hhbmdlZC5jb25uZWN0KHRoaXMuX3VwZGF0ZVJlbmRlcmVyLCB0aGlzKTtcblxuICAgIHZvaWQgdGhpcy5fY29udGV4dC5yZWFkeS50aGVuKCgpID0+IHtcbiAgICAgIHRoaXMuX3VwZGF0ZUdyaWQoKTtcbiAgICAgIHRoaXMuX3JldmVhbGVkLnJlc29sdmUodW5kZWZpbmVkKTtcbiAgICAgIC8vIFRocm90dGxlIHRoZSByZW5kZXJpbmcgcmF0ZSBvZiB0aGUgd2lkZ2V0LlxuICAgICAgdGhpcy5fbW9uaXRvciA9IG5ldyBBY3Rpdml0eU1vbml0b3Ioe1xuICAgICAgICBzaWduYWw6IGNvbnRleHQubW9kZWwuY29udGVudENoYW5nZWQsXG4gICAgICAgIHRpbWVvdXQ6IFJFTkRFUl9USU1FT1VUXG4gICAgICB9KTtcbiAgICAgIHRoaXMuX21vbml0b3IuYWN0aXZpdHlTdG9wcGVkLmNvbm5lY3QodGhpcy5fdXBkYXRlR3JpZCwgdGhpcyk7XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogVGhlIENTViB3aWRnZXQncyBjb250ZXh0LlxuICAgKi9cbiAgZ2V0IGNvbnRleHQoKTogRG9jdW1lbnRSZWdpc3RyeS5Db250ZXh0IHtcbiAgICByZXR1cm4gdGhpcy5fY29udGV4dDtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIHByb21pc2UgdGhhdCByZXNvbHZlcyB3aGVuIHRoZSBjc3Ygdmlld2VyIGlzIHJlYWR5IHRvIGJlIHJldmVhbGVkLlxuICAgKi9cbiAgZ2V0IHJldmVhbGVkKCk6IFByb21pc2U8dm9pZD4ge1xuICAgIHJldHVybiB0aGlzLl9yZXZlYWxlZC5wcm9taXNlO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBkZWxpbWl0ZXIgZm9yIHRoZSBmaWxlLlxuICAgKi9cbiAgZ2V0IGRlbGltaXRlcigpOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLl9kZWxpbWl0ZXI7XG4gIH1cbiAgc2V0IGRlbGltaXRlcih2YWx1ZTogc3RyaW5nKSB7XG4gICAgaWYgKHZhbHVlID09PSB0aGlzLl9kZWxpbWl0ZXIpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgdGhpcy5fZGVsaW1pdGVyID0gdmFsdWU7XG4gICAgdGhpcy5fdXBkYXRlR3JpZCgpO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBzdHlsZSB1c2VkIGJ5IHRoZSBkYXRhIGdyaWQuXG4gICAqL1xuICBnZXQgc3R5bGUoKTogRGF0YUdyaWQuU3R5bGUge1xuICAgIHJldHVybiB0aGlzLl9ncmlkLnN0eWxlO1xuICB9XG4gIHNldCBzdHlsZSh2YWx1ZTogRGF0YUdyaWQuU3R5bGUpIHtcbiAgICB0aGlzLl9ncmlkLnN0eWxlID0gdmFsdWU7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGNvbmZpZyB1c2VkIHRvIGNyZWF0ZSB0ZXh0IHJlbmRlcmVyLlxuICAgKi9cbiAgc2V0IHJlbmRlcmVyQ29uZmlnKHJlbmRlcmVyQ29uZmlnOiBUZXh0UmVuZGVyQ29uZmlnKSB7XG4gICAgdGhpcy5fYmFzZVJlbmRlcmVyID0gcmVuZGVyZXJDb25maWc7XG4gICAgdGhpcy5fdXBkYXRlUmVuZGVyZXIoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgc2VhcmNoIHNlcnZpY2VcbiAgICovXG4gIGdldCBzZWFyY2hTZXJ2aWNlKCk6IEdyaWRTZWFyY2hTZXJ2aWNlIHtcbiAgICByZXR1cm4gdGhpcy5fc2VhcmNoU2VydmljZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIG9mIHRoZSByZXNvdXJjZXMgdXNlZCBieSB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgZGlzcG9zZSgpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5fbW9uaXRvcikge1xuICAgICAgdGhpcy5fbW9uaXRvci5kaXNwb3NlKCk7XG4gICAgfVxuICAgIHN1cGVyLmRpc3Bvc2UoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHbyB0byBsaW5lXG4gICAqL1xuICBnb1RvTGluZShsaW5lTnVtYmVyOiBudW1iZXIpOiB2b2lkIHtcbiAgICB0aGlzLl9ncmlkLnNjcm9sbFRvUm93KGxpbmVOdW1iZXIpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBgJ2FjdGl2YXRlLXJlcXVlc3QnYCBtZXNzYWdlcy5cbiAgICovXG4gIHByb3RlY3RlZCBvbkFjdGl2YXRlUmVxdWVzdChtc2c6IE1lc3NhZ2UpOiB2b2lkIHtcbiAgICB0aGlzLm5vZGUudGFiSW5kZXggPSAtMTtcbiAgICB0aGlzLm5vZGUuZm9jdXMoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBDcmVhdGUgdGhlIG1vZGVsIGZvciB0aGUgZ3JpZC5cbiAgICovXG4gIHByaXZhdGUgX3VwZGF0ZUdyaWQoKTogdm9pZCB7XG4gICAgY29uc3QgZGF0YTogc3RyaW5nID0gdGhpcy5fY29udGV4dC5tb2RlbC50b1N0cmluZygpO1xuICAgIGNvbnN0IGRlbGltaXRlciA9IHRoaXMuX2RlbGltaXRlcjtcbiAgICBjb25zdCBvbGRNb2RlbCA9IHRoaXMuX2dyaWQuZGF0YU1vZGVsIGFzIERTVk1vZGVsO1xuICAgIGNvbnN0IGRhdGFNb2RlbCA9ICh0aGlzLl9ncmlkLmRhdGFNb2RlbCA9IG5ldyBEU1ZNb2RlbCh7XG4gICAgICBkYXRhLFxuICAgICAgZGVsaW1pdGVyXG4gICAgfSkpO1xuICAgIHRoaXMuX2dyaWQuc2VsZWN0aW9uTW9kZWwgPSBuZXcgQmFzaWNTZWxlY3Rpb25Nb2RlbCh7IGRhdGFNb2RlbCB9KTtcbiAgICBpZiAob2xkTW9kZWwpIHtcbiAgICAgIG9sZE1vZGVsLmRpc3Bvc2UoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogVXBkYXRlIHRoZSByZW5kZXJlciBmb3IgdGhlIGdyaWQuXG4gICAqL1xuICBwcml2YXRlIF91cGRhdGVSZW5kZXJlcigpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5fYmFzZVJlbmRlcmVyID09PSBudWxsKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbnN0IHJlbmRlcmVyQ29uZmlnID0gdGhpcy5fYmFzZVJlbmRlcmVyO1xuICAgIGNvbnN0IHJlbmRlcmVyID0gbmV3IFRleHRSZW5kZXJlcih7XG4gICAgICB0ZXh0Q29sb3I6IHJlbmRlcmVyQ29uZmlnLnRleHRDb2xvcixcbiAgICAgIGhvcml6b250YWxBbGlnbm1lbnQ6IHJlbmRlcmVyQ29uZmlnLmhvcml6b250YWxBbGlnbm1lbnQsXG4gICAgICBiYWNrZ3JvdW5kQ29sb3I6XG4gICAgICAgIHRoaXMuX3NlYXJjaFNlcnZpY2UuY2VsbEJhY2tncm91bmRDb2xvclJlbmRlcmVyRnVuYyhyZW5kZXJlckNvbmZpZylcbiAgICB9KTtcbiAgICB0aGlzLl9ncmlkLmNlbGxSZW5kZXJlcnMudXBkYXRlKHtcbiAgICAgIGJvZHk6IHJlbmRlcmVyLFxuICAgICAgJ2NvbHVtbi1oZWFkZXInOiByZW5kZXJlcixcbiAgICAgICdjb3JuZXItaGVhZGVyJzogcmVuZGVyZXIsXG4gICAgICAncm93LWhlYWRlcic6IHJlbmRlcmVyXG4gICAgfSk7XG4gIH1cblxuICBwcml2YXRlIF9jb250ZXh0OiBEb2N1bWVudFJlZ2lzdHJ5LkNvbnRleHQ7XG4gIHByaXZhdGUgX2dyaWQ6IERhdGFHcmlkO1xuICBwcml2YXRlIF9zZWFyY2hTZXJ2aWNlOiBHcmlkU2VhcmNoU2VydmljZTtcbiAgcHJpdmF0ZSBfbW9uaXRvcjogQWN0aXZpdHlNb25pdG9yPERvY3VtZW50UmVnaXN0cnkuSU1vZGVsLCB2b2lkPiB8IG51bGwgPVxuICAgIG51bGw7XG4gIHByaXZhdGUgX2RlbGltaXRlciA9ICcsJztcbiAgcHJpdmF0ZSBfcmV2ZWFsZWQgPSBuZXcgUHJvbWlzZURlbGVnYXRlPHZvaWQ+KCk7XG4gIHByaXZhdGUgX2Jhc2VSZW5kZXJlcjogVGV4dFJlbmRlckNvbmZpZyB8IG51bGwgPSBudWxsO1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBgQ1NWVmlld2VyYCBzdGF0aWNzLlxuICovXG5leHBvcnQgbmFtZXNwYWNlIENTVlZpZXdlciB7XG4gIC8qKlxuICAgKiBJbnN0YW50aWF0aW9uIG9wdGlvbnMgZm9yIENTViB3aWRnZXRzLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIGRvY3VtZW50IGNvbnRleHQgZm9yIHRoZSBDU1YgYmVpbmcgcmVuZGVyZWQgYnkgdGhlIHdpZGdldC5cbiAgICAgKi9cbiAgICBjb250ZXh0OiBEb2N1bWVudFJlZ2lzdHJ5LkNvbnRleHQ7XG4gIH1cbn1cblxuLyoqXG4gKiBBIGRvY3VtZW50IHdpZGdldCBmb3IgQ1NWIGNvbnRlbnQgd2lkZ2V0cy5cbiAqL1xuZXhwb3J0IGNsYXNzIENTVkRvY3VtZW50V2lkZ2V0IGV4dGVuZHMgRG9jdW1lbnRXaWRnZXQ8Q1NWVmlld2VyPiB7XG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IENTVkRvY3VtZW50V2lkZ2V0LklPcHRpb25zKSB7XG4gICAgbGV0IHsgY29udGVudCwgY29udGV4dCwgZGVsaW1pdGVyLCByZXZlYWwsIC4uLm90aGVyIH0gPSBvcHRpb25zO1xuICAgIGNvbnRlbnQgPSBjb250ZW50IHx8IFByaXZhdGUuY3JlYXRlQ29udGVudChjb250ZXh0KTtcbiAgICByZXZlYWwgPSBQcm9taXNlLmFsbChbcmV2ZWFsLCBjb250ZW50LnJldmVhbGVkXSk7XG4gICAgc3VwZXIoeyBjb250ZW50LCBjb250ZXh0LCByZXZlYWwsIC4uLm90aGVyIH0pO1xuXG4gICAgaWYgKGRlbGltaXRlcikge1xuICAgICAgY29udGVudC5kZWxpbWl0ZXIgPSBkZWxpbWl0ZXI7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFNldCBVUkkgZnJhZ21lbnQgaWRlbnRpZmllciBmb3Igcm93c1xuICAgKi9cbiAgc2V0RnJhZ21lbnQoZnJhZ21lbnQ6IHN0cmluZyk6IHZvaWQge1xuICAgIGNvbnN0IHBhcnNlRnJhZ21lbnRzID0gZnJhZ21lbnQuc3BsaXQoJz0nKTtcblxuICAgIC8vIFRPRE86IGV4cGFuZCB0byBhbGxvdyBjb2x1bW5zIGFuZCBjZWxscyB0byBiZSBzZWxlY3RlZFxuICAgIC8vIHJlZmVyZW5jZTogaHR0cHM6Ly90b29scy5pZXRmLm9yZy9odG1sL3JmYzcxMTEjc2VjdGlvbi0zXG4gICAgaWYgKHBhcnNlRnJhZ21lbnRzWzBdICE9PSAnI3JvdycpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICAvLyBtdWx0aXBsZSByb3dzLCBzZXBhcmF0ZWQgYnkgc2VtaS1jb2xvbnMgY2FuIGJlIHByb3ZpZGVkLCB3ZSB3aWxsIGp1c3RcbiAgICAvLyBnbyB0byB0aGUgdG9wIG9uZVxuICAgIGxldCB0b3BSb3cgPSBwYXJzZUZyYWdtZW50c1sxXS5zcGxpdCgnOycpWzBdO1xuXG4gICAgLy8gYSByYW5nZSBvZiByb3dzIGNhbiBiZSBwcm92aWRlZCwgd2Ugd2lsbCB0YWtlIHRoZSBmaXJzdCB2YWx1ZVxuICAgIHRvcFJvdyA9IHRvcFJvdy5zcGxpdCgnLScpWzBdO1xuXG4gICAgLy8gZ28gdG8gdGhhdCByb3dcbiAgICB2b2lkIHRoaXMuY29udGV4dC5yZWFkeS50aGVuKCgpID0+IHtcbiAgICAgIHRoaXMuY29udGVudC5nb1RvTGluZShOdW1iZXIodG9wUm93KSk7XG4gICAgfSk7XG4gIH1cbn1cblxuZXhwb3J0IG5hbWVzcGFjZSBDU1ZEb2N1bWVudFdpZGdldCB7XG4gIC8vIFRPRE86IEluIFR5cGVTY3JpcHQgMi44LCB3ZSBjYW4gbWFrZSBqdXN0IHRoZSBjb250ZW50IHByb3BlcnR5IG9wdGlvbmFsXG4gIC8vIHVzaW5nIHNvbWV0aGluZyBsaWtlIGh0dHBzOi8vc3RhY2tvdmVyZmxvdy5jb20vYS80Njk0MTgyNCwgaW5zdGVhZCBvZlxuICAvLyBpbmhlcml0aW5nIGZyb20gdGhpcyBJT3B0aW9uc09wdGlvbmFsQ29udGVudC5cblxuICBleHBvcnQgaW50ZXJmYWNlIElPcHRpb25zXG4gICAgZXh0ZW5kcyBEb2N1bWVudFdpZGdldC5JT3B0aW9uc09wdGlvbmFsQ29udGVudDxDU1ZWaWV3ZXI+IHtcbiAgICAvKipcbiAgICAgKiBEYXRhIGRlbGltaXRlciBjaGFyYWN0ZXJcbiAgICAgKi9cbiAgICBkZWxpbWl0ZXI/OiBzdHJpbmc7XG4gIH1cbn1cblxubmFtZXNwYWNlIFByaXZhdGUge1xuICBleHBvcnQgZnVuY3Rpb24gY3JlYXRlQ29udGVudChcbiAgICBjb250ZXh0OiBEb2N1bWVudFJlZ2lzdHJ5LklDb250ZXh0PERvY3VtZW50UmVnaXN0cnkuSU1vZGVsPlxuICApOiBDU1ZWaWV3ZXIge1xuICAgIHJldHVybiBuZXcgQ1NWVmlld2VyKHsgY29udGV4dCB9KTtcbiAgfVxufVxuXG4vKipcbiAqIEEgd2lkZ2V0IGZhY3RvcnkgZm9yIENTViB3aWRnZXRzLlxuICovXG5leHBvcnQgY2xhc3MgQ1NWVmlld2VyRmFjdG9yeSBleHRlbmRzIEFCQ1dpZGdldEZhY3Rvcnk8XG4gIElEb2N1bWVudFdpZGdldDxDU1ZWaWV3ZXI+XG4+IHtcbiAgLyoqXG4gICAqIENyZWF0ZSBhIG5ldyB3aWRnZXQgZ2l2ZW4gYSBjb250ZXh0LlxuICAgKi9cbiAgcHJvdGVjdGVkIGNyZWF0ZU5ld1dpZGdldChcbiAgICBjb250ZXh0OiBEb2N1bWVudFJlZ2lzdHJ5LkNvbnRleHRcbiAgKTogSURvY3VtZW50V2lkZ2V0PENTVlZpZXdlcj4ge1xuICAgIGNvbnN0IHRyYW5zbGF0b3IgPSB0aGlzLnRyYW5zbGF0b3I7XG4gICAgcmV0dXJuIG5ldyBDU1ZEb2N1bWVudFdpZGdldCh7IGNvbnRleHQsIHRyYW5zbGF0b3IgfSk7XG4gIH1cblxuICAvKipcbiAgICogRGVmYXVsdCBmYWN0b3J5IGZvciB0b29sYmFyIGl0ZW1zIHRvIGJlIGFkZGVkIGFmdGVyIHRoZSB3aWRnZXQgaXMgY3JlYXRlZC5cbiAgICovXG4gIHByb3RlY3RlZCBkZWZhdWx0VG9vbGJhckZhY3RvcnkoXG4gICAgd2lkZ2V0OiBJRG9jdW1lbnRXaWRnZXQ8Q1NWVmlld2VyPlxuICApOiBEb2N1bWVudFJlZ2lzdHJ5LklUb29sYmFySXRlbVtdIHtcbiAgICByZXR1cm4gW1xuICAgICAge1xuICAgICAgICBuYW1lOiAnZGVsaW1pdGVyJyxcbiAgICAgICAgd2lkZ2V0OiBuZXcgQ1NWRGVsaW1pdGVyKHtcbiAgICAgICAgICB3aWRnZXQ6IHdpZGdldC5jb250ZW50LFxuICAgICAgICAgIHRyYW5zbGF0b3I6IHRoaXMudHJhbnNsYXRvclxuICAgICAgICB9KVxuICAgICAgfVxuICAgIF07XG4gIH1cbn1cblxuLyoqXG4gKiBBIHdpZGdldCBmYWN0b3J5IGZvciBUU1Ygd2lkZ2V0cy5cbiAqL1xuZXhwb3J0IGNsYXNzIFRTVlZpZXdlckZhY3RvcnkgZXh0ZW5kcyBDU1ZWaWV3ZXJGYWN0b3J5IHtcbiAgLyoqXG4gICAqIENyZWF0ZSBhIG5ldyB3aWRnZXQgZ2l2ZW4gYSBjb250ZXh0LlxuICAgKi9cbiAgcHJvdGVjdGVkIGNyZWF0ZU5ld1dpZGdldChcbiAgICBjb250ZXh0OiBEb2N1bWVudFJlZ2lzdHJ5LkNvbnRleHRcbiAgKTogSURvY3VtZW50V2lkZ2V0PENTVlZpZXdlcj4ge1xuICAgIGNvbnN0IGRlbGltaXRlciA9ICdcXHQnO1xuICAgIHJldHVybiBuZXcgQ1NWRG9jdW1lbnRXaWRnZXQoe1xuICAgICAgY29udGV4dCxcbiAgICAgIGRlbGltaXRlcixcbiAgICAgIHRyYW5zbGF0b3I6IHRoaXMudHJhbnNsYXRvclxuICAgIH0pO1xuICB9XG59XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=