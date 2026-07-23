using System;

namespace Example.CSharp;

/// <summary>
/// Represents a validated sample value used only as a project-adaptation starting point.
/// </summary>
public sealed class SampleValue : IEquatable<SampleValue>
{
    /// <summary>
    /// Initializes a new instance after validating the required value.
    /// </summary>
    /// <param name="value">A nonempty value.</param>
    /// <exception cref="ArgumentException">
    /// Thrown when <paramref name="value"/> is empty or whitespace.
    /// </exception>
    public SampleValue(string value)
    {
        ArgumentException.ThrowIfNullOrWhiteSpace(value);
        Value = value;
    }

    /// <summary>
    /// Gets the validated value.
    /// </summary>
    public string Value { get; }

    /// <inheritdoc />
    public bool Equals(SampleValue? other) =>
        other is not null && StringComparer.Ordinal.Equals(Value, other.Value);

    /// <inheritdoc />
    public override bool Equals(object? obj) => obj is SampleValue other && Equals(other);

    /// <inheritdoc />
    public override int GetHashCode() => StringComparer.Ordinal.GetHashCode(Value);

    /// <inheritdoc />
    public override string ToString() => Value;
}
