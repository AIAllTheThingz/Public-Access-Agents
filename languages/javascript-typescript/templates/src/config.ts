export interface ApplicationConfig {
  readonly serviceBaseUrl: URL;
  readonly requestTimeoutMs: number;
}

/**
 * Reads and validates process configuration once at application startup.
 *
 * Environment variables are untrusted strings. This function parses and
 * validates them before business modules receive configuration.
 */
export function loadApplicationConfig(
  environment: NodeJS.ProcessEnv = process.env,
): ApplicationConfig {
  const rawServiceBaseUrl = environment["SERVICE_BASE_URL"];
  const rawRequestTimeoutMs = environment["REQUEST_TIMEOUT_MS"] ?? "30000";

  if (rawServiceBaseUrl === undefined || rawServiceBaseUrl.trim() === "") {
    throw new Error("SERVICE_BASE_URL is required.");
  }

  const serviceBaseUrl = new URL(rawServiceBaseUrl);

  if (serviceBaseUrl.protocol !== "https:") {
    throw new Error("SERVICE_BASE_URL must use HTTPS.");
  }

  const requestTimeoutMs = Number.parseInt(rawRequestTimeoutMs, 10);

  if (
    !Number.isInteger(requestTimeoutMs) ||
    requestTimeoutMs < 100 ||
    requestTimeoutMs > 120_000
  ) {
    throw new Error(
      "REQUEST_TIMEOUT_MS must be an integer between 100 and 120000.",
    );
  }

  return Object.freeze({
    serviceBaseUrl,
    requestTimeoutMs,
  });
}
