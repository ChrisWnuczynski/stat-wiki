// The webR release the site loads, and the one the block check runs.
// The browser loads it from the webR CDN. package.json pins the same release
// for the check, and the tests fail if the two differ.
export const WEBR_VERSION = "0.6.0";
export const WEBR_BASE = `https://webr.r-wasm.org/v${WEBR_VERSION}/`;
