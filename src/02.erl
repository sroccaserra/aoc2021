-module(aoc).
-export([main/1]).
-mode(compile).

-include("common/common.hrl").

solve(Commands) ->
    solve(Commands, 0, 0, 0, 0).

solve([], HPos, Depth1, Depth2, _) ->
    {results, HPos * Depth1, HPos * Depth2};

solve([{command, Direction, Value} | Rest], HPos, Depth1, Depth2, Aim) ->
    case Direction of
        forward -> solve(Rest, HPos+Value, Depth1, Depth2+Aim*Value, Aim);
        up -> solve(Rest, HPos, Depth1-Value, Depth2, Aim-Value);
        down -> solve(Rest, HPos, Depth1+Value, Depth2, Aim+Value)
    end.

parse_command(Line) ->
    [Part1, Part2 | _] = string:tokens(Line, [$\s]),
    {command, list_to_atom(Part1), list_to_integer(Part2)}.

main([Filename]) ->
    Commands = get_parsed_lines(Filename, fun parse_command/1),
    {results, Result1, Result2} = solve(Commands),
    io:fwrite("~w~n~w~n", [Result1, Result2]).
