using Microsoft.AspNetCore.Http.HttpResults;

namespace Example.Project.Api.Endpoints;

/// <summary>
/// Maps example minimal API endpoints.
/// </summary>
public static class ExampleEndpoints
{
    /// <summary>
    /// Maps the example resource endpoints.
    /// </summary>
    public static IEndpointRouteBuilder MapExampleEndpoints(
        this IEndpointRouteBuilder endpoints)
    {
        ArgumentNullException.ThrowIfNull(endpoints);

        RouteGroupBuilder group = endpoints
            .MapGroup("/api/examples")
            .RequireAuthorization()
            .WithTags("Examples");

        group.MapGet("/{identifier}", GetAsync)
            .WithName("GetExample")
            .Produces<ExampleResponse>(StatusCodes.Status200OK)
            .Produces(StatusCodes.Status404NotFound)
            .ProducesProblem(StatusCodes.Status400BadRequest)
            .Produces(StatusCodes.Status401Unauthorized)
            .Produces(StatusCodes.Status403Forbidden);

        return endpoints;
    }

    private static async Task<Results<
        Ok<ExampleResponse>,
        NotFound,
        ProblemHttpResult>> GetAsync(
        string identifier,
        ExampleService service,
        CancellationToken cancellationToken)
    {
        if (string.IsNullOrWhiteSpace(identifier))
        {
            return TypedResults.Problem(
                statusCode: StatusCodes.Status400BadRequest,
                title: "Invalid identifier",
                detail: "The identifier cannot be empty or whitespace.");
        }

        ExampleItem? item = await service.GetAsync(
            identifier,
            cancellationToken);

        if (item is null)
        {
            return TypedResults.NotFound();
        }

        return TypedResults.Ok(new ExampleResponse(
            item.Identifier,
            item.DisplayName));
    }
}

/// <summary>
/// Represents the public endpoint response.
/// </summary>
public sealed record ExampleResponse(
    string Identifier,
    string DisplayName);
