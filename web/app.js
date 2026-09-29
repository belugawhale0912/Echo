/**
 * Echo frontend - UI logic shared by both pages.
 * Chooses its behaviour from the page it is loaded on (the body's data-page
 * attribute), calls the /api endpoints, renders errors and the expiry
 * countdown, offers the one-time link for copying, and clears the key fragment
 * from the address bar once a secret has been revealed. All cryptography is
 * delegated to ./crypto.js.
 */

