using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace Example.Project.Api.Controllers;

/// <summary>
/// Provides operations for example resources.
/// </summary>
[ApiController]
[Route("api/examples")]
[Authorize]
public sealed class ExamplesController : ControllerBase
{
    private readonly ExampleService _service;

    /// <summary>
    /// Initializes a new instance of the <see cref="ExamplesController"/> class.
    /// </summary>
    public ExamplesController(ExampleService service)
    {
        ArgumentNullException.ThrowIfNull(service);
        _service = service;
    }

    /// <summary>
    /// Retrieves an example resource.
    /// </summary>
    /// <param name="identifier">The stable resource identifier.</param>
    /// <param name="cancellationToken">Cancels the request.</param>
    /// <returns>The matching resource or a safe HTTP error.</returns>
    [HttpGet("{identifier}")]
    [ProducesResponseType<ExampleResponse>(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    [ProducesResponseType<ProblemDetails>(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status401Unauthorized)]
    [ProducesResponseType(StatusCodes.Status403Forbidden)]
    public async Task<ActionResult<ExampleResponse>> GetAsync(
        [FromRoute] string identifier,
        CancellationToken cancellationToken)
    {
        if (string.IsNullOrWhiteSpace(identifier))
        {
            return Problem(
                statusCode: StatusCodes.Status400BadRequest,
                title: "Invalid identifier",
                detail: "The identifier cannot be empty or whitespace.");
        }

        ExampleItem? item = await _service.GetAsync(
            identifier,
            cancellationToken);

        if (item is null)
        {
            return NotFound();
        }

        return Ok(new ExampleResponse(
            item.Identifier,
            item.DisplayName));
    }
}

/// <summary>
/// Represents the public API response.
/// </summary>
public sealed record ExampleResponse(
    string Identifier,
    string DisplayName);
